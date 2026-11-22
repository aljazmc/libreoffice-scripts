"""Every project fills the number of pages its name promises: onepage,
twopages, fourpages or eightpages.

Each project gets two tests of its own:

- test_estimate_<project>: the estimate of its typesetter. It needs no
  LibreOffice and takes a fraction of a second, so it runs in CI.
- test_pdf_<project>: the page count of build/<project>.pdf, the document
  Writer really produced. Skipped when the PDF has not been built, or is
  older than the project's scripts.

Run: python3 -m unittest tests.test_pages             # every project
     python3 -m unittest tests.test_pages -k cv-onepage  # some projects
     python3 -m unittest tests.test_pages -k estimate    # estimates only
     python3 -m unittest tests.test_pages -k test_pdf    # built PDFs only

The estimate checks the typesetting, not Writer: a PDF can still come out a
page longer if the estimate is wrong, which only the PDF test shows.
"""
import importlib
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
BUILD = ROOT / "build"
sys.path.insert(0, str(SCRIPTS))
PAGES = {"onepage": 1, "twopages": 2, "fourpages": 4, "eightpages": 8}
WORDS = {1: "one page", 2: "two pages", 4: "four pages", 8: "eight pages"}
# what the length scripts pass to typeset() before DOCUMENT
SUBJECTS = ("BUSINESS", "PERSONA", "PROJECT")
# the page tree's own count; LibreOffice writes it as plain text
PAGE_COUNT = re.compile(rb"/Type\s*/Pages\b[^>]*?/Count\s+(\d+)"
                        rb"|/Count\s+(\d+)[^>]*?/Type\s*/Pages\b")


def projects():
    return sorted(folder for folder in SCRIPTS.iterdir()
                  if folder.is_dir()
                  and folder.name.rsplit("-", 1)[-1] in PAGES)


def promised(folder):
    return PAGES[folder.name.rsplit("-", 1)[1]]


def estimate(folder):
    """What the project's fill() returns for the pages it promises."""
    length = folder.name.rsplit("-", 1)[1]
    sys.path.insert(0, str(folder))
    try:
        forget(length)
        script = importlib.import_module(length)
        # the shared typesetter the length script imports typeset() from
        typesetting = sys.modules[script.typeset.__module__]
        subject = next(getattr(script, name) for name in SUBJECTS
                       if hasattr(script, name))
        return typesetting.fill(subject, script.DOCUMENT, script.DESIGN,
                                promised(folder))
    finally:
        sys.path.pop(0)
        forget(length)


def forget(length):
    """Unload the project's modules and the typesetters, so every project
    starts from a fresh import, as it does under project.sh."""
    for name in list(sys.modules):
        if name in ("content", length) or name.startswith("typesetting"):
            del sys.modules[name]


def pdf_pages(path):
    """The page count of a PDF, read from its page tree."""
    counts = [int(a or b) for a, b in PAGE_COUNT.findall(path.read_bytes())]
    if not counts:
        raise ValueError(f"{path.name}: no page tree found")
    # nested page trees each carry a count; the root holds them all
    return max(counts)


def newest_source(folder):
    """When the project's scripts last changed, typesetters included."""
    files = [*folder.glob("*.py"), *(SCRIPTS / "typesetting").glob("*.py")]
    return max(f.stat().st_mtime for f in files)


class PagesTest(unittest.TestCase):

    def check_estimate(self, folder):
        pages, result = promised(folder), estimate(folder)
        if isinstance(result, tuple):
            # simulated pages: the count and how full the last one is
            count, last = result
            self.assertEqual(count, pages,
                             f"estimated {count} pages, the name promises "
                             f"{pages}")
            self.assertGreater(last, 0, "the last page is empty")
        else:
            # a share of all pages: it must reach the last page without
            # running past it
            self.assertGreater(result, (pages - 1) / pages,
                               f"fills {result:.2f} of {pages} pages, "
                               f"the last page stays empty")
            self.assertLessEqual(result, 1,
                                 f"fills {result:.2f} of {pages} pages, "
                                 f"more than fit")

    def check_pdf(self, folder):
        pdf = BUILD / f"{folder.name}.pdf"
        if not pdf.exists():
            self.skipTest(f"build/{pdf.name} is not built")
        if pdf.stat().st_mtime < newest_source(folder):
            self.skipTest(f"build/{pdf.name} is older than its scripts")
        count, pages = pdf_pages(pdf), promised(folder)
        self.assertEqual(count, pages,
                         f"build/{pdf.name} has {count} pages, the name "
                         f"promises {pages}")


def add_tests():
    """One estimate test and one PDF test per project, named after it, so
    -k can pick projects and the failures name the document."""
    for folder in projects():
        for kind in ("estimate", "pdf"):
            check = getattr(PagesTest, f"check_{kind}")

            def test(self, folder=folder, check=check):
                check(self, folder)

            test.__doc__ = f"{folder.name} fits on {WORDS[promised(folder)]}"
            setattr(PagesTest, f"test_{kind}_{folder.name}", test)


add_tests()


if __name__ == "__main__":
    unittest.main()
