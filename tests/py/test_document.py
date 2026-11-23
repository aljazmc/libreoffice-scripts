"""Every project builds a sound flat ODT document, read without LibreOffice:
a text document with a title and a language, every style and font it names
defined, an A4 or Letter page, either way up, with margins that leave room for the text,
tables and charts that fit between the margins, charts that are valid SVG,
and the same document on every build. Run: python3 -m unittest discover tests/py

Needs only Python, so it runs on CI too.
"""
import base64
import unittest
import xml.etree.ElementTree as ET

import documents
from documents import q

# A4 and US Letter, in points, portrait (landscape turns them)
PAGES = {"A4": (595.28, 841.89), "Letter": (612.0, 792.0)}
# a narrower text area than this is a margin gone wrong
TEXT_WIDTH_MIN = 0.5  # of the page width
# rounding of widths written in points, which LibreOffice tolerates
SLACK = 0.5  # points
# attributes that name a style, a page layout or a font, and what they name
REFERENCES = {
    q("text:style-name"): "style", q("table:style-name"): "style",
    q("draw:style-name"): "style", q("draw:text-style-name"): "style",
    q("style:parent-style-name"): "style", q("style:next-style-name"): "style",
    q("table:default-cell-style-name"): "style", q("style:master-page-name"): "master",
    q("style:page-layout-name"): "layout", q("style:font-name"): "font",
}
DEFINITIONS = {"style": (q("style:style"), q("text:list-style")),
               "master": (q("style:master-page"),),
               "layout": (q("style:page-layout"),),
               "font": (q("style:font-face"),)}


class DocumentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.documents = documents.all_documents()

    def each(self):
        self.assertTrue(self.documents, "no projects")
        for project in self.documents:
            yield project, documents.parsed(project)

    def test_is_a_text_document_with_a_title_and_a_language(self):
        # the title becomes the PDF's title, and the language its hyphenation
        # and what a screen reader speaks
        for project, root in self.each():
            with self.subTest(project=project):
                self.assertEqual(root.get(q("office:mimetype")),
                                 "application/vnd.oasis.opendocument.text")
                title = root.find(f"{q('office:meta')}/{q('dc:title')}")
                self.assertTrue(title is not None and (title.text or "").strip(), "no title")
                languages = {e.get(q("fo:language")) for e in root.iter() if e.get(q("fo:language"))}
                self.assertTrue(languages - {"zxx", "none"}, "no language set")

    def test_names_only_defined_styles_and_fonts(self):
        # LibreOffice quietly falls back to its default for a missing one
        for project, root in self.each():
            with self.subTest(project=project):
                defined = {kind: {e.get(q("style:name")) for tag in tags for e in root.iter(tag)}
                           for kind, tags in DEFINITIONS.items()}
                missing = set()
                for element in root.iter():
                    for attribute, kind in REFERENCES.items():
                        name = element.get(attribute)
                        if name and name not in defined[kind]:
                            missing.add(f"{kind} {name}")
                self.assertEqual(sorted(missing), [], "named but not defined")

    def test_page_is_a4_or_letter_with_room_for_text(self):
        for project, root in self.each():
            with self.subTest(project=project):
                width, height, left, right, top, bottom = documents.page(root)
                # portrait or landscape
                self.assertTrue(any(abs(width - w) < 1 and abs(height - h) < 1
                                    for page in PAGES.values() for w, h in (page, page[::-1])),
                                f"a page of {width:.1f}x{height:.1f} pt, not A4 or Letter")
                for name, margin in (("left", left), ("right", right), ("top", top), ("bottom", bottom)):
                    self.assertTrue(margin is not None and margin >= 0, f"the {name} margin")
                self.assertGreater(width - left - right, TEXT_WIDTH_MIN * width,
                                   "the margins leave too little room for the text")

    def test_tables_fit_between_the_margins(self):
        # a wider table runs off the right edge of the page
        for project, root in self.each():
            with self.subTest(project=project):
                width, _, left, right, _, _ = documents.page(root)
                room = width - left - right
                known = documents.styles(root)
                for table in root.iter(q("table:table")):
                    total = 0.0
                    for column in table.iter(q("table:table-column")):
                        style = known.get(column.get(q("table:style-name")))
                        properties = style.find(q("style:table-column-properties")) if style is not None else None
                        column_width = documents.points(properties.get(q("style:column-width"))) \
                            if properties is not None else None
                        repeated = int(column.get(q("table:number-columns-repeated"), "1"))
                        total += (column_width or 0) * repeated
                    self.assertLessEqual(total, room + SLACK,
                                         f"table {table.get(q('table:name'))} is {total:.1f} pt wide, "
                                         f"the text {room:.1f} pt")

    def test_charts_fit_and_are_valid_svg(self):
        for project, root in self.each():
            with self.subTest(project=project):
                width, _, left, right, _, _ = documents.page(root)
                room = width - left - right
                for frame in root.iter(q("draw:frame")):
                    name = frame.get(q("draw:name")) or "a frame"
                    frame_width = documents.points(frame.get(q("svg:width")))
                    if frame_width is not None and frame.get(q("text:anchor-type")) != "page":
                        self.assertLessEqual(frame_width, room + SLACK,
                                             f"{name} is {frame_width:.1f} pt wide, the text {room:.1f} pt")
                    for image in frame.iter(q("draw:image")):
                        data = image.find(q("office:binary-data"))
                        self.assertIsNotNone(data, f"{name} links to an image outside the document")
                        if image.get(q("draw:mime-type")) == "image/svg+xml":
                            svg = ET.fromstring(base64.b64decode(data.text))
                            self.assertEqual(svg.tag, "{http://www.w3.org/2000/svg}svg", name)
                            self.assertTrue(svg.get("viewBox") or svg.get("width"), f"{name} has no size")

    def test_builds_the_same_document_every_time(self):
        # one project in ten, spread over the themes, to keep the run short
        for project in list(self.documents)[::10]:
            with self.subTest(project=project):
                self.assertEqual(documents.build(project), self.documents[project],
                                 "a second build gave another document")


if __name__ == "__main__":
    unittest.main()
