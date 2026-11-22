"""Partner Capital Account Statement of Atelier Nord, one page.

One partner's share of the year's profit and her capital account.
"""
from content import BUSINESS, DOCUMENT
from typesetting.accounting import typeset

DESIGN = {
    "accent": "#c08a1e",
    "ink": "#111111",
    "muted": "#6b6b6b",
    "page": "#ffffff",
    "font": "TeX Gyre Termes",
    "series": ["#111111", "#c08a1e", "#8c8c8c", "#5b7c8d", "#d6d2c4"],
    "good": "#4f7a4a",
    "warn": "#c08a1e",
    "bad": "#a33a2a",
    "info": "#5b7c8d",
    "radius": 0,
    "heading_font": "TeX Gyre Termes",
    "chart_font": "TeX Gyre Termes",
    "header": "centered",
    "heading": "center",
    "table": "lines",
    "body_align": "justify",
    "margin": 70,
    "footer": "Atelier Nord Architects · Partner Capital Account Statement · Fictional example",
}


def onepage():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 1)
