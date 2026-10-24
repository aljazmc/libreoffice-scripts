"""Curriculum Vitae of Felix Amadi, two pages.

Two pages on a strict grid, gaps marked in red.
"""
from content import DOCUMENT, PERSONA
from typesetting import typeset

DESIGN = {
    "accent": "#ff2a00",
    "ink": "#000000",
    "muted": "#555555",
    "page": "#ffffff",
    "font": "TeX Gyre Heros",
    "heading_font": "TeX Gyre Heros Cn",
    "header": "rule",
    "display": 2.1,
    "name_case": "upper",
    "heading": "slab",
    "heading_case": "upper",
    "heading_format": "{number:02d}  {title}",
    "bullet": "—",
    "bullet_width": 16,
    "separator": " / ",
    "contact_join": " / ",
    "body_align": "start",
    "footer": "FELIX AMADI / CV / ZÜRICH 2026",
}


def twopages():
    return typeset(PERSONA, DOCUMENT, DESIGN, 2)
