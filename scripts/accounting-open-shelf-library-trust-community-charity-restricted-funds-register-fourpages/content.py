"""Restricted Funds Register of Open Shelf Library Trust: the business and
everything the document could say. The typesetting keeps what fits into four
pages, the most important first."""

BUSINESS = {
    "name": "Open Shelf Library Trust",
    "author": "Raj Patel, treasurer",
}

# fund, funder, purpose, opening, income, spent, transfers, ends
FUNDS = [
    ("Reading Rooms", "Northfield Foundation",
     "Two new reading rooms and their staff", 18_400, 120_000, -81_400, 0,
     "Mar 2029"),
    ("Library service agreement", "Hull Town Council",
     "Opening hours at Northgate and Westfield", 0, 52_500, -52_500, 0,
     "Mar 2028"),
    ("Digital Skills", "Digital Skills Fund",
     "Laptops and classes for adults", 6_200, 24_000, -27_900, 0,
     "Dec 2027"),
    ("Children's library, Northgate", "Legacy of Mrs E. Marsh",
     "Books and furniture for under-12s", 0, 22_000, -8_600, 0,
     "none"),
    ("Reading room roof", "Heritage Grant and trustees",
     "Repairs to the Victorian roof", 41_800, 0, -53_800, 12_000,
     "Sep 2027"),
    ("Mobile library van", "Rotary Club appeal",
     "Replacement van", 18_200, 0, -3_300, 0, "Mar 2028"),
]


def k(value):
    return f"({-value:,})" if value < 0 else f"{value:,}" if value else "—"


ROWS = [(f, by, p, o, i, s, t, o + i + s + t, end)
        for f, by, p, o, i, s, t, end in FUNDS]
T = [sum(r[i] for r in ROWS) for i in (3, 4, 5, 6, 7)]

DOCUMENT = {
    "title": "Restricted Funds Register",
    "subtitle": "Money given for a purpose: what came in, what was spent "
                "and what is left · year to 31 March 2027",
    "meta": [("Funds", str(len(ROWS))), ("Received", f"£{T[1]:,}"),
             ("Spent", f"£{-T[2]:,}"), ("Balance", f"£{T[4]:,}"),
             ("Reviewed", "Finance committee")],
    "sections": [
        {"heading": "Register", "kind": "table", "whole": True,
         "weight": 0.1,
         "columns": [("Fund", 1.8), ("Funder", 1.7),
                     ("1 Apr 2026", 0.9, "end"), ("Income", 0.9, "end"),
                     ("Spent", 0.9, "end"), ("Transfers", 0.9, "end"),
                     ("31 Mar 2027", 0.9, "end")],
         "rows": [[f, by, k(o), k(i), k(s), k(t), k(c)]
                  for f, by, p, o, i, s, t, c, end in ROWS]
         + [{"cells": ["Total", "", k(T[0]), k(T[1]), k(T[2]), k(T[3]),
                       k(T[4])], "style": "total"}]},
        {"heading": "Spent against what came in", "kind": "figure",
         "weight": 0.2, "height": {1: 165, 2: 175, 4: 185}, "charts": [{
             "type": "progress", "format": "{:.0f} %", "items": [
                 {"label": f, "value": round(-s / (o + i + t) * 100),
                  "note": f"£{-s:,} of £{o + i + t:,} · {by}",
                  "status": "warn" if -s / (o + i + t) > 0.95 else 0}
                 for f, by, p, o, i, s, t, c, end in ROWS]}]},
        {"heading": "Purposes and deadlines", "kind": "table",
         "whole": True, "weight": 0.3, "min_pages": 2,
         "badges": {"Dec 2027": "warn", "Sep 2027": "warn"},
         "columns": [("Fund", 1.8), ("Purpose", 3), ("Spend by", 1,
                                                     "center")],
         "rows": [[f, p, end] for f, by, p, o, i, s, t, c, end in ROWS]},
        {"heading": "Balances left", "kind": "figure", "weight": 0.4,
         "min_pages": 2, "height": 150, "widths": [2, 3], "charts": [
             {"type": "donut", "title": "At 31 March 2027",
              "segments": [(r[0], r[7]) for r in ROWS if r[7] > 0],
              "format": "£{:,.0f}", "center": (f"£{T[4] / 1000:.1f}k",
                                               "restricted")},
             {"type": "bars", "title": "Restricted balance over time",
              "subtitle": "£k", "format": "{:,.0f}",
              "categories": ["Mar 23", "Mar 24", "Mar 25", "Mar 26",
                             "Mar 27"],
              "series": [{"name": "Balance", "values": [61, 72, 79,
                                                        T[0] / 1000,
                                                        T[4] / 1000],
                          "colors": [4, 4, 4, 4, 0]}]},
         ]},
        {"heading": "Movements in detail", "kind": "entries",
         "weight": 0.5, "step": 0.15, "inner": 0.05, "min_pages": 4,
         "entries": [
             {"title": "Reading Rooms", "dates": f"£{ROWS[0][7]:,} left",
              "text": ["Year two of three. Staff costs £56,000, books and "
                       "furniture £18,200, evaluation £7,200. The balance "
                       "pays for the Westfield room's fit-out in May."]},
             {"title": "Digital Skills", "dates": "spend by Dec 2027",
              "text": ["£2,300 left after 40 laptops and 96 classes; the "
                       "fund closes when the last class is paid for."]},
             {"title": "Reading room roof", "dates": "complete",
              "text": ["The roof cost £53,800, £12,000 more than the "
                       "grant; the trustees transferred the difference "
                       "from unrestricted funds."]},
             {"title": "Mobile library van", "dates": "appeal open",
              "text": ["£14,900 of the £42,000 needed; the van is ordered "
                       "only when the appeal reaches £35,000."]},
         ]},
        {"heading": "Fund by month", "kind": "figure", "weight": 0.6,
         "min_pages": 4, "height": 150, "charts": [{"type": "line",
          "title": "Reading Rooms fund", "subtitle": "£k, balance",
          "x": ["Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov",
                "Dec", "Jan", "Feb", "Mar"], "format": "{:.0f}",
          "series": [{"name": "Balance", "area": True,
                      "values": [71.6, 64.8, 58.0, 51.2, 44.4, 97.6, 90.8,
                                 84.0, 77.2, 70.4, 63.6, 57.0]}],
          "marks": [(5, "second payment")]}]},
        {"heading": "Reporting to funders", "kind": "table",
         "whole": True, "weight": 0.7, "min_pages": 4,
         "badges": {"Sent": "good", "Due": "warn"},
         "columns": [("Funder", 2), ("Report", 2.4), ("Date", 1),
                     ("", 0.8, "center")],
         "rows": [["Northfield Foundation", "Year 2 report and accounts",
                   "30 Apr 2027", "Sent"],
                  ["Hull Town Council", "Quarterly visitor numbers",
                   "15 Apr 2027", "Sent"],
                  ["Digital Skills Fund", "Final report", "31 Jan 2028",
                   "Due"],
                  ["Heritage Grant", "Completion certificate",
                   "31 Oct 2027", "Due"]]},
        {"heading": "Rules", "kind": "bullets", "weight": 0.8,
         "step": 0.1, "min_pages": 4, "items": [
             "Restricted money is only spent on the purpose in the grant "
             "letter or the donor's wishes.",
             "Shared costs (rent, utilities) are charged to a fund only "
             "if the funder agreed in writing.",
             "Overspends are covered by unrestricted funds through a "
             "transfer approved by the trustees.",
             "Unspent balances at the end of a grant are returned unless "
             "the funder agrees otherwise.",
         ]},
        {"heading": "Income by funder over three years", "kind": "figure",
         "weight": 0.9, "min_pages": 4, "height": 150, "charts": [{
             "type": "bars", "stacked": True, "subtitle": "£k",
             "format": "{:,.0f}",
             "categories": ["2024/25", "2025/26", "2026/27"],
             "series": [{"name": "Northfield Foundation",
                         "values": [0, 120, 120]},
                        {"name": "Hull Town Council",
                         "values": [50, 51, 52.5]},
                        {"name": "Digital Skills Fund", "color": 2,
                         "values": [0, 24, 24]},
                        {"name": "Legacies and appeals", "color": 4,
                         "values": [38, 22, 22]}]}]},
        {"heading": "Checks by the treasurer", "kind": "table",
         "whole": True, "weight": 1.0, "min_pages": 4,
         "badges": {"Done": "good"},
         "columns": [("Check", 4), ("", 0.8, "center")],
         "rows": [["Every restricted receipt matched to a fund", "Done"],
                  ["No fund in deficit at the year end", "Done"],
                  ["Grant conditions reviewed for each fund", "Done"],
                  ["Transfers minuted by the trustees", "Done"]]},
        {"heading": "Fund timeline", "kind": "figure", "weight": 1.1,
         "min_pages": 4, "height": 140, "charts": [{"type": "gantt",
          "columns": ["2025", "2026", "2027", "2028", "2029"],
          "today": 2.25, "today_label": "31 Mar 27",
          "tasks": [{"label": "Reading Rooms", "start": 0.25,
                     "end": 4.25, "progress": 0.6},
                    {"label": "Library service agreement", "start": 1.25,
                     "end": 3.25, "progress": 0.5},
                    {"label": "Digital Skills", "start": 0.75,
                     "end": 3.0, "progress": 0.9},
                    {"label": "Reading room roof", "start": 1.0,
                     "end": 2.7, "progress": 1},
                    {"label": "Mobile library van appeal", "start": 1.5,
                     "end": 3.25, "progress": 0.35}]}]},
    ],
}
