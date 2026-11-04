"""Object Loan Tracker of The Abyss: Life Below Light: the project and
everything the document could say. The typesetting keeps what fits into two
pages, the most important first."""

PROJECT = {
    "name": "The Abyss: Life Below Light",
    "code": "EX-27",
    "author": "Anouk de Wit, Registrar",
}

STATUS = {"Agreed": "good", "Contract": "info", "Requested": "warn",
          "At risk": "bad", "Declined": "neutral"}

DOCUMENT = {
    "title": "Object Loan Tracker",
    "subtitle": "Loans in for The Abyss, from 14 lenders in 6 countries · "
                "status on 1 October 2026",
    "meta": [("Exhibition", "EX-27"), ("Objects", "212"),
             ("Lenders", "14"), ("Agreed", "71 %"),
             ("Registrar", "Anouk de Wit")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "height": {1: 130, 2: 140},
         "widths": [2, 3], "charts": [
             {"type": "donut", "title": "Objects by status",
              "segments": [("Agreed", 151, "good"),
                           ("Contract", 28, "info"),
                           ("Requested", 21, "warn"),
                           ("At risk", 8, "bad"),
                           ("Declined", 4, "neutral")],
              "center": ("212", "objects")},
             {"type": "bars", "horizontal": True, "stacked": True,
              "title": "By lender", "values": False,
              "categories": ["Natural History, Leiden",
                             "Oceanographic Inst., Kiel",
                             "Marine Museum, Lisbon", "Univ. of Bergen",
                             "Royal Collection", "Nine others"],
              "series": [{"name": "Agreed", "color": "good",
                          "values": [64, 30, 18, 14, 0, 25]},
                         {"name": "In progress", "color": "warn",
                          "values": [6, 8, 9, 4, 6, 16]},
                         {"name": "At risk", "color": "bad",
                          "values": [0, 0, 0, 0, 8, 0]}]},
         ]},
        {"heading": "Loans that could fall through", "kind": "table",
         "weight": 0.2, "step": 0.1, "badges": STATUS,
         "columns": [("Object", 2.8), ("Lender", 1.8), ("Issue", 3),
                     ("Status", 1, "center")],
         "rows": [
             ["Giant squid, 7.2 m, in fluid", "Royal Collection",
              "Lender wants a case at 15 °C; ours holds 18 °C",
              "At risk"],
             ["Bathyscaphe porthole, 1960", "Marine Museum, Lisbon",
              "Needed for their own anniversary in June", "Requested"],
             ["Gulper eel, 3 specimens", "Univ. of Bergen", "Export "
              "licence for CITES species pending", "Contract"],
             ["Hydrothermal chimney fragment", "Oceanographic Inst., "
              "Kiel", "Weight 640 kg; floor loading check", "Contract"],
             ["Challenger expedition notebooks", "Royal Collection",
              "Light limit of 50 lux for 3 months only", "At risk"],
         ]},
        {"heading": "Timeline", "kind": "figure", "weight": 0.3,
         "height": {1: 150, 2: 165, 4: 175}, "charts": [{"type": "gantt",
          "columns": ["Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr",
                      "May"],
          "groups": ["Agreements", "Logistics", "Install"],
          "today": 0.05,
          "tasks": [
              {"label": "Loan requests answered", "start": 0, "end": 1.5,
               "progress": 0.7},
              {"label": "Contracts signed", "start": 0.5, "end": 3,
               "progress": 0.3},
              {"label": "Facility reports to lenders", "start": 1,
               "end": 2.5, "group": 1},
              {"label": "Insurance and indemnity", "start": 2, "end": 4,
               "group": 1},
              {"label": "Crating and transport", "start": 5, "end": 6.4,
               "group": 1, "critical": True},
              {"label": "Couriers and installation", "start": 6,
               "end": 7.4, "group": 2, "critical": True},
              {"label": "Opening", "start": 7.45, "milestone": True,
               "text": "14 May"},
          ]}]},
        {"heading": "By gallery", "kind": "figure", "weight": 0.4,
         "min_pages": 2, "height": 155, "charts": [{"type": "bars",
          "stacked": True, "title": "Objects per gallery",
          "categories": ["I. Sunlight", "II. Twilight", "III. Midnight",
                         "IV. Abyss", "V. Trenches", "VI. Surface"],
          "series": [{"name": "Our collection", "color": 0,
                      "values": [18, 24, 31, 12, 6, 9]},
                     {"name": "Loans", "color": 1,
                      "values": [12, 38, 64, 41, 32, 25]}],
          "inside": True}]},
        {"heading": "Conditions from lenders", "kind": "bullets",
         "weight": 0.5, "step": 0.15, "min_pages": 2, "items": [
             "Fluid-preserved specimens kept between 16 and 20 °C, "
             "relative humidity 45 – 55 %, logged every 15 minutes.",
             "Paper and photographs under 50 lux, no more than 12 weeks "
             "on display; facsimiles for the rest of the run.",
             "Couriers for 41 objects, present at unpacking and "
             "installation.",
             "Credit lines in the wording each lender gives us.",
         ]},
        {"heading": "Insurance", "kind": "figure", "weight": 0.6,
         "min_pages": 2, "height": 130, "widths": [3, 2], "charts": [
             {"type": "bars", "horizontal": True, "title": "Insured "
              "value by lender", "subtitle": "€m", "format": "{:.1f}",
              "categories": ["Royal Collection", "Leiden", "Lisbon",
                             "Kiel", "Others"],
              "series": [{"name": "Value", "values": [6.2, 3.8, 2.1, 1.4,
                                                      1.9]}]},
             {"type": "donut", "title": "Cover",
              "segments": [("State indemnity", 11.6, 0),
                           ("Commercial insurance", 3.8, 1)],
              "format": "€{:.1f}m", "center": ("€15.4m", "insured")},
         ]},
        {"heading": "Couriers", "kind": "table", "weight": 0.8,
         "step": 0.1, "min_pages": 4,
         "columns": [("Lender", 2), ("Couriers", 0.9, "center"),
                     ("Arrive", 1), ("Transport", 2.4)],
         "rows": [
             ["Natural History, Leiden", "2", "6 Apr",
              "Climate-controlled truck"],
             ["Oceanographic Inst., Kiel", "1", "9 Apr", "Truck, crane "
              "for the chimney"],
             ["Marine Museum, Lisbon", "1", "13 Apr", "Air freight to "
              "Amsterdam"],
             ["Univ. of Bergen", "1", "15 Apr", "Ferry and truck"],
             ["Royal Collection", "2", "20 Apr", "Fine art shipper, "
              "escorted"],
         ]},
        {"heading": "Case climate", "kind": "figure", "weight": 0.9,
         "min_pages": 4, "height": 150, "charts": [{"type": "line",
          "title": "Test of the fluid specimen cases", "subtitle":
          "°C over 14 days, September", "zero": False,
          "x": [str(d) for d in range(1, 15)], "format": "{:.0f}",
          "band": (16, 20, "lender range"),
          "series": [{"name": "Case 3 (giant squid)", "values": [
                         18.1, 18.0, 18.3, 18.6, 18.2, 17.9, 18.0, 18.4,
                         18.8, 18.5, 18.1, 18.0, 18.2, 18.3]},
                     {"name": "Gallery", "color": 1, "dash": True,
                      "values": [20.5, 20.2, 21.0, 21.8, 21.1, 20.4, 20.6,
                                 21.4, 22.0, 21.6, 20.8, 20.5, 20.9,
                                 21.2]}]}]},
        {"heading": "The giant squid", "kind": "text", "weight": 1.0,
         "step": 0.3, "min_pages": 4, "paragraphs": [
             "The Royal Collection's squid is the star of gallery III and "
             "the reason many visitors will come. Its lender asks for "
             "15 °C, three degrees below what our cases hold. We have "
             "offered a dedicated case with its own chiller, tested for "
             "three months before the loan; the decision is expected at "
             "their November committee.",
             "If they say no, the squid is replaced by a full-size cast "
             "and the museum's own 2.4 m specimen.",
         ]},
        {"heading": "Declined", "kind": "bullets", "weight": 1.1,
         "step": 0.2, "min_pages": 4, "items": [
             "Coelacanth, Paris: on loan to Tokyo until 2028.",
             "Vent tubeworms, Woods Hole: too fragile to travel.",
             "Trieste bathyscaphe model, Venice: being restored.",
         ]},
        {"heading": "Loan agreements", "kind": "figure", "weight": 1.15,
         "min_pages": 4, "height": 150, "widths": [3, 2], "charts": [
             {"type": "line", "title": "Objects agreed", "subtitle":
              "cumulative, of 212", "x": ["Mar", "Apr", "May", "Jun",
                                          "Jul", "Aug", "Sep", "Oct"],
              "target": 212, "target_label": "all", "end_labels": True,
              "series": [{"name": "Agreed", "area": True,
                          "values": [12, 30, 58, 84, 110, 128, 151,
                                     None]},
                         {"name": "Plan", "dash": True, "color": 1,
                          "values": [10, 28, 55, 85, 115, 145, 170,
                                     190]}]},
             {"type": "bars", "title": "Days to answer a request",
              "horizontal": True, "format": "{:.0f}",
              "categories": ["Leiden", "Kiel", "Lisbon", "Bergen",
                             "Royal Coll."],
              "series": [{"name": "Days", "values": [24, 31, 46, 38, 92],
                          "colors": [0, 0, 0, 0, "bad"]}]},
         ]},
        {"heading": "Facility report", "kind": "tags", "weight": 1.2,
         "step": 0.1, "min_pages": 4, "items": [
             ("Building", "1912 brick, fire compartments of 600 m²"),
             ("Security", "24-hour guards, CCTV in every gallery"),
             ("Climate", "18 – 22 °C, 45 – 55 % RH, logged every 15 "
                         "min"),
             ("Light", "UV filtered, dimmable to 30 lux"),
             ("Handling", "four trained art handlers, two cranes"),
         ]},
        {"heading": "Objects by type", "kind": "figure", "weight": 1.25,
         "min_pages": 4, "height": 140, "widths": [2, 3], "charts": [
             {"type": "donut", "title": "Loans by type",
              "segments": [("Fluid specimens", 96), ("Dry specimens", 38),
                           ("Instruments", 14), ("Archive and art", 12),
                           ("Models and casts", 8)],
              "center": ("168", "loans")},
             {"type": "heatmap", "title": "Conditions per type",
              "rows": ["Fluid specimens", "Dry specimens", "Instruments",
                       "Archive and art"],
              "cols": ["Climate", "Light", "Courier", "Mount"],
              "values": [["Strict", "Normal", "Some", "Normal"],
                         ["Normal", "Normal", "None", "Custom"],
                         ["Normal", "Normal", "Some", "Custom"],
                         ["Strict", "Strict", "All", "Custom"]],
              "badges": {"Strict": "bad", "All": "bad", "Some": "warn",
                         "Custom": "warn", "Normal": "good",
                         "None": "good"}},
         ]},
        {"heading": "Next steps", "kind": "bullets", "weight": 1.3,
         "step": 0.2, "min_pages": 4, "items": [
             "Send facility reports to the last four lenders by 15 "
             "October.",
             "Chiller case test for the giant squid from 1 November, "
             "with the Royal Collection's conservator.",
             "Book the fine art shipper for the April window.",
         ]},
    ],
}
