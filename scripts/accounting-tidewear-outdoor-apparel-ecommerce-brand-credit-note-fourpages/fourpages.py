"""Credit Note CN-3317 of Tidewear, four pages.

The credit note, the inspection, the account after credit and the returns
policy.
"""
from content import BUSINESS, DOCUMENT
from typesetting.accounting import typeset

DESIGN = {
    "accent": "#e4572e",
    "ink": "#1b263b",
    "muted": "#5c677d",
    "page": "#ffffff",
    "font": "URW Gothic",
    "series": ["#1b263b", "#e4572e", "#17bebb", "#76b041", "#adb5bd"],
    "good": "#76b041",
    "warn": "#f4a259",
    "bad": "#e4572e",
    "info": "#17bebb",
    "radius": 2,
    "heading_font": "URW Gothic",
    "chart_font": "URW Gothic",
    "header": "band",
    "heading": "plain",
    "table": "zebra",
    "body_align": "start",
    "margin": 60,
    "footer": "Tidewear Outdoor Ltd · Credit Note CN-3317 · Fictional example",
}


def fourpages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 4)
