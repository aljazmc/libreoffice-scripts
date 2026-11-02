"""Stack Plan of Wharf Street HQ Move: the project and everything the document
could say. The typesetting keeps what fits into four pages, the most
important first."""

PROJECT = {
    "name": "Wharf Street HQ Move",
    "code": "WS-HQ",
    "author": "Tomás Reyes, Workplace Strategist",
}

FLOORS = ["9 · Executive, Board", "8 · Labs", "7 · Finance, Legal",
          "6 · People, Comms", "5 · Data", "4 · Design", "3 · Product",
          "2 · Customer service", "1 · Sales", "G · Café, Events"]

DOCUMENT = {
    "title": "Stack Plan",
    "subtitle": "Who sits on which floor at Wharf Street, and how full "
                "each floor is · version 5 for the steering group",
    "meta": [("Project", "WS-HQ"), ("Floors", "10"),
             ("Desks", "980"), ("People", "1,240"),
             ("Sharing ratio", "0.79 desks / person")],
    "sections": [
        {"heading": "The stack", "kind": "figure", "weight": 0.1,
         "height": {1: 225, 2: 240, 4: 250}, "charts": [{"type": "bars",
          "horizontal": True, "stacked": True, "inside": True,
          "title": "Settings per floor",
          "categories": FLOORS,
          "series": [{"name": "Desks", "values": [60, 40, 110, 100, 100,
                                                  95, 120, 140, 160, 0],
                      "color": 0},
                     {"name": "Meeting seats", "values": [40, 10, 30, 30,
                                                          30, 40, 40, 20,
                                                          30, 60],
                      "color": 1},
                     {"name": "Focus booths", "values": [4, 6, 12, 10, 14,
                                                         10, 12, 8, 8, 0],
                      "color": 2},
                     {"name": "Social seats", "values": [10, 8, 20, 20,
                                                         20, 30, 25, 20,
                                                         30, 160],
                      "color": 3}]}]},
        {"heading": "Occupancy", "kind": "figure", "weight": 0.2,
         "height": {1: 150, 2: 165, 4: 175}, "widths": [3, 2],
         "charts": [
             {"type": "bars", "title": "People per desk, by floor",
              "format": "{:.2f}", "target": 1.3, "target_label":
              "policy limit",
              "categories": ["9", "8", "7", "6", "5", "4", "3", "2", "1"],
              "series": [{"name": "Ratio",
                          "values": [1.0, 1.0, 1.24, 1.28, 1.35, 1.26,
                                     1.29, 1.1, 1.38],
                          "colors": [4, 4, 0, 0, "bad", 0, 0, 0,
                                     "bad"]}]},
             {"type": "donut", "title": "Space by use",
              "segments": [("Desks", 52), ("Meeting", 18),
                           ("Social and café", 16), ("Focus", 6),
                           ("Support", 8)],
              "format": "{:.0f}%", "center": ("14,200", "m² net")},
         ]},
        {"heading": "Floors", "kind": "table", "weight": 0.3,
         "step": 0.05, "badges": {"Over": "bad", "Tight": "warn",
                                  "OK": "good"},
         "columns": [("Floor", 2.4), ("People", 0.8, "end"),
                     ("Desks", 0.8, "end"), ("Rooms", 0.8, "end"),
                     ("Ratio", 0.8, "end"), ("Fit", 0.8, "center")],
         "rows": [
             ["9 · Executive, Board", "60", "60", "8", "1.00", "OK"],
             ["8 · Labs", "40", "40", "3", "1.00", "OK"],
             ["7 · Finance, Legal", "136", "110", "7", "1.24", "OK"],
             ["6 · People, Comms", "128", "100", "7", "1.28", "Tight"],
             ["5 · Data", "135", "100", "6", "1.35", "Over"],
             ["4 · Design", "120", "95", "9", "1.26", "OK"],
             ["3 · Product", "155", "120", "9", "1.29", "Tight"],
             ["2 · Customer service", "154", "140", "4", "1.10", "OK"],
             ["1 · Sales", "220", "160", "6", "1.38", "Over"],
         ]},
        {"heading": "Adjacencies", "kind": "figure", "weight": 0.4,
         "min_pages": 2, "height": 175, "charts": [{"type": "heatmap",
          "title": "How much teams need to be near each other",
          "subtitle": "from the survey, 0 to 5",
          "rows": ["Sales", "Service", "Product", "Design", "Data",
                   "Finance", "Legal", "People"],
          "cols": ["Sales", "Service", "Product", "Design", "Data",
                   "Finance", "Legal", "People"],
          "values": [["", 5, 3, 1, 2, 2, 1, 1],
                     [5, "", 4, 1, 3, 1, 1, 1],
                     [3, 4, "", 5, 4, 1, 1, 1],
                     [1, 1, 5, "", 3, 0, 0, 1],
                     [2, 3, 4, 3, "", 3, 1, 1],
                     [2, 1, 1, 0, 3, "", 4, 3],
                     [1, 1, 1, 0, 1, 4, "", 3],
                     [1, 1, 1, 1, 1, 3, 3, ""]],
          "format": "{:.0f}", "labels": 0.12}]},
        {"heading": "Principles", "kind": "bullets", "weight": 0.5,
         "step": 0.15, "min_pages": 2, "items": [
             "Teams that work together most sit on the same or the next "
             "floor: Sales and Service on 1 – 2, Product, Design and "
             "Data on 3 – 5.",
             "No floor above 1.3 people per desk on its busiest day.",
             "Every floor has a quiet zone at the far end from the "
             "lifts.",
             "The ground floor is for everyone, and for guests.",
         ]},
        {"heading": "Busiest days", "kind": "figure", "weight": 0.6,
         "min_pages": 2, "height": 150, "charts": [{"type": "heatmap",
          "title": "Expected desk use, % of desks",
          "rows": ["Sales", "Service", "Product", "Design", "Data",
                   "Finance and Legal"],
          "cols": ["Mon", "Tue", "Wed", "Thu", "Fri"],
          "values": [[72, 96, 98, 94, 48], [88, 90, 92, 90, 84],
                     [60, 95, 97, 92, 40], [55, 90, 95, 88, 35],
                     [58, 99, 101, 85, 38], [70, 88, 90, 86, 52]],
          "thresholds": [(0, "good"), (85, "warn"), (98, "bad")],
          "format": "{:.0f}", "labels": 0.2}]},
        {"heading": "Fixing the two tight floors", "kind": "entries",
         "weight": 0.8, "step": 0.2, "inner": 0.1, "min_pages": 4,
         "entries": [
             {"title": "Floor 1 · Sales", "dates": "1.38", "text": [
                 "Sales anchor days moved from Tuesday and Wednesday to "
                 "Monday and Thursday, which spreads the peak. Twenty "
                 "touchdown desks added in the café on G."]},
             {"title": "Floor 5 · Data", "dates": "1.35", "text": [
                 "The analytics team of 18 moves to floor 4, beside "
                 "Design, which it works with on research. Floor 5 "
                 "drops to 1.17."]},
         ]},
        {"heading": "Growth", "kind": "figure", "weight": 0.9,
         "min_pages": 4, "height": 150, "charts": [{"type": "line",
          "title": "People against capacity", "x": ["2027", "2028",
                                                     "2029", "2030"],
          "format": "{:,.0f}", "target": 1270, "target_label":
          "capacity at 1.3",
          "series": [{"name": "Forecast headcount", "values": [1240,
                                                               1290,
                                                               1340,
                                                               1380]},
                     {"name": "With one floor sublet back", "color": 4,
                      "dash": True, "values": [1240, 1290, 1340,
                                               1380]}]}]},
        {"heading": "Rooms", "kind": "table", "weight": 1.0, "step": 0.1,
         "min_pages": 4,
         "columns": [("Room type", 2), ("Seats", 0.8, "center"),
                     ("Number", 0.8, "end"), ("Where", 2.4)],
         "rows": [
             ["Focus booth", "1", "84", "Every floor, quiet end"],
             ["Small meeting", "4", "48", "Every floor"],
             ["Project room", "8", "22", "Floors 3 – 5"],
             ["Board room", "20", "1", "Floor 9"],
             ["Event space", "200", "1", "Ground floor"],
         ]},
        {"heading": "Lockers and storage", "kind": "text", "weight": 1.1,
         "step": 0.3, "min_pages": 4, "paragraphs": [
             "Everyone gets a locker; teams get one metre of shelving "
             "per four people. Paper is the hardest habit to break: "
             "each team has been asked to clear 60 % of its files "
             "before the move, and the archive crates are counted "
             "against that target.",
         ]},
        {"heading": "Before and after", "kind": "figure", "weight": 1.15,
         "min_pages": 4, "height": 150, "widths": [1, 1], "charts": [
             {"type": "bars", "title": "Floor area", "subtitle": "m² net",
              "format": "{:,.0f}",
              "categories": ["Canal House", "Brickworks", "Station Road",
                             "Wharf Street"],
              "series": [{"name": "Area", "values": [7200, 5100, 4300,
                                                     14200],
                          "colors": [4, 4, 4, 0]}]},
             {"type": "bars", "title": "Area per person", "subtitle":
              "m²", "format": "{:.1f}",
              "categories": ["Old buildings", "Wharf Street"],
              "series": [{"name": "m²", "values": [13.4, 11.5],
                          "colors": [4, 0]}]},
         ]},
    ],
}
