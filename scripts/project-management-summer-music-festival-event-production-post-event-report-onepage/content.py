"""Post-Event Report of Saltmarsh Sound Festival: the project and everything
the document could say. The typesetting keeps what fits into one page, the
most important first."""

PROJECT = {
    "name": "Saltmarsh Sound Festival",
    "code": "SSF-27",
    "author": "Rosa Lindqvist, Festival Director",
}

DOCUMENT = {
    "title": "Post-Event Report",
    "subtitle": "Saltmarsh Sound 2027 · 16 – 18 July · for the board, "
                "partners and the town council",
    "meta": [("Edition", "2027"), ("Attendance", "58,900"),
             ("Satisfaction", "4.5 / 5"), ("Result", "+€368k"),
             ("Author", "Rosa Lindqvist")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "charts": [{"type": "kpis",
         "tiles": [
             {"label": "Attendance", "value": "58,900", "status": 2,
              "note": "98 % of capacity", "delta": "+4 %"},
             {"label": "Rating", "value": "4.5", "status": 1,
              "note": "of 5, from 6,200 answers", "delta": "+0.2"},
             {"label": "Result", "value": "+€368k", "status": "good",
              "note": "budget +€330k"},
             {"label": "Waste recycled", "value": "71 %", "status": 3,
              "note": "target 65 %", "delta": "+9 pts"},
         ]}]},
        {"heading": "Three things to change", "kind": "figure",
         "weight": 0.2, "charts": [{"type": "board", "size": 7.2,
          "columns": [
              {"title": "Fix", "tone": "bad", "cards": [
                  ("Exit from the main stage took 41 minutes on "
                   "Saturday; target is 25", "crowd management"),
              ]},
              {"title": "Fix", "tone": "warn", "cards": [
                  ("Queues at the Friday campsite gate peaked at "
                   "2 h 10 min", "site and box office"),
              ]},
              {"title": "Keep and grow", "tone": "good", "cards": [
                  ("Reusable cups: 92 % returned; extend to food "
                   "plates", "sustainability"),
              ]},
          ]}]},
        {"heading": "Attendance", "kind": "figure", "weight": 0.3,
         "height": {1: 140, 2: 155, 4: 165}, "widths": [3, 2],
         "charts": [
             {"type": "line", "title": "People on site", "subtitle":
              "thousands, by hour", "format": "{:.0f}",
              "x": ["11", "13", "15", "17", "19", "21", "23", "01"],
              "series": [
                  {"name": "Friday", "color": 2, "values": [3, 7, 10, 13,
                                                           16, 18, 17,
                                                           6]},
                  {"name": "Saturday", "values": [5, 10, 13, 15, 18, 19.6,
                                                  18, 7]},
                  {"name": "Sunday", "color": 1, "values": [4, 9, 12, 15,
                                                           17, 18.8, 15,
                                                           3]}]},
             {"type": "bars", "title": "By day", "subtitle":
              "thousands", "format": "{:.1f}",
              "categories": ["Friday", "Saturday", "Sunday"],
              "target": 20, "target_label": "capacity",
              "series": [{"name": "Attendance",
                          "values": [19.2, 19.9, 19.8]}]},
         ]},
        {"heading": "Audience satisfaction", "kind": "figure",
         "weight": 0.4, "min_pages": 2, "height": 165, "charts": [{
             "type": "bars", "horizontal": True, "format": "{:.1f}",
             "title": "Average rating", "subtitle": "of 5",
             "categories": ["Music", "Atmosphere", "Food", "Toilets",
                            "Getting in", "Getting home", "Value for "
                            "money", "Camping"],
             "series": [{"name": "2026", "color": 4,
                         "values": [4.6, 4.6, 4.0, 3.1, 3.6, 3.2, 3.9,
                                    3.7]},
                        {"name": "2027", "values": [4.7, 4.7, 4.2, 3.6,
                                                    3.4, 3.5, 4.0,
                                                    3.8]}]}]},
        {"heading": "Safety", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": 140, "widths": [1, 1], "charts": [
             {"type": "funnel", "title": "Medical cases",
              "stages": [("Seen by welfare or medics", 742),
                         ("Treated at the medical centre", 214),
                         ("Taken to hospital", 11)], "power": 0.5,
              "shares": False},
             {"type": "donut", "title": "Incidents logged",
              "segments": [("Lost property and people", 160),
                           ("Medical", 214), ("Crowd", 18),
                           ("Theft", 42), ("Other", 66)],
              "center": ("500", "incidents")},
         ]},
        {"heading": "Money", "kind": "table", "weight": 0.6, "step": 0.1,
         "min_pages": 2, "badges": {"Better": "good", "Worse": "bad"},
         "columns": [("Line", 2.6), ("Budget", 1.1, "end"),
                     ("Actual", 1.1, "end"), ("Against budget", 1.3,
                                              "center")],
         "rows": [
             ["Ticket income", "€3,720k", "€3,758k", "Better"],
             ["Bars and food", "€850k", "€912k", "Better"],
             ["Sponsors and grants", "€320k", "€320k", "Better"],
             ["Artist costs", "€1,650k", "€1,668k", "Worse"],
             ["Production and site", "€1,880k", "€1,911k", "Worse"],
             ["Contingency used", "€230k", "€120k", "Better"],
             ["Result", "+€330k", "+€368k", "Better"],
         ]},
        {"heading": "Operations", "kind": "text", "weight": 0.7,
         "step": 0.3, "min_pages": 2, "paragraphs": [
             "The build finished half a day early thanks to the new "
             "trackway supplier. The Friday campsite queue was caused "
             "by one scanning lane failing for 50 minutes and too few "
             "staff on the wristband exchange; both are fixed by "
             "moving the exchange to the car parks.",
             "On Saturday the exit from the main stage after the "
             "headliner took 41 minutes, inside the safety plan but "
             "far from our target. The one-way route through the food "
             "court will be widened by 6 m next year.",
         ]},
        {"heading": "Sustainability", "kind": "figure", "weight": 0.9,
         "min_pages": 4, "height": 150, "widths": [3, 2], "charts": [
             {"type": "bars", "title": "Carbon by source",
              "subtitle": "tonnes CO2e", "stacked": True,
              "categories": ["2025", "2026", "2027"],
              "series": [{"name": "Audience travel",
                          "values": [1840, 1790, 1610]},
                         {"name": "Power", "values": [260, 240, 120]},
                         {"name": "Food", "values": [180, 175, 160]},
                         {"name": "Waste and other", "color": 4,
                          "values": [90, 80, 60]}]},
             {"type": "progress", "title": "Targets",
              "format": "{:.0f} %", "items": [
                  {"label": "Waste recycled", "value": 71, "target": 65,
                   "status": "good"},
                  {"label": "Power from battery and solar", "value": 48,
                   "target": 50, "status": "warn"},
                  {"label": "Audience by bus, bike, train", "value": 39,
                   "target": 45, "status": "warn"},
              ]},
         ]},
        {"heading": "What the town said", "kind": "bullets",
         "weight": 1.0, "step": 0.2, "min_pages": 4, "items": [
             "38 noise complaints, down from 61; most about the tent "
             "after 23:00 on Friday.",
             "Local businesses reported their best weekend of the year; "
             "the high street footfall was up 31 % on a normal July "
             "Saturday.",
             "The shuttle from the station worked well but stopped too "
             "early on Sunday: the last bus will run at 00:30.",
         ]},
        {"heading": "For 2028", "kind": "entries", "weight": 1.1,
         "step": 0.2, "inner": 0.1, "min_pages": 4, "entries": [
             {"title": "Same size, better flow", "text": [
                 "Capacity stays at 20,000. Money goes into exits, "
                 "gates and toilets, not more stages."]},
             {"title": "A fourth day for the town", "text": [
                 "A free Thursday evening on the beach for residents, "
                 "with local acts, if the council agrees."]},
             {"title": "Half the travel carbon by 2030", "text": [
                 "Ticket bundles with train and coach, and a bike park "
                 "with 1,000 places."]},
         ]},
        {"heading": "Thank you", "kind": "motto", "weight": 1.2,
         "min_pages": 4, "text": "To 1,140 crew and volunteers, 124 "
         "artists, our neighbours on the marsh and 58,900 people who "
         "sang along: see you in 2028."},
        {"heading": "Artists", "kind": "figure", "weight": 1.05,
         "min_pages": 4, "height": 140, "widths": [3, 2], "charts": [
             {"type": "bars", "title": "Sets that started on time",
              "subtitle": "%", "format": "{:.0f}", "target": 90,
              "target_label": "aim",
              "categories": ["Tidal", "Reedbed", "Saltwater",
                             "Wild Ideas"],
              "series": [{"name": "On time",
                          "values": [94, 86, 97, 100],
                          "colors": ["good", "warn", "good",
                                     "good"]}]},
             {"type": "donut", "title": "Artists by origin",
              "segments": [("Local", 38), ("Rest of country", 52),
                           ("Europe", 26), ("Further", 8)],
              "center": ("124", "artists")},
         ]},
        {"heading": "Press and social", "kind": "figure", "weight": 1.08,
         "min_pages": 4, "charts": [{"type": "kpis", "tiles": [
             {"label": "Reviews", "value": "46", "status": 0,
              "note": "average 4.3 stars"},
             {"label": "Video views", "value": "3.1m", "status": 1,
              "note": "festival week"},
             {"label": "New followers", "value": "+28k", "status": 2,
              "note": "all channels"},
             {"label": "Mentions", "value": "12,400", "status": 3,
              "note": "84 % positive"},
         ]}]},
    ],
}
