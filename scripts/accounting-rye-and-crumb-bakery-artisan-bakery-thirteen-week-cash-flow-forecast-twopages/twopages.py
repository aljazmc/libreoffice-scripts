"""13-Week Cash Flow Forecast of Rye & Crumb Bakery, two pages.

Landscape. The forecast week by week, with the receipts and the payments.
"""
from content import BUSINESS, DOCUMENT
from typesetting.accounting import typeset

DESIGN = {
    "accent": "#8c4a1f",
    "ink": "#3b2a1e",
    "muted": "#7a6352",
    "page": "#ffffff",
    "font": "Nimbus Sans",
    "heading_font": "URW Gothic",
    "chart_font": "URW Gothic",
    "series": ["#8c4a1f", "#d9a441", "#6b8f71", "#c46a4a", "#b9a58f"],
    "good": "#5f8f4e",
    "warn": "#d9a441",
    "bad": "#b8432f",
    "info": "#6b8f71",
    "radius": 2,
    "orientation": "landscape",
    "header": "bar",
    "heading": "tint",
    "heading_case": "upper",
    "table": "zebra",
    "density": "compact",
    "body_align": "start",
    "footer": "Rye & Crumb Ltd · 13-Week Cash Flow Forecast · company no. "
        "11829304",
}


def twopages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 2)
