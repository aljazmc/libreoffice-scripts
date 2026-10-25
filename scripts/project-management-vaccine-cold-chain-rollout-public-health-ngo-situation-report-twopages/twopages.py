"""Situation Report of Cold Chain for Every Child, two pages.

Sitrep 31 with coverage, the cold chain, stock and the actions.
"""
from content import DOCUMENT, PROJECT
from typesetting import typeset

DESIGN = {
    "accent": "#0072bc",
    "ink": "#1a1a1a",
    "muted": "#5a6670",
    "page": "#ffffff",
    "font": "DejaVu Sans",
    "header": "band",
    "heading": "box",
    "heading_case": "upper",
    "bullet": "■",
    "body_align": "start",
    "table": "grid",
    "density": "compact",
    "series": ["#0072bc", "#f7941d", "#00a1de", "#8dc63f", "#a0a8ae"],
    "good": "#4f9a2f",
    "warn": "#f7941d",
    "bad": "#e2231a",
    "info": "#00a1de",
    "radius": 1,
    "footer": "Cold Chain for Every Child · Situation Report · not for "
        "publication",
}


def twopages():
    return typeset(PROJECT, DOCUMENT, DESIGN, 2)
