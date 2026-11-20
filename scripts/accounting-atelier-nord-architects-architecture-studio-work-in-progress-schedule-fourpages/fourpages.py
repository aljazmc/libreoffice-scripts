"""Work in Progress Schedule of Atelier Nord, four pages.

Landscape. The schedule, the provisions, the aging and the billing plan.
"""
from content import BUSINESS, DOCUMENT
from typesetting import typeset

DESIGN = {
    "accent": "#c08a1e",
    "ink": "#111111",
    "muted": "#6b6b6b",
    "page": "#ffffff",
    "font": "Liberation Sans Narrow",
    "series": ["#111111", "#c08a1e", "#8c8c8c", "#5b7c8d", "#d6d2c4"],
    "good": "#4f7a4a",
    "warn": "#c08a1e",
    "bad": "#a33a2a",
    "info": "#5b7c8d",
    "radius": 0,
    "orientation": "landscape",
    "heading_font": "Nimbus Sans",
    "header": "bar",
    "heading": "tint",
    "table": "zebra",
    "chart_font": "Liberation Sans Narrow",
    "body_align": "start",
    "footer": "Atelier Nord Architects · Work in Progress Schedule",
}


def fourpages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 4)
