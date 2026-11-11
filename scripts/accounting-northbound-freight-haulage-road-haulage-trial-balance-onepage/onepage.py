"""Trial Balance of Northbound Freight, one page.

Every account in the ledger at the year end, debits and credits.
"""
from content import DOCUMENT, BUSINESS
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


def onepage():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 1)
