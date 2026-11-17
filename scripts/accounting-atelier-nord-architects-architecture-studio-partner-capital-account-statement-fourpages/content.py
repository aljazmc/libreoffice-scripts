"""Partner Capital Account Statement of Atelier Nord: the business and
everything the document could say. The typesetting keeps what fits into four
pages, the most important first."""

BUSINESS = {
    "name": "Atelier Nord",
    "author": "Atelier Nord Architects LLP, for the members",
}

PROFIT = 412_600         # profit available for members, year to 5 Apr
SALARIES = {"Ingrid Lund": 60_000, "Erik Nord": 60_000,
            "Oskar Berg": 30_000}
INTEREST_RATE = 0.04
CAPITAL = {"Ingrid Lund": 120_000, "Erik Nord": 120_000,
           "Oskar Berg": 40_000}
SHARES = {"Ingrid Lund": 0.42, "Erik Nord": 0.42, "Oskar Berg": 0.16}
INTEREST = {m: CAPITAL[m] * INTEREST_RATE for m in CAPITAL}
RESIDUAL = PROFIT - sum(SALARIES.values()) - sum(INTEREST.values())
ALLOC = {m: SALARIES[m] + INTEREST[m] + RESIDUAL * SHARES[m]
         for m in CAPITAL}

MEMBER = "Ingrid Lund"
OPENING_CURRENT = 18_420
DRAWINGS = 9_500 * 12
TAX_RESERVE = 61_300
PENSION = 12_000
CLOSING_CURRENT = (OPENING_CURRENT + ALLOC[MEMBER] - DRAWINGS
                   - TAX_RESERVE - PENSION)


def gbp(value):
    return f"({-value:,.0f})" if value < 0 else f"{value:,.0f}"


DOCUMENT = {
    "title": "Partner Capital Account Statement",
    "subtitle": f"{MEMBER} · year ended 5 April 2027 · prepared under the "
                "members' agreement of 1 May 2019",
    "meta": [("Member", MEMBER), ("Profit share", f"{SHARES[MEMBER]:.0%}"),
             ("Allocated", f"£{ALLOC[MEMBER]:,.0f}"),
             ("Capital", f"£{CAPITAL[MEMBER]:,.0f}"),
             ("Current account", f"£{CLOSING_CURRENT:,.0f}")],
    "sections": [
        {"heading": "Current account", "kind": "table", "whole": True,
         "weight": 0.1, "columns": [("£", 3.6), ("Amount", 1, "end")],
         "rows": [["Balance at 6 April 2026", gbp(OPENING_CURRENT)],
                  {"cells": ["Share of profit for the year",
                             gbp(ALLOC[MEMBER])], "style": "indent"},
                  {"cells": ["Monthly drawings, £9,500 × 12",
                             gbp(-DRAWINGS)], "style": "indent"},
                  {"cells": ["Transfer to the tax reserve",
                             gbp(-TAX_RESERVE)], "style": "indent"},
                  {"cells": ["Pension contributions paid by the firm",
                             gbp(-PENSION)], "style": "indent"},
                  {"cells": ["Balance at 5 April 2027",
                             gbp(CLOSING_CURRENT)], "style": "total"}]},
        {"heading": "Capital account", "kind": "table", "whole": True,
         "weight": 0.2, "columns": [("£", 3.6), ("Amount", 1, "end")],
         "rows": [["Fixed capital at 6 April 2026", gbp(CAPITAL[MEMBER])],
                  ["Introduced in the year", "0"],
                  {"cells": ["Fixed capital at 5 April 2027",
                             gbp(CAPITAL[MEMBER])], "style": "total"}]},
        {"heading": "How the profit was shared", "kind": "table",
         "whole": True, "weight": 0.3,
         "columns": [("£", 2.4)] + [(m, 1, "end") for m in CAPITAL]
         + [("Total", 1, "end")],
         "rows": [{"cells": ["Salaries"] + [gbp(SALARIES[m])
                                           for m in CAPITAL]
                   + [gbp(sum(SALARIES.values()))], "style": "indent"},
                  {"cells": ["Interest on capital at 4 %"]
                   + [gbp(INTEREST[m]) for m in CAPITAL]
                   + [gbp(sum(INTEREST.values()))], "style": "indent"},
                  {"cells": ["Residual profit, 42 : 42 : 16"]
                   + [gbp(RESIDUAL * SHARES[m]) for m in CAPITAL]
                   + [gbp(RESIDUAL)], "style": "indent"},
                  {"cells": ["Total allocated"] + [gbp(ALLOC[m])
                                                   for m in CAPITAL]
                   + [gbp(PROFIT)], "style": "total"}]},
        {"heading": "Your share", "kind": "figure", "weight": 0.4,
         "height": 150, "widths": [2, 3], "charts": [
             {"type": "donut", "title": "Profit by member",
              "segments": [(m, ALLOC[m]) for m in CAPITAL],
              "format": "£{:,.0f}", "center": (f"£{PROFIT / 1000:.0f}k",
                                               "profit")},
             {"type": "waterfall", "title": "Your current account",
              "format": "{:,.0f}", "subtitle": "£",
              "axis_format": "{:,.0f}", "total_color": 0,
              "steps": [("6 Apr 2026", OPENING_CURRENT),
                        ("Profit", ALLOC[MEMBER]), ("Drawings", -DRAWINGS),
                        ("Tax reserve", -TAX_RESERVE),
                        ("Pension", -PENSION), ("5 Apr 2027", None)]},
         ]},
        {"heading": "Tax", "kind": "text", "weight": 0.5, "step": 0.3,
         "min_pages": 2, "paragraphs": [
             "As a member of an LLP you are taxed as self-employed on "
             f"your share of the profit, £{ALLOC[MEMBER]:,.0f}, whether "
             "or not you draw it. The firm holds a tax reserve for you "
             f"of £{TAX_RESERVE:,.0f} and pays your payments on account "
             "on 31 January and 31 July from it.",
             "The reserve is an estimate at 45 % on income above the "
             "higher-rate threshold plus Class 4 National Insurance; "
             "your own tax return may differ.",
         ]},
        {"heading": "Five years", "kind": "figure", "weight": 0.6,
         "min_pages": 4, "height": 150, "charts": [{"type": "bars",
          "title": "Your profit share and drawings", "subtitle": "£k",
          "format": "{:,.0f}",
          "categories": ["2022/23", "2023/24", "2024/25", "2025/26",
                         "2026/27"],
          "series": [{"name": "Profit share", "values": [
              142, 151, 163, 158, ALLOC[MEMBER] / 1000]},
                     {"name": "Drawings", "color": 4,
                      "values": [96, 102, 108, 108, DRAWINGS / 1000]}]}]},
        {"heading": "Members' agreement", "kind": "entries",
         "weight": 0.7, "step": 0.2, "inner": 0.1, "min_pages": 4,
         "entries": [
             {"title": "Profit sharing", "text": [
                 "First a salary to each member for the work they do, "
                 "then 4 % interest on fixed capital, then the residual "
                 "in fixed shares reviewed every three years."]},
             {"title": "Drawings", "text": [
                 "Monthly drawings are set each April at about 70 % of "
                 "the expected salary and residual share after tax."]},
             {"title": "Capital", "text": [
                 "Fixed capital is repaid over two years after a member "
                 "retires; current account balances within three "
                 "months."]},
         ]},
        {"heading": "Firm's result", "kind": "table", "whole": True,
         "weight": 0.8, "min_pages": 4,
         "columns": [("£", 3), ("2026/27", 1, "end"),
                     ("2025/26", 1, "end")],
         "rows": [["Fee income", "1,612,400", "1,544,900"],
                  ["Staff costs", "(842,300)", "(815,200)"],
                  ["Premises and running costs", "(287,500)",
                   "(276,400)"],
                  ["Professional indemnity insurance", "(70,000)",
                   "(66,300)"],
                  {"cells": ["Profit available for members",
                             gbp(PROFIT), "377,000"], "style": "total"}]},
        {"heading": "Agreed", "kind": "table", "look": "plain",
         "header": False, "whole": True, "weight": 0.9, "min_pages": 4,
         "columns": [("", 1), ("", 1)],
         "rows": [["Ingrid Lund ____________________",
                   "Erik Nord ____________________"],
                  ["Date ____________", "Date ____________"]]},
        {"heading": "Tax reserve", "kind": "table", "whole": True,
         "weight": 0.95, "min_pages": 4,
         "columns": [("£", 3.4), ("Amount", 1, "end")],
         "rows": [["Reserve at 6 April 2026", "38,900"],
                  {"cells": ["Transferred from the current account",
                             gbp(TAX_RESERVE)], "style": "indent"},
                  {"cells": ["Paid: balancing payment 2025/26, 31 Jan",
                             "(21,700)"], "style": "indent"},
                  {"cells": ["Paid: payments on account 2026/27",
                             "(56,800)"], "style": "indent"},
                  {"cells": ["Reserve at 5 April 2027", gbp(
                      38_900 + TAX_RESERVE - 21_700 - 56_800)],
                   "style": "total"}]},
        {"heading": "All members", "kind": "table", "whole": True,
         "weight": 1.0, "min_pages": 4,
         "columns": [("£", 2)] + [(m, 1, "end") for m in CAPITAL],
         "rows": [["Fixed capital"] + [gbp(CAPITAL[m]) for m in CAPITAL],
                  ["Profit allocated"] + [gbp(ALLOC[m]) for m in CAPITAL],
                  ["Drawings"] + [gbp(-d) for d in (114_000, 114_000,
                                                     54_000)],
                  {"cells": ["Share of profit"] + [f"{ALLOC[m] / PROFIT:.0%}"
                                                   for m in CAPITAL],
                   "style": "muted"}]},
        {"heading": "Drawings by month", "kind": "figure",
         "weight": 1.1, "min_pages": 4, "height": 140, "charts": [{
             "type": "line", "subtitle": "£k, cumulative",
             "x": ["Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov",
                   "Dec", "Jan", "Feb", "Mar"], "format": "{:.0f}",
             "series": [{"name": "Drawings", "values": [
                 9.5 * (i + 1) for i in range(12)]},
                        {"name": "Profit earned (estimate)", "color": 1,
                         "dash": True, "values": [
                             round(ALLOC[MEMBER] / 12000 * (i + 1), 1)
                             for i in range(12)]}]}]},
        {"heading": "Notes to the statement", "kind": "bullets",
         "weight": 1.2, "step": 0.1, "min_pages": 4, "items": [
             "Profit is after professional indemnity insurance and "
             "before members' tax, which is each member's own.",
             "Pension contributions of £1,000 a month are paid by the "
             "firm and charged to the member's current account.",
             "Interest on capital is part of the profit allocation, not "
             "an expense of the firm.",
             "The residual shares were last reviewed in April 2025 and "
             "will be reviewed again in April 2028.",
         ]},
        {"heading": "Ratios", "kind": "figure", "weight": 1.3,
         "min_pages": 4, "charts": [{"type": "gauges", "items": [
             {"label": "Profit margin", "value": PROFIT / 1_612_400 * 100,
              "max": 50, "target": 25, "status": "good",
              "display": f"{PROFIT / 1_612_400:.0%}"},
             {"label": "Profit per member", "value": PROFIT / 3 / 1000,
              "max": 200, "status": 0,
              "display": f"£{PROFIT / 3000:.0f}k"},
             {"label": "Drawings ÷ profit", "value": DRAWINGS
              / ALLOC[MEMBER] * 100, "max": 100, "target": 70,
              "status": "warn",
              "display": f"{DRAWINGS / ALLOC[MEMBER]:.0%}"}]}]},
    ],
}
