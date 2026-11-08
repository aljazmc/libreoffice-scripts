"""Departmental Profit and Loss of Salt & Pine Hotel: the business and
everything the document could say. The typesetting keeps what fits into four
pages, the most important first."""

BUSINESS = {
    "name": "Salt & Pine Hotel",
    "author": "Salt & Pine Hotel Ltd, Marta Lindqvist, financial controller",
}


def k(value):
    return f"({-value:,.1f})" if value < 0 else f"{value:,.1f}"


# £k for August: actual, budget, last year
DEPARTMENTS = {
    "Rooms": {"revenue": (412.6, 398.0, 371.2),
              "cost": (-96.8, -94.0, -88.9)},
    "Food and beverage": {"revenue": (238.4, 245.0, 219.7),
                          "cost": (-171.2, -169.0, -158.4)},
    "Spa": {"revenue": (61.8, 58.0, 49.3),
            "cost": (-38.9, -37.5, -33.1)},
    "Other operated": {"revenue": (14.2, 12.0, 11.8),
                       "cost": (-6.1, -5.5, -5.2)},
}
UNDISTRIBUTED = [("Administration and general", (-58.4, -56.0, -54.1)),
                 ("Sales and marketing", (-41.2, -44.0, -36.8)),
                 ("Property operations and maintenance",
                  (-27.6, -25.0, -24.9)),
                 ("Utilities", (-22.9, -24.0, -26.7)),
                 ("Information and telecoms", (-9.8, -9.5, -8.6))]
FIXED = [("Rent and rates", (-48.0, -48.0, -46.5)),
         ("Insurance", (-6.4, -6.4, -6.0)),
         ("Management fee", (-21.1, -20.6, -19.0))]


def add(*tuples):
    return tuple(round(sum(v), 1) for v in zip(*tuples))


REVENUE = add(*[d["revenue"] for d in DEPARTMENTS.values()])
DEPT_PROFIT = add(*[d["revenue"] for d in DEPARTMENTS.values()],
                  *[d["cost"] for d in DEPARTMENTS.values()])
UNDIST = add(*[v for _, v in UNDISTRIBUTED])
GOP = add(DEPT_PROFIT, UNDIST)
FIX = add(*[v for _, v in FIXED])
EBITDA = add(GOP, FIX)
COLUMNS = [("£ thousands", 2.6), ("Actual", 1, "end"),
           ("Budget", 1, "end"), ("Last year", 1, "end"),
           ("vs budget", 1, "end")]


def line(name, values, style="indent"):
    return {"cells": [name] + [k(v) for v in values]
            + [k(round(values[0] - values[1], 1))], "style": style}


ROWS = [{"cells": ["Operated departments", "", "", "", ""],
         "style": "section"}]
for name, d in DEPARTMENTS.items():
    ROWS.append(line(f"{name}: revenue", d["revenue"]))
    ROWS.append(dict(line(f"{name}: expenses", d["cost"]),
                     min_pages=2))
    ROWS.append(dict(line(f"{name}: profit", add(d["revenue"],
                                                 d["cost"]), "muted"),
                     min_pages=2))
ROWS += [line("Total revenue", REVENUE, "subtotal"),
         line("Departmental profit", DEPT_PROFIT, "subtotal"),
         {"cells": ["Undistributed operating expenses", "", "", "", ""],
          "style": "section"}]
ROWS += [line(n, v) for n, v in UNDISTRIBUTED]
ROWS += [line("Gross operating profit", GOP, "highlight"),
         {"cells": ["GOP margin"] + [f"{g / r:.1%}" for g, r in
                                     zip(GOP, REVENUE)] + [""],
          "style": "muted"}]
ROWS += [line(n, v) for n, v in FIXED]
ROWS += [line("EBITDA", EBITDA, "total")]

DOCUMENT = {
    "title": "Departmental Profit and Loss",
    "subtitle": "August 2027 · Uniform System of Accounts for the Lodging "
                "Industry · 42 rooms",
    "meta": [("Month", "August 2027"), ("Revenue", f"£{REVENUE[0]:.1f}k"),
             ("GOP", f"£{GOP[0]:.1f}k"),
             ("GOP margin", f"{GOP[0] / REVENUE[0]:.1%}"),
             ("EBITDA", f"£{EBITDA[0]:.1f}k")],
    "sections": [
        {"heading": "Statement", "kind": "table", "whole": True,
         "weight": 0.1, "columns": COLUMNS, "rows": ROWS},
        {"heading": "Where the profit is made", "kind": "figure",
         "weight": 0.2, "height": {1: 150, 2: 175, 4: 190},
         "charts": [{"type": "bars", "horizontal": True, "stacked": True,
          "inside": True, "values": False, "format": "£{:,.0f}k",
          "subtitle": "revenue split into cost and profit, £k",
          "categories": list(DEPARTMENTS),
          "series": [{"name": "Departmental expenses", "color": 4,
                      "values": [-d["cost"][0]
                                 for d in DEPARTMENTS.values()]},
                     {"name": "Departmental profit", "color": 1,
                      "values": [round(d["revenue"][0] + d["cost"][0], 1)
                                 for d in DEPARTMENTS.values()]}]}]},
        {"heading": "Margins", "kind": "figure", "weight": 0.3,
         "min_pages": 2, "charts": [{"type": "gauges", "items": [
             {"label": name, "value": (d["revenue"][0] + d["cost"][0])
              / d["revenue"][0] * 100, "max": 100, "status": i,
              "display": f"{1 + d['cost'][0] / d['revenue'][0]:.0%}",
              "note": "departmental margin"}
             for i, (name, d) in enumerate(list(DEPARTMENTS.items())[:3])]
             + [{"label": "Hotel", "value": GOP[0] / REVENUE[0] * 100,
                 "max": 100, "target": 38, "status": "good",
                 "display": f"{GOP[0] / REVENUE[0]:.0%}",
                 "note": "GOP margin"}]}]},
        {"heading": "Commentary", "kind": "entries", "weight": 0.4,
         "step": 0.2, "inner": 0.1, "min_pages": 2, "entries": [
             {"title": "Rooms ahead of budget", "text": [
                 "Occupancy of 94 % at an average rate of £337; the "
                 "Saltwater Festival week sold out at £420 a night."]},
             {"title": "Food and beverage behind", "text": [
                 "Two wet weekends closed the terrace; the restaurant "
                 "made up half the gap with a second sitting."]},
             {"title": "Utilities down 14 % on last year", "text": [
                 "The heat pump for the spa pool has run a full summer "
                 "and the gas bill has halved."]},
         ]},
        {"heading": "Year to date", "kind": "figure", "weight": 0.5,
         "min_pages": 4, "height": 160, "charts": [{"type": "line",
          "subtitle": "£k per month, GOP", "format": "{:.0f}",
          "x": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"],
          "end_labels": True,
          "series": [{"name": "2027", "area": True,
                      "values": [38, 52, 89, 141, 196, 248, 281,
                                 round(GOP[0])]},
                     {"name": "Budget", "dash": True, "color": 4,
                      "values": [41, 55, 86, 133, 188, 239, 276,
                                 round(GOP[1])]},
                     {"name": "2026", "color": 2,
                      "values": [29, 44, 77, 120, 171, 221, 256,
                                 round(GOP[2])]}]}]},
        {"heading": "Payroll by department", "kind": "table",
         "whole": True, "weight": 0.6, "min_pages": 4,
         "columns": [("Department", 2.4), ("Staff", 0.8, "end"),
                     ("Cost £k", 1, "end"),
                     ("% of revenue", 1, "end")],
         "rows": [["Rooms", "18", "61.4", "14.9 %"],
                  ["Food and beverage", "34", "104.8", "44.0 %"],
                  ["Spa", "9", "27.2", "44.0 %"],
                  ["Administration, sales, maintenance", "11", "52.6",
                   "7.2 %"],
                  {"cells": ["Hotel", "72", "246.0", "33.8 %"],
                   "style": "total"}]},
        {"heading": "Key ratios", "kind": "table", "whole": True,
         "weight": 0.7, "min_pages": 4,
         "badges": {"Better": "good", "Worse": "bad"},
         "columns": [("Ratio", 2.4), ("Actual", 1, "end"),
                     ("Budget", 1, "end"), ("", 0.9, "center")],
         "rows": [["Occupancy", "94.1 %", "92.0 %", "Better"],
                  ["Average daily rate", "£337", "£332", "Better"],
                  ["RevPAR", "£317", "£306", "Better"],
                  ["Food cost", "29.4 %", "28.0 %", "Worse"],
                  ["Beverage cost", "22.1 %", "23.0 %", "Better"],
                  ["Covers in the restaurant", "4,210", "4,400",
                   "Worse"]]},
        {"heading": "Notes", "kind": "text", "weight": 0.8, "step": 0.3,
         "min_pages": 4, "paragraphs": [
             "Departmental expenses include the payroll, cost of sales "
             "and direct costs of each department. Undistributed "
             "expenses support the whole hotel and are not charged to "
             "departments. Figures in brackets are costs; the variance "
             "column is actual less budget.",
         ]},
        {"heading": "Undistributed costs", "kind": "figure",
         "weight": 0.9, "min_pages": 4, "height": 150, "charts": [{
             "type": "bars", "horizontal": True, "format": "£{:,.1f}k",
             "categories": [n for n, _ in UNDISTRIBUTED],
             "series": [{"name": "Budget", "color": 4,
                         "values": [-v[1] for _, v in UNDISTRIBUTED]},
                        {"name": "Actual", "values": [
                            -v[0] for _, v in UNDISTRIBUTED]}]}]},
        {"heading": "Revenue per guest", "kind": "figure",
         "weight": 1.0, "min_pages": 4, "charts": [{"type": "kpis",
          "tiles": [
              {"label": "Per occupied room", "value": "£591",
               "status": 0, "note": "all departments"},
              {"label": "Food and drink per guest", "value": "£102",
               "status": 1, "note": "per night"},
              {"label": "Spa capture", "value": "21 %", "status": 2,
               "note": "of guests book a treatment"},
              {"label": "Guest rating", "value": "9.3", "status": "good",
               "note": "of 10, 214 reviews"}]}]},
    ],
}
