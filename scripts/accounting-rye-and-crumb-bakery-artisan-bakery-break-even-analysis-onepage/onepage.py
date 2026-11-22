"""Break-Even Analysis of Rye & Crumb Bakery, one page.

How many loaves a day the new shop must sell to break even.
"""
from content import BUSINESS, DOCUMENT
from typesetting.accounting import typeset

DESIGN = {
    "accent": "#8c4a1f",
    "ink": "#3b2a1e",
    "muted": "#7a6352",
    "page": "#ffffff",
    "font": "Tuffy",
    "heading_font": "URW Gothic",
    "chart_font": "URW Gothic",
    "series": ["#8c4a1f", "#d9a441", "#6b8f71", "#c46a4a", "#b9a58f"],
    "good": "#5f8f4e",
    "warn": "#d9a441",
    "bad": "#b8432f",
    "info": "#6b8f71",
    "radius": 4,
    "header": "bar",
    "heading": "slab",
    "table": "lines",
    "body_align": "start",
    "footer": "Rye & Crumb Ltd · Break-Even Analysis · company no. 11829304 · Fictional example",
}


def onepage():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 1)
