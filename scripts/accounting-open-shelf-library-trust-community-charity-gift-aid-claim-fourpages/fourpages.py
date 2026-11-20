"""Gift Aid Claim of Open Shelf Library Trust, four pages.

The claim, the full donor schedule, the declarations check and the history.
"""
from content import BUSINESS, DOCUMENT
from typesetting import typeset

DESIGN = {
    "accent": "#1d7874",
    "ink": "#22313f",
    "muted": "#5d6d7e",
    "page": "#ffffff",
    "font": "DejaVu Sans",
    "heading_font": "DejaVu Sans",
    "chart_font": "Liberation Sans",
    "series": ["#1d7874", "#ee6c4d", "#f6c85f", "#679436", "#a7b1bc"],
    "good": "#679436",
    "warn": "#f6c85f",
    "bad": "#ee6c4d",
    "info": "#4f9dc6",
    "radius": 0,
    "header": "frame",
    "heading": "box",
    "heading_case": "upper",
    "table": "grid",
    "density": "compact",
    "body_align": "start",
    "footer": "Open Shelf Library Trust · registered charity 1187342 · Gift "
        "Aid Claim",
}


def fourpages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 4)
