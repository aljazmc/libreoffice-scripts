"""Three-Week Lookahead of Harbour Bridge Retrofit: the project and everything
the document could say. The typesetting keeps what fits into two pages, the
most important first."""

PROJECT = {
    "name": "Harbour Bridge Retrofit",
    "code": "HBR-24",
    "author": "Tomas Brandt, Site Manager, Ferrand Civils",
}

DAYS = ["Mo 14", "Tu 15", "We 16", "Th 17", "Fr 18", "Sa 19", "Su 20",
        "Mo 21", "Tu 22", "We 23", "Th 24", "Fr 25", "Sa 26", "Su 27",
        "Mo 28", "Tu 29", "We 30", "Th 1", "Fr 2", "Sa 3", "Su 4"]

DOCUMENT = {
    "title": "Three-Week Lookahead",
    "subtitle": "Weeks 38 to 40 · Monday 14 September to Sunday 4 October "
                "2026",
    "meta": [("Project", "HBR-24"), ("Issued", "Fri 11 Sep 2026"),
             ("Site manager", "Tomas Brandt"), ("Possessions", "11 nights"),
             ("Revision", "L38-A")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "height": {1: 300, 2: 330,
                                                       4: 340},
         "charts": [{"type": "gantt", "columns": DAYS, "labels": 0.24,
          "groups": ["Steel", "Bearings", "Deck", "Traffic"],
          "today": 0.2, "today_label": "issue",
          "tasks": [
              {"label": "South span", "section": True, "start": 0,
               "end": 21},
              {"label": "Blast and prime, bays S5 – S6", "start": 0,
               "end": 5, "progress": 0.1, "text": "day shift, crew B"},
              {"label": "Intermediate coat, S3 – S4", "start": 2, "end": 9,
               "text": "crew A"},
              {"label": "Finish coat, S1 – S2", "start": 9, "end": 16},
              {"label": "Containment move to S7", "start": 16, "end": 19,
               "critical": True},
              {"label": "Pier 3", "section": True, "start": 0, "end": 15},
              {"label": "Jacking frames installed", "start": 0, "end": 4,
               "group": 1, "critical": True},
              {"label": "Jack and swap bearings B3-1 – B3-4", "start": 7,
               "end": 10, "group": 1, "critical": True,
               "text": "nights"},
              {"label": "Jack and swap bearings B3-5 – B3-8", "start": 14,
               "end": 17, "group": 1, "critical": True,
               "text": "nights"},
              {"label": "Hold point: check engineer", "start": 10.5,
               "milestone": True, "text": "HP-14"},
              {"label": "Deck, north carriageway", "section": True,
               "start": 2, "end": 21},
              {"label": "Plane off surfacing", "start": 2, "end": 5,
               "group": 2, "text": "nights"},
              {"label": "Waterproofing membrane", "start": 7, "end": 12,
               "group": 2, "text": "dry weather only"},
              {"label": "Surfacing and lining", "start": 14, "end": 18,
               "group": 2},
              {"label": "Lane 1 reopens", "start": 18.5,
               "milestone": True, "text": "Fri 2 Oct, 05:30"},
              {"label": "Night possessions", "start": 0, "end": 18,
               "group": 3, "text": "Sun – Thu, 22:00 – 05:30"},
          ], "deps": [(6, 7), (7, 9), (9, 8)]}]},
        {"heading": "Constraints to clear", "kind": "table", "weight": 0.3,
         "step": 0.15, "columns": [
             ("Activity", 2.4), ("Constraint", 3.4), ("Owner", 1.2),
             ("Due", 0.9), ("Status", 1, "center")],
         "badges": {"Clear": "good", "At risk": "warn", "Open": "bad"},
         "rows": [
             ["Pier 3 jacking", "Revised frame design accepted by the "
              "check engineer", "Halden", "15 Sep", "At risk"],
             ["Bearings B3-1 to B3-8", "Bearings delivered and inspected",
              "Ferrand", "18 Sep", "Clear"],
             ["Waterproofing", "Three dry nights forecast; membrane in "
              "the compound", "Ferrand", "21 Sep", "Open"],
             ["Night possessions", "Friday nights agreed with the "
              "council and buses", "Highways", "14 Sep", "Clear"],
             ["Containment move", "Harbour notice to mariners issued",
              "Project", "25 Sep", "Open"],
             ["Surfacing", "Asphalt plant booked for nights", "Ferrand",
              "24 Sep", "Clear"],
         ]},
        {"heading": "Crews and plant", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": 170, "widths": [3, 2], "charts": [
             {"type": "bars", "title": "Operatives on site per day",
              "stacked": True, "values": False,
              "categories": [d.split()[1] for d in DAYS],
              "series": [
                  {"name": "Paint", "values": [14, 14, 14, 14, 14, 6, 0,
                                               16, 16, 16, 16, 16, 6, 0,
                                               16, 16, 16, 12, 12, 0, 0]},
                  {"name": "Bearings", "values": [6, 6, 6, 6, 0, 0, 0, 8,
                                                  8, 8, 0, 0, 0, 0, 8, 8,
                                                  8, 0, 0, 0, 0]},
                  {"name": "Deck", "values": [0, 0, 10, 10, 10, 0, 0, 8,
                                              8, 8, 8, 8, 0, 0, 12, 12,
                                              12, 12, 0, 0, 0]},
                  {"name": "Traffic", "values": [4, 4, 4, 4, 4, 0, 4, 4,
                                                 4, 4, 4, 4, 0, 4, 4, 4,
                                                 4, 4, 0, 0, 4]}]},
             {"type": "heatmap", "title": "Key plant", "size": 6.8,
              "rows": ["Mobile crane 60 t", "Jacking system",
                       "Planer", "Paver", "Blast unit"],
              "cols": ["Wk 38", "Wk 39", "Wk 40"],
              "values": [["On site", "On site", "Off"],
                         ["On site", "On site", "On site"],
                         ["On site", "Off", "Off"],
                         ["Off", "Off", "On site"],
                         ["On site", "On site", "On site"]],
              "badges": {"On site": "accent", "Off": "neutral"}},
         ]},
        {"heading": "Possessions", "kind": "table", "weight": 0.7,
         "step": 0.1, "min_pages": 2, "columns": [
             ("Night", 1.2), ("Lanes closed", 1.6), ("Work", 3),
             ("Buses", 1.6)],
         "rows": [
             ["Sun 13 – Thu 17", "Northbound 1 and 2", "Plane off "
              "surfacing; jacking frames", "Diverted via Quay Rd"],
             ["Fri 18", "Northbound 1", "Jacking frames", "Normal"],
             ["Sun 20 – Thu 24", "Northbound 1 and 2", "Bearings "
              "B3-1 – B3-4; membrane", "Diverted via Quay Rd"],
             ["Sun 27 – Thu 1", "Northbound 1 and 2", "Bearings "
              "B3-5 – B3-8; surfacing", "Diverted via Quay Rd"],
         ]},
        {"heading": "Deliveries", "kind": "figure", "weight": 1.0,
         "min_pages": 4, "height": 120, "charts": [{"type": "timeline",
          "start": 0, "end": 21, "label_width": 110,
          "ticks": [(0, "14 Sep"), (7, "21 Sep"), (14, "28 Sep"),
                    (21, "5 Oct")],
          "events": [
              {"at": 1, "label": "Jacking frames", "sub": "2 loads, "
               "crane"},
              {"at": 3, "label": "Bearings B3-1 – B3-8", "sub": "from "
               "Mageba"},
              {"at": 6, "label": "Membrane, 40 rolls", "sub": "compound"},
              {"at": 9, "label": "Paint, finish coat", "sub": "8,000 l"},
              {"at": 13, "label": "Scaffold for S7", "sub": "by barge",
               "status": "now"},
              {"at": 15, "label": "Asphalt", "sub": "nights, 12 loads"},
              {"at": 19, "label": "Road markings", "sub": "subcontract"},
          ]}]},
        {"heading": "Safety focus", "kind": "bullets", "weight": 1.1,
         "step": 0.2, "min_pages": 4, "items": [
             "**Jacking:** exclusion zone of 5 m around every jack; "
             "nobody under the deck while the load is transferred.",
             "**Working over water:** life jackets and the rescue boat "
             "manned whenever anyone is outside the containment.",
             "**Night work:** two-person rule, task lighting checked at "
             "21:30, fatigue log signed at the end of the shift.",
             "**Hot asphalt:** burns kit at the paver; no work within "
             "10 m of the cycle lane barrier.",
         ]},
        {"heading": "Weather", "kind": "figure", "weight": 1.2,
         "min_pages": 4, "height": 120, "charts": [{"type": "bars",
          "title": "Chance of rain, nights", "subtitle": "%, forecast "
          "of 11 Sep", "categories": [d.split()[1] for d in DAYS[:14]],
          "format": "{:.0f}", "target": 40, "target_label": "membrane "
          "limit",
          "series": [{"name": "Rain", "values": [10, 20, 60, 70, 30, 10,
                                                 20, 30, 20, 50, 60, 20,
                                                 10, 10],
                      "colors": ["good", "good", "bad", "bad", "good",
                                 "good", "good", "good", "good", "bad",
                                 "bad", "good", "good", "good"]}]}]},
        {"heading": "Notes", "kind": "text", "weight": 1.4, "step": 0.2,
         "min_pages": 4, "paragraphs": [
             "The pier 3 bearing swap is on the critical path. If the "
             "check engineer has not accepted the frame design by "
             "Tuesday 15, the first jacking night moves to Sunday 27 and "
             "the second set of bearings to the week of 5 October, which "
             "takes one week out of the float to the load test.",
             "The membrane can only go down on a dry deck. If two of the "
             "nights in week 39 are lost to rain, the crew moves to the "
             "joint preparation at the south abutment instead.",
         ]},
    ],
}
