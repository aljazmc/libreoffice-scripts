"""Year-End Close Checklist of Copperline Bicycle Works: the business and
everything the document could say. The typesetting keeps what fits into four
pages, the most important first."""

BUSINESS = {
    "name": "Copperline Bicycle Works",
    "author": "Copperline Bicycle Works Ltd, finance",
}

STATE = {"Done": "good", "In progress": "warn", "Not started": "bad",
         "N/A": "neutral"}
# area, task, owner, due (working day), state
TASKS = [
    ("Cash", "Bank reconciliations for all three accounts", "AM", "WD1",
     "Done"),
    ("Cash", "Petty cash counted and signed", "AM", "WD1", "Done"),
    ("Sales", "Last invoices of the year raised; cut-off tested on 20 "
     "dispatches", "HW", "WD1", "Done"),
    ("Sales", "Debtors aged; provision for doubtful debts reviewed", "AM",
     "WD2", "Done"),
    ("Purchases", "Goods received not invoiced accrued", "JC", "WD2",
     "Done"),
    ("Purchases", "Supplier statements reconciled for the top 20", "JC",
     "WD3", "In progress"),
    ("Stock", "Full stock count, raw materials and finished bikes", "PT",
     "WD0", "Done"),
    ("Stock", "Count sheets entered and differences investigated", "PT",
     "WD2", "Done"),
    ("Stock", "Work in progress valued at the year-end stage", "PT",
     "WD3", "In progress"),
    ("Stock", "Slow-moving parts reviewed for write-down", "PT", "WD4",
     "Not started"),
    ("Fixed assets", "Additions capitalised; register agreed to the "
     "ledger", "AM", "WD3", "Done"),
    ("Fixed assets", "Depreciation run for December", "AM", "WD2",
     "Done"),
    ("Payroll", "December payroll and bonuses accrued", "AM", "WD2",
     "Done"),
    ("Payroll", "Holiday pay accrual for untaken leave", "AM", "WD4",
     "Not started"),
    ("Tax", "VAT return for the quarter to December", "AM", "WD5",
     "Not started"),
    ("Tax", "Corporation tax estimate and R&D claim", "Adviser", "WD10",
     "Not started"),
    ("Reporting", "Trial balance reviewed by the FD", "RS", "WD5",
     "Not started"),
    ("Reporting", "Management accounts and board pack", "RS", "WD7",
     "Not started"),
    ("Audit", "Audit request list, items 1 – 40", "AM", "WD10",
     "In progress"),
]
COUNTS = {s: sum(1 for t in TASKS if t[4] == s) for s in STATE}
AREAS = []
for t in TASKS:
    if t[0] not in AREAS:
        AREAS.append(t[0])

DOCUMENT = {
    "title": "Year-End Close Checklist",
    "eyebrow": "COPPERLINE BICYCLE WORKS · FINANCE · FORM YE-1",
    "subtitle": "Closing the books for the year ended 31 December 2027 · "
                "status on working day 3 (5 January 2028)",
    "meta": [("Year end", "31 Dec 2027"), ("Tasks", str(len(TASKS))),
             ("Done", str(COUNTS["Done"])),
             ("Open", str(len(TASKS) - COUNTS["Done"])),
             ("Board pack", "WD7 · 11 Jan")],
    "sections": [
        {"heading": "Checklist", "kind": "table", "weight": 0.1,
         "whole": True, "badges": STATE,
         "columns": [("Area", 1), ("Task", 3.6), ("Owner", 0.7,
                                                  "center"),
                     ("Due", 0.6, "center"), ("State", 1, "center")],
         "rows": [[a, t, o, d, s] for a, t, o, d, s in TASKS]},
        {"heading": "Progress", "kind": "figure", "weight": 0.2,
         "height": {1: 120, 2: 150, 4: 160}, "widths": [2, 3],
         "charts": [
             {"type": "donut", "title": "Tasks",
              "segments": [(s, COUNTS[s], STATE[s]) for s in STATE
                           if COUNTS[s]],
              "center": (f"{COUNTS['Done'] / len(TASKS):.0%}", "done")},
             {"type": "bars", "horizontal": True, "stacked": True,
              "title": "By area", "values": False,
              "categories": AREAS,
              "series": [{"name": s, "color": STATE[s], "values": [
                  sum(1 for t in TASKS if t[0] == a and t[4] == s)
                  for a in AREAS]} for s in ("Done", "In progress",
                                              "Not started")]},
         ]},
        {"heading": "Timetable", "kind": "figure", "weight": 0.3,
         "min_pages": 2, "height": 120, "charts": [{"type": "timeline",
          "start": 0, "end": 10, "label_width": 95,
          "ticks": [(i, f"WD{i}") for i in range(0, 11, 2)],
          "events": [{"at": 0, "label": "Stock count", "sub": "31 Dec",
                      "status": "done"},
                     {"at": 2, "label": "Ledgers closed", "sub": "4 Jan",
                      "status": "done"},
                     {"at": 3, "label": "Today", "sub": "5 Jan",
                      "status": "now"},
                     {"at": 5, "label": "Trial balance", "sub": "9 Jan"},
                     {"at": 7, "label": "Board pack", "sub": "11 Jan"},
                     {"at": 10, "label": "Audit starts",
                      "sub": "16 Jan"}]}]},
        {"heading": "Owners", "kind": "tags", "weight": 0.4, "step": 0.1,
         "min_pages": 2, "items": [
             ("AM", "Asha Mistry, accountant"),
             ("JC", "Joe Carter, purchase ledger"),
             ("HW", "Hannah Ward, sales office"),
             ("PT", "Pete Tranter, production manager"),
             ("RS", "Ruth Sandell, finance director"),
         ]},
        {"heading": "Issues found so far", "kind": "entries",
         "weight": 0.5, "step": 0.2, "inner": 0.1, "min_pages": 2,
         "entries": [
             {"title": "Stock count difference on 105 groupsets",
              "text": ["Count 14 short of the system; six were fitted to "
                       "warranty bikes without a job card. Written off "
                       "£1,820 and the process changed."]},
             {"title": "Cut-off", "text": [
                 "Two bikes dispatched on 31 December were invoiced on "
                 "2 January; moved into December."]},
         ]},
        {"heading": "Sign-off", "kind": "table", "look": "plain",
         "header": False, "whole": True, "weight": 0.6, "min_pages": 2,
         "columns": [("", 1), ("", 1)],
         "rows": [["Prepared: Asha Mistry ____________",
                   "Reviewed: Ruth Sandell ____________"],
                  ["Date ____________", "Date ____________"]]},
        {"heading": "Close days over the years", "kind": "figure",
         "weight": 0.7, "min_pages": 4, "height": 140, "charts": [{
             "type": "bars", "subtitle": "working days to the board pack",
             "categories": ["2023", "2024", "2025", "2026", "2027"],
             "target": 7, "target_label": "target",
             "series": [{"name": "Days", "values": [15, 12, 10, 8, 7],
                         "colors": ["bad", "warn", "warn", 0, "good"]}]}]},
        {"heading": "Audit request list", "kind": "table", "whole": True,
         "weight": 0.8, "min_pages": 4, "badges": STATE,
         "columns": [("Item", 3.6), ("Owner", 0.8, "center"),
                     ("State", 1, "center")],
         "rows": [["Fixed asset additions with invoices", "AM", "Done"],
                  ["Stock count sheets and valuation", "PT",
                   "In progress"],
                  ["Debtors circularisation list", "AM", "Done"],
                  ["Bank confirmations", "RS", "In progress"],
                  ["Payroll reconciliation to HMRC", "AM", "Not started"],
                  ["Board minutes for 2027", "RS", "Done"]]},
        {"heading": "Lessons from last year", "kind": "bullets",
         "weight": 0.9, "step": 0.1, "min_pages": 4, "items": [
             "Count stock on the last working day, not the first of "
             "January: the factory is quiet and the count is cleaner.",
             "Accrue December's subcontract coating from the delivery "
             "notes, not from the invoices that arrive in February.",
             "Start the audit list in November.",
         ]},
        {"heading": "Tasks by working day", "kind": "figure",
         "weight": 1.0, "min_pages": 4, "height": 140, "charts": [{
             "type": "bars", "stacked": True,
             "categories": ["WD0", "WD1", "WD2", "WD3", "WD4", "WD5",
                            "WD7", "WD10"],
             "series": [{"name": s, "color": STATE[s], "values": [
                 sum(1 for t in TASKS if t[3] == d and t[4] == s)
                 for d in ["WD0", "WD1", "WD2", "WD3", "WD4", "WD5",
                           "WD7", "WD10"]]}
                 for s in ("Done", "In progress", "Not started")]}]},
        {"heading": "Open items by owner", "kind": "figure",
         "weight": 1.1, "min_pages": 4, "height": 130, "charts": [{
             "type": "bars", "horizontal": True, "format": "{:.0f}",
             "categories": ["AM", "JC", "PT", "RS", "Adviser"],
             "series": [{"name": "Open tasks", "values": [
                 sum(1 for t in TASKS if t[2] == o and t[4] != "Done")
                 for o in ["AM", "JC", "PT", "RS", "Adviser"]]}]}]},
    ],
}
