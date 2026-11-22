"""Every example document says on every page that it is fictional.

The businesses, people and projects of the example projects are invented,
so the footer of each, which is printed on every page, ends with
"Fictional example". Projects whose name starts with "aljazmc" describe a
real person and must not carry the notice.

Run: python3 -m unittest tests.test_fiction
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_fonts import design
from test_pages import projects

NOTICE = "fictional example"
REAL = "aljazmc"


class FictionTest(unittest.TestCase):

    def test_examples_say_they_are_fictional(self):
        for folder in projects():
            if folder.name.startswith(REAL):
                continue
            with self.subTest(project=folder.name):
                footer = design(folder)[0].get("footer", "")
                self.assertTrue(footer.lower().endswith(NOTICE),
                                f"the footer {footer!r} does not end with "
                                f"the notice")

    def test_real_documents_do_not(self):
        for folder in projects():
            if not folder.name.startswith(REAL):
                continue
            with self.subTest(project=folder.name):
                footer = design(folder)[0].get("footer", "")
                self.assertNotIn(NOTICE, footer.lower())


if __name__ == "__main__":
    unittest.main()
