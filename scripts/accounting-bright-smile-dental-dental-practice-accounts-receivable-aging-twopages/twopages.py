"""Accounts Receivable Aging of Bright Smile Dental, two pages.

The aging by payer, the oldest balances and the trend.
"""
from content import BUSINESS, DOCUMENT
from typesetting.accounting import typeset

DESIGN = {
    "accent": "#0e9f9a",
    "ink": "#1f2d3d",
    "muted": "#5f7183",
    "page": "#ffffff",
    "font": "Tuffy",
    "heading_font": "URW Gothic",
    "chart_font": "Liberation Sans",
    "series": ["#0e9f9a", "#5bc0eb", "#f25f5c", "#f2b134", "#a0aec0"],
    "good": "#2bb673",
    "warn": "#f2b134",
    "bad": "#f25f5c",
    "info": "#5bc0eb",
    "radius": 4,
    "header": "bar",
    "heading": "bar",
    "table": "zebra",
    "body_align": "start",
    "footer": "Bright Smile Dental Practice · Accounts Receivable Aging",
}


def twopages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 2)
