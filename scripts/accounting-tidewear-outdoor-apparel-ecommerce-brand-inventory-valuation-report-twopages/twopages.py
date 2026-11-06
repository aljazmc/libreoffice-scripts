"""Inventory Valuation of Tidewear, two pages.

Landscape. The valuation by category with the provisions.
"""
from content import DOCUMENT, BUSINESS
from typesetting import typeset

DESIGN = {
    "accent": "#e4572e",
    "ink": "#1b263b",
    "muted": "#5c677d",
    "page": "#ffffff",
    "font": "Liberation Sans Narrow",
    "series": ["#1b263b", "#e4572e", "#17bebb", "#76b041", "#adb5bd"],
    "good": "#76b041",
    "warn": "#f4a259",
    "bad": "#e4572e",
    "info": "#17bebb",
    "radius": 2,
    "orientation": "landscape",
    "heading_font": "TeX Gyre Heros",
    "header": "bar",
    "heading": "tint",
    "table": "zebra",
    "chart_font": "Liberation Sans Narrow",
    "density": "compact",
    "body_align": "start",
    "footer": "Tidewear Outdoor Ltd · Inventory Valuation",
}


def twopages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 2)
