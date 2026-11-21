"""Unit Economics of Tidewear, one page.

What one order and one customer are worth.
"""
from content import BUSINESS, DOCUMENT
from typesetting.accounting import typeset

DESIGN = {
    "accent": "#e4572e",
    "ink": "#1b263b",
    "muted": "#5c677d",
    "page": "#f4f1ea",
    "font": "TeX Gyre Adventor",
    "series": ["#1b263b", "#e4572e", "#17bebb", "#76b041", "#adb5bd"],
    "good": "#76b041",
    "warn": "#f4a259",
    "bad": "#e4572e",
    "info": "#17bebb",
    "radius": 5,
    "heading_font": "TeX Gyre Adventor",
    "chart_font": "TeX Gyre Adventor",
    "header": "bar",
    "heading": "bar",
    "table": "lines",
    "body_align": "start",
    "footer": "Tidewear Outdoor Ltd · Unit Economics",
}


def onepage():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 1)
