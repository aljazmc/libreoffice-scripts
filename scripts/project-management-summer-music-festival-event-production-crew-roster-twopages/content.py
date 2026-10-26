"""Crew Roster of Saltmarsh Sound Festival: the project and everything the
document could say. The typesetting keeps what fits into two pages, the most
important first."""

PROJECT = {
    "name": "Saltmarsh Sound Festival",
    "code": "SSF-27",
    "author": "Kit Ashworth, Production Manager",
}

DAYS = ["Mo 12", "Tu 13", "We 14", "Th 15", "Fr 16", "Sa 17", "Su 18",
        "Mo 19", "Tu 20", "We 21"]

DOCUMENT = {
    "title": "Crew Roster",
    "subtitle": "Build, show and break · 12 to 21 July 2027 · 1,140 people "
                "in 9 departments",
    "meta": [("Edition", "2027"), ("Crew", "1,140"),
             ("Peak", "640 on Saturday"), ("Crew office", "Gate C, "
                                           "Portakabin 4"),
             ("Version", "Roster v6")],
    "sections": [
        {"heading": "Crew on site per day", "kind": "figure",
         "weight": 0.1, "height": {1: 190, 2: 200, 4: 210},
         "charts": [{"type": "bars", "stacked": True,
          "categories": DAYS, "format": "{:,.0f}",
          "series": [
              {"name": "Production", "values": [60, 90, 120, 140, 150,
                                                150, 150, 120, 80, 30]},
              {"name": "Site", "values": [80, 100, 110, 120, 140, 140,
                                          140, 130, 110, 60]},
              {"name": "Security and stewards", "values": [10, 20, 30,
                                                           60, 210, 230,
                                                           220, 40, 20,
                                                           10]},
              {"name": "Bars and food", "values": [0, 0, 20, 40, 110,
                                                   120, 120, 20, 0, 0]},
              {"name": "Welfare and medical", "color": 4,
               "values": [5, 5, 10, 15, 40, 40, 40, 10, 5, 5]}]}]},
        {"heading": "Departments", "kind": "table", "weight": 0.2,
         "step": 0.08, "columns": [("Department", 2), ("Lead", 1.6),
                                   ("Peak", 0.7, "end"), ("Shifts", 2.2),
                                   ("Base", 1.4)],
         "rows": [
             ["Production and stages", "Kit Ashworth", "150",
              "08:00 – 20:00 / 18:00 – 02:00", "Production office"],
             ["Site and infrastructure", "Bram de Vries", "140",
              "07:00 – 19:00", "Site yard"],
             ["Security", "Sentinel Events", "140", "10:00 – 22:00 / "
              "20:00 – 08:00", "Control, Gate A"],
             ["Stewards", "Faye Mallory", "90", "10:30 – 18:30 / "
              "17:30 – 01:30", "Steward hub"],
             ["Bars", "Marsh Bars Co.", "80", "11:00 – 19:00 / "
              "18:00 – 01:00", "Bar compound"],
             ["Food", "Traders", "40", "own rotas", "Traders' field"],
             ["Medical", "Coastline Medics", "28", "10:00 – 02:00",
              "Medical centre"],
             ["Welfare and access", "Jo Achebe", "12", "11:00 – 01:00",
              "Welfare tent"],
             ["Artist liaison", "Nadia Reyes", "14", "10:00 – 01:00",
              "Backstage"],
         ]},
        {"heading": "Who reports to whom", "kind": "figure",
         "weight": 0.4, "min_pages": 2, "charts": [{"type": "tree",
          "root": {"label": "Festival Director", "note": "Rosa Lindqvist",
                   "children": [
              {"label": "Production", "note": "Kit Ashworth",
               "children": [
                   {"label": "Stage managers × 4"},
                   {"label": "Sound, light, video"},
                   {"label": "Artist liaison"}]},
              {"label": "Site", "note": "Bram de Vries", "children": [
                  {"label": "Power and water"},
                  {"label": "Fencing and traffic"},
                  {"label": "Waste and cleaning"}]},
              {"label": "Safety", "note": "Ama Boateng", "children": [
                  {"label": "Security contractor"},
                  {"label": "Stewards"},
                  {"label": "Medical", "status": "bad"}]},
              {"label": "Audience", "note": "Jo Achebe", "children": [
                  {"label": "Welfare and access"},
                  {"label": "Bars and food"},
                  {"label": "Box office"}]},
          ]}}]},
        {"heading": "Welfare rules", "kind": "bullets", "weight": 0.5,
         "step": 0.15, "min_pages": 2, "items": [
             "No shift longer than 12 hours, and at least 10 hours "
             "between shifts.",
             "Crew catering open 06:30 to 02:30; one hot meal per shift "
             "is free.",
             "Night crew sleep in the quiet crew camp, away from the "
             "public campsite.",
             "Anyone can call the welfare line on channel 6 or 0800 "
             "555 0127, at any hour, without asking their lead.",
         ]},
        {"heading": "Shifts by hour", "kind": "figure", "weight": 0.7,
         "min_pages": 4, "height": 155, "charts": [{"type": "heatmap",
          "title": "Saturday, people on duty",
          "rows": ["Production", "Site", "Security", "Stewards", "Bars",
                   "Medical"],
          "cols": ["06", "08", "10", "12", "14", "16", "18", "20", "22",
                   "00", "02"],
          "values": [[10, 60, 120, 140, 150, 150, 150, 150, 140, 90, 30],
                     [30, 110, 140, 140, 120, 110, 120, 100, 80, 40, 20],
                     [40, 40, 120, 140, 140, 140, 140, 140, 140, 120, 60],
                     [0, 0, 60, 90, 90, 90, 90, 90, 90, 60, 10],
                     [0, 10, 40, 80, 80, 80, 80, 80, 80, 40, 0],
                     [4, 6, 20, 28, 28, 28, 28, 28, 28, 20, 8]],
          "format": "{:.0f}", "color": 0}]},
        {"heading": "Hours", "kind": "figure", "weight": 0.8,
         "min_pages": 4, "height": 150, "widths": [3, 2], "charts": [
             {"type": "bars", "horizontal": True, "title": "Average "
              "hours per person per day", "format": "{:.1f}",
              "target": 12, "target_label": "limit",
              "categories": ["Production", "Site", "Security",
                             "Stewards", "Bars", "Medical", "Welfare"],
              "series": [{"name": "Hours", "values": [11.4, 10.8, 11.8,
                                                      8.0, 7.5, 10.0,
                                                      9.0],
                          "colors": ["warn", 0, "warn", 0, 0, 0, 0]}]},
             {"type": "donut", "title": "Who they are",
              "segments": [("Paid crew", 520), ("Contractors", 380),
                           ("Volunteers", 240)],
              "center": ("1,140", "people"), "format": "{:,.0f}"},
         ]},
        {"heading": "Volunteers", "kind": "text", "weight": 0.9,
         "step": 0.3, "min_pages": 4, "paragraphs": [
             "240 volunteers work three six-hour shifts across the "
             "weekend in exchange for a weekend ticket, camping in the "
             "crew field and meals. Most return year after year; 40 % "
             "of this year's stewards started as volunteers.",
             "Every volunteer has a two-hour induction on Thursday, "
             "including the site tour, the radio, safeguarding and what "
             "to do when someone is unwell.",
         ]},
        {"heading": "Key dates", "kind": "figure", "weight": 1.0,
         "min_pages": 4, "height": 115, "charts": [{"type": "timeline",
          "start": 0, "end": 9, "label_width": 95,
          "ticks": [(i, d) for i, d in enumerate(DAYS)],
          "events": [
              {"at": 0, "label": "Site handover", "sub": "08:00",
               "status": "done"},
              {"at": 3, "label": "Crew inductions", "sub": "all day"},
              {"at": 4, "label": "Gates open", "sub": "Fri 11:00",
               "status": "now"},
              {"at": 6, "label": "Last set", "sub": "Sun 23:00"},
              {"at": 9, "label": "Site handed back", "sub": "18:00"},
          ]}]},
        {"heading": "Crew camp and catering", "kind": "figure",
         "weight": 1.05, "min_pages": 4, "height": 150, "widths": [1, 1],
         "charts": [
             {"type": "bars", "title": "Crew camp beds used",
              "categories": DAYS, "values": False, "target": 520,
              "target_label": "beds",
              "series": [{"name": "Beds", "values": [90, 140, 210, 330,
                                                     480, 500, 490, 260,
                                                     150, 40]}]},
             {"type": "line", "title": "Meals served by crew catering",
              "x": DAYS, "format": "{:,.0f}",
              "series": [{"name": "Meals", "color": 1, "area": True,
                          "values": [180, 260, 380, 610, 1220, 1340,
                                     1290, 480, 300, 90]}]},
         ]},
        {"heading": "Contacts", "kind": "table", "weight": 1.1,
         "step": 0.1, "min_pages": 4,
         "columns": [("Role", 2), ("Name", 1.6), ("Radio", 0.8,
                                                  "center"),
                     ("Phone", 1.6)],
         "rows": [
             ["Production manager", "Kit Ashworth", "Ch 1",
              "+44 7700 900 101"],
             ["Site manager", "Bram de Vries", "Ch 1",
              "+44 7700 900 102"],
             ["Head of safety", "Ama Boateng", "Ch 4",
              "+44 7700 900 103"],
             ["Head of stewarding", "Faye Mallory", "Ch 4",
              "+44 7700 900 104"],
             ["Crew office", "Lou Fenwick", "Ch 1", "+44 7700 900 105"],
             ["Welfare line", "24 hours", "Ch 6", "0800 555 0127"],
         ]},
        {"heading": "Accreditation", "kind": "figure", "weight": 1.15,
         "min_pages": 4, "height": 90, "charts": [{"type": "heatmap",
          "rows": ["Wristband colour"],
          "cols": ["Production", "Site", "Security", "Bars and food",
                   "Artists", "Press"],
          "values": [["All areas", "Site and arena", "Arena and "
                      "gates", "Arena", "Backstage", "Arena and pit"]],
          "badges": {"All areas": "bad", "Site and arena": 2,
                     "Arena and gates": 3, "Arena": 1,
                     "Backstage": 0, "Arena and pit": 4},
          "header": 18, "labels": 0.16}]},
    ],
}
