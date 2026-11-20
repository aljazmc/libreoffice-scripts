"""Night Audit of Salt & Pine Hotel, two pages.

Landscape. The audit with the revenue by outlet and the exceptions.
"""
from content import BUSINESS, DOCUMENT
from typesetting import typeset

DESIGN = {
    "accent": "#b08d57",
    "ink": "#1f2a36",
    "muted": "#66707a",
    "page": "#ffffff",
    "font": "DejaVu Sans",
    "heading_font": "DejaVu Sans",
    "chart_font": "DejaVu Sans",
    "series": ["#1f3a5f", "#b08d57", "#7a9e9f", "#c97b63", "#cfd8dc"],
    "good": "#5a8f6a",
    "warn": "#d6a64f",
    "bad": "#b5503c",
    "info": "#7a9e9f",
    "radius": 1,
    "orientation": "landscape",
    "header": "rule",
    "heading": "box",
    "heading_case": "upper",
    "table": "grid",
    "density": "compact",
    "body_align": "start",
    "footer": "Salt & Pine · a hotel by the dunes · Night Audit",
}


def twopages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 2)
