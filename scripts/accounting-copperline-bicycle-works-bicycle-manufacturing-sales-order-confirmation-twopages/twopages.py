"""Sales Order Confirmation of Copperline Bicycle Works, two pages.

The order with the build slots and payment schedule.
"""
from content import BUSINESS, DOCUMENT
from typesetting.accounting import typeset

DESIGN = {
    "accent": "#c26a2d",
    "ink": "#22262b",
    "muted": "#6a6f75",
    "page": "#ffffff",
    "font": "Nimbus Sans",
    "series": ["#22262b", "#c26a2d", "#5a8fa3", "#a3a86b", "#c9ced3"],
    "good": "#5f9e6e",
    "warn": "#d9a03f",
    "bad": "#c0392b",
    "info": "#5a8fa3",
    "radius": 1,
    "header": "band",
    "heading": "plain",
    "table": "zebra",
    "body_align": "start",
    "margin": 60,
    "footer": "Copperline Bicycle Works · Sales Order Confirmation · Fictional example",
}


def twopages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 2)
