"""Cover Letter of Yuki Mori, one page.

A short letter to a car maker about the sound of silence.
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
    "heading": "plain",
    "heading_format": "{title}",
    "bullet": "♪",
    "bullet_width": 14,
    "separator": " · ",
    "contact_join": "  ·  ",
    "margin": 62,
    "footer": "Yuki Mori · letter · andante",
}


def onepage():
    return typeset(PERSONA, DOCUMENT, DESIGN, 1)
