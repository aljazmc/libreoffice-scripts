"""Launch Marketing Calendar of Keeper of the Last Light, one page.

The beats to launch day and the wishlists they should bring.
"""
from content import DOCUMENT, PROJECT
from typesetting import typeset

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
        "Tidepool Games",
}


def onepage():
    return typeset(PROJECT, DOCUMENT, DESIGN, 1)
