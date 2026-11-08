"""RevPAR Performance of Salt & Pine Hotel, one page.

Occupancy, rate and revenue per room against the competitors.
"""
from content import DOCUMENT, BUSINESS
from typesetting import typeset

DESIGN = {
    "accent": "#d4b37a",
    "ink": "#f1ece2",
    "muted": "#aab4c3",
    "page": "#13233a",
    "font": "TeX Gyre Termes",
    "heading_font": "URW Bookman",
    "chart_font": "Nimbus Sans",
    "series": ["#d4b37a", "#7fb7be", "#e08e6d", "#a3c4a8", "#6c7a8c"],
    "good": "#5a8f6a",
    "warn": "#d6a64f",
    "bad": "#b5503c",
    "info": "#7a9e9f",
    "radius": 1,
    "grid": "#2c3e57",
    "header": "rule",
    "heading": "rule",
    "table": "lines",
    "body_align": "start",
    "footer": "Salt & Pine · a hotel by the dunes · RevPAR Performance",
}


def onepage():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 1)
