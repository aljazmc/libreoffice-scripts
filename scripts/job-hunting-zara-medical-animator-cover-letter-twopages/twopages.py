"""Cover Letter of Zara Haddad, two pages.

The letter with the story of the heart that changed her career.
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


def twopages():
    return typeset(PERSONA, DOCUMENT, DESIGN, 2)
