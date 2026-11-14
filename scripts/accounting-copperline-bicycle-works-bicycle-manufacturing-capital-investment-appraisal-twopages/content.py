"""Capital Investment Appraisal of Copperline Bicycle Works: the business and
everything the document could say. The typesetting keeps what fits into two
pages, the most important first."""

BUSINESS = {
    "name": "Copperline Bicycle Works",
    "author": "Ruth Sandell, finance director",
}

INVESTMENT = 286_000          # robotic welding cell, installed
RATE = 0.09                   # cost of capital
YEARS = 7
SALVAGE = 30_000
# yearly cash savings and extra contribution £, years 1 – 7
LABOUR_SAVED = [62_000, 66_000, 68_000, 70_000, 72_000, 74_000, 76_000]
EXTRA_BIKES = [18_000, 36_000, 48_000, 52_000, 54_000, 54_000, 54_000]
RUNNING = [-14_000, -16_000, -16_500, -17_000, -18_000, -18_500, -19_000]

FLOWS = [-INVESTMENT] + [round(a + b + c) for a, b, c in
                         zip(LABOUR_SAVED, EXTRA_BIKES, RUNNING)]
FLOWS[-1] += SALVAGE


def npv(rate, flows):
    return sum(f / (1 + rate) ** i for i, f in enumerate(flows))


def irr(flows):
    low, high = -0.9, 1.0
    for _ in range(100):
        mid = (low + high) / 2
        if npv(mid, flows) > 0:
            low = mid
        else:
            high = mid
    return mid


NPV = npv(RATE, FLOWS)
IRR = irr(FLOWS)
CUMULATIVE = []
total = 0
for f in FLOWS:
    total += f
    CUMULATIVE.append(total)
PAYBACK = next(i - 1 + -CUMULATIVE[i - 1] / FLOWS[i]
               for i in range(1, len(FLOWS)) if CUMULATIVE[i] >= 0)


def kk(value):
    """Thousands of pounds, negatives in brackets."""
    return (f"({-value / 1000:,.1f})" if value < 0
            else f"{value / 1000:,.1f}")


def gbp(value):
    sign = "−" if value < 0 else ""
    return f"{sign}£{abs(value):,.0f}"


DOCUMENT = {
    "title": "Capital Investment Appraisal",
    "subtitle": "A robotic TIG welding cell for the Harbour city frames · "
                "for the board, February 2028",
    "meta": [("Investment", gbp(INVESTMENT)), ("NPV at 9 %", gbp(NPV)),
             ("IRR", f"{IRR:.1%}"), ("Payback", f"{PAYBACK:.1f} years"),
             ("Decision", "Recommended")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "charts": [{"type": "gauges",
         "items": [
             {"label": "NPV", "value": NPV / 1000, "min": -100,
              "max": 300, "target": 0, "status": "good",
              "display": f"£{NPV / 1000:.0f}k", "note": "at 9 %"},
             {"label": "IRR", "value": IRR * 100, "max": 40,
              "target": 9, "status": "good", "display": f"{IRR:.0%}",
              "note": "hurdle 9 %"},
             {"label": "Payback", "value": PAYBACK, "max": 7,
              "target": 4, "status": 0,
              "display": f"{PAYBACK:.1f} y", "note": "limit 4 years"}]}]},
        {"heading": "Cash flows", "kind": "table", "whole": True,
         "weight": 0.2,
         "columns": [("£ thousands", 2.2)] + [(f"Y{i}", 0.8, "end")
                                   for i in range(YEARS + 1)],
         "rows": [["Investment", kk(-INVESTMENT)] + [""] * YEARS,
                  ["Labour saved", ""] + [kk(v) for v in LABOUR_SAVED],
                  ["Extra bikes, contribution", ""]
                  + [kk(v) for v in EXTRA_BIKES],
                  ["Running costs", ""] + [kk(v) for v in RUNNING],
                  ["Salvage value", ""] + [""] * (YEARS - 1)
                  + [kk(SALVAGE)],
                  {"cells": ["Net cash flow"] + [kk(f) for f in FLOWS],
                   "style": "subtotal"},
                  {"cells": ["Discounted at 9 %"] + [
                      kk(f / (1 + RATE) ** i)
                      for i, f in enumerate(FLOWS)], "style": "muted"},
                  {"cells": ["Cumulative"] + [kk(c) for c in CUMULATIVE],
                   "style": "total"}]},
        {"heading": "Payback", "kind": "figure", "weight": 0.3,
         "height": {1: 150, 2: 170, 4: 180}, "charts": [{"type": "line",
          "subtitle": "£k, cumulative cash", "format": "{:,.0f}",
          "x": [f"Y{i}" for i in range(YEARS + 1)], "zero": False,
          "target": 0, "target_label": "paid back", "end_labels": True,
          "series": [{"name": "Undiscounted", "area": True,
                      "values": [round(c / 1000) for c in CUMULATIVE]},
                     {"name": "Discounted", "color": 1, "dash": True,
                      "values": [round(sum(
                          f / (1 + RATE) ** j for j, f in
                          enumerate(FLOWS[:i + 1])) / 1000)
                          for i in range(YEARS + 1)]}]}]},
        {"heading": "Options", "kind": "table", "whole": True,
         "weight": 0.4, "min_pages": 2,
         "badges": {"Recommended": "good", "Rejected": "bad",
                    "Fallback": "warn"},
         "columns": [("Option", 2.6), ("Cost", 0.9, "end"),
                     ("NPV", 0.9, "end"), ("Verdict", 1.1, "center")],
         "rows": [["Do nothing: hire two more welders", "£0",
                   "−£96,000", "Rejected"],
                  ["Second-hand robot cell", "£164,000", "£71,000",
                   "Fallback"],
                  ["New robot cell (this proposal)", gbp(INVESTMENT),
                   gbp(NPV), "Recommended"]]},
        {"heading": "Sensitivities", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": 165, "charts": [{"type": "bars",
          "horizontal": True, "format": "£{:,.0f}k",
          "title": "NPV if…", "target": 0, "target_label": "break-even",
          "categories": ["As planned", "Extra bikes −50 %",
                         "Labour saving −25 %", "Cost +15 %",
                         "Rate 12 %", "Two years' delay in demand"],
          "series": [{"name": "NPV", "values": [
              round(NPV / 1000),
              round((NPV - npv(RATE, [0] + [b / 2 for b in EXTRA_BIKES]))
                    / 1000),
              round((NPV - npv(RATE, [0] + [a / 4 for a in
                                            LABOUR_SAVED])) / 1000),
              round((NPV - INVESTMENT * 0.15) / 1000),
              round(npv(0.12, FLOWS) / 1000),
              round((NPV - npv(RATE, [0] + [EXTRA_BIKES[0], EXTRA_BIKES[
                  1]] + [0] * 5) * 0.6) / 1000)],
              "colors": ["good", 0, 0, 0, 0, "warn"]}]}]},
        {"heading": "Why invest", "kind": "bullets", "weight": 0.6,
         "step": 0.1, "min_pages": 2, "items": [
             "**Harbour city frames** are simple, repeated welds: the "
             "robot does them in 40 minutes instead of 150.",
             "**Our brazers move to the Ridgeline and custom frames**, "
             "where their skill earns the most.",
             "**Capacity** rises by 600 frames a year without a second "
             "shift.",
         ]},
        {"heading": "Risks", "kind": "table", "whole": True,
         "weight": 0.7, "min_pages": 4,
         "badges": {"High": "bad", "Medium": "warn", "Low": "good"},
         "columns": [("Risk", 3), ("Level", 0.8, "center"),
                     ("Response", 3)],
         "rows": [["Demand for Harbour bikes falls", "Medium",
                   "The cell can weld trailer and cargo frames for "
                   "others"],
                  ["Quality of robot welds", "Low",
                   "Trial of 50 frames before acceptance"],
                  ["Staff see it as a threat", "Medium",
                   "No redundancies; two welders trained to program it"],
                  ["Supplier support", "Low",
                   "Five-year service contract priced in"]]},
        {"heading": "Financing", "kind": "figure", "weight": 0.8,
         "min_pages": 4, "height": 140, "charts": [{"type": "donut",
          "segments": [("Asset finance, 5 years", 200_000),
                       ("Cash reserves", 56_000),
                       ("Made Smarter grant", 30_000, "good")],
          "format": "£{:,.0f}", "center": (gbp(INVESTMENT),
                                           "funding")}]},
        {"heading": "Recommendation", "kind": "motto", "weight": 0.9,
         "min_pages": 4, "text": "Buy the robot cell: it pays back "
         "within the lease, frees our best brazers for our best bikes "
         "and adds 600 frames of capacity."},
        {"heading": "Frames per year", "kind": "figure", "weight": 1.0,
         "min_pages": 4, "height": 150, "charts": [{"type": "bars",
          "stacked": True, "subtitle": "capacity with the cell",
          "categories": ["2027", "2028", "2029", "2030"],
          "series": [{"name": "Brazed by hand", "values": [3420, 3100,
                                                           3200, 3300]},
                     {"name": "Robot cell", "color": 1,
                      "values": [0, 650, 900, 1000]}]}]},
        {"heading": "Assumptions", "kind": "tags", "weight": 1.1,
         "step": 0.1, "min_pages": 4, "items": [
             ("Cost of capital", "9 %, the group's hurdle rate"),
             ("Life", "seven years, £30,000 resale"),
             ("Labour saved", "1.8 welders at £34,000, rising 3 % a "
                              "year"),
             ("Extra bikes", "contribution of £90 a frame on the "
                             "added capacity"),
             ("Tax", "ignored; full expensing would improve the case"),
         ]},
        {"heading": "Discounted cash flow", "kind": "figure",
         "weight": 1.2, "min_pages": 4, "height": 150, "charts": [{
             "type": "waterfall", "format": "£{:,.0f}k",
             "axis_format": "{:,.0f}", "total_color": 0,
             "subtitle": "present value of each year at 9 %",
             "steps": [("Investment", -INVESTMENT / 1000)]
             + [(f"Y{i}", round(f / (1 + RATE) ** i / 1000))
                for i, f in enumerate(FLOWS) if i]
             + [("NPV", None)]}]},
        {"heading": "Implementation", "kind": "figure", "weight": 1.3,
         "min_pages": 4, "height": 130, "charts": [{"type": "gantt",
          "columns": ["Mar", "Apr", "May", "Jun", "Jul"],
          "tasks": [{"label": "Order and deposit", "start": 0,
                     "end": 0.3},
                    {"label": "Factory floor and power", "start": 0.5,
                     "end": 2},
                    {"label": "Install and commission", "start": 2,
                     "end": 3},
                    {"label": "Trial of 50 frames", "start": 3,
                     "end": 3.8},
                    {"label": "In production", "start": 4,
                     "milestone": True, "text": "July"}]}]},
    ],
}
