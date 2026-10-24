"""Curriculum Vitae of Leo Brandt, two pages.

Two receipts: the workshop years and the code years.
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
    "heading": "center",
    "heading_format": "*** {title} ***",
    "divider": "- - - - - - - - - - - - - - - - - -",
    "bullet": "*",
    "bullet_width": 12,
    "separator": " x ",
    "contact_join": " / ",
    "body_align": "start",
    "margin": 140,
    "dates_below": True,
    "footer": "THANK YOU FOR READING · PLEASE KEEP THIS RECEIPT",
}


def twopages():
    return typeset(PERSONA, DOCUMENT, DESIGN, 2)
