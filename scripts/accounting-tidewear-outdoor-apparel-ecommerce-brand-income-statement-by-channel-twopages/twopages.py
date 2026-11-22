"""Income Statement by Channel of Tidewear, two pages.

The statement by channel with contribution and margins.
"""
from content import BUSINESS, DOCUMENT
from typesetting.accounting import typeset

DESIGN = {
    "accent": "#e4572e",
    "ink": "#1b263b",
    "muted": "#5c677d",
    "page": "#ffffff",
    "font": "TeX Gyre Heros",
    "series": ["#1b263b", "#e4572e", "#17bebb", "#76b041", "#adb5bd"],
    "good": "#76b041",
    "warn": "#f4a259",
    "bad": "#e4572e",
    "info": "#17bebb",
    "radius": 2,
    "header": "rule",
    "heading": "slab",
    "heading_case": "upper",
    "table": "lines",
    "body_align": "start",
    "footer": "Tidewear Outdoor Ltd · Income Statement by Channel · Fictional example",
}


def twopages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 2)
