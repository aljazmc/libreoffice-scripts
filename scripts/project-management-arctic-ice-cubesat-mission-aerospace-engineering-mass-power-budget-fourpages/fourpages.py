"""Mass and Power Budget of FROSTBYTE-1 CubeSat, four pages.

The budgets in full: mass, power by mode, the orbit energy balance, margins
and the trend.
"""
from content import DOCUMENT, PROJECT
from typesetting import typeset

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
    "footer": "FROSTBYTE-1 · Mass and Power Budget · FB1-PM · Rev C",
}


def fourpages():
    return typeset(PROJECT, DOCUMENT, DESIGN, 4)
