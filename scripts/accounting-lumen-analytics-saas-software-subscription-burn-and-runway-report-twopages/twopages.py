"""Burn and Runway of Lumen Analytics, two pages.

Burn by team, runway scenarios and the levers.
"""
from content import DOCUMENT, BUSINESS
from typesetting import typeset

DESIGN = {
    "accent": "#818cf8",
    "ink": "#e5e7eb",
    "muted": "#9aa3b5",
    "page": "#0b1020",
    "font": "Lato",
    "series": ["#818cf8", "#22d3ee", "#c084fc", "#fbbf24", "#64748b"],
    "good": "#10b981",
    "warn": "#f59e0b",
    "bad": "#ef4444",
    "info": "#06b6d4",
    "radius": 3,
    "grid": "#26304a",
    "header": "rule",
    "heading": "bar",
    "table": "lines",
    "body_align": "start",
    "footer": "Lumen Analytics Inc. · Burn and Runway · confidential",
}


def twopages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 2)
