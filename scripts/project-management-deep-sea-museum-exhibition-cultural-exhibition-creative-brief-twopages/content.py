"""Creative Brief of The Abyss: Life Below Light: the project and everything
the document could say. The typesetting keeps what fits into two pages, the
most important first."""

PROJECT = {
    "name": "The Abyss: Life Below Light",
    "code": "EX-27",
    "author": "Dr Helena Varga, Lead Curator",
}

DOCUMENT = {
    "title": "Creative Brief",
    "subtitle": "A temporary exhibition about the deep sea, the largest "
                "and least known place where things live",
    "meta": [("Exhibition", "EX-27"), ("Opens", "14 May 2027"),
             ("Space", "1,100 m², 6 galleries"),
             ("Curator", "Dr Helena Varga")],
    "sections": [
        {"kind": "motto", "weight": 0.1,
         "text": "Below 200 metres the light runs out. Below 1,000 metres "
                 "it is dark forever. Most of the life on Earth lives "
                 "there, and almost nobody has seen it."},
        {"heading": "The idea", "kind": "text", "weight": 0.2, "step": 0.5,
         "paragraphs": [
             "Visitors descend, gallery by gallery, from the sunlit "
             "surface to the deepest trench, 11 kilometres down. Light, "
             "sound and temperature change as they go. At each depth they "
             "meet the animals that live there and the people who study "
             "them, and leave knowing that the deep sea is not empty "
             "and not far away: it is under threat now.",
         ]},
        {"heading": "The descent", "kind": "figure", "weight": 0.3,
         "height": {1: 150, 2: 160, 4: 170}, "charts": [{"type": "bars",
          "horizontal": True, "stacked": True, "values": False,
          "title": "Six galleries, six depths", "subtitle": "planned "
          "visitor minutes and floor area",
          "categories": ["I. Sunlight · 0 – 200 m",
                         "II. Twilight · 200 – 1,000 m",
                         "III. Midnight · 1,000 – 4,000 m",
                         "IV. The abyss · 4,000 – 6,000 m",
                         "V. The trenches · 6,000 – 11,000 m",
                         "VI. The surface again · us"],
          "series": [{"name": "Minutes", "values": [6, 10, 12, 9, 7, 6],
                      "labels": ["6 min", "10 min", "12 min", "9 min",
                                 "7 min", "6 min"]},
                     {"name": "Area ×10 m²", "color": 4,
                      "values": [14, 20, 26, 22, 14, 14]}],
          "inside": True}]},
        {"heading": "Audiences", "kind": "figure", "weight": 0.4,
         "height": {1: 125, 2: 135}, "widths": [2, 3], "charts": [
             {"type": "donut", "title": "Expected visitors",
              "segments": [("Families", 42), ("Adults", 27),
                           ("Schools", 18), ("Tourists", 13)],
              "format": "{:.0f}%", "center": ("180k", "in 9 months")},
             {"type": "progress", "title": "What each should take away",
              "format": "{:.0f}", "max": 5, "items": [
                  {"label": "Families: wonder", "value": 5,
                   "display": "5 / 5", "status": 0},
                  {"label": "Adults: understanding", "value": 4,
                   "display": "4 / 5", "status": 1},
                  {"label": "Schools: curriculum links", "value": 4,
                   "display": "4 / 5", "status": 2},
                  {"label": "Tourists: a reason to come", "value": 3,
                   "display": "3 / 5", "status": 3},
              ]},
         ]},
        {"heading": "Tone", "kind": "bullets", "weight": 0.5,
         "step": 0.15, "items": [
             "**Wonder before facts.** Every gallery opens with something "
             "to look at, not something to read.",
             "**Dark, but never frightening.** The anglerfish is "
             "fascinating, not a monster.",
             "**Real objects first.** Specimens, instruments and a "
             "piece of the submersible hull, not only screens.",
             "**Honest about harm.** Deep-sea mining, trawling and "
             "plastic, shown with evidence, not slogans.",
         ]},
        {"heading": "Galleries", "kind": "entries", "weight": 0.6,
         "step": 0.2, "inner": 0.1, "min_pages": 2, "entries": [
             {"title": "I. Sunlight", "dates": "0 – 200 m", "text": [
                 "Bright and loud with the sound of waves. The plankton "
                 "that makes half of the oxygen we breathe, under "
                 "microscopes visitors can drive."]},
             {"title": "II. Twilight", "dates": "200 – 1,000 m", "text": [
                 "The light fades to blue. The daily migration of "
                 "billions of animals to the surface and back, the "
                 "largest on Earth, shown on a 12 m wall."]},
             {"title": "III. Midnight", "dates": "1,000 – 4,000 m",
              "text": [
                  "Total darkness, except for the animals that make "
                  "their own light. The centrepiece: forty specimens in "
                  "ultraviolet-lit cases."]},
             {"title": "IV. The abyss", "dates": "4,000 – 6,000 m",
              "text": [
                  "The cold plain covered in snow made of dead plankton, "
                  "and a whale fall that feeds a community for fifty "
                  "years."]},
             {"title": "V. The trenches", "dates": "6,000 – 11,000 m",
              "text": [
                  "Pressure you can feel: a hydraulic press crushes a "
                  "polystyrene cup every ten minutes. The submersible "
                  "hull and the pilots who went down."]},
             {"title": "VI. The surface again", "dates": "us", "text": [
                 "What we take from the deep and what we put into it. "
                 "Visitors leave a pledge on a wall of light."]},
         ]},
        {"heading": "Measures of success", "kind": "table", "weight": 0.7,
         "step": 0.1, "min_pages": 2, "columns": [
             ("Measure", 3), ("Target", 1.2, "center"),
             ("How we know", 2.4)],
         "rows": [
             ["Visitors in nine months", "180,000", "Ticketing"],
             ["Visitors who rate it 4 or 5 of 5", "85 %",
              "Exit survey"],
             ["Can name one deep-sea threat a week later", "60 %",
              "Follow-up survey"],
             ["School groups", "1,100", "Learning bookings"],
             ["Average time in the galleries", "50 min",
              "Sensor counts"],
         ]},
        {"heading": "Constraints", "kind": "tags", "weight": 0.9,
         "step": 0.1, "min_pages": 4, "items": [
             ("Budget", "€2.4m including design, build, loans and "
                        "marketing"),
             ("Space", "the east wing, 1,100 m², ceilings of 4.2 m"),
             ("Conservation", "fluid-preserved specimens at 18 °C, "
                              "light under 50 lux"),
             ("Access", "every gallery step-free, with seating every "
                        "30 m"),
             ("Languages", "English and Dutch; audio guide in six "
                           "languages"),
         ]},
        {"heading": "Budget", "kind": "figure", "weight": 1.0,
         "min_pages": 4, "height": 140, "charts": [{"type": "donut",
          "format": "€{:,.0f}k", "center": ("€2.4m", "total"),
          "segments": [("Build and fit-out", 980), ("Design", 310),
                       ("Media and interactives", 420),
                       ("Loans, couriers, insurance", 260),
                       ("Marketing", 240), ("Contingency", 190)]}]},
        {"heading": "Team", "kind": "figure", "weight": 1.1,
         "min_pages": 4, "charts": [{"type": "tree", "root": {
             "label": "Exhibition board", "note": "director chairs",
             "children": [
                 {"label": "Curatorial", "note": "Dr Helena Varga",
                  "children": [{"label": "Two curators"},
                               {"label": "Science advisers × 4"}]},
                 {"label": "Design", "note": "Studio Fathom",
                  "children": [{"label": "3D and lighting"},
                               {"label": "Graphics"}]},
                 {"label": "Learning", "note": "Pieter Jansen",
                  "children": [{"label": "Schools programme"},
                               {"label": "Family trails"}]},
                 {"label": "Project", "note": "Marta Kowalski",
                  "children": [{"label": "Registrar"},
                               {"label": "Build contractor"}]},
             ]}}]},
        {"heading": "Timeline", "kind": "figure", "weight": 1.2,
         "min_pages": 4, "height": 120, "charts": [{"type": "timeline",
          "start": 0, "end": 18, "label_width": 95,
          "ticks": [(0, "Dec 25"), (6, "Jun 26"), (12, "Dec 26"),
                    (17.5, "May 27")],
          "events": [
              {"at": 0, "label": "Brief approved", "status": "now"},
              {"at": 3, "label": "Concept design"},
              {"at": 7, "label": "Developed design"},
              {"at": 10, "label": "Loans confirmed"},
              {"at": 14, "label": "Build starts"},
              {"at": 17.5, "label": "Opening night", "sub": "14 May"},
          ]}]},
        {"heading": "What it is not", "kind": "bullets", "weight": 1.3,
         "step": 0.2, "min_pages": 4, "items": [
             "Not an aquarium: there are no live animals.",
             "Not a horror show: no jump scares, no monster music.",
             "Not a lecture: no panel longer than 80 words.",
         ]},
        {"heading": "References", "kind": "text", "weight": 1.4,
         "step": 0.3, "min_pages": 4, "paragraphs": [
             "The galleries draw on the expeditions of the research "
             "vessel *Pelagia*, on footage lent by three oceanographic "
             "institutes and on the national collection of fluid-"
             "preserved deep-sea fishes, most of which has never been on "
             "display.",
         ]},
        {"heading": "Visitor journey", "kind": "figure", "weight": 1.45,
         "min_pages": 4, "height": 150, "charts": [{"type": "line",
          "title": "Light, sound and temperature on the way down",
          "subtitle": "relative, gallery by gallery",
          "x": ["I", "II", "III", "IV", "V", "VI"], "format": "{:.0f}",
          "series": [{"name": "Light", "color": 1,
                      "values": [100, 45, 8, 4, 6, 80]},
                     {"name": "Sound", "color": 2,
                      "values": [80, 50, 25, 15, 60, 70]},
                     {"name": "Temperature", "color": 0, "dash": True,
                      "values": [70, 60, 45, 40, 40, 70]}]}]},
        {"heading": "Key objects", "kind": "table", "weight": 1.5,
         "step": 0.05, "min_pages": 4,
         "columns": [("Object", 2.6), ("Gallery", 0.9, "center"),
                     ("Why it matters", 3.2)],
         "rows": [
             ["Giant squid, 7.2 m", "III", "The animal everyone has "
              "heard of and nobody has seen"],
             ["Anglerfish, female with attached male", "III",
              "The strangest love story on Earth"],
             ["Whale vertebra with bone-eating worms", "IV",
              "A whale fall feeds a community for decades"],
             ["Submersible hull section", "V", "What it takes to go "
              "down eleven kilometres"],
             ["Manganese nodules", "VI", "What deep-sea miners want, "
              "and what it took millions of years to grow"],
         ]},
    ],
}
