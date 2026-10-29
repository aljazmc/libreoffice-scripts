"""Consent Tracker of Northgate Offshore Wind: the project and everything the
document could say. The typesetting keeps what fits into one page, the most
important first."""

PROJECT = {
    "name": "Northgate Offshore Wind",
    "code": "NOW-1",
    "author": "Clara Mendes, Consents Manager",
}

STATUS = {"Granted": "good", "Discharging": "info", "In review": "warn",
          "At risk": "bad", "Not started": "neutral"}

DOCUMENT = {
    "title": "Consent Tracker",
    "subtitle": "Every consent, licence and condition the wind farm "
                "needs, from the seabed to the substation · March 2026",
    "meta": [("Project", "NOW-1"), ("Consents", "27"),
             ("Granted", "21"), ("Conditions", "146"),
             ("Owner", "Clara Mendes")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "height": {1: 120, 2: 130},
         "widths": [2, 3], "charts": [
             {"type": "donut", "title": "Consents",
              "segments": [("Granted", 21, "good"),
                           ("In review", 4, "warn"),
                           ("At risk", 1, "bad"),
                           ("Not started", 1, "neutral")],
              "center": ("27", "consents")},
             {"type": "progress", "title": "Conditions discharged",
              "format": "{:.0f}", "max": 146, "items": [
                  {"label": "Pre-construction", "value": 58,
                   "display": "58 / 71", "status": "warn"},
                  {"label": "During construction", "value": 12,
                   "display": "12 / 49", "status": 0},
                  {"label": "Operation", "value": 0, "display": "0 / 26",
                   "status": 4},
              ]},
         ]},
        {"heading": "Consents on the critical path", "kind": "figure",
         "weight": 0.2, "height": {1: 165, 2: 185, 4: 200},
         "charts": [{"type": "gantt",
          "columns": ["Q1 25", "Q2", "Q3", "Q4", "Q1 26", "Q2", "Q3",
                      "Q4", "Q1 27", "Q2"],
          "groups": ["Offshore", "Onshore", "Grid"], "today": 4.6,
          "tasks": [
              {"label": "Development consent order", "start": 0,
               "end": 1.2, "progress": 1, "text": "granted"},
              {"label": "Marine licence", "start": 0, "end": 2,
               "progress": 1},
              {"label": "Protected species licence", "start": 3,
               "end": 6.2, "progress": 0.4, "critical": True,
               "text": "harbour porpoise"},
              {"label": "Piling noise plan approval", "start": 4,
               "end": 6.5, "progress": 0.2, "critical": True},
              {"label": "Onshore cable route, planning", "start": 1,
               "end": 3.5, "group": 1, "progress": 1},
              {"label": "Landfall drilling permit", "start": 3.5,
               "end": 5.5, "group": 1, "progress": 0.6},
              {"label": "Substation building control", "start": 4.5,
               "end": 6, "group": 1, "progress": 0.1},
              {"label": "Grid connection agreement", "start": 0,
               "end": 1.5, "group": 2, "progress": 1},
              {"label": "Foundation installation starts", "start": 8,
               "milestone": True, "text": "needs all offshore"},
          ]}]},
        {"heading": "Register", "kind": "table", "weight": 0.3,
         "step": 0.06, "badges": STATUS,
         "columns": [("Consent", 3), ("Authority", 2),
                     ("Due", 0.9), ("Status", 1.1, "center")],
         "rows": [
             ["Development consent order", "Energy ministry",
              "Granted", "Granted"],
             ["Marine licence", "Marine agency", "Granted",
              "Discharging"],
             ["Protected species licence (porpoise)", "Nature agency",
              "Jun 26", "At risk"],
             ["Piling noise management plan", "Marine agency",
              "Jul 26", "In review"],
             ["Unexploded ordnance clearance", "Marine agency",
              "May 26", "In review"],
             ["Landfall drilling permit", "Coastal council", "May 26",
              "In review"],
             ["Substation building control", "Eastport council",
              "Aug 26", "In review"],
             ["Aviation lighting", "Aviation authority", "Granted",
              "Granted"],
             ["Navigation risk assessment", "Coastguard", "Granted",
              "Granted"],
             ["Archaeology written scheme", "Heritage body", "Granted",
              "Discharging"],
             ["Operations base lease", "Eastport harbour", "Sep 26",
              "Not started"],
         ]},
        {"heading": "The porpoise licence", "kind": "text", "weight": 0.4,
         "step": 0.3, "min_pages": 2, "paragraphs": [
             "The site lies at the edge of a protected area for harbour "
             "porpoise. The nature agency asked in February for a third "
             "season of acoustic monitoring data before it decides, "
             "which would push the decision to December and the first "
             "piling to 2029.",
             "We have offered instead a bubble curtain around every pile, "
             "a 30-minute soft start and no piling between January and "
             "April, when the porpoises calve. A decision on the offer "
             "is expected on 15 May.",
         ]},
        {"heading": "Conditions by theme", "kind": "figure",
         "weight": 0.5, "min_pages": 2, "height": 160, "charts": [{
             "type": "bars", "horizontal": True, "stacked": True,
             "categories": ["Marine mammals", "Birds", "Fish and "
                            "fisheries", "Navigation", "Archaeology",
                            "Onshore ecology", "Noise and traffic"],
             "series": [{"name": "Discharged", "color": "good",
                         "values": [6, 10, 9, 14, 8, 7, 16]},
                        {"name": "Submitted", "color": "warn",
                         "values": [5, 3, 2, 1, 1, 4, 2]},
                        {"name": "To do", "color": "neutral",
                         "values": [9, 8, 7, 9, 3, 10, 12]}],
             "inside": True}]},
        {"heading": "Stakeholders", "kind": "figure", "weight": 0.7,
         "min_pages": 4, "height": 175, "charts": [{"type": "quadrant",
          "x": "interest", "y": "influence on consents",
          "quadrants": ["Keep satisfied", "Manage closely", "Monitor",
                        "Keep informed"],
          "points": [("Nature agency", 7, 9.5, "bad"),
                     ("Marine agency", 6, 8.5, 0),
                     ("Coastal council", 7.5, 6.5, 0),
                     ("Fishing association", 9, 5, "warn"),
                     ("Bird trust", 8.5, 4, 1),
                     ("Eastport harbour", 5, 6, 0),
                     ("Ferry operator", 4, 3.5, 2),
                     ("Residents at landfall", 8, 2.5, 2),
                     ("Coastguard", 3, 7, 0)]}]},
        {"heading": "Surveys", "kind": "table", "weight": 0.8,
         "step": 0.1, "min_pages": 4, "badges": STATUS,
         "columns": [("Survey", 3), ("Season", 1.6),
                     ("For", 2), ("Status", 1.1, "center")],
         "rows": [
             ["Acoustic monitoring, porpoise", "Year 3, 2026",
              "Species licence", "In review"],
             ["Bird collision radar", "Spring 2026", "Condition 18",
              "Discharging"],
             ["Benthic grab samples", "Summer 2025", "Marine licence",
              "Granted"],
             ["Unexploded ordnance, magnetometer", "Winter 2025",
              "UXO clearance", "Granted"],
             ["Great crested newts, onshore", "Spring 2026",
              "Onshore route", "Not started"],
         ]},
        {"heading": "What happens if we are late", "kind": "entries",
         "weight": 0.9, "step": 0.2, "inner": 0.1, "min_pages": 4,
         "entries": [
             {"title": "Porpoise licence after August",
              "dates": "high impact", "text": [
                  "No piling in 2028: first power slips a year, NPV −€140m. "
                  "The vessel charter has a one-season deferral at "
                  "€18m."]},
             {"title": "Landfall drilling after June",
              "dates": "medium", "text": [
                  "Drilling moves to the autumn window; cable pull-in "
                  "still possible before the 2028 season."]},
             {"title": "Operations base lease", "dates": "low", "text": [
                 "Temporary offices in the port authority building are "
                 "available until 2030."]},
         ]},
        {"heading": "Next month", "kind": "bullets", "weight": 1.0,
         "step": 0.2, "min_pages": 4, "items": [
             "Meeting with the nature agency on the bubble curtain "
             "offer, 9 April.",
             "Submit the final piling noise plan with the curtain test "
             "results.",
             "Discharge conditions 31 to 37 (archaeology) with the "
             "heritage body.",
         ]},
        {"heading": "Consents over time", "kind": "figure", "weight": 1.05,
         "min_pages": 4, "height": 160, "widths": [3, 2], "charts": [
             {"type": "line", "title": "Conditions discharged",
              "subtitle": "cumulative, of 71 pre-construction",
              "x": ["Q3 25", "Q4", "Q1 26", "Q2", "Q3", "Q4"],
              "target": 71, "target_label": "all", "end_labels": True,
              "series": [{"name": "Actual", "area": True,
                          "values": [12, 31, 58, None, None, None]},
                         {"name": "Plan", "dash": True, "color": 1,
                          "values": [10, 28, 52, 64, 71, 71]}]},
             {"type": "bars", "title": "Days to a decision",
              "subtitle": "average, by authority", "horizontal": True,
              "format": "{:.0f}",
              "categories": ["Marine agency", "Nature agency",
                             "Coastal council", "Heritage body"],
              "series": [{"name": "Days", "values": [46, 112, 38, 27],
                          "colors": [0, "bad", 0, 0]}]},
         ]},
        {"heading": "Conditions with the most work", "kind": "table",
         "weight": 1.1, "step": 0.1, "min_pages": 4, "badges": STATUS,
         "columns": [("No.", 0.6), ("Condition", 3.8), ("Owner", 1.3),
                     ("Status", 1.1, "center")],
         "rows": [
             ["M12", "Marine mammal mitigation plan, with the bubble "
              "curtain", "Environment", "In review"],
             ["M18", "Bird collision monitoring for three years after "
              "commissioning", "Environment", "Discharging"],
             ["M24", "Fisheries liaison and compensation scheme",
              "Stakeholders", "Discharging"],
             ["M31", "Archaeological exclusion zones around 14 wrecks",
              "Engineering", "Discharging"],
             ["O07", "Hedgerow and badger mitigation on the cable route",
              "Onshore", "Not started"],
             ["O15", "Construction traffic plan for Eastport",
              "Onshore", "In review"],
         ]},
        {"kind": "callout", "weight": 1.15, "tone": "warn",
         "min_pages": 4, "label": "Watch:",
         "text": "the nature agency is short of staff until July; our "
                 "offer of a seconded ecologist to support its review "
                 "was accepted on 20 March."},
    ],
}
