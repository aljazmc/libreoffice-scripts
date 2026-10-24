"""Cover Letter of Felix Amadi, two pages.

Why a motion designer wants to explain public health.
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
    "display": 1.6,
    "name_case": "upper",
    "heading": "rule",
    "heading_case": "upper",
    "heading_format": "{number:02d}  {title}",
    "bullet": "—",
    "bullet_width": 16,
    "separator": " / ",
    "contact_join": " / ",
    "body_align": "start",
    "footer": "FELIX AMADI / LETTER",
}


def twopages():
    return typeset(PERSONA, DOCUMENT, DESIGN, 2)
