"""Profit and Loss Statement of Rye & Crumb Bakery: the business and everything
the document could say. The typesetting keeps what fits into two pages, the
most important first."""

BUSINESS = {
    "name": "Rye & Crumb Bakery",
    "author": "Rye & Crumb Ltd, prepared by Marta Ilić, bookkeeper",
}

YEARS = [("", 3.2), ("2026/27", 1, "end"), ("2025/26", 1, "end"),
         ("Change", 0.8, "end")]

MONTHS = ["Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
          "Jan", "Feb", "Mar"]

DOCUMENT = {
    "title": "Profit and Loss Statement",
    "subtitle": "For the year ended 31 March 2027 · all amounts in euro",
    "meta": [("Company", "Rye & Crumb Ltd"), ("Year", "2026/27"),
             ("Shops", "2 and a wholesale bakery"),
             ("Status", "Draft for the directors")],
    "sections": [
        {"heading": "Statement", "kind": "table", "whole": True,
         "weight": 0.1, "columns": YEARS,
         "rows": [
             {"cells": ["Revenue", "", "", ""], "style": "section"},
             {"cells": ["Shop sales, Mill Lane", "268,400", "254,100",
                        "+5.6 %"], "style": "indent", "min_pages": 2},
             {"cells": ["Shop sales, Harbour Road", "143,900", "134,000",
                        "+7.4 %"], "style": "indent", "min_pages": 2},
             {"cells": ["Shop sales", "412,300", "388,100", "+6.2 %"],
              "style": "indent", "max_pages": 1},
             {"cells": ["Wholesale to cafés and delis", "198,700",
                        "171,400", "+15.9 %"], "style": "indent"},
             {"cells": ["Bread school and events", "24,600", "16,200",
                        "+51.9 %"], "style": "indent"},
             {"cells": ["Total revenue", "635,600", "575,700", "+10.4 %"],
              "style": "subtotal"},
             {"cells": ["Cost of sales", "", "", ""], "style": "section"},
             {"cells": ["Flour and grain", "(96,200)", "(82,400)",
                        "+16.7 %"], "style": "indent", "min_pages": 2},
             {"cells": ["Butter, dairy and eggs", "(61,300)", "(58,900)",
                        "+4.1 %"], "style": "indent", "min_pages": 2},
             {"cells": ["Other ingredients", "(38,400)", "(36,100)",
                        "+6.4 %"], "style": "indent", "min_pages": 2},
             {"cells": ["Packaging", "(19,800)", "(18,700)", "+5.9 %"],
              "style": "indent", "min_pages": 2},
             {"cells": ["Ingredients and packaging", "(215,700)",
                        "(196,100)", "+10.0 %"], "style": "indent",
              "max_pages": 1},
             {"cells": ["Bakery wages", "(118,500)", "(109,200)",
                        "+8.5 %"], "style": "indent"},
             {"cells": ["Gross profit", "301,400", "270,400", "+11.5 %"],
              "style": "subtotal"},
             {"cells": ["Gross margin", "47.4 %", "47.0 %", "+0.4 pts"],
              "style": "muted"},
             {"cells": ["Operating costs", "", "", ""], "style": "section"},
             {"cells": ["Shop wages", "(112,600)", "(104,900)", "+7.3 %"],
              "style": "indent"},
             {"cells": ["Rent and service charges", "(54,000)",
                        "(52,800)", "+2.3 %"], "style": "indent"},
             {"cells": ["Energy (ovens and shops)", "(31,900)",
                        "(38,600)", "−17.4 %"], "style": "indent"},
             {"cells": ["Delivery van and fuel", "(12,400)", "(10,100)",
                        "+22.8 %"], "style": "indent", "min_pages": 2},
             {"cells": ["Card fees and bank charges", "(8,300)",
                        "(7,600)", "+9.2 %"], "style": "indent",
              "min_pages": 2},
             {"cells": ["Marketing", "(6,100)", "(5,400)", "+13.0 %"],
              "style": "indent", "min_pages": 2},
             {"cells": ["Repairs and maintenance", "(9,700)", "(11,200)",
                        "−13.4 %"], "style": "indent", "min_pages": 2},
             {"cells": ["Accountancy, insurance, other", "(10,800)",
                        "(10,300)", "+4.9 %"], "style": "indent",
              "min_pages": 2},
             {"cells": ["Other operating costs", "(47,300)", "(44,600)",
                        "+6.1 %"], "style": "indent", "max_pages": 1},
             {"cells": ["EBITDA", "55,600", "29,500", "+88.5 %"],
              "style": "subtotal"},
             {"cells": ["Depreciation of ovens and fit-out", "(18,900)",
                        "(17,400)", "+8.6 %"], "style": "indent"},
             {"cells": ["Interest on the oven loan", "(3,100)", "(3,600)",
                        "−13.9 %"], "style": "indent"},
             {"cells": ["Profit before tax", "33,600", "8,500",
                        "+295 %"], "style": "subtotal"},
             {"cells": ["Corporation tax", "(6,400)", "(1,600)", ""],
              "style": "indent"},
             {"cells": ["Profit for the year", "27,200", "6,900",
                        "+294 %"], "style": "total"},
         ]},
        {"kind": "callout", "weight": 0.15, "tone": "good",
         "label": "In short:",
         "text": "revenue up 10 %, a margin that held despite flour "
                 "prices, and energy down by a sixth after the new "
                 "ovens: profit almost four times last year's."},
        {"heading": "Where each euro went", "kind": "figure",
         "weight": 0.2, "min_pages": 2, "height": {2: 190, 4: 210},
         "charts": [{"type": "sankey", "format": "€{:,.0f}k",
          "nodes": [
              {"id": "shops", "label": "Shops", "col": 0, "color": 0},
              {"id": "whole", "label": "Wholesale", "col": 0, "color": 1},
              {"id": "school", "label": "Bread school", "col": 0,
               "color": 2},
              {"id": "rev", "label": "Revenue", "col": 1, "color": 0},
              {"id": "ing", "label": "Ingredients", "col": 2,
               "color": 3},
              {"id": "wages", "label": "Wages", "col": 2, "color": 1},
              {"id": "prem", "label": "Rent and energy", "col": 2,
               "color": 4},
              {"id": "other", "label": "Other costs", "col": 2,
               "color": 4},
              {"id": "profit", "label": "Profit", "col": 2,
               "color": "good"}],
          "links": [("shops", "rev", 412), ("whole", "rev", 199),
                    ("school", "rev", 25), ("rev", "ing", 216),
                    ("rev", "wages", 231), ("rev", "prem", 86),
                    ("rev", "other", 75), ("rev", "profit", 28)]}]},
        {"heading": "Margins", "kind": "figure", "weight": 0.3,
         "min_pages": 2, "charts": [{"type": "kpis", "tiles": [
             {"label": "Gross margin", "value": "47.4 %", "delta": "+0.4",
              "status": 0, "note": "after bakery wages"},
             {"label": "EBITDA margin", "value": "8.7 %", "delta": "+3.5",
              "status": 1, "note": "€55.6k"},
             {"label": "Net margin", "value": "4.3 %", "delta": "+3.1",
              "status": "good", "note": "€27.2k"},
             {"label": "Wages / revenue", "value": "36.4 %",
              "delta": "−0.6", "delta_status": "good", "status": 2,
              "note": "target under 38 %"},
         ]}]},
        {"heading": "Month by month", "kind": "figure", "weight": 0.5,
         "min_pages": 4, "height": 180, "charts": [{"type": "bars",
          "stacked": True, "title": "Revenue by stream", "subtitle":
          "€k", "categories": MONTHS, "values": False,
          "series": [{"name": "Shops", "values": [32, 33, 34, 37, 38, 33,
                                                  33, 34, 41, 31, 30,
                                                  36.3]},
                     {"name": "Wholesale", "values": [15, 16, 16, 17, 17,
                                                      16, 16, 17, 20, 15,
                                                      15, 18.7]},
                     {"name": "Bread school", "values": [1.5, 2, 2, 1.5,
                                                         1.5, 2, 2.5, 3,
                                                         3.5, 1.5, 2,
                                                         2.1]}]}]},
        {"heading": "Monthly profit", "kind": "figure", "weight": 0.55,
         "min_pages": 4, "height": 150, "charts": [{"type": "line",
          "subtitle": "€k, EBITDA", "x": MONTHS, "format": "{:.1f}",
          "series": [{"name": "2026/27", "area": True,
                      "values": [4.1, 4.6, 4.9, 5.8, 6.2, 3.9, 4.0, 4.4,
                                 7.6, 2.1, 2.5, 5.5]},
                     {"name": "2025/26", "dash": True, "color": 4,
                      "values": [2.0, 2.4, 2.6, 3.4, 3.8, 1.6, 2.2, 2.3,
                                 5.1, 0.4, 0.6, 3.3]}]}]},
        {"heading": "Notes", "kind": "entries", "weight": 0.6,
         "step": 0.15, "inner": 0.05, "min_pages": 2, "entries": [
             {"title": "1. Revenue", "text": [
                 "Revenue is recognised when bread is sold in the shops "
                 "or delivered to wholesale customers. Bread school "
                 "courses are recognised on the day of the course; "
                 "€2,400 paid in advance for April courses is held as "
                 "deferred income."]},
             {"title": "2. Cost of sales", "text": [
                 "Flour rose 17 % because wholesale volumes grew and "
                 "the organic rye price rose by 9 % in the autumn. "
                 "Butter and dairy were steadier after the new contract "
                 "with Ashby Creamery."]},
             {"title": "3. Energy", "text": [
                 "Two electric deck ovens replaced the old gas oven in "
                 "May 2026 and are heated overnight on the cheaper "
                 "tariff. Energy fell by €6,700 despite longer hours."]},
             {"title": "4. Tax", "text": [
                 "Corporation tax at 19 % after capital allowances on "
                 "the new ovens; payable by 1 January 2028."]},
         ]},
        {"heading": "Costs as a share of revenue", "kind": "figure",
         "weight": 0.7, "min_pages": 4, "height": 160, "charts": [{
             "type": "bars", "horizontal": True, "format": "{:.1f} %",
             "categories": ["Ingredients and packaging", "Bakery wages",
                            "Shop wages", "Rent", "Energy",
                            "Other costs"],
             "series": [{"name": "2025/26", "color": 4,
                         "values": [34.1, 19.0, 18.2, 9.2, 6.7, 7.7]},
                        {"name": "2026/27", "values": [33.9, 18.6, 17.7,
                                                       8.5, 5.0, 7.4]}]}]},
        {"heading": "Basis of preparation", "kind": "text",
         "weight": 0.8, "step": 0.3, "min_pages": 4, "paragraphs": [
             "These management accounts are prepared from the bakery's "
             "ledger on the accruals basis and have not been audited. "
             "Stock of flour and packaging was counted on 31 March 2027 "
             "and valued at the lower of cost and net realisable value.",
             "Figures in brackets are costs or negative amounts; changes "
             "are against the year to 31 March 2026.",
         ]},
        {"heading": "Approved", "kind": "table", "look": "plain",
         "header": False, "whole": True, "weight": 0.9, "min_pages": 4,
         "columns": [("", 1), ("", 1)],
         "rows": [["**Ana Rye**, director", "**Tomás Crumb**, director"],
                  ["Signed ______________________",
                   "Signed ______________________"],
                  ["Date 14 May 2027", "Date 14 May 2027"]]},
    ],
}
