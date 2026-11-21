"""Product Cost Sheet of Copperline Bicycle Works, four pages.

The full bill of materials, routing, overhead rates and price points.
"""
from content import BUSINESS, DOCUMENT
from typesetting.accounting import typeset

DESIGN = {
    "accent": "#c26a2d",
    "ink": "#22262b",
    "muted": "#6a6f75",
    "page": "#ffffff",
    "font": "Liberation Sans Narrow",
    "series": ["#22262b", "#c26a2d", "#5a8fa3", "#a3a86b", "#c9ced3"],
    "good": "#5f9e6e",
    "warn": "#d9a03f",
    "bad": "#c0392b",
    "info": "#5a8fa3",
    "radius": 1,
    "heading_font": "Noto Sans Mono",
    "chart_font": "Liberation Sans Narrow",
    "header": "bar",
    "heading": "tint",
    "heading_case": "upper",
    "table": "zebra",
    "body_align": "start",
    "footer": "Copperline Bicycle Works · Product Cost Sheet",
}


def fourpages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 4)
