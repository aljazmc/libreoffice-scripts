"""Launch Campaign Plan of FROSTBYTE-1 CubeSat: the project and everything the
document could say. The typesetting keeps what fits into four pages, the
most important first."""

PROJECT = {
    "name": "FROSTBYTE-1 CubeSat",
    "code": "FB1",
    "author": "Dr Kaisa Virtanen, Project Manager",
}

DOCUMENT = {
    "title": "Launch Campaign Plan",
    "subtitle": "From shipping the flight model to the first ice data · "
                "rideshare on Transporter-14, target launch 9 September "
                "2027",
    "meta": [("Mission", "FROSTBYTE-1"), ("Launch", "L = 9 Sep 2027"),
             ("Site", "Vandenberg SLC-4E"), ("Integration", "L−30"),
             ("Document", "FB1-PM-031")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "height": {1: 285, 2: 300,
                                                       4: 310},
         "charts": [{"type": "gantt", "start": -70, "end": 30,
          "ticks": [(-70, "L−70"), (-60, "L−60"), (-50, "L−50"),
                    (-40, "L−40"), (-30, "L−30"), (-20, "L−20"),
                    (-10, "L−10"), (0, "L"), (10, "L+10"),
                    (20, "L+20"), (30, "L+30")],
          "groups": ["Satellite", "Launch provider", "Operations",
                     "Reviews"],
          "today": -70, "today_label": "plan", "labels": 0.24,
          "tasks": [
              {"label": "Before shipping", "section": True,
               "start": -70, "end": -45},
              {"label": "Flight acceptance review", "start": -66,
               "milestone": True, "text": "go to ship"},
              {"label": "Final functional tests", "start": -70,
               "end": -58},
              {"label": "Battery charged, pack and ship", "start": -58,
               "end": -48, "critical": True, "text": "air freight"},
              {"label": "At the dispenser integrator", "section": True,
               "start": -48, "end": -25},
              {"label": "Arrival and inspection", "start": -48,
               "end": -44, "group": 1},
              {"label": "Fit check and integration in dispenser",
               "start": -40, "end": -32, "group": 1, "critical": True},
              {"label": "Last access, remove before flight tags",
               "start": -30, "milestone": True, "text": "L−30"},
              {"label": "Dispenser to the launch site", "start": -28,
               "end": -18, "group": 1},
              {"label": "Launch and early orbit", "section": True,
               "start": 0, "end": 30},
              {"label": "Launch readiness review", "start": -3,
               "milestone": True},
              {"label": "Launch and separation", "start": 0, "end": 0.6,
               "critical": True, "text": "T+58 min"},
              {"label": "LEOP: first contact, detumble", "start": 0,
               "end": 5, "group": 2},
              {"label": "Antenna deployment", "start": 5, "end": 7,
               "group": 2, "critical": True},
              {"label": "Commissioning", "start": 7, "end": 24,
               "group": 2},
              {"label": "First ice data", "start": 25, "milestone": True,
               "text": "L+25"},
          ]}]},
        {"heading": "Key dates", "kind": "table", "weight": 0.2,
         "step": 0.1, "columns": [("Date", 1.1), ("Event", 3.2),
                                  ("Who", 1.6), ("Gate", 1.8)],
         "rows": [
             ["4 Jul", "Flight acceptance review", "Review board",
              "Go to ship"],
             ["13 Jul", "Ship to the dispenser integrator", "AIT",
              "Shipping checklist"],
             ["31 Jul – 8 Aug", "Integration in the dispenser",
              "AIT, provider", "Fit check signed"],
             ["10 Aug", "Last access to the satellite", "AIT",
              "Battery at 60 %"],
             ["6 Sep", "Launch readiness review", "Provider, us",
              "Go for launch"],
             ["9 Sep", "Launch", "Provider", "—"],
             ["4 Oct", "End of commissioning", "Operations",
              "Go for science"],
         ]},
        {"heading": "First passes", "kind": "figure", "weight": 0.4,
         "min_pages": 2, "height": 150, "widths": [3, 2], "charts": [
             {"type": "bars", "title": "Contact minutes per day",
              "subtitle": "first week, by ground station",
              "stacked": True, "categories": ["L", "L+1", "L+2", "L+3",
                                              "L+4", "L+5", "L+6"],
              "series": [{"name": "Kiruna", "values": [18, 42, 42, 44,
                                                       42, 43, 42]},
                         {"name": "Svalbard (rented)", "values": [22, 61,
                                                                  60, 62,
                                                                  61, 0,
                                                                  0]},
                         {"name": "University", "color": 4,
                          "values": [8, 20, 21, 20, 22, 21, 20]}]},
             {"type": "donut", "title": "LEOP team",
              "segments": [("Operators", 6), ("Engineers", 8),
                           ("Students", 10), ("Provider liaison", 1)],
              "center": ("25", "people")},
         ]},
        {"heading": "Go / no-go", "kind": "bullets", "weight": 0.5,
         "step": 0.15, "min_pages": 2, "items": [
             "**Ship:** all flight acceptance tests passed; no open "
             "non-conformance on flight hardware.",
             "**Last access:** battery between 55 and 65 %, inhibits "
             "verified by two people.",
             "**Launch:** ground stations tested with a satellite "
             "simulator; LEOP team rehearsed twice.",
         ]},
        {"heading": "Contingencies", "kind": "entries", "weight": 0.7,
         "step": 0.2, "inner": 0.1, "min_pages": 4, "entries": [
             {"title": "No contact after 24 hours", "text": [
                 "Ask the radio amateur network for beacon reports; "
                 "send a reset command from all three stations at every "
                 "pass."]},
             {"title": "Antenna fails to deploy", "text": [
                 "Retry with the second burn wire; then a thermal "
                 "cycle by pointing the antenna to the sun."]},
             {"title": "Launch slips more than 30 days", "text": [
                 "Battery recharged at the site under the provider's "
                 "procedure; the satellite stays in the dispenser."]},
         ]},
        {"heading": "People on the campaign", "kind": "figure",
         "weight": 0.8, "min_pages": 4, "height": 130, "charts": [{
             "type": "heatmap", "rows": ["AIT lead", "Systems engineer",
                                         "Two AIT technicians",
                                         "Mission operators",
                                         "Project manager"],
             "cols": ["Shipping", "Integration", "Launch site", "LEOP",
                      "Commissioning"],
             "values": [["Lead", "Lead", "Remote", "Support", ""],
                        ["Support", "Support", "On site", "Lead",
                         "Lead"],
                        ["Lead", "Lead", "", "", ""],
                        ["", "", "", "Lead", "Lead"],
                        ["Support", "Support", "On site", "Support",
                         "Support"]],
             "badges": {"Lead": "bad", "Support": "warn", "On site": 0,
                        "Remote": 4}, "labels": 0.24}]},
        {"heading": "Shipping", "kind": "tags", "weight": 0.9,
         "step": 0.1, "min_pages": 4, "items": [
             ("Container", "nitrogen-purged, shock and humidity logged"),
             ("Battery", "shipped at 30 % under dangerous goods rules"),
             ("Escort", "AIT lead travels with the container"),
             ("Insurance", "€1.2m transit cover"),
         ]},
        {"heading": "Commissioning", "kind": "figure", "weight": 1.0,
         "min_pages": 4, "charts": [{"type": "chevrons", "steps": [
             {"label": "Detumble", "status": "now",
              "sub": "L to L+2 · rates under 1°/s"},
             {"label": "Sun pointing", "sub": "L+2 · batteries "
                                             "charging"},
             {"label": "Deploy antenna", "sub": "L+5 · over Kiruna, "
                                              "both stations"},
             {"label": "Payload on", "sub": "L+10 · noise and "
                                           "calibration"},
             {"label": "Science", "sub": "L+25 · first ice map"},
         ]}]},
        {"heading": "Launch window", "kind": "figure", "weight": 1.05,
         "min_pages": 4, "height": 120, "charts": [{"type": "bars",
          "title": "Chance of launch on each day", "subtitle": "%, "
          "provider's weather and range statistics", "format":
          "{:.0f}", "categories": ["9 Sep", "10", "11", "12", "13", "14",
                                  "15"],
          "series": [{"name": "Chance", "values": [72, 78, 81, 80, 76, 83,
                                                   85]}]}]},
    ],
}
