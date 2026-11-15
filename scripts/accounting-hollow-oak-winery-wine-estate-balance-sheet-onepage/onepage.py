"""Balance Sheet of Hollow Oak Estate, one page.

What the estate owns and owes on 30 June 2027.
"""
from content import DOCUMENT, BUSINESS
from typesetting import typeset

DESIGN = {
    "accent": "#3f5e3a",
    "ink": "#2a2622",
    "muted": "#6d655c",
    "page": "#fbf8f1",
    "font": "P052",
    "chart_font": "P052",
    "series": ["#3f5e3a", "#8b1e3f", "#c9a227", "#7d8f69", "#cbbfa8"],
    "good": "#5d8a4e",
    "warn": "#c9a227",
    "bad": "#8b1e3f",
    "info": "#5f7f8f",
    "radius": 0,
    "header": "centered",
    "heading": "center",
    "heading_format": "{roman}. {title}",
    "table": "lines",
    "body_align": "justify",
    "footer": "Hollow Oak Estate Winery · Balance Sheet",
}


def onepage():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 1)
