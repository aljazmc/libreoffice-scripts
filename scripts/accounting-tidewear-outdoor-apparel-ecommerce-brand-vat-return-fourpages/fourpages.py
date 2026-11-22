"""VAT Return of Tidewear, four pages.

The return, workings, overseas sales, adjustments and the checks.
"""
from content import BUSINESS, DOCUMENT
from typesetting.accounting import typeset

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
    "footer": "Tidewear Outdoor Ltd · VAT Return · Fictional example",
}


def fourpages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 4)
