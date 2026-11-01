"""Data Migration Report of St Brigid's EHR Migration, two pages.

Trial load 3 with the funnel of records, the errors by type and the trend of
the loads.
"""
from content import DOCUMENT, PROJECT
from typesetting import typeset

DESIGN = {
    "accent": "#005eb8",
    "ink": "#212b32",
    "muted": "#4c6272",
    "page": "#ffffff",
    "font": "Liberation Sans",
    "header": "bar",
    "heading": "tint",
    "heading_case": "upper",
    "bullet": "•",
    "body_align": "start",
    "table": "lines",
    "series": ["#005eb8", "#41b6e6", "#00a499", "#768692", "#ae2573"],
    "good": "#007f3b",
    "warn": "#ffb81c",
    "bad": "#da291c",
    "info": "#41b6e6",
    "radius": 2,
    "footer": "St Brigid's University Hospital · Data Migration Report · "
        "OFFICIAL",
}


def twopages():
    return typeset(PROJECT, DOCUMENT, DESIGN, 2)
