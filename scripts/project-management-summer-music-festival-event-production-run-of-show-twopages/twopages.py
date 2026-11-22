"""Run of Show of Saltmarsh Sound Festival, two pages.

Landscape. Saturday by stage, with changeovers, curfews and the cues.
"""
from content import DOCUMENT, PROJECT
from typesetting.project_management import typeset

DESIGN = {
    "accent": "#ff3d8b",
    "ink": "#fdf4ff",
    "muted": "#d8b4fe",
    "page": "#1d0b2e",
    "font": "Quicksand",
    "heading_font": "TeX Gyre Adventor",
    "header": "frame",
    "title_case": "upper",
    "heading": "slab",
    "heading_case": "upper",
    "bullet": "✦",
    "body_align": "start",
    "table": "zebra",
    "series": ["#ff3d8b", "#ffd23f", "#3ee0cf", "#a78bfa", "#ff8a3d"],
    "good": "#3ee0cf",
    "warn": "#ffd23f",
    "bad": "#ff5c5c",
    "info": "#a78bfa",
    "grid": "#4a3361",
    "radius": 5,
    "orientation": "landscape",
    "footer": "SALTMARSH SOUND 2027 · Run of Show · Fictional example",
}


def twopages():
    return typeset(PROJECT, DOCUMENT, DESIGN, 2)
