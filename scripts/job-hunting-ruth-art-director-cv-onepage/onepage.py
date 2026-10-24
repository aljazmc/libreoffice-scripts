"""Curriculum Vitae of Ruth Okonkwo-Lane, one page.

A one-page zine, folded from a CV.
"""
from content import DOCUMENT, PERSONA
from typesetting import typeset

DESIGN = {
    "accent": "#e63946",
    "ink": "#1b1b1b",
    "muted": "#6b4f3a",
    "page": "#fff4d6",
    "font": "Liberation Serif",
    "heading_font": "Liberation Sans Narrow",
    "header": "bar",
    "name_case": "lower",
    "display": 1.5,
    "heading": "slab",
    "heading_case": "lower",
    "bullet": "✶",
    "bullet_width": 14,
    "separator": " ~ ",
    "contact_join": "  ✶  ",
    "body_align": "start",
    "footer": "ruth okonkwo-lane · cv · photocopy freely",
    "density": "compact",
}


def onepage():
    return typeset(PERSONA, DOCUMENT, DESIGN, 1)
