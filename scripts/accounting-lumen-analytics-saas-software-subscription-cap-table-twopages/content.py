"""Capitalisation Table of Lumen Analytics: the business and everything the
document could say. The typesetting keeps what fits into two pages, the most
important first."""

BUSINESS = {
    "name": "Lumen Analytics",
    "author": "Lumen Analytics Inc., legal and finance",
}

# holder, class, shares by round: founding, seed (SAFE converted), Series A
HOLDERS = [
    ("Elena Marsh", "Founder", "Common", 3_600_000, 0, 0),
    ("Rafael Ortiz", "Founder", "Common", 3_200_000, 0, 0),
    ("Jun Park", "Founding engineer", "Common", 400_000, 0, 0),
    ("Harbour Angels", "Investor", "Seed preferred", 0, 1_050_000, 0),
    ("Pioneer Fund II", "Investor", "Seed preferred", 0, 1_420_000,
     480_000),
    ("Northlake Ventures", "Investor", "Series A preferred", 0, 0,
     3_260_000),
    ("Atlas Seed", "Investor", "Series A preferred", 0, 0, 380_000),
]
POOL_GRANTED = 1_140_000
POOL_UNGRANTED = 760_000
A_PRICE = 4.37

ROWS = [(name, role, cls, f + s + a) for name, role, cls, f, s, a in
        HOLDERS]
ROWS += [("Employees, options granted", "Option pool", "Options",
          POOL_GRANTED),
         ("Pool, not yet granted", "Option pool", "Options",
          POOL_UNGRANTED)]
FD = sum(row[3] for row in ROWS)


def pct(value):
    return f"{value / FD:.2%}"


def n(value):
    return f"{value:,.0f}"


GROUPS = {}
for name, role, cls, shares in ROWS:
    group = ("Founders" if role in ("Founder", "Founding engineer")
             else "Option pool" if role == "Option pool"
             else "Seed investors" if cls == "Seed preferred"
             else "Series A investors")
    if name == "Pioneer Fund II":
        group = "Seed investors"
    GROUPS[group] = GROUPS.get(group, 0) + shares

DOCUMENT = {
    "title": "Capitalisation Table",
    "subtitle": "Fully diluted, after the Series A closing on 14 March 2026",
    "meta": [("Company", "Lumen Analytics Inc."),
             ("Fully diluted", n(FD) + " shares"),
             ("Series A price", f"${A_PRICE:.2f}"),
             ("Post-money", f"${FD * A_PRICE / 1e6:.1f}m"),
             ("As of", "31 Dec 2026")],
    "sections": [
        {"heading": "Ownership", "kind": "table", "whole": True,
         "weight": 0.1,
         "columns": [("Holder", 2.2), ("Role", 1.4), ("Class", 1.6),
                     ("Founding", 1, "end"), ("Seed", 1, "end"),
                     ("Series A", 1, "end"), ("Fully diluted", 1.1, "end"),
                     ("%", 0.8, "end")],
         "rows": [[name, role, cls, n(f) if f else "—", n(s) if s else "—",
                   n(a) if a else "—", n(f + s + a), pct(f + s + a)]
                  for name, role, cls, f, s, a in HOLDERS]
         + [["Employees, options granted", "Option pool", "Options", "—",
             "—", "—", n(POOL_GRANTED), pct(POOL_GRANTED)],
            {"cells": ["Pool, not yet granted", "Option pool", "Options",
                       "—", "—", "—", n(POOL_UNGRANTED),
                       pct(POOL_UNGRANTED)], "style": "muted"},
            {"cells": ["Total", "", "", "", "", "", n(FD), "100.00%"],
             "style": "total"}]},
        {"heading": "Who owns Lumen", "kind": "figure", "weight": 0.2,
         "height": {1: 135, 2: 150, 4: 160}, "widths": [2, 3],
         "charts": [
             {"type": "donut", "title": "Fully diluted",
              "segments": [(group, shares / 1000) for group, shares in
                           GROUPS.items()],
              "format": "{:,.0f}k", "center": (f"{FD / 1e6:.1f}m",
                                              "shares")},
             {"type": "bars", "horizontal": True, "stacked": True,
              "title": "Ownership after each round", "subtitle": "%",
              "format": "{:.0f}", "inside": True, "values": False,
              "categories": ["Founding 2023", "Seed 2024",
                             "Series A 2026"],
              "series": [{"name": "Founders",
                          "values": [100, 72.7, 45.9]},
                         {"name": "Seed", "color": 1,
                          "values": [0, 24.8, 18.8]},
                         {"name": "Series A", "color": 2,
                          "values": [0, 0, 23.2]},
                         {"name": "Pool", "color": 4,
                          "values": [0, 2.5, 12.1]}]},
         ]},
        {"heading": "Rounds", "kind": "table", "whole": True,
         "weight": 0.3, "min_pages": 2,
         "columns": [("Round", 1.4), ("Date", 1), ("Price per share", 1.1,
                                                   "end"),
                     ("Raised", 1, "end"), ("Pre-money", 1, "end"),
                     ("Post-money", 1, "end"), ("Lead", 1.8)],
         "rows": [["Founding", "Feb 2023", "$0.0001", "$700", "—", "—",
                   "Founders"],
                  ["Seed (SAFEs converted)", "Jun 2024", "$1.05",
                   "$2.6m", "$7.6m", "$10.2m", "Pioneer Fund II"],
                  ["Series A", "Mar 2026", f"${A_PRICE:.2f}", "$18.0m",
                   "$50.6m", "$68.6m", "Northlake Ventures"]]},
        {"heading": "Option pool", "kind": "figure", "weight": 0.4,
         "min_pages": 2, "height": 120, "charts": [{"type": "progress",
          "format": "{:,.0f}", "max": POOL_GRANTED + POOL_UNGRANTED,
          "items": [{"label": "Granted", "value": POOL_GRANTED,
                     "status": 0, "note": "34 employees"},
                    {"label": "Vested", "value": 410_000, "status": 1,
                     "note": "4-year vesting, 1-year cliff"},
                    {"label": "Exercised", "value": 90_000, "status": 2,
                     "note": "included in common at exercise"},
                    {"label": "Available", "value": POOL_UNGRANTED,
                     "status": 4, "note": "for hires in 2027 – 2028"}]}]},
        {"heading": "Exit waterfall", "kind": "figure", "weight": 0.5,
         "min_pages": 4, "height": 180, "charts": [{"type": "bars",
          "stacked": True, "title": "Who receives what at a sale",
          "subtitle": "$m, by sale price, 1× non-participating "
                      "preferences",
          "format": "{:,.0f}",
          "categories": ["$20m", "$50m", "$100m", "$250m", "$500m"],
          "series": [{"name": "Series A", "color": 2,
                      "values": [18.0, 18.0, 23.2, 58.0, 116.0]},
                     {"name": "Seed", "color": 1,
                      "values": [2.0, 7.8, 18.8, 47.0, 94.0]},
                     {"name": "Founders", "color": 0,
                      "values": [0.0, 19.1, 45.9, 114.8, 229.5]},
                     {"name": "Employees", "color": 4,
                      "values": [0.0, 5.0, 12.1, 30.2, 60.5]}]}]},
        {"heading": "Preferred share terms", "kind": "table",
         "whole": True, "weight": 0.6, "min_pages": 4,
         "columns": [("Term", 1.6), ("Seed preferred", 2.4),
                     ("Series A preferred", 2.4)],
         "rows": [["Liquidation preference", "1×, non-participating",
                   "1×, non-participating, senior to seed"],
                  ["Conversion", "1:1 into common", "1:1 into common"],
                  ["Anti-dilution", "Broad-based weighted average",
                   "Broad-based weighted average"],
                  ["Board seats", "One, jointly with Series A",
                   "One seat, Northlake Ventures"],
                  ["Pro-rata rights", "Yes, major investors only",
                   "Yes"]]},
        {"heading": "Notes", "kind": "bullets", "weight": 0.7,
         "step": 0.1, "min_pages": 4, "items": [
             "Fully diluted counts every issued share, every option "
             "granted and the options still available in the pool.",
             "Pioneer Fund II bought 480,000 Series A shares under its "
             "pro-rata right.",
             "The pool was topped up to 12 % of the fully diluted "
             "shares before the Series A, at the investors' request.",
             "Founders' shares are subject to reverse vesting until "
             "March 2027.",
         ]},
        {"heading": "Founder dilution", "kind": "figure", "weight": 0.8,
         "min_pages": 4, "height": 140, "charts": [{"type": "line",
          "title": "Founders' share of the company", "subtitle": "%",
          "x": ["Founding", "Seed", "Series A", "Series B (plan)"],
          "format": "{:.0f}", "end_labels": True,
          "series": [{"name": "Founders", "values": [100, 72.7, 45.9,
                                                     37.0]},
                     {"name": "Value of founders' shares, $m", "color": 1,
                      "dash": True, "values": [0, 7.4, 31.5, 92.5]}]}]},
    ],
}
