"""Credit Note CN-3317 of Tidewear: the business and everything the document
could say. The typesetting keeps what fits into one page, the most important
first."""

BUSINESS = {
    "name": "Tidewear",
    "author": "Tidewear Outdoor Ltd, customer accounts",
}

# style, colour, size, qty, unit price (wholesale, ex VAT), reason
LINES = [("Shoreline waterproof jacket", "Kelp green", "M", 4, 74.00,
          "Seam tape lifting"),
         ("Shoreline waterproof jacket", "Kelp green", "L", 3, 74.00,
          "Seam tape lifting"),
         ("Shoreline waterproof jacket", "Storm navy", "L", 2, 74.00,
          "Seam tape lifting"),
         ("Tor fleece", "Heather", "S", 6, 31.50, "Wrong size sent"),
         ("Ridge beanie", "Rust", "One size", 10, 8.40,
          "Ordered in error, agreed return")]
RESTOCKING = 0.10   # on items returned in error only
VAT = 0.20


def gbp(value):
    sign = "−" if value < 0 else ""
    return f"{sign}£{abs(value):,.2f}"


GOODS = round(sum(q * p for *_, q, p, _ in LINES), 2)
ERROR = round(sum(q * p for *_, q, p, r in LINES if "error" in r), 2)
FEE = round(ERROR * RESTOCKING, 2)
POSTAGE = 18.50
NET = round(GOODS - FEE + POSTAGE, 2)
TAX = round(NET * VAT, 2)
TOTAL = round(NET + TAX, 2)
INVOICE_BALANCE = 3_486.00

DOCUMENT = {
    "title": "Credit Note CN-3317",
    "eyebrow": "Tidewear Outdoor Ltd · wholesale",
    "subtitle": "Returned goods from Peak & Paddle, Keswick · against "
                "invoice INV-21944 of 2 October 2027",
    "meta": [("Credit note", "CN-3317"), ("Date", "4 Nov 2027"),
             ("Account", "W-0118"), ("Invoice", "INV-21944"),
             ("Credit", gbp(TOTAL))],
    "sections": [
        {"kind": "table", "look": "plain", "header": False, "whole": True,
         "weight": 0.05, "columns": [("", 1), ("", 1)],
         "rows": [["**From** Tidewear Outdoor Ltd",
                   "**To** Peak & Paddle Ltd"],
                  ["Unit 7, Harbour Works, Falmouth TR11 2AA",
                   "18 Lake Road, Keswick CA12 5BX"],
                  ["VAT GB 401 2288 61", "Returns authorisation RA-0884"],
                  ["wholesale@tidewear.example", "Contact: Jo Ellis"]]},
        {"heading": "Credited items", "kind": "table", "whole": True,
         "weight": 0.1,
         "columns": [("Item", 2.4), ("Colour", 1), ("Size", 0.8),
                     ("Qty", 0.5, "end"), ("Price", 0.8, "end"),
                     ("Credit", 0.9, "end"), ("Reason", 1.7)],
         "rows": [[s, c, z, str(q), gbp(p), gbp(q * p), r]
                  for s, c, z, q, p, r in LINES]
         + [{"cells": ["Goods returned", "", "", "", "", gbp(GOODS), ""],
             "style": "subtotal"},
            {"cells": ["Restocking fee, 10 % on items ordered in error",
                       "", "", "", "", gbp(-FEE), ""], "style": "muted"},
            {"cells": ["Return postage refunded", "", "", "", "",
                       gbp(POSTAGE), ""], "style": "indent"},
            {"cells": ["Net credit", "", "", "", "", gbp(NET), ""],
             "style": "subtotal"},
            {"cells": ["VAT at 20 %", "", "", "", "", gbp(TAX), ""],
             "style": "indent"},
            {"cells": ["Total credit", "", "", "", "", gbp(TOTAL), ""],
             "style": "total"}]},
        {"kind": "callout", "weight": 0.2, "tone": "good",
         "label": "How it is applied:",
         "text": f"this credit of {gbp(TOTAL)} is set against invoice "
                 f"INV-21944. The balance of that invoice is now "
                 f"{gbp(INVOICE_BALANCE - TOTAL)}, due on 1 December "
                 "2027."},
        {"heading": "Returns inspection", "kind": "table", "whole": True,
         "weight": 0.3, "min_pages": 2,
         "badges": {"Faulty": "bad", "Resaleable": "good",
                    "Seconds": "warn"},
         "columns": [("Item", 2.6), ("Qty", 0.5, "end"),
                     ("Finding", 2.6), ("Outcome", 1, "center")],
         "rows": [["Shoreline jacket, kelp green and navy", "9",
                   "Hem seam tape lifting after washing; batch SL-0727",
                   "Faulty"],
                  ["Tor fleece, heather S", "6", "Unworn, tags on",
                   "Resaleable"],
                  ["Ridge beanie, rust", "10", "Unworn, two tags torn",
                   "Seconds"]]},
        {"heading": "Account after this credit", "kind": "figure",
         "weight": 0.4, "min_pages": 2, "height": 150, "charts": [{
             "type": "waterfall", "format": "£{:,.0f}",
             "axis_format": "{:,.0f}", "total_color": 0,
             "steps": [("Owed before", INVOICE_BALANCE + 2_140),
                       ("This credit", -TOTAL),
                       ("Paid 28 Oct", -1_200),
                       ("Owed now", None)]}]},
        {"heading": "What happens to the goods", "kind": "bullets",
         "weight": 0.5, "step": 0.1, "min_pages": 2, "items": [
             "The nine jackets go back to the factory under the quality "
             "agreement; the factory credits us for them.",
             "The fleeces return to stock at full value.",
             "The beanies are sold as seconds at the sample sale.",
         ]},
        {"heading": "Batch SL-0727", "kind": "figure", "weight": 0.6,
         "min_pages": 4, "height": 150, "widths": [3, 2], "charts": [
             {"type": "bars", "title": "Jackets returned as faulty",
              "subtitle": "by stockist", "horizontal": True,
              "format": "{:.0f}",
              "categories": ["Peak & Paddle", "Web shop customers",
                             "Coast & Crag", "Fell Outdoors",
                             "Marketplace"],
              "series": [{"name": "Jackets", "values": [9, 31, 6, 4, 12],
                          "colors": ["bad", 0, 0, 0, 0]}]},
             {"type": "donut", "title": "Batch of 1,200",
              "segments": [("Sold, no issue", 1_046, "good"),
                           ("Returned faulty", 62, "bad"),
                           ("Held back for testing", 92, 4)],
              "format": "{:,.0f}", "center": ("5.2 %", "faulty")},
         ]},
        {"heading": "Accounting entries", "kind": "table", "whole": True,
         "weight": 0.7, "min_pages": 4,
         "columns": [("Account", 2.8), ("Debit", 1, "end"),
                     ("Credit", 1, "end")],
         "rows": [["Sales returns", gbp(GOODS - FEE + POSTAGE), ""],
                  ["VAT on sales", gbp(TAX), ""],
                  ["Trade debtors: Peak & Paddle", "", gbp(TOTAL)],
                  ["Stock: resaleable returns at cost",
                   gbp(6 * 31.50 * 0.42), ""],
                  ["Cost of sales", "", gbp(6 * 31.50 * 0.42)],
                  ["Claim on supplier: faulty jackets",
                   gbp(9 * 74.00 * 0.4), ""],
                  ["Cost of sales", "", gbp(9 * 74.00 * 0.4)]]},
        {"heading": "Returns policy for stockists", "kind": "entries",
         "weight": 0.8, "step": 0.2, "inner": 0.1, "min_pages": 4,
         "entries": [
             {"title": "Faulty goods", "text": [
                 "Credited in full, with return postage, at any time "
                 "within the two-year guarantee."]},
             {"title": "Our mistakes", "text": [
                 "Wrong items or sizes are credited in full and the "
                 "right ones sent the same day."]},
             {"title": "Ordered in error", "text": [
                 "Returns within 30 days in resaleable condition, less "
                 "a 10 % restocking fee."]},
         ]},
        {"heading": "Stockist returns this season", "kind": "figure",
         "weight": 0.9, "min_pages": 4, "height": 140, "charts": [{
             "type": "line", "subtitle": "% of wholesale units returned",
             "x": ["Aug", "Sep", "Oct", "Nov"], "format": "{:.1f}",
             "series": [{"name": "Returns", "area": True,
                         "values": [1.8, 2.4, 4.1, 3.0]}],
             "marks": [(2, "batch SL-0727")]}]},
        {"heading": "Peak & Paddle account", "kind": "table", "whole": True,
         "weight": 1.0, "min_pages": 4,
         "badges": {"Paid": "good", "Open": "warn", "Credit": "info"},
         "columns": [("Date", 1), ("Document", 1.6), ("Amount", 1, "end"),
                     ("Balance", 1, "end"), ("", 0.8, "center")],
         "rows": [["2 Aug", "INV-21512", "£2,140.00", "£2,140.00",
                   "Open"],
                  ["2 Oct", "INV-21944", gbp(INVOICE_BALANCE),
                   gbp(INVOICE_BALANCE + 2_140), "Open"],
                  ["28 Oct", "Payment", "−£1,200.00",
                   gbp(INVOICE_BALANCE + 940), "Paid"],
                  ["4 Nov", "CN-3317", gbp(-TOTAL),
                   gbp(INVOICE_BALANCE + 940 - TOTAL), "Credit"]]},
        {"heading": "Goods returned", "kind": "figure", "weight": 1.1,
         "min_pages": 4, "height": 140, "charts": [{"type": "donut",
          "segments": [("Faulty, back to factory", 9 * 74.0, "bad"),
                       ("Back to stock", 6 * 31.5, "good"),
                       ("Sold as seconds", 10 * 8.4, "warn")],
          "format": "£{:,.0f}", "center": (gbp(GOODS)[:-3],
                                           "at wholesale")}]},
        {"heading": "Contact", "kind": "tags", "weight": 1.2,
         "step": 0.1, "min_pages": 4, "items": [
             ("Wholesale accounts", "Kerry Trelawny, 01326 555 0110"),
             ("Returns warehouse", "Unit 7, Harbour Works, Falmouth"),
             ("Questions about this credit", "quote CN-3317"),
         ]},
    ],
}
