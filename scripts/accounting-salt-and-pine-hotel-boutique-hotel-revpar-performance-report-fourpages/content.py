"""RevPAR Performance of Salt & Pine Hotel: the business and everything the
document could say. The typesetting keeps what fits into four pages, the
most important first."""

BUSINESS = {
    "name": "Salt & Pine Hotel",
    "author": "Salt & Pine Hotel, revenue manager Ines Carvalho",
}

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep"]
OCC = [0.49, 0.55, 0.62, 0.76, 0.84, 0.90, 0.93, 0.94, 0.86]
ADR = [198, 204, 219, 247, 276, 304, 326, 337, 291]
COMP_OCC = [0.51, 0.56, 0.60, 0.72, 0.80, 0.86, 0.91, 0.93, 0.83]
COMP_ADR = [182, 186, 198, 221, 249, 275, 301, 312, 268]
OCC_INDEX = round(OCC[-1] / COMP_OCC[-1] * 100)
RATE_INDEX = round(ADR[-1] / COMP_ADR[-1] * 100)
REVPAR = [round(o * a) for o, a in zip(OCC, ADR)]
COMP_REVPAR = [round(o * a) for o, a in zip(COMP_OCC, COMP_ADR)]
INDEX = [round(r / c * 100) for r, c in zip(REVPAR, COMP_REVPAR)]

DOCUMENT = {
    "title": "RevPAR Performance",
    "subtitle": "January to September 2027 · against a competitive set "
                "of five coastal hotels",
    "meta": [("Period", "Jan – Sep 2027"),
             ("Occupancy", f"{sum(OCC) / len(OCC):.0%}"),
             ("Average rate", f"£{sum(ADR) / len(ADR):.0f}"),
             ("RevPAR", f"£{sum(REVPAR) / len(REVPAR):.0f}"),
             ("RevPAR index", f"{sum(INDEX) / len(INDEX):.0f}")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "charts": [{"type": "kpis",
         "tiles": [
             {"label": "RevPAR, September", "value": f"£{REVPAR[-1]}",
              "status": 0, "delta": "+11 %", "spark": REVPAR},
             {"label": "Occupancy index", "value": str(OCC_INDEX),
              "status": 1, "note": "100 = the comp set"},
             {"label": "Rate index", "value": str(RATE_INDEX),
              "status": 2, "note": "we charge 9 % more"},
             {"label": "RevPAR index", "value": str(INDEX[-1]),
              "status": "good", "note": "fair share is 100"}]}]},
        {"heading": "RevPAR against the market", "kind": "figure",
         "weight": 0.2, "height": {1: 170, 2: 185, 4: 195},
         "charts": [{"type": "line", "subtitle": "£ revenue per "
                                                 "available room",
          "x": MONTHS, "format": "{:.0f}", "end_labels": True,
          "series": [{"name": "Salt & Pine", "area": True,
                      "values": REVPAR},
                     {"name": "Competitive set", "color": 1, "dash": True,
                      "values": COMP_REVPAR}]}]},
        {"heading": "Month by month", "kind": "table", "whole": True,
         "weight": 0.3,
         "badges": {str(i): "good" for i in range(105, 130)},
         "columns": [("", 1.4)] + [(m, 0.7, "end") for m in MONTHS],
         "rows": [["Occupancy"] + [f"{o:.0%}" for o in OCC],
                  ["Average rate"] + [f"£{a}" for a in ADR],
                  {"cells": ["RevPAR"] + [f"£{r}" for r in REVPAR],
                   "style": "subtotal"},
                  {"cells": ["Comp set RevPAR"] + [f"£{r}" for r in
                                                   COMP_REVPAR],
                   "style": "muted"},
                  {"cells": ["RevPAR index"] + [str(i) for i in INDEX],
                   "style": "highlight"}]},
        {"heading": "By segment", "kind": "figure", "weight": 0.4,
         "min_pages": 2, "height": 160, "widths": [2, 3], "charts": [
             {"type": "donut", "title": "Room nights",
              "segments": [("Leisure, direct", 46), ("Online agencies",
                                                     28),
                           ("Packages and breaks", 14),
                           ("Groups and weddings", 8),
                           ("Corporate", 4)],
              "format": "{:.0f}%", "center": ("8,970", "room nights")},
             {"type": "bars", "horizontal": True, "title": "Average rate "
              "by segment", "format": "£{:.0f}",
              "categories": ["Leisure, direct", "Online agencies",
                             "Packages", "Groups", "Corporate"],
              "series": [{"name": "Rate", "values": [301, 274, 338, 246,
                                                     212]}]},
         ]},
        {"heading": "Channels", "kind": "table", "whole": True,
         "weight": 0.5, "min_pages": 2,
         "columns": [("Channel", 2), ("Share", 0.8, "end"),
                     ("Commission", 1, "end"),
                     ("Net rate", 1, "end")],
         "rows": [["Own website", "39 %", "2 %", "£293"],
                  ["Telephone and email", "18 %", "0 %", "£301"],
                  ["Online agency A", "21 %", "18 %", "£224"],
                  ["Online agency B", "7 %", "15 %", "£235"],
                  ["Tour operators and groups", "15 %", "20 %", "£203"]]},
        {"heading": "Pace for the next three months", "kind": "figure",
         "weight": 0.6, "min_pages": 4, "height": 155, "charts": [{
             "type": "bars", "subtitle": "room nights on the books today "
             "against the same day last year",
             "categories": ["October", "November", "December"],
             "series": [{"name": "Last year", "color": 4,
                         "values": [812, 498, 611]},
                        {"name": "This year", "values": [874, 552,
                                                         703]}]}]},
        {"heading": "Pricing decisions", "kind": "entries",
         "weight": 0.7, "step": 0.2, "inner": 0.1, "min_pages": 4,
         "entries": [
             {"title": "Hold rates in October", "text": [
                 "Pace is 8 % ahead; no discounting for half term."]},
             {"title": "Winter breaks from November", "text": [
                 "Three nights for the price of two with dinner, sold "
                 "direct only, to protect the rate and cut commission."]},
             {"title": "Close online agency B for December weekends",
              "text": ["The direct channel already covers the demand."]},
         ]},
        {"heading": "Occupancy and rate", "kind": "figure",
         "weight": 0.8, "min_pages": 4, "height": 150, "charts": [{
             "type": "quadrant", "x": "occupancy index",
             "y": "rate index",
             "quadrants": ["Rate leader", "Market leader",
                           "Losing ground", "Volume leader"],
             "points": [(m, min(o / c * 100 - 90, 10) * 0.7 + 1,
                         min(a / ca * 100 - 100, 12) * 0.75,
                         0 if i == len(MONTHS) - 1 else 4)
                        for i, (m, o, c, a, ca) in enumerate(zip(
                            MONTHS, OCC, COMP_OCC, ADR, COMP_ADR))]}]},
        {"heading": "Definitions", "kind": "tags", "weight": 0.9,
         "step": 0.1, "min_pages": 4, "items": [
             ("Occupancy", "rooms sold ÷ rooms available"),
             ("Average rate", "room revenue ÷ rooms sold, net of VAT "
                              "and breakfast"),
             ("RevPAR", "room revenue ÷ rooms available"),
             ("Index", "ours ÷ the competitive set × 100"),
         ]},
        {"heading": "Day of week", "kind": "figure", "weight": 1.0,
         "min_pages": 4, "height": 150, "charts": [{"type": "heatmap",
          "subtitle": "occupancy %, by month and day",
          "rows": ["Jun", "Jul", "Aug", "Sep"],
          "cols": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
          "values": [[82, 84, 86, 92, 98, 99, 88],
                     [88, 89, 91, 95, 99, 100, 90],
                     [90, 91, 92, 96, 99, 100, 91],
                     [76, 79, 82, 88, 97, 99, 80]],
          "thresholds": [(0, "warn"), (85, 0), (95, "good")],
          "format": "{:.0f}", "labels": 0.12}]},
        {"heading": "Competitive set", "kind": "table", "whole": True,
         "weight": 1.1, "min_pages": 4,
         "columns": [("Hotel", 2.4), ("Rooms", 0.8, "end"),
                     ("Average rate", 1, "end"),
                     ("Occupancy", 1, "end")],
         "rows": [["The Harbour Inn", "28", "£258", "84 %"],
                  ["Coastline Manor", "64", "£281", "79 %"],
                  ["Saltmarsh Lodge", "19", "£236", "86 %"],
                  ["The Victoria", "51", "£248", "82 %"],
                  ["Dunes Retreat", "34", "£312", "77 %"],
                  {"cells": ["Salt & Pine", "42", f"£{ADR[-1]}",
                             f"{OCC[-1]:.0%}"], "style": "highlight"}]},
        {"heading": "What drove the gain", "kind": "figure",
         "weight": 1.2, "min_pages": 4, "height": 150, "charts": [{
             "type": "waterfall", "format": "£{:.0f}",
             "axis_format": "{:.0f}", "total_color": 0,
             "subtitle": "September RevPAR against last year",
             "steps": [("Sep 2026", 225), ("Higher rate", 15),
                       ("Higher occupancy", 7), ("Packages", 3),
                       ("Sep 2027", None)]}]},
    ],
}
