"""VAT Return of Tidewear, one page.

The quarter's VAT return, box by box.
"""
from content import BUSINESS, DOCUMENT
from typesetting import typeset

DESIGN = {
    "accent": "#e4572e",
    "ink": "#1b263b",
    "muted": "#5c677d",
    "page": "#fbfbfb",
    "font": "Nimbus Sans",
    "series": ["#1b263b", "#e4572e", "#17bebb", "#76b041", "#adb5bd"],
    "good": "#76b041",
    "warn": "#f4a259",
    "bad": "#e4572e",
    "info": "#17bebb",
    "radius": 0,
    "heading_font": "Nimbus Sans",
    "header": "frame",
    "heading": "box",
    "heading_case": "upper",
    "table": "grid",
    "density": "compact",
    "body_align": "start",
    "footer": "Tidewear Outdoor Ltd · VAT Return",
}


def onepage():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 1)
