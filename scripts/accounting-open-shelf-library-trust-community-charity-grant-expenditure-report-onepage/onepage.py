"""Grant Expenditure Report of Open Shelf Library Trust, one page.

How the Reading Rooms grant was spent in year two.
"""
from content import BUSINESS, DOCUMENT
from typesetting.accounting import typeset

DESIGN = {
    "accent": "#1d7874",
    "ink": "#22313f",
    "muted": "#5d6d7e",
    "page": "#ffffff",
    "font": "Quicksand",
    "heading_font": "TeX Gyre Adventor",
    "chart_font": "Quicksand",
    "series": ["#1d7874", "#ee6c4d", "#f6c85f", "#679436", "#a7b1bc"],
    "good": "#679436",
    "warn": "#f6c85f",
    "bad": "#ee6c4d",
    "info": "#4f9dc6",
    "radius": 6,
    "header": "band",
    "heading": "slab",
    "table": "lines",
    "body_align": "start",
    "footer": "Open Shelf Library Trust · registered charity 1187342 · Grant "
        "Expenditure Report",
}


def onepage():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 1)
