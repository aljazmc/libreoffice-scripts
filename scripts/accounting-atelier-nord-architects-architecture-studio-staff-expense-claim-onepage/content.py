"""Expense Claim of Atelier Nord: the business and everything the document
could say. The typesetting keeps what fits into one page, the most important
first."""

BUSINESS = {
    "name": "Atelier Nord",
    "author": "Mia Holm, architect",
}

MILEAGE_RATE = 0.45
# date, from – to, purpose, project, miles
TRIPS = [("15 Sep", "Hull – Ashby", "Site meeting, library", "AN-2318",
          84),
         ("16 Sep", "Hull – York", "Planning officer, Mill Yard",
          "AN-2302", 76),
         ("18 Sep", "Hull – Ashby", "Façade sample panel", "AN-2318", 84),
         ("22 Sep", "Hull – Leeds", "Client workshop, Kestrel offices",
          "AN-2331", 118),
         ("25 Sep", "Hull – Ashby", "Structural inspection", "AN-2318",
          84)]
# date, item, category, project, amount incl. VAT, VAT, receipt
ITEMS = [("16 Sep", "Parking, York council car park", "Travel",
          "AN-2302", 9.60, 1.60, "R1"),
         ("18 Sep", "Hi-vis and safety boots", "Site equipment",
          "AN-2318", 64.80, 10.80, "R2"),
         ("22 Sep", "Train Hull – Leeds (car to garage)", "Travel",
          "AN-2331", 31.40, 0.00, "R3"),
         ("22 Sep", "Lunch with client, two people", "Subsistence",
          "AN-2331", 38.50, 6.42, "R4"),
         ("24 Sep", "Model-making materials", "Materials", "AN-2331",
          46.20, 7.70, "R5"),
         ("25 Sep", "Printing at the site office", "Printing", "AN-2318",
          12.00, 2.00, "R6")]


def gbp(value):
    return f"£{value:,.2f}"


MILES = sum(t[4] for t in TRIPS)
MILEAGE = round(MILES * MILEAGE_RATE, 2)
RECEIPTS = round(sum(i[4] for i in ITEMS), 2)
VAT = round(sum(i[5] for i in ITEMS), 2)
TOTAL = round(MILEAGE + RECEIPTS, 2)

DOCUMENT = {
    "title": "Expense Claim",
    "eyebrow": "Atelier Nord · form EX-2 · claim 0291",
    "subtitle": "Mia Holm · site visits and client meetings, 15 – 26 "
                "September 2027",
    "meta": [("Claimant", "Mia Holm"), ("Claim", "0291"),
             ("Period", "15 – 26 Sep 2027"), ("Total claimed", gbp(TOTAL)),
             ("Paid with", "October salary")],
    "sections": [
        {"heading": "1 · Mileage", "kind": "table", "whole": True,
         "weight": 0.1,
         "columns": [("Date", 0.7), ("Journey", 1.3), ("Purpose", 2.4),
                     ("Project", 0.9), ("Miles", 0.7, "end"),
                     ("Amount", 0.9, "end")],
         "rows": [[d, j, p, pr, str(m), gbp(m * MILEAGE_RATE)]
                  for d, j, p, pr, m in TRIPS]
         + [{"cells": ["", "", f"At {MILEAGE_RATE * 100:.0f}p a mile",
                       "", str(MILES), gbp(MILEAGE)],
             "style": "subtotal"}]},
        {"heading": "2 · Receipts", "kind": "table", "whole": True,
         "weight": 0.2,
         "columns": [("Date", 0.7), ("Item", 2.6), ("Category", 1.2),
                     ("Project", 0.9), ("VAT", 0.7, "end"),
                     ("Amount", 0.9, "end"), ("Rcpt", 0.5, "center")],
         "rows": [[d, i, c, p, gbp(v), gbp(a), r]
                  for d, i, c, p, a, v, r in ITEMS]
         + [{"cells": ["", "", "", "", gbp(VAT), gbp(RECEIPTS), ""],
             "style": "subtotal"}]},
        {"heading": "3 · Total", "kind": "table", "whole": True,
         "weight": 0.3, "columns": [("", 3.4), ("Amount", 1, "end")],
         "rows": [["Mileage", gbp(MILEAGE)], ["Receipts", gbp(RECEIPTS)],
                  {"cells": ["Total claimed", gbp(TOTAL)],
                   "style": "total"}]},
        {"heading": "4 · Declaration and approval", "kind": "table",
         "look": "plain", "header": False, "whole": True, "weight": 0.4,
         "columns": [("", 1), ("", 1)],
         "rows": [["I confirm these expenses were incurred wholly for "
                   "the firm's business.", "Approved: Oskar Berg, "
                   "associate, 29 Sep"],
                  ["Signed: Mia Holm, 26 Sep 2027",
                   "Checked: finance, 30 Sep"]]},
        {"heading": "5 · By project", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": 140, "widths": [2, 3], "charts": [
             {"type": "donut", "title": "Recharge to projects",
              "segments": [(p, round(sum(t[4] * MILEAGE_RATE
                                         for t in TRIPS if t[3] == p)
                                     + sum(i[4] for i in ITEMS
                                           if i[3] == p), 2))
                           for p in ("AN-2318", "AN-2302", "AN-2331")],
              "format": "£{:,.2f}", "center": (gbp(TOTAL), "claimed")},
             {"type": "bars", "horizontal": True, "title": "Miles by "
              "journey", "format": "{:.0f}",
              "categories": [f"{t[0]} {t[1].split(' – ')[1]}"
                             for t in TRIPS],
              "series": [{"name": "Miles", "values": [t[4]
                                                      for t in TRIPS]}]},
         ]},
        {"heading": "6 · Rechargeable to clients", "kind": "table",
         "whole": True, "weight": 0.6, "min_pages": 2,
         "badges": {"Yes": "good", "No": "neutral"},
         "columns": [("Project", 1), ("Client", 2.2),
                     ("Rechargeable", 1, "center"),
                     ("Amount", 1, "end")],
         "rows": [["AN-2318", "Ashby Town Council", "Yes",
                   gbp(84 * 3 * MILEAGE_RATE + 64.80 + 12.00)],
                  ["AN-2302", "Mill Yard Developments", "Yes",
                   gbp(76 * MILEAGE_RATE + 9.60)],
                  ["AN-2331", "Kestrel Retail Group", "No",
                   gbp(118 * MILEAGE_RATE + 31.40 + 38.50 + 46.20)]]},
        {"heading": "7 · Policy", "kind": "bullets", "weight": 0.7,
         "step": 0.1, "min_pages": 4, "items": [
             "Mileage at 45p a mile for the first 10,000 business miles "
             "in the tax year; journeys from home count only beyond the "
             "usual commute.",
             "Receipts are required for every item; VAT receipts for "
             "anything over £25.",
             "Client entertainment needs the associate's approval in "
             "advance and is not rechargeable.",
             "Claims are submitted within a month and paid with the next "
             "salary.",
         ]},
        {"heading": "8 · Mia's claims this year", "kind": "figure",
         "weight": 0.8, "min_pages": 4, "height": 150, "charts": [{
             "type": "bars", "stacked": True, "subtitle": "£ per month",
             "format": "£{:,.0f}",
             "categories": ["Apr", "May", "Jun", "Jul", "Aug", "Sep"],
             "series": [{"name": "Mileage", "values": [98, 141, 186, 76,
                                                       0, MILEAGE]},
                        {"name": "Receipts", "color": 1,
                         "values": [44, 62, 118, 21, 0, RECEIPTS]}]}]},
        {"heading": "9 · Mileage allowance used", "kind": "figure",
         "weight": 0.9, "min_pages": 4, "height": 90, "charts": [{
             "type": "progress", "format": "{:,.0f} miles",
             "max": 10_000, "items": [
                 {"label": "Business miles, tax year to date",
                  "value": 1_204 + MILES, "status": 0,
                  "note": "the 45p rate applies up to 10,000"}]}]},
        {"heading": "10 · Finance checks", "kind": "table", "whole": True,
         "weight": 1.0, "min_pages": 4, "badges": {"OK": "good"},
         "columns": [("Check", 4), ("", 0.8, "center")],
         "rows": [["Every receipt attached and legible", "OK"],
                  ["Mileage agrees to the route planner", "OK"],
                  ["VAT reclaimed only on valid VAT receipts", "OK"],
                  ["Project codes valid and open", "OK"],
                  ["Approved by someone other than the claimant", "OK"]]},
        {"heading": "11 · VAT reclaimed", "kind": "table", "whole": True,
         "weight": 1.1, "min_pages": 4,
         "columns": [("Receipt", 0.8), ("Supplier", 2.4),
                     ("Net", 1, "end"), ("VAT", 1, "end")],
         "rows": [[r, i, gbp(a - v), gbp(v)] for d, i, c, p, a, v, r
                  in ITEMS if v]
         + [{"cells": ["", "Total", gbp(RECEIPTS - VAT
                                        - sum(i[4] for i in ITEMS
                                              if not i[5])), gbp(VAT)],
             "style": "total"}]},
        {"heading": "12 · Studio expenses this quarter", "kind": "figure",
         "weight": 1.2, "min_pages": 4, "height": 150, "widths": [3, 2],
         "charts": [
             {"type": "bars", "horizontal": True, "title": "By person",
              "format": "£{:,.0f}",
              "categories": ["Mia Holm", "Oskar Berg", "Jonas Aalto",
                             "Leo Strand", "Ingrid Lund", "Ana Sousa"],
              "series": [{"name": "Claimed", "values": [
                  round(TOTAL + 284 + 422), 612, 488, 241, 1_104, 96]}]},
             {"type": "donut", "title": "By category",
              "segments": [("Mileage", 1820), ("Travel", 640),
                           ("Subsistence", 410), ("Site equipment", 260),
                           ("Materials and printing", 480)],
              "format": "£{:,.0f}", "center": ("£3.6k", "Q3")},
         ]},
        {"heading": "13 · Journeys in detail", "kind": "table",
         "whole": True, "weight": 1.3, "min_pages": 4,
         "columns": [("Date", 0.7), ("Start", 1.4), ("Destination", 2),
                     ("Return", 0.7, "center"), ("Miles", 0.7, "end")],
         "rows": [["15 Sep", "Studio, Rope Walk", "Ashby library site, "
                   "Market Place", "Yes", "84"],
                  ["16 Sep", "Studio, Rope Walk", "York council offices, "
                   "Hungate", "Yes", "76"],
                  ["18 Sep", "Home, Cottingham", "Ashby library site",
                   "Yes", "84"],
                  ["22 Sep", "Studio, Rope Walk", "Garage, Leeds Road "
                   "(then train)", "Yes", "118"],
                  ["25 Sep", "Studio, Rope Walk", "Ashby library site",
                   "Yes", "84"]]},
        {"heading": "14 · Notes from finance", "kind": "callout",
         "weight": 1.4, "tone": "info", "min_pages": 4,
         "label": "Paid in full.",
         "text": "The journey from home on 18 September is shorter than "
                 "the usual commute plus the site trip, so the full "
                 "mileage is allowed."},
    ],
}
