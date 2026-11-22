"""Revenue by Treatment of Bright Smile Dental, four pages.

The analysis by treatment, dentist, payer and month, with the opportunities.
"""
from content import BUSINESS, DOCUMENT
from typesetting.accounting import typeset

DESIGN = {
    "accent": "#0e9f9a",
    "ink": "#1f2d3d",
    "muted": "#5f7183",
    "page": "#f4fbfa",
    "font": "Liberation Sans",
    "heading_font": "URW Gothic",
    "chart_font": "Liberation Sans",
    "series": ["#0e9f9a", "#5bc0eb", "#f25f5c", "#f2b134", "#a0aec0"],
    "good": "#2bb673",
    "warn": "#f2b134",
    "bad": "#f25f5c",
    "info": "#5bc0eb",
    "radius": 4,
    "header": "bar",
    "heading": "plain",
    "table": "lines",
    "body_align": "start",
    "footer": "Bright Smile Dental Practice · Revenue by Treatment · Fictional example",
}


def fourpages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 4)
