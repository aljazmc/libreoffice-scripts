"""Utilisation Report of Atelier Nord, two pages.

Utilisation by person, project and week.
"""
from content import BUSINESS, DOCUMENT
from typesetting.accounting import typeset

DESIGN = {
    "accent": "#c08a1e",
    "ink": "#111111",
    "muted": "#6b6b6b",
    "page": "#ffffff",
    "font": "Nimbus Sans",
    "series": ["#111111", "#c08a1e", "#8c8c8c", "#5b7c8d", "#d6d2c4"],
    "good": "#4f7a4a",
    "warn": "#c08a1e",
    "bad": "#a33a2a",
    "info": "#5b7c8d",
    "radius": 0,
    "header": "band",
    "heading": "bar",
    "table": "lines",
    "body_align": "start",
    "footer": "Atelier Nord Architects · Utilisation Report · Fictional example",
}


def twopages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 2)
