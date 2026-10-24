"""Curriculum Vitae of Zara Haddad, two pages.

Credits, gaps and the turn to medicine, on two black pages.
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
    "divider": "▬▬▬▬▬▬▬▬",
    "bullet": "◦",
    "separator": " · ",
    "contact_join": "   ·   ",
    "margin": 64,
    "heading_format": "Reel {number} · {title}",
    "footer": "ZARA HADDAD · CURRICULUM VITAE · ALL RIGHTS RESERVED",
}


def twopages():
    return typeset(PERSONA, DOCUMENT, DESIGN, 2)
