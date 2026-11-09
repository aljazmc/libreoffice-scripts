"""Invoice of Rye & Crumb Bakery, one page.

A wholesale invoice to a café: the deliveries of October and what is due.
"""
from content import DOCUMENT, BUSINESS
from typesetting import typeset

DESIGN = {
    "accent": "#8c4a1f",
    "ink": "#3b2a1e",
    "muted": "#7a6352",
    "page": "#ffffff",
    "font": "URW Gothic",
    "heading_font": "URW Gothic",
    "chart_font": "URW Gothic",
    "series": ["#8c4a1f", "#d9a441", "#6b8f71", "#c46a4a", "#b9a58f"],
    "good": "#5f8f4e",
    "warn": "#d9a441",
    "bad": "#b8432f",
    "info": "#6b8f71",
    "radius": 2,
    "header": "band",
    "heading": "plain",
    "table": "zebra",
    "body_align": "start",
    "margin": 56,
    "footer": "Rye & Crumb Ltd · Invoice · company no. 11829304",
}


def onepage():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 1)
