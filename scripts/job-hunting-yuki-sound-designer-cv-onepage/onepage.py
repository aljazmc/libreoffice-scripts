"""Curriculum Vitae of Yuki Mori, one page.

A CV set like a single page of a printed score.
"""
from content import DOCUMENT, PERSONA
from typesetting import typeset

DESIGN = {
    "accent": "#7c2d12",
    "ink": "#2b2118",
    "muted": "#8b6f5a",
    "page": "#fbf7ee",
    "font": "TeX Gyre Schola",
    "header": "centered",
    "heading": "center",
    "heading_format": "Movement {roman} · {title}",
    "bullet": "♪",
    "bullet_width": 14,
    "separator": " · ",
    "contact_join": "  ·  ",
    "margin": 62,
    "footer": "Yuki Mori · Curriculum Vitae · tempo rubato",
    "density": "compact",
}


def onepage():
    return typeset(PERSONA, DOCUMENT, DESIGN, 1)
