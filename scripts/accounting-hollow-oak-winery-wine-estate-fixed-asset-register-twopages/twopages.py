"""Fixed Asset Register of Hollow Oak Estate, two pages.

Landscape. The register by class with the depreciation of the year.
"""
from content import DOCUMENT, BUSINESS
from typesetting import typeset

DESIGN = {
    "accent": "#3f5e3a",
    "ink": "#2a2622",
    "muted": "#6d655c",
    "page": "#fbf8f1",
    "font": "Liberation Sans Narrow",
    "chart_font": "Liberation Sans Narrow",
    "series": ["#3f5e3a", "#8b1e3f", "#c9a227", "#7d8f69", "#cbbfa8"],
    "good": "#5d8a4e",
    "warn": "#c9a227",
    "bad": "#8b1e3f",
    "info": "#5f7f8f",
    "radius": 0,
    "orientation": "landscape",
    "heading_font": "P052",
    "header": "bar",
    "heading": "tint",
    "table": "zebra",
    "density": "compact",
    "body_align": "start",
    "footer": "Hollow Oak Estate Winery · Fixed Asset Register",
}


def twopages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 2)
