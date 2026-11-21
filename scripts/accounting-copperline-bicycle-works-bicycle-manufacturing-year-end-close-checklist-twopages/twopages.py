"""Year-End Close Checklist of Copperline Bicycle Works, two pages.

The checklist by area with owners and dates.
"""
from content import BUSINESS, DOCUMENT
from typesetting.accounting import typeset

DESIGN = {
    "accent": "#c26a2d",
    "ink": "#22262b",
    "muted": "#6a6f75",
    "page": "#ffffff",
    "font": "Liberation Sans",
    "series": ["#22262b", "#c26a2d", "#5a8fa3", "#a3a86b", "#c9ced3"],
    "good": "#5f9e6e",
    "warn": "#d9a03f",
    "bad": "#c0392b",
    "info": "#5a8fa3",
    "radius": 0,
    "heading_font": "Noto Sans Mono",
    "header": "frame",
    "heading": "box",
    "heading_case": "upper",
    "table": "grid",
    "density": "compact",
    "body_align": "start",
    "footer": "Copperline Bicycle Works · Year-End Close Checklist",
}


def twopages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 2)
