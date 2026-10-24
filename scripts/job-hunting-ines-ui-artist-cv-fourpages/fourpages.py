"""Curriculum Vitae of Inês Duarte, four pages.

The full game with every secret level unlocked.
"""
from content import DOCUMENT, PERSONA
from typesetting import typeset

DESIGN = {
    "accent": "#ffcc00",
    "ink": "#f5f3ff",
    "muted": "#c4b5fd",
    "page": "#1a1033",
    "font": "DejaVu Sans Mono",
    "header": "frame",
    "name_case": "upper",
    "display": 1.2,
    "heading": "slab",
    "heading_case": "upper",
    "bullet": "■",
    "bullet_width": 16,
    "separator": " ✦ ",
    "contact_join": "  ✦  ",
    "body_align": "start",
    "margin": 50,
    "heading_format": "▶ LEVEL {number}-1 · {title}",
    "footer": "INSERT COIN TO CONTINUE · INÊS DUARTE · CV",
    "divider": "★ ☆ ★ ☆ ★ ☆ ★",
    "density": "airy",
}


def fourpages():
    return typeset(PERSONA, DOCUMENT, DESIGN, 4)
