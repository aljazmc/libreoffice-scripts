"""Departmental Profit and Loss of Salt & Pine Hotel, four pages.

The statement, each department, the costs, the ratios and the commentary.
"""
from content import BUSINESS, DOCUMENT
from typesetting.accounting import typeset

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
        "Loss · Fictional example",
}


def fourpages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 4)
