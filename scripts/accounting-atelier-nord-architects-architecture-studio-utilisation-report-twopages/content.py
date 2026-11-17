"""Utilisation Report of Atelier Nord: the business and everything the document
could say. The typesetting keeps what fits into two pages, the most
important first."""

BUSINESS = {
    "name": "Atelier Nord",
    "author": "Oskar Berg, associate",
}

# person, role, available hours in the quarter, billable hours,
# target utilisation
PEOPLE = [("Ingrid Lund", "Partner", 462, 231, 0.50),
          ("Erik Nord", "Partner", 462, 208, 0.50),
          ("Oskar Berg", "Associate", 476, 343, 0.70),
          ("Mia Holm", "Architect", 476, 381, 0.80),
          ("Jonas Aalto", "Architect", 434, 330, 0.80),
          ("Ana Sousa", "Technologist", 476, 400, 0.85),
          ("Leo Strand", "Part 2 assistant", 476, 357, 0.80),
          ("Freya Dahl", "Part 1 assistant", 420, 273, 0.75),
          ("Sam Reid", "Studio manager", 476, 24, 0.05)]
WEEKS = ["W27", "W28", "W29", "W30", "W31", "W32", "W33", "W34", "W35",
         "W36", "W37", "W38", "W39"]
STUDIO = [0.63, 0.65, 0.67, 0.62, 0.51, 0.45, 0.48, 0.64, 0.67, 0.69,
          0.68, 0.66, 0.64]

AVAILABLE = sum(p[2] for p in PEOPLE)
BILLABLE = sum(p[3] for p in PEOPLE)

DOCUMENT = {
    "title": "Utilisation Report",
    "subtitle": "Q3 2027 · July to September · how much of the studio's "
                "time was spent on fee-earning work",
    "meta": [("Quarter", "Q3 2027"), ("People", str(len(PEOPLE))),
             ("Hours available", f"{AVAILABLE:,}"),
             ("Billable", f"{BILLABLE:,}"),
             ("Utilisation", f"{BILLABLE / AVAILABLE:.0%}")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "charts": [{"type": "kpis",
         "tiles": [
             {"label": "Studio utilisation",
              "value": f"{BILLABLE / AVAILABLE:.0%}", "status": 1,
              "note": "target 70 %", "spark": [s * 100 for s in STUDIO]},
             {"label": "Billable hours", "value": f"{BILLABLE:,}",
              "status": 0, "note": "+6 % on Q2"},
             {"label": "Recovery", "value": "88 %", "status": "warn",
              "note": "of billable time at full rate"},
             {"label": "Holiday taken", "value": "41 days",
              "status": 2, "note": "summer quarter"}]}]},
        {"heading": "By person", "kind": "figure", "weight": 0.2,
         "height": {1: 190, 2: 200, 4: 210}, "charts": [{
             "type": "progress", "format": "{:.0f} %", "items": [
                 {"label": f"{n} · {r}", "value": b / a * 100,
                  "target": t * 100,
                  "status": "good" if b / a >= t else "warn"
                  if b / a >= t - 0.1 else "bad",
                  "display": f"{b / a:.0%}"} for n, r, a, b, t in
                 PEOPLE]}]},
        {"heading": "Week by week", "kind": "figure", "weight": 0.3,
         "height": {1: 130, 2: 150, 4: 160}, "charts": [{"type": "line",
          "subtitle": "% of available hours billed", "x": WEEKS,
          "format": "{:.0f}", "target": 70, "target_label": "target",
          "zero": False, "marks": [(4, "summer holidays")],
          "series": [{"name": "Studio", "area": True,
                      "values": [s * 100 for s in STUDIO]}]}]},
        {"heading": "Hours by project", "kind": "figure", "weight": 0.4,
         "min_pages": 2, "height": 175, "charts": [{"type": "heatmap",
          "subtitle": "billable hours in the quarter",
          "rows": [p[0] for p in PEOPLE[:8]],
          "cols": ["Ashby Library", "Mill Yard", "Kestrel", "Sandhill",
                   "Harbour House", "St Mary's", "Ferry study"],
          "values": [[42, 61, 38, 54, 12, 14, 10],
                     [18, 52, 20, 70, 22, 8, 18],
                     [88, 96, 41, 72, 18, 12, 16],
                     [126, 102, 54, 54, 21, 12, 12],
                     [62, 94, 36, 98, 18, 14, 8],
                     [104, 88, 12, 148, 6, 38, 4],
                     [118, 98, 48, 52, 24, 9, 8],
                     [72, 84, 46, 34, 22, 4, 11]],
          "format": "{:.0f}", "labels": 0.16}]},
        {"heading": "Where the other time went", "kind": "figure",
         "weight": 0.5, "min_pages": 2, "height": 150, "widths": [2, 3],
         "charts": [
             {"type": "donut", "title": "Non-billable hours",
              "segments": [("Holiday", 328), ("Competitions and bids",
                                              412),
                           ("Studio admin and IT", 452),
                           ("Training and CPD", 168),
                           ("Marketing", 151), ("Sickness", 100)],
              "format": "{:,.0f} h", "center": (
                  f"{AVAILABLE - BILLABLE:,}", "hours")},
             {"type": "bars", "title": "Utilisation by role",
              "format": "{:.0f}%", "target": 70, "target_label": "studio",
              "categories": ["Partners", "Associate", "Architects",
                             "Technologist", "Assistants"],
              "series": [{"name": "Q2", "color": 4,
                          "values": [44, 69, 76, 82, 70]},
                         {"name": "Q3", "values": [47, 72, 78, 84, 70]}]},
         ]},
        {"heading": "Observations", "kind": "bullets", "weight": 0.6,
         "step": 0.1, "min_pages": 2, "items": [
             "**Ana Sousa is over-stretched** at 84 %; Sandhill School "
             "construction drawings fall almost entirely on her.",
             "**Freya Dahl is under target** because she spent 60 hours "
             "on the Ferry Terminal competition, which we did not win.",
             "**Partners' time** went into two bids and the Mill Yard "
             "fee dispute.",
         ]},
        {"heading": "Capacity next quarter", "kind": "table",
         "whole": True, "weight": 0.7, "min_pages": 4,
         "columns": [("Month", 1), ("Available", 1, "end"),
                     ("Booked on projects", 1.2, "end"),
                     ("Free", 1, "end"), ("Booked", 0.8, "end")],
         "rows": [["October", "1,410", "1,082", "328", "77 %"],
                  ["November", "1,380", "934", "446", "68 %"],
                  ["December", "1,050", "612", "438", "58 %"],
                  {"cells": ["Q4", "3,840", "2,628", "1,212", "68 %"],
                   "style": "total"}]},
        {"heading": "Recovery by project", "kind": "figure",
         "weight": 0.8, "min_pages": 4, "height": 150, "charts": [{
             "type": "bars", "horizontal": True, "format": "{:.0f}%",
             "title": "Fee earned ÷ time at standard rates",
             "target": 100, "target_label": "full recovery",
             "categories": ["Sandhill School", "St Mary's Chapel",
                            "Ashby Library", "Ferry study", "Kestrel",
                            "Harbour House", "Mill Yard"],
             "series": [{"name": "Recovery", "values": [128, 116, 104, 92,
                                                        86, 74, 81],
                         "colors": ["good", "good", "good", "warn",
                                    "warn", "bad", "bad"]}]}]},
        {"heading": "Actions", "kind": "entries", "weight": 0.9,
         "step": 0.2, "inner": 0.1, "min_pages": 4, "entries": [
             {"title": "Second technologist", "text": [
                 "A contract technologist for six months from November "
                 "relieves Ana and costs less than the overtime."]},
             {"title": "Bid discipline", "text": [
                 "Competitions need a partner's go/no-go and a budget of "
                 "hours before work starts."]},
             {"title": "Fill December", "text": [
                 "438 free hours: bring forward the Ashby stage 5 "
                 "information and pitch two feasibility studies."]},
         ]},
        {"heading": "Definitions", "kind": "tags", "weight": 1.0,
         "step": 0.1, "min_pages": 4, "items": [
             ("Available hours", "contracted hours less bank holidays"),
             ("Billable", "time booked to a fee-earning project stage"),
             ("Utilisation", "billable ÷ available"),
             ("Recovery", "fee earned ÷ billable time at standard rates"),
         ]},
        {"heading": "Leave planner", "kind": "figure", "weight": 1.1,
         "min_pages": 4, "height": 150, "charts": [{"type": "heatmap",
          "subtitle": "days of leave booked",
          "rows": [p[0] for p in PEOPLE[:8]],
          "cols": ["Oct", "Nov", "Dec", "Jan", "Feb", "Mar"],
          "values": [[2, 0, 5, 0, 3, 0], [0, 3, 4, 2, 0, 0],
                     [1, 0, 6, 0, 0, 3], [3, 2, 5, 0, 0, 0],
                     [0, 0, 7, 2, 0, 0], [2, 0, 4, 0, 5, 0],
                     [0, 4, 3, 0, 0, 2], [5, 0, 4, 0, 0, 0]],
          "format": "{:.0f}", "labels": 0.16}]},
        {"heading": "Utilisation over two years", "kind": "figure",
         "weight": 1.2, "min_pages": 4, "height": 150, "charts": [{
             "type": "bars", "subtitle": "% by quarter",
             "format": "{:.0f}%", "target": 70, "target_label": "target",
             "categories": ["Q4 25", "Q1 26", "Q2 26", "Q3 26", "Q4 26",
                            "Q1 27", "Q2 27", "Q3 27"],
             "series": [{"name": "Studio", "values": [64, 67, 66, 58, 63,
                                                      66, 65, 61],
                         "colors": [4, 4, 4, 4, 4, 4, 4, 0]}]}]},
        {"heading": "Fee income per head", "kind": "table",
         "whole": True, "weight": 1.3, "min_pages": 4,
         "columns": [("Quarter", 1.2), ("Fee income", 1, "end"),
                     ("Staff", 0.8, "end"), ("Per head", 1, "end")],
         "rows": [["Q1 2027", "£396k", "9", "£44.0k"],
                  ["Q2 2027", "£408k", "9", "£45.3k"],
                  ["Q3 2027", "£392k", "9", "£43.6k"]]},
    ],
}
