"""Annual Operating Budget of Salt & Pine Hotel, four pages.

Landscape. The budget, the drivers, the payroll, the capital plan and the
risks.
"""
from content import BUSINESS, DOCUMENT
from typesetting import typeset

DESIGN = {
    "accent": "#b08d57",
    "ink": "#1f2a36",
    "muted": "#66707a",
    "page": "#fdfbf7",
    "font": "Liberation Sans Narrow",
    "heading_font": "URW Bookman",
    "chart_font": "Liberation Sans Narrow",
    "series": ["#1f3a5f", "#b08d57", "#7a9e9f", "#c97b63", "#cfd8dc"],
    "good": "#5a8f6a",
    "warn": "#d6a64f",
    "bad": "#b5503c",
    "info": "#7a9e9f",
    "radius": 1,
    "orientation": "landscape",
    "header": "bar",
    "heading": "tint",
    "table": "zebra",
    "body_align": "start",
    "footer": "Salt & Pine · a hotel by the dunes · Annual Operating Budget",
}


def fourpages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 4)
