"""Capital Investment Appraisal of Copperline Bicycle Works, four pages.

The appraisal, the options, the sensitivities, the risks and the
recommendation.
"""
from content import BUSINESS, DOCUMENT
from typesetting.accounting import typeset

DESIGN = {
    "accent": "#e08a4b",
    "ink": "#eceff1",
    "muted": "#9aa3ab",
    "page": "#1c1f23",
    "font": "Liberation Sans",
    "series": ["#e08a4b", "#7fb3c8", "#c5c97d", "#d96c5f", "#6f7780"],
    "good": "#5f9e6e",
    "warn": "#d9a03f",
    "bad": "#c0392b",
    "info": "#5a8fa3",
    "radius": 1,
    "grid": "#353b42",
    "header": "rule",
    "heading": "bar",
    "table": "lines",
    "body_align": "start",
    "footer": "Copperline Bicycle Works · Capital Investment Appraisal · Fictional example",
}


def fourpages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 4)
