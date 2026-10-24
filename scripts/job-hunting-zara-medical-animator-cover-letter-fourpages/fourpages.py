"""Cover Letter of Zara Haddad, four pages.

The long letter with a first idea for the lab's next film.
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
    "divider": "· · ·",
    "bullet": "◦",
    "separator": " · ",
    "contact_join": "   ·   ",
    "margin": 64,
    "heading_format": "{title}",
    "body_align": "justify",
    "footer": "ZARA HADDAD · LETTER",
    "density": "spacious",
}


def fourpages():
    return typeset(PERSONA, DOCUMENT, DESIGN, 4)
