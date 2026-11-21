"""Typeset a project management document as a flat ODT document of exactly
the given number of A4 pages: see report.py, which does the work.

A document is the PROJECT and the DOCUMENT of content.py.
"""
from typesetting import report

# project management documents keep the look they were made with: capitals
# 1.22 times wider than prose in every font, and no rows of financial
# statements
FAMILY = {"capitals": 1.22, "statements": False}


def typeset(project, document, design, pages):
    return report.typeset(project, document, {**FAMILY, **design}, pages)


def fill(project, document, design, pages):
    return report.fill(project, document, {**FAMILY, **design}, pages)
