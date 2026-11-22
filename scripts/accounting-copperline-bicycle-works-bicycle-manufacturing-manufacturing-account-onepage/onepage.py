"""Manufacturing Account of Copperline Bicycle Works, one page.

The cost of the bicycles made in 2027, from raw steel to finished frame.
"""
from content import BUSINESS, DOCUMENT
from typesetting.accounting import typeset

DESIGN = {
    "accent": "#c26a2d",
    "ink": "#22262b",
    "muted": "#6a6f75",
    "page": "#ffffff",
    "font": "C059",
    "series": ["#22262b", "#c26a2d", "#5a8fa3", "#a3a86b", "#c9ced3"],
    "good": "#5f9e6e",
    "warn": "#d9a03f",
    "bad": "#c0392b",
    "info": "#5a8fa3",
    "radius": 1,
    "heading_font": "C059",
    "chart_font": "Liberation Sans",
    "header": "rule",
    "heading": "rule",
    "table": "lines",
    "body_align": "justify",
    "footer": "Copperline Bicycle Works · Manufacturing Account · Fictional example",
}


def onepage():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 1)
