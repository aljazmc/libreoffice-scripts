"""Helpers for the tests of the documents: the projects, their flat ODT
documents and the ODF namespaces.

A project is built in its own Python process, as project.sh runs it, with its
output directory in a temporary folder, so nothing is written into the
repository. All documents are built once per test run, several at a time.
Not a test itself.
"""
import functools
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"

NS = {
    "office": "urn:oasis:names:tc:opendocument:xmlns:office:1.0",
    "style": "urn:oasis:names:tc:opendocument:xmlns:style:1.0",
    "text": "urn:oasis:names:tc:opendocument:xmlns:text:1.0",
    "table": "urn:oasis:names:tc:opendocument:xmlns:table:1.0",
    "draw": "urn:oasis:names:tc:opendocument:xmlns:drawing:1.0",
    "fo": "urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0",
    "svg": "urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0",
    "dc": "http://purl.org/dc/elements/1.1/",
    "xlink": "http://www.w3.org/1999/xlink",
}

BUILD = """
import sys, tempfile
sys.path.insert(0, sys.argv[1])
from common import load_project
document, _ = load_project(tempfile.mkdtemp())
sys.stdout.write(document)
"""

UNITS = {"pt": 1, "cm": 72 / 2.54, "mm": 72 / 25.4, "in": 72, "px": 0.75, "pc": 12}


def q(name):
    """"fo:color" -> "{urn:...xsl-fo-compatible:1.0}color", for ElementTree."""
    prefix, local = name.split(":")
    return f"{{{NS[prefix]}}}{local}"


def points(value):
    """A length such as "12pt", "2.5cm" or "0.5in" in points, or None."""
    match = re.fullmatch(r"(-?\d+(?:\.\d+)?)(pt|cm|mm|in|px|pc)", (value or "").strip())
    return float(match.group(1)) * UNITS[match.group(2)] if match else None


def projects():
    """The projects, as project.sh lists them: folders of scripts/ holding
    <name>.py, apart from the shared typesetters."""
    return sorted(folder.name for folder in SCRIPTS.iterdir()
                  if folder.is_dir() and folder.name != "typesetting"
                  and (folder / (folder.name.rsplit("-", 1)[-1] + ".py")).is_file())


def build(project):
    """The project's flat ODT document, as a string, built afresh."""
    result = subprocess.run(
        [sys.executable, "-c", BUILD, str(SCRIPTS)],
        capture_output=True, text=True, cwd=ROOT,
        env={**os.environ, "PROJECT": project, "PYTHONDONTWRITEBYTECODE": "1"},
    )
    if result.returncode != 0:
        raise AssertionError(f"{project} failed to build:\n{result.stderr[-3000:]}")
    return result.stdout


@functools.cache
def all_documents():
    """{project: document} of every project, built once per test run."""
    with ThreadPoolExecutor(os.cpu_count() or 2) as pool:
        return dict(zip(projects(), pool.map(build, projects())))


@functools.cache
def parsed(project):
    return ET.fromstring(all_documents()[project])


def page(root):
    """(width, height, left, right, top, bottom) of the page layout, in points."""
    properties = root.find(f".//{q('style:page-layout-properties')}")
    return tuple(points(properties.get(q("fo:" + key))) for key in
                 ("page-width", "page-height", "margin-left", "margin-right",
                  "margin-top", "margin-bottom"))


def styles(root):
    """{name: style element} of the document's styles."""
    return {s.get(q("style:name")): s for s in root.iter(q("style:style"))}


def visible_text(element):
    """The text inside an element, as it reads."""
    return "".join(element.itertext())


if __name__ == "__main__":
    sys.exit("a helper for the tests, not a test")
