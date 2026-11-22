"""Loan Amortisation Schedule of Northbound Freight, two pages.

Landscape. The schedule, the split of interest and capital and the balance.
"""
from content import BUSINESS, DOCUMENT
from typesetting.accounting import typeset

DESIGN = {
    "accent": "#2b2b2b",
    "ink": "#1c1c1c",
    "muted": "#5e5e5e",
    "page": "#ffffff",
    "font": "Liberation Sans Narrow",
    "series": ["#1c1c1c", "#f2b705", "#8a8a8a", "#d9480f", "#c9c9c9"],
    "good": "#4c9a2a",
    "warn": "#f2b705",
    "bad": "#d9480f",
    "info": "#3b7ea1",
    "radius": 0,
    "orientation": "landscape",
    "heading_font": "TeX Gyre Heros Cn",
    "chart_font": "Liberation Sans Narrow",
    "header": "bar",
    "heading": "tint",
    "table": "zebra",
    "body_align": "start",
    "footer": "NORTHBOUND FREIGHT LTD · Loan Amortisation Schedule · Fictional example",
}


def twopages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 2)
