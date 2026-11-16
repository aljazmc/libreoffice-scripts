"""Accounts Receivable Aging of Bright Smile Dental: the business and
everything the document could say. The typesetting keeps what fits into two
pages, the most important first."""

BUSINESS = {
    "name": "Bright Smile Dental",
    "author": "Hannah Price, practice manager",
}

BUCKETS = ["Current", "31–60 days", "61–90 days", "Over 90 days"]
# payer, balances by bucket (£)
PAYERS = [("NHS contract (England)", [22_100, 0, 0, 0]),
          ("Denplan plan fees", [4_210, 0, 0, 0]),
          ("Bupa Dental insurance", [2_840, 1_120, 410, 0]),
          ("AXA Health insurance", [1_960, 780, 0, 220]),
          ("Patients: treatment plans", [3_420, 1_640, 960, 1_480]),
          ("Patients: missed appointment fees", [180, 140, 120, 390]),
          ("Corporate: Harbourside Bank staff scheme", [1_200, 1_200, 0,
                                                       0])]
TOTALS = [sum(b[i] for _, b in PAYERS) for i in range(4)]
GRAND = sum(TOTALS)
OVERDUE = sum(TOTALS[1:])

# individual overdue patient accounts over 60 days
ACCOUNTS = [("P-10482", "Mr D. Okoro", "Implant, stage 2", 1_140, 96,
             "Payment plan agreed"),
            ("P-09917", "Ms L. Hart", "Crown and root canal", 640, 74,
             "Second reminder sent"),
            ("P-11203", "Mr S. Banerjee", "Orthodontics deposit", 420,
             121, "Passed to collection agency"),
            ("P-08745", "Mrs J. Walsh", "Missed appointments × 3", 150,
             98, "Write off proposed"),
            ("P-10951", "Mr A. Novak", "Whitening", 320, 65,
             "Phone call booked"),
            ("P-07718", "Ms R. Costa", "Veneers balance", 760, 88,
             "Disputed: shade"),
            ("P-11420", "Ms K. Ito", "Missed appointments × 2", 100, 95,
             "Waive: bereavement")]


def gbp(value):
    return f"£{value:,.0f}" if value else "—"


DOCUMENT = {
    "title": "Accounts Receivable Aging",
    "subtitle": "Who owes the practice money, and for how long · at 30 "
                "September 2027",
    "meta": [("Total owed", gbp(GRAND)), ("Overdue", gbp(OVERDUE)),
             ("Over 90 days", gbp(TOTALS[3])),
             ("Debtor days", "29"), ("Owner", "Hannah Price")],
    "sections": [
        {"heading": "By payer", "kind": "table", "whole": True,
         "weight": 0.1,
         "columns": [("Payer", 2.8)] + [(b, 0.9, "end") for b in BUCKETS]
         + [("Total", 0.9, "end")],
         "rows": [[p] + [gbp(v) for v in b] + [gbp(sum(b))]
                  for p, b in PAYERS]
         + [{"cells": ["Total"] + [gbp(v) for v in TOTALS] + [gbp(GRAND)],
             "style": "total"},
            {"cells": ["Share"] + [f"{v / GRAND:.0%}" for v in TOTALS]
             + ["100%"], "style": "muted"}]},
        {"heading": "Aging profile", "kind": "figure", "weight": 0.2,
         "height": {1: 165, 2: 175, 4: 185}, "widths": [3, 2],
         "charts": [
             {"type": "bars", "horizontal": True, "stacked": True,
              "values": False, "format": "£{:,.0f}",
              "categories": [p.split(":")[0].split(" (")[0]
                             .replace(" insurance", "")
                             for p, _ in PAYERS],
              "series": [{"name": BUCKETS[i], "color": ["good", "info",
                                                        "warn", "bad"][i],
                          "values": [b[i] for _, b in PAYERS]}
                         for i in range(4)]},
             {"type": "donut", "title": "By age",
              "segments": [(BUCKETS[i], TOTALS[i], ["good", "info", "warn",
                                                    "bad"][i])
                           for i in range(4)],
              "format": "£{:,.0f}", "center": (f"£{GRAND / 1000:.1f}k",
                                               "owed")},
         ]},
        {"heading": "Overdue patient accounts", "kind": "table",
         "weight": 0.3, "step": 0.05, "min_pages": 2,
         "badges": {"Passed to collection agency": "bad",
                    "Write off proposed": "warn",
                    "Disputed: shade": "warn",
                    "Payment plan agreed": "good"},
         "columns": [("Account", 0.8), ("Patient", 1.4),
                     ("Treatment", 1.8), ("Owed", 0.8, "end"),
                     ("Days", 0.6, "end"), ("Status", 2)],
         "rows": [[a, n, t, gbp(o), str(d), s]
                  for a, n, t, o, d, s in ACCOUNTS]},
        {"heading": "Trend", "kind": "figure", "weight": 0.4,
         "min_pages": 2, "height": 150, "charts": [{"type": "line",
          "subtitle": "£k owed at month end", "format": "{:.0f}",
          "x": ["Apr", "May", "Jun", "Jul", "Aug", "Sep"],
          "series": [{"name": "Total", "area": True,
                      "values": [41.8, 43.2, 40.6, 44.9, 41.5,
                                 GRAND / 1000]},
                     {"name": "Overdue", "color": "bad",
                      "values": [9.4, 10.8, 9.9, 11.6, 10.4,
                                 OVERDUE / 1000]}]}]},
        {"heading": "Collection policy", "kind": "bullets",
         "weight": 0.5, "step": 0.1, "min_pages": 2, "items": [
             "Treatment over £500 is paid 50 % at booking and the rest "
             "on the day of the final appointment.",
             "Reminders at 14, 30 and 45 days; a phone call at 60 days.",
             "Accounts over 90 days go to the collection agency after "
             "the principal agrees.",
             "Missed appointment fees are waived once a year, and always "
             "for illness or bereavement.",
         ]},
        {"heading": "Insurer claims", "kind": "figure", "weight": 0.6,
         "min_pages": 4, "height": 150, "charts": [{"type": "bars",
          "title": "Days from claim to payment", "subtitle": "average, "
          "last six months", "format": "{:.0f}", "target": 30,
          "target_label": "terms",
          "categories": ["NHS", "Denplan", "Bupa", "AXA", "Harbourside"],
          "series": [{"name": "Days", "values": [14, 8, 37, 44, 52],
                      "colors": ["good", "good", "warn", "bad",
                                 "bad"]}]}]},
        {"heading": "Provision for bad debts", "kind": "table",
         "whole": True, "weight": 0.7, "min_pages": 4,
         "columns": [("Age", 1.6), ("Balance", 1, "end"),
                     ("Rate", 0.8, "end"), ("Provision", 1, "end")],
         "rows": [[b, gbp(t), f"{r:.0%}", gbp(round(t * r))]
                  for b, t, r in zip(BUCKETS, TOTALS,
                                     [0.0, 0.05, 0.25, 0.6])]
         + [{"cells": ["Total", gbp(GRAND), "", gbp(sum(
             round(t * r) for t, r in zip(TOTALS,
                                          [0.0, 0.05, 0.25, 0.6])))],
             "style": "total"}]},
        {"heading": "Actions this month", "kind": "entries",
         "weight": 0.8, "step": 0.2, "inner": 0.1, "min_pages": 4,
         "entries": [
             {"title": "AXA: resubmit four claims", "text": [
                 "Rejected for missing tooth notation; corrected and "
                 "resent on 1 October."]},
             {"title": "Harbourside Bank", "text": [
                 "The scheme invoice for August is unpaid; their new "
                 "purchase order process needs a PO number on every "
                 "invoice."]},
             {"title": "Write-offs for approval", "text": [
                 "£250 of missed appointment fees (two patients), for "
                 "Dr Yusuf to approve."]},
         ]},
        {"heading": "Measures", "kind": "figure", "weight": 0.9,
         "min_pages": 4, "charts": [{"type": "gauges", "items": [
             {"label": "Debtor days", "value": 29, "max": 60,
              "target": 30, "status": "good", "display": "29"},
             {"label": "Overdue share", "value": OVERDUE / GRAND * 100,
              "max": 50, "target": 20, "status": "warn",
              "display": f"{OVERDUE / GRAND:.0%}"},
             {"label": "Over 90 days", "value": TOTALS[3] / GRAND * 100,
              "max": 20, "target": 5, "status": "warn",
              "display": f"{TOTALS[3] / GRAND:.0%}"}]}]},
        {"heading": "Payment methods", "kind": "figure", "weight": 1.0,
         "min_pages": 4, "height": 150, "widths": [2, 3], "charts": [
             {"type": "donut", "title": "How patients paid, September",
              "segments": [("Card at reception", 68), ("Online link", 17),
                           ("Finance plan", 9), ("Bank transfer", 6)],
              "format": "{:.0f}%", "center": ("£61k", "private")},
             {"type": "bars", "title": "Overdue by month of treatment",
              "subtitle": "£", "format": "{:,.0f}",
              "categories": ["Apr", "May", "Jun", "Jul", "Aug"],
              "series": [{"name": "Still owed", "values": [620, 870, 1290,
                                                           2010, 3670],
                          "colors": ["bad", "bad", "warn", "warn",
                                     "info"]}]},
         ]},
        {"heading": "Reminder letters sent", "kind": "table",
         "whole": True, "weight": 1.1, "min_pages": 4,
         "columns": [("Stage", 2.4), ("Sent", 0.8, "end"),
                     ("Paid within 14 days", 1.4, "end")],
         "rows": [["First reminder, day 14", "42", "71 %"],
                  ["Second reminder, day 30", "16", "56 %"],
                  ["Final notice, day 45", "7", "43 %"],
                  ["Phone call, day 60", "5", "60 %"]]},
        {"heading": "Debtor days over the year", "kind": "figure",
         "weight": 1.2, "min_pages": 4, "height": 150, "charts": [{
             "type": "line", "format": "{:.0f}", "target": 30,
             "target_label": "target",
             "x": ["Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr", "May",
                   "Jun", "Jul", "Aug", "Sep"],
             "series": [{"name": "Debtor days", "area": True,
                         "values": [36, 35, 38, 34, 33, 31, 32, 33, 30,
                                    32, 30, 29]}]}]},
        {"heading": "Who to call", "kind": "tags", "weight": 1.3,
         "step": 0.1, "min_pages": 4, "items": [
             ("Insurers", "claims team at each insurer, via the portal"),
             ("Patients", "reception, Monday and Thursday afternoons"),
             ("Collection agency", "Fairway Credit, 0161 555 0190"),
         ]},
    ],
}
