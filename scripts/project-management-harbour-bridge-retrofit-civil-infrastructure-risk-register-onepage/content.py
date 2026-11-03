"""Risk Register of Harbour Bridge Retrofit: the project and everything the
document could say. The typesetting keeps what fits into one page, the most
important first."""

PROJECT = {
    "name": "Harbour Bridge Retrofit",
    "code": "HBR-24",
    "author": "Ana Novak, Project Manager, Port Aldwick City Works",
}

SCORES = {"25": "bad", "20": "bad", "16": "bad", "15": "bad", "12": "warn",
          "10": "warn", "9": "warn", "8": "warn", "6": "good", "5": "good",
          "4": "good", "3": "good", "2": "good"}

DOCUMENT = {
    "title": "Risk Register",
    "subtitle": "Open risks at the September 2026 project board",
    "meta": [("Project", "HBR-24"), ("Open risks", "23"),
             ("Above appetite", "4"), ("Risk owner", "Ana Novak"),
             ("Reviewed", "7 Sep 2026")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "charts": [{"type": "kpis",
         "tiles": [
             {"label": "Exposure", "value": "€3.2m", "delta": "▼ €0.6m",
              "delta_status": "good", "status": "warn",
              "note": "probability × cost, open risks"},
             {"label": "Contingency left", "value": "€1.7m",
              "status": "bad", "note": "covers 53 % of exposure"},
             {"label": "Red risks", "value": "4", "delta": "▼ 2",
              "delta_status": "good", "status": "bad",
              "note": "score 15 or more"},
             {"label": "Overdue actions", "value": "3", "status": "warn",
              "note": "of 41 open actions"},
         ]}]},
        {"heading": "Heat map", "kind": "figure", "weight": 0.2,
         "height": {1: 200, 2: 210, 4: 250}, "charts": [{"type": "risk",
          "risks": [
              ("R07", 4, 5, "Corrosion under the south span paint worse "
                            "than surveyed"),
              ("R12", 4, 4, "Pier 3 bearings seized, jacking load "
                            "higher than designed"),
              ("R03", 3, 5, "Fatigue cracks found at the cross-girder "
                            "welds"),
              ("R15", 4, 4, "Winter weather stops the paint curing"),
              ("R21", 3, 3, "Bus operator withdraws night diversions"),
              ("R09", 2, 4, "Lead paint found outside containment"),
              ("R18", 3, 2, "Peregrine nest moves to pier 3"),
              ("R04", 2, 3, "Surfacing subcontractor goes bust"),
          ],
          "residual": [("R07", 3, 4), ("R12", 2, 4), ("R03", 2, 4),
                       ("R15", 2, 3)]}]},
        {"heading": "Top risks", "kind": "table", "weight": 0.3, "step": 0.1,
         "badges": SCORES, "columns": [
             ("ID", 0.6), ("Risk", 3.2), ("Score", 0.7, "center"),
             ("Owner", 1.2), ("Response", 3.2)],
         "rows": [
             ["R07", "Corrosion under the south span paint is worse than "
              "the 2023 survey found", "20", "Halden",
              "Reduce: plate designs for 40 % loss pre-approved; €1.2m "
              "provisional sum"],
             ["R12", "Pier 3 bearings seized; jacking load higher than "
              "designed", "16", "Ferrand", "Reduce: reuse the pier 4 "
              "frames, strengthened; load cells on every jack"],
             ["R03", "Fatigue cracks at cross-girder welds", "15",
              "Halden", "Reduce: magnetic particle testing of every weld "
              "as it is exposed"],
             ["R15", "Winter stops the paint curing", "16", "Ferrand",
              "Avoid: heated, dehumidified enclosures from November"],
             ["R21", "Bus operator withdraws night diversions", "9",
              "Highways", "Share: diversion costs paid per night"],
             ["R09", "Lead paint outside containment", "8", "Ferrand",
              "Avoid: class A containment, daily air monitoring"],
             ["R18", "Peregrine nest moves to pier 3", "6", "Ecologist",
              "Accept: work around a 50 m zone if it happens"],
             ["R04", "Surfacing subcontractor fails", "6", "Ferrand",
              "Transfer: performance bond of 10 %"],
         ]},
        {"heading": "Exposure trend", "kind": "figure", "weight": 0.6,
         "min_pages": 2, "height": 165, "widths": [3, 2], "charts": [
             {"type": "bars", "title": "Open risks by rating",
              "stacked": True, "inside": True,
              "categories": ["Mar", "Apr", "May", "Jun", "Jul", "Aug",
                             "Sep"],
              "series": [
                  {"name": "Red", "color": "bad",
                   "values": [7, 7, 6, 6, 6, 6, 4]},
                  {"name": "Amber", "color": "warn",
                   "values": [11, 12, 12, 10, 10, 9, 9]},
                  {"name": "Green", "color": "good",
                   "values": [8, 9, 9, 10, 10, 10, 10]}]},
             {"type": "line", "title": "Exposure vs contingency",
              "subtitle": "€m", "x": ["Mar", "Apr", "May", "Jun", "Jul",
                                      "Aug", "Sep"],
              "format": "{:.1f}",
              "series": [
                  {"name": "Exposure", "color": "bad",
                   "values": [4.6, 4.4, 4.3, 4.1, 3.9, 3.8, 3.2]},
                  {"name": "Contingency", "color": 0,
                   "values": [3.4, 3.1, 2.8, 2.5, 2.2, 1.9, 1.7]}]},
         ]},
        {"heading": "Responses", "kind": "figure", "weight": 0.8,
         "min_pages": 2, "height": 120, "widths": [2, 3], "charts": [
             {"type": "donut", "title": "By strategy",
              "segments": [("Reduce", 13), ("Avoid", 4), ("Transfer", 3),
                           ("Accept", 2), ("Share", 1)],
              "center": ("23", "open risks")},
             {"type": "progress", "title": "Actions by owner",
              "max": 12, "format": "{:.0f} open",
              "items": [
                  {"label": "Ferrand Civils", "value": 12,
                   "status": "warn"},
                  {"label": "Halden Engineers", "value": 9, "status": 0},
                  {"label": "City Highways", "value": 7, "status": 0},
                  {"label": "Project team", "value": 9, "status": 0},
                  {"label": "Ecologist", "value": 4, "status": "good"}]},
         ]},
        {"heading": "Contingency drawdown", "kind": "figure",
         "weight": 1.0, "min_pages": 4, "height": 160, "charts": [{
             "type": "waterfall", "format": "€{:.1f}m",
             "axis_format": "{:.0f}", "invert": False,
             "steps": [("Contingency at start", 4.1),
                       ("R02 piling", -0.3), ("R07 corrosion, north", -0.9),
                       ("R11 traffic", -0.3), ("R12 jacking", -0.7),
                       ("R16 design", -0.2), ("Remaining", None)]}]},
        {"heading": "Where the risk sits", "kind": "figure",
         "weight": 1.05, "min_pages": 4, "height": 150, "widths": [3, 2],
         "charts": [
             {"type": "heatmap", "title": "Open risks by package and "
              "impact", "rows": ["Design", "Steel", "Paint", "Bearings",
                                 "Deck", "Traffic"],
              "cols": ["Cost", "Time", "Safety", "Environment",
                       "Reputation"],
              "values": [[2, 3, 0, 0, 0], [3, 2, 1, 0, 0],
                         [2, 3, 1, 2, 1], [3, 3, 2, 0, 0],
                         [1, 2, 1, 0, 1], [1, 1, 1, 0, 3]],
              "format": "{:.0f}"},
             {"type": "bars", "horizontal": True, "title": "Exposure",
              "subtitle": "€k", "format": "{:,.0f}",
              "categories": ["Steel", "Bearings", "Paint", "Traffic",
                             "Deck", "Design"],
              "series": [{"name": "Exposure",
                          "values": [1150, 820, 540, 310, 230, 150],
                          "colors": ["bad", "bad", "warn", 0, 0, 0]}]},
         ]},
        {"heading": "Top two in depth", "kind": "entries", "weight": 1.08,
         "step": 0.1, "inner": 0.05, "min_pages": 4, "entries": [
             {"title": "R07 Corrosion under the south span paint",
              "dates": "score 20 → 12", "fields": [
                  ("Cause", "The 2023 survey sampled 4 % of the steel, "
                            "mostly where it was easy to reach."),
                  ("Effect", "Up to 60 extra plates, €0.9m and four "
                             "weeks on the critical path."),
                  ("Trigger", "Section loss over 25 % found in more than "
                              "three bays once blasted."),
                  ("Response", "Plate designs for losses up to 40 % "
                               "approved in advance; plates cut in "
                               "batches of ten; a second plating crew "
                               "on call."),
                  ("Fallback", "Temporary weight limit of 26 t on the "
                               "south span until plated."),
              ]},
             {"title": "R12 Pier 3 bearings seized",
              "dates": "score 16 → 8", "fields": [
                  ("Cause", "Pier 4 showed that the bearings have not "
                            "moved for decades."),
                  ("Effect", "Jacking loads 30 % over design; frames "
                             "could deflect; €0.7m and three weeks."),
                  ("Trigger", "Any bearing not free after 40 % of the "
                              "design jacking load."),
                  ("Response", "Pier 4 frames reused and strengthened; "
                               "load cells on every jack; bearings cut "
                               "out rather than freed."),
                  ("Fallback", "Jack one girder at a time, adding two "
                               "nights per bearing."),
              ]},
         ]},
        {"heading": "Other open risks", "kind": "table", "weight": 1.1,
         "step": 0.1, "min_pages": 4,
         "badges": {**SCORES, "up": "bad", "down": "good"},
         "columns": [("ID", 0.6), ("Risk", 4), ("Score", 0.7, "center"),
                     ("Trend", 0.9, "center"), ("Owner", 1.3)],
         "rows": [
             ["R01", "Utilities in the deck not where the records say",
              "8", "steady", "Halden"],
             ["R05", "Steel delivery late from the mill", "6", "down",
              "Ferrand"],
             ["R06", "Complaints about night noise", "9", "up",
              "Comms"],
             ["R08", "Harbour authority changes the exclusion zone",
              "6", "steady", "Project"],
             ["R10", "Check engineer unavailable for load test", "4",
              "down", "Halden"],
             ["R11", "Diversion signage damaged or stolen", "6",
              "steady", "Highways"],
             ["R13", "Expansion joints from new supplier not approved",
              "8", "up", "Halden"],
             ["R14", "Scaffold struck by a vessel", "5", "steady",
              "Ferrand"],
             ["R16", "Late design changes from the check", "4", "down",
              "Halden"],
             ["R17", "Key staff leave the contractor", "6", "steady",
              "Ferrand"],
             ["R19", "Tall ships festival moved to September", "4",
              "steady", "Project"],
             ["R20", "Load test fails at the first attempt", "10", "up",
              "Halden"],
         ]},
        {"heading": "Closed this quarter", "kind": "bullets", "weight": 1.3,
         "step": 0.2, "min_pages": 4, "items": [
             "**R02** Piling for the temporary platform hits rock: closed "
             "when the platform was finished in June.",
             "**R16b** Lead found in the north span primer: contained, "
             "air tests clear for eight weeks.",
             "**R22** Steel price rise: all steel delivered.",
         ]},
        {"heading": "How we score", "kind": "text", "weight": 1.5,
         "step": 0.3, "min_pages": 4, "paragraphs": [
             "Likelihood and impact are each scored from 1 to 5; the "
             "score is their product. Impact is the worst of cost "
             "(5 means more than €1m), time (5 means more than eight "
             "weeks on the load test), safety and reputation. Our "
             "appetite is 12: anything above it needs a response the "
             "board has seen.",
             "Exposure is the probability times the most likely cost, "
             "summed over the open risks, and is compared every month "
             "with the contingency left.",
         ]},
        {"kind": "callout", "weight": 0.5, "tone": "bad", "min_pages": 2,
         "label": "Escalated to the board:",
         "text": "R07 and R12 together could cost more than the "
                 "contingency left. We ask the board to note the gap and "
                 "keep €0.4m of management reserve available until the "
                 "south span paint is off."},
    ],
}
