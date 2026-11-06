"""Inventory Valuation of Tidewear: the business and everything the document
could say. The typesetting keeps what fits into two pages, the most
important first."""

BUSINESS = {
    "name": "Tidewear",
    "author": "Tidewear Outdoor Ltd, finance and warehouse",
}

# category, units, unit cost £, expected selling price net £,
# selling cost per unit £, share older than 12 months
STOCK = [("Waterproof jackets", 3_840, 38.20, 96.00, 14.00, 0.08),
         ("Insulated jackets", 2_160, 44.60, 112.00, 15.00, 0.21),
         ("Fleeces and midlayers", 5_420, 16.80, 42.00, 7.50, 0.12),
         ("Base layers", 6_900, 9.40, 28.00, 5.20, 0.05),
         ("Trousers", 3_310, 21.70, 58.00, 8.80, 0.09),
         ("Kids' range", 2_640, 11.20, 26.00, 5.00, 0.18),
         ("Hats, gloves, socks", 9_850, 3.10, 11.00, 2.40, 0.14),
         ("Last season's colours (clearance)", 4_120, 22.50, 21.00, 6.00,
          1.00)]


def gbp(value):
    return f"£{value:,.0f}"


ROWS = []
for name, units, cost, price, sell, old in STOCK:
    at_cost = units * cost
    nrv = units * (price - sell)
    value = min(at_cost, nrv)
    ROWS.append((name, units, cost, at_cost, nrv, value, at_cost - value,
                 old))
UNITS = sum(r[1] for r in ROWS)
COST = sum(r[3] for r in ROWS)
VALUE = sum(r[5] for r in ROWS)
WRITE_DOWN = COST - VALUE

DOCUMENT = {
    "title": "Inventory Valuation",
    "subtitle": "Stock at the year end, 31 January 2028 · at the lower of "
                "cost and net realisable value · Falmouth warehouse",
    "meta": [("Units", f"{UNITS:,}"), ("At cost", gbp(COST)),
             ("Write-down", gbp(WRITE_DOWN)),
             ("Carrying value", gbp(VALUE)), ("Count", "31 Jan 2028")],
    "sections": [
        {"heading": "Valuation by category", "kind": "table",
         "whole": True, "weight": 0.1,
         "badges": {"100%": "bad"},
         "columns": [("Category", 2.6), ("Units", 0.8, "end"),
                     ("Unit cost", 0.8, "end"), ("At cost", 1, "end"),
                     ("Net realisable", 1, "end"),
                     ("Carrying value", 1, "end"),
                     ("Write-down", 0.9, "end"),
                     ("Over 12 months", 0.9, "end")],
         "rows": [[n, f"{u:,}", f"£{c:.2f}", gbp(ac), gbp(nrv), gbp(v),
                   gbp(w) if w else "—", f"{o:.0%}"]
                  for n, u, c, ac, nrv, v, w, o in ROWS]
         + [{"cells": ["Total", f"{UNITS:,}", "", gbp(COST), "",
                       gbp(VALUE), gbp(WRITE_DOWN), ""],
             "style": "total"}]},
        {"heading": "Stock by category", "kind": "figure", "weight": 0.2,
         "min_pages": 2, "height": 160, "widths": [3, 2], "charts": [
             {"type": "bars", "horizontal": True, "stacked": True,
              "values": False, "format": "£{:,.0f}k",
              "subtitle": "£k at cost, split by age",
              "categories": [r[0].split(" (")[0] for r in ROWS],
              "series": [{"name": "Under 12 months", "values": [
                  round(r[3] * (1 - r[7]) / 1000, 1) for r in ROWS]},
                         {"name": "Older", "color": "warn", "values": [
                             round(r[3] * r[7] / 1000, 1)
                             for r in ROWS]}]},
             {"type": "donut", "title": "Carrying value",
              "segments": [(r[0].split(" (")[0].split(",")[0],
                            round(r[5] / 1000, 1)) for r in ROWS[:5]]
              + [("Other", round(sum(r[5] for r in ROWS[5:]) / 1000, 1),
                  4)],
              "format": "£{:,.0f}k", "center": (f"£{VALUE / 1000:.0f}k",
                                                "stock")},
         ]},
        {"heading": "Write-down", "kind": "callout", "weight": 0.3,
         "min_pages": 2, "tone": "warn", "label": "Clearance stock",
         "text": f"of {ROWS[-1][1]:,} units of last season's colours "
                 "sells for less than it cost once marketplace fees and "
                 f"postage are paid: written down by {gbp(WRITE_DOWN)} "
                 "to net realisable value."},
        {"heading": "Stock count", "kind": "table", "whole": True,
         "weight": 0.5, "min_pages": 4,
         "badges": {"Agreed": "good", "Adjusted": "warn"},
         "columns": [("Area", 2.4), ("Book units", 1, "end"),
                     ("Counted", 1, "end"), ("Difference", 1, "end"),
                     ("", 0.9, "center")],
         "rows": [["Aisle A – jackets", "6,012", "6,000", "−12",
                   "Adjusted"],
                  ["Aisle B – fleeces and trousers", "8,734", "8,730",
                   "−4", "Agreed"],
                  ["Aisle C – base layers and kids", "9,540", "9,540",
                   "0", "Agreed"],
                  ["Mezzanine – accessories", "9,861", "9,850", "−11",
                   "Adjusted"],
                  ["Returns cage", "4,138", "4,120", "−18", "Adjusted"],
                  {"cells": ["Total", "38,285", "38,240", "−45", ""],
                   "style": "total"}]},
        {"heading": "Turnover", "kind": "figure", "weight": 0.6,
         "min_pages": 4, "height": 150, "charts": [{"type": "bars",
          "title": "Weeks of stock at the current rate of sale",
          "format": "{:.0f}", "target": 26, "target_label": "policy",
          "categories": [r[0].split(" (")[0].split(",")[0]
                         for r in ROWS],
          "series": [{"name": "Weeks", "values": [18, 31, 22, 14, 20, 29,
                                                  26, 64],
                      "colors": [0, "warn", 0, 0, 0, "warn", 0,
                                 "bad"]}]}]},
        {"heading": "Policy", "kind": "bullets", "weight": 0.7,
         "step": 0.1, "min_pages": 4, "items": [
             "Cost is the purchase price plus freight and duty to the "
             "warehouse, on a first-in, first-out basis.",
             "Net realisable value is the expected selling price, net "
             "of VAT, less the cost of selling: fees, postage and "
             "returns.",
             "Lines over 12 months old are reviewed one by one; "
             "anything not expected to sell at full price is valued at "
             "its clearance price.",
         ]},
        {"heading": "Movement in the year", "kind": "figure",
         "weight": 0.8, "min_pages": 4, "height": 150, "charts": [{
             "type": "waterfall", "format": "£{:,.0f}k",
             "axis_format": "{:,.0f}", "total_color": 0,
             "steps": [("1 Feb 2027", 548), ("Purchases", 2_520),
                       ("Sold at cost", -2_443), ("Write-down",
                                                  -round(WRITE_DOWN / 1000)),
                       ("Count differences", -1),
                       ("31 Jan 2028", None)]}]},
        {"heading": "Signed off", "kind": "table", "look": "plain",
         "header": False, "whole": True, "weight": 0.9, "min_pages": 2,
         "columns": [("", 1), ("", 1)],
         "rows": [["Count supervised: Dan Pascoe, warehouse manager",
                   "Valuation: Nadia Okafor, financial controller"],
                  ["Observed by the auditor: Penhallow & Co",
                   "Date: 6 February 2028"]]},
    ],
}
