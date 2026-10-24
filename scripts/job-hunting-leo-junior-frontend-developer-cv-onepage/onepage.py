"""Curriculum Vitae of Leo Brandt, one page.

A CV printed on a till receipt, one page long.
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
    "bullet": "*",
    "bullet_width": 12,
    "separator": " x ",
    "contact_join": " / ",
    "body_align": "start",
    "margin": 140,
    "dates_below": True,
    "footer": "THANK YOU FOR READING · PLEASE KEEP THIS RECEIPT",
    "density": "compact",
}


def onepage():
    return typeset(PERSONA, DOCUMENT, DESIGN, 1)
