"""Procurement Plan of Cold Chain for Every Child: the project and everything
the document could say. The typesetting keeps what fits into one page, the
most important first."""

PROJECT = {
    "name": "Cold Chain for Every Child",
    "code": "CCEC",
    "author": "Fatuma Hassan, Procurement and Logistics Manager",
}

METHOD = {"Open tender": "info", "UN agency": "good",
          "Request for quotes": "warn", "Framework": "accent"}

DOCUMENT = {
    "title": "Procurement Plan",
    "subtitle": "What we buy for the cold chain, how, when and for how "
                "much · 2025 – 2026",
    "meta": [("Programme", "CCEC"), ("Lots", "9"),
             ("Value", "US$ 3.94m"), ("Rules", "Donor + national"),
             ("Owner", "Fatuma Hassan")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "height": {1: 125, 2: 135},
         "widths": [2, 3], "charts": [
             {"type": "donut", "title": "Value by lot",
              "format": "${:,.0f}k", "center": ("$3.94m", "9 lots"),
              "segments": [("Solar fridges", 2120),
                           ("Remote monitors", 310),
                           ("Motorbikes", 540),
                           ("Cold boxes and carriers", 190),
                           ("Tablets", 240), ("Other lots", 540)]},
             {"type": "bars", "horizontal": True, "title": "By method",
              "format": "${:,.0f}k",
              "categories": ["UN agency", "Open tender", "Framework",
                             "Request for quotes"],
              "series": [{"name": "Value", "values": [2430, 780, 410,
                                                      320],
                          "colors": ["good", "info", "accent",
                                     "warn"]}]},
         ]},
        {"heading": "Lots", "kind": "table", "weight": 0.2, "step": 0.05,
         "badges": METHOD,
         "columns": [("Lot", 2.4), ("Quantity", 1, "end"),
                     ("Value", 0.9, "end"), ("Method", 1.4, "center"),
                     ("Award", 0.9, "center")],
         "rows": [
             ["1 Solar direct-drive fridges", "212", "$2,120k",
              "UN agency", "Mar 25"],
             ["2 Remote temperature monitors", "260", "$310k",
              "UN agency", "Mar 25"],
             ["3 Motorbikes, 125 cc", "120", "$540k", "Open tender",
              "May 25"],
             ["4 Cold boxes and vaccine carriers", "900", "$190k",
              "Framework", "Apr 25"],
             ["5 Tablets and cases", "260", "$240k", "Open tender",
              "Jun 25"],
             ["6 Installation services", "4 districts", "$220k",
              "Framework", "Apr 25"],
             ["7 Spare parts kits", "40", "$90k", "Request for quotes",
              "Sep 25"],
             ["8 Motorbike servicing", "3 years", "$130k",
              "Request for quotes", "Jul 25"],
             ["9 Anti-theft frames", "212", "$100k", "Request for "
              "quotes", "Aug 26"],
         ]},
        {"heading": "Timeline", "kind": "figure", "weight": 0.3,
         "height": {1: 160, 2: 175, 4: 185}, "charts": [{"type": "gantt",
          "columns": ["Q1 25", "Q2", "Q3", "Q4", "Q1 26", "Q2", "Q3"],
          "groups": ["Tender", "Delivery", "Install"],
          "tasks": [
              {"label": "Fridges and monitors (UN)", "start": 0,
               "end": 0.8, "progress": 1},
              {"label": "Fridges shipped and cleared", "start": 0.8,
               "end": 2.2, "group": 1, "progress": 1,
               "text": "sea freight"},
              {"label": "Installation, 212 sites", "start": 1.6,
               "end": 4.2, "group": 2, "progress": 1, "critical": True},
              {"label": "Motorbikes tender", "start": 0.5, "end": 1.6,
               "progress": 1},
              {"label": "Motorbikes delivered", "start": 1.8, "end": 2.6,
               "group": 1, "progress": 1},
              {"label": "Tablets tender and delivery", "start": 1,
               "end": 2.8, "group": 1, "progress": 1},
              {"label": "Spare parts kits", "start": 2.6, "end": 3.6,
               "group": 1, "progress": 1},
              {"label": "Anti-theft frames", "start": 6, "end": 6.9,
               "progress": 0.2},
          ]}]},
        {"heading": "Why these methods", "kind": "text", "weight": 0.4,
         "step": 0.3, "min_pages": 2, "paragraphs": [
             "Fridges and monitors are bought through the UN agency's "
             "procurement service: the prices are pooled across "
             "countries, every model is prequalified for vaccines, and "
             "the warranty includes the first two years of service.",
             "Motorbikes and tablets go to open national tender, so that "
             "local dealers can bid and service what they sell. Small "
             "lots under US$ 150,000 use requests for at least three "
             "quotes.",
         ]},
        {"heading": "Spend", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": 150, "charts": [{"type": "line",
          "title": "Committed and paid", "subtitle": "US$ m, "
          "cumulative", "format": "{:.1f}",
          "x": ["Q1 25", "Q2", "Q3", "Q4", "Q1 26", "Q2", "Q3"],
          "end_labels": True,
          "series": [{"name": "Committed", "color": 1,
                      "values": [2.4, 3.3, 3.6, 3.8, 3.8, 3.8, 3.94]},
                     {"name": "Paid", "area": True,
                      "values": [0.8, 1.9, 2.9, 3.4, 3.6, 3.7, 3.8]}]}]},
        {"heading": "Controls", "kind": "bullets", "weight": 0.6,
         "step": 0.15, "min_pages": 2, "items": [
             "Evaluation committees of three, with a member from the "
             "district health office, sign conflict of interest "
             "declarations.",
             "Every award over US$ 50,000 is approved by the country "
             "director and reported to the donor.",
             "Goods are received by two people and checked against the "
             "specification before payment.",
             "Assets are tagged and listed in the asset register within "
             "a week of delivery.",
         ]},
        {"heading": "Supplier performance", "kind": "figure",
         "weight": 0.8, "min_pages": 4, "height": 145, "charts": [{
             "type": "heatmap", "rows": ["Fridges (UN agency)",
                                         "Motorbikes (Highland Motors)",
                                         "Tablets (TechHub)",
                                         "Installation (SolarServe)",
                                         "Cold boxes (framework)"],
             "cols": ["On time", "Quality", "Documents", "Service"],
             "values": [["Good", "Good", "Good", "Good"],
                        ["Late", "Good", "Fair", "Good"],
                        ["Good", "Fair", "Good", "Fair"],
                        ["Fair", "Good", "Good", "Good"],
                        ["Good", "Good", "Fair", "Good"]],
             "badges": {"Good": "good", "Fair": "warn", "Late": "bad"},
             "labels": 0.3}]},
        {"heading": "Risks", "kind": "table", "weight": 0.9, "step": 0.1,
         "min_pages": 4, "badges": {"High": "bad", "Medium": "warn",
                                    "Low": "good"},
         "columns": [("Risk", 3.2), ("Level", 0.9, "center"),
                     ("Control", 3.2)],
         "rows": [
             ["Customs delays on fridges", "High", "Duty waiver letter "
              "from the ministry before shipping"],
             ["Currency moves on local tenders", "Medium", "Prices fixed "
              "in US dollars where the law allows"],
             ["Theft of solar panels", "Medium", "Anti-theft frames, "
              "community watch"],
             ["Single bidder for motorbikes", "Low", "Market survey "
              "showed four dealers"],
         ]},
        {"heading": "Savings", "kind": "figure", "weight": 1.0,
         "min_pages": 4, "height": 150, "charts": [{"type": "waterfall",
          "format": "${:,.0f}k", "axis_format": "{:,.0f}",
          "invert": True, "total_color": 0,
          "steps": [("Budget", 4210), ("Pooled fridge price", -190),
                    ("Motorbike tender", -60), ("Freight", 40),
                    ("Anti-theft frames", 100),
                    ("Tablets", -40), ("Other", -120),
                    ("Committed", None)]}]},
        {"heading": "Lessons", "kind": "bullets", "weight": 1.1,
         "step": 0.2, "min_pages": 4, "items": [
             "Order spare parts with the equipment, not after the first "
             "failure.",
             "Ask the district to receive goods with us: they know what "
             "works on their roads.",
             "Plan for theft from the start in remote sites.",
         ]},
        {"heading": "Deliveries by district", "kind": "figure",
         "weight": 1.15, "min_pages": 4, "height": 150, "charts": [{
             "type": "bars", "stacked": True, "title": "Items delivered",
             "categories": ["Baringo North", "Lake Shore",
                            "Highlands East", "Dry Plains"],
             "series": [{"name": "Fridges", "values": [54, 68, 41, 49]},
                        {"name": "Motorbikes", "values": [28, 34, 30,
                                                          28]},
                        {"name": "Tablets", "values": [62, 78, 52, 58]},
                        {"name": "Cold boxes", "color": 4,
                         "values": [210, 260, 200, 230]}],
             "inside": True}]},
        {"heading": "Asset register", "kind": "table", "weight": 1.2,
         "step": 0.1, "min_pages": 4, "badges": {"In use": "good",
                                                "Repair": "warn",
                                                "Lost": "bad"},
         "columns": [("Asset", 2.4), ("Count", 0.9, "end"),
                     ("In use", 0.9, "end"), ("Repair", 0.9, "end"),
                     ("Lost or stolen", 1.2, "end")],
         "rows": [
             ["Solar fridges", "212", "206", "4", "2"],
             ["Remote monitors", "260", "251", "6", "3"],
             ["Motorbikes", "120", "113", "6", "1"],
             ["Tablets", "260", "244", "9", "7"],
         ]},
        {"kind": "callout", "weight": 1.25, "tone": "info",
         "min_pages": 4, "label": "Next tender:",
         "text": "motorbike replacements for 2027 will be bought under "
                 "the ministry's national framework, which the programme "
                 "helped set up."},
    ],
}
