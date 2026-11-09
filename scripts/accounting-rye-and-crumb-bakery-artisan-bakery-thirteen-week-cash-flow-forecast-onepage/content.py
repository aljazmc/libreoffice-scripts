"""13-Week Cash Flow Forecast of Rye & Crumb Bakery: the business and
everything the document could say. The typesetting keeps what fits into one
page, the most important first."""

BUSINESS = {
    "name": "Rye & Crumb Bakery",
    "author": "Marta Ilić, bookkeeper",
}

W = ["W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9", "W10", "W11",
     "W12", "W13"]
COLS = [("€", 2.2)] + [(w, 0.62, "end") for w in W] + [("Total", 0.8,
                                                         "end")]

DOCUMENT = {
    "title": "13-Week Cash Flow Forecast",
    "subtitle": "Week starting 3 November 2027 to week starting 26 January "
                "2028 · prepared before the Harbour Road refit",
    "meta": [("Opening cash", "€38,400"), ("Lowest point", "€1,400 · W10"),
             ("Closing cash", "€11,500"), ("Overdraft limit", "€15,000"),
             ("Version", "v3 · 31 Oct")],
    "sections": [
        {"kind": "figure", "weight": 0.15, "max_pages": 1, "charts": [{
            "type": "kpis", "tiles": [
                {"label": "Opening cash", "value": "€38.4k", "status": 0,
                 "note": "3 November"},
                {"label": "Lowest point", "value": "€1.4k",
                 "status": "warn", "note": "week 10, after the refit"},
                {"label": "Closing cash", "value": "€11.5k", "status": 1,
                 "note": "26 January"},
                {"label": "Overdraft unused", "value": "€15.0k",
                 "status": "good", "note": "headroom at the low point "
                 "€16.4k"}]}]},
        {"heading": "Cash balance", "kind": "figure", "weight": 0.3,
         "min_pages": 2, "height": {2: 150, 4: 175},
         "charts": [
             {"type": "line", "x": W, "format": "{:.1f}",
              "subtitle": "€k at the end of each week",
              "target": 0, "target_label": "zero",
              "band": (-15, 0, "overdraft available"),
              "zero": False, "marks": [(7, "refit pays out")],
              "series": [{"name": "Base case", "area": True,
                          "values": [36.1, 33.8, 38.2, 35.0, 31.4, 30.6,
                                     37.7, 13.9, 2.1, 1.4, 4.6, 7.9,
                                     11.5]},
                         {"name": "Wet December", "dash": True,
                          "color": "bad",
                          "values": [36.1, 33.8, 38.2, 35.0, 29.2, 25.9,
                                     30.0, 4.6, -7.2, -7.9, -4.7, -1.4,
                                     2.2]}]}]},
        {"heading": "Forecast", "kind": "table", "whole": True,
         "weight": 0.1, "columns": COLS,
         "rows": [
             {"cells": ["Opening balance", "38.4", "36.1", "33.8", "38.2",
                        "35.0", "31.4", "30.6", "37.7", "13.9", "2.1", "1.4",
                        "4.6", "7.9", "38.4"],
              "style": "highlight"},
             {"cells": ["Receipts"] + [""] * 14, "style": "section",
              "min_pages": 2},
             {"cells": ["Shop takings", "9.6", "9.8", "10.1", "10.4", "11.2",
                        "12.6", "14.9", "8.1", "8.0", "8.3", "8.5", "8.6",
                        "8.9", "129.0"],
              "style": "indent", "min_pages": 2},
             {"cells": ["Wholesale receipts", "4.1", "3.9", "4.4", "3.8",
                        "4.2", "4.6", "4.3", "5.1", "3.6", "3.9", "4.0", "4.1",
                        "4.2", "54.2"],
              "style": "indent", "min_pages": 2},
             {"cells": ["Bread school", "0.6", "0.8", "1.1", "0.9", "1.2",
                        "1.4", "0.4", "0.0", "0.3", "0.6", "0.7", "0.8", "0.9",
                        "9.7"],
              "style": "indent", "min_pages": 2},
             {"cells": ["Total receipts", "14.3", "14.5", "15.6", "15.1",
                        "16.6", "18.6", "19.6", "13.2", "11.9", "12.8", "13.2",
                        "13.5", "14.0", "192.9"],
              "style": "subtotal"},
             {"cells": ["Payments"] + [""] * 14, "style": "section",
              "min_pages": 2},
             {"cells": ["Ingredients and packaging", "(4.8)", "(4.9)", "(5.1)",
                        "(5.0)", "(5.6)", "(6.2)", "(6.9)", "(3.8)", "(4.0)",
                        "(4.1)", "(4.2)", "(4.3)", "(4.4)", "(63.3)"],
              "style": "indent", "min_pages": 2},
             {"cells": ["Wages", "(4.6)", "(9.1)", "(4.6)", "(9.3)", "(4.8)",
                        "(9.6)", "(5.0)", "(9.8)", "(4.6)", "(4.6)", "(4.6)",
                        "(4.6)", "(4.6)", "(79.8)"],
              "style": "indent", "min_pages": 2},
             {"cells": ["Rent and service charges", "(4.5)", "", "", "",
                        "(4.5)", "", "", "", "(4.5)", "", "", "", "",
                        "(13.5)"],
              "style": "indent", "min_pages": 2},
             {"cells": ["Energy", "", "(2.6)", "", "", "", "(2.8)", "", "", "",
                        "(3.0)", "", "", "", "(8.4)"],
              "style": "indent", "min_pages": 2},
             {"cells": ["VAT quarter", "", "", "", "(3.6)", "", "", "", "", "",
                        "", "", "", "", "(3.6)"],
              "style": "indent", "min_pages": 2},
             {"cells": ["Oven loan", "(0.7)", "", "", "", "(0.7)", "", "", "",
                        "(0.7)", "", "", "", "(0.7)", "(2.8)"],
              "style": "indent", "min_pages": 2},
             {"cells": ["Harbour Road refit", "", "", "", "", "", "", "",
                        "(22.9)", "(9.5)", "", "", "", "", "(32.4)"],
              "style": "indent", "min_pages": 2},
             {"cells": ["Other costs", "(2.0)", "(0.2)", "(1.5)", "(0.4)",
                        "(4.6)", "(0.8)", "(0.6)", "(0.5)", "(0.4)", "(1.8)",
                        "(1.2)", "(1.3)", "(0.7)", "(16.0)"],
              "style": "indent", "min_pages": 2},
             {"cells": ["Total payments", "(16.6)", "(16.8)", "(11.2)",
                        "(18.3)", "(20.2)", "(19.4)", "(12.5)", "(37.0)",
                        "(23.7)", "(13.5)", "(10.0)", "(10.2)", "(10.4)",
                        "(219.8)"],
              "style": "subtotal"},
             {"cells": ["Net cash flow", "(2.3)", "(2.3)", "4.4", "(3.2)",
                        "(3.6)", "(0.8)", "7.1", "(23.8)", "(11.8)", "(0.7)",
                        "3.2", "3.3", "3.6", "(26.9)"],
              "style": "indent"},
             {"cells": ["Closing balance", "36.1", "33.8", "38.2", "35.0",
                        "31.4", "30.6", "37.7", "13.9", "2.1", "1.4", "4.6",
                        "7.9", "11.5", "11.5"],
              "style": "total"},
         ]},
        {"kind": "callout", "weight": 0.25, "tone": "warn",
         "label": "Watch weeks 9 and 10:",
         "text": "the refit's stage payments land in the quietest weeks "
                 "of the year and the balance falls to €1,400. Agree with "
                 "the shopfitter to move the second payment to week 13, "
                 "or keep the overdraft ready."},
        {"heading": "Receipts and payments", "kind": "figure",
         "weight": 0.4, "min_pages": 2, "height": 150, "charts": [{
             "type": "bars", "categories": W, "values": False,
             "subtitle": "€k per week", "format": "{:.0f}",
             "series": [{"name": "Receipts", "color": "good",
                         "values": [14.3, 14.5, 15.6, 15.1, 16.6, 18.6,
                                    19.6, 13.2, 11.9, 12.8, 13.2, 13.5,
                                    14.0]},
                        {"name": "Payments", "color": "bad",
                         "values": [16.6, 16.8, 11.2, 18.3, 20.2, 19.2,
                                    11.9, 36.5, 23.3, 9.5, 8.6, 10.2,
                                    10.4]}]}]},
        {"heading": "Assumptions", "kind": "bullets", "weight": 0.5,
         "step": 0.1, "min_pages": 2, "items": [
             "Shop takings follow last year's weekly pattern plus 6 %; "
             "the Harbour Road shop is closed in weeks 8 and 9 for the "
             "refit.",
             "Wholesale customers pay in 14 days on average; Harbour "
             "Café and the two delis pay monthly.",
             "Wages are paid fortnightly; the Christmas bonus is in "
             "week 8.",
             "No new borrowing; the €15,000 overdraft is unused today.",
         ]},
        {"heading": "Scenarios", "kind": "table", "weight": 0.6,
         "whole": True, "min_pages": 4,
         "badges": {"Safe": "good", "Tight": "warn", "Overdrawn": "bad"},
         "columns": [("Scenario", 3), ("Lowest balance", 1.2, "end"),
                     ("Week", 0.7, "center"), ("Closing", 1, "end"),
                     ("", 1, "center")],
         "rows": [
             ["Base case", "€1,400", "W10", "€11,500", "Tight"],
             ["Wet December: shop sales −20 % in weeks 5 – 8", "−€7,900",
              "W10", "€2,200", "Overdrawn"],
             ["Second refit payment moved to week 13", "€10,900", "W10",
              "€11,500", "Safe"],
             ["Wholesale pays 10 days later", "−€2,400", "W10", "€7,700",
              "Overdrawn"],
             ["Refit overruns by 15 %", "−€3,500", "W10", "€6,600",
              "Overdrawn"],
         ]},
        {"heading": "Actions", "kind": "entries", "weight": 0.7,
         "step": 0.15, "inner": 0.05, "min_pages": 4, "entries": [
             {"title": "Split the refit payment", "dates": "Ana, by "
              "10 Nov", "text": [
                  "The shopfitter has agreed in principle to 60 % on "
                  "completion and 40 % two weeks later."]},
             {"title": "Christmas pre-orders with deposit",
              "dates": "Tomás, from W4", "text": [
                  "Stollen, panettone and party platters ordered online "
                  "with 50 % deposit bring about €3,500 forward into "
                  "weeks 5 to 7."]},
             {"title": "Chase monthly wholesale accounts",
              "dates": "Marta, weekly", "text": [
                  "Statements every Monday; two accounts over 30 days "
                  "today."]},
         ]},
        {"heading": "Where the cash goes", "kind": "figure",
         "weight": 0.8, "min_pages": 4, "height": 150, "widths": [2, 3],
         "charts": [
             {"type": "donut", "title": "13 weeks of payments",
              "format": "€{:.1f}k", "center": ("€219.8k", "out"),
              "segments": [("Wages", 79.8), ("Ingredients", 63.3),
                           ("Refit", 32.4), ("Rent", 13.5),
                           ("Other", 30.8)]},
             {"type": "progress", "title": "Overdraft headroom at the "
              "low point", "format": "€{:,.0f}", "max": 20000,
              "items": [{"label": "Base case", "value": 16400,
                         "status": "good"},
                        {"label": "Wet December", "value": 7100,
                         "status": "bad"},
                        {"label": "Late wholesale", "value": 12600,
                         "status": "warn"}]},
         ]},
    ],
}
