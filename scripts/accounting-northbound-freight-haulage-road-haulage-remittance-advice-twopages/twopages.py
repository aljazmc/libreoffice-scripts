"""Remittance Advice of Northbound Freight, two pages.

The remittance with deductions and the account after payment.
"""
from content import DOCUMENT, BUSINESS
from typesetting import typeset

DESIGN = {
    "accent": "#1c1c1c",
    "ink": "#1c1c1c",
    "muted": "#5e5e5e",
    "page": "#ffffff",
    "font": "Nimbus Sans",
    "series": ["#1c1c1c", "#f2b705", "#8a8a8a", "#d9480f", "#c9c9c9"],
    "good": "#4c9a2a",
    "warn": "#f2b705",
    "bad": "#d9480f",
    "info": "#3b7ea1",
    "radius": 0,
    "heading_font": "Nimbus Sans",
    "header": "band",
    "heading": "plain",
    "table": "zebra",
    "body_align": "start",
    "margin": 60,
    "footer": "NORTHBOUND FREIGHT LTD · Remittance Advice",
}


def twopages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 2)
