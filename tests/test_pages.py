"""Every project fills the number of pages its name promises, by the
estimate of its typesetter. Run: python3 -m unittest discover tests

The estimate needs no LibreOffice, so this runs in seconds. It checks the
typesetting, not Writer: a PDF can still come out a page longer if the
estimate is wrong, which only a build shows.
"""
import importlib
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))
PAGES = {"onepage": 1, "twopages": 2, "fourpages": 4, "eightpages": 8}
# what the length scripts pass to typeset() before DOCUMENT
SUBJECTS = ("BUSINESS", "PERSONA", "PROJECT")


def projects():
    return sorted(folder for folder in SCRIPTS.iterdir()
                  if folder.is_dir()
                  and folder.name.rsplit("-", 1)[-1] in PAGES)


def estimate(folder):
    """The pages the project should fill and what its fill() returns."""
    length = folder.name.rsplit("-", 1)[1]
    sys.path.insert(0, str(folder))
    try:
        forget(length)
        script = importlib.import_module(length)
        # the shared typesetter the length script imports typeset() from
        typesetting = sys.modules[script.typeset.__module__]
        subject = next(getattr(script, name) for name in SUBJECTS
                       if hasattr(script, name))
        pages = PAGES[length]
        return pages, typesetting.fill(subject, script.DOCUMENT,
                                       script.DESIGN, pages)
    finally:
        sys.path.pop(0)
        forget(length)


def forget(length):
    """Unload the project's modules and the typesetters, so every project
    starts from a fresh import, as it does under project.sh."""
    for name in list(sys.modules):
        if name in ("content", length) or name.startswith("typesetting"):
            del sys.modules[name]


class PagesTest(unittest.TestCase):

    def test_every_project_fills_its_pages(self):
        for folder in projects():
            with self.subTest(project=folder.name):
                pages, result = estimate(folder)
                if isinstance(result, tuple):
                    # simulated pages: the count and how full the last is
                    count, last = result
                    self.assertEqual(count, pages)
                    self.assertGreater(last, 0)
                else:
                    # a share of all pages: it must reach the last page
                    # without running past it
                    self.assertGreater(result, (pages - 1) / pages)
                    self.assertLessEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
