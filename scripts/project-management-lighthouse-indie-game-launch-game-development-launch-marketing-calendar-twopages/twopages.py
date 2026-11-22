"""Launch Marketing Calendar of Keeper of the Last Light, two pages.

The calendar of beats, channels and the wishlist curve.
"""
from content import DOCUMENT, PROJECT
from typesetting.project_management import typeset

DESIGN = {
    "accent": "#7cff6b",
    "ink": "#e8f1ff",
    "muted": "#8fa7c7",
    "page": "#0e1a2b",
    "font": "DejaVu Sans Mono",
    "chart_font": "DejaVu Sans Mono",
    "header": "rule",
    "heading": "slab",
    "heading_format": "> {title}_",
    "bullet": "»",
    "bullet_width": 14,
    "body_align": "start",
    "table": "zebra",
    "density": "compact",
    "title_size": 22,
    "series": ["#7cff6b", "#ff6bcb", "#6bd5ff", "#ffd36b", "#a78bfa"],
    "good": "#7cff6b",
    "warn": "#ffd36b",
    "bad": "#ff6b6b",
    "info": "#6bd5ff",
    "grid": "#2a3b55",
    "radius": 0,
    "footer": "KEEPER OF THE LAST LIGHT · Launch Marketing Calendar · "
        "Tidepool Games · Fictional example",
}


def twopages():
    return typeset(PROJECT, DOCUMENT, DESIGN, 2)
