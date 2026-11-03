"""Earned Value Report of Harbour Bridge Retrofit: the project and everything
the document could say. The typesetting keeps what fits into one page, the
most important first."""

PROJECT = {
    "name": "Harbour Bridge Retrofit",
    "code": "HBR-24",
    "author": "Ana Novak, Project Manager, Port Aldwick City Works",
}

MONTHS = ["Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov",
          "Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
          "Sep", "Oct", "Nov", "Dec"]

DOCUMENT = {
    "title": "Earned Value Report",
    "subtitle": "Period 18 · August 2026 · cumulative to 31 August",
    "meta": [("Project", "HBR-24"), ("Period", "18 of 23"),
             ("BAC", "€45.8m"), ("Prepared by", "Ana Novak"),
             ("Status", "Amber")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "charts": [{"type": "kpis",
         "tiles": [
             {"label": "CPI", "value": "0.95", "delta": "▼ 0.01",
              "status": "warn", "note": "€0.95 earned per €1 spent",
              "spark": [1.01, 1.0, 0.99, 0.98, 0.97, 0.96, 0.96, 0.95]},
             {"label": "SPI", "value": "0.93", "delta": "▲ 0.02",
              "status": "warn", "note": "3.5 weeks behind plan",
              "spark": [0.98, 0.97, 0.94, 0.91, 0.9, 0.91, 0.92, 0.93]},
             {"label": "EAC", "value": "€47.9m", "status": "bad",
              "note": "€2.1m over BAC (4.6 %)"},
             {"label": "% complete", "value": "71 %", "status": "accent",
              "note": "EV €32.5m of €45.8m"},
         ]}]},
        {"heading": "Summary", "kind": "text", "weight": 0.2, "step": 0.6,
         "paragraphs": [
             "The project is **behind schedule and over cost, but "
             "recovering on time**. SPI has improved for the third month "
             "running as the second paint crew works through the south "
             "span. CPI keeps sliding because the bearing replacement at "
             "pier 4 needed twice the jacking we planned for.",
             "The forecast at completion is €47.9m against a budget of "
             "€45.8m. The remaining contingency of €1.7m does not cover "
             "the gap: the board is asked to release €0.4m of "
             "management reserve (see the decision below).",
         ]},
        {"heading": "Performance curves", "kind": "figure", "weight": 0.3,
         "height": {1: 170, 2: 200, 4: 240}, "charts": [{"type": "line",
          "title": "Cumulative cost", "subtitle": "€m", "x": MONTHS,
          "format": "{:.0f}", "marks": [(17, "Aug 26")],
          "end_labels": True,
          "series": [
              {"name": "Planned value (PV)", "dash": True, "color": 2,
               "values": [0.6, 1.4, 2.6, 4.4, 6.6, 9.2, 12.0, 14.6, 17.2,
                          19.6, 21.9, 24.0, 26.0, 28.0, 29.8, 31.6, 33.3,
                          34.9, 37.6, 40.4, 43.2, 45.8]},
              {"name": "Earned value (EV)", "color": 0,
               "values": [0.6, 1.3, 2.5, 4.1, 6.0, 8.4, 10.9, 13.5, 16.0,
                          18.4, 20.7, 22.9, 25.0, 27.1, 29.1, 30.9, 31.8,
                          32.5, None, None, None, None]},
              {"name": "Actual cost (AC)", "color": "accent",
               "values": [0.6, 1.3, 2.5, 4.2, 6.2, 8.6, 11.2, 13.9, 16.6,
                          19.1, 21.5, 23.8, 26.1, 28.3, 30.4, 32.0, 33.3,
                          34.2, None, None, None, None]},
          ]}]},
        {"kind": "callout", "weight": 0.35, "tone": "warn",
         "label": "Decision needed:",
         "text": "release €0.4m of management reserve to the bearings "
                 "package before the September board, so the pier 3 "
                 "jacking can be ordered on time."},
        {"heading": "Variance by package", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": 160, "widths": [1, 1], "charts": [
             {"type": "bars", "title": "Cost variance", "subtitle": "€k, "
              "EV − AC", "categories": ["Steel", "Paint", "Bearings",
                                        "Deck", "Traffic", "Design"],
              "series": [{"name": "CV", "values": [-310, 120, -980, -60,
                                                   -240, 40],
                          "colors": ["bad", "good", "bad", "bad", "bad",
                                     "good"]}],
              "format": "{:+,.0f}", "axis_format": "{:,.0f}"},
             {"type": "bars", "title": "Schedule variance",
              "subtitle": "€k, EV − PV", "categories": ["Steel", "Paint",
                                                        "Bearings", "Deck",
                                                        "Traffic",
                                                        "Design"],
              "series": [{"name": "SV", "values": [-420, -1350, -510, 90,
                                                   -30, 0],
                          "colors": ["bad", "bad", "bad", "good", "bad",
                                     "good"]}],
              "format": "{:+,.0f}", "axis_format": "{:,.0f}"},
         ]},
        {"heading": "Work packages", "kind": "table", "weight": 0.6,
         "step": 0.15, "min_pages": 2, "columns": [
             ("Package", 2.2), ("BAC", 1, "end"), ("PV", 1, "end"),
             ("EV", 1, "end"), ("AC", 1, "end"), ("CPI", 0.8, "center"),
             ("SPI", 0.8, "center")],
         "badges": {"0.76": "bad", "0.81": "bad", "0.88": "warn",
                    "0.89": "warn", "0.97": "warn", "0.98": "good",
                    "1.02": "good", "1.06": "good", "1.00": "good",
                    "1.04": "good", "1.01": "good", "0.94": "warn",
                    "0.95": "warn", "0.85": "warn"},
         "rows": [
             ["1.1 Design", "€3.1m", "€3.1m", "€3.1m", "€3.06m", "1.01",
              "1.00"],
             ["1.2 Steel strengthening", "€13.5m", "€12.8m", "€11.4m",
              "€11.7m", "0.97", "0.89"],
             ["1.2.3 Blast and paint", "€11.2m", "€9.6m", "€8.3m",
              "€8.2m", "1.01", "0.85"],
             ["1.3 Bearings and joints", "€6.8m", "€5.0m", "€4.5m",
              "€5.5m", "0.81", "0.89"],
             ["1.4 Deck", "€5.4m", "€1.4m", "€1.5m", "€1.6m", "0.94",
              "1.06"],
             ["1.5 Traffic and public", "€4.8m", "€3.8m", "€3.7m",
              "€4.0m", "0.94", "0.97"],
         ]},
        {"heading": "Forecast", "kind": "figure", "weight": 0.7,
         "min_pages": 2, "height": 170, "widths": [3, 2], "charts": [
             {"type": "waterfall", "title": "From budget to forecast",
              "subtitle": "€m", "format": "{:.1f}", "invert": True,
              "steps": [("BAC", 45.8), ("Bearing jacking", 1.4),
                        ("Corrosion", 0.9), ("Traffic nights", 0.4),
                        ("Paint savings", -0.4), ("Design savings", -0.2),
                        ("EAC", None)]},
             {"type": "donut", "title": "Contingency", "format":
              "€{:.1f}m", "center": ("€4.1m", "at start"),
              "segments": [("Used", 2.4, "accent"),
                           ("Remaining", 1.7, 0)]},
         ]},
        {"heading": "Indices over time", "kind": "figure", "weight": 1.0,
         "min_pages": 4, "height": 160, "charts": [{"type": "line",
          "x": MONTHS[:18], "zero": False, "format": "{:.2f}",
          "band": (0.95, 1.05, "tolerance"), "end_labels": True,
          "series": [
              {"name": "CPI", "color": "accent",
               "values": [1.0, 1.0, 1.0, 0.98, 0.97, 0.98, 0.97, 0.97,
                          0.96, 0.96, 0.96, 0.96, 0.96, 0.96, 0.96, 0.95,
                          0.95, 0.95]},
              {"name": "SPI", "color": 0,
               "values": [1.0, 0.93, 0.96, 0.93, 0.91, 0.91, 0.91, 0.91,
                          0.9, 0.9, 0.9, 0.91, 0.9, 0.9, 0.9, 0.9, 0.92,
                          0.93]},
          ]}]},
        {"heading": "Where the money went", "kind": "figure",
         "weight": 1.05, "min_pages": 4, "height": 150, "widths": [1, 1],
         "charts": [
             {"type": "bars", "title": "Actual cost by type",
              "subtitle": "€m, to date", "format": "{:.1f}",
              "categories": ["Labour", "Plant", "Materials",
                             "Subcontract", "Fees", "Traffic"],
              "series": [{"name": "Budget to date", "color": 4,
                          "values": [9.8, 5.1, 7.9, 6.2, 3.1, 2.8]},
                         {"name": "Actual", "color": 0,
                          "values": [10.6, 5.6, 7.8, 6.5, 3.06, 3.0]}]},
             {"type": "progress", "title": "Packages complete",
              "format": "{:.0f} %",
              "items": [
                  {"label": "Design", "value": 100, "status": "good"},
                  {"label": "Steel strengthening", "value": 84,
                   "target": 95, "status": "warn"},
                  {"label": "Blast and paint", "value": 74, "target": 86,
                   "status": "warn"},
                  {"label": "Bearings and joints", "value": 66,
                   "target": 74, "status": "bad"},
                  {"label": "Deck", "value": 28, "target": 26,
                   "status": "good"},
                  {"label": "Traffic and public", "value": 77,
                   "target": 79, "status": 0}]},
         ]},
        {"heading": "Forecast methods", "kind": "table", "weight": 1.1,
         "step": 0.2, "min_pages": 4, "columns": [
             ("Method", 2.6), ("Formula", 2.2), ("EAC", 1, "end"),
             ("Use", 2.2)],
         "rows": [
             ["Bottom-up (reported)", "AC + ETC by package", "€47.9m",
              "The forecast we stand behind"],
             ["CPI only", "BAC ÷ CPI", "€48.2m", "If overspend continues"],
             ["CPI × SPI", "AC + (BAC − EV) ÷ (CPI × SPI)", "€48.9m",
              "Pessimistic, delay costs money"],
             ["Original rate", "AC + (BAC − EV)", "€47.5m",
              "If the rest goes to plan"],
         ]},
        {"heading": "Corrective actions", "kind": "entries", "weight": 1.2,
         "step": 0.4, "inner": 0.2, "min_pages": 2, "entries": [
             {"title": "Second paint crew on the south span",
              "dates": "from 3 Aug", "items": [
                  "Recovers 2.5 of the 3.5 weeks by the end of October.",
                  "Costs €180k, paid from the paint savings."]},
             {"title": "Pier 3 jacking redesigned", "dates": "by 18 Sep",
              "items": [
                  "Halden Engineers reuse the pier 4 frames: €260k less "
                  "than a new design.",
                  "The check engineer reviews it in one week instead of "
                  "three."]},
             {"title": "Night possessions extended to Friday",
              "dates": "Sep – Nov", "items": [
                  "Agreed with the council for nine weeks; buses "
                  "diverted at a cost of €45k."]},
         ]},
        {"heading": "Earned value in brief", "kind": "tags", "weight": 1.6,
         "step": 0.1, "min_pages": 4, "items": [
             ("PV", "the budgeted cost of the work planned to date"),
             ("EV", "the budgeted cost of the work actually done"),
             ("AC", "what that work actually cost"),
             ("CPI", "EV ÷ AC; under 1 means over cost"),
             ("SPI", "EV ÷ PV; under 1 means behind plan"),
             ("EAC", "the forecast of the total cost at completion"),
         ]},
        {"heading": "Next period", "kind": "bullets", "weight": 1.4,
         "step": 0.2, "min_pages": 4, "items": [
             "Finish the jacking of pier 3 and swap its eight bearings "
             "(planned value €1.6m).",
             "Complete the second coat on spans 5 to 7.",
             "Start the deck waterproofing on the north carriageway, "
             "nights only.",
             "Agree the final account for the design contract.",
         ]},
    ],
}
