"""Restricted Funds Register of Open Shelf Library Trust, one page.

Every restricted fund, what came in, what was spent and what is left.
"""
from content import BUSINESS, DOCUMENT
from typesetting.accounting import typeset

DESIGN = {
    "accent": "#1d7874",
    "ink": "#22313f",
    "muted": "#5d6d7e",
    "page": "#ffffff",
    "font": "Tuffy",
    "heading_font": "Tuffy",
    "chart_font": "Tuffy",
    "series": ["#1d7874", "#ee6c4d", "#f6c85f", "#679436", "#a7b1bc"],
    "good": "#679436",
    "warn": "#f6c85f",
    "bad": "#ee6c4d",
    "info": "#4f9dc6",
    "radius": 3,
    "header": "bar",
    "heading": "tint",
    "table": "zebra",
    "body_align": "start",
    "footer": "Open Shelf Library Trust · registered charity 1187342 · "
        "Restricted Funds Register",
}


def onepage():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 1)
