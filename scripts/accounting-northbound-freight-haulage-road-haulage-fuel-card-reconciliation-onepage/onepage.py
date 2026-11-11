"""Fuel Card Reconciliation of Northbound Freight, one page.

The month's fuel card statement checked against the vehicles.
"""
from content import DOCUMENT, BUSINESS
from typesetting import typeset

DESIGN = {
    "accent": "#1c1c1c",
    "ink": "#1c1c1c",
    "muted": "#5e5e5e",
    "page": "#fffbea",
    "font": "Liberation Mono",
    "series": ["#1c1c1c", "#f2b705", "#8a8a8a", "#d9480f", "#c9c9c9"],
    "good": "#4c9a2a",
    "warn": "#f2b705",
    "bad": "#d9480f",
    "info": "#3b7ea1",
    "radius": 0,
    "heading_font": "TeX Gyre Heros Cn",
    "chart_font": "TeX Gyre Heros Cn",
    "header": "frame",
    "heading": "box",
    "heading_case": "upper",
    "table": "grid",
    "density": "compact",
    "body_align": "start",
    "footer": "NORTHBOUND FREIGHT LTD · Fuel Card Reconciliation",
}


def onepage():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 1)
