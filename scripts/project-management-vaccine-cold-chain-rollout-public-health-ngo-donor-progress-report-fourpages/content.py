"""Donor Progress Report of Cold Chain for Every Child: the project and
everything the document could say. The typesetting keeps what fits into four
pages, the most important first."""

PROJECT = {
    "name": "Cold Chain for Every Child",
    "code": "CCEC",
    "author": "Amani Mwangi, Programme Manager",
}

QUARTERS = ["Q1 25", "Q2", "Q3", "Q4", "Q1 26", "Q2", "Q3", "Q4"]

DOCUMENT = {
    "title": "Donor Progress Report",
    "subtitle": "Year 2 · January to December 2026 · for the Northfield "
                "Foundation",
    "meta": [("Programme", "CCEC"), ("Grant", "NF-2024-117"),
             ("Period", "Year 2 of 4"), ("Spent", "US$ 2.31m"),
             ("Overall", "On track")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "charts": [{"type": "kpis",
         "tiles": [
             {"label": "Fully immunised", "value": "71 %", "status": 0,
              "delta": "+13 pts", "note": "baseline 58 %"},
             {"label": "Children vaccinated", "value": "38,900",
              "status": 2, "note": "in year 2"},
             {"label": "Fridges working", "value": "187 / 212",
              "status": "good", "note": "88 %"},
             {"label": "Doses wasted", "value": "6.1 %", "status": 1,
              "delta": "▼ 8.3 pts", "delta_status": "good",
              "note": "baseline 14.4 %"},
         ]}]},
        {"heading": "Results against targets", "kind": "figure",
         "weight": 0.2, "height": {1: 165, 2: 175, 4: 185},
         "charts": [{"type": "bars", "horizontal": True,
          "format": "{:.0f}%",
          "categories": ["Fully immunised", "Facilities with fridge",
                         "Fridges without alarm", "Outreach held",
                         "On-time reports", "Caregivers who know"],
          "series": [{"name": "Year 2 target", "color": 4,
                      "values": [72, 85, 75, 80, 80, 60]},
                     {"name": "Year 2 actual", "values": [71, 88, 79, 82,
                                                          91, 58]}]}]},
        {"heading": "Spending", "kind": "figure", "weight": 0.3,
         "height": {1: 135, 2: 150}, "widths": [3, 2], "charts": [
             {"type": "line", "title": "Cumulative spend", "subtitle":
              "US$ m", "x": QUARTERS, "format": "{:.1f}",
              "series": [{"name": "Budget", "dash": True, "color": 4,
                          "values": [0.5, 1.4, 2.4, 3.1, 3.5, 3.9, 4.3,
                                     4.7]},
                         {"name": "Actual", "area": True,
                          "values": [0.4, 1.2, 2.1, 2.9, 3.4, 3.9, 4.4,
                                     4.7]}], "end_labels": True},
             {"type": "donut", "title": "Year 2 by output",
              "format": "${:,.0f}k", "center": ("$2.31m", "year 2"),
              "segments": [("Storage", 920), ("Outreach", 480),
                           ("Data", 330), ("Demand", 290),
                           ("Management", 290)]},
         ]},
        {"heading": "From the field", "kind": "motto", "weight": 0.4,
         "min_pages": 2,
         "text": "“Before the fridge came, I sent mothers to the town, two "
                 "hours on foot. Now the vaccines are here every day, and "
                 "the mothers come.” — Grace Chebet, nurse, Kiptagat "
                 "dispensary"},
        {"heading": "Highlights", "kind": "bullets", "weight": 0.5,
         "step": 0.15, "min_pages": 2, "items": [
             "**All 212 solar fridges installed**, three months ahead of "
             "plan, thanks to a second installation team from March.",
             "**Wastage halved.** Remote temperature monitors caught 41 "
             "fridge failures before any vaccine was lost.",
             "**Dry Plains district** went from 44 % to 63 % fully "
             "immunised, the largest gain of the four.",
             "**The ministry adopted our outreach planning tool** for "
             "eleven more districts.",
         ]},
        {"heading": "Coverage by district", "kind": "figure",
         "weight": 0.6, "min_pages": 2, "height": 150, "charts": [{
             "type": "bars", "format": "{:.0f}%",
             "categories": ["Baringo North", "Lake Shore",
                            "Highlands East", "Dry Plains"],
             "series": [{"name": "Baseline", "color": 4,
                         "values": [61, 66, 52, 44]},
                        {"name": "Year 1", "color": 2,
                         "values": [67, 71, 59, 54]},
                        {"name": "Year 2", "values": [74, 77, 66, 63]}],
             "target": 85, "target_label": "end target"}]},
        {"heading": "Challenges", "kind": "entries", "weight": 0.7,
         "step": 0.2, "inner": 0.1, "min_pages": 2, "entries": [
             {"title": "Caregiver knowledge lags", "text": [
                 "Radio spots reached fewer women than planned. From "
                 "January, community health workers give the schedule "
                 "card at the first antenatal visit."]},
             {"title": "Fridge repairs in Highlands East", "text": [
                 "Spare parts took up to five weeks. A spares stock now "
                 "sits at each district store."]},
             {"title": "Health worker turnover", "text": [
                 "19 % of trained staff left in the year, above the 15 % "
                 "assumption; a third person is now trained per "
                 "facility."]},
         ]},
        {"heading": "Budget against actual", "kind": "table",
         "weight": 0.8, "step": 0.1, "min_pages": 4,
         "badges": {"Under": "good", "Over": "bad", "On": "neutral"},
         "columns": [("Line", 2.4), ("Budget", 1, "end"),
                     ("Actual", 1, "end"), ("Variance", 1, "end"),
                     ("", 0.8, "center")],
         "rows": [
             ["Solar fridges and installation", "$880k", "$920k",
              "+$40k", "Over"],
             ["Motorbikes, fuel and outreach", "$520k", "$480k",
              "−$40k", "Under"],
             ["Data system and tablets", "$310k", "$330k", "+$20k",
              "Over"],
             ["Community demand", "$300k", "$290k", "−$10k", "On"],
             ["Management and M&E", "$300k", "$290k", "−$10k", "On"],
             ["Total", "$2,310k", "$2,310k", "$0k", "On"],
         ]},
        {"heading": "Wastage", "kind": "figure", "weight": 0.9,
         "min_pages": 4, "height": 150, "charts": [{"type": "line",
          "title": "Doses wasted", "subtitle": "% of doses opened",
          "x": QUARTERS, "format": "{:.0f}", "target": 5,
          "target_label": "target",
          "series": [{"name": "Wastage", "color": "bad", "area": True,
                      "values": [14.4, 12.8, 10.9, 9.6, 8.1, 7.0, 6.5,
                                 6.1]}]}]},
        {"heading": "Plan for year 3", "kind": "bullets", "weight": 1.0,
         "step": 0.2, "min_pages": 4, "items": [
             "Reach 79 % fully immunised; focus on the 61 remote "
             "villages of Highlands East.",
             "District budgets take over 25 % of fuel and maintenance.",
             "Coverage survey in October, the midline of the "
             "programme.",
             "Share the outreach tool with the eleven new districts.",
         ]},
        {"heading": "Risks", "kind": "table", "weight": 1.1, "step": 0.1,
         "min_pages": 4, "badges": {"High": "bad", "Medium": "warn",
                                    "Low": "good"},
         "columns": [("Risk", 3.4), ("Level", 0.9, "center"),
                     ("Response", 3)],
         "rows": [
             ["Districts cannot fund their share in 2027", "High",
              "Ministry letter of commitment; phased handover"],
             ["National measles vaccine shortage", "Medium",
              "Buffer stock of three months at district level"],
             ["Election period disrupts outreach", "Medium",
              "Outreach front-loaded before August"],
         ]},
        {"heading": "Thank you", "kind": "text", "weight": 1.2,
         "step": 0.3, "min_pages": 4, "paragraphs": [
             "None of this happens without the 640 health workers and "
             "community volunteers of the four districts, and the "
             "trust of the Northfield Foundation in a programme that "
             "puts its money into fridges and fuel rather than "
             "headlines.",
         ]},
        {"heading": "Equity", "kind": "figure", "weight": 1.25,
         "min_pages": 4, "height": 150, "widths": [3, 2], "charts": [
             {"type": "bars", "title": "Fully immunised by distance to "
              "a facility", "format": "{:.0f}%",
              "categories": ["Under 2 km", "2 – 5 km", "5 – 10 km",
                             "Over 10 km"],
              "series": [{"name": "Baseline", "color": 4,
                          "values": [72, 63, 49, 31]},
                         {"name": "Year 2", "values": [80, 74, 66,
                                                       52]}]},
             {"type": "progress", "title": "Gap between richest and "
              "poorest wards", "format": "{:.0f} pts", "max": 35,
              "items": [
                  {"label": "Baseline", "value": 31, "status": "bad"},
                  {"label": "Year 1", "value": 24, "status": "warn"},
                  {"label": "Year 2", "value": 17, "status": "warn"},
                  {"label": "Target 2028", "value": 10,
                   "status": "good"},
              ]},
         ]},
    ],
}
