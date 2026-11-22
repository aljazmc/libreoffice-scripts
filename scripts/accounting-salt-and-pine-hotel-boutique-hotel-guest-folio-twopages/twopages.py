"""Guest Folio of Salt & Pine Hotel, two pages.

The folio with every charge, night by night.
"""
from content import BUSINESS, DOCUMENT
from typesetting.accounting import typeset

DESIGN = {
    "accent": "#b08d57",
    "ink": "#1f2a36",
    "muted": "#66707a",
    "page": "#ffffff",
    "font": "P052",
    "heading_font": "URW Bookman",
    "chart_font": "Nimbus Sans",
    "series": ["#1f3a5f", "#b08d57", "#7a9e9f", "#c97b63", "#cfd8dc"],
    "good": "#5a8f6a",
    "warn": "#d6a64f",
    "bad": "#b5503c",
    "info": "#7a9e9f",
    "radius": 1,
    "header": "frame",
    "heading": "plain",
    "table": "lines",
    "body_align": "start",
    "margin": 70,
    "footer": "Salt & Pine · a hotel by the dunes · Guest Folio · Fictional example",
}


def twopages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 2)
