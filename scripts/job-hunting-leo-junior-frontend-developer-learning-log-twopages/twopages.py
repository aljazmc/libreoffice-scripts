"""Learning Log of Leo Brandt, two pages.

What Leo learned, when and from what, like a receipt.
"""
from content import DOCUMENT, PERSONA
from typesetting import typeset

DESIGN = {
    "accent": "#000000",
    "ink": "#222222",
    "muted": "#666666",
    "page": "#ffffff",
    "font": "Liberation Mono",
    "header": "centered",
    "name_case": "upper",
    "display": 1.1,
    "heading": "plain",
    "heading_format": "#{number:04d} {title}",
    "divider": "- - - - - - - - - - - - - - - - - -",
    "bullet": "*",
    "bullet_width": 12,
    "separator": " x ",
    "contact_join": " / ",
    "body_align": "start",
    "margin": 140,
    "dates_below": True,
    "heading_case": "upper",
    "footer": "LEARNING LOG · SUBTOTAL: 2,100 HOURS",
}


def twopages():
    return typeset(PERSONA, DOCUMENT, DESIGN, 2)
