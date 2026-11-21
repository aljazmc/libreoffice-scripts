"""Excise Duty Return of Hollow Oak Estate, four pages.

The return, the bond account, the losses and the year so far.
"""
from content import BUSINESS, DOCUMENT
from typesetting.accounting import typeset

DESIGN = {
    "accent": "#3f5e3a",
    "ink": "#2a2622",
    "muted": "#6d655c",
    "page": "#ffffff",
    "font": "DejaVu Sans",
    "chart_font": "DejaVu Sans",
    "series": ["#3f5e3a", "#8b1e3f", "#c9a227", "#7d8f69", "#cbbfa8"],
    "good": "#5d8a4e",
    "warn": "#c9a227",
    "bad": "#8b1e3f",
    "info": "#5f7f8f",
    "radius": 0,
    "heading_font": "DejaVu Sans",
    "header": "frame",
    "heading": "box",
    "heading_case": "upper",
    "table": "grid",
    "density": "compact",
    "body_align": "start",
    "footer": "Hollow Oak Estate Winery · Excise Duty Return",
}


def fourpages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 4)
