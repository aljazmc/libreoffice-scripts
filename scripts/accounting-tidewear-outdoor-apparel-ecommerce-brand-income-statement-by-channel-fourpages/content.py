"""Income Statement by Channel of Tidewear: the business and everything the
document could say. The typesetting keeps what fits into four pages, the
most important first."""

BUSINESS = {
    "name": "Tidewear",
    "author": "Tidewear Outdoor Ltd, finance",
}

CHANNELS = ["Web shop", "Marketplaces", "Wholesale"]
# £k by channel
REVENUE = [3_120, 1_480, 1_260]
RETURNS = [-410, -236, -38]
COGS = [-1_090, -598, -702]
FULFILMENT = [-322, -0, -61]          # pick, pack, postage
MARKETPLACE_FEES = [0, -246, 0]
PAYMENT_FEES = [-58, 0, -6]
MARKETING = [-612, -188, -54]
SHARED = [("Design and product team", -426),
          ("Warehouse rent and staff", -268),
          ("Head office and finance", -301),
          ("Depreciation", -64)]
INTEREST, TAX = -38, -27


def k(value):
    return f"({-value:,})" if value < 0 else f"{value:,}" if value else "—"


def add(*rows):
    return [sum(v) for v in zip(*rows)]


NET_REVENUE = add(REVENUE, RETURNS)
GROSS = add(NET_REVENUE, COGS)
CONTRIB1 = add(GROSS, FULFILMENT, MARKETPLACE_FEES, PAYMENT_FEES)
CONTRIB2 = add(CONTRIB1, MARKETING)
SHARED_TOTAL = sum(v for _, v in SHARED)
EBITDA = sum(CONTRIB2) + SHARED_TOTAL + 64
PBT = EBITDA - 64 + INTEREST
PROFIT = PBT + TAX


def line(label, values, style="indent", total=True):
    cells = [label] + [k(v) for v in values]
    cells.append(k(sum(values)) if total else "")
    return {"cells": cells, "style": style}


COLUMNS = [("£ thousands", 2.6)] + [(c, 1, "end") for c in CHANNELS] + [
    ("Total", 1, "end")]

DOCUMENT = {
    "title": "Income Statement by Channel",
    "subtitle": "Year ended 31 January 2028 · contribution by sales "
                "channel, shared costs below the line",
    "meta": [("Company", "Tidewear Outdoor Ltd"),
             ("Net revenue", f"£{sum(NET_REVENUE) / 1000:.2f}m"),
             ("Contribution", f"£{sum(CONTRIB2) / 1000:.2f}m"),
             ("Profit after tax", f"£{PROFIT}k"),
             ("Year", "FY 2027/28")],
    "sections": [
        {"heading": "Statement", "kind": "table", "whole": True,
         "weight": 0.1, "columns": COLUMNS,
         "rows": [line("Gross sales", REVENUE),
                  line("Returns and refunds", RETURNS),
                  line("Net revenue", NET_REVENUE, "subtotal"),
                  line("Cost of goods sold", COGS),
                  line("Gross profit", GROSS, "subtotal"),
                  {"cells": ["Gross margin"] + [
                      f"{g / n:.0%}" for g, n in zip(GROSS, NET_REVENUE)]
                   + [f"{sum(GROSS) / sum(NET_REVENUE):.0%}"],
                   "style": "muted"},
                  line("Fulfilment and postage", FULFILMENT),
                  line("Marketplace fees", MARKETPLACE_FEES),
                  line("Payment fees", PAYMENT_FEES),
                  line("Contribution before marketing", CONTRIB1,
                       "subtotal"),
                  line("Marketing", MARKETING),
                  line("Channel contribution", CONTRIB2, "highlight"),
                  {"cells": ["Contribution margin"] + [
                      f"{c / n:.0%}" for c, n in zip(CONTRIB2,
                                                     NET_REVENUE)]
                   + [f"{sum(CONTRIB2) / sum(NET_REVENUE):.0%}"],
                   "style": "muted"}]
         + [{"cells": [n, "", "", "", k(v)], "style": "indent"}
            for n, v in SHARED]
         + [{"cells": ["Operating profit", "", "", "",
                       k(sum(CONTRIB2) + SHARED_TOTAL)],
             "style": "subtotal"},
            {"cells": ["Interest", "", "", "", k(INTEREST)],
             "style": "indent"},
            {"cells": ["Tax", "", "", "", k(TAX)], "style": "indent"},
            {"cells": ["Profit for the year", "", "", "", k(PROFIT)],
             "style": "total"}]},
        {"heading": "Channels side by side", "kind": "figure",
         "weight": 0.2, "height": {1: 160, 2: 180, 4: 190},
         "charts": [{"type": "bars", "horizontal": True, "stacked": True,
          "inside": True, "format": "£{:,.0f}k", "values": False,
          "subtitle": "where each channel's net revenue goes, £k",
          "categories": CHANNELS,
          "series": [{"name": "Cost of goods", "color": 4,
                      "values": [-v for v in COGS]},
                     {"name": "Fees and fulfilment", "color": 2,
                      "values": [-(a + b + c) for a, b, c in zip(
                          FULFILMENT, MARKETPLACE_FEES, PAYMENT_FEES)]},
                     {"name": "Marketing", "color": 1,
                      "values": [-v for v in MARKETING]},
                     {"name": "Contribution", "color": "good",
                      "values": CONTRIB2}]}]},
        {"heading": "Margins", "kind": "figure", "weight": 0.3,
         "min_pages": 2, "charts": [{"type": "gauges", "items": [
             {"label": c, "value": v / n * 100, "max": 50,
              "target": 25, "status": i,
              "display": f"{v / n:.0%}", "note": "contribution margin"}
             for i, (c, v, n) in enumerate(zip(CHANNELS, CONTRIB2,
                                                NET_REVENUE))]}]},
        {"heading": "Commentary", "kind": "entries", "weight": 0.4,
         "step": 0.2, "inner": 0.1, "min_pages": 2, "entries": [
             {"title": "Web shop: the biggest and the most expensive to "
                       "run", "text": [
                 "Returns of 13 % and paid social ads take a quarter of "
                 "every pound, but the full-price mix keeps the gross "
                 "margin at 60 %."]},
             {"title": "Marketplaces: growth with a toll", "text": [
                 "Marketplace fees of 20 % and heavy discounting; "
                 "useful for clearing last season's colours."]},
             {"title": "Wholesale: the quiet winner", "text": [
                 "Lower gross margin, but almost no returns, no "
                 "marketing and orders in bulk. Twelve outdoor shops "
                 "took the autumn range."]},
         ]},
        {"heading": "Revenue by quarter", "kind": "figure",
         "weight": 0.5, "min_pages": 4, "height": 160, "charts": [{
             "type": "bars", "stacked": True, "subtitle": "£k, gross",
             "format": "{:,.0f}",
             "categories": ["Q1 Feb–Apr", "Q2 May–Jul", "Q3 Aug–Oct",
                            "Q4 Nov–Jan"],
             "series": [{"name": c, "values": v} for c, v in zip(
                 CHANNELS, [[560, 690, 820, 1050], [270, 300, 380, 530],
                            [180, 120, 640, 320]])]}]},
        {"heading": "Shared costs", "kind": "figure", "weight": 0.6,
         "min_pages": 4, "height": 140, "charts": [{"type": "donut",
          "segments": [(n, -v) for n, v in SHARED],
          "format": "£{:,.0f}k", "center": (f"£{-SHARED_TOTAL:,}k",
                                            "not allocated")}]},
        {"heading": "Year on year", "kind": "table", "whole": True,
         "weight": 0.7, "min_pages": 4,
         "badges": {"Better": "good", "Worse": "bad"},
         "columns": [("Measure", 2.4), ("FY 2027/28", 1, "end"),
                     ("FY 2026/27", 1, "end"), ("", 0.9, "center")],
         "rows": [["Net revenue", f"£{sum(NET_REVENUE):,}k", "£4,612k",
                   "Better"],
                  ["Gross margin",
                   f"{sum(GROSS) / sum(NET_REVENUE):.1%}", "57.4%",
                   "Worse"],
                  ["Return rate, web shop", "13.1 %", "14.8 %", "Better"],
                  ["Marketing ÷ revenue",
                   f"{-sum(MARKETING) / sum(NET_REVENUE):.1%}", "17.9%",
                   "Better"],
                  ["Wholesale accounts", "12", "7", "Better"]]},
        {"heading": "How costs are assigned", "kind": "text",
         "weight": 0.8, "step": 0.3, "min_pages": 4, "paragraphs": [
             "Costs that a channel causes are charged to it: the goods "
             "it sells, its returns, fees, postage and the marketing "
             "aimed at it. Costs that would not change if a channel "
             "closed, such as the design team, the warehouse lease and "
             "head office, stay below the contribution line and are not "
             "allocated.",
         ]},
        {"heading": "Contribution per order", "kind": "figure",
         "weight": 0.9, "min_pages": 4, "height": 150, "charts": [{
             "type": "bars", "title": "Average order and its contribution",
             "subtitle": "£", "format": "£{:,.0f}",
             "categories": CHANNELS,
             "series": [{"name": "Net order value", "color": 4,
                         "values": [79, 61, 1_420]},
                        {"name": "Contribution", "values": [18, 10, 464]}]}]},
        {"heading": "Board questions", "kind": "bullets", "weight": 1.0,
         "step": 0.1, "min_pages": 4, "items": [
             "Should wholesale grow faster than the web shop, given its "
             "margin after costs?",
             "Do we keep the second marketplace, which makes 4 % "
             "contribution after its fees?",
             "Can the web shop's returns fall below 10 % with better "
             "size guidance?",
         ]},
    ],
}
