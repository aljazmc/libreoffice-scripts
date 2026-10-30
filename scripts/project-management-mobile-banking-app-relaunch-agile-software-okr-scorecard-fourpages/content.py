"""OKR Scorecard of Pocket Bank App Relaunch: the project and everything the
document could say. The typesetting keeps what fits into four pages, the
most important first."""

PROJECT = {
    "name": "Pocket Bank App Relaunch",
    "code": "PB-5",
    "author": "Priya Raman, Head of Product, Pocket Bank",
}

WEEKS = ["W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9", "W10",
         "W11", "W12", "W13"]

DOCUMENT = {
    "title": "Q3 OKR Scorecard",
    "subtitle": "Digital banking tribe · July to September 2026 · scored "
                "in week 11",
    "meta": [("Tribe", "Digital banking"), ("Quarter", "Q3 2026"),
             ("Week", "11 of 13"), ("Average score", "0.68")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "charts": [{"type": "kpis",
         "tiles": [
             {"label": "Objectives", "value": "3", "status": 0,
              "note": "9 key results"},
             {"label": "On track", "value": "5", "status": "good",
              "note": "score 0.7 or more"},
             {"label": "At risk", "value": "3", "status": "warn",
              "note": "0.4 to 0.7"},
             {"label": "Off track", "value": "1", "status": "bad",
              "note": "under 0.4"},
         ]}]},
        {"heading": "O1 · Make everyday banking effortless", "kind":
         "figure", "weight": 0.2, "charts": [{"type": "progress",
          "format": "{:.2f}", "max": 1, "items": [
              {"label": "KR1 Home screen loads in under 1 s for 90 %",
               "value": 0.9, "status": "good", "note": "0.94 s, from "
               "2.3 s"},
              {"label": "KR2 Login success rate 98 %", "value": 0.75,
               "status": "warn", "note": "97.2 %, from 94 %"},
              {"label": "KR3 Weekly active customers 48 %", "value": 0.6,
               "status": "warn", "note": "45 %, from 41 %"},
          ]}]},
        {"heading": "O2 · Help customers grow their money", "kind":
         "figure", "weight": 0.3, "charts": [{"type": "progress",
          "format": "{:.2f}", "max": 1, "items": [
              {"label": "KR1 Spaces in beta with 20,000 customers",
               "value": 1.0, "status": "good", "note": "23,400"},
              {"label": "KR2 Round-ups switched on by 30 % of them",
               "value": 0.8, "status": "good", "note": "26 %"},
              {"label": "KR3 €5m saved in Spaces", "value": 0.3,
               "status": "bad", "note": "€1.6m; savings approval late"},
          ]}]},
        {"heading": "O3 · Be there when it matters", "kind": "figure",
         "weight": 0.4, "charts": [{"type": "progress", "format": "{:.2f}",
          "max": 1, "items": [
              {"label": "KR1 Card freeze in the app in 2 taps",
               "value": 1.0, "status": "good", "note": "live 12 Aug"},
              {"label": "KR2 Card support calls down 30 %", "value": 0.7,
               "status": "good", "note": "−21 %"},
              {"label": "KR3 Chat vendor live for 10 % of customers",
               "value": 0.1, "status": "bad", "note": "contract not "
               "signed"},
          ]}]},
        {"heading": "Confidence", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": {2: 150, 4: 170},
         "charts": [{"type": "heatmap",
          "rows": ["O1 KR1", "O1 KR2", "O1 KR3", "O2 KR1", "O2 KR2",
                   "O2 KR3", "O3 KR1", "O3 KR2", "O3 KR3"],
          "cols": ["W1", "W3", "W5", "W7", "W9", "W11"],
          "values": [[5, 6, 7, 8, 9, 9], [5, 5, 6, 6, 7, 7],
                     [5, 5, 5, 6, 6, 6], [5, 6, 8, 9, 10, 10],
                     [5, 5, 6, 7, 8, 8], [5, 4, 4, 3, 3, 2],
                     [5, 7, 8, 10, 10, 10], [5, 5, 6, 6, 7, 7],
                     [5, 4, 3, 2, 1, 1]],
          "thresholds": [(0, "bad"), (4, "warn"), (7, "good")],
          "format": "{:.0f}/10", "row": 14}]},
        {"heading": "Key metrics", "kind": "figure", "weight": 0.6,
         "min_pages": 2, "height": {2: 150, 4: 185}, "widths": [1, 1],
         "charts": [
             {"type": "line", "title": "Weekly active customers",
              "subtitle": "%", "x": WEEKS, "zero": False,
              "format": "{:.0f}", "target": 48, "target_label": "KR",
              "series": [{"name": "WAC", "values": [41, 41, 42, 42, 43,
                                                    43, 44, 44, 45, 45,
                                                    45, None, None]}]},
             {"type": "line", "title": "Saved in Spaces", "subtitle":
              "€m", "x": WEEKS, "format": "{:.1f}", "target": 5,
              "target_label": "KR",
              "series": [{"name": "Saved", "color": 1, "area": True,
                          "values": [0, 0, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9,
                                     1.1, 1.4, 1.6, None, None]}]},
         ]},
        {"heading": "Learnings", "kind": "bullets", "weight": 0.7,
         "step": 0.2, "min_pages": 2, "items": [
             "**Speed sells itself.** Every 100 ms we took off the home "
             "screen added about 0.3 points of weekly active customers.",
             "**Savings need permission before code.** Spaces was ready "
             "in week 4; the savings product approval arrived in week 9.",
             "**Vendor contracts are on the critical path.** O3 KR3 "
             "never stood a chance once procurement started in week 2.",
         ]},
        {"heading": "Scores by squad", "kind": "figure", "weight": 0.9,
         "min_pages": 4, "height": 140, "widths": [3, 2], "charts": [
             {"type": "bars", "horizontal": True, "format": "{:.2f}",
              "title": "Average score", "target": 0.7,
              "target_label": "aim",
              "categories": ["Home", "Login", "Cards", "Spaces", "Bills",
                             "Chat"],
              "series": [{"name": "Score",
                          "values": [0.82, 0.75, 0.85, 0.7, 0.55, 0.1],
                          "colors": ["good", "good", "good", "good",
                                     "warn", "bad"]}]},
             {"type": "donut", "title": "Key results",
              "segments": [("On track", 5, "good"),
                           ("At risk", 3, "warn"),
                           ("Off track", 1, "bad")],
              "center": ("0.68", "average")},
         ]},
        {"heading": "Initiatives behind the key results", "kind": "table",
         "weight": 0.95, "step": 0.1, "min_pages": 4,
         "badges": {"Shipped": "good", "Building": "info",
                    "Blocked": "bad", "Discovery": "neutral"},
         "columns": [("Initiative", 3), ("Key result", 1.2),
                     ("Squad", 1), ("Status", 1.1, "center")],
         "rows": [
             ["Image caching and lazy loading on the home screen",
              "O1 KR1", "Home", "Shipped"],
             ["Biometric login v2 with fallback to PIN", "O1 KR2",
              "Login", "Shipped"],
             ["Push nudges for dormant customers", "O1 KR3", "Home",
              "Building"],
             ["Spaces beta with round-ups", "O2 KR1", "Spaces",
              "Shipped"],
             ["Interest on Spaces (needs approval)", "O2 KR3", "Spaces",
              "Blocked"],
             ["Two-tap card freeze", "O3 KR1", "Cards", "Shipped"],
             ["Card replacement tracking", "O3 KR2", "Cards",
              "Building"],
             ["Human chat vendor and integration", "O3 KR3", "Chat",
              "Blocked"],
             ["Bill calendar research", "Q4", "Bills", "Discovery"],
         ]},
        {"heading": "Rhythm", "kind": "figure", "weight": 1.1,
         "min_pages": 4, "charts": [{"type": "chevrons", "steps": [
             {"label": "Draft", "status": "done",
              "sub": "Squads propose OKRs in week −2"},
             {"label": "Align", "status": "done",
              "sub": "Tribe review, one hour, week −1"},
             {"label": "Check-in", "status": "now",
              "sub": "Confidence every second week"},
             {"label": "Score", "sub": "Week 13, honest and public"},
             {"label": "Learn", "sub": "Retro feeds the next draft"},
         ]}]},
        {"heading": "Draft for Q4", "kind": "table", "weight": 1.0,
         "step": 0.15, "min_pages": 4, "columns": [
             ("Objective", 2.2), ("Key result", 3.6), ("Baseline", 1,
                                                        "center")],
         "rows": [
             ["Make everyday banking effortless", "Weekly active "
              "customers 54 %", "45 %"],
             ["", "Login success rate 98.5 %", "97.2 %"],
             ["Help customers grow their money", "€8m saved in Spaces",
              "€1.6m"],
             ["", "Spaces opened by 15 % of customers", "1.3 %"],
             ["Be there when it matters", "Human chat for 25 % of "
              "customers, answered in 5 minutes", "0 %"],
             ["", "NPS +8 for customers who used help", "+21"],
         ]},
        {"heading": "Scoring", "kind": "text", "weight": 1.2, "step": 0.3,
         "min_pages": 4, "paragraphs": [
             "Key results are scored from 0 to 1 on how much of the "
             "change they asked for has happened. A score of 0.7 is a "
             "good quarter: if every key result scores 1, they were not "
             "ambitious enough.",
             "Confidence is asked every second week in the squad's "
             "check-in, from 1 (no chance) to 10 (done). A falling "
             "confidence is our earliest warning, and the reason O2 KR3 "
             "and O3 KR3 were escalated in week 7.",
         ]},
        {"heading": "Asks of leadership", "kind": "callout",
         "weight": 0.8, "tone": "warn", "min_pages": 2,
         "label": "Two asks:",
         "text": "sign the chat vendor contract this month, and give "
                 "product a seat at the savings product committee so "
                 "approvals start with the design, not after it."},
    ],
}
