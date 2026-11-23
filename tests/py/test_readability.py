"""Every document can be read: its text stands out from what it is printed on,
is big enough to read on paper, and holds no leftovers of the Python that
wrote it (an unfilled {placeholder}, None, nan) or of a template (TODO,
lorem ipsum). Run: python3 -m unittest discover tests/py

Read from the flat ODT, without LibreOffice, so it runs on CI too.
"""
import re
import unittest

import documents
from documents import q

# contrast ratio of text and background, as WCAG 2 defines it: 21 is black on
# white, 1 is no contrast at all. WCAG AA asks 4.5 for body text and 3 for
# large text; many of the designs use muted or pale accents below that, so
# this only catches text that can't be read at all, such as ink on ink
CONTRAST_MIN = 2.0
# the smallest text that stays readable on paper
SIZE_MIN = 6.0  # points
LEFTOVERS = re.compile(r"\{[A-Za-z_][\w.]*\}|\bTODO\b|\bFIXME\b|lorem ipsum", re.IGNORECASE)
# a whole paragraph or cell reading like a Python value that wasn't formatted
VALUES = {"None", "nan", "NaN", "inf", "-inf", "[]", "{}", "()"}
TEXT = (q("text:p"), q("text:h"), q("text:span"))


def luminance(color):
    def channel(value):
        value /= 255
        return value / 12.92 if value <= 0.03928 else ((value + 0.055) / 1.055) ** 2.4
    red, green, blue = (int(color[i:i + 2], 16) for i in (1, 3, 5))
    return 0.2126 * channel(red) + 0.7152 * channel(green) + 0.0722 * channel(blue)


def contrast(a, b):
    light, dark = sorted((luminance(a), luminance(b)), reverse=True)
    return (light + 0.05) / (dark + 0.05)


def solid(color):
    return color if color and re.fullmatch(r"#[0-9a-fA-F]{6}", color) else None


class Styles:
    """Looks up a property of a style, through its parents and the default
    style of its family."""

    def __init__(self, root):
        self.styles = documents.styles(root)
        self.defaults = {s.get(q("style:family")): s for s in root.iter(q("style:default-style"))}

    def get(self, name, properties, attribute):
        seen = set()
        style = self.styles.get(name)
        while style is not None and name not in seen:
            seen.add(name)
            found = style.find(properties)
            if found is not None and found.get(attribute):
                return found.get(attribute)
            name = style.get(q("style:parent-style-name"))
            family = style.get(q("style:family"))
            style = self.styles.get(name) if name else self.defaults.get(family)
        return None


def runs(root):
    """(text, color, background, size) of every piece of text in the body,
    the header and the footer, with what it inherits from its paragraph,
    table cell and page."""
    styles = Styles(root)
    layout = root.find(f".//{q('style:page-layout-properties')}")
    page = solid(layout.get(q("fo:background-color"))) or "#ffffff"
    default = styles.defaults.get("paragraph")
    default_text = default.find(q("style:text-properties")) if default is not None else None
    color = solid(default_text.get(q("fo:color"))) if default_text is not None else None
    size = default_text.get(q("fo:font-size")) if default_text is not None else None

    def walk(element, color, background, size):
        name = element.get(q("text:style-name")) or element.get(q("table:style-name"))
        if name:
            background = solid(styles.get(name, q("style:table-cell-properties"), q("fo:background-color"))) \
                or solid(styles.get(name, q("style:paragraph-properties"), q("fo:background-color"))) \
                or background
            color = solid(styles.get(name, q("style:text-properties"), q("fo:color"))) or color
            size = styles.get(name, q("style:text-properties"), q("fo:font-size")) or size
        if element.tag in TEXT:
            # the text of this element itself, not of its spans
            own = (element.text or "") + "".join(child.tail or "" for child in element)
            if own.strip():
                yield own.strip(), color or "#000000", background, size
        for child in element:
            yield from walk(child, color, background, size)

    for part in (root.find(q("office:body")), *root.iter(q("style:header")),
                 *root.iter(q("style:footer"))):
        if part is not None:
            yield from walk(part, color, page, size)


class ReadabilityTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.runs = {project: list(runs(documents.parsed(project)))
                    for project in documents.all_documents()}

    def test_text_stands_out_from_its_background(self):
        self.assertTrue(self.runs, "no projects")
        for project, found in self.runs.items():
            with self.subTest(project=project):
                worst = min(((contrast(color, background), text, color, background)
                             for text, color, background, _ in found), default=None)
                self.assertIsNotNone(worst, "no text")
                ratio, text, color, background = worst
                self.assertGreaterEqual(ratio, CONTRAST_MIN,
                                        f"{text[:40]!r}: {color} on {background}, "
                                        f"contrast {ratio:.2f}:1")

    def test_text_is_big_enough(self):
        for project, found in self.runs.items():
            with self.subTest(project=project):
                small = sorted({(documents.points(size), text[:30]) for text, _, _, size in found
                                if size and documents.points(size) is not None
                                and documents.points(size) < SIZE_MIN})
                self.assertEqual(small, [], f"text below {SIZE_MIN} pt")

    def test_no_leftovers(self):
        for project, found in self.runs.items():
            with self.subTest(project=project):
                leftovers = sorted({text[:60] for text, _, _, _ in found
                                    if LEFTOVERS.search(text) or text in VALUES})
                self.assertEqual(leftovers, [], "placeholders, unformatted values or notes")


if __name__ == "__main__":
    unittest.main()
