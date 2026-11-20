"""Donation Receipt of Open Shelf Library Trust, one page.

A receipt and thank-you for a donor's gifts in 2026/27.
"""
from content import BUSINESS, DOCUMENT
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


def onepage():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 1)
