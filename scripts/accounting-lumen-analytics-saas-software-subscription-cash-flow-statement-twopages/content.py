"""Cash Flow Statement of Lumen Analytics: the business and everything the
document could say. The typesetting keeps what fits into two pages, the most
important first."""

BUSINESS = {
    "name": "Lumen Analytics",
    "author": "Lumen Analytics Inc., finance team",
}


def k(value):
    """Thousands of dollars, negatives in brackets."""
    return f"({-value:,.0f})" if value < 0 else f"{value:,.0f}"


# $k for 2026 and 2025
OPERATING = [("Net loss", -6840, -8120),
             ("Depreciation and amortisation", 410, 360),
             ("Share-based compensation", 1260, 980),
             ("Increase in accounts receivable", -1140, -720),
             ("Increase in prepaid expenses", -230, -160),
             ("Increase in deferred revenue", 2980, 2110),
             ("Increase in accounts payable and accruals", 520, 340)]
INVESTING = [("Purchase of equipment", -310, -280),
             ("Capitalised software development", -1180, -940)]
FINANCING = [("Series A preferred shares, net of costs", 17600, 0),
             ("Exercise of stock options", 90, 40),
             ("Repayment of venture debt", -1500, -500)]
OPENING = (7310, 14200)


def total(lines, column):
    return sum(line[column] for line in lines)


def rows(lines, detail=1):
    return [{"cells": [name, k(a), k(b)], "style": "indent",
             "min_pages": detail} for name, a, b in lines]


NET_OP = (total(OPERATING, 1), total(OPERATING, 2))
NET_INV = (total(INVESTING, 1), total(INVESTING, 2))
NET_FIN = (total(FINANCING, 1), total(FINANCING, 2))
CHANGE = tuple(NET_OP[i] + NET_INV[i] + NET_FIN[i] for i in range(2))
CLOSING = tuple(OPENING[i] + CHANGE[i] for i in range(2))
COLUMNS = [("$ thousands", 3.4), ("2026", 1, "end"), ("2025", 1, "end")]

DOCUMENT = {
    "title": "Statement of Cash Flows",
    "subtitle": "For the year ended 31 December 2026 · indirect method · "
                "unaudited",
    "meta": [("Company", "Lumen Analytics Inc."), ("Year", "2026"),
             ("Cash at year end", f"${CLOSING[0] / 1000:.1f}m"),
             ("Free cash flow", f"−${-(NET_OP[0] + NET_INV[0]) / 1000:.1f}m"),
             ("Prepared", "CFO office")],
    "sections": [
        {"heading": "Statement", "kind": "table", "whole": True,
         "weight": 0.1, "columns": COLUMNS,
         "rows": [{"cells": ["Operating activities", "", ""],
                   "style": "section"}]
         + rows(OPERATING[:1])
         + [{"cells": ["Adjustments for non-cash items", "", ""],
             "style": "muted", "min_pages": 2}]
         + rows(OPERATING[1:3], 2)
         + [{"cells": ["Non-cash items", k(sum(line[1] for line in
                                              OPERATING[1:3])),
                       k(sum(line[2] for line in OPERATING[1:3]))],
             "style": "indent", "max_pages": 1},
            {"cells": ["Changes in working capital", "", ""],
             "style": "muted", "min_pages": 2}]
         + rows(OPERATING[3:], 2)
         + [{"cells": ["Working capital", k(sum(line[1] for line in
                                               OPERATING[3:])),
                       k(sum(line[2] for line in OPERATING[3:]))],
             "style": "indent", "max_pages": 1},
            {"cells": ["Net cash used in operating activities",
                       k(NET_OP[0]), k(NET_OP[1])], "style": "subtotal"},
            {"cells": ["Investing activities", "", ""], "style": "section"}]
         + rows(INVESTING)
         + [{"cells": ["Net cash used in investing activities",
                       k(NET_INV[0]), k(NET_INV[1])], "style": "subtotal"},
            {"cells": ["Financing activities", "", ""], "style": "section"}]
         + rows(FINANCING)
         + [{"cells": ["Net cash from financing activities",
                       k(NET_FIN[0]), k(NET_FIN[1])], "style": "subtotal"},
            {"cells": ["Net change in cash", k(CHANGE[0]), k(CHANGE[1])],
             "style": "highlight"},
            {"cells": ["Cash at 1 January", k(OPENING[0]), k(OPENING[1])],
             "style": "indent"},
            {"cells": ["Cash at 31 December", k(CLOSING[0]),
                       k(CLOSING[1])], "style": "total"}]},
        {"heading": "From loss to cash", "kind": "figure", "weight": 0.2,
         "height": {1: 165, 2: 180, 4: 190}, "charts": [{
             "type": "waterfall", "format": "{:,.0f}",
             "subtitle": "$k, 2026", "total_color": 0,
             "steps": [("Opening cash", OPENING[0]),
                       ("Net loss", OPERATING[0][1]),
                       ("Non-cash items", 1670),
                       ("Deferred revenue", 2980),
                       ("Other working capital", -850),
                       ("Investing", NET_INV[0]),
                       ("Series A", 17600),
                       ("Debt and options", -1410),
                       ("Closing cash", None)]}]},
        {"kind": "callout", "weight": 0.25, "tone": "info",
         "label": "Customers fund us:",
         "text": "annual contracts are billed up front, so deferred "
                 "revenue grew by $2.98m and paid for almost half of the "
                 "operating loss."},
        {"heading": "Quarter by quarter", "kind": "figure", "weight": 0.4,
         "min_pages": 2, "height": 160, "widths": [3, 2], "charts": [
             {"type": "bars", "title": "Operating cash flow",
              "subtitle": "$k", "format": "{:,.0f}",
              "categories": ["Q1", "Q2", "Q3", "Q4"],
              "series": [{"name": "2025", "color": 4,
                          "values": [-1620, -1380, -1150, -1060]},
                         {"name": "2026", "values": [-1440, -880, -530,
                                                     -190]}]},
             {"type": "donut", "title": "Where the Series A went",
              "format": "${:,.1f}m", "center": ("$17.6m", "raised"),
              "segments": [("Still in the bank", 10.8),
                           ("Operating burn", 2.99),
                           ("Product investment", 1.49),
                           ("Venture debt repaid", 1.5),
                           ("Other", 0.82)]},
         ]},
        {"heading": "Notes", "kind": "entries", "weight": 0.5,
         "step": 0.15, "inner": 0.05, "min_pages": 2, "entries": [
             {"title": "1. Series A", "text": [
                 "Series A preferred shares of $18.0m were issued in "
                 "March 2026 to Northlake Ventures and existing investors; "
                 "costs of $0.4m were deducted from the proceeds."]},
             {"title": "2. Capitalised software", "text": [
                 "Development costs of the new forecasting engine are "
                 "capitalised from technical feasibility and amortised "
                 "over three years."]},
             {"title": "3. Venture debt", "text": [
                 "The $2.0m facility from Cobalt Bank was repaid in full "
                 "in 2026; there is no debt at the year end."]},
         ]},
        {"heading": "Cash conversion", "kind": "figure", "weight": 0.6,
         "min_pages": 4, "charts": [{"type": "kpis", "tiles": [
             {"label": "Operating cash flow", "value": "−$3.0m",
              "delta": "+$2.2m", "delta_status": "good", "status": 0,
              "note": "vs −$5.2m in 2025"},
             {"label": "Free cash flow", "value": "−$4.5m",
              "status": "warn", "note": "after product investment"},
             {"label": "Burn multiple", "value": "1.3×", "delta": "−0.9",
              "delta_status": "good", "status": 1,
              "note": "net burn ÷ net new ARR"},
             {"label": "Months of cash", "value": "29", "status": "good",
              "note": "at the Q4 burn"},
         ]}]},
        {"heading": "Monthly cash balance", "kind": "figure",
         "weight": 0.7, "min_pages": 4, "height": 160, "charts": [{
             "type": "line", "subtitle": "$m at month end",
             "x": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
                   "Aug", "Sep", "Oct", "Nov", "Dec"],
             "format": "{:.1f}", "marks": [(2, "Series A")],
             "series": [{"name": "Cash", "area": True,
                         "values": [6.8, 6.3, 23.4, 22.6, 22.0, 21.4,
                                    20.9, 20.4, 20.0, 19.6, 19.3,
                                    19.0]}]}]},
        {"heading": "Accounting policies", "kind": "text", "weight": 0.8,
         "step": 0.3, "min_pages": 4, "paragraphs": [
             "Cash includes bank balances and money market funds with "
             "maturities under three months. The statement uses the "
             "indirect method, starting from the net loss and removing "
             "non-cash items and changes in working capital.",
             "Interest received of $0.31m is included in operating "
             "activities; there was no tax paid.",
         ]},
        {"heading": "Cash by quarter", "kind": "table", "whole": True,
         "weight": 0.9, "min_pages": 4,
         "columns": [("$ thousands", 2.6), ("Q1", 1, "end"),
                     ("Q2", 1, "end"), ("Q3", 1, "end"), ("Q4", 1, "end"),
                     ("2026", 1, "end")],
         "rows": [["Operating activities", "(1,440)", "(880)", "(530)",
                   "(190)", "(3,040)"],
                  ["Investing activities", "(340)", "(360)", "(390)",
                   "(400)", "(1,490)"],
                  ["Financing activities", "16,960", "(380)", "(380)",
                   "(10)", "16,190"],
                  {"cells": ["Net change in cash", "15,180", "(1,620)",
                             "(1,300)", "(600)", "11,660"],
                   "style": "total"}]},
        {"heading": "Deferred revenue", "kind": "figure", "weight": 0.95,
         "min_pages": 4, "height": 150, "charts": [{"type": "bars",
          "title": "Deferred revenue at quarter end", "subtitle": "$k",
          "format": "{:,.0f}",
          "categories": ["Q4 25", "Q1 26", "Q2 26", "Q3 26", "Q4 26"],
          "series": [{"name": "Deferred revenue",
                      "values": [3840, 4710, 5120, 5390, 6820],
                      "colors": [4, 0, 0, 0, 0]}]}]},
        {"heading": "Reconciliation to the balance sheet", "kind": "table",
         "whole": True, "weight": 1.0, "min_pages": 4,
         "columns": [("$ thousands", 3), ("31 Dec 2026", 1, "end"),
                     ("31 Dec 2025", 1, "end")],
         "rows": [["Bank accounts", "4,120", "3,410"],
                  ["Money market funds", "14,850", "3,900"],
                  {"cells": ["Cash and cash equivalents", "18,970",
                             "7,310"], "style": "total"}]},
    ],
}
