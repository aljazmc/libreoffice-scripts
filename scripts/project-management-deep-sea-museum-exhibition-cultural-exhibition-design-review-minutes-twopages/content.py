"""Design Review Minutes of The Abyss: Life Below Light: the project and
everything the document could say. The typesetting keeps what fits into two
pages, the most important first."""

PROJECT = {
    "name": "The Abyss: Life Below Light",
    "code": "EX-27",
    "author": "Marta Kowalski, Exhibition Project Manager",
}

DOCUMENT = {
    "title": "Design Review Minutes",
    "subtitle": "Review 3 of the developed design · Thursday 10 September "
                "2026, 10:00 – 13:00, the board room",
    "meta": [("Exhibition", "EX-27"), ("Review", "3 · developed design"),
             ("Chair", "Marta Kowalski"), ("Attendees", "11"),
             ("Outcome", "Approved, 6 changes")],
    "sections": [
        {"heading": "Decisions", "kind": "table", "weight": 0.1,
         "step": 0.1, "badges": {"Approved": "good", "Changed": "warn",
                                 "Deferred": "neutral",
                                 "Rejected": "bad"},
         "columns": [("No.", 0.5), ("Decision", 4.2),
                     ("Outcome", 1.1, "center")],
         "rows": [
             ["D1", "The developed design is approved, with the changes "
              "below", "Approved"],
             ["D2", "Gallery III light level drops from 80 to 50 lux; "
              "specimen cases get their own lighting", "Changed"],
             ["D3", "The pressure press moves from gallery V to the "
              "end of gallery IV, nearer the seating", "Changed"],
             ["D4", "Panel text limited to 80 words; the extra goes to "
              "the audio guide", "Approved"],
             ["D5", "A second exit from gallery III for visitors who "
              "find the dark too much", "Changed"],
             ["D6", "Projection floor in gallery II: deferred until the "
              "cost is known", "Deferred"],
             ["D7", "Smell of the sea in gallery I", "Rejected"],
         ]},
        {"heading": "Actions", "kind": "table", "weight": 0.2, "step": 0.1,
         "badges": {"Open": "warn", "Done": "good"},
         "columns": [("No.", 0.5), ("Action", 3.6), ("Owner", 1.3),
                     ("Due", 0.9), ("Status", 0.9, "center")],
         "rows": [
             ["A1", "Revise the gallery III lighting plan at 50 lux",
              "Studio Fathom", "24 Sep", "Open"],
             ["A2", "Check the floor loading for the press in gallery IV",
              "Engineer", "1 Oct", "Open"],
             ["A3", "Price the projection floor, three options",
              "Media", "1 Oct", "Open"],
             ["A4", "Draw the second exit with fire safety",
              "Studio Fathom", "24 Sep", "Open"],
             ["A5", "Cut panel texts to 80 words", "Curators", "15 Oct",
              "Open"],
             ["A6", "Send the developed design to the lenders",
              "Registrar", "14 Sep", "Done"],
         ]},
        {"heading": "Comments by gallery", "kind": "figure",
         "weight": 0.3, "height": {1: 135, 2: 150, 4: 160},
         "widths": [3, 2], "charts": [
             {"type": "bars", "stacked": True, "title": "Comments raised",
              "categories": ["I", "II", "III", "IV", "V", "VI"],
              "series": [{"name": "Resolved in the room", "color": 2,
                          "values": [4, 6, 9, 5, 3, 4]},
                         {"name": "Action", "color": 0,
                          "values": [0, 1, 3, 2, 1, 0]},
                         {"name": "Deferred", "color": 4,
                          "values": [1, 1, 0, 0, 0, 1]}]},
             {"type": "donut", "title": "By topic",
              "segments": [("Access", 11), ("Conservation", 9),
                           ("Story and text", 8), ("Cost", 6),
                           ("Safety", 7)],
              "center": ("41", "comments")},
         ]},
        {"heading": "Discussion", "kind": "entries", "weight": 0.4,
         "step": 0.2, "inner": 0.1, "min_pages": 2, "entries": [
             {"title": "Gallery III, the dark", "text": [
                 "The conservator asked for 50 lux on the fluid "
                 "specimens; the designers worried the room would feel "
                 "dead. Agreed: the room stays dark, the cases glow, and "
                 "the bioluminescence film plays on the ceiling."]},
             {"title": "Access", "text": [
                 "The access panel walked the model with a wheelchair "
                 "user and a visually impaired visitor. Main points: the "
                 "ramp in gallery IV is too steep at 1:12 (changed to "
                 "1:15), and every case needs a tactile object nearby."]},
             {"title": "The pressure press", "text": [
                 "Everyone loves it. It is loud, so it moves next to the "
                 "seating at the end of gallery IV, where a crowd can "
                 "gather without blocking the route."]},
         ]},
        {"heading": "Budget check", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": 165, "charts": [{"type": "waterfall",
          "format": "€{:,.0f}k", "axis_format": "{:,.0f}", "invert": True,
          "steps": [("Budget for build and media", 1400),
                    ("Lighting changes", 35), ("Second exit", 22),
                    ("Ramp", 8), ("Cases: own lighting", 41),
                    ("Savings: fewer screens", -60),
                    ("Savings: reused plinths", -28),
                    ("After review 3", None)]}]},
        {"heading": "Attendees", "kind": "tags", "weight": 0.6,
         "step": 0.1, "min_pages": 2, "items": [
             ("Museum", "Marta Kowalski (chair), Dr Helena Varga, "
                        "Pieter Jansen, Anouk de Wit, Ilse Brouwer "
                        "(conservation)"),
             ("Studio Fathom", "Jonas Lind, Amara Osei"),
             ("Media", "Kasper Holm"),
             ("Access panel", "Ruth Peeters, Daan Smit"),
             ("Fire safety", "Bas Visser"),
         ]},
        {"heading": "Route through the galleries", "kind": "figure",
         "weight": 0.8, "min_pages": 4, "charts": [{"type": "chevrons",
          "steps": [
              {"label": "I. Sunlight", "status": "done",
               "sub": "Approved as drawn"},
              {"label": "II. Twilight", "status": "now",
               "sub": "Projection floor deferred"},
              {"label": "III. Midnight", "status": "now",
               "sub": "Lighting to 50 lux; second exit"},
              {"label": "IV. Abyss", "status": "now",
               "sub": "Press moves here; ramp 1:15"},
              {"label": "V. Trenches", "status": "done",
               "sub": "Approved"},
              {"label": "VI. Surface", "status": "done",
               "sub": "Approved"},
          ]}]},
        {"heading": "Design programme", "kind": "figure", "weight": 0.9,
         "min_pages": 4, "height": 150, "charts": [{"type": "gantt",
          "columns": ["Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar",
                      "Apr", "May"],
          "groups": ["Design", "Make", "Install"], "today": 0.33,
          "tasks": [
              {"label": "Changes from review 3", "start": 0.3, "end": 1.2},
              {"label": "Technical design", "start": 1, "end": 3},
              {"label": "Review 4 (technical)", "start": 3,
               "milestone": True, "text": "3 Dec"},
              {"label": "Tender and contract", "start": 3, "end": 4.5,
               "group": 1},
              {"label": "Build in the workshop", "start": 4.5, "end": 7,
               "group": 1},
              {"label": "Install on site", "start": 6.5, "end": 8.4,
               "group": 2, "critical": True},
              {"label": "Opening", "start": 8.45, "milestone": True},
          ]}]},
        {"heading": "Open questions", "kind": "bullets", "weight": 1.0,
         "step": 0.2, "min_pages": 4, "items": [
             "Can the giant squid case hold 15 °C? (Registrar, after "
             "the lender's committee in November.)",
             "Do we need a quiet room near gallery III for visitors with "
             "sensory needs? (Learning team to propose.)",
             "Should the pledge wall in gallery VI be digital or "
             "handwritten? (Curators to test with visitors.)",
         ]},
        {"heading": "Next review", "kind": "callout", "weight": 1.1,
         "tone": "info", "min_pages": 4, "label": "Review 4,",
         "text": "the technical design, on Thursday 3 December, 10:00, "
                 "with the build contractors invited for the second "
                 "half."},
        {"heading": "Previous actions", "kind": "table", "weight": 1.2,
         "step": 0.1, "min_pages": 4, "badges": {"Done": "good",
                                                "Open": "warn"},
         "columns": [("From review 2", 4), ("Status", 1, "center")],
         "rows": [
             ["Add seating every 30 m along the route", "Done"],
             ["Check the floor for the chimney fragment", "Open"],
             ["Write the family trail", "Done"],
             ["Test the bioluminescence film at full size", "Done"],
         ]},
        {"heading": "Changes since review 2", "kind": "figure",
         "weight": 1.25, "min_pages": 4, "height": 150, "widths": [3, 2],
         "charts": [
             {"type": "bars", "title": "Drawings issued",
              "subtitle": "by discipline", "stacked": True,
              "categories": ["Layout", "Joinery", "Cases", "Lighting",
                             "Graphics", "AV"],
              "series": [{"name": "Review 2", "color": 4,
                          "values": [8, 14, 6, 4, 10, 3]},
                         {"name": "Review 3", "color": 0,
                          "values": [10, 22, 12, 9, 18, 7]}]},
             {"type": "progress", "title": "Design complete",
              "format": "{:.0f} %", "items": [
                  {"label": "Layout", "value": 95, "status": "good"},
                  {"label": "Cases", "value": 80, "status": "good"},
                  {"label": "Lighting", "value": 60, "status": "warn"},
                  {"label": "Graphics", "value": 55, "status": "warn"},
                  {"label": "AV", "value": 45, "status": "bad"},
              ]},
         ]},
        {"heading": "Risks raised", "kind": "table", "weight": 1.3,
         "step": 0.1, "min_pages": 4, "badges": {"High": "bad",
                                                "Medium": "warn",
                                                "Low": "good"},
         "columns": [("Risk", 3.6), ("Level", 0.9, "center"),
                     ("Owner", 1.4)],
         "rows": [
             ["Giant squid loan declined", "High", "Registrar"],
             ["Projection floor cost over €80k", "Medium", "Media"],
             ["Gallery III too dark for some visitors", "Medium",
              "Learning"],
             ["Press noise disturbs gallery V", "Low", "Studio Fathom"],
         ]},
    ],
}
