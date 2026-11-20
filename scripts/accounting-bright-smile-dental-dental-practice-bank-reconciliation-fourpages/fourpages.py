"""Bank Reconciliation of Bright Smile Dental, four pages.

The reconciliation, the items, the card settlements and the review.
"""
from content import BUSINESS, DOCUMENT
from typesetting import typeset

DESIGN = {
    "accent": "#0e9f9a",
    "ink": "#1f2d3d",
    "muted": "#5f7183",
    "page": "#ffffff",
    "font": "Liberation Mono",
    "heading_font": "URW Gothic",
    "chart_font": "Liberation Sans",
    "series": ["#0e9f9a", "#5bc0eb", "#f25f5c", "#f2b134", "#a0aec0"],
    "good": "#2bb673",
    "warn": "#f2b134",
    "bad": "#f25f5c",
    "info": "#5bc0eb",
    "radius": 0,
    "header": "rule",
    "heading": "slab",
    "table": "grid",
    "density": "compact",
    "body_align": "start",
    "footer": "Bright Smile Dental Practice · Bank Reconciliation",
}


def fourpages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 4)
