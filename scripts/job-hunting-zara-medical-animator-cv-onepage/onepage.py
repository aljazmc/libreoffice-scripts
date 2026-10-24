"""Curriculum Vitae of Zara Haddad, one page.

A CV that opens like a title sequence, in one reel.
"""
from content import DOCUMENT, PERSONA
from typesetting import typeset

DESIGN = {
    "accent": "#fbbf24",
    "ink": "#e7e5e4",
    "muted": "#a8a29e",
    "page": "#050505",
    "font": "TeX Gyre Bonum",
    "header": "centered",
    "display": 1.35,
    "name_case": "upper",
    "heading": "center",
    "bullet": "◦",
    "separator": " · ",
    "contact_join": "   ·   ",
    "margin": 64,
    "heading_format": "Reel {number} · {title}",
    "footer": "ZARA HADDAD · CURRICULUM VITAE · ALL RIGHTS RESERVED",
    "density": "compact",
}


def onepage():
    return typeset(PERSONA, DOCUMENT, DESIGN, 1)
