"""Move Schedule of Wharf Street HQ Move: the project and everything the
document could say. The typesetting keeps what fits into four pages, the
most important first."""

PROJECT = {
    "name": "Wharf Street HQ Move",
    "code": "WS-HQ",
    "author": "Elif Demir, Move Manager",
}

WEEKENDS = ["5 Sep", "12 Sep", "19 Sep", "26 Sep", "3 Oct", "10 Oct",
            "17 Oct", "24 Oct", "31 Oct", "7 Nov"]

DOCUMENT = {
    "title": "Move Schedule",
    "subtitle": "1,240 people from three buildings to Wharf Street in "
                "four waves · September to November 2027",
    "meta": [("Project", "WS-HQ"), ("People", "1,240"),
             ("Waves", "4"), ("Crates", "6,800"),
             ("Move manager", "Elif Demir")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "height": {1: 270, 2: 285,
                                                       4: 300},
         "charts": [{"type": "gantt", "columns": WEEKENDS,
          "groups": ["Prepare", "Move weekend", "Settle"],
          "labels": 0.22, "today": 0.2, "today_label": "plan issued",
          "tasks": [
              {"label": "Building", "section": True, "start": 0,
               "end": 2},
              {"label": "Fit-out complete, snagging", "start": 0,
               "end": 1.5},
              {"label": "IT network live on all floors", "start": 0.5,
               "end": 2, "critical": True},
              {"label": "Wave 1 · Finance, Legal (290)", "section": True,
               "start": 1, "end": 3.5},
              {"label": "Crates out, packing", "start": 1, "end": 2},
              {"label": "Move weekend", "start": 2, "end": 2.4,
               "group": 1, "critical": True, "text": "Sat – Sun"},
              {"label": "Floor walkers, first week", "start": 2.4,
               "end": 3.4, "group": 2},
              {"label": "Wave 2 · Product, Design (380)",
               "section": True, "start": 3, "end": 5.5},
              {"label": "Crates out, packing", "start": 3, "end": 4},
              {"label": "Move weekend", "start": 4, "end": 4.4,
               "group": 1, "critical": True},
              {"label": "Floor walkers", "start": 4.4, "end": 5.4,
               "group": 2},
              {"label": "Wave 3 · Sales, Service (360)",
               "section": True, "start": 5, "end": 7.5},
              {"label": "Move weekend", "start": 6, "end": 6.4,
               "group": 1, "critical": True},
              {"label": "Wave 4 · Labs, Exec, IT (210)",
               "section": True, "start": 7, "end": 9.5},
              {"label": "Lab equipment, specialist movers", "start": 7,
               "end": 8.4, "group": 1, "critical": True},
              {"label": "Old buildings handed back", "start": 9.6,
               "milestone": True, "text": "30 Nov"},
          ]}]},
        {"heading": "Waves", "kind": "table", "weight": 0.2, "step": 0.1,
         "columns": [("Wave", 0.8), ("Teams", 2.4), ("From", 1.6),
                     ("To", 1.2), ("People", 0.8, "end"),
                     ("Weekend", 1.1, "center")],
         "rows": [
             ["1", "Finance, Legal, People", "Canal House",
              "Floors 6 – 7", "290", "18 – 19 Sep"],
             ["2", "Product, Design, Data", "Brickworks", "Floors 3 – 5",
              "380", "2 – 3 Oct"],
             ["3", "Sales, Customer service", "Canal House",
              "Floors 1 – 2", "360", "16 – 17 Oct"],
             ["4", "Labs, Executive, IT", "Station Road",
              "Floors 8 – 9, basement", "210", "30 – 31 Oct"],
         ]},
        {"heading": "Weekend runsheet", "kind": "table", "weight": 0.4,
         "step": 0.06, "min_pages": 2,
         "columns": [("Time", 0.8), ("Step", 3.6), ("Who", 1.6),
                     ("Check", 1.6)],
         "rows": [
             ["Fri 17:00", "Last crates sealed; desks cleared; PCs "
              "labelled", "Teams", "Floor captain walk"],
             ["Fri 18:00", "IT disconnects and tags equipment", "IT",
              "Asset list"],
             ["Sat 07:00", "Movers load at the old building",
              "Movers", "Crate count"],
             ["Sat 14:00", "Crates delivered to labelled desks",
              "Movers", "Floor plan"],
             ["Sun 09:00", "IT reconnects and tests every desk", "IT",
              "Test sheet"],
             ["Sun 16:00", "Floor captains check every desk",
              "Captains", "Sign-off"],
             ["Mon 08:00", "Welcome desk, coffee, floor walkers",
              "Facilities", "Issue log"],
         ]},
        {"heading": "Crates and loads", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": 150, "widths": [3, 2], "charts": [
             {"type": "bars", "title": "Crates by wave",
              "stacked": True, "categories": ["Wave 1", "Wave 2",
                                              "Wave 3", "Wave 4"],
              "series": [{"name": "Personal", "values": [870, 1140, 1080,
                                                         420]},
                         {"name": "Team storage", "values": [620, 540,
                                                             380, 610]},
                         {"name": "Archive", "color": 4,
                          "values": [580, 120, 90, 350]}]},
             {"type": "donut", "title": "Truck loads",
              "segments": [("Wave 1", 22), ("Wave 2", 24),
                           ("Wave 3", 19), ("Wave 4", 31)],
              "center": ("96", "loads")},
         ]},
        {"heading": "Go / no-go for each wave", "kind": "bullets",
         "weight": 0.6, "step": 0.15, "min_pages": 2, "items": [
             "Floors signed off by building control and the fire "
             "officer.",
             "Network, Wi-Fi and printers tested on every desk of the "
             "wave.",
             "Lifts booked: two goods lifts at the old building, three "
             "at Wharf Street.",
             "Teams told their desk numbers at least five days before.",
         ]},
        {"heading": "Issues after each wave", "kind": "figure",
         "weight": 0.8, "min_pages": 4, "height": 150, "widths": [3, 2],
         "charts": [
             {"type": "bars", "title": "Issues logged in the first week",
              "subtitle": "target per wave", "stacked": True,
              "categories": ["Wave 1", "Wave 2", "Wave 3", "Wave 4"],
              "series": [{"name": "IT", "values": [40, 34, 30, 30]},
                         {"name": "Furniture", "values": [20, 18, 15,
                                                          10]},
                         {"name": "Building", "values": [15, 12, 10, 8]},
                         {"name": "Other", "color": 4,
                          "values": [5, 5, 5, 5]}]},
             {"type": "progress", "title": "Fixed within", "format":
              "{:.0f} %", "items": [
                  {"label": "Same day", "value": 70, "status": "good"},
                  {"label": "Two days", "value": 92, "status": "good"},
                  {"label": "A week", "value": 99, "status": 0},
              ]},
         ]},
        {"heading": "Special moves", "kind": "entries", "weight": 0.9,
         "step": 0.2, "inner": 0.1, "min_pages": 4, "entries": [
             {"title": "The labs", "dates": "Wave 4", "text": [
                 "Twelve instruments moved by specialist movers with the "
                 "manufacturers' engineers; recalibration takes a "
                 "week."]},
             {"title": "Server room", "dates": "23 – 24 Oct", "text": [
                 "Moved a week before wave 4, on a separate weekend, "
                 "with the cloud failover tested first."]},
             {"title": "The archive", "dates": "Sep – Nov", "text": [
                 "1,140 crates of paper: 60 % to the off-site store, "
                 "40 % to the basement."]},
         ]},
        {"heading": "Contacts", "kind": "tags", "weight": 1.0,
         "step": 0.1, "min_pages": 4, "items": [
             ("Move manager", "Elif Demir, 07700 900 501"),
             ("IT move lead", "Sam Okoro, 07700 900 502"),
             ("Movers", "Harbour Removals, 0800 555 0167"),
             ("Building", "Wharf Street reception, ext. 1000"),
         ]},
    ],
}
