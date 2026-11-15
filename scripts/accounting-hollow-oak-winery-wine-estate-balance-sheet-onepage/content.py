"""Balance Sheet of Hollow Oak Estate: the business and everything the document
could say. The typesetting keeps what fits into one page, the most important
first."""

BUSINESS = {
    "name": "Hollow Oak Estate",
    "author": "Hollow Oak Estate Ltd, prepared by Clare Ashdown ACA",
}


def k(value):
    return f"({-value:,})" if value < 0 else f"{value:,}"


# € thousands: 30 June 2027, 30 June 2026
FIXED = [("Land and buildings", 2840, 2870),
         ("Vineyards (bearer plants)", 612, 588),
         ("Winery equipment and barrels", 734, 701),
         ("Vehicles and tractors", 118, 96)]
CURRENT = [("Wine in barrel and tank", 1186, 1042),
           ("Bottled wine", 742, 688),
           ("Dry goods: glass, corks, labels", 96, 88),
           ("Trade receivables", 214, 187),
           ("Prepayments", 38, 31),
           ("Cash at bank", 162, 241)]
CURRENT_LIAB = [("Trade payables", -168, -152),
                ("Excise duty and VAT", -94, -86),
                ("Accruals", -57, -49),
                ("Bank loan, due within a year", -120, -120)]
LONG_LIAB = [("Bank loan, due after a year", -1080, -1200),
             ("Deferred tax", -146, -131)]
EQUITY = [("Share capital", 500, 500),
          ("Revaluation reserve", 1240, 1240)]


def total(lines, i):
    return sum(line[i] for line in lines)


TOTALS = {}
for i in (1, 2):
    fixed, current = total(FIXED, i), total(CURRENT, i)
    cl, ll = total(CURRENT_LIAB, i), total(LONG_LIAB, i)
    net = fixed + current + cl + ll
    TOTALS[i] = dict(fixed=fixed, current=current, cl=cl, ll=ll,
                     nca=current + cl, net=net,
                     retained=net - total(EQUITY, i))
EQUITY.append(("Retained earnings", TOTALS[1]["retained"],
               TOTALS[2]["retained"]))


def lines(items, detail=1):
    return [{"cells": [name, k(a), k(b)], "style": "indent",
             "min_pages": detail} for name, a, b in items]


def line(name, key, style):
    return {"cells": [name, k(TOTALS[1][key]), k(TOTALS[2][key])],
            "style": style}


COLUMNS = [("€ thousands", 3.2), ("30 June 2027", 1, "end"),
           ("30 June 2026", 1, "end")]

DOCUMENT = {
    "title": "Balance Sheet",
    "subtitle": "Hollow Oak Estate Ltd · as at 30 June 2027",
    "meta": [("Company", "Hollow Oak Estate Ltd"),
             ("Year end", "30 June 2027"),
             ("Net assets", f"€{TOTALS[1]['net'] / 1000:.2f}m"),
             ("Status", "Audited")],
    "sections": [
        {"heading": "Statement of financial position", "kind": "table",
         "whole": True, "weight": 0.1, "columns": COLUMNS,
         "rows": [{"cells": ["Fixed assets", "", ""], "style": "section"}]
         + lines(FIXED)
         + [line("", "fixed", "subtotal"),
            {"cells": ["Current assets", "", ""], "style": "section"}]
         + lines(CURRENT[:3], 2)
         + [{"cells": ["Stock of wine and dry goods",
                       k(sum(c[1] for c in CURRENT[:3])),
                       k(sum(c[2] for c in CURRENT[:3]))],
             "style": "indent", "max_pages": 1}]
         + lines(CURRENT[3:])
         + [line("", "current", "subtotal"),
            {"cells": ["Creditors due within one year", "", ""],
             "style": "section"}]
         + lines(CURRENT_LIAB)
         + [line("Net current assets", "nca", "subtotal"),
            {"cells": ["Creditors due after one year", "", ""],
             "style": "section"}]
         + lines(LONG_LIAB)
         + [line("Net assets", "net", "total"),
            {"cells": ["Capital and reserves", "", ""],
             "style": "section"}]
         + lines(EQUITY)
         + [line("Total equity", "net", "total")]},
        {"heading": "What the estate is made of", "kind": "figure",
         "weight": 0.2, "height": {1: 130, 2: 160, 4: 170},
         "widths": [1, 1], "charts": [
             {"type": "donut", "title": "Assets",
              "format": "€{:,.0f}k", "center": (
                  f"€{(TOTALS[1]['fixed'] + TOTALS[1]['current']) / 1e3:.1f}m",
                  "total assets"),
              "segments": [("Land and buildings", 2840),
                           ("Wine and dry goods", 2024),
                           ("Vines", 612), ("Equipment", 852),
                           ("Debtors and cash", 414)]},
             {"type": "bars", "horizontal": True, "stacked": True,
              "title": "Financed by", "subtitle": "€k",
              "format": "{:,.0f}", "values": False, "inside": True,
              "categories": ["2027", "2026"],
              "series": [{"name": "Equity", "values": [
                  TOTALS[1]["net"], TOTALS[2]["net"]]},
                         {"name": "Bank loan", "color": 1,
                          "values": [1200, 1320]},
                         {"name": "Suppliers and tax", "color": 4,
                          "values": [465, 418]}]},
         ]},
        {"heading": "Ratios", "kind": "figure", "weight": 0.3,
         "min_pages": 2, "charts": [{"type": "gauges", "items": [
             {"label": "Current ratio",
              "value": TOTALS[1]["current"] / -TOTALS[1]["cl"], "max": 6,
              "target": 2, "status": "good",
              "display": f"{TOTALS[1]['current'] / -TOTALS[1]['cl']:.1f}×",
              "note": "current assets ÷ liabilities"},
             {"label": "Quick ratio",
              "value": 414 / -TOTALS[1]["cl"], "max": 2, "target": 1,
              "status": "warn",
              "display": f"{414 / -TOTALS[1]['cl']:.2f}×",
              "note": "without the wine"},
             {"label": "Gearing", "value": 1200 / TOTALS[1]["net"] * 100,
              "max": 100, "target": 50, "status": "good",
              "display": f"{1200 / TOTALS[1]['net']:.0%}",
              "note": "loan ÷ equity"},
             {"label": "Stock cover", "value": 31, "max": 48,
              "status": 0, "display": "31 mo", "note": "of sales in "
                                                       "the cellar"}]}]},
        {"heading": "Notes", "kind": "entries", "weight": 0.4,
         "step": 0.15, "inner": 0.05, "min_pages": 2, "entries": [
             {"title": "1. Wine stock", "text": [
                 "Wine is valued at the lower of cost and net realisable "
                 "value. Cost includes the grapes, the cellar labour and "
                 "a share of the winery overheads; the 2025 and 2026 "
                 "vintages are still in barrel."]},
             {"title": "2. Vineyards", "text": [
                 "Vines are bearer plants, carried at cost less "
                 "depreciation over 30 years. The 2.1 ha of Pinot Noir "
                 "planted in 2024 are not depreciated until their first "
                 "commercial harvest in 2027."]},
             {"title": "3. Land and buildings", "text": [
                 "Revalued to €2.9m in 2023 by Hartley & Sons, chartered "
                 "surveyors; the revaluation reserve is not "
                 "distributable."]},
             {"title": "4. Bank loan", "text": [
                 "A €1.8m loan from Agri Bank, secured on the land, "
                 "repaid in equal instalments of €120k a year until "
                 "2036 at a fixed 4.1 %."]},
         ]},
        {"heading": "Movements in the year", "kind": "figure",
         "weight": 0.5, "min_pages": 4, "height": 175, "charts": [{
             "type": "waterfall", "format": "{:,.0f}",
             "subtitle": "€k, net assets", "total_color": 0,
             "steps": [("1 July 2026", TOTALS[2]["net"]),
                       ("Profit for the year",
                        TOTALS[1]["net"] - TOTALS[2]["net"] + 60),
                       ("Dividend paid", -60),
                       ("30 June 2027", None)]}]},
        {"heading": "Stock of wine", "kind": "table", "whole": True,
         "weight": 0.6, "min_pages": 4,
         "columns": [("Vintage and wine", 2.6), ("Litres", 1, "end"),
                     ("Bottles", 1, "end"), ("Cost €k", 1, "end")],
         "rows": [["2026 Bacchus, tank", "18,400", "—", "142"],
                  ["2026 Pinot Noir, barrel", "21,600", "—", "318"],
                  ["2025 Pinot Noir, barrel", "19,800", "—", "336"],
                  ["2025 Traditional method, on lees", "32,200", "—",
                   "390"],
                  ["Bottled, all wines", "—", "71,300", "742"],
                  {"cells": ["Total wine", "92,000", "71,300", "1,928"],
                   "style": "total"}]},
        {"heading": "Five years", "kind": "figure", "weight": 0.7,
         "min_pages": 4, "height": 150, "charts": [{"type": "line",
          "subtitle": "€k at 30 June", "x": ["2023", "2024", "2025",
                                             "2026", "2027"],
          "format": "{:,.0f}", "end_labels": True,
          "series": [{"name": "Net assets", "values": [4180, 4410, 4590,
                                                       TOTALS[2]["net"],
                                                       TOTALS[1]["net"]]},
                     {"name": "Bank loan", "color": 1, "dash": True,
                      "values": [1680, 1560, 1440, 1320, 1200]}]}]},
        {"heading": "Approval", "kind": "text", "weight": 0.8,
         "step": 0.2, "min_pages": 4, "paragraphs": [
             "These financial statements were approved by the board on "
             "18 October 2027 and signed on its behalf by Hugh Marlow, "
             "director. The auditor's report, by Penrose Audit LLP, is "
             "unqualified."]},
        {"heading": "Changes in equity", "kind": "table", "whole": True,
         "weight": 0.85, "min_pages": 4,
         "columns": [("€ thousands", 2.6), ("Share capital", 1, "end"),
                     ("Revaluation", 1, "end"), ("Retained", 1, "end"),
                     ("Total", 1, "end")],
         "rows": [["At 1 July 2026", "500", "1,240",
                   k(TOTALS[2]["retained"]), k(TOTALS[2]["net"])],
                  ["Profit for the year", "", "",
                   k(TOTALS[1]["net"] - TOTALS[2]["net"] + 60),
                   k(TOTALS[1]["net"] - TOTALS[2]["net"] + 60)],
                  ["Dividend paid", "", "", "(60)", "(60)"],
                  {"cells": ["At 30 June 2027", "500", "1,240",
                             k(TOTALS[1]["retained"]),
                             k(TOTALS[1]["net"])], "style": "total"}]},
        {"heading": "Loan repayments", "kind": "figure", "weight": 0.9,
         "min_pages": 4, "height": 150, "charts": [{"type": "bars",
          "title": "Loan outstanding at 30 June", "subtitle": "€k",
          "format": "{:,.0f}",
          "categories": [str(y) for y in range(2027, 2037)],
          "series": [{"name": "Loan", "values": [1200 - 120 * i
                                                 for i in range(10)],
                      "colors": [0] + [4] * 9}]}]},
        {"heading": "Working capital", "kind": "figure", "weight": 0.95,
         "min_pages": 4, "charts": [{"type": "kpis", "tiles": [
             {"label": "Debtor days", "value": "38", "status": 0,
              "note": "trade customers"},
             {"label": "Creditor days", "value": "44", "status": 1,
              "note": "suppliers"},
             {"label": "Wine stock", "value": "€1.9m", "status": 2,
              "note": "+€0.2m, longer ageing"},
             {"label": "Cash", "value": "€162k", "status": "warn",
              "note": "−€79k after barrels"}]}]},
    ],
}
