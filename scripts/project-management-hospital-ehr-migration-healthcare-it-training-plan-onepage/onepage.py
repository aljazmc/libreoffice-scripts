"""Training Plan of St Brigid's EHR Migration, one page.

Who is trained by when: the staff trained per week against the target.
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
    "footer": "St Brigid's University Hospital · Training Plan · OFFICIAL",
}


def onepage():
    return typeset(PROJECT, DOCUMENT, DESIGN, 1)
