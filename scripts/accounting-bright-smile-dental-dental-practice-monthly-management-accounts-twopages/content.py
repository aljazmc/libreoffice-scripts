"""Management Accounts of Bright Smile Dental: the business and everything the
document could say. The typesetting keeps what fits into two pages, the most
important first."""

BUSINESS = {
    "name": "Bright Smile Dental",
    "author": "Bright Smile Dental Ltd, practice manager Hannah Price",
}


def k(value):
    return f"({-value:,.1f})" if value < 0 else f"{value:,.1f}"


# £k: September actual, September budget, year to date actual, YTD budget
PL = [("Private treatment", 61.4, 58.0, 318.2, 302.0),
      ("Plan members (monthly fees)", 38.6, 38.0, 228.9, 226.0),
      ("NHS contract", 22.1, 22.1, 132.6, 132.6),
      ("Hygienist", 14.8, 13.5, 82.3, 79.0)]
COSTS = [("Associate dentists (50 % of fees)", -41.2, -39.5, -233.5,
          -226.0),
         ("Lab fees", -9.6, -8.8, -52.4, -50.0),
         ("Materials and consumables", -7.1, -6.9, -40.3, -39.0),
         ("Nurses and reception", -24.3, -24.0, -145.1, -144.0),
         ("Rent and rates", -8.5, -8.5, -51.0, -51.0),
         ("Equipment finance", -3.2, -3.2, -19.2, -19.2),
         ("Other overheads", -6.4, -6.0, -37.9, -36.0)]


def col(lines, i):
    return round(sum(line[i] for line in lines), 1)


INCOME = [col(PL, i) for i in range(1, 5)]
SPEND = [col(COSTS, i) for i in range(1, 5)]
PROFIT = [round(INCOME[i] + SPEND[i], 1) for i in range(4)]
COLUMNS = [("£ thousands", 2.8), ("Sep actual", 1, "end"),
           ("Sep budget", 1, "end"), ("YTD actual", 1, "end"),
           ("YTD budget", 1, "end")]

DOCUMENT = {
    "title": "Management Accounts",
    "subtitle": "September 2027 · month 6 of the financial year · two "
                "surgeries, five chairs",
    "meta": [("Practice", "Bright Smile Dental"), ("Month", "Sep 2027"),
             ("Income", f"£{INCOME[0]:.1f}k"),
             ("Profit", f"£{PROFIT[0]:.1f}k"),
             ("Against budget", f"+£{PROFIT[0] - PROFIT[1]:.1f}k")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "charts": [{"type": "kpis",
         "tiles": [
             {"label": "Income", "value": f"£{INCOME[0]:.1f}k",
              "delta": f"+{INCOME[0] / INCOME[1] - 1:.0%}", "status": 0,
              "note": "vs budget",
              "spark": [118, 124, 131, 129, 122, INCOME[0]]},
             {"label": "Profit", "value": f"£{PROFIT[0]:.1f}k",
              "delta": f"+£{PROFIT[0] - PROFIT[1]:.1f}k", "status": "good",
              "note": f"{PROFIT[0] / INCOME[0]:.0%} margin"},
             {"label": "Chair occupancy", "value": "86 %", "status": 1,
              "note": "target 85 %"},
             {"label": "Cash", "value": "£92.4k", "status": 2,
              "note": "end of September"}]}]},
        {"heading": "Profit and loss", "kind": "table", "whole": True,
         "weight": 0.2, "columns": COLUMNS,
         "rows": [{"cells": ["Income", "", "", "", ""], "style": "section"}]
         + [{"cells": [n] + [k(v) for v in vals], "style": "indent"}
            for n, *vals in PL]
         + [{"cells": ["Total income"] + [k(v) for v in INCOME],
             "style": "subtotal"},
            {"cells": ["Costs", "", "", "", ""], "style": "section"}]
         + [{"cells": [n] + [k(v) for v in vals], "style": "indent"}
            for n, *vals in COSTS]
         + [{"cells": ["Total costs"] + [k(v) for v in SPEND],
             "style": "subtotal"},
            {"cells": ["Profit"] + [k(v) for v in PROFIT],
             "style": "total"}]},
        {"heading": "Commentary", "kind": "bullets", "weight": 0.3,
         "step": 0.1, "items": [
             "**Private treatment beat budget by £3.4k**, mostly two "
             "implant cases moved from August.",
             "**Lab fees ran ahead** with the implants; they follow "
             "income and are not a concern.",
             "**Hygienist sessions are full** on Tuesdays and Thursdays; "
             "a third day from November is in the plan.",
         ]},
        {"heading": "Six months", "kind": "figure", "weight": 0.4,
         "min_pages": 2, "height": 160, "widths": [3, 2], "charts": [
             {"type": "bars", "stacked": True, "title": "Income by type",
              "subtitle": "£k", "format": "{:,.0f}",
              "categories": ["Apr", "May", "Jun", "Jul", "Aug", "Sep"],
              "series": [{"name": "Private", "values": [51, 54, 56, 50,
                                                        45.8, 61.4]},
                         {"name": "Plans", "values": [37.5, 37.8, 38.0,
                                                      38.4, 38.6, 38.6]},
                         {"name": "NHS", "values": [22.1] * 6},
                         {"name": "Hygienist", "values": [12.9, 13.6,
                                                          14.0, 13.2,
                                                          13.8, 14.8]}]},
             {"type": "donut", "title": "Where income goes",
              "segments": [("Associates", 41.2), ("Staff", 24.3),
                           ("Lab and materials", 16.7),
                           ("Premises and finance", 11.7),
                           ("Other", 6.4), ("Profit", PROFIT[0], "good")],
              "format": "£{:.1f}k", "center": (f"£{INCOME[0]:.0f}k",
                                               "income")},
         ]},
        {"heading": "Balance sheet", "kind": "table", "whole": True,
         "weight": 0.5, "min_pages": 2,
         "columns": [("£ thousands", 3), ("30 Sep", 1, "end"),
                     ("31 Aug", 1, "end")],
         "rows": [{"cells": ["Equipment and fit-out", "184.6", "187.1"],
                   "style": "indent"},
                  {"cells": ["Debtors (patients and NHS)", "38.2", "41.5"],
                   "style": "indent"},
                  {"cells": ["Stock of materials", "12.4", "11.9"],
                   "style": "indent"},
                  {"cells": ["Cash at bank", "92.4", "81.7"],
                   "style": "indent"},
                  {"cells": ["Creditors and accruals", "(46.8)", "(44.3)"],
                   "style": "indent"},
                  {"cells": ["Equipment finance", "(61.0)", "(63.6)"],
                   "style": "indent"},
                  {"cells": ["Net assets", "219.8", "214.3"],
                   "style": "total"}]},
        {"heading": "Dentists", "kind": "table", "weight": 0.6,
         "whole": True, "min_pages": 4,
         "badges": {"Above": "good", "On": "neutral", "Below": "warn"},
         "columns": [("Dentist", 1.8), ("Sessions", 0.8, "end"),
                     ("Gross fees", 1, "end"), ("Per session", 1, "end"),
                     ("Target", 0.9, "center")],
         "rows": [["Dr Amina Yusuf (principal)", "18", "£24,100", "£1,339",
                   "Above"],
                  ["Dr Tom Hale", "16", "£19,800", "£1,238", "On"],
                  ["Dr Priya Nair", "14", "£15,600", "£1,114", "On"],
                  ["Dr Josef Novak", "12", "£11,800", "£983", "Below"],
                  ["Dr Lena Fischer (implants)", "6", "£12,700",
                   "£2,117", "Above"]]},
        {"heading": "Chairs", "kind": "figure", "weight": 0.7,
         "min_pages": 4, "height": 150, "charts": [{"type": "heatmap",
          "title": "Chair occupancy", "subtitle": "% of booked minutes",
          "rows": ["Surgery 1", "Surgery 2", "Surgery 3", "Surgery 4",
                   "Hygienist room"],
          "cols": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
          "values": [[92, 95, 91, 94, 88, 71], [90, 93, 89, 92, 84, 0],
                     [84, 88, 82, 90, 79, 68], [78, 85, 74, 86, 72, 0],
                     [70, 98, 64, 97, 61, 0]],
          "thresholds": [(0, "bad"), (75, "warn"), (85, "good")],
          "format": "{:.0f}", "labels": 0.2}]},
        {"heading": "Cash", "kind": "figure", "weight": 0.8,
         "min_pages": 4, "height": 140, "charts": [{"type": "line",
          "subtitle": "£k at month end", "x": ["Apr", "May", "Jun", "Jul",
                                               "Aug", "Sep"],
          "format": "{:.0f}", "end_labels": True,
          "series": [{"name": "Cash", "area": True,
                      "values": [58.2, 64.9, 72.4, 77.0, 81.7, 92.4]}]}]},
        {"heading": "Actions", "kind": "entries", "weight": 0.9,
         "step": 0.2, "inner": 0.1, "min_pages": 4, "entries": [
             {"title": "Third hygienist day from November", "text": [
                 "Adds about £4.5k of income a month for £2.1k of cost."]},
             {"title": "Dr Novak's diary", "text": [
                 "Cancellations at 14 %; reminders by text 48 and 24 "
                 "hours before from October."]},
             {"title": "Plan price review", "text": [
                 "Plan fees rise by £1 a month in January, the first "
                 "change in two years."]},
         ]},
        {"heading": "Key numbers", "kind": "table", "whole": True,
         "weight": 0.95, "min_pages": 4,
         "badges": {"Better": "good", "Worse": "bad", "Same": "neutral"},
         "columns": [("Measure", 2.6), ("September", 1, "end"),
                     ("August", 1, "end"), ("Target", 1, "end"),
                     ("", 0.9, "center")],
         "rows": [["New patients", "64", "51", "55", "Better"],
                  ["Plan members", "1,412", "1,398", "1,450", "Better"],
                  ["Failed appointments", "4.1 %", "5.3 %", "4.0 %",
                   "Better"],
                  ["Treatment plans accepted", "71 %", "74 %", "75 %",
                   "Worse"],
                  ["Average private fee", "£184", "£176", "£180",
                   "Better"],
                  ["Google rating", "4.8", "4.8", "4.7", "Same"]]},
        {"heading": "Year to date against budget", "kind": "figure",
         "weight": 1.0, "min_pages": 4, "height": 150, "charts": [{
             "type": "bars", "horizontal": True, "format": "£{:,.1f}k",
             "categories": [n for n, *_ in PL] + ["Profit"],
             "series": [{"name": "Budget", "color": 4,
                         "values": [v[4] for v in PL] + [PROFIT[3]]},
                        {"name": "Actual", "values": [v[3] for v in PL]
                         + [PROFIT[2]]}]}]},
    ],
}
