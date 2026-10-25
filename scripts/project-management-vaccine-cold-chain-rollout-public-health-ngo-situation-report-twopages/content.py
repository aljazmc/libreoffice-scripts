"""Situation Report of Cold Chain for Every Child: the project and everything
the document could say. The typesetting keeps what fits into two pages, the
most important first."""

PROJECT = {
    "name": "Cold Chain for Every Child",
    "code": "CCEC",
    "author": "Field coordination team, Baringo office",
}

WEEKS = ["W22", "W23", "W24", "W25", "W26", "W27", "W28", "W29", "W30",
         "W31"]

DOCUMENT = {
    "title": "Situation Report 31",
    "subtitle": "Week 31 · 27 July to 2 August 2026 · four districts",
    "meta": [("Programme", "CCEC"), ("Sitrep", "No. 31"),
             ("Week", "31, 2026"), ("Fridges down", "6"),
             ("Status", "Amber")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "charts": [{"type": "kpis",
         "tiles": [
             {"label": "Doses given", "value": "4,212", "status": 0,
              "note": "this week", "delta": "+6 %"},
             {"label": "Outreach held", "value": "141 / 160",
              "status": "warn", "note": "88 %"},
             {"label": "Fridges working", "value": "206 / 212",
              "status": "good", "note": "6 under repair"},
             {"label": "Stock-outs", "value": "3", "status": "bad",
              "note": "facilities, measles vaccine"},
         ]}]},
        {"heading": "Coverage by district", "kind": "figure",
         "weight": 0.2, "height": {1: 125, 2: 135, 4: 145},
         "charts": [{"type": "heatmap",
          "title": "DTP3 coverage, % of monthly target, last ten weeks",
          "rows": ["Baringo North", "Lake Shore", "Highlands East",
                   "Dry Plains"],
          "cols": WEEKS,
          "values": [[92, 95, 97, 94, 98, 101, 96, 99, 97, 100],
                     [101, 99, 104, 102, 98, 103, 105, 101, 99, 104],
                     [78, 81, 76, 72, 69, 74, 80, 83, 79, 85],
                     [84, 88, 86, 91, 89, 87, 93, 95, 90, 94]],
          "thresholds": [(0, "bad"), (80, "warn"), (95, "good")],
          "format": "{:.0f}", "labels": 0.2}]},
        {"heading": "Cold chain", "kind": "table", "weight": 0.3,
         "step": 0.1, "badges": {"Repaired": "good", "In repair": "warn",
                                 "Waiting parts": "bad"},
         "columns": [("Facility", 2), ("District", 1.4),
                     ("Problem", 2.6), ("Status", 1.2, "center")],
         "rows": [
             ["Kiptagat dispensary", "Highlands E.", "Solar panel "
              "cracked by hail", "Waiting parts"],
             ["Loruk health centre", "Baringo N.", "Thermostat fault",
              "In repair"],
             ["Ng'ambo dispensary", "Lake Shore", "Door seal", "In "
              "repair"],
             ["Kapedo health centre", "Dry Plains", "Cable cut",
              "In repair"],
             ["Tangulbei dispensary", "Dry Plains", "Panel stolen",
              "Waiting parts"],
             ["Sibilo dispensary", "Highlands E.", "Controller fault",
              "In repair"],
             ["Marigat sub-county", "Baringo N.", "Compressor (old "
              "fridge)", "Repaired"],
         ]},
        {"heading": "Actions this week", "kind": "bullets", "weight": 0.4,
         "step": 0.15, "items": [
             "Move 1,200 doses of measles vaccine from Lake Shore to the "
             "three facilities out of stock by Wednesday.",
             "Replace the stolen panel at Tangulbei and fit an "
             "anti-theft frame; the chief has offered a night guard.",
             "Hold the four missed outreach sessions in Highlands East "
             "on Saturday, when the road reopens.",
         ]},
        {"heading": "Stock", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": 160, "charts": [{"type": "bars",
          "title": "Months of stock at district stores",
          "categories": ["BCG", "OPV", "Penta", "PCV", "Rota",
                         "Measles", "HPV"],
          "format": "{:.1f}", "target": 1, "target_label": "minimum",
          "series": [{"name": "Months", "values": [3.2, 2.8, 2.1, 1.9,
                                                   2.4, 0.6, 3.6],
                      "colors": [0, 0, 0, 0, 0, "bad", 0]}]}]},
        {"heading": "Trend", "kind": "figure", "weight": 0.6,
         "min_pages": 2, "height": 150, "widths": [1, 1], "charts": [
             {"type": "line", "title": "Doses given per week",
              "x": WEEKS, "format": "{:,.0f}",
              "series": [{"name": "Doses", "area": True,
                          "values": [3810, 3920, 3760, 3640, 3580, 3890,
                                     4020, 4110, 3970, 4212]}]},
             {"type": "line", "title": "Temperature alarms", "x": WEEKS,
              "format": "{:.0f}",
              "series": [{"name": "Alarms", "color": "bad",
                          "values": [21, 18, 17, 24, 29, 22, 15, 13, 14,
                                     11]}]},
         ]},
        {"heading": "In the field", "kind": "text", "weight": 0.7,
         "step": 0.3, "min_pages": 2, "paragraphs": [
             "Heavy rain closed the road from Kabarnet to the upper "
             "villages of Highlands East from Tuesday to Friday. Four "
             "outreach sessions were postponed; nurses walked to two of "
             "them with vaccine carriers.",
             "In Dry Plains the switch to market-day outreach continues "
             "to work: 312 children came to the two market sessions, "
             "the most in a week since the programme began.",
         ]},
        {"heading": "Logistics", "kind": "figure", "weight": 0.8,
         "min_pages": 4, "height": 140, "widths": [3, 2], "charts": [
             {"type": "progress", "title": "Motorbikes and fuel",
              "format": "{:.0f} %", "items": [
                  {"label": "Motorbikes running", "value": 94,
                   "status": "good", "display": "113 / 120"},
                  {"label": "Fuel received vs plan", "value": 81,
                   "target": 100, "status": "warn"},
                  {"label": "Cold boxes in good condition", "value": 97,
                   "status": "good"},
              ]},
             {"type": "donut", "title": "Distance ridden",
              "segments": [("Outreach", 9100), ("Stock moves", 2400),
                           ("Repairs", 1300), ("Supervision", 900)],
              "format": "{:,.0f} km", "center": ("13,700", "km")},
         ]},
        {"heading": "Requests", "kind": "table", "weight": 0.9,
         "step": 0.1, "min_pages": 4,
         "columns": [("To", 1.6), ("Request", 3.6), ("By", 1)],
         "rows": [
             ["Ministry", "Release 4,000 measles doses from the "
              "regional store", "5 Aug"],
             ["County roads", "Grade the Kabarnet – Tenges road",
              "15 Aug"],
             ["Supplier", "Ship four replacement solar panels",
              "10 Aug"],
         ]},
        {"heading": "Security", "kind": "callout", "weight": 1.0,
         "tone": "warn", "min_pages": 4, "label": "Note:",
         "text": "two solar panels stolen in a month in Dry Plains. All "
                 "panels there get anti-theft frames by the end of "
                 "August, and the community health committees have "
                 "agreed to watch the sites."},
        {"heading": "Next week", "kind": "bullets", "weight": 1.1,
         "step": 0.2, "min_pages": 4, "items": [
             "Quarterly data quality audit in Lake Shore.",
             "Visit of the Northfield Foundation to Baringo North on "
             "Thursday.",
             "Training of 24 new community health workers in Dry "
             "Plains.",
         ]},
        {"heading": "Facilities", "kind": "figure", "weight": 1.2,
         "min_pages": 4, "height": 130, "charts": [{"type": "bars",
          "horizontal": True, "stacked": True, "inside": True,
          "title": "Facility status by district",
          "categories": ["Baringo North", "Lake Shore",
                         "Highlands East", "Dry Plains"],
          "series": [{"name": "Working", "color": "good",
                      "values": [53, 67, 39, 47]},
                     {"name": "In repair", "color": "bad",
                      "values": [1, 1, 2, 2]}]}]},
        {"heading": "Outreach by district", "kind": "figure",
         "weight": 1.25, "min_pages": 4, "height": 150, "widths": [3, 2],
         "charts": [
             {"type": "bars", "title": "Sessions held and planned",
              "categories": ["Baringo N.", "Lake Shore", "Highlands E.",
                             "Dry Plains"],
              "series": [{"name": "Planned", "color": 4,
                          "values": [38, 44, 46, 32]},
                         {"name": "Held", "values": [36, 43, 32, 30]}]},
             {"type": "donut", "title": "Children reached",
              "segments": [("At facilities", 2860), ("At outreach",
                                                     1352)],
              "format": "{:,.0f}", "center": ("4,212", "doses")},
         ]},
        {"heading": "Contacts", "kind": "tags", "weight": 1.3,
         "step": 0.1, "min_pages": 4, "items": [
             ("Field coordinator", "Amani Mwangi, +254 700 000 101"),
             ("Cold chain", "Peter Kiprono, +254 700 000 102"),
             ("Logistics", "Fatuma Hassan, +254 700 000 103"),
             ("M&E", "Joseph Otieno, +254 700 000 104"),
         ]},
    ],
}
