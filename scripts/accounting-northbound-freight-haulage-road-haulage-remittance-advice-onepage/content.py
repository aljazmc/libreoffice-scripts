"""Remittance Advice of Northbound Freight: the business and everything the
document could say. The typesetting keeps what fits into one page, the most
important first."""

BUSINESS = {
    "name": "Northbound Freight",
    "author": "Northbound Freight Ltd, accounts payable",
}

# invoice, date, description, gross £
INVOICES = [("TS-88412", "02 Feb 2028", "12 drive tyres, 315/70 R22.5, "
             "fitted", 4_812.00),
            ("TS-88507", "09 Feb 2028", "Trailer tyres × 8, fitted",
             2_664.00),
            ("TS-88631", "16 Feb 2028", "Puncture call-outs × 3, M62",
             486.00),
            ("TS-88702", "21 Feb 2028", "Tyre inspection contract, "
             "February", 720.00),
            ("TS-88745", "24 Feb 2028", "Steer tyres × 4, fitted",
             1_996.80)]
DISCOUNT_RATE = 0.015


def gbp(value):
    sign = "−" if value < 0 else ""
    return f"{sign}£{abs(value):,.2f}"


GROSS = round(sum(i[3] for i in INVOICES), 2)
CREDIT = -802.00
DISCOUNT = -round((GROSS + CREDIT) * DISCOUNT_RATE, 2)
PAID = round(GROSS + CREDIT + DISCOUNT, 2)

DOCUMENT = {
    "title": "Remittance Advice",
    "eyebrow": "NORTHBOUND FREIGHT LTD · ACCOUNTS PAYABLE",
    "subtitle": "Payment run 2028-09 · to TyreServe UK Ltd · by BACS",
    "meta": [("Payment run", "2028-09"), ("Date paid", "1 Mar 2028"),
             ("Supplier", "TyreServe UK"), ("Account", "S-0217"),
             ("Amount paid", gbp(PAID))],
    "sections": [
        {"kind": "table", "look": "plain", "header": False, "whole": True,
         "weight": 0.05, "columns": [("", 1), ("", 1)],
         "rows": [["**From** Northbound Freight Ltd",
                   "**To** TyreServe UK Ltd, credit control"],
                  ["Depot 3, Ings Road, Wakefield WF1 1DS",
                   "Unit 12, Croda Park, Leeds LS9 0RD"],
                  ["payables@northbound.example",
                   "Your account ref.: NBF-001"]]},
        {"heading": "Invoices paid", "kind": "table", "whole": True,
         "weight": 0.1,
         "columns": [("Your ref.", 1), ("Date", 1), ("Description", 3),
                     ("Amount", 1, "end")],
         "rows": [[r, d, n, gbp(a)] for r, d, n, a in INVOICES]
         + [{"cells": ["", "", "Invoices", gbp(GROSS)],
             "style": "subtotal"},
            {"cells": ["CN-2291", "26 Feb 2028", "Credit note: wrong tyre "
                       "size on TS-88412", gbp(CREDIT)],
             "style": "indent"},
            {"cells": ["", "", "Settlement discount 1.5 %",
                       gbp(DISCOUNT)], "style": "muted"},
            {"cells": ["", "", "Paid by BACS on 1 March 2028", gbp(PAID)],
             "style": "total"}]},
        {"kind": "callout", "weight": 0.2, "tone": "accent",
         "label": "Payment details:",
         "text": f"{gbp(PAID)} paid to TyreServe UK Ltd, sort code "
                 "40-11-62, account ••••7731, reference NBF-2028-09. "
                 "Please allow two working days."},
        {"heading": "Account after this payment", "kind": "table",
         "whole": True, "weight": 0.3, "min_pages": 2,
         "badges": {"Paid": "good", "Not yet due": "neutral",
                    "Disputed": "warn"},
         "columns": [("Invoice", 1), ("Date", 1), ("Amount", 1, "end"),
                     ("Status", 1.2, "center")],
         "rows": [[r, d, gbp(a), "Paid"] for r, d, n, a in INVOICES]
         + [["TS-88811", "28 Feb 2028", gbp(3_240.00), "Not yet due"],
            ["TS-88119", "14 Jan 2028", gbp(612.00), "Disputed"]]},
        {"heading": "The payment", "kind": "figure", "weight": 0.4,
         "min_pages": 2, "height": 150, "charts": [{"type": "waterfall",
          "format": "£{:,.0f}", "axis_format": "{:,.0f}",
          "total_color": 0, "steps": [("Invoices", GROSS),
                                      ("Credit note", CREDIT),
                                      ("Discount", DISCOUNT),
                                      ("Paid", None)]}]},
        {"heading": "Disputed invoice", "kind": "entries", "weight": 0.5,
         "min_pages": 2, "step": 0.2, "inner": 0.1, "entries": [
             {"title": "TS-88119 · £612.00 held", "text": [
                 "Call-out to truck NB21 on 9 January charged at the "
                 "out-of-hours rate; our telematics show the driver "
                 "called at 16:40, inside normal hours. Please send a "
                 "credit note for £204.00 and we will pay the rest."]},
         ]},
        {"heading": "Spend with TyreServe", "kind": "figure",
         "weight": 0.6, "min_pages": 4, "height": 150, "charts": [{
             "type": "bars", "subtitle": "£k per month, gross",
             "format": "{:,.1f}",
             "categories": ["Sep", "Oct", "Nov", "Dec", "Jan", "Feb"],
             "series": [{"name": "Invoiced", "values": [8.4, 9.1, 11.6,
                                                        7.9, 10.8,
                                                        GROSS / 1000],
                         "colors": [4, 4, 4, 4, 4, 0]}]}]},
        {"heading": "Payment terms", "kind": "tags", "weight": 0.7,
         "step": 0.1, "min_pages": 4, "items": [
             ("Standard terms", "30 days from the end of the month"),
             ("Early payment", "1.5 % discount within 14 days, as "
                               "agreed in the 2027 contract"),
             ("Payment runs", "1st and 15th of each month"),
             ("Queries", "within 7 days of the invoice"),
         ]},
        {"heading": "This payment run", "kind": "table", "whole": True,
         "weight": 0.8, "min_pages": 4,
         "columns": [("Supplier", 2.4), ("Invoices", 0.8, "end"),
                     ("Amount", 1.2, "end")],
         "rows": [["TyreServe UK Ltd", "5", gbp(PAID)],
                  ["Pennine Fuels", "8", "£84,216.40"],
                  ["Volvo Truck Finance", "1", "£21,600.00"],
                  ["Eurotunnel Freight", "3", "£6,912.00"],
                  ["Others", "17", "£12,488.65"],
                  {"cells": ["Run total", "34",
                             gbp(PAID + 84_216.40 + 21_600 + 6_912
                                 + 12_488.65)], "style": "total"}]},
        {"heading": "Approvals", "kind": "table", "look": "plain",
         "header": False, "whole": True, "weight": 0.9, "min_pages": 4,
         "columns": [("", 1), ("", 1)],
         "rows": [["Prepared: Kim Hollis, payables, 28 Feb",
                   "Approved: Raj Mehta, finance director, 29 Feb"],
                  ["Second signature (over £50,000): Sean Walsh, MD",
                   "Released to the bank: 1 Mar, 07:30"]]},
        {"heading": "How the discount pays", "kind": "figure",
         "weight": 1.0, "min_pages": 4, "height": 140, "charts": [{
             "type": "bars", "title": "Settlement discounts taken",
             "subtitle": "£, last six payment runs",
             "format": "£{:,.0f}",
             "categories": ["2028-04", "2028-05", "2028-06", "2028-07",
                            "2028-08", "2028-09"],
             "series": [{"name": "Discount", "values": [
                 1_084, 1_212, 968, 1_340, 1_156, -DISCOUNT],
                 "colors": [4, 4, 4, 4, 4, 0]}]}]},
        {"heading": "Notes", "kind": "bullets", "weight": 1.1,
         "step": 0.1, "min_pages": 4, "items": [
             "Paying within 14 days earns 1.5 %, which is worth about "
             "39 % a year: cheaper than any other use of the cash.",
             "Disputed items are held, not the whole invoice.",
             "Remittances are emailed to the supplier when the run is "
             "released.",
         ]},
        {"heading": "Supplier statement match", "kind": "table",
         "whole": True, "weight": 1.2, "min_pages": 4,
         "badges": {"Matched": "good", "Held": "warn"},
         "columns": [("Item", 2.6), ("Their statement", 1.1, "end"),
                     ("Our ledger", 1.1, "end"), ("", 0.9, "center")],
         "rows": [["Balance at 29 February", "£14,692.80", "£14,692.80",
                   "Matched"],
                  ["TS-88119, call-out rate", "£612.00", "£408.00",
                   "Held"],
                  ["CN-2291 credit note", "−£802.00", "−£802.00",
                   "Matched"]]},
        {"heading": "Spend by category", "kind": "figure", "weight": 1.3,
         "min_pages": 4, "height": 130, "charts": [{"type": "donut",
          "segments": [("Drive tyres", 4_812), ("Trailer tyres", 2_664),
                       ("Steer tyres", 1_997), ("Call-outs", 486),
                       ("Inspections", 720)],
          "format": "£{:,.0f}", "center": (gbp(GROSS)[:-3],
                                           "this run")}]},
    ],
}
