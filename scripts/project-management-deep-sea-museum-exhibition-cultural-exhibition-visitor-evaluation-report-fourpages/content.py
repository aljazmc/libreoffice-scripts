"""Visitor Evaluation Report of The Abyss: Life Below Light: the project and
everything the document could say. The typesetting keeps what fits into four
pages, the most important first."""

PROJECT = {
    "name": "The Abyss: Life Below Light",
    "code": "EX-27",
    "author": "Pieter Jansen, Head of Learning and Evaluation",
}

MONTHS = ["May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan"]

DOCUMENT = {
    "title": "Visitor Evaluation Report",
    "subtitle": "What 196,400 visitors did, felt and remembered · "
                "summative evaluation, May 2027 to January 2028",
    "meta": [("Exhibition", "EX-27"), ("Visitors", "196,400"),
             ("Surveys", "3,812"), ("Observations", "640"),
             ("Author", "Pieter Jansen")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "charts": [{"type": "kpis",
         "tiles": [
             {"label": "Visitors", "value": "196,400", "status": 0,
              "note": "target 180,000", "delta": "+9 %"},
             {"label": "Rated 4 or 5", "value": "91 %", "status": 1,
              "note": "target 85 %"},
             {"label": "Time in galleries", "value": "54 min",
              "status": 2, "note": "target 50"},
             {"label": "Remembered a threat", "value": "57 %",
              "status": 3, "note": "target 60 %"},
         ]}]},
        {"heading": "Visits by month", "kind": "figure", "weight": 0.2,
         "height": {1: 155, 2: 165, 4: 175}, "widths": [3, 2],
         "charts": [
             {"type": "bars", "title": "Visitors", "subtitle":
              "thousands", "format": "{:.1f}", "categories": MONTHS,
              "series": [{"name": "Actual", "values": [24.1, 21.6, 29.8,
                                                       31.2, 18.4, 22.0,
                                                       14.6, 19.3,
                                                       15.4]},
                         {"name": "Forecast", "color": 4,
                          "values": [22, 19, 26, 28, 17, 20, 14, 18,
                                     16]}]},
             {"type": "donut", "title": "Who came",
              "segments": [("Families", 46), ("Adults", 24),
                           ("Schools", 16), ("Tourists", 14)],
              "format": "{:.0f}%", "center": ("196k", "visitors")},
         ]},
        {"heading": "Dwell time by gallery", "kind": "figure",
         "weight": 0.3, "height": {1: 145, 2: 160}, "charts": [{
             "type": "bars", "horizontal": True, "format": "{:.1f} min",
             "title": "Average minutes", "subtitle": "observed, 640 "
             "visitors tracked",
             "categories": ["I. Sunlight", "II. Twilight",
                            "III. Midnight", "IV. Abyss", "V. Trenches",
                            "VI. Surface"],
             "series": [{"name": "Planned", "color": 4,
                         "values": [6, 10, 12, 9, 7, 6]},
                        {"name": "Observed", "values": [5.1, 9.4, 15.8,
                                                        10.6, 8.2,
                                                        4.9]}]}]},
        {"heading": "Key findings", "kind": "bullets", "weight": 0.4,
         "step": 0.15, "items": [
             "**Gallery III is the heart of the exhibition.** Visitors "
             "stayed four minutes longer than planned and named it as "
             "their favourite moment twice as often as any other.",
             "**The pressure press is the most photographed object** in "
             "the museum's history: 41,000 posts with its hashtag.",
             "**Gallery VI is rushed.** Visitors arrive tired, and the "
             "message about threats lands less well than planned.",
         ]},
        {"heading": "Ratings", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": 155, "charts": [{"type": "heatmap",
          "rows": ["Overall", "Objects", "Lighting and mood",
                   "Text and labels", "Interactives", "Accessibility",
                   "Value for money"],
          "cols": ["Families", "Adults", "Schools", "Tourists"],
          "values": [[4.6, 4.5, 4.4, 4.7], [4.5, 4.7, 4.3, 4.6],
                     [4.7, 4.6, 4.5, 4.8], [4.0, 4.3, 3.9, 4.1],
                     [4.4, 3.9, 4.6, 4.0], [4.2, 4.3, 4.1, 4.2],
                     [4.1, 3.8, 4.5, 3.9]],
          "thresholds": [(0, "bad"), (4.0, "warn"), (4.3, "good")],
          "format": "{:.1f}", "labels": 0.24}]},
        {"heading": "What visitors said", "kind": "figure", "weight": 0.6,
         "min_pages": 2, "charts": [{"type": "board", "size": 7.2,
          "columns": [
              {"title": "Loved", "tone": "good", "cards": [
                  ("“My son wouldn't leave the glowing room.”",
                   "parent, 38"),
                  ("“I didn't know there was this much life down "
                   "there.”", "adult, 62"),
              ]},
              {"title": "Missed", "tone": "warn", "cards": [
                  ("“More places to sit, please.”", "adult, 71"),
                  ("“The last room felt like homework.”", "teenager, "
                                                          "15"),
              ]},
              {"title": "Will do", "tone": "info", "cards": [
                  ("“I'll check where my fish comes from.”",
                   "adult, 29"),
                  ("“I want to be a submarine pilot.”", "child, 9"),
              ]},
          ]}]},
        {"heading": "Learning", "kind": "figure", "weight": 0.7,
         "min_pages": 2, "height": 140, "widths": [1, 1], "charts": [
             {"type": "progress", "title": "A week later, visitors "
              "could", "format": "{:.0f} %", "items": [
                  {"label": "Name a deep-sea animal", "value": 88,
                   "status": "good"},
                  {"label": "Explain bioluminescence", "value": 64,
                   "status": "good"},
                  {"label": "Name a threat to the deep", "value": 57,
                   "target": 60, "status": "warn"},
                  {"label": "Say what they can do", "value": 34,
                   "target": 40, "status": "warn"},
              ]},
             {"type": "funnel", "title": "School visits",
              "stages": [("Groups booked", 1240),
                         ("Used the trail", 1010),
                         ("Did the classroom activity", 610)]},
         ]},
        {"heading": "Accessibility", "kind": "text", "weight": 0.9,
         "step": 0.3, "min_pages": 4, "paragraphs": [
             "The second exit from gallery III was used by about one "
             "visitor in forty, most of them with small children. Wheel"
             "chair users rated the route 4.4 of 5; their main request "
             "was lower cases in gallery II.",
             "The quiet sessions on the first Sunday of each month, with "
             "the sound off and the lights up, sold out every time and "
             "will become part of every exhibition.",
         ]},
        {"heading": "Where visitors slowed", "kind": "figure",
         "weight": 1.0, "min_pages": 4, "height": 140, "charts": [{
             "type": "line", "title": "Visitors stopping, by point on "
             "the route", "subtitle": "% of tracked visitors",
             "x": ["Entry", "Plankton", "Migration", "Glow cases",
                   "Film", "Whale fall", "Press", "Hull", "Pledges",
                   "Exit"],
             "format": "{:.0f}",
             "series": [{"name": "Stopped", "area": True,
                         "values": [62, 71, 66, 94, 78, 74, 91, 69, 38,
                                    20]}]}]},
        {"heading": "Recommendations", "kind": "entries", "weight": 1.1,
         "step": 0.2, "inner": 0.1, "min_pages": 4, "entries": [
             {"title": "Give the ending room", "text": [
                 "Put seating and the threats film before the last "
                 "gallery, not in it, so visitors meet it rested."]},
             {"title": "Make the action concrete", "text": [
                 "Replace the pledge wall with three specific things "
                 "visitors can do, each with a card to take home."]},
             {"title": "Tour the dark room", "text": [
                 "Gallery III could travel as a smaller exhibition; two "
                 "museums have asked."]},
         ]},
        {"heading": "Method", "kind": "tags", "weight": 1.2, "step": 0.1,
         "min_pages": 4, "items": [
             ("Exit survey", "3,812 visitors, on tablets, every day"),
             ("Tracking", "640 visitors observed from entry to exit"),
             ("Follow-up", "412 visitors, by email, a week later"),
             ("Schools", "38 teachers interviewed"),
             ("Social", "hashtag and reviews analysed monthly"),
         ]},
        {"heading": "Money", "kind": "figure", "weight": 1.25,
         "min_pages": 4, "height": 150, "widths": [1, 1], "charts": [
             {"type": "bars", "title": "Income", "subtitle": "€k",
              "format": "{:,.0f}", "categories": ["Tickets", "Shop",
                                                   "Café", "Events"],
              "series": [{"name": "Target", "color": 4,
                          "values": [1620, 310, 240, 90]},
                         {"name": "Actual", "values": [1790, 402, 268,
                                                       135]}]},
             {"type": "donut", "title": "Shop best-sellers",
              "segments": [("Glow-in-the-dark squid", 38),
                           ("Exhibition book", 22), ("Posters", 18),
                           ("Anglerfish plush", 14), ("Other", 8)],
              "format": "{:.0f}%", "center": ("€402k", "shop")},
         ]},
        {"heading": "Press and online", "kind": "figure", "weight": 1.3,
         "min_pages": 4, "charts": [{"type": "kpis", "tiles": [
             {"label": "Reviews", "value": "31", "status": 0,
              "note": "average 4.4 stars"},
             {"label": "Hashtag posts", "value": "41k", "status": 1,
              "note": "#theabyss"},
             {"label": "Website visits", "value": "612k", "status": 2,
              "note": "exhibition pages"},
             {"label": "Travelling offers", "value": "2", "status": 3,
              "note": "Oslo, Lyon"},
         ]}]},
    ],
}
