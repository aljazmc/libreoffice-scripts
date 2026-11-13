"""R&D Tax Credit Claim of Lumen Analytics: the business and everything the
document could say. The typesetting keeps what fits into one page, the most
important first."""

BUSINESS = {
    "name": "Lumen Analytics",
    "author": "Lumen Analytics Ltd (UK subsidiary), with Fenwick Tax LLP",
}


def gbp(value):
    return f"£{value:,.0f}"


# qualifying cost categories: total cost, share that is R&D
COSTS = [("Staff costs: salaries, NIC, pension", 1_412_000, 0.72),
         ("External workers, counted at 65 %", 186_000, 0.80),
         ("Subcontracted R&D (connected)", 0, 0.0),
         ("Software licences", 64_000, 0.55),
         ("Cloud computing and data", 238_000, 0.61),
         ("Consumables", 9_000, 0.40)]
QUALIFYING = [(name, cost, share, round(cost * share)) for name, cost,
              share in COSTS]
EXTERNAL_CAP = 0.65  # externally provided workers count at 65 %
QUALIFYING[1] = (QUALIFYING[1][0], QUALIFYING[1][1], QUALIFYING[1][2],
                 round(QUALIFYING[1][3] * EXTERNAL_CAP))
TOTAL_QE = sum(q[3] for q in QUALIFYING)
RATE = 0.20  # merged scheme expenditure credit
CREDIT = round(TOTAL_QE * RATE)
TAX = round(CREDIT * 0.25)  # the notional tax deduction
NET = CREDIT - TAX

PROJECTS = [("P1", "Probabilistic demand engine", 0.46),
            ("P2", "Store-level reconciliation of forecasts", 0.31),
            ("P3", "Explainability of forecast drivers", 0.23)]

DOCUMENT = {
    "title": "R&D Tax Credit Claim",
    "eyebrow": "Lumen Analytics Ltd · company 12950431",
    "subtitle": "Merged R&D expenditure credit for the accounting period "
                "1 January to 31 December 2026",
    "meta": [("Period", "FY 2026"), ("Scheme", "Merged RDEC"),
             ("Qualifying spend", gbp(TOTAL_QE)),
             ("Credit, net", gbp(NET)), ("Form", "CT600 box 650")],
    "sections": [
        {"heading": "A · Qualifying expenditure", "kind": "table",
         "whole": True, "weight": 0.1,
         "columns": [("Category", 3), ("Total cost", 1, "end"),
                     ("R&D share", 0.8, "end"),
                     ("Qualifying", 1, "end")],
         "rows": [[name, gbp(cost), f"{share:.0%}", gbp(q)]
                  for name, cost, share, q in QUALIFYING]
         + [{"cells": ["Total qualifying expenditure", "", "",
                       gbp(TOTAL_QE)], "style": "total"}]},
        {"heading": "B · Credit calculation", "kind": "table",
         "whole": True, "weight": 0.2,
         "columns": [("Line", 0.6), ("Description", 3.6),
                     ("Amount", 1, "end")],
         "rows": [["B1", "Qualifying expenditure (from A)", gbp(TOTAL_QE)],
                  ["B2", "Expenditure credit at 20 %", gbp(CREDIT)],
                  ["B3", "Less notional tax at 25 %", f"({gbp(TAX)})"],
                  {"cells": ["B4", "Net credit claimed", gbp(NET)],
                   "style": "total"},
                  ["B5", "Set against corporation tax due", "£0"],
                  ["B6", "Payable credit, to bank account", gbp(NET)]]},
        {"heading": "C · Declaration", "kind": "callout", "weight": 0.3,
         "tone": "accent", "label": "I declare",
         "text": "that the information in this claim is correct and "
                 "complete to the best of my knowledge, and that the "
                 "additional information form was submitted on 2 March "
                 "2027. — Elena Marsh, director"},
        {"heading": "D · Projects", "kind": "table", "weight": 0.4,
         "whole": True, "min_pages": 2,
         "columns": [("No.", 0.5), ("Project", 2.8),
                     ("Share of costs", 1, "end"),
                     ("Qualifying", 1, "end")],
         "rows": [[code, name, f"{share:.0%}", gbp(TOTAL_QE * share)]
                  for code, name, share in PROJECTS]},
        {"heading": "E · Costs by category", "kind": "figure",
         "weight": 0.5, "min_pages": 2, "height": 150, "widths": [3, 2],
         "charts": [
             {"type": "bars", "horizontal": True, "format": "£{:,.0f}k",
              "title": "Total cost and qualifying part",
              "categories": [q[0].split(":")[0].split(" (")[0]
                             for q in QUALIFYING if q[1]],
              "stacked": False,
              "series": [{"name": "Total cost", "color": 4,
                          "values": [q[1] / 1000 for q in QUALIFYING
                                     if q[1]]},
                         {"name": "Qualifying",
                          "values": [q[3] / 1000 for q in QUALIFYING
                                     if q[1]]}]},
             {"type": "donut", "title": "Qualifying by project",
              "segments": [(code, TOTAL_QE * share / 1000)
                           for code, _, share in PROJECTS],
              "format": "£{:,.0f}k", "center": (f"£{TOTAL_QE / 1e6:.2f}m",
                                                "qualifying")},
         ]},
        {"heading": "F · How staff time was apportioned", "kind": "table",
         "weight": 0.6, "step": 0.05, "min_pages": 2,
         "columns": [("Role", 2), ("People", 0.7, "end"),
                     ("R&D time", 0.9, "end"), ("Evidence", 2.6)],
         "rows": [
             ["Machine learning engineers", "6", "90 %", "Sprint tickets "
              "tagged by project"],
             ["Data engineers", "4", "70 %", "Timesheets, monthly"],
             ["Backend engineers", "5", "60 %", "Sprint tickets tagged by "
              "project"],
             ["Engineering managers", "2", "40 %", "Interviews and "
              "calendars"],
             ["Product and design", "4", "15 %", "Interviews only"],
         ]},
        {"heading": "G · Technical narrative", "kind": "entries",
         "weight": 0.7, "step": 0.2, "inner": 0.1, "min_pages": 4,
         "entries": [
             {"title": "P1 · Probabilistic demand engine", "fields": [
                 ("Advance sought", "forecasts with calibrated "
                                    "uncertainty for 400,000 store and "
                                    "product series, recomputed nightly"),
                 ("Uncertainty", "whether hierarchical models could be "
                                 "fitted at that scale within a six-hour "
                                 "window was not known to a competent "
                                 "professional"),
                 ("Work done", "four model families tested; a new "
                               "sampling method cut the fitting time from "
                               "31 to 4.5 hours")]},
             {"title": "P2 · Store-level reconciliation", "fields": [
                 ("Advance sought", "forecasts that add up across "
                                    "stores, regions and the warehouse "
                                    "without losing accuracy"),
                 ("Uncertainty", "published reconciliation methods "
                                 "degrade badly for intermittent "
                                 "demand")]},
             {"title": "P3 · Explainability", "fields": [
                 ("Advance sought", "a breakdown of every forecast into "
                                    "drivers a planner understands"),
                 ("Status", "ongoing; costs after September are excluded "
                            "as the remaining work is routine")]},
         ]},
        {"heading": "H · Claims history", "kind": "figure", "weight": 0.8,
         "min_pages": 4, "height": 140, "charts": [{"type": "bars",
          "title": "Net credit by year", "subtitle": "£k",
          "format": "{:,.0f}", "categories": ["2022", "2023", "2024",
                                              "2025", "2026"],
          "series": [{"name": "Claimed", "values": [61, 118, 164, 189,
                                                    NET / 1000],
                      "colors": [4, 4, 4, 4, 0]}]}]},
        {"heading": "I · Checks before filing", "kind": "table",
         "weight": 0.9, "whole": True, "min_pages": 4,
         "badges": {"Done": "good", "N/A": "neutral"},
         "columns": [("Check", 4), ("Status", 0.8, "center")],
         "rows": [["Claim notification filed within 6 months of period "
                   "end", "N/A"],
                  ["Additional information form submitted", "Done"],
                  ["Grants and subsidised costs excluded", "Done"],
                  ["Overseas workers excluded (from April 2024 rules)",
                   "Done"],
                  ["PAYE and NIC cap tested", "Done"],
                  ["Director's sign-off", "Done"]]},
        {"heading": "J · Monthly qualifying cost", "kind": "figure",
         "weight": 1.0, "min_pages": 4, "height": 150, "charts": [{
             "type": "bars", "stacked": True, "subtitle": "£k",
             "format": "{:,.0f}", "values": False,
             "categories": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
             "series": [{"name": "P1", "values": [52, 54, 51, 53, 50, 49,
                                                  48, 47, 46, 45, 44, 58]},
                        {"name": "P2", "color": 1,
                         "values": [28, 30, 32, 34, 35, 36, 35, 34, 33, 34,
                                    35, 36]},
                        {"name": "P3", "color": 2,
                         "values": [20, 22, 24, 26, 28, 30, 31, 33, 34, 0,
                                    0, 0]}]}]},
        {"heading": "K · Records kept", "kind": "bullets", "weight": 1.1,
         "step": 0.1, "min_pages": 4, "items": [
             "Payroll reports by employee and month, reconciled to the "
             "PAYE submissions.",
             "Sprint boards exported monthly, with every ticket tagged "
             "P1, P2, P3 or none.",
             "Cloud invoices split by project tag in the billing "
             "console.",
             "Contracts with the two external workers' agencies.",
         ]},
        {"heading": "L · Adviser's note", "kind": "text", "weight": 1.2,
         "step": 0.3, "min_pages": 4, "paragraphs": [
             "We have reviewed the projects against the government's "
             "guidelines on the meaning of R&D. P1 and P2 sought an "
             "advance in the overall knowledge of forecasting at scale, "
             "not only in Lumen's own product, and the uncertainties "
             "were real: two of the four approaches tried in P1 failed.",
             "Software licences and cloud costs are apportioned by the "
             "share of compute and usage tagged to the projects, not by "
             "headcount. Costs of routine maintenance, bug fixing and "
             "the commercial roll-out of finished features are "
             "excluded. — Fenwick Tax LLP",
         ]},
        {"heading": "M · Effect on cash", "kind": "figure",
         "weight": 1.3, "min_pages": 4, "charts": [{"type": "kpis",
          "tiles": [
              {"label": "Credit, gross", "value": f"£{CREDIT / 1000:.0f}k",
               "status": 0, "note": "20 % of qualifying spend"},
              {"label": "Credit, net", "value": f"£{NET / 1000:.0f}k",
               "status": "good", "note": "paid in cash"},
              {"label": "Months of UK payroll", "value": "1.7",
               "status": 1, "note": "covered by the credit"},
              {"label": "Expected", "value": "Jun 2027", "status": 2,
               "note": "about 40 days after filing"}]}]},
    ],
}
