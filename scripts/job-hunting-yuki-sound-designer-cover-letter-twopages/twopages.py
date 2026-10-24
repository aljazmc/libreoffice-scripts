"""Cover Letter of Yuki Mori, two pages.

Why a game sound designer wants to give electric cars a voice.
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


def twopages():
    return typeset(PERSONA, DOCUMENT, DESIGN, 2)
