"""Departmental Profit and Loss of Salt & Pine Hotel, two pages.

The departmental statement with the undistributed costs.
"""
from content import DOCUMENT, BUSINESS
from typesetting import typeset

DESIGN = {
    "accent": "#b08d57",
    "ink": "#1f2a36",
    "muted": "#66707a",
    "page": "#fdfbf7",
    "font": "TeX Gyre Termes",
    "heading_font": "URW Bookman",
    "chart_font": "Nimbus Sans",
    "series": ["#1f3a5f", "#b08d57", "#7a9e9f", "#c97b63", "#cfd8dc"],
    "good": "#5a8f6a",
    "warn": "#d6a64f",
    "bad": "#b5503c",
    "info": "#7a9e9f",
    "radius": 1,
    "header": "centered",
    "heading": "center",
    "table": "lines",
    "body_align": "justify",
    "footer": "Salt & Pine · a hotel by the dunes · Departmental Profit and "
        "Loss",
}


def twopages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 2)
