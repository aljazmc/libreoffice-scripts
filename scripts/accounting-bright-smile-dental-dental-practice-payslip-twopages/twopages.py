"""Payslip of Bright Smile Dental, two pages.

The payslip with the year to date and the employer's costs.
"""
from content import BUSINESS, DOCUMENT
from typesetting import typeset

DESIGN = {
    "accent": "#0e9f9a",
    "ink": "#1f2d3d",
    "muted": "#5f7183",
    "page": "#ffffff",
    "font": "Nimbus Sans",
    "heading_font": "Nimbus Sans",
    "chart_font": "Liberation Sans",
    "series": ["#0e9f9a", "#5bc0eb", "#f25f5c", "#f2b134", "#a0aec0"],
    "good": "#2bb673",
    "warn": "#f2b134",
    "bad": "#f25f5c",
    "info": "#5bc0eb",
    "radius": 0,
    "header": "frame",
    "heading": "box",
    "heading_case": "upper",
    "table": "grid",
    "density": "compact",
    "body_align": "start",
    "margin": 60,
    "footer": "Bright Smile Dental Practice · Payslip",
}


def twopages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 2)
