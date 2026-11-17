"""Work in Progress Schedule of Atelier Nord: the business and everything the
document could say. The typesetting keeps what fits into two pages, the most
important first."""

BUSINESS = {
    "name": "Atelier Nord",
    "author": "Atelier Nord Architects LLP, finance",
}

# project, client, stage, fee £k, % complete, billed £k, cost to date £k
PROJECTS = [
    ("AN-2318 Ashby Library", "Ashby Town Council", "4", 186.0, 0.53,
     87.4, 71.2),
    ("AN-2302 Mill Yard housing", "Mill Yard Developments", "3", 242.0,
     0.38, 72.6, 98.1),
    ("AN-2331 Kestrel offices", "Kestrel Retail Group", "2", 128.0, 0.16,
     12.8, 22.4),
    ("AN-2290 Sandhill School", "East Riding Council", "5", 310.0, 0.71,
     214.0, 168.9),
    ("AN-2324 Harbour House", "Private client", "2", 64.0, 0.22, 6.4,
     17.6),
    ("AN-2276 St Mary's Chapel", "Diocese of York", "6", 88.0, 0.94, 82.7,
     71.0),
    ("AN-2335 Ferry Terminal study", "Hull Port Authority", "1", 36.0,
     0.40, 0.0, 12.8),
]


def k(value):
    return f"({-value:,.1f})" if value < 0 else f"{value:,.1f}"


ROWS = []
for name, client, stage, fee, done, billed, cost in PROJECTS:
    earned = fee * done
    wip = earned - billed
    margin = earned - cost
    ROWS.append((name, client, stage, fee, done, earned, billed, wip,
                 cost, margin))
T = [sum(r[i] for r in ROWS) for i in (3, 5, 6, 7, 8, 9)]

DOCUMENT = {
    "title": "Work in Progress Schedule",
    "subtitle": "Unbilled fees and project margins at the quarter end, "
                "30 September 2027 · £ thousands",
    "meta": [("Projects", str(len(ROWS))), ("Fees", f"£{T[0]:,.0f}k"),
             ("Earned", f"£{T[1]:,.1f}k"),
             ("Unbilled WIP", f"£{T[3]:,.1f}k"),
             ("Margin to date", f"{T[5] / T[1]:.0%}")],
    "sections": [
        {"heading": "Schedule", "kind": "table", "whole": True,
         "weight": 0.1,
         "badges": {"(6.1)": "bad", "(1.9)": "bad", "(3.5)": "bad"},
         "columns": [("Project", 2.2), ("Client", 1.8),
                     ("Stage", 0.5, "center"), ("Fee", 0.8, "end"),
                     ("Complete", 0.8, "end"), ("Earned", 0.8, "end"),
                     ("Billed", 0.8, "end"), ("WIP", 0.8, "end"),
                     ("Cost", 0.8, "end"), ("Margin", 0.8, "end")],
         "rows": [[n, c, s, k(f), f"{d:.0%}", k(e), k(b), k(w), k(co),
                   k(m)] for n, c, s, f, d, e, b, w, co, m in ROWS]
         + [{"cells": ["Total", "", "", k(T[0]), "", k(T[1]), k(T[2]),
                       k(T[3]), k(T[4]), k(T[5])], "style": "total"}]},
        {"heading": "Earned, billed and unbilled", "kind": "figure",
         "weight": 0.2, "min_pages": 2, "height": 170, "widths": [3, 2],
         "charts": [
             {"type": "bars", "horizontal": True, "stacked": True,
              "values": False, "format": "£{:,.0f}k",
              "categories": [r[0].split(" ", 1)[1] for r in ROWS],
              "series": [{"name": "Billed", "values": [r[6]
                                                       for r in ROWS]},
                         {"name": "Unbilled", "color": 1,
                          "values": [max(r[7], 0) for r in ROWS]},
                         {"name": "Still to earn", "color": 4,
                          "values": [r[3] - r[5] for r in ROWS]}]},
             {"type": "quadrant", "title": "Margin and progress",
              "x": "% complete", "y": "margin",
              "quadrants": ["Early winners", "Healthy",
                            "Watch closely", "Losing money"],
              "points": [(r[0].split(" ", 1)[1].split()[0],
                          r[4] * 10, max(min(5 + r[9] / r[5] * 12, 9.5),
                                         0.5),
                          "bad" if r[9] < 0 else 0) for r in ROWS]},
         ]},
        {"kind": "callout", "weight": 0.3, "tone": "bad",
         "label": "Three projects are under water:",
         "text": "Mill Yard has £98k of cost against £92k earned at "
                 "stage 3, after the client changed the brief twice; a "
                 "claim for additional fees of £38k was sent on 22 "
                 "September. Kestrel and Harbour House are early-stage "
                 "and should recover as the design settles."},
        {"heading": "Aging of unbilled work", "kind": "figure",
         "weight": 0.5, "min_pages": 4, "height": 150, "charts": [{
             "type": "bars", "stacked": True, "format": "£{:,.0f}k",
             "subtitle": "£k unbilled, by how long ago the work was done",
             "categories": ["Under 30 days", "30 – 60 days",
                            "60 – 90 days", "Over 90 days"],
             "series": [{"name": "Unbilled", "values": [34.1, 19.8, 7.6,
                                                        4.9],
                         "colors": ["good", 0, "warn", "bad"]}]}]},
        {"heading": "Provisions", "kind": "table", "whole": True,
         "weight": 0.6, "min_pages": 4,
         "columns": [("Project", 2.4), ("Risk", 3.2),
                     ("Provision £k", 1, "end")],
         "rows": [["AN-2302 Mill Yard housing", "Additional fees may not "
                   "be agreed", "(9.0)"],
                  ["AN-2335 Ferry Terminal study", "Billed only on "
                   "acceptance of the report", "(2.0)"],
                  {"cells": ["Total provision", "", "(11.0)"],
                   "style": "total"}]},
        {"heading": "Billing plan", "kind": "table", "whole": True,
         "weight": 0.7, "min_pages": 4,
         "columns": [("Project", 2.4), ("October", 1, "end"),
                     ("November", 1, "end"), ("December", 1, "end")],
         "rows": [["AN-2318 Ashby Library", "13.8", "9.3", "9.3"],
                  ["AN-2290 Sandhill School", "12.1", "12.4", "11.8"],
                  ["AN-2302 Mill Yard housing", "19.4", "8.0", "8.0"],
                  ["AN-2276 St Mary's Chapel", "", "", "5.3"],
                  ["Others", "8.6", "6.9", "7.2"],
                  {"cells": ["Total", "53.9", "36.6", "41.6"],
                   "style": "total"}]},
        {"heading": "Recovery", "kind": "figure", "weight": 0.8,
         "min_pages": 4, "charts": [{"type": "gauges", "items": [
             {"label": "Fee earned per £1 of cost",
              "value": T[1] / T[4], "max": 2, "target": 1.25,
              "status": "good", "display": f"£{T[1] / T[4]:.2f}"},
             {"label": "WIP days", "value": 34, "max": 90, "target": 30,
              "status": "warn", "display": "34"},
             {"label": "Projects in loss", "value": 3, "max": 7,
              "status": "bad", "display": "3 of 7"}]}]},
        {"heading": "Method", "kind": "text", "weight": 0.9, "step": 0.3,
         "min_pages": 2, "paragraphs": [
             "Fees are earned as each RIBA stage progresses, measured by "
             "the project architect's estimate of completion checked "
             "against the drawings issued. Work in progress is the fee "
             "earned less the fee billed; costs are timesheet hours at "
             "cost rates (salary and overhead) plus direct expenses.",
         ]},
    ],
}
