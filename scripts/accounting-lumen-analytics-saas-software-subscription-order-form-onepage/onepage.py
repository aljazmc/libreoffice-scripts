"""Enterprise Order Form of Lumen Analytics, one page.

A three-year subscription order: the plan, the price and the signatures.
"""
from content import DOCUMENT, BUSINESS
from typesetting import typeset

DESIGN = {
    "accent": "#4f46e5",
    "ink": "#111827",
    "muted": "#6b7280",
    "page": "#ffffff",
    "font": "Nimbus Sans",
    "series": ["#4f46e5", "#06b6d4", "#a855f7", "#f59e0b", "#9ca3af"],
    "good": "#10b981",
    "warn": "#f59e0b",
    "bad": "#ef4444",
    "info": "#06b6d4",
    "radius": 3,
    "heading_font": "Lato",
    "header": "frame",
    "heading": "bar",
    "table": "lines",
    "body_align": "justify",
    "margin": 60,
    "footer": "Lumen Analytics Inc. · Enterprise Order Form · confidential",
}


def onepage():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 1)
