import importlib
import io
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

OFFICE = "urn:oasis:names:tc:opendocument:xmlns:office:1.0"
STYLE = "urn:oasis:names:tc:opendocument:xmlns:style:1.0"
TEXT = "urn:oasis:names:tc:opendocument:xmlns:text:1.0"
DRAW = "urn:oasis:names:tc:opendocument:xmlns:drawing:1.0"

GRAPHICS = "application/vnd.oasis.opendocument.graphics"

scripts_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(scripts_dir)


def load_project(target):
    """Build the flat ODT document of the project named by the PROJECT
    environment variable and return it with the output path (without
    extension) inside the root-level target directory.

    A project scripts/<theme>-<name>/ must provide <name>.py with a <name>()
    function returning the flat ODT (.fodt) document as a string, e.g.
    scripts/cyberpunk-butterfly00/butterfly00.py:butterfly00().
    """
    project = os.environ.get("PROJECT")
    if not project:
        sys.exit("usage: PROJECT=<project> PYTHONPATH=scripts "
                 "python3 <script>")

    project_dir = os.path.join(scripts_dir, project)
    if not os.path.isdir(project_dir):
        sys.exit(f"project not found: {project_dir}")

    name = project.rsplit("-", 1)[-1]
    sys.path.insert(0, project_dir)
    document = getattr(importlib.import_module(name), name)()

    target_dir = os.path.join(root_dir, target)
    os.makedirs(target_dir, exist_ok=True)

    return document, os.path.join(target_dir, project)


def drawing(document):
    """Move the page-anchored shapes of the flat ODT document onto the page
    of a flat ODG document, so LibreOffice Draw converts it instead of
    Writer. The styles and the page layout stay as they are.
    """
    for _, (prefix, uri) in ET.iterparse(io.BytesIO(document.encode()),
                                         events=["start-ns"]):
        ET.register_namespace(prefix, uri)

    root = ET.fromstring(document)
    root.set(f"{{{OFFICE}}}mimetype", GRAPHICS)
    master = root.find(f"{{{OFFICE}}}master-styles/{{{STYLE}}}master-page")
    body = root.find(f"{{{OFFICE}}}body")
    text = body.find(f"{{{OFFICE}}}text")
    body.remove(text)

    page = ET.SubElement(ET.SubElement(body, f"{{{OFFICE}}}drawing"),
                         f"{{{DRAW}}}page",
                         {f"{{{DRAW}}}name": "page1",
                          f"{{{DRAW}}}master-page-name":
                              master.get(f"{{{STYLE}}}name")})
    for shape in text:
        if shape.tag.startswith(f"{{{DRAW}}}"):
            shape.attrib.pop(f"{{{TEXT}}}anchor-type", None)
            shape.attrib.pop(f"{{{TEXT}}}anchor-page-number", None)
            page.append(shape)

    return ET.tostring(root, encoding="unicode", xml_declaration=True)


def filter_data(settings):
    """Encode filter settings as the JSON that --convert-to accepts."""
    data = {}
    for key, value in settings.items():
        if isinstance(value, bool):
            data[key] = {"type": "boolean", "value": str(value).lower()}
        elif isinstance(value, int):
            data[key] = {"type": "long", "value": str(value)}
        else:
            data[key] = {"type": "string", "value": str(value)}
    return json.dumps(data, separators=(",", ":"))


def export(document, filepath, filter_name, options=None, **settings):
    """Run a LibreOffice conversion non-interactively.

    The document is a flat ODT, which Writer converts, or a flat ODG made
    by drawing(), which Draw converts, so filter_name must be an export
    filter of that application, e.g. "writer_pdf_Export" or
    "draw_svg_Export". options is the filter's option string, e.g. "UTF8"
    for "Text (encoded)". Keyword arguments are filter settings, e.g.
    PixelWidth=1920, and replace options.
    """
    if ET.fromstring(document).get(f"{{{OFFICE}}}mimetype") == GRAPHICS:
        suffix, infilter = ".fodg", "OpenDocument Drawing Flat XML"
    else:
        suffix, infilter = ".fodt", "OpenDocument Text Flat XML"
    if settings:
        options = filter_data(settings)

    # the output gets the source name and the last extension of the target
    extension = os.path.splitext(filepath)[1][1:]
    target = f"{extension}:{filter_name}" + (f":{options}" if options else "")

    if os.path.exists(filepath):
        os.remove(filepath)

    with tempfile.TemporaryDirectory() as tmp:
        source = os.path.join(tmp, "document" + suffix)
        outdir = os.path.join(tmp, "out")
        with open(source, "w", encoding="utf-8") as file:
            file.write(document)

        # a profile of its own keeps a running LibreOffice out of it, and
        # the input filter keeps the type detection from opening flat ODG
        # documents in Writer
        profile = pathlib.Path(tmp, "profile").as_uri()
        args = ["soffice", f"-env:UserInstallation={profile}", "--headless",
                "--norestore", f"--infilter={infilter}", "--convert-to",
                target, "--outdir", outdir, source]

        # soffice exits with 0 even when a conversion fails, so check the file
        result = subprocess.run(args, capture_output=True)
        converted = os.path.join(outdir, "document." + extension)
        if result.returncode != 0 or not os.path.isfile(converted):
            sys.exit(f"libreoffice export failed for {filepath}:\n"
                     + result.stdout.decode(errors="replace")
                     + result.stderr.decode(errors="replace"))
        shutil.move(converted, filepath)
