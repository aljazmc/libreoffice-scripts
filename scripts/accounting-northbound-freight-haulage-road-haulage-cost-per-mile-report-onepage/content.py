"""Cost per Mile of Northbound Freight: the business and everything the
document could say. The typesetting keeps what fits into one page, the most
important first."""

BUSINESS = {
    "name": "Northbound Freight",
    "author": "Raj Mehta, finance director",
}

MILES = 2_412_000            # loaded and empty miles, the whole fleet
# cost line, £ for the year, fixed or variable
COSTS = [("Drivers' wages and expenses", 1_486_200, "Variable"),
         ("Diesel and AdBlue", 1_126_400, "Variable"),
         ("Tyres, repairs and maintenance", 286_900, "Variable"),
         ("Tolls, ferries and crossings", 114_300, "Variable"),
         ("Depreciation", 231_600, "Fixed"),
         ("Finance interest", 43_800, "Fixed"),
         ("Insurance", 138_400, "Fixed"),
         ("Yard, office and transport managers", 320_600, "Fixed"),
         ("Telematics and other", 61_410, "Fixed")]
REVENUE = 4_408_500 - 298_700   # own fleet revenue, without subcontract
TOTAL = sum(c[1] for c in COSTS)


def ppm(value):
    return f"£{value / MILES:.3f}"


# customer, revenue per mile, empty running %
CUSTOMERS = [("Pennine Foods (chilled)", 1.94, 0.18),
             ("Harrow Building Supplies", 1.71, 0.31),
             ("Medway Foods", 1.62, 0.34),
             ("Northern Paper Mills", 1.88, 0.12),
             ("Spot work (load boards)", 1.58, 0.27)]

DOCUMENT = {
    "title": "Cost per Mile",
    "eyebrow": "NORTHBOUND FREIGHT · FLEET ECONOMICS",
    "subtitle": "Year to 31 March 2028 · 30 tractor units, 2.41 million "
                "miles",
    "meta": [("Miles", f"{MILES:,}"), ("Cost per mile", ppm(TOTAL)),
             ("Revenue per mile", ppm(REVENUE)),
             ("Margin per mile", ppm(REVENUE - TOTAL)),
             ("Trucks", "30")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "charts": [{"type": "kpis",
         "tiles": [
             {"label": "Cost per mile", "value": ppm(TOTAL), "status": 0,
              "delta": "+4.1p", "delta_status": "bad",
              "spark": [1.52, 1.55, 1.57, 1.58, 1.60, TOTAL / MILES]},
             {"label": "Revenue per mile", "value": ppm(REVENUE),
              "status": 1, "delta": "+5.3p"},
             {"label": "Empty miles", "value": "24 %", "status": "warn",
              "note": "target 20 %"},
             {"label": "Fuel per mile", "value": ppm(COSTS[1][1]),
              "status": 2, "note": "8.6 mpg fleet average"}]}]},
        {"heading": "What a mile costs", "kind": "table", "whole": True,
         "weight": 0.2, "badges": {"Fixed": "info", "Variable": "warn"},
         "columns": [("Cost", 2.8), ("Year", 1.1, "end"),
                     ("Per mile", 0.9, "end"), ("Share", 0.7, "end"),
                     ("Type", 0.9, "center")],
         "rows": [[n, f"£{v:,.0f}", ppm(v), f"{v / TOTAL:.0%}", t]
                  for n, v, t in COSTS]
         + [{"cells": ["Total", f"£{TOTAL:,.0f}", ppm(TOTAL), "100%", ""],
             "style": "total"}]},
        {"heading": "A mile, broken down", "kind": "figure",
         "weight": 0.3, "height": {1: 120, 2: 140, 4: 150}, "charts": [{
             "type": "bars", "horizontal": True, "stacked": True,
             "inside": True, "format": "{:.0f}p", "values": False,
             "categories": ["Cost per mile"],
             "series": [{"name": n.split(" and")[0].split(",")[0],
                         "color": i if i < 5 else 4,
                         "values": [round(v / MILES * 100, 1)]}
                        for i, (n, v, _) in enumerate(COSTS)]}]},
        {"heading": "By truck", "kind": "figure", "weight": 0.4,
         "min_pages": 2, "height": 170, "charts": [{"type": "bars",
          "title": "Cost per mile by truck age", "subtitle": "£",
          "format": "{:.2f}", "axis_format": "{:.1f}",
          "target": REVENUE / MILES, "target_label": "revenue per mile",
          "categories": ["2028 units", "2026", "2025", "2023", "2021",
                         "2019"],
          "series": [{"name": "Cost per mile", "values": [1.58, 1.61,
                                                          1.64, 1.69,
                                                          1.77, 1.86],
                      "colors": ["good", "good", 0, 0, "warn",
                                 "bad"]}]}]},
        {"heading": "By customer", "kind": "table", "whole": True,
         "weight": 0.5, "min_pages": 2,
         "badges": {"Keep": "good", "Reprice": "warn", "Review": "bad"},
         "columns": [("Customer", 2.4), ("Revenue per loaded mile", 1.2,
                                         "end"),
                     ("Empty running", 1, "end"),
                     ("Revenue per mile run", 1.2, "end"),
                     ("", 0.9, "center")],
         "rows": [[c, f"£{r:.2f}", f"{e:.0%}", f"£{r * (1 - e):.2f}",
                   "Keep" if r * (1 - e) > TOTAL / MILES else "Reprice"
                   if r * (1 - e) > 1.1 else "Review"]
                  for c, r, e in CUSTOMERS]},
        {"heading": "Trend", "kind": "figure", "weight": 0.6,
         "min_pages": 2, "height": 150, "charts": [{"type": "line",
          "subtitle": "£ per mile by quarter",
          "x": ["Q1 26", "Q2", "Q3", "Q4", "Q1 27", "Q2", "Q3", "Q4"],
          "format": "{:.2f}", "zero": False, "end_labels": True,
          "series": [{"name": "Revenue", "values": [1.58, 1.60, 1.62,
                                                    1.63, 1.66, 1.68,
                                                    1.69, 1.71]},
                     {"name": "Cost", "color": "bad",
                      "values": [1.50, 1.52, 1.53, 1.55, 1.57, 1.59,
                                 1.60, round(TOTAL / MILES, 2)]}]}]},
        {"heading": "Actions", "kind": "entries", "weight": 0.7,
         "step": 0.2, "inner": 0.1, "min_pages": 4, "entries": [
             {"title": "Back-loads for Harrow and Medway", "text": [
                 "A third of their miles run empty. Two back-load "
                 "partners in Kent would cut empty running to 20 % and "
                 "add about 6p per mile."]},
             {"title": "Replace the 2019 trucks first", "text": [
                 "At 28p a mile more than the new units, the three 2019 "
                 "trucks cost £70,000 a year more to run."]},
             {"title": "Reprice Medway Foods", "text": [
                 "The contract renews in June; at today's rates every "
                 "mile for them loses money."]},
         ]},
        {"heading": "Fixed and variable", "kind": "figure",
         "weight": 0.8, "min_pages": 4, "height": 140, "charts": [{
             "type": "donut", "format": "£{:,.0f}k",
             "segments": [("Variable", round(sum(
                 v for _, v, t in COSTS if t == "Variable") / 1000)),
                          ("Fixed", round(sum(
                              v for _, v, t in COSTS if t == "Fixed")
                              / 1000))],
             "center": (ppm(TOTAL), "a mile")}]},
        {"heading": "How it is measured", "kind": "text", "weight": 0.9,
         "step": 0.3, "min_pages": 4, "paragraphs": [
             "Miles come from the telematics of each truck, loaded and "
             "empty. Costs come from the ledger for the year, without "
             "subcontracted haulage, which is charged per job. Revenue "
             "per mile is the own-fleet revenue divided by all miles "
             "run, so empty miles lower it.",
         ]},
        {"heading": "Loaded and empty", "kind": "figure", "weight": 1.0,
         "min_pages": 4, "height": 150, "charts": [{"type": "bars",
          "stacked": True, "subtitle": "thousand miles per month",
          "format": "{:,.0f}", "values": False,
          "categories": ["Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct",
                         "Nov", "Dec", "Jan", "Feb", "Mar"],
          "series": [{"name": "Loaded", "values": [152, 155, 158, 149,
                                                   146, 154, 160, 162,
                                                   141, 147, 150, 159]},
                     {"name": "Empty", "color": "warn",
                      "values": [49, 48, 50, 47, 46, 49, 50, 52, 45, 47,
                                 48, 49]}]}]},
        {"heading": "What 1p a mile is worth", "kind": "table",
         "whole": True, "weight": 1.1, "min_pages": 4,
         "columns": [("Change", 3), ("Effect on profit", 1.2, "end")],
         "rows": [["1p a mile less cost", f"+£{MILES / 100:,.0f}"],
                  ["1 mpg better fuel economy", "+£126,000"],
                  ["Empty running from 24 % to 20 %", "+£148,000"],
                  ["2 % rate rise on contract work", "+£68,000"]]},
        {"heading": "Benchmarks", "kind": "figure", "weight": 1.2,
         "min_pages": 4, "charts": [{"type": "gauges", "items": [
             {"label": "Cost per mile", "value": TOTAL / MILES,
              "min": 1.2, "max": 2.0, "target": 1.62, "status": "good",
              "display": ppm(TOTAL), "note": "industry £1.62"},
             {"label": "Fuel economy", "value": 8.6, "min": 6, "max": 11,
              "target": 8.4, "status": "good", "display": "8.6 mpg",
              "note": "industry 8.4"},
             {"label": "Empty running", "value": 24, "max": 40,
              "target": 20, "status": "warn", "display": "24 %",
              "note": "industry 22 %"}]}]},
        {"heading": "Assumptions", "kind": "bullets", "weight": 1.3,
         "step": 0.1, "min_pages": 4, "items": [
             "Drivers' wages include overtime, night-out allowances and "
             "employer's National Insurance.",
             "Depreciation is straight line over seven years; the new "
             "units cost more but use 6 % less fuel.",
             "Yard and office costs are shared over all miles, not by "
             "truck.",
         ]},
    ],
}
