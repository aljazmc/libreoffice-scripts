"""Statement of Financial Activities of Open Shelf Library Trust, one page.

Income and spending of the trust for 2026/27 by fund.
"""
from content import BUSINESS, DOCUMENT
from typesetting.accounting import typeset

DESIGN = {
    "accent": "#1d7874",
    "ink": "#22313f",
    "muted": "#5d6d7e",
    "page": "#ffffff",
    "font": "TeX Gyre Schola",
    "heading_font": "TeX Gyre Schola",
    "chart_font": "Liberation Sans",
    "series": ["#1d7874", "#ee6c4d", "#f6c85f", "#679436", "#a7b1bc"],
    "good": "#679436",
    "warn": "#f6c85f",
    "bad": "#ee6c4d",
    "info": "#4f9dc6",
    "radius": 3,
    "header": "rule",
    "heading": "rule",
    "table": "lines",
    "body_align": "justify",
    "footer": "Open Shelf Library Trust · registered charity 1187342 · "
        "Statement of Financial Activities",
}


def onepage():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 1)
