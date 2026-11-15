"""Purchase Order of Hollow Oak Estate: the business and everything the
document could say. The typesetting keeps what fits into four pages, the
most important first."""

BUSINESS = {
    "name": "Hollow Oak Estate",
    "author": "Hollow Oak Estate Ltd, winery",
}

# item, quantity, unit price €
LINES = [("Barrique 225 l, French oak, medium toast, Allier", 12, 945.0),
         ("Barrique 225 l, French oak, medium-plus toast, Vosges", 8,
          965.0),
         ("Puncheon 500 l, French oak, light toast", 4, 1620.0),
         ("Silicone bungs, 52 mm", 24, 6.5),
         ("Barrel racks, two-barrel steel", 12, 118.0)]
DISCOUNT = 0.05  # early-order discount on barrels
FREIGHT = 640.0
VAT = 0.20


def eur(value):
    return f"€{value:,.2f}"


GOODS = sum(q * p for _, q, p in LINES)
BARRELS = sum(q * p for name, q, p in LINES if "oak" in name)
DISC = round(BARRELS * DISCOUNT, 2)
NET = GOODS - DISC + FREIGHT
TAX = round(NET * VAT, 2)
TOTAL = NET + TAX

DOCUMENT = {
    "title": "Purchase Order PO-2027-063",
    "eyebrow": "Hollow Oak Estate · winery purchasing",
    "subtitle": "Oak barrels for the 2027 vintage, delivered before the "
                "harvest",
    "meta": [("PO number", "PO-2027-063"), ("Date", "12 Apr 2027"),
             ("Supplier", "Tonnellerie Marchand"),
             ("Deliver by", "15 Aug 2027"), ("Total", eur(TOTAL))],
    "sections": [
        {"kind": "table", "look": "plain", "header": False, "whole": True,
         "weight": 0.05, "columns": [("", 1), ("", 1)],
         "rows": [["**Supplier** Tonnellerie Marchand SAS",
                   "**Deliver to** Hollow Oak Estate, the barrel hall"],
                  ["Route de Cognac, 16100 Cognac, France",
                   "Oak Lane, Ditchling BN6 8TR, England"],
                  ["Quote Q-27-0417 of 2 April 2027",
                   "Goods in: Mon – Fri, 08:00 – 15:00"],
                  ["Contact: Juliette Marchand",
                   "Contact: Sam Okoro, cellar master"]]},
        {"heading": "Order lines", "kind": "table", "whole": True,
         "weight": 0.1,
         "columns": [("Line", 0.5), ("Description", 3.6),
                     ("Qty", 0.6, "end"), ("Unit price", 1, "end"),
                     ("Amount", 1.1, "end")],
         "rows": [[str(i + 1), name, str(q), eur(p), eur(q * p)]
                  for i, (name, q, p) in enumerate(LINES)]
         + [{"cells": ["", "Goods", "", "", eur(GOODS)],
             "style": "subtotal"},
            {"cells": ["", "Early-order discount, 5 % on barrels", "", "",
                       f"−{eur(DISC)}"], "style": "muted"},
            {"cells": ["", "Freight, insured, to Ditchling", "", "",
                       eur(FREIGHT)], "style": "indent"},
            {"cells": ["", "Net", "", "", eur(NET)], "style": "subtotal"},
            {"cells": ["", "Import VAT at 20 % (paid at the border)", "",
                       "", eur(TAX)], "style": "indent"},
            {"cells": ["", "Total commitment", "", "", eur(TOTAL)],
             "style": "total"}]},
        {"heading": "Approval", "kind": "table", "weight": 0.2,
         "whole": True, "badges": {"Approved": "good", "Within budget":
                                   "good"},
         "columns": [("Step", 1.6), ("By", 1.8), ("Date", 1),
                     ("", 1.2, "center")],
         "rows": [["Requested", "Sam Okoro, cellar master", "8 Apr",
                   "Approved"],
                  ["Budget check", "Clare Ashdown, finance", "10 Apr",
                   "Within budget"],
                  ["Authorised (over €10k)", "Hugh Marlow, director",
                   "12 Apr", "Approved"]]},
        {"heading": "Terms", "kind": "bullets", "weight": 0.3,
         "step": 0.1, "items": [
             "Payment 30 % with order, 70 % within 30 days of delivery, "
             "in euros.",
             "Barrels to be delivered wrapped, with toasting certificates "
             "and the forest of origin for each.",
             "Please quote PO-2027-063 on every invoice and delivery "
             "note.",
         ]},
        {"heading": "Budget", "kind": "figure", "weight": 0.4,
         "min_pages": 2, "height": 120, "charts": [{"type": "progress",
          "format": "€{:,.0f}", "max": 40000, "items": [
              {"label": "Cooperage budget 2027", "value": 40000,
               "status": 4},
              {"label": "Committed before this order", "value": 9800,
               "status": 3},
              {"label": "This order, net", "value": NET, "status": 0},
              {"label": "Left after this order",
               "value": 40000 - 9800 - NET, "status": "good"}]}]},
        {"heading": "Delivery schedule", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": 120, "charts": [{"type": "timeline",
          "start": 0, "end": 22, "label_width": 100,
          "ticks": [(0, "Apr"), (4, "May"), (8, "Jun"), (13, "Jul"),
                    (17, "Aug"), (22, "Sep")],
          "events": [{"at": 0.4, "label": "Order and deposit",
                      "sub": "12 Apr", "status": "done"},
                     {"at": 7, "label": "Toasting", "sub": "June"},
                     {"at": 14, "label": "Shipped from Cognac",
                      "sub": "late July"},
                     {"at": 17, "label": "Delivered", "sub": "by 15 Aug"},
                     {"at": 21, "label": "Harvest", "sub": "September"}]}]},
        {"heading": "Payments", "kind": "table", "weight": 0.6,
         "whole": True, "min_pages": 2,
         "columns": [("Instalment", 2.4), ("Due", 1.4),
                     ("Amount", 1, "end")],
         "rows": [["Deposit, 30 % of the net", "with order",
                   eur(round(NET * 0.3, 2))],
                  ["Balance, 70 % of the net", "30 days after delivery",
                   eur(round(NET * 0.7, 2))],
                  ["Import VAT", "at the border, reclaimed in Q3",
                   eur(TAX)]]},
        {"heading": "Quotes compared", "kind": "table", "weight": 0.7,
         "whole": True, "min_pages": 4,
         "badges": {"Chosen": "good"},
         "columns": [("Cooperage", 2), ("Barrique price", 1, "end"),
                     ("Lead time", 1, "center"),
                     ("Previous barrels", 2), ("", 0.8, "center")],
         "rows": [["Tonnellerie Marchand", "€945", "14 weeks",
                   "Used since 2019, consistent toast", "Chosen"],
                  ["Seguin Frères", "€920", "18 weeks",
                   "Two leaking barrels in 2025", ""],
                  ["Hungarian Oak Co.", "€690", "10 weeks",
                   "Not tried; strong vanilla", ""]]},
        {"heading": "Barrel programme", "kind": "figure", "weight": 0.8,
         "min_pages": 4, "height": 150, "widths": [3, 2], "charts": [
             {"type": "bars", "stacked": True, "title": "Barrels in the "
              "hall by age", "categories": ["2025", "2026", "2027"],
              "series": [{"name": "New", "values": [18, 20, 24]},
                         {"name": "1 – 2 years", "color": 1,
                          "values": [34, 36, 38]},
                         {"name": "3 – 5 years", "color": 4,
                          "values": [52, 48, 44]}]},
             {"type": "donut", "title": "This order",
              "segments": [("Allier", 12), ("Vosges", 8),
                           ("Puncheons", 4)],
              "format": "{:.0f}", "center": ("24", "vessels")},
         ]},
        {"heading": "Specification", "kind": "tags", "weight": 0.9,
         "step": 0.1, "min_pages": 4, "items": [
             ("Wood", "French oak, air-dried 36 months, fine grain"),
             ("Toast", "medium and medium-plus, as per line; heads "
                       "untoasted"),
             ("Use", "Pinot Noir from the 2027 vintage, 11 months"),
             ("Checks", "pressure test on arrival; rejects collected at "
                        "the supplier's cost"),
         ]},
        {"heading": "Accounting", "kind": "text", "weight": 1.0,
         "step": 0.2, "min_pages": 4, "paragraphs": [
             "Barrels are capitalised as winery equipment and "
             "depreciated over five years; bungs are expensed. The "
             "deposit is booked as a prepayment until delivery. Import "
             "VAT is reclaimed on the Q3 return under postponed "
             "accounting.",
         ]},
        {"heading": "Supplier history", "kind": "figure", "weight": 1.1,
         "min_pages": 4, "height": 150, "widths": [3, 2], "charts": [
             {"type": "bars", "title": "Spend with Tonnellerie Marchand",
              "subtitle": "€k, net", "format": "{:,.1f}",
              "categories": ["2023", "2024", "2025", "2026", "2027"],
              "series": [{"name": "Spend", "values": [17.2, 19.8, 21.4,
                                                      23.9, NET / 1000],
                          "colors": [4, 4, 4, 4, 0]}]},
             {"type": "gauges", "items": [
                 {"label": "On-time deliveries", "value": 96, "max": 100,
                  "target": 90, "status": "good", "display": "96 %",
                  "note": "last 5 years"}]},
         ]},
        {"heading": "Three-way match", "kind": "table", "whole": True,
         "weight": 1.2, "min_pages": 4,
         "columns": [("Document", 1.8), ("Reference", 1.4),
                     ("Checked against", 2.2), ("By", 1)],
         "rows": [["Purchase order", "PO-2027-063", "Quote Q-27-0417",
                   "Finance"],
                  ["Goods received note", "to follow", "Order lines and "
                   "the pressure test", "Cellar"],
                  ["Supplier invoice", "to follow", "Order and goods "
                   "received", "Finance"],
                  ["Payment", "to follow", "Matched invoice, two "
                   "signatures", "Director"]]},
        {"heading": "Goods-in check", "kind": "bullets", "weight": 1.3,
         "step": 0.1, "min_pages": 4, "items": [
             "Count the vessels against the delivery note and the order.",
             "Fill each barrel with water for 24 hours; mark any that "
             "weep.",
             "Record the forest, toast and cooper's number of each "
             "barrel in the barrel book.",
             "Report rejects to the supplier within 7 days.",
         ]},
    ],
}
