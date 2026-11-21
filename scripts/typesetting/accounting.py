"""Typeset an accounting document as a flat ODT document of exactly the
given number of A4 pages: see report.py, which does the work.

A document is the BUSINESS and the DOCUMENT of content.py. Its tables can
have the rows of financial statements (sections, subtotals and totals).
"""
from typesetting import report


def typeset(business, document, design, pages):
    return report.typeset(business, document, design, pages)


def fill(business, document, design, pages):
    return report.fill(business, document, design, pages)
