"""Sprint Review of Pocket Bank App Relaunch: the project and everything the
document could say. The typesetting keeps what fits into two pages, the most
important first."""

PROJECT = {
    "name": "Pocket Bank App Relaunch",
    "code": "PB-5",
    "author": "Jonas Weber, Scrum Master, Home squad",
}

DAYS = ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10"]

DOCUMENT = {
    "title": "Sprint 14 Review",
    "subtitle": "Home squad · 18 – 29 August 2026 · Sprint goal: customers "
                "can see this month's spending on the new home screen",
    "meta": [("Squad", "Home"), ("Sprint", "14 of 18"),
             ("Product owner", "Mia Laine"), ("Goal", "Met")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "charts": [{"type": "kpis",
         "tiles": [
             {"label": "Committed", "value": "34 pts", "status": 0,
              "note": "9 stories"},
             {"label": "Done", "value": "31 pts", "status": "good",
              "note": "8 stories, 91 %", "delta": "+3 vs avg"},
             {"label": "Carried over", "value": "3 pts", "status": "warn",
              "note": "1 story"},
             {"label": "Escaped bugs", "value": "0", "status": "good",
              "note": "from sprint 13"},
         ]}]},
        {"heading": "Burndown", "kind": "figure", "weight": 0.2,
         "height": {1: 165, 2: 175, 4: 210}, "widths": [3, 2], "charts": [
             {"type": "line", "title": "Story points remaining",
              "x": DAYS + ["End"], "markers": True,
              "series": [
                  {"name": "Ideal", "dash": True, "color": 4,
                   "values": [34, 30.6, 27.2, 23.8, 20.4, 17, 13.6, 10.2,
                              6.8, 3.4, 0]},
                  {"name": "Actual", "color": 0, "area": True,
                   "values": [34, 34, 31, 31, 26, 21, 21, 13, 8, 3, 3]},
                  {"name": "Scope", "color": 2,
                   "values": [34, 34, 34, 36, 36, 34, 34, 34, 34, 34,
                              34]}],
              "marks": [(3, "+2 pts bug"), (5, "−2 pts split")]},
             {"type": "bars", "title": "Velocity", "subtitle": "points",
              "categories": ["S9", "S10", "S11", "S12", "S13", "S14"],
              "target": 28, "target_label": "average",
              "series": [{"name": "Velocity",
                          "values": [22, 26, 29, 27, 30, 31],
                          "colors": [4, 4, 4, 4, 4, 0]}]},
         ]},
        {"heading": "What we finished", "kind": "table", "weight": 0.3,
         "step": 0.1, "badges": {"Done": "good", "Carried": "warn"},
         "columns": [("Story", 4), ("Points", 0.8, "center"),
                     ("Status", 1, "center")],
         "rows": [
             ["Spending this month, on the home screen", "8", "Done"],
             ["Tap the total to see the list of payments", "5", "Done"],
             ["Merchant logos for the top 500 merchants", "3", "Done"],
             ["Empty state for new customers", "2", "Done"],
             ["Accessibility: totals read out by VoiceOver and TalkBack",
              "3", "Done"],
             ["Performance: home screen under 800 ms on a mid-range "
              "phone", "5", "Done"],
             ["Bug: pending payments counted twice", "2", "Done"],
             ["Analytics events for the home screen", "3", "Done"],
             ["Compare with last month", "3", "Carried"],
         ]},
        {"heading": "Demo feedback", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "charts": [{"type": "board", "columns": [
             {"title": "Loved", "tone": "good", "cards": [
                 ("“Finally I can see where it all went without "
                  "scrolling.”", "customer panel, 6 of 8"),
                 ("Logos make the list scannable", "Head of CX"),
             ]},
             {"title": "Questions", "tone": "warn", "cards": [
                 ("Does the total include pending card payments?",
                  "Compliance"),
                 ("Can I hide the total in public?", "customer panel"),
             ]},
             {"title": "Ideas for later", "tone": "info", "cards": [
                 ("Show spending by category", "customer panel"),
                 ("A widget for the phone's home screen", "Marketing"),
             ]},
         ]}]},
        {"heading": "Quality", "kind": "figure", "weight": 0.6,
         "min_pages": 2, "height": 120, "widths": [1, 1], "charts": [
             {"type": "progress", "title": "Definition of done",
              "format": "{:.0f} %", "items": [
                  {"label": "Unit test coverage", "value": 86,
                   "target": 80, "status": "good"},
                  {"label": "UI tests passing", "value": 100,
                   "status": "good"},
                  {"label": "Accessibility checks", "value": 100,
                   "status": "good"},
                  {"label": "Crash-free sessions (beta)", "value": 99.6,
                   "display": "99.6 %", "target": 99.5,
                   "status": "good"}]},
             {"type": "bars", "title": "Bugs this sprint",
              "stacked": True, "categories": ["Found", "Fixed", "Open"],
              "series": [{"name": "Critical", "color": "bad",
                          "values": [1, 1, 0]},
                         {"name": "Major", "color": "warn",
                          "values": [3, 3, 0]},
                         {"name": "Minor", "color": 4,
                          "values": [7, 5, 2]}]},
         ]},
        {"heading": "Scope change", "kind": "text", "weight": 0.8,
         "step": 0.3, "min_pages": 2, "paragraphs": [
             "On day 4 the double-counting of pending payments reached "
             "the beta group and was pulled into the sprint (+2 points). "
             "To protect the goal, the product owner split *Compare with "
             "last month* in two on day 6 and moved the comparison chart "
             "to sprint 15.",
         ]},
        {"heading": "Where the time went", "kind": "figure",
         "weight": 1.0, "min_pages": 4, "height": 150, "widths": [2, 3],
         "charts": [
             {"type": "donut", "title": "Squad hours",
              "segments": [("Stories", 61), ("Bugs", 9),
                           ("Ceremonies", 12), ("Support", 8),
                           ("Learning", 10)],
              "format": "{:.0f}%", "center": ("520 h", "7 people")},
             {"type": "bars", "title": "Cycle time by story",
              "subtitle": "days, start to done", "horizontal": True,
              "format": "{:.1f}", "target": 4, "target_label": "target",
              "categories": ["Spending total", "Payment list", "Logos",
                             "Empty state", "Accessibility",
                             "Performance", "Pending bug", "Analytics"],
              "series": [{"name": "Days",
                          "values": [6.5, 4.0, 2.5, 1.0, 3.0, 5.5, 1.5,
                                     2.0],
                          "colors": ["warn", 0, 0, 0, 0, "warn", 0, 0]}]},
         ]},
        {"heading": "Release burnup", "kind": "figure", "weight": 0.95,
         "min_pages": 4, "height": 175, "charts": [{"type": "line",
          "title": "Release 5.0, points done against scope",
          "x": ["S9", "S10", "S11", "S12", "S13", "S14", "S15", "S16"],
          "end_labels": True,
          "series": [
              {"name": "Scope", "color": 2,
               "values": [180, 185, 190, 196, 196, 198, 198, 198]},
              {"name": "Done", "color": 0, "area": True,
               "values": [22, 48, 77, 104, 134, 165, None, None]},
              {"name": "Forecast", "color": 0, "dash": True,
               "values": [None, None, None, None, None, 165, 194,
                          223]}]}]},
        {"heading": "Team availability", "kind": "figure", "weight": 0.97,
         "min_pages": 4, "height": 125, "charts": [{"type": "heatmap",
          "rows": ["Mia (PO)", "Aisha (iOS)", "Leo (iOS)",
                   "Sam (Android)", "Ravi (backend)", "Ines (design)",
                   "Tom (QA)"],
          "cols": DAYS, "row": 13,
          "values": [["In"] * 10,
                     ["In"] * 10,
                     ["In"] * 6 + ["Off"] * 2 + ["In"] * 2,
                     ["In"] * 10,
                     ["In", "In", "Sup", "Sup", "In", "In", "In", "In",
                      "In", "In"],
                     ["In"] * 4 + ["Off"] + ["In"] * 5,
                     ["In"] * 10],
          "badges": {"In": "good", "Off": "neutral", "Sup": "warn"},
          "show": False}]},
        {"heading": "Stakeholders present", "kind": "tags", "weight": 1.2,
         "step": 0.1, "min_pages": 4, "items": [
             ("Product", "Priya Raman, Mia Laine"),
             ("Customer experience", "Ola Mensah"),
             ("Compliance", "Rafael Ortiz"),
             ("Marketing", "Hana Sato"),
             ("Customer panel", "eight customers, remote"),
         ]},
        {"heading": "Next sprint", "kind": "entries", "weight": 0.9,
         "step": 0.2, "inner": 0.1, "min_pages": 4, "entries": [
             {"title": "Sprint 15 goal", "dates": "1 – 12 Sep", "text": [
                 "Customers can compare this month's spending with last "
                 "month's and understand why it changed."],
              "items": [
                  "Comparison chart (carried over, 3 points)",
                  "Pending card payments shown separately (Compliance)",
                  "Hide the total with a tap",
                  "Release 5.0 hardening: performance on old Android "
                  "phones"]},
         ]},
        {"heading": "Release readiness", "kind": "figure", "weight": 1.1,
         "min_pages": 4, "charts": [{"type": "chevrons", "steps": [
             {"label": "Sprint 13", "status": "done",
              "sub": "Login and home screen shell"},
             {"label": "Sprint 14", "status": "done",
              "sub": "Spending on the home screen"},
             {"label": "Sprint 15", "status": "now",
              "sub": "Comparison, hardening"},
             {"label": "Sprint 16", "sub": "Release candidate, beta to "
                                           "5 % of customers"},
             {"label": "5.0 live", "sub": "15 October"},
         ]}]},
        {"heading": "Notes", "kind": "bullets", "weight": 1.5, "step": 0.2,
         "min_pages": 4, "items": [
             "The customer panel will now join every second review.",
             "Compliance asked to see the copy of every new money "
             "number before the sprint starts, not at the review.",
             "Thanks to the Cards squad for lending us a tester for "
             "three days.",
         ]},
    ],
}
