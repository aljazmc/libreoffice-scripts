"""Curriculum Vitae of Felix Amadi, one page.

A Swiss poster that happens to be a CV.
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
    "display": 1.8,
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
    "density": "compact",
}


def onepage():
    return typeset(PERSONA, DOCUMENT, DESIGN, 1)
