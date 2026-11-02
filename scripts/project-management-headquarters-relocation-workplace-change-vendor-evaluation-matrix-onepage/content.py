"""Vendor Evaluation Matrix of Wharf Street HQ Move: the project and everything
the document could say. The typesetting keeps what fits into one page, the
most important first."""

PROJECT = {
    "name": "Wharf Street HQ Move",
    "code": "WS-HQ",
    "author": "Grant Holloway, Procurement Lead",
}

DOCUMENT = {
    "title": "Vendor Evaluation Matrix",
    "subtitle": "Fit-out contractor for floors 1 to 9 · four bidders, "
                "scored by a panel of five",
    "meta": [("Project", "WS-HQ"), ("Contract", "Fit-out, design and "
                                                 "build"),
             ("Budget", "£9.8m"), ("Bidders", "4"),
             ("Recommended", "Northlight Interiors")],
    "sections": [
        {"heading": "Ranking", "kind": "figure", "weight": 0.1,
         "height": {1: 145, 2: 150, 4: 160}, "widths": [3, 2],
         "charts": [
             {"type": "bars", "horizontal": True, "stacked": True,
              "title": "Weighted score", "subtitle": "out of 100",
              "categories": ["Northlight Interiors", "Cobalt Build",
                             "Meridian Fit-Out", "Ashford & Lane"],
              "series": [{"name": "Quality (60)", "color": 0,
                          "values": [49.2, 51.0, 43.8, 39.0]},
                         {"name": "Price (30)", "color": 1,
                          "values": [27.6, 22.8, 30.0, 25.2]},
                         {"name": "Social value (10)", "color": 3,
                          "values": [8.5, 6.0, 5.5, 7.0]}],
              "inside": True},
             {"type": "quadrant", "title": "Price against quality",
              "x": "price score", "y": "quality score",
              "quadrants": ["Dear, good", "Best value", "Poor value",
                            "Cheap"],
              "points": [("Northlight", 9.2, 8.2, "good", 5),
                         ("Cobalt", 7.6, 8.5, 0),
                         ("Meridian", 10, 7.3, 0),
                         ("Ashford", 8.4, 6.5, 0)]},
         ]},
        {"heading": "Recommendation", "kind": "callout", "weight": 0.15,
         "tone": "good", "label": "Award to Northlight Interiors",
         "text": "at £9.41m: the highest overall score, the strongest "
                 "plan for working floor by floor around the move waves, "
                 "and the best social value offer."},
        {"heading": "Scores by criterion", "kind": "table",
         "weight": 0.2, "step": 0.05, "columns": [
             ("Criterion", 2.4), ("Weight", 0.8, "center"),
             ("Northlight", 1, "center"), ("Cobalt", 1, "center"),
             ("Meridian", 1, "center"), ("Ashford", 1, "center")],
         "badges": {"5": "good", "4": "good", "3": "warn", "2": "bad",
                    "1": "bad"},
         "rows": [
             ["Programme and phasing", "15 %", "5", "4", "3", "3"],
             ["Design quality", "10 %", "4", "5", "4", "3"],
             ["Team and experience", "10 %", "4", "5", "4", "3"],
             ["Health and safety", "10 %", "4", "4", "4", "4"],
             ["Sustainability and materials", "10 %", "4", "4", "3",
              "3"],
             ["Managing risk", "5 %", "4", "4", "3", "3"],
             ["Price", "30 %", "4.6", "3.8", "5", "4.2"],
             ["Social value", "10 %", "4.3", "3", "2.8", "3.5"],
         ]},
        {"heading": "Prices", "kind": "figure", "weight": 0.3,
         "min_pages": 2, "height": 160, "charts": [{"type": "bars",
          "stacked": True, "title": "Tender price", "subtitle": "£m",
          "format": "{:.2f}",
          "categories": ["Northlight", "Cobalt", "Meridian", "Ashford"],
          "target": 9.8, "target_label": "budget",
          "series": [{"name": "Construction", "values": [6.31, 7.02,
                                                         5.98, 6.62]},
                     {"name": "Furniture", "values": [1.84, 2.05, 1.71,
                                                      1.92]},
                     {"name": "Design and fees", "values": [0.74, 0.88,
                                                            0.62,
                                                            0.71]},
                     {"name": "Risk allowance", "color": 4,
                      "values": [0.52, 0.56, 0.75, 0.48]}]}]},
        {"heading": "Strengths and concerns", "kind": "entries",
         "weight": 0.4, "step": 0.2, "inner": 0.1, "min_pages": 2,
         "entries": [
             {"title": "Northlight Interiors", "dates": "82.3",
              "fields": [
                  ("Strengths", "phasing plan built around our four "
                                "waves; 40 apprentices; reused "
                                "furniture"),
                  ("Concerns", "smaller design team; key designer "
                               "named for two other projects")]},
             {"title": "Cobalt Build", "dates": "79.8", "fields": [
                 ("Strengths", "the best design; strong references"),
                 ("Concerns", "£0.93m dearer; phasing assumes empty "
                              "floors")]},
             {"title": "Meridian Fit-Out", "dates": "79.3", "fields": [
                 ("Strengths", "lowest price"),
                 ("Concerns", "risk allowance hides exclusions worth "
                              "about £0.6m; weak on sustainability")]},
             {"title": "Ashford & Lane", "dates": "71.2", "fields": [
                 ("Strengths", "local, good social value"),
                 ("Concerns", "largest job so far is a third of this")]},
         ]},
        {"heading": "References", "kind": "figure", "weight": 0.6,
         "min_pages": 4, "height": 140, "charts": [{"type": "heatmap",
          "title": "Reference checks", "subtitle": "three clients each",
          "rows": ["Northlight", "Cobalt", "Meridian", "Ashford"],
          "cols": ["On time", "On budget", "Quality", "Would hire "
                   "again"],
          "values": [["Yes", "Yes", "Yes", "Yes"],
                     ["Yes", "Partly", "Yes", "Yes"],
                     ["Partly", "No", "Partly", "Partly"],
                     ["Yes", "Yes", "Partly", "Yes"]],
          "badges": {"Yes": "good", "Partly": "warn", "No": "bad"},
          "labels": 0.2}]},
        {"heading": "Risks", "kind": "table", "weight": 0.7, "step": 0.1,
         "min_pages": 4, "badges": {"High": "bad", "Medium": "warn",
                                    "Low": "good"},
         "columns": [("Risk with Northlight", 3.4),
                     ("Level", 0.9, "center"), ("Mitigation", 3)],
         "rows": [
             ["Design team stretched", "Medium", "Named designer "
              "contracted for 3 days a week minimum"],
             ["Furniture lead times", "Medium", "Order in week 2 of the "
              "contract"],
             ["Financial standing", "Low", "Parent company guarantee "
              "and 10 % bond"],
         ]},
        {"heading": "Panel", "kind": "tags", "weight": 0.8, "step": 0.1,
         "min_pages": 4, "items": [
             ("Procurement", "Grant Holloway (chair, no vote)"),
             ("Workplace", "Tomás Reyes"),
             ("Facilities", "Mary Okafor"),
             ("Finance", "Ian Price"),
             ("Employee rep", "Lucy Chen"),
             ("Adviser", "Studio Arc, cost consultant"),
         ]},
        {"heading": "Process", "kind": "figure", "weight": 0.9,
         "min_pages": 4, "charts": [{"type": "chevrons", "steps": [
             {"label": "Selection", "status": "done",
              "sub": "11 applied; 4 shortlisted"},
             {"label": "Tender", "status": "done",
              "sub": "6 weeks, two site visits"},
             {"label": "Evaluation", "status": "done",
              "sub": "Individual scores, then moderation"},
             {"label": "Interviews", "status": "done",
              "sub": "Two hours each"},
             {"label": "Award", "status": "now",
              "sub": "Steering group, 14 Apr"},
         ]}]},
        {"heading": "Scoring rules", "kind": "text", "weight": 1.0,
         "step": 0.3, "min_pages": 4, "paragraphs": [
             "Quality questions are scored 0 to 5 by each panel member "
             "on their own, then moderated together; the moderated "
             "score counts. Price scores give 5 to the lowest price and "
             "less to the others in proportion. A bidder scoring 2 or "
             "less on health and safety is excluded, whatever its total.",
         ]},
        {"heading": "Price per square metre", "kind": "figure",
         "weight": 1.1, "min_pages": 4, "height": 130, "charts": [{
             "type": "bars", "horizontal": True, "format": "£{:.0f}",
             "title": "Fit-out cost", "subtitle": "£ per m² net",
             "categories": ["Northlight", "Cobalt", "Meridian",
                            "Ashford", "Benchmark"],
             "series": [{"name": "£/m²", "values": [663, 728, 638, 690,
                                                    700],
                         "colors": ["good", 0, 0, 0, 4]}]}]},
        {"heading": "Programme offered", "kind": "figure", "weight": 1.15,
         "min_pages": 4, "height": 150, "charts": [{"type": "gantt",
          "columns": ["May", "Jun", "Jul", "Aug", "Sep", "Oct"],
          "groups": ["Northlight", "Cobalt"],
          "tasks": [
              {"label": "Northlight · floors 6 – 9", "start": 0,
               "end": 2.5},
              {"label": "Northlight · floors 1 – 5", "start": 1.5,
               "end": 4},
              {"label": "Northlight · ground and snagging", "start": 3.5,
               "end": 4.5},
              {"label": "Cobalt · all floors", "start": 0, "end": 4.8,
               "group": 1},
              {"label": "Cobalt · snagging", "start": 4.8, "end": 5.3,
               "group": 1},
              {"label": "Wave 1 moves in", "start": 3.6,
               "milestone": True, "text": "18 Sep"},
          ]}]},
        {"heading": "Social value offered", "kind": "figure",
         "weight": 1.2, "min_pages": 4, "height": 120, "charts": [{
             "type": "progress", "format": "{:.0f}", "max": 40,
             "items": [
                 {"label": "Apprentices", "value": 40, "status": "good",
                  "display": "40 · Northlight"},
                 {"label": "Local suppliers (%)", "value": 34,
                  "status": "good", "display": "34 % · Northlight"},
                 {"label": "Furniture reused (%)", "value": 28,
                  "status": 0, "display": "28 % · Northlight"},
                 {"label": "School visits", "value": 12, "status": 3,
                  "display": "12 · Northlight"},
             ]}]},
    ],
}
