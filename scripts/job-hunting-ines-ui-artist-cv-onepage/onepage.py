"""Curriculum Vitae of Inês Duarte, one page.

A CV as a title screen: one level, no continues needed.
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
    "density": "compact",
}


def onepage():
    return typeset(PERSONA, DOCUMENT, DESIGN, 1)
