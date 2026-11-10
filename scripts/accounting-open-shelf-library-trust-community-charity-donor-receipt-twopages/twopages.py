"""Donation Receipt of Open Shelf Library Trust, two pages.

The receipt with every gift and what it paid for.
"""
from content import DOCUMENT, BUSINESS
from typesetting import typeset

DESIGN = {
    "accent": "#1d7874",
    "ink": "#22313f",
    "muted": "#5d6d7e",
    "page": "#fffaf2",
    "font": "URW Bookman",
    "heading_font": "URW Bookman",
    "chart_font": "URW Bookman",
    "series": ["#1d7874", "#ee6c4d", "#f6c85f", "#679436", "#a7b1bc"],
    "good": "#679436",
    "warn": "#f6c85f",
    "bad": "#ee6c4d",
    "info": "#4f9dc6",
    "radius": 3,
    "header": "centered",
    "heading": "plain",
    "table": "lines",
    "body_align": "justify",
    "margin": 76,
    "title_size": 22,
    "footer": "Open Shelf Library Trust · registered charity 1187342 · "
        "Donation Receipt",
}


def twopages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 2)
