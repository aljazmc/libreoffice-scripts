"""Process Book of Felix Amadi, two pages.

The process of an explainer film, step by step.
"""
from content import DOCUMENT, PERSONA
from typesetting import typeset

DESIGN = {
    "accent": "#000000",
    "ink": "#000000",
    "muted": "#ff2a00",
    "page": "#ffffff",
    "font": "TeX Gyre Heros",
    "heading_font": "TeX Gyre Heros Cn",
    "header": "rule",
    "display": 1,
    "name_case": "upper",
    "heading": "slab",
    "heading_case": "upper",
    "heading_format": "{number:02d} / {title}",
    "bullet": "—",
    "bullet_width": 16,
    "separator": " / ",
    "contact_join": " / ",
    "body_align": "start",
    "footer": "PROCESS BOOK / “HOW A VIRUS TRAVELS”",
}


def twopages():
    return typeset(PERSONA, DOCUMENT, DESIGN, 2)
