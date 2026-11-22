"""Work Breakdown Structure of FROSTBYTE-1 CubeSat, one page.

The mission broken down to work packages on one page.
"""
from content import DOCUMENT, PROJECT
from typesetting.project_management import typeset

DESIGN = {
    "accent": "#c8102e",
    "ink": "#111111",
    "muted": "#5a5a5a",
    "page": "#ffffff",
    "font": "Liberation Serif",
    "heading_font": "Noto Sans Mono",
    "chart_font": "Liberation Sans Narrow",
    "header": "frame",
    "heading": "box",
    "heading_case": "upper",
    "heading_format": "{number}.0 {title}",
    "bullet": "–",
    "body_align": "justify",
    "table": "grid",
    "title_size": 21,
    "series": ["#111111", "#c8102e", "#7a7a7a", "#3d7ea6", "#bdbdbd"],
    "good": "#2e7d32",
    "warn": "#f9a825",
    "bad": "#c8102e",
    "info": "#3d7ea6",
    "radius": 0,
    "footer": "FROSTBYTE-1 · Work Breakdown Structure · FB1-PM · Rev C · Fictional example",
}


def onepage():
    return typeset(PROJECT, DOCUMENT, DESIGN, 1)
