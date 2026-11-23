"""Every export script writes a valid file of its format, checked by what is
inside it: Writer formats keep the document's words (and the PDF the pages
the name promises), office formats carry the right document type, images
come out at the size the script asks for, and drawings carry their format's
signature. Run: python3 -m unittest discover tests/py

By default it exports the projects shown in gallery/; set EXPORTS to a
pattern of projects (fnmatch), or to all. The exports run on a temporary copy
of scripts/, as project.sh runs them, several at a time, so nothing is
written into the repository; about 15 seconds a project. Needs soffice on
the PATH and Pillow; skipped without them, as on CI.
"""
import fnmatch
import gzip
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
import zipfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import documents
from test_pages import PAGES, pdf_pages

SOFFICE = shutil.which("soffice")
# LibreOffice's APNG filter ignores PixelWidth and PixelHeight and writes the
# page at its own resolution; remove the entry when it no longer does
KNOWN = {("apng", "size"): "LibreOffice's APNG filter ignores PixelWidth and PixelHeight"}


def pillow():
    try:
        import PIL  # noqa: F401
        return True
    except ImportError:
        return False


def formats():
    """The FORMATS of project.sh, and odf."""
    text = (documents.ROOT / "project.sh").read_text()
    listed = re.search(r"^FORMATS=\((.*?)^\)", text, re.MULTILINE | re.DOTALL).group(1)
    return listed.split() + ["odf"]


def chosen():
    """The projects to export: EXPORTS, or those shown in gallery/."""
    pattern = os.environ.get("EXPORTS", "")
    if pattern == "all":
        return documents.projects()
    if pattern:
        return [p for p in documents.projects() if fnmatch.fnmatch(p, pattern)]
    shown = {path.name.split(".")[0] for path in (documents.ROOT / "gallery").iterdir()}
    return [p for p in documents.projects() if p in shown]


def output(tmp, project, format):
    if format == "odf":
        return Path(tmp, "odf", project + ".odt")
    extension = f"{format}.xml" if format in ("docbook", "wordxml") else format
    return Path(tmp, "build", f"{project}.{extension}")


def requested_size(format):
    """The PixelWidth and PixelHeight the export script asks for, if any."""
    script = (documents.SCRIPTS / f"export{format}.py").read_text()
    width, height = (re.search(rf"{key}=(\d+)", script) for key in ("PixelWidth", "PixelHeight"))
    return (int(width.group(1)), int(height.group(1))) if width and height else None


def words(root):
    """A few plain words of the document's body, to look for in the exports."""
    found = []
    # from the body: Word formats keep the header and footer elsewhere
    for paragraph in root.find(documents.q("office:body")).iter(documents.q("text:p")):
        for word in re.findall(r"\b[A-Za-z]{6,}\b", documents.visible_text(paragraph)):
            if word not in found:
                found.append(word)
        if len(found) >= 3:
            break
    return found[:3]


def local(tag):
    return tag.rsplit("}", 1)[-1]


class Checks:
    """One method per format: check_<format>(path, context) raises on a bad
    file. context has the project's words, promised pages and the size the
    format's script asks for."""

    def __init__(self, test):
        self.t = test

    def has_words(self, text, context):
        missing = [word for word in context["words"] if word not in text]
        self.t.assertEqual(missing, [], "the document's words are missing")

    # --- Writer formats, which keep the text -------------------------------

    def check_pdf(self, path, context):
        data = path.read_bytes()
        self.t.assertTrue(data.startswith(b"%PDF-1.7"), "a PDF 1.7 header")
        self.t.assertEqual(pdf_pages(path), context["pages"], "the pages the name promises")

    def opendocument(self, path, mimetype, context, part="content.xml"):
        with zipfile.ZipFile(path) as archive:
            self.t.assertIsNone(archive.testzip())
            self.t.assertEqual(archive.namelist()[0], "mimetype", "mimetype comes first")
            self.t.assertEqual(archive.read("mimetype").decode(), mimetype)
            if context is not None:
                self.has_words(archive.read(part).decode(), context)

    def check_odf(self, path, context):
        self.opendocument(path, "application/vnd.oasis.opendocument.text", context)

    def check_ott(self, path, context):
        self.opendocument(path, "application/vnd.oasis.opendocument.text-template", context)

    def check_fodt(self, path, context):
        text = path.read_text()
        root = ET.fromstring(text.encode())
        self.t.assertEqual(root.get(documents.q("office:mimetype")),
                           "application/vnd.oasis.opendocument.text")
        self.has_words(text, context)

    def word(self, path, content_type, context):
        with zipfile.ZipFile(path) as archive:
            self.t.assertIsNone(archive.testzip())
            self.t.assertIn(content_type, archive.read("[Content_Types].xml").decode())
            self.has_words(archive.read("word/document.xml").decode(), context)

    def check_docx(self, path, context):
        self.word(path, "wordprocessingml.document.main+xml", context)

    def check_docm(self, path, context):
        self.word(path, "document.macroEnabled.main+xml", context)

    def check_dotx(self, path, context):
        self.word(path, "wordprocessingml.template.main+xml", context)

    def word97(self, path, context):
        data = path.read_bytes()
        self.t.assertEqual(data[:8], b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1", "an OLE2 compound file")
        for word in context["words"]:
            self.t.assertTrue(word.encode("latin-1") in data or word.encode("utf-16-le") in data,
                              f"the document's word {word!r} is missing")

    def check_doc(self, path, context):
        self.word97(path, context)

    def check_dot(self, path, context):
        self.word97(path, context)

    def check_rtf(self, path, context):
        text = path.read_text(encoding="latin-1")
        self.t.assertTrue(text.startswith("{\\rtf1"))
        self.t.assertTrue(text.rstrip().endswith("}"), "a complete RTF")
        self.has_words(text, context)

    def xml(self, path, tag, context):
        root = ET.parse(path).getroot()
        self.t.assertEqual(local(root.tag), tag)
        self.has_words(ET.tostring(root, encoding="unicode"), context)
        return root

    def check_wordxml(self, path, context):
        self.xml(path, "wordDocument", context)

    def check_docbook(self, path, context):
        self.xml(path, "article", context)

    def check_uot(self, path, context):
        self.xml(path, "UOF", context)

    def check_xhtml(self, path, context):
        self.xml(path, "html", context)

    def check_html(self, path, context):
        text = path.read_text()
        self.t.assertTrue(text.lstrip().lower().startswith("<!doctype html"))
        self.has_words(text, context)
        # EmbedImages: nothing links to a file next to the page
        for source in re.findall(r'<img[^>]+src="([^"]+)"', text):
            self.t.assertTrue(source.startswith("data:"), f"an image outside the page: {source[:40]}")

    def check_txt(self, path, context):
        self.has_words(path.read_text(encoding="utf-8-sig"), context)

    def check_epub(self, path, context):
        with zipfile.ZipFile(path) as archive:
            self.t.assertIsNone(archive.testzip())
            first = archive.infolist()[0]
            self.t.assertEqual((first.filename, first.compress_type), ("mimetype", zipfile.ZIP_STORED),
                               "an uncompressed mimetype first")
            self.t.assertEqual(archive.read("mimetype"), b"application/epub+zip")
            self.t.assertTrue(any(n.endswith(".opf") for n in archive.namelist()), "a package file")
            pages = "".join(archive.read(n).decode() for n in archive.namelist()
                            if n.endswith(".xhtml"))
            self.has_words(pages, context)

    # --- images and drawings, made by Draw from the shapes on the page -----

    def image(self, path, context, kind, format):
        from PIL import Image
        with Image.open(path) as image:
            self.t.assertEqual(image.format, kind)
            if context["size"] and image.size != context["size"]:
                if (format, "size") in KNOWN:
                    self.t.skipTest(f"known: {KNOWN[(format, 'size')]} ({image.size})")
                self.t.assertEqual(image.size, context["size"], "the size the script asks for")
            image.load()

    def check_png(self, path, context):
        self.image(path, context, "PNG", "png")

    def check_apng(self, path, context):
        self.image(path, context, "PNG", "apng")

    def check_jpg(self, path, context):
        self.image(path, context, "JPEG", "jpg")

    def check_gif(self, path, context):
        self.image(path, context, "GIF", "gif")

    def check_bmp(self, path, context):
        self.image(path, context, "BMP", "bmp")

    def check_tif(self, path, context):
        self.image(path, context, "TIFF", "tif")

    def check_webp(self, path, context):
        self.image(path, context, "WEBP", "webp")

    def svg(self, data):
        self.t.assertEqual(local(ET.fromstring(data).tag), "svg")

    def check_svg(self, path, context):
        self.svg(path.read_bytes())

    def check_svgz(self, path, context):
        self.svg(gzip.decompress(path.read_bytes()))

    def check_eps(self, path, context):
        head = path.read_bytes()[:2000]
        self.t.assertTrue(head.startswith(b"%!PS-Adobe-3.0 EPSF"))
        self.t.assertRegex(head, rb"%%BoundingBox: \d+ \d+ \d+ \d+")

    def emf(self, data):
        self.t.assertEqual(data[:4], b"\x01\x00\x00\x00", "an EMF header record")
        self.t.assertEqual(data[40:44], b" EMF", "the EMF signature")

    def check_emf(self, path, context):
        self.emf(path.read_bytes())

    def check_emz(self, path, context):
        self.emf(gzip.decompress(path.read_bytes()))

    def wmf(self, data):
        self.t.assertEqual(data[:4], b"\xd7\xcd\xc6\x9a", "a placeable WMF")

    def check_wmf(self, path, context):
        self.wmf(path.read_bytes())

    def check_wmz(self, path, context):
        self.wmf(gzip.decompress(path.read_bytes()))

    def check_odg(self, path, context):
        self.opendocument(path, "application/vnd.oasis.opendocument.graphics", None)

    def check_otg(self, path, context):
        self.opendocument(path, "application/vnd.oasis.opendocument.graphics-template", None)

    def check_fodg(self, path, context):
        root = ET.parse(path).getroot()
        self.t.assertEqual(root.get(documents.q("office:mimetype")),
                           "application/vnd.oasis.opendocument.graphics")


def export(tmp, project, format):
    """Run one export script on the copy in tmp; returns its error, if any."""
    script = "saveodf.py" if format == "odf" else f"export{format}.py"
    result = subprocess.run(
        [sys.executable, f"scripts/{script}"], cwd=tmp, capture_output=True, text=True,
        timeout=600, env={**os.environ, "PROJECT": project, "PYTHONPATH": "scripts",
                          "PYTHONDONTWRITEBYTECODE": "1"})
    return None if result.returncode == 0 else (result.stdout + result.stderr)[-2000:]


@unittest.skipUnless(SOFFICE and pillow(), "needs soffice and Pillow")
class ExportTest(unittest.TestCase):

    def test_every_format_has_a_check(self):
        missing = [f for f in formats() if not hasattr(Checks, "check_" + f)]
        self.assertEqual(missing, [], "formats without a check in test_exports.py")

    def test_exports_are_valid(self):
        checks = Checks(self)
        projects = chosen()
        self.assertTrue(projects, f"no project matches EXPORTS={os.environ.get('EXPORTS', '')}")
        for project in projects:
            root = documents.parsed(project)
            context = {"words": words(root), "pages": PAGES[project.rsplit("-", 1)[1]]}
            with tempfile.TemporaryDirectory() as tmp:
                shutil.copytree(documents.SCRIPTS, Path(tmp, "scripts"),
                                ignore=shutil.ignore_patterns("__pycache__"))
                with ThreadPoolExecutor(os.cpu_count() or 2) as pool:
                    errors = dict(zip(formats(), pool.map(lambda f: export(tmp, project, f),
                                                          formats())))
                for format in formats():
                    with self.subTest(project=project, format=format):
                        self.assertIsNone(errors[format], errors[format])
                        path = output(tmp, project, format)
                        self.assertTrue(path.is_file(), f"no {path.name}")
                        self.assertGreater(path.stat().st_size, 0, f"{path.name} is empty")
                        getattr(checks, "check_" + format)(
                            path, {**context, "size": requested_size(format)
                                   if format != "odf" else None})


if __name__ == "__main__":
    unittest.main()
