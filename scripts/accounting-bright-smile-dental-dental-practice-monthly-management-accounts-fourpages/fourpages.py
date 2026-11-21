"""Management Accounts of Bright Smile Dental, four pages.

The pack: profit and loss, balance sheet, cash, dentists and commentary.
"""
from content import BUSINESS, DOCUMENT
from typesetting.accounting import typeset

DESIGN = {
    "accent": "#0e9f9a",
    "ink": "#1f2d3d",
    "muted": "#5f7183",
    "page": "#ffffff",
    "font": "Liberation Sans",
    "heading_font": "URW Gothic",
    "chart_font": "Liberation Sans",
    "series": ["#0e9f9a", "#5bc0eb", "#f25f5c", "#f2b134", "#a0aec0"],
    "good": "#2bb673",
    "warn": "#f2b134",
    "bad": "#f25f5c",
    "info": "#5bc0eb",
    "radius": 4,
    "header": "band",
    "heading": "tint",
    "table": "lines",
    "body_align": "start",
    "footer": "Bright Smile Dental Practice · Management Accounts",
}


def fourpages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 4)
