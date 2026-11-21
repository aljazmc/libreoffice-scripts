"""Consent Tracker of Northgate Offshore Wind, two pages.

The consents with their timelines, conditions and owners.
"""
from content import DOCUMENT, PROJECT
from typesetting.project_management import typeset

DESIGN = {
    "accent": "#00707a",
    "ink": "#16302f",
    "muted": "#557071",
    "page": "#f7fbfb",
    "font": "Liberation Sans",
    "heading_font": "TeX Gyre Adventor",
    "header": "rule",
    "heading": "rule",
    "bullet": "›",
    "body_align": "justify",
    "table": "slab",
    "series": ["#00707a", "#f4a259", "#2f4858", "#7cc6c9", "#bcd4d6"],
    "good": "#3a9d5d",
    "warn": "#f4a259",
    "bad": "#c8553d",
    "info": "#4c8db5",
    "radius": 1,
    "footer": "Northgate Offshore Wind · Consent Tracker · Commercial in "
        "confidence",
}


def twopages():
    return typeset(PROJECT, DOCUMENT, DESIGN, 2)
