"""Change Impact Assessment of Wharf Street HQ Move: the project and everything
the document could say. The typesetting keeps what fits into four pages, the
most important first."""

PROJECT = {
    "name": "Wharf Street HQ Move",
    "code": "WS-HQ",
    "author": "Nadia Benali, Change Lead",
}

GROUPS = ["Sales", "Customer service", "Product", "Design", "Data",
          "Finance", "Legal", "People", "Labs", "Executive"]

IMPACT = {"High": "bad", "Medium": "warn", "Low": "good", "None":
          "neutral"}

DOCUMENT = {
    "title": "Change Impact Assessment",
    "subtitle": "How hard the move to Wharf Street hits each group, and "
                "the support each group will get",
    "meta": [("Project", "WS-HQ"), ("Groups", "10"),
             ("Survey", "1,012 answers"), ("High impact", "4 groups"),
             ("Change lead", "Nadia Benali")],
    "sections": [
        {"heading": "Impact by group and area", "kind": "figure",
         "weight": 0.1, "height": {1: 200, 2: 210, 4: 220},
         "charts": [{"type": "heatmap", "rows": GROUPS,
          "cols": ["Commute", "Desk sharing", "Ways of working",
                   "Technology", "Storage", "Team location"],
          "values": [["Medium", "High", "Medium", "Low", "Low", "Low"],
                     ["Medium", "Low", "Low", "Medium", "Low", "Low"],
                     ["Low", "High", "Medium", "Low", "Low", "Medium"],
                     ["Low", "High", "Low", "Low", "High", "Low"],
                     ["High", "High", "Medium", "Low", "Low", "Medium"],
                     ["Medium", "Medium", "Medium", "Low", "High",
                      "Low"],
                     ["Medium", "Medium", "Low", "Low", "High", "Low"],
                     ["Low", "Medium", "Low", "Low", "Medium", "Low"],
                     ["High", "None", "High", "High", "Medium", "Low"],
                     ["Low", "Low", "Low", "Low", "Low", "None"]],
          "badges": IMPACT, "labels": 0.18}]},
        {"heading": "What changes", "kind": "bullets", "weight": 0.2,
         "step": 0.15, "items": [
             "**From owned desks to shared ones** for most teams, at "
             "0.79 desks per person, booked in an app.",
             "**From three buildings to one**: Station Road people "
             "travel 25 minutes longer on average, Canal House people "
             "8 minutes less.",
             "**From paper to digital**: 60 % of files cleared, lockers "
             "instead of pedestals.",
         ]},
        {"heading": "Readiness", "kind": "figure", "weight": 0.3,
         "height": {1: 150, 2: 165, 4: 175}, "widths": [3, 2],
         "charts": [
             {"type": "bars", "horizontal": True, "title": "Ready for "
              "the move", "subtitle": "% agree, survey of June",
              "format": "{:.0f}%", "target": 70, "target_label": "aim",
              "categories": GROUPS,
              "series": [{"name": "Ready", "values": [61, 74, 66, 52,
                                                      48, 63, 70, 81, 39,
                                                      88],
                          "colors": ["warn", "good", "warn", "bad", "bad",
                                     "warn", "good", "good", "bad",
                                     "good"]}]},
             {"type": "donut", "title": "How people feel",
              "segments": [("Excited", 31, "good"),
                           ("Open", 34, 0), ("Worried", 26, "warn"),
                           ("Against", 9, "bad")],
              "format": "{:.0f}%", "center": ("1,012", "answers")},
         ]},
        {"heading": "Support by group", "kind": "table", "weight": 0.4,
         "step": 0.1, "min_pages": 2, "badges": IMPACT,
         "columns": [("Group", 1.4), ("Impact", 0.9, "center"),
                     ("Main concern", 2.6), ("Support", 3)],
         "rows": [
             ["Labs", "High", "Instruments and longer commute",
              "Instruments moved by makers; shuttle from Station Road "
              "for a year"],
             ["Data", "High", "No fixed desk with two screens",
              "Team zone with dual-screen desks; focus booths"],
             ["Design", "High", "Where do the samples and boards go?",
              "Project room on floor 4 for the team only"],
             ["Sales", "Medium", "Noise on calls", "Phone booths and "
              "anchor days on Monday and Thursday"],
             ["Finance", "Medium", "Paper files", "Scanning service "
              "for three months before the move"],
         ]},
        {"heading": "Concerns from the survey", "kind": "figure",
         "weight": 0.5, "min_pages": 2, "height": 155, "charts": [{
             "type": "bars", "horizontal": True, "format": "{:.0f}%",
             "title": "Top concerns", "subtitle": "% who chose it, up to "
             "three each",
             "categories": ["Finding a desk", "Noise", "Commute",
                            "Storage", "Meeting rooms",
                            "Losing the team spirit", "Parking"],
             "series": [{"name": "Concern", "values": [58, 46, 39, 33,
                                                       28, 24, 19]}]}]},
        {"heading": "Change plan", "kind": "figure", "weight": 0.6,
         "min_pages": 2, "charts": [{"type": "chevrons", "steps": [
             {"label": "Aware", "status": "done",
              "sub": "Town halls, the move site, FAQs (Mar – May)"},
             {"label": "Involved", "status": "done",
              "sub": "Change champions, floor tours (Jun – Jul)"},
             {"label": "Ready", "status": "now",
              "sub": "Desk booking pilot, packing guides (Aug)"},
             {"label": "Moved", "sub": "Floor walkers, welcome desk "
                                      "(Sep – Oct)"},
             {"label": "Settled", "sub": "Pulse surveys, fixes "
                                        "(Nov – Jan)"},
         ]}]},
        {"heading": "Champions", "kind": "figure", "weight": 0.8,
         "min_pages": 4, "height": 140, "widths": [3, 2], "charts": [
             {"type": "bars", "title": "Change champions per group",
              "categories": ["Sales", "Service", "Product", "Design",
                             "Data", "Finance", "Legal", "People",
                             "Labs", "Exec"],
              "series": [{"name": "Champions",
                          "values": [8, 7, 6, 4, 5, 4, 2, 3, 3, 1]}]},
             {"type": "progress", "title": "Champion activity",
              "format": "{:.0f} %", "items": [
                  {"label": "Ran a team session", "value": 86,
                   "status": "good"},
                  {"label": "Did the floor tour", "value": 74,
                   "status": "good"},
                  {"label": "Tested the booking app", "value": 58,
                   "status": "warn"},
              ]},
         ]},
        {"heading": "Resistance", "kind": "text", "weight": 0.9,
         "step": 0.3, "min_pages": 4, "paragraphs": [
             "The Labs team signed a letter against the move in May. "
             "Their concerns are real: a longer commute for most of "
             "them and the risk to instruments. The shuttle bus and the "
             "makers' engineers answer the practical part; the director "
             "of research now meets them monthly.",
             "Elsewhere, worry is mostly about desk sharing. The booking "
             "pilot on floor 7 in August will show whether 0.79 works "
             "in practice before the waves begin.",
         ]},
        {"heading": "Pulse after the move", "kind": "figure",
         "weight": 1.0, "min_pages": 4, "height": 145, "charts": [{
             "type": "line", "title": "Planned pulse survey", "subtitle":
             "% positive about the new office",
             "x": ["Jun", "Aug", "Oct", "Dec", "Feb"], "format": "{:.0f}",
             "target": 70, "target_label": "aim",
             "series": [{"name": "Actual", "values": [65, None, None,
                                                      None, None]},
                        {"name": "Expected", "dash": True, "color": 1,
                         "values": [65, 66, 58, 68, 74]}],
             "marks": [(2, "move dip")]}]},
        {"heading": "Measures", "kind": "tags", "weight": 1.1,
         "step": 0.1, "min_pages": 4, "items": [
             ("Adoption", "desk bookings per person per week"),
             ("Experience", "pulse survey, every two months"),
             ("Productivity", "self-rated, and meeting room use"),
             ("Retention", "leavers who name the office as a reason"),
         ]},
        {"heading": "Commute", "kind": "figure", "weight": 1.15,
         "min_pages": 4, "height": 150, "widths": [3, 2], "charts": [
             {"type": "bars", "title": "Change in commute", "subtitle":
              "minutes each way, average, by old building",
              "format": "{:+.0f}",
              "categories": ["Canal House", "Brickworks", "Station Road"],
              "series": [{"name": "Change", "values": [-8, 4, 25],
                          "colors": ["good", "warn", "bad"]}]},
             {"type": "donut", "title": "How people will travel",
              "segments": [("Train and tram", 46), ("Bike and walk", 22),
                           ("Bus", 17), ("Car", 15)],
              "format": "{:.0f}%", "center": ("1,240", "people")},
         ]},
        {"heading": "Managers' role", "kind": "bullets", "weight": 1.2,
         "step": 0.2, "min_pages": 4, "items": [
             "Hold a team session on the move before the floor tour, "
             "using the manager pack.",
             "Agree the team's anchor days and how the zone will be "
             "used.",
             "Spot people who struggle and tell the change team early, "
             "in confidence.",
             "Be on the floor on the first Monday after the move.",
         ]},
        {"heading": "Risks", "kind": "table", "weight": 1.25, "step": 0.1,
         "min_pages": 4, "badges": {"High": "bad", "Medium": "warn",
                                    "Low": "good"},
         "columns": [("Risk", 3.4), ("Level", 0.9, "center"),
                     ("Response", 3)],
         "rows": [
             ["Labs staff leave over the commute", "High",
              "Shuttle, flexible start times, a review after 6 months"],
             ["Desk sharing fails on busy days", "Medium",
              "Pilot on floor 7; anchor days spread across the week"],
             ["Managers do not hold team sessions", "Medium",
              "Champions follow up; HR business partners join"],
         ]},
    ],
}
