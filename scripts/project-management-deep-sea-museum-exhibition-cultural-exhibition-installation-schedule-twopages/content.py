"""Installation Schedule of The Abyss: Life Below Light: the project and
everything the document could say. The typesetting keeps what fits into two
pages, the most important first."""

PROJECT = {
    "name": "The Abyss: Life Below Light",
    "code": "EX-27",
    "author": "Marta Kowalski, Exhibition Project Manager",
}

WEEKS = ["16 Mar", "23 Mar", "30 Mar", "6 Apr", "13 Apr", "20 Apr",
         "27 Apr", "4 May", "11 May"]

DOCUMENT = {
    "title": "Installation Schedule",
    "subtitle": "Eight weeks from empty halls to the opening night · "
                "16 March to 14 May 2027",
    "meta": [("Exhibition", "EX-27"), ("On site", "8 weeks"),
             ("Trades", "9"), ("Objects to install", "212"),
             ("Opening", "Fri 14 May, 19:00")],
    "sections": [
        {"heading": "The eight weeks", "kind": "figure", "weight": 0.1,
         "height": {1: 250, 2: 270, 4: 290}, "charts": [{"type": "gantt",
          "columns": WEEKS, "today": 0.0, "today_label": "start",
          "groups": ["Build", "Services", "Objects", "Finish"],
          "tasks": [
              {"label": "Walls and floors", "section": True, "start": 0,
               "end": 3},
              {"label": "Strip out and protect floors", "start": 0,
               "end": 0.8},
              {"label": "Partitions and ramps", "start": 0.6, "end": 2.6},
              {"label": "Paint, dark blue to black", "start": 2, "end": 3.4},
              {"label": "Services", "section": True, "start": 1,
               "end": 5},
              {"label": "Power and data", "start": 1, "end": 2.8,
               "group": 1},
              {"label": "Lighting rig and focus", "start": 2.8, "end": 5,
               "group": 1},
              {"label": "Projection and sound", "start": 3, "end": 5.2,
               "group": 1},
              {"label": "Cases and objects", "section": True, "start": 3,
               "end": 7.5},
              {"label": "Cases in, climate tested", "start": 3, "end": 4.6,
               "group": 2, "critical": True},
              {"label": "Loans arrive with couriers", "start": 3.4,
               "end": 5.2, "group": 2, "critical": True},
              {"label": "Install specimens and objects", "start": 4.4,
               "end": 7, "group": 2, "critical": True},
              {"label": "Finish", "section": True, "start": 6,
               "end": 9},
              {"label": "Graphics and labels", "start": 5.5, "end": 7,
               "group": 3},
              {"label": "Snagging", "start": 7, "end": 8.2, "group": 3},
              {"label": "Staff training and soft opening", "start": 8,
               "end": 8.8, "group": 3},
              {"label": "Opening night", "start": 8.85, "milestone": True,
               "text": "14 May"},
          ], "deps": [(9, 11), (10, 11)]}]},
        {"heading": "Hold points", "kind": "table", "weight": 0.2,
         "step": 0.1, "columns": [("When", 1), ("Check", 3.6),
                                  ("Who signs", 1.8)],
         "rows": [
             ["2 Apr", "Gallery dust-free and painted for 7 days before "
              "any case opens", "Conservator"],
             ["9 Apr", "Every case holds 16 – 20 °C and 45 – 55 % for 72 "
              "hours", "Conservator"],
             ["16 Apr", "Fire strategy signed off with the second exit "
              "from gallery III", "Fire officer"],
             ["7 May", "Access walk-through by the access panel",
              "Access panel"],
             ["12 May", "Final safety inspection for opening",
              "Building control"],
         ]},
        {"heading": "Trades on site", "kind": "figure", "weight": 0.4,
         "min_pages": 2, "height": 160, "charts": [{"type": "heatmap",
          "rows": ["Joiners", "Painters", "Electricians", "Lighting",
                   "AV", "Case makers", "Art handlers", "Graphics",
                   "Cleaners"],
          "cols": WEEKS,
          "values": [[6, 8, 6, 2, 0, 0, 0, 1, 0],
                     [0, 0, 4, 4, 1, 0, 0, 1, 0],
                     [2, 4, 4, 2, 1, 0, 0, 0, 0],
                     [0, 0, 2, 4, 4, 2, 1, 1, 0],
                     [0, 0, 0, 2, 3, 3, 1, 1, 0],
                     [0, 0, 0, 3, 4, 2, 0, 0, 0],
                     [0, 0, 0, 0, 4, 6, 6, 2, 0],
                     [0, 0, 0, 0, 0, 2, 3, 2, 0],
                     [1, 1, 1, 1, 2, 2, 2, 3, 4]],
          "format": "{:.0f}", "color": 0, "labels": 0.16}]},
        {"heading": "Object moves", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": 150, "widths": [3, 2], "charts": [
             {"type": "bars", "title": "Objects installed per week",
              "stacked": True, "categories": WEEKS[3:8],
              "series": [{"name": "Our collection", "color": 0,
                          "values": [0, 20, 40, 30, 10]},
                         {"name": "Loans", "color": 1,
                          "values": [0, 30, 50, 22, 10]}]},
             {"type": "donut", "title": "Courier days",
              "segments": [("Leiden", 4), ("Kiel", 2), ("Lisbon", 2),
                           ("Bergen", 1), ("Royal Collection", 3)],
              "center": ("12", "days")},
         ]},
        {"heading": "Rules on site", "kind": "bullets", "weight": 0.6,
         "step": 0.15, "min_pages": 2, "items": [
             "No dust-making work in a gallery once its cases are in.",
             "Objects move only with two art handlers and the registrar "
             "present.",
             "Hot works need a permit from the building manager, every "
             "day.",
             "The east wing stays locked outside working hours; keys "
             "from security only.",
         ]},
        {"heading": "Snag list targets", "kind": "figure", "weight": 0.8,
         "min_pages": 4, "height": 140, "charts": [{"type": "line",
          "title": "Open snags", "subtitle": "expected, last three weeks",
          "x": ["27 Apr", "29", "1 May", "4", "6", "8", "11", "13"],
          "target": 0, "target_label": "zero by opening",
          "series": [{"name": "Plan", "dash": True, "color": 4,
                      "values": [60, 85, 90, 70, 45, 25, 10, 0]}]}]},
        {"heading": "Gallery handover", "kind": "table", "weight": 0.9,
         "step": 0.1, "min_pages": 4,
         "columns": [("Gallery", 1.8), ("Build done", 1.2, "center"),
                     ("Objects in", 1.2, "center"),
                     ("Handover", 1.2, "center")],
         "rows": [
             ["I. Sunlight", "2 Apr", "23 Apr", "30 Apr"],
             ["II. Twilight", "2 Apr", "27 Apr", "4 May"],
             ["III. Midnight", "6 Apr", "30 Apr", "7 May"],
             ["IV. Abyss", "6 Apr", "30 Apr", "7 May"],
             ["V. Trenches", "9 Apr", "4 May", "10 May"],
             ["VI. Surface", "9 Apr", "4 May", "10 May"],
         ]},
        {"heading": "Opening week", "kind": "entries", "weight": 1.0,
         "step": 0.2, "inner": 0.1, "min_pages": 4, "entries": [
             {"title": "Monday 10 May", "text": [
                 "Staff walk-through and training for 60 front of house "
                 "staff and volunteers."]},
             {"title": "Wednesday 12 May", "text": [
                 "Soft opening for 400 members and families of the "
                 "team; feedback cards at the exit."]},
             {"title": "Thursday 13 May", "text": [
                 "Press view from 10:00; scientists available for "
                 "interviews."]},
             {"title": "Friday 14 May", "text": [
                 "Opening night for 600 guests, doors at 19:00; open to "
                 "the public from Saturday 10:00."]},
         ]},
        {"heading": "Contacts", "kind": "tags", "weight": 1.1,
         "step": 0.1, "min_pages": 4, "items": [
             ("Project manager", "Marta Kowalski, ext. 214"),
             ("Registrar", "Anouk de Wit, ext. 233"),
             ("Site supervisor", "Henk Bakker, Fathom Build"),
             ("Conservator", "Ilse Brouwer, ext. 241"),
             ("Security", "control room, ext. 100"),
         ]},
        {"heading": "Crew on site", "kind": "figure", "weight": 1.15,
         "min_pages": 4, "height": 150, "widths": [3, 2], "charts": [
             {"type": "bars", "title": "People per week", "stacked": True,
              "categories": WEEKS,
              "series": [{"name": "Build", "values": [9, 13, 16, 9, 2, 0,
                                                      0, 2, 0]},
                         {"name": "Services", "values": [2, 4, 6, 8, 8, 5,
                                                         2, 2, 0]},
                         {"name": "Objects", "values": [0, 0, 0, 3, 8, 8,
                                                        6, 2, 0]},
                         {"name": "Finish", "color": 4,
                          "values": [1, 1, 1, 1, 2, 4, 5, 6, 4]}]},
             {"type": "donut", "title": "Install cost", "format":
              "€{:,.0f}k", "center": ("€1.36m", "on site"),
              "segments": [("Build", 520), ("Lighting and AV", 380),
                           ("Cases", 290), ("Handling", 110),
                           ("Graphics", 60)]},
         ]},
        {"heading": "If something slips", "kind": "bullets",
         "weight": 1.2, "step": 0.2, "min_pages": 4, "items": [
             "Cases late: install our own collection first; loans wait "
             "in the climate store for up to two weeks.",
             "Courier delayed: the lender's object goes in last; the "
             "graphics for its case are printed with and without it.",
             "Lighting focus late: two extra night shifts are booked "
             "provisionally for 3 and 4 May.",
         ]},
    ],
}
