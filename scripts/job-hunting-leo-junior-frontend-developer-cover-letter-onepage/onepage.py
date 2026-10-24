"""Cover Letter of Leo Brandt, one page.

A short letter from the workshop to a start-up for craftspeople.
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
    "heading_format": "> {title}",
    "bullet": "*",
    "bullet_width": 12,
    "separator": " x ",
    "contact_join": " / ",
    "body_align": "start",
    "margin": 120,
    "dates_below": True,
    "footer": "LETTER · NO REFUNDS · LOTS OF ENTHUSIASM",
}


def onepage():
    return typeset(PERSONA, DOCUMENT, DESIGN, 1)
