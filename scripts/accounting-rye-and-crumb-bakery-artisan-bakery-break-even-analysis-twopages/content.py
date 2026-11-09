"""Break-Even Analysis of Rye & Crumb Bakery: the business and everything the
document could say. The typesetting keeps what fits into two pages, the most
important first."""

BUSINESS = {
    "name": "Rye & Crumb Bakery",
    "author": "Ana Rye, director",
}

DOCUMENT = {
    "title": "Break-Even Analysis",
    "subtitle": "A third shop at the station: how much must it sell to pay "
                "its way?",
    "meta": [("Proposal", "Station kiosk"), ("Fixed costs", "€96,000 / yr"),
             ("Margin per €", "€0.41"), ("Break-even", "€640 a day"),
             ("Decision", "Board, 3 Dec")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "charts": [{"type": "kpis",
         "tiles": [
             {"label": "Break-even sales", "value": "€234k", "status": 0,
              "note": "a year, 365 days"},
             {"label": "Per day", "value": "€640", "status": 1,
              "note": "about 210 customers"},
             {"label": "Forecast", "value": "€780", "status": "good",
              "note": "a day, from footfall"},
             {"label": "Margin of safety", "value": "18 %",
              "status": "warn", "note": "of forecast sales"},
         ]}]},
        {"heading": "Cost, volume, profit", "kind": "figure",
         "weight": 0.2, "height": {1: 190, 2: 200, 4: 215},
         "charts": [{"type": "line", "title": "Yearly revenue and costs",
          "subtitle": "€k, by average daily sales",
          "x": ["€300", "€400", "€500", "€600", "€640", "€700", "€800",
                "€900", "€1,000"],
          "format": "{:.0f}", "marks": [(4, "break-even"),
                                        (5.8, "forecast")],
          "series": [
              {"name": "Revenue", "color": 0,
               "values": [110, 146, 183, 219, 234, 256, 292, 329, 365]},
              {"name": "Total costs", "color": "bad",
               "values": [161, 182, 204, 225, 234, 247, 268, 290, 311]},
              {"name": "Fixed costs", "color": 4, "dash": True,
               "values": [96, 96, 96, 96, 96, 96, 96, 96, 96]}]}]},
        {"heading": "Costs of the kiosk", "kind": "table", "whole": True,
         "weight": 0.3, "columns": [("", 3), ("Per year", 1, "end"),
                                    ("Per day", 1, "end"),
                                    ("Behaviour", 1.2, "center")],
         "badges": {"Fixed": "info", "Variable": "warn"},
         "rows": [
             {"cells": ["Fixed costs", "", "", ""], "style": "section"},
             {"cells": ["Rent and station levy", "€38,400", "€105",
                        "Fixed"], "style": "indent"},
             {"cells": ["Two staff, opening hours 06:00 – 14:00",
                        "€44,800", "€123", "Fixed"], "style": "indent"},
             {"cells": ["Energy, card terminal, insurance", "€6,300",
                        "€17", "Fixed"], "style": "indent"},
             {"cells": ["Depreciation of the fit-out over 5 years",
                        "€6,500", "€18", "Fixed"], "style": "indent"},
             {"cells": ["Total fixed costs", "€96,000", "€263", ""],
              "style": "subtotal"},
             {"cells": ["Variable costs per €1 of sales", "", "", ""],
              "style": "section"},
             {"cells": ["Bread and pastry at bakery cost", "€0.46", "",
                        "Variable"], "style": "indent"},
             {"cells": ["Coffee, milk and cups", "€0.08", "",
                        "Variable"], "style": "indent"},
             {"cells": ["Card fees and waste", "€0.05", "", "Variable"],
              "style": "indent"},
             {"cells": ["Contribution per €1 of sales", "€0.41", "", ""],
              "style": "total"},
         ]},
        {"kind": "callout", "weight": 0.35, "tone": "accent",
         "label": "Break-even",
         "text": "= fixed costs ÷ contribution margin = €96,000 ÷ 0.41 = "
                 "**€234,000 a year**, or €640 a day, seven days a week."},
        {"heading": "Sensitivity", "kind": "figure", "weight": 0.4,
         "min_pages": 2, "height": 165, "widths": [3, 2], "charts": [
             {"type": "bars", "horizontal": True, "title": "Break-even "
              "per day if…", "format": "€{:.0f}", "target": 780,
              "target_label": "forecast",
              "categories": ["As planned", "Rent +15 %",
                             "One more staff member", "Flour +20 %",
                             "Coffee share doubles",
                             "Open Saturdays only to 12:00"],
              "series": [{"name": "Break-even",
                          "values": [640, 680, 725, 702, 598, 655],
                          "colors": [0, "warn", "bad", "warn", "good",
                                     "warn"]}]},
             {"type": "gauges", "items": [
                 {"label": "Margin of safety", "value": 18, "max": 50,
                  "target": 25, "status": "warn", "display": "18 %",
                  "note": "aim for 25 %"}]},
         ]},
        {"heading": "Sales mix", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": 150, "widths": [2, 3], "charts": [
             {"type": "donut", "title": "Forecast sales",
              "segments": [("Coffee", 34), ("Pastries", 29),
                           ("Sandwiches", 22), ("Loaves", 15)],
              "format": "{:.0f}%", "center": ("€780", "a day")},
             {"type": "bars", "title": "Contribution per €1 by product",
              "format": "€{:.2f}", "axis_format": "{:.1f}",
              "categories": ["Coffee", "Pastries", "Sandwiches",
                             "Loaves"],
              "series": [{"name": "Contribution",
                          "values": [0.68, 0.42, 0.24, 0.18],
                          "colors": ["good", 0, "warn", "bad"]}]},
         ]},
        {"heading": "Footfall", "kind": "text", "weight": 0.6, "step": 0.3,
         "min_pages": 2, "paragraphs": [
             "The station counts 14,200 passengers on a weekday and "
             "6,100 on a Sunday. The two cafés already in the hall serve "
             "about 4 % of them. At an average spend of €3.70, the "
             "forecast of €780 a day needs 1.5 % of the weekday "
             "passengers, which is what our Harbour Road shop achieved "
             "in its first year from the ferry crowd.",
         ]},
        {"heading": "Scenarios", "kind": "table", "weight": 0.7,
         "whole": True, "min_pages": 4,
         "badges": {"Profit": "good", "Loss": "bad", "Break-even": "warn"},
         "columns": [("Scenario", 2.6), ("Sales per day", 1, "end"),
                     ("Profit per year", 1.1, "end"),
                     ("Payback", 0.9, "end"), ("", 1, "center")],
         "rows": [
             ["Pessimistic: 1.1 % of passengers", "€575", "−€9,900", "—",
              "Loss"],
             ["Break-even", "€640", "€0", "—", "Break-even"],
             ["Forecast: 1.5 %", "€780", "+€20,700", "1.2 years",
              "Profit"],
             ["Optimistic: 2 %", "€1,040", "+€59,600", "0.5 years",
              "Profit"],
         ]},
        {"heading": "Weekdays and weekends", "kind": "figure",
         "weight": 0.8, "min_pages": 4, "height": 150, "charts": [{
             "type": "bars", "title": "Forecast sales by day",
             "subtitle": "€", "format": "{:,.0f}", "target": 640,
             "target_label": "break-even",
             "categories": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat",
                            "Sun"],
             "series": [{"name": "Sales", "values": [890, 860, 870, 880,
                                                     910, 560, 490],
                         "colors": [0, 0, 0, 0, 0, "warn", "bad"]}]}]},
        {"heading": "Recommendation", "kind": "entries", "weight": 0.9,
         "step": 0.2, "inner": 0.1, "min_pages": 4, "entries": [
             {"title": "Open the kiosk, weekdays first", "text": [
                 "Weekdays clear the break-even by a third. Open Monday "
                 "to Saturday for the first six months and add Sundays "
                 "only if Saturday sales pass €640."]},
             {"title": "Push coffee", "text": [
                 "Coffee earns 68 cents in the euro. A loyalty card and "
                 "a commuter bundle of coffee and a pastry lift the "
                 "contribution margin to about 0.44, which takes the "
                 "break-even down to €600 a day."]},
             {"title": "Review at month six", "text": [
                 "If the average is under €640 a day for three months "
                 "running, the lease allows us to leave with three "
                 "months' notice."]},
         ]},
        {"heading": "Method", "kind": "bullets", "weight": 1.0,
         "step": 0.1, "min_pages": 4, "items": [
             "Bread and pastry are charged to the kiosk at the bakery's "
             "full cost, not at the wholesale price.",
             "Fixed costs include the staff because two people are "
             "needed whatever the sales are.",
             "All amounts exclude VAT.",
         ]},
        {"heading": "Investment", "kind": "table", "whole": True,
         "weight": 1.1, "min_pages": 4,
         "columns": [("Item", 3), ("Cost", 1, "end"),
                     ("Life", 0.8, "center")],
         "rows": [
             ["Counter, shelving and signage", "€14,200", "5 years"],
             ["Bake-off oven and proving cabinet", "€9,800", "5 years"],
             ["Espresso machine and grinder", "€6,400", "5 years"],
             ["Tills, card terminal, small equipment", "€2,100",
              "3 years"],
             {"cells": ["Total fit-out", "€32,500", ""], "style": "total"},
         ]},
        {"heading": "Payback", "kind": "figure", "weight": 1.2,
         "min_pages": 4, "height": 150, "charts": [{"type": "line",
          "title": "Cumulative cash from the kiosk", "subtitle":
          "€k, forecast case", "x": ["0", "3", "6", "9", "12", "15", "18",
                                     "21", "24 months"],
          "format": "{:.0f}", "target": 0, "target_label": "paid back",
          "zero": False,
          "series": [{"name": "Forecast", "area": True,
                      "values": [-32.5, -27.0, -20.3, -13.5, -6.2, 0.6,
                                 7.4, 14.2, 21.0]},
                     {"name": "Pessimistic", "color": "bad",
                      "dash": True,
                      "values": [-32.5, -33.3, -34.1, -34.9, -35.7,
                                 -36.5, -37.3, -38.1, -38.9]}]}]},
    ],
}
