"""Grant Expenditure Report of Open Shelf Library Trust: the business and
everything the document could say. The typesetting keeps what fits into four
pages, the most important first."""

BUSINESS = {
    "name": "Open Shelf Library Trust",
    "author": "Sophie Marlowe, director",
}

# budget line, year 2 budget, year 2 actual (£)
LINES = [("Reading room coordinators, 2 × 0.8 FTE", 58_000, 56_000),
         ("Books and digital subscriptions", 14_000, 12_400),
         ("Furniture and fit-out, Westfield room", 22_000, 5_800),
         ("Volunteer training and expenses", 6_000, 4_600),
         ("Events and author visits", 8_000, 3_400),
         ("Independent evaluation", 7_000, 7_200),
         ("Contribution to running costs (10 %)", 5_000, 0)]
CARRIED = 18_400
RECEIVED = 120_000

BUDGET = sum(line[1] for line in LINES)
ACTUAL = sum(line[2] for line in LINES)


def gbp(value):
    sign = "−" if value < 0 else ""
    return f"{sign}£{abs(value):,}"


DOCUMENT = {
    "title": "Grant Expenditure Report",
    "eyebrow": "Open Shelf Library Trust · for the Northfield Foundation",
    "subtitle": "Reading Rooms grant NF-2025-031 · year 2 of 3 · 1 April "
                "2026 to 31 March 2027",
    "meta": [("Grant", "NF-2025-031"), ("Year", "2 of 3"),
             ("Budget", gbp(BUDGET)), ("Spent", gbp(ACTUAL)),
             ("To carry forward", gbp(CARRIED + RECEIVED - ACTUAL))],
    "sections": [
        {"kind": "figure", "weight": 0.1, "charts": [{"type": "kpis",
         "tiles": [
             {"label": "Visits", "value": "18,640", "status": 0,
              "note": "target 15,000", "delta": "+24 %"},
             {"label": "Children's sessions", "value": "312",
              "status": 1, "note": "target 280"},
             {"label": "Volunteers", "value": "64", "status": 2,
              "note": "in the reading rooms"},
             {"label": "Spent", "value": f"{ACTUAL / BUDGET:.0%}",
              "status": "warn", "note": "of the year 2 budget"}]}]},
        {"heading": "Budget and actual", "kind": "table", "whole": True,
         "weight": 0.2,
         "columns": [("Budget line", 3), ("Budget", 1, "end"),
                     ("Actual", 1, "end"), ("Variance", 1, "end"),
                     ("Spent", 0.7, "end")],
         "rows": [[n, gbp(b), gbp(a), gbp(a - b), f"{a / b:.0%}"]
                  for n, b, a in LINES]
         + [{"cells": ["Total", gbp(BUDGET), gbp(ACTUAL),
                       gbp(ACTUAL - BUDGET), f"{ACTUAL / BUDGET:.0%}"],
             "style": "total"}]},
        {"heading": "Explaining the underspend", "kind": "bullets",
         "weight": 0.3, "step": 0.1, "items": [
             "**The Westfield room opens in May, not January.** The "
             "lease was signed four months late; £16,200 of fit-out "
             "moves into year 3.",
             "**Author visits cost less** because two publishers paid "
             "their authors' fees.",
             "**We did not charge the 10 % running cost contribution** "
             "this year; it will be claimed in year 3 with the "
             "foundation's agreement.",
         ]},
        {"heading": "Spending against budget", "kind": "figure",
         "weight": 0.4, "min_pages": 2, "height": 170, "charts": [{
             "type": "bars", "horizontal": True, "format": "£{:,.0f}",
             "categories": [n.split(",")[0].split(" (")[0]
                            for n, _, _ in LINES],
             "series": [{"name": "Budget", "color": 4,
                         "values": [b for _, b, _ in LINES]},
                        {"name": "Actual",
                         "values": [a for _, _, a in LINES]}]}]},
        {"heading": "Outcomes", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": 130, "charts": [{"type": "progress",
          "format": "{:.0f} %", "items": [
              {"label": "Children reading more than before", "value": 72,
               "target": 60, "status": "good",
               "note": "parents' survey, 141 answers"},
              {"label": "Adults joining the library", "value": 88,
               "target": 100, "status": "warn", "display": "438",
               "note": "target 500"},
              {"label": "Volunteers trained", "value": 100, "target": 100,
               "status": "good", "display": "64"},
              {"label": "Visitors from the target wards", "value": 61,
               "target": 50, "status": "good"}]}]},
        {"heading": "A story from Northgate", "kind": "motto",
         "weight": 0.6, "min_pages": 2,
         "text": "“My daughter didn't like reading. Now she runs to the "
                 "reading room after school and tells me the stories on "
                 "the way home.” — a parent at Northgate"},
        {"heading": "Money over the three years", "kind": "figure",
         "weight": 0.7, "min_pages": 4, "height": 150, "charts": [{
             "type": "bars", "stacked": True, "subtitle": "£k",
             "format": "{:,.0f}",
             "categories": ["Year 1", "Year 2", "Year 3 (plan)"],
             "series": [{"name": "Spent", "values": [101.6, ACTUAL / 1000,
                                                     0]},
                        {"name": "Planned", "color": 4,
                         "values": [0, 0, 137.0]}]}]},
        {"heading": "Year 3 plan", "kind": "table", "whole": True,
         "weight": 0.8, "min_pages": 4,
         "columns": [("Budget line", 3), ("Year 3 budget", 1, "end")],
         "rows": [["Reading room coordinators", "£60,000"],
                  ["Books and subscriptions", "£15,000"],
                  ["Westfield fit-out (moved from year 2)", "£22,000"],
                  ["Volunteer training", "£6,000"],
                  ["Events", "£9,000"],
                  ["Final evaluation", "£10,000"],
                  ["Running cost contribution (years 2 and 3)",
                   "£15,000"],
                  {"cells": ["Total", "£137,000"], "style": "total"}]},
        {"heading": "Visits by month", "kind": "figure", "weight": 0.9,
         "min_pages": 4, "height": 140, "charts": [{"type": "line",
          "x": ["Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov",
                "Dec", "Jan", "Feb", "Mar"], "format": "{:,.0f}",
          "series": [{"name": "Visits", "area": True,
                      "values": [1210, 1340, 1480, 1920, 2040, 1460, 1520,
                                 1580, 1340, 1460, 1580, 1710]}]}]},
        {"heading": "Lessons", "kind": "entries", "weight": 1.0,
         "step": 0.2, "inner": 0.1, "min_pages": 4, "entries": [
             {"title": "Summer is the busiest time", "text": [
                 "The reading challenge brought twice as many children in "
                 "August as in March; we will staff the rooms for it."]},
             {"title": "Volunteers need a coordinator", "text": [
                 "Rooms with a paid coordinator kept 90 % of their "
                 "volunteers; the room without one kept 60 %."]},
         ]},
        {"heading": "Certified by", "kind": "table", "look": "plain",
         "header": False, "whole": True, "weight": 1.1, "min_pages": 4,
         "columns": [("", 1), ("", 1)],
         "rows": [["Sophie Marlowe, director", "Raj Patel, treasurer"],
                  ["28 April 2027", "28 April 2027"]]},
        {"heading": "Who used the reading rooms", "kind": "figure",
         "weight": 1.2, "min_pages": 4, "height": 140, "widths": [2, 3],
         "charts": [
             {"type": "donut", "title": "Visitors by age",
              "segments": [("Under 12", 41), ("12 – 17", 14),
                           ("18 – 64", 31), ("65 and over", 14)],
              "format": "{:.0f}%", "center": ("18,640", "visits")},
             {"type": "bars", "horizontal": True, "title": "Visits by "
              "reading room", "format": "{:,.0f}",
              "categories": ["Northgate", "Westfield (pop-up)",
                             "Marfleet"],
              "series": [{"name": "Visits", "values": [9_810, 2_140,
                                                       6_690]}]},
         ]},
    ],
}
