"""Burn and Runway of Lumen Analytics: the business and everything the document
could say. The typesetting keeps what fits into four pages, the most
important first."""

BUSINESS = {
    "name": "Lumen Analytics",
    "author": "Tomás Lind, CFO",
}

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
          "Oct", "Nov", "Dec"]

# 2027 plan, $k per month
REVENUE = [612, 638, 671, 702, 731, 768, 801, 838, 872, 910, 948, 990]
COSTS = [1238, 1262, 1301, 1344, 1380, 1428, 1459, 1494, 1528, 1556,
         1582, 1611]
BURN = [c - r for r, c in zip(REVENUE, COSTS)]
CASH = []
balance = 18970
for b in BURN:
    balance -= b
    CASH.append(balance)
RUNWAY = round(CASH[-1] / BURN[-1])

DOCUMENT = {
    "title": "Burn and Runway",
    "subtitle": "The 2027 plan: what we spend, what we earn and how long "
                "the Series A lasts",
    "meta": [("Cash, 1 Jan 2027", "$19.0m"),
             ("Net burn, Dec 2027", f"${BURN[-1]}k / month"),
             ("Cash, 31 Dec 2027", f"${CASH[-1] / 1000:.1f}m"),
             ("Runway after 2027", f"{RUNWAY} months"),
             ("For", "Board, 22 Jan 2027")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "charts": [{"type": "kpis",
         "tiles": [
             {"label": "Net burn, January", "value": f"${BURN[0]}k",
              "status": 0, "note": "a month", "spark": BURN},
             {"label": "Revenue growth", "value": "+62 %", "status": 1,
              "note": "December on January"},
             {"label": "Runway", "value": f"{RUNWAY + 12} mo",
              "status": "good", "note": "from 1 January"},
             {"label": "Default alive?", "value": "Yes", "status": "good",
              "note": "break-even in Q3 2028"},
         ]}]},
        {"heading": "Revenue, costs and burn", "kind": "figure",
         "weight": 0.2, "height": {1: 170, 2: 185, 4: 195},
         "charts": [{"type": "line", "subtitle": "$k per month, 2027",
          "x": MONTHS, "format": "{:,.0f}", "end_labels": True,
          "series": [{"name": "Costs", "color": 3, "values": COSTS},
                     {"name": "Revenue", "color": 0, "area": True,
                      "values": REVENUE},
                     {"name": "Net burn", "color": 1, "dash": True,
                      "values": BURN}]}]},
        {"heading": "Monthly plan", "kind": "table", "whole": True,
         "weight": 0.3, "columns": [("$k", 1.25)]
         + [(m, 0.62, "end") for m in MONTHS],
         "rows": [["Revenue"] + [f"{v:,}" for v in REVENUE],
                  ["Costs"] + [f"{v:,}" for v in COSTS],
                  {"cells": ["Net burn"] + [f"{v:,}" for v in BURN],
                   "style": "subtotal"},
                  {"cells": ["Cash, end"]
                   + [f"{v / 1000:.1f}m" for v in CASH],
                   "style": "total"}]},
        {"heading": "Where the money goes", "kind": "figure",
         "weight": 0.4, "min_pages": 2, "height": 165, "widths": [2, 3],
         "charts": [
             {"type": "donut", "title": "Costs by team, 2027",
              "format": "${:,.1f}m", "center": ("$17.1m", "costs"),
              "segments": [("Engineering", 6.9), ("Sales", 3.8),
                           ("Marketing", 1.9), ("Customer success", 1.6),
                           ("Cloud hosting", 1.5), ("G&A", 1.4)]},
             {"type": "bars", "title": "Headcount", "stacked": True,
              "categories": ["Dec 25", "Jun 26", "Dec 26", "Jun 27",
                             "Dec 27"],
              "series": [{"name": "Engineering", "values": [18, 22, 26,
                                                            31, 34]},
                         {"name": "Go-to-market", "values": [9, 13, 17,
                                                             22, 25]},
                         {"name": "G&A", "color": 4,
                          "values": [4, 5, 6, 7, 7]}]},
         ]},
        {"heading": "Runway scenarios", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": 160, "charts": [{"type": "line",
          "title": "Cash", "subtitle": "$m", "format": "{:.0f}",
          "x": ["Jan 27", "Jul 27", "Jan 28", "Jul 28", "Jan 29",
                "Jul 29", "Jan 30"], "target": 3,
          "target_label": "raise by here",
          "series": [{"name": "Plan", "values": [19.0, 15.0, 11.3, 9.4,
                                                 9.0, 9.4, 10.3]},
                     {"name": "Growth 20 % slower", "color": 3,
                      "dash": True, "values": [19.0, 14.6, 10.2, 6.9,
                                               4.5, 2.6, 1.0]},
                     {"name": "Hiring freeze from July", "color": 2,
                      "dash": True, "values": [19.0, 15.0, 12.6, 11.9,
                                               12.3, 13.4, 15.0]}]}]},
        {"heading": "Levers", "kind": "table", "weight": 0.6,
         "whole": True, "min_pages": 2,
         "badges": {"Ready": "good", "Prepared": "warn"},
         "columns": [("Lever", 2.8), ("Monthly saving", 1.1, "end"),
                     ("Runway added", 1, "end"), ("State", 0.9,
                                                  "center")],
         "rows": [["Pause the 8 open sales roles", "$128k", "+7 months",
                   "Ready"],
                  ["Move to committed cloud spend", "$31k", "+2 months",
                   "Ready"],
                  ["Cut paid marketing by half", "$58k", "+3 months",
                   "Prepared"],
                  ["Annual billing for all new customers", "$70k*",
                   "+4 months", "Prepared"]]},
        {"heading": "Efficiency", "kind": "figure", "weight": 0.8,
         "min_pages": 4, "charts": [{"type": "gauges", "items": [
             {"label": "Burn multiple", "value": 1.3, "max": 3,
              "target": 1.5, "status": "good", "display": "1.3×",
              "note": "under 1.5 is good"},
             {"label": "Gross margin", "value": 78, "max": 100,
              "target": 75, "status": 0, "display": "78 %"},
             {"label": "CAC payback", "value": 17, "max": 36,
              "target": 18, "status": "warn", "display": "17 mo"},
             {"label": "Net revenue retention", "value": 118, "min": 80,
              "max": 140, "target": 110, "status": "good",
              "display": "118 %"}]}]},
        {"heading": "Board decisions", "kind": "entries", "weight": 0.9,
         "step": 0.2, "inner": 0.1, "min_pages": 4, "entries": [
             {"title": "Approve the 2027 plan", "text": [
                 "A net burn of about $650k a month falling to $620k, "
                 "with 17 hires, and cash of about $11.3m at the end of "
                 "the year."]},
             {"title": "Trigger for the levers", "text": [
                 "If new ARR is more than 20 % behind plan for two "
                 "quarters running, the sales hiring pause starts "
                 "automatically."]},
             {"title": "Series B timing", "text": [
                 "Start conversations in Q1 2028 with 18 months of cash "
                 "left, not 12."]},
         ]},
        {"heading": "Definitions", "kind": "tags", "weight": 1.0,
         "step": 0.1, "min_pages": 4, "items": [
             ("Net burn", "cash costs minus cash revenue in a month"),
             ("Runway", "cash ÷ the latest month's net burn"),
             ("Burn multiple", "net burn ÷ net new ARR in the period"),
             ("Default alive", "reaches profitability on today's cash if "
                               "growth and costs follow the plan"),
         ]},
        {"kind": "text", "weight": 1.1, "step": 0.2, "min_pages": 4,
         "paragraphs": ["* Annual billing brings cash forward rather than "
                        "saving it; the runway effect is shown at a 60 % "
                        "take-up by new customers."]},
        {"heading": "Hiring plan", "kind": "table", "whole": True,
         "weight": 1.2, "min_pages": 4,
         "columns": [("Role", 2.4), ("Team", 1.3), ("Start", 0.8),
                     ("Annual cost", 1, "end"), ("Why", 2.4)],
         "rows": [["Senior ML engineers × 3", "Engineering", "Q1",
                   "$690k", "Forecast engine at 1m series"],
                  ["Platform engineers × 2", "Engineering", "Q2",
                   "$420k", "EU data residency, SOC 2"],
                  ["Account executives × 4", "Sales", "Q1 – Q3", "$760k",
                   "Retail and grocery in the UK"],
                  ["Solutions engineers × 2", "Sales", "Q2", "$380k",
                   "Onboarding time from 16 to 10 weeks"],
                  ["Customer success managers × 3", "Customer success",
                   "Q2 – Q4", "$390k", "Net retention above 115 %"],
                  ["Product marketing × 1", "Marketing", "Q1", "$170k",
                   "Launch of the replenishment module"],
                  ["Financial controller × 1", "G&A", "Q3", "$180k",
                   "Audit readiness for the Series B"],
                  {"cells": ["17 hires", "", "", "$2,990k", ""],
                   "style": "total"}]},
        {"heading": "Burn by team", "kind": "figure", "weight": 1.3,
         "min_pages": 4, "height": 165, "charts": [{"type": "bars",
          "stacked": True, "subtitle": "$k per month, costs by team",
          "format": "{:,.0f}", "values": False, "categories": MONTHS,
          "series": [{"name": "Engineering",
                      "values": [520, 530, 545, 560, 575, 590, 600, 612,
                                 625, 635, 645, 655]},
                     {"name": "Sales and marketing", "color": 1,
                      "values": [430, 440, 455, 470, 480, 500, 510, 520,
                                 530, 535, 540, 545]},
                     {"name": "Customer success", "color": 2,
                      "values": [120, 122, 126, 132, 136, 140, 144, 148,
                                 152, 156, 160, 165]},
                     {"name": "Cloud and G&A", "color": 4,
                      "values": [168, 170, 175, 182, 189, 198, 205, 214,
                                 221, 230, 237, 246]}]}]},
    ],
}
