"""Purchase Order of Hollow Oak Estate, one page.

An order for French oak barrels, priced and approved.
"""
from content import BUSINESS, DOCUMENT
from typesetting.accounting import typeset

DESIGN = {
    "accent": "#3f5e3a",
    "ink": "#2a2622",
    "muted": "#6d655c",
    "page": "#ffffff",
    "font": "Nimbus Sans",
    "chart_font": "Nimbus Sans",
    "series": ["#3f5e3a", "#8b1e3f", "#c9a227", "#7d8f69", "#cbbfa8"],
    "good": "#5d8a4e",
    "warn": "#c9a227",
    "bad": "#8b1e3f",
    "info": "#5f7f8f",
    "radius": 0,
    "heading_font": "P052",
    "header": "band",
    "heading": "plain",
    "table": "zebra",
    "body_align": "start",
    "footer": "Hollow Oak Estate Winery · Purchase Order · Fictional example",
}


def onepage():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 1)
