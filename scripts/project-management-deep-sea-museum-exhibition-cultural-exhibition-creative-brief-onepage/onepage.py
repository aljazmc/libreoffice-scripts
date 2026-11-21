"""Creative Brief of The Abyss: Life Below Light, one page.

The exhibition in a page: the idea, the audience, the journey and the tone.
"""
from content import DOCUMENT, PROJECT
from typesetting.project_management import typeset

DESIGN = {
    "accent": "#7a1f3d",
    "ink": "#2b2320",
    "muted": "#6e5f58",
    "page": "#fbf7f0",
    "font": "TeX Gyre Pagella",
    "chart_font": "TeX Gyre Pagella",
    "header": "centered",
    "heading": "center",
    "heading_format": "{roman}. {title}",
    "bullet": "–",
    "body_align": "justify",
    "table": "lines",
    "series": ["#7a1f3d", "#c9a227", "#2f5d62", "#a7727d", "#d8c3a5"],
    "good": "#5b8c5a",
    "warn": "#c9a227",
    "bad": "#a4343a",
    "info": "#2f5d62",
    "radius": 0,
    "subtitle_italic": True,
    "footer": "The Abyss · Creative Brief · Museum of the North Sea",
}


def onepage():
    return typeset(PROJECT, DOCUMENT, DESIGN, 1)
