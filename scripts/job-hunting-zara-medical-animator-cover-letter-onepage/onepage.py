"""Cover Letter of Zara Haddad, one page.

A short letter, white on black, like an end credit.
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
    "heading": "plain",
    "bullet": "◦",
    "separator": " · ",
    "contact_join": "   ·   ",
    "margin": 64,
    "heading_format": "{title}",
    "body_align": "justify",
    "footer": "ZARA HADDAD · LETTER",
}


def onepage():
    return typeset(PERSONA, DOCUMENT, DESIGN, 1)
