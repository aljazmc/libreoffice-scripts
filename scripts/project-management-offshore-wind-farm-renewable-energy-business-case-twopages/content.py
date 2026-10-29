"""Business Case of Northgate Offshore Wind: the project and everything the
document could say. The typesetting keeps what fits into two pages, the most
important first."""

PROJECT = {
    "name": "Northgate Offshore Wind",
    "code": "NOW-1",
    "author": "Ingrid Solberg, Development Director",
}

DOCUMENT = {
    "title": "Business Case",
    "subtitle": "Final investment decision for a 1.2 GW offshore wind farm, "
                "62 km off the coast, in water 28 to 41 m deep",
    "meta": [("Project", "NOW-1"), ("Capacity", "1,200 MW"),
             ("Capex", "€3.9bn"), ("Decision", "FID, Board of 12 May"),
             ("Version", "4.0")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "charts": [{"type": "kpis",
         "tiles": [
             {"label": "NPV at 7 %", "value": "€612m", "status": "good",
              "note": "post-tax, real"},
             {"label": "Project IRR", "value": "9.4 %", "status": 0,
              "note": "hurdle 8.0 %"},
             {"label": "LCOE", "value": "€58/MWh", "status": 1,
              "note": "CfD strike €71/MWh"},
             {"label": "Homes powered", "value": "1.3m", "status": 3,
              "note": "4.9 TWh a year"},
         ]}]},
        {"heading": "The ask", "kind": "callout", "weight": 0.15,
         "tone": "accent", "label": "The board is asked",
         "text": "to take the final investment decision on Northgate "
                 "Offshore Wind: €3.9bn of capital expenditure, of which "
                 "€1.4bn equity from us and €2.5bn project finance, for "
                 "first power in Q3 2029 and full operation in Q2 2030."},
        {"heading": "Strategic case", "kind": "text", "weight": 0.2,
         "step": 0.5, "paragraphs": [
             "Northgate takes our offshore portfolio from 1.6 GW to "
             "2.8 GW and delivers 40 % of the 2030 renewable target in "
             "the group strategy. It has a 15-year contract for "
             "difference at €71/MWh, indexed to inflation, which takes "
             "away most of the price risk for the life of the debt.",
             "The site has the best wind resource of our pipeline: a "
             "mean wind speed of 10.1 m/s at hub height and a net "
             "capacity factor of 46.6 %.",
         ]},
        {"heading": "Options considered", "kind": "table", "weight": 0.3,
         "step": 0.1, "badges": {"Preferred": "good", "Rejected": "bad",
                                 "Fallback": "warn"},
         "columns": [("Option", 2.4), ("Capex", 1, "end"),
                     ("NPV", 1, "end"), ("IRR", 0.8, "end"),
                     ("Verdict", 1.1, "center")],
         "rows": [
             ["Do nothing: sell the seabed lease", "€0", "€85m", "—",
              "Rejected"],
             ["800 MW with 15 MW turbines", "€2.8bn", "€310m", "8.6 %",
              "Fallback"],
             ["1,200 MW with 15 MW turbines", "€3.9bn", "€612m", "9.4 %",
              "Preferred"],
             ["1,200 MW with 18 MW turbines", "€3.8bn", "€640m", "9.6 %",
              "Rejected"],
         ]},
        {"heading": "Value bridge", "kind": "figure", "weight": 0.4,
         "min_pages": 2, "height": 175, "charts": [{"type": "waterfall",
          "format": "€{:,.0f}m", "axis_format": "{:,.0f}",
          "total_color": 0,
          "steps": [("Revenue (CfD + merchant)", 7840),
                    ("Operations", -1960), ("Grid charges", -540),
                    ("Capex", -3900), ("Decommissioning", -310),
                    ("Tax", -360), ("Discounting", -158),
                    ("NPV", None)]}]},
        {"heading": "Sensitivities", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": 170, "charts": [{"type": "bars",
          "horizontal": True, "stacked": False, "format": "{:+,.0f}",
          "title": "Change in NPV", "subtitle": "€m, for a plausible "
          "swing either way",
          "categories": ["Capex ±10 %", "Capacity factor ±2 pts",
                         "Merchant price ±20 %", "Opex ±10 %",
                         "Delay 6 months", "Interest ±1 pt"],
          "series": [{"name": "Downside", "color": "bad",
                      "values": [-330, -260, -110, -150, -140, -120]},
                     {"name": "Upside", "color": "good",
                      "values": [330, 260, 110, 150, 0, 120]}]}]},
        {"heading": "Financing", "kind": "figure", "weight": 0.6,
         "min_pages": 2, "height": 150, "widths": [2, 3], "charts": [
             {"type": "donut", "title": "Sources", "format": "€{:,.1f}bn",
              "center": ("€3.9bn", "capex"),
              "segments": [("Senior debt", 2.3), ("Export credit", 0.2),
                           ("Our equity", 1.0), ("Partner equity",
                                                 0.4)]},
             {"type": "line", "title": "Debt service cover ratio",
              "x": ["2030", "2032", "2034", "2036", "2038", "2040",
                    "2042", "2044"],
              "zero": False, "format": "{:.2f}", "target": 1.3,
              "target_label": "covenant",
              "series": [{"name": "P50", "values": [1.45, 1.48, 1.5, 1.52,
                                                   1.55, 1.57, 1.6,
                                                   1.62]},
                         {"name": "P90", "color": 1, "dash": True,
                          "values": [1.31, 1.33, 1.35, 1.36, 1.38, 1.4,
                                     1.42, 1.44]}]},
         ]},
        {"heading": "Economic case", "kind": "bullets", "weight": 0.7,
         "step": 0.15, "min_pages": 2, "items": [
             "Avoids 2.1 million tonnes of CO2 a year against the "
             "current grid mix.",
             "1,800 jobs in construction and 140 permanent jobs at the "
             "operations base in Eastport.",
             "€290m of the contracts go to suppliers in the region, "
             "including the cable laying and the operations vessels.",
         ]},
        {"heading": "Commercial case", "kind": "entries", "weight": 0.8,
         "step": 0.2, "inner": 0.1, "min_pages": 4, "entries": [
             {"title": "Turbines", "org": "Nordvind 15 MW",
              "dates": "€1.35bn", "text": [
                  "80 turbines, reserved under a capacity agreement; "
                  "five-year service agreement with availability "
                  "guaranteed at 97 %."]},
             {"title": "Foundations", "org": "Monopiles, Steelbridge",
              "dates": "€0.72bn", "text": [
                  "Fixed price for steel bought by June; transition "
                  "pieces from a yard in the region."]},
             {"title": "Cables", "org": "Baltic Cable",
              "dates": "€0.58bn", "text": [
                  "Export and array cables, supply and installation, "
                  "under one contract."]},
             {"title": "Substations", "org": "Two offshore, one onshore",
              "dates": "€0.61bn", "text": [
                  "Transferred to the grid operator 18 months after "
                  "completion at a regulated price."]},
         ]},
        {"heading": "Capex by year", "kind": "figure", "weight": 0.9,
         "min_pages": 4, "height": 160, "charts": [{"type": "bars",
          "stacked": True, "subtitle": "€m", "title": "Spend profile",
          "format": "{:,.0f}",
          "categories": ["2026", "2027", "2028", "2029", "2030"],
          "series": [{"name": "Turbines", "values": [120, 270, 540, 400,
                                                     20]},
                     {"name": "Foundations", "values": [90, 300, 280, 50,
                                                        0]},
                     {"name": "Electrical", "values": [80, 360, 520, 210,
                                                       20]},
                     {"name": "Development and other", "color": 4,
                      "values": [140, 110, 120, 110, 40]}]}]},
        {"heading": "Management case", "kind": "figure", "weight": 1.0,
         "min_pages": 4, "height": 135, "charts": [{"type": "timeline",
          "start": 2025, "end": 2031, "label_width": 100,
          "phases": [(2025, 2026.4, "Develop"),
                     (2026.4, 2029.5, "Construct"),
                     (2029.5, 2031, "Operate")],
          "ticks": [(y, str(y)) for y in range(2025, 2032)],
          "events": [
              {"at": 2025.3, "label": "Consent granted", "status":
               "done"},
              {"at": 2025.9, "label": "CfD awarded", "status": "done"},
              {"at": 2026.36, "label": "FID", "sub": "12 May 2026",
               "status": "now"},
              {"at": 2027.5, "label": "Onshore works"},
              {"at": 2028.4, "label": "First foundation"},
              {"at": 2029.6, "label": "First power"},
              {"at": 2030.4, "label": "Full operation"},
          ]}]},
        {"heading": "Key risks", "kind": "table", "weight": 1.1,
         "step": 0.15, "min_pages": 4, "badges": {"High": "bad",
                                                 "Medium": "warn",
                                                 "Low": "good"},
         "columns": [("Risk", 3), ("Level", 0.8, "center"),
                     ("Mitigation", 3.2)],
         "rows": [
             ["Installation vessel not available in 2028", "High",
              "Reserved with a two-season window; second vessel on "
              "option"],
             ["Grid connection delayed", "Medium", "Connection "
              "agreement with damages; onshore works started early"],
             ["Turbine supplier capacity", "Medium", "Reservation fee "
              "paid; factory slots fixed"],
             ["Seabed boulders", "Low", "Geophysical survey of 100 % "
              "of positions done"],
         ]},
        {"heading": "Recommendation", "kind": "motto", "weight": 1.2,
         "min_pages": 4, "text": "Take the final investment decision: the "
         "project clears the hurdle in every scenario but the combined "
         "downside, and secures 40 % of our 2030 target."},
    ],
}
