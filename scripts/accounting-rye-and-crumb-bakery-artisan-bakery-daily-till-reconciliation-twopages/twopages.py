"""Daily Till Reconciliation of Rye & Crumb Bakery, two pages.

The cash-up with the coin count, the card terminals and the banking.
"""
from content import BUSINESS, DOCUMENT
from typesetting import typeset

DESIGN = {
    "accent": "#8c4a1f",
    "ink": "#3b2a1e",
    "muted": "#7a6352",
    "page": "#fffdf5",
    "font": "Nimbus Sans",
    "heading_font": "Nimbus Sans",
    "chart_font": "URW Gothic",
    "series": ["#8c4a1f", "#d9a441", "#6b8f71", "#c46a4a", "#b9a58f"],
    "good": "#5f8f4e",
    "warn": "#d9a441",
    "bad": "#b8432f",
    "info": "#6b8f71",
    "radius": 0,
    "header": "frame",
    "heading": "box",
    "heading_case": "upper",
    "table": "grid",
    "density": "compact",
    "body_align": "start",
    "footer": "Rye & Crumb Ltd · Daily Till Reconciliation · company no. "
        "11829304",
}


def twopages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 2)
