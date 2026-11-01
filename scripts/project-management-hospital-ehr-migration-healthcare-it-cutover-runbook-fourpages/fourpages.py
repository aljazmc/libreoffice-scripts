"""Cutover Runbook of St Brigid's EHR Migration, four pages.

Landscape. The runbook in full: timeline, steps, owners, checkpoints,
rollback and the command centre.
"""
from content import DOCUMENT, PROJECT
from typesetting import typeset

DESIGN = {
    "accent": "#005eb8",
    "ink": "#212b32",
    "muted": "#4c6272",
    "page": "#ffffff",
    "font": "Liberation Sans",
    "header": "bar",
    "heading": "tint",
    "heading_case": "upper",
    "bullet": "•",
    "body_align": "start",
    "table": "lines",
    "series": ["#005eb8", "#41b6e6", "#00a499", "#768692", "#ae2573"],
    "good": "#007f3b",
    "warn": "#ffb81c",
    "bad": "#da291c",
    "info": "#41b6e6",
    "radius": 2,
    "orientation": "landscape",
    "footer": "St Brigid's University Hospital · Cutover Runbook · OFFICIAL",
}


def fourpages():
    return typeset(PROJECT, DOCUMENT, DESIGN, 4)
