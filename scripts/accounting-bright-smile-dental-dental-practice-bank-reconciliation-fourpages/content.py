"""Bank Reconciliation of Bright Smile Dental: the business and everything the
document could say. The typesetting keeps what fits into four pages, the
most important first."""

BUSINESS = {
    "name": "Bright Smile Dental",
    "author": "Hannah Price, practice manager",
}

STATEMENT = 96_218.37   # bank statement balance, 30 September
# deposits recorded in the cash book, not yet on the statement
IN_TRANSIT = [("30 Sep", "Card terminal settlement, 30 Sep", 3_412.80),
              ("30 Sep", "Cheque from Denplan, September", 1_186.00)]
# payments recorded in the cash book, not yet cleared
UNPRESENTED = [("26 Sep", "100412", "Northern Dental Lab", 2_948.50),
               ("28 Sep", "BACS", "Henry Schein, materials", 1_874.22),
               ("29 Sep", "100413", "Waste collection Q3", 412.00),
               ("30 Sep", "BACS", "HMRC PAYE, September", 3_211.84)]
# items on the statement, not yet in the cash book
BANK_ONLY = [("Bank charges, September", -48.60),
             ("Interest received", 12.41),
             ("Card terminal fees, September", -261.30)]

IN_TOTAL = round(sum(a for *_, a in IN_TRANSIT), 2)
UNP_TOTAL = round(sum(a for *_, a in UNPRESENTED), 2)
ADJUSTED_BANK = round(STATEMENT + IN_TOTAL - UNP_TOTAL, 2)
BOOK_ONLY_TOTAL = round(sum(a for _, a in BANK_ONLY), 2)
CASH_BOOK = round(ADJUSTED_BANK - BOOK_ONLY_TOTAL, 2)


def gbp(value):
    sign = "−" if value < 0 else ""
    return f"{sign}£{abs(value):,.2f}"


DOCUMENT = {
    "title": "Bank Reconciliation",
    "eyebrow": "Bright Smile Dental · business current account ••••2210",
    "subtitle": "At 30 September 2027 · statement no. 141 · "
                "reconciled 2 October 2027",
    "meta": [("Account", "••••2210"), ("Statement", gbp(STATEMENT)),
             ("Cash book", gbp(CASH_BOOK)),
             ("Difference", "£0.00"), ("Prepared by", "H. Price")],
    "sections": [
        {"heading": "Reconciliation", "kind": "table", "whole": True,
         "weight": 0.1, "columns": [("", 3.4), ("£", 1, "end")],
         "rows": [["Balance per bank statement, 30 September",
                   gbp(STATEMENT)],
                  {"cells": ["Add: deposits in transit", gbp(IN_TOTAL)],
                   "style": "indent"},
                  {"cells": ["Less: unpresented payments",
                             gbp(-UNP_TOTAL)], "style": "indent"},
                  {"cells": ["Adjusted bank balance", gbp(ADJUSTED_BANK)],
                   "style": "subtotal"},
                  {"cells": ["Add back: fees net of interest, not yet "
                             "in the books", gbp(-BOOK_ONLY_TOTAL)],
                   "style": "indent"},
                  {"cells": ["Balance per cash book, 30 September",
                             gbp(CASH_BOOK)], "style": "subtotal"},
                  {"cells": ["Unexplained difference", "£0.00"],
                   "style": "total"}]},
        {"heading": "Deposits in transit", "kind": "table", "whole": True,
         "weight": 0.2,
         "columns": [("Date", 0.8), ("Item", 3), ("Amount", 1, "end")],
         "rows": [[d, i, gbp(a)] for d, i, a in IN_TRANSIT]
         + [{"cells": ["", "Total", gbp(IN_TOTAL)], "style": "subtotal"}]},
        {"heading": "Unpresented payments", "kind": "table",
         "whole": True, "weight": 0.3,
         "columns": [("Date", 0.8), ("Ref", 0.8), ("Payee", 2.4),
                     ("Amount", 1, "end")],
         "rows": [[d, r, p, gbp(a)] for d, r, p, a in UNPRESENTED]
         + [{"cells": ["", "", "Total", gbp(UNP_TOTAL)],
             "style": "subtotal"}]},
        {"heading": "To post to the cash book", "kind": "table",
         "whole": True, "weight": 0.4,
         "columns": [("Item", 3.4), ("Amount", 1, "end")],
         "rows": [[i, gbp(a)] for i, a in BANK_ONLY]
         + [{"cells": ["Net", gbp(BOOK_ONLY_TOTAL)],
             "style": "subtotal"}]},
        {"heading": "Sign-off", "kind": "table", "look": "plain",
         "header": False, "whole": True, "weight": 0.5,
         "columns": [("", 1), ("", 1)],
         "rows": [["Prepared: Hannah Price, 2 Oct 2027",
                   "Reviewed: Dr Amina Yusuf, 3 Oct 2027"],
                  ["Signature ____________________",
                   "Signature ____________________"]]},
        {"heading": "Card settlements", "kind": "figure", "weight": 0.6,
         "min_pages": 2, "height": 150, "charts": [{"type": "bars",
          "title": "Card takings and settlements, last week of "
                   "September", "subtitle": "£", "format": "{:,.0f}",
          "categories": ["24 Sep", "25 Sep", "26 Sep", "27 Sep",
                         "28 Sep", "29 Sep", "30 Sep"],
          "series": [{"name": "Taken at reception", "color": 4,
                      "values": [2980, 3410, 3120, 3360, 1840, 2870,
                                 3412.8]},
                     {"name": "Settled to the bank", "values": [2980,
                                                                3410,
                                                                3120,
                                                                3360,
                                                                1840,
                                                                2870,
                                                                0]}]}]},
        {"heading": "Balance over the month", "kind": "figure",
         "weight": 0.7, "min_pages": 2, "height": 140, "charts": [{
             "type": "line", "subtitle": "£k", "format": "{:.0f}",
             "x": ["1", "5", "10", "15", "20", "25", "30"],
             "series": [{"name": "Bank statement", "values": [
                 81.7, 86.4, 71.2, 79.8, 88.3, 90.6, STATEMENT / 1000]},
                        {"name": "Cash book", "color": 1, "dash": True,
                         "values": [81.7, 85.1, 70.6, 78.9, 87.4, 88.2,
                                    CASH_BOOK / 1000]}]}]},
        {"heading": "Checks", "kind": "table", "whole": True,
         "weight": 0.8, "min_pages": 4, "badges": {"Done": "good",
                                                   "Follow up": "warn"},
         "columns": [("Check", 4), ("", 1, "center")],
         "rows": [["Opening balance agrees to last month's reconciliation",
                   "Done"],
                  ["Every deposit in transit cleared within 3 days",
                   "Done"],
                  ["Cheques unpresented for over 3 months", "Done"],
                  ["Card fees agree to the merchant statement", "Done"],
                  ["Cheque 100412 to the lab: confirm it was posted",
                   "Follow up"]]},
        {"heading": "Month by month", "kind": "table", "whole": True,
         "weight": 0.9, "min_pages": 4,
         "columns": [("Month", 1), ("Statement", 1.2, "end"),
                     ("Cash book", 1.2, "end"), ("Reconciling items",
                                                 1.2, "end"),
                     ("Reconciled", 1, "center")],
         "badges": {"Yes": "good"},
         "rows": [["April", "£58,912.40", "£58,204.11", "4", "Yes"],
                  ["May", "£66,041.92", "£64,893.07", "6", "Yes"],
                  ["June", "£73,118.55", "£72,402.80", "5", "Yes"],
                  ["July", "£78,206.13", "£77,015.48", "5", "Yes"],
                  ["August", "£82,944.70", "£81,706.33", "7", "Yes"],
                  ["September", gbp(STATEMENT), gbp(CASH_BOOK), "9",
                   "Yes"]]},
        {"heading": "How to reconcile", "kind": "bullets", "weight": 1.0,
         "step": 0.1, "min_pages": 4, "items": [
             "Tick every line of the statement against the cash book.",
             "List what is in the books but not on the statement "
             "(deposits in transit, unpresented payments).",
             "Post to the books what is on the statement but not in "
             "them (charges, interest, fees).",
             "The adjusted balances must agree to the penny; any "
             "difference is investigated the same day.",
         ]},
        {"heading": "Reconciling items", "kind": "figure", "weight": 1.1,
         "min_pages": 4, "height": 130, "charts": [{"type": "donut",
          "segments": [("Unpresented payments", UNP_TOTAL),
                       ("Deposits in transit", IN_TOTAL),
                       ("Bank charges and fees", 309.90),
                       ("Interest", 12.41)],
          "format": "£{:,.0f}", "center": ("9", "items")}]},
        {"heading": "Where the money went in September", "kind": "figure",
         "weight": 1.2, "min_pages": 4, "height": 170, "charts": [{
             "type": "waterfall", "format": "£{:,.0f}",
             "axis_format": "{:,.0f}", "subtitle": "cash book",
             "total_color": 0,
             "steps": [("1 Sep", 81706), ("Patients and plans", 104870),
                       ("NHS", 22100), ("Associates", -41200),
                       ("Wages and PAYE", -31390), ("Lab and materials",
                                                    -16420),
                       ("Premises", -11700),
                       ("Other", -14878), ("30 Sep", None)]}]},
        {"heading": "Bank accounts held", "kind": "table", "whole": True,
         "weight": 1.3, "min_pages": 4,
         "columns": [("Account", 2.4), ("Use", 2.4),
                     ("Balance 30 Sep", 1, "end")],
         "rows": [["Business current ••••2210", "Day-to-day, card "
                   "settlements", gbp(STATEMENT)],
                  ["Business savings ••••7781", "Tax and VAT reserve",
                   "£42,500.00"],
                  ["Equipment finance ••••0315", "Loan for the CBCT "
                   "scanner", "−£61,012.44"]]},
        {"heading": "Notes", "kind": "text", "weight": 1.4, "step": 0.2,
         "min_pages": 4, "paragraphs": [
             "The practice moved its card terminals to next-day "
             "settlement in June, so the takings of the last day of the "
             "month are always in transit. Bank charges rose by £6 a "
             "month after the bank's tariff change on 1 August.",
         ]},
    ],
}
