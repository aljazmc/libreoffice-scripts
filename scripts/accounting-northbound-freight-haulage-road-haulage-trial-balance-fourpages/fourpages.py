"""Trial Balance of Northbound Freight, four pages.

The trial balance, the adjusting journals, the control accounts and the
checks.
"""
from content import BUSINESS, DOCUMENT
from typesetting import typeset

DESIGN = {
    "accent": "#1c1c1c",
    "ink": "#1c1c1c",
    "muted": "#5e5e5e",
    "page": "#ffffff",
    "font": "DejaVu Sans Mono",
    "series": ["#1c1c1c", "#f2b705", "#8a8a8a", "#d9480f", "#c9c9c9"],
    "good": "#4c9a2a",
    "warn": "#f2b705",
    "bad": "#d9480f",
    "info": "#3b7ea1",
    "radius": 0,
    "heading_font": "DejaVu Sans Mono",
    "chart_font": "DejaVu Sans Mono",
    "header": "rule",
    "heading": "plain",
    "heading_format": "[{number}] {title}",
    "table": "lines",
    "density": "compact",
    "body_align": "start",
    "title_size": 20,
    "footer": "NORTHBOUND FREIGHT LTD · Trial Balance",
}


def fourpages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 4)
