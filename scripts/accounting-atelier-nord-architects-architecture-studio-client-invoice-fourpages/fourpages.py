"""Invoice 2027-041 of Atelier Nord, four pages.

The invoice, the fee account, the timesheet appendix and the expenses.
"""
from content import BUSINESS, DOCUMENT
from typesetting import typeset

DESIGN = {
    "accent": "#c08a1e",
    "ink": "#111111",
    "muted": "#6b6b6b",
    "page": "#ffffff",
    "font": "Nimbus Sans",
    "series": ["#111111", "#c08a1e", "#8c8c8c", "#5b7c8d", "#d6d2c4"],
    "good": "#4f7a4a",
    "warn": "#c08a1e",
    "bad": "#a33a2a",
    "info": "#5b7c8d",
    "radius": 0,
    "header": "rule",
    "heading": "plain",
    "table": "lines",
    "body_align": "start",
    "margin": 72,
    "title_size": 30,
    "footer": "Atelier Nord Architects · Invoice 2027-041",
}


def fourpages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 4)
