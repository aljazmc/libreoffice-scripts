"""The fonts of the projects: known to the typesetters, installed, and
really used in the PDFs.

The typesetters estimate line wrapping from each font's average character
width, so a font they do not know breaks the page count, and a font
LibreOffice cannot find is replaced by another with other widths.

- FontTablesTest: the width tables of the typesetters agree, and their
  values are plausible.
- test_design_<project>: every font the project's DESIGN names is in the
  width table of its typesetter. Needs nothing but Python.
- FontsInstalledTest: every font of the width tables is installed, by
  fontconfig. Skipped where fc-list is missing and on CI, whose runners
  do not have the fonts.
- test_pdf_fonts_<project>: build/<project>.pdf embeds the body and the
  heading font of the DESIGN, and not a replacement. Skipped when the PDF
  is not built or older than the project's scripts, and without pdffonts
  (poppler-utils) and fc-list.

Run: python3 -m unittest discover tests/py -p test_fonts.py                 # everything
     python3 -m unittest discover tests/py -p test_fonts.py -k design       # the designs only
     python3 -m unittest discover tests/py -p test_fonts.py -k cv-onepage   # some projects
"""
import functools
import importlib
import os
import re
import shutil
import subprocess
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_pages import BUILD, PAGES, SCRIPTS, forget, newest_source, projects

from typesetting import job_hunting, report

README = SCRIPTS.parent / "README.md"
# the keys of a DESIGN that name a font
FONT_KEYS = ("font", "heading_font", "chart_font", "chart_heading_font")
# how the README's license section names each font, by the start of its
# family name
LICENSED = {"Lato": "Lato", "Liberation": "Liberation", "TeX Gyre": "TeX Gyre",
            "DejaVu": "DejaVu", "Quicksand": "Quicksand", "Noto": "Noto",
            "Tuffy": "Tuffy", "C059": "URW base 35", "P052": "URW base 35",
            "Nimbus": "URW base 35", "URW": "URW base 35"}


def design(folder):
    """The project's DESIGN, with the defaults its typesetter adds, and the
    width table of that typesetter."""
    length = folder.name.rsplit("-", 1)[1]
    sys.path.insert(0, str(folder))
    try:
        forget(length)
        script = importlib.import_module(length)
        family = sys.modules[script.typeset.__module__]
        fonts = job_hunting.FONTS if family.__name__.endswith(
            "job_hunting") else report.FONTS
        return {**getattr(family, "FAMILY", {}), **script.DESIGN}, fonts
    finally:
        sys.path.pop(0)
        forget(length)


@functools.cache
def postscript_names(family):
    """The PostScript family names fontconfig gives a font, e.g.
    TeXGyreHerosCondensed for TeX Gyre Heros Cn, without the style."""
    out = subprocess.run(["fc-list", f":family={family}", "postscriptname"],
                         capture_output=True, text=True, check=True).stdout
    return {line.split("=", 1)[1].split("-")[0]
            for line in out.splitlines() if "=" in line}


def embedded(pdf):
    """The PostScript family names of the fonts embedded in a PDF."""
    out = subprocess.run(["pdffonts", str(pdf)], capture_output=True,
                         text=True, check=True).stdout.splitlines()[2:]
    # a subset is named ABCDEF+Name-Style
    return {re.sub(r"^[A-Z]{6}\+", "", line.split()[0]).split("-")[0]
            for line in out if line.strip()}


class FontTablesTest(unittest.TestCase):

    def test_tables_agree(self):
        for font, widths in job_hunting.FONTS.items():
            with self.subTest(font=font):
                self.assertEqual(report.FONTS.get(font), widths,
                                 "job_hunting.py and report.py differ")

    def test_widths_are_plausible(self):
        for font, (regular, bold) in report.FONTS.items():
            with self.subTest(font=font):
                # average advances of prose, in ems
                self.assertTrue(0.3 < regular < 0.7, regular)
                self.assertTrue(0.3 < bold < 0.7, bold)
                self.assertGreaterEqual(bold, regular)

    def test_monospaced_fonts(self):
        for font in report.MONOSPACED:
            with self.subTest(font=font):
                regular, bold = report.FONTS[font]
                self.assertAlmostEqual(regular, 0.6, delta=0.01)
                self.assertEqual(regular, bold)

    def test_capitals_name_known_fonts(self):
        for font, scale in report.CAPITALS.items():
            with self.subTest(font=font):
                self.assertIn(font, report.FONTS)
                self.assertTrue(1 < scale < 1.6, scale)

    def test_readme_names_every_license(self):
        # the license section wraps its lines; compare words, not lines
        text = " ".join(README.read_text().split())
        for font in report.FONTS:
            with self.subTest(font=font):
                name = next((v for k, v in LICENSED.items()
                             if font.startswith(k)), None)
                self.assertIsNotNone(name, "no license known for this font")
                self.assertTrue(name in text,
                                f"the README names no license for {name}")


class FontsInstalledTest(unittest.TestCase):

    def test_every_font_is_installed(self):
        if not shutil.which("fc-list"):
            self.skipTest("fc-list (fontconfig) is not installed")
        if os.environ.get("CI"):
            self.skipTest("the CI runners do not have the fonts")
        for font in report.FONTS:
            with self.subTest(font=font):
                self.assertTrue(postscript_names(font),
                                f"{font} is not installed")


class ProjectFontsTest(unittest.TestCase):

    def check_design(self, folder):
        settings, fonts = design(folder)
        for key in FONT_KEYS:
            if key in settings:
                self.assertIn(settings[key], fonts,
                              f"{key} {settings[key]!r} has no width in "
                              f"its typesetter")

    def check_pdf_fonts(self, folder):
        pdf = BUILD / f"{folder.name}.pdf"
        if not shutil.which("pdffonts") or not shutil.which("fc-list"):
            self.skipTest("needs pdffonts (poppler-utils) and fc-list")
        if not pdf.exists():
            self.skipTest(f"build/{pdf.name} is not built")
        if pdf.stat().st_mtime < newest_source(folder):
            self.skipTest(f"build/{pdf.name} is older than its scripts")
        settings, _ = design(folder)
        names = embedded(pdf)
        for key in ("font", "heading_font"):
            if key not in settings:
                continue
            font = settings[key]
            wanted = postscript_names(font)
            self.assertTrue(wanted, f"{font} is not installed")
            self.assertTrue(names & wanted,
                            f"{key} {font!r} is not in build/{pdf.name}, "
                            f"which embeds {', '.join(sorted(names))}; "
                            f"rebuild it where the font is installed")


def add_tests():
    """A design test and a PDF test per project, named after it."""
    for folder in projects():
        if folder.name.rsplit("-", 1)[1] not in PAGES:
            continue
        for kind in ("design", "pdf_fonts"):
            check = getattr(ProjectFontsTest, f"check_{kind}")

            def test(self, folder=folder, check=check):
                check(self, folder)

            test.__doc__ = f"{folder.name}: {kind.replace('_', ' ')}"
            setattr(ProjectFontsTest, f"test_{kind}_{folder.name}", test)


add_tests()


if __name__ == "__main__":
    unittest.main()
