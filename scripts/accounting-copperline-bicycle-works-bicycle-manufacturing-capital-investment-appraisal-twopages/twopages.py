"""Capital Investment Appraisal of Copperline Bicycle Works, two pages.

The appraisal: cash flows, NPV, IRR and payback.
"""
from content import DOCUMENT, BUSINESS
from typesetting import typeset

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
    "footer": "Copperline Bicycle Works · Capital Investment Appraisal",
}


def twopages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 2)
