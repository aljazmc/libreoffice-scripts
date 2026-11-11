"""Loan Amortisation Schedule of Northbound Freight: the business and
everything the document could say. The typesetting keeps what fits into two
pages, the most important first."""

BUSINESS = {
    "name": "Northbound Freight",
    "author": "Northbound Freight Ltd, finance",
}

PRINCIPAL = 648_000.00     # six tractor units at £108,000
RATE = 0.069               # fixed, a year
YEARS = 5
N = YEARS * 12
BALLOON = 120_000.00       # final payment, the trucks' residual value
r = RATE / 12
PAYMENT = round((PRINCIPAL - BALLOON / (1 + r) ** N) * r
                / (1 - (1 + r) ** -N), 2)

SCHEDULE = []
balance = PRINCIPAL
for month in range(1, N + 1):
    interest = round(balance * r, 2)
    capital = round(PAYMENT - interest, 2)
    if month == N:
        capital = round(balance - BALLOON, 2)
    balance = round(balance - capital, 2)
    SCHEDULE.append((month, interest, capital, balance))
MONTHS = ["Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
          "Jan", "Feb", "Mar"]
TOTAL_INTEREST = round(sum(s[1] for s in SCHEDULE), 2)


def gbp(value):
    return f"£{value:,.2f}"


def label(month):
    year = 2028 + (month + 2) // 12
    return f"{MONTHS[(month - 1) % 12]} {year}"


YEARLY = []
for y in range(YEARS):
    part = SCHEDULE[y * 12:(y + 1) * 12]
    YEARLY.append((f"Year {y + 1}", sum(p[1] for p in part),
                   sum(p[2] for p in part), part[-1][3]))


def rows(months):
    return [[str(m), label(m), gbp(PAYMENT), gbp(i), gbp(c), gbp(b)]
            for m, i, c, b in SCHEDULE if m in months]


COLUMNS = [("No.", 0.5, "center"), ("Month", 1), ("Payment", 1, "end"),
           ("Interest", 1, "end"), ("Capital", 1, "end"),
           ("Balance", 1.1, "end")]

DOCUMENT = {
    "title": "Loan Amortisation Schedule",
    "subtitle": "Hire purchase for six Volvo FH tractor units · Volvo "
                "Truck Finance agreement VTF-2028-0331",
    "meta": [("Amount", gbp(PRINCIPAL)), ("Rate", f"{RATE:.1%} fixed"),
             ("Term", f"{N} months"), ("Monthly payment", gbp(PAYMENT)),
             ("Final payment", gbp(BALLOON))],
    "sections": [
        {"heading": "Balance over the term", "kind": "figure",
         "weight": 0.1, "min_pages": 2, "height": {2: 170, 4: 180},
         "widths": [3, 2], "charts": [
             {"type": "bars", "stacked": True, "values": False,
              "subtitle": "£k paid each year", "format": "{:,.0f}",
              "categories": [y[0] for y in YEARLY],
              "series": [{"name": "Capital", "values": [
                  round(y[2] / 1000, 1) for y in YEARLY]},
                         {"name": "Interest", "color": 1, "values": [
                             round(y[1] / 1000, 1) for y in YEARLY]}]},
             {"type": "line", "subtitle": "£k outstanding",
              "x": ["Start"] + [y[0][-1] for y in YEARLY],
              "format": "{:,.0f}", "end_labels": True,
              "series": [{"name": "Balance", "area": True, "values": [
                  PRINCIPAL / 1000] + [round(y[3] / 1000) for y in
                                       YEARLY]}]},
         ]},
        {"heading": "Year 1, month by month", "kind": "table",
         "whole": True, "weight": 0.2, "columns": COLUMNS,
         "rows": rows(range(1, 13))
         + [{"cells": ["", "Year 1", gbp(PAYMENT * 12),
                       gbp(YEARLY[0][1]), gbp(YEARLY[0][2]),
                       gbp(YEARLY[0][3])], "style": "total"}]},
        {"heading": "By year", "kind": "table", "whole": True,
         "weight": 0.3, "min_pages": 2,
         "columns": [("Year", 1), ("Payments", 1, "end"),
                     ("Interest", 1, "end"), ("Capital", 1, "end"),
                     ("Balance at the end", 1.2, "end")],
         "rows": [[y, gbp(i + c), gbp(i), gbp(c), gbp(b)]
                  for y, i, c, b in YEARLY]
         + [{"cells": ["Total", gbp(sum(i + c for _, i, c, _ in YEARLY)),
                       gbp(TOTAL_INTEREST),
                       gbp(sum(c for _, _, c, _ in YEARLY)), ""],
             "style": "total"}]},
        {"heading": "Years 2 and 3", "kind": "table", "whole": True,
         "weight": 0.5, "min_pages": 4, "columns": COLUMNS,
         "rows": rows(range(13, 37))},
        {"heading": "Years 4 and 5", "kind": "table", "whole": True,
         "weight": 0.6, "min_pages": 4, "columns": COLUMNS,
         "rows": rows(range(37, 61))
         + [{"cells": ["", "Mar 2033", "", "", "Final payment",
                       gbp(BALLOON)], "style": "total"}]},
        {"heading": "Terms", "kind": "tags", "weight": 0.4, "step": 0.1,
         "min_pages": 2, "items": [
             ("Lender", "Volvo Truck Finance UK Ltd"),
             ("Security", "the six vehicles, NB30 to NB35"),
             ("Payments", "by direct debit on the 1st of each month"),
             ("Early settlement", "allowed, with interest to the end of "
                                  "the following month"),
             ("Covenant", "operator's licence kept in good standing; "
                          "vehicles insured comprehensively"),
         ]},
        {"heading": "In the accounts", "kind": "text", "weight": 0.7,
         "step": 0.3, "min_pages": 4, "paragraphs": [
             f"The trucks are capitalised at {gbp(PRINCIPAL)} and "
             "depreciated over seven years to a residual value of "
             "£20,000 each. The loan is a liability split between "
             "amounts due within one year and after one year; interest "
             f"of {gbp(YEARLY[0][1])} is charged in the first year.",
         ]},
    ],
}
