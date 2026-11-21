"""Expense Claim of Atelier Nord, four pages.

The claim, the mileage, the receipts list, the policy and the approvals.
"""
from content import BUSINESS, DOCUMENT
from typesetting.accounting import typeset

DESIGN = {
    "accent": "#c08a1e",
    "ink": "#111111",
    "muted": "#6b6b6b",
    "page": "#ffffff",
    "font": "TeX Gyre Heros",
    "series": ["#111111", "#c08a1e", "#8c8c8c", "#5b7c8d", "#d6d2c4"],
    "good": "#4f7a4a",
    "warn": "#c08a1e",
    "bad": "#a33a2a",
    "info": "#5b7c8d",
    "radius": 0,
    "heading_font": "TeX Gyre Heros Cn",
    "header": "frame",
    "heading": "box",
    "heading_case": "upper",
    "table": "grid",
    "density": "compact",
    "body_align": "start",
    "footer": "Atelier Nord Architects · Expense Claim",
}


def fourpages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 4)
