"""Harvest Cost Allocation of Hollow Oak Estate, two pages.

The costs of the vintage, how they are shared and the cost per bottle.
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
    "header": "bar",
    "heading": "rule",
    "table": "lines",
    "body_align": "justify",
    "footer": "Hollow Oak Estate Winery · Harvest Cost Allocation",
}


def twopages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 2)
