"""Sales Order Confirmation of Copperline Bicycle Works: the business and
everything the document could say. The typesetting keeps what fits into two
pages, the most important first."""

BUSINESS = {
    "name": "Copperline Bicycle Works",
    "author": "Copperline Bicycle Works Ltd, sales office",
}

# model, size mix, colour, quantity, dealer price ex VAT £
LINES = [("Ridgeline gravel, 105 groupset", "S 4 · M 8 · L 6",
          "Oxide red", 18, 1_046.00),
         ("Ridgeline gravel, GRX Di2", "M 4 · L 4", "Slate", 8, 1_710.00),
         ("Harbour city, hub gear", "S 3 · M 5 · L 2", "Sea green", 10,
          668.00),
         ("Long Mynd touring", "M 2 · L 2", "Copper", 4, 1_215.00)]
DISCOUNT = 0.04   # volume discount for 40 bikes or more
DEPOSIT = 0.30
VAT = 0.20


def gbp(value):
    sign = "−" if value < 0 else ""
    return f"{sign}£{abs(value):,.2f}"


GOODS = sum(q * p for *_, q, p in LINES)
DISC = round(GOODS * DISCOUNT, 2)
CARRIAGE = 240.00
NET = round(GOODS - DISC + CARRIAGE, 2)
TAX = round(NET * VAT, 2)
TOTAL = round(NET + TAX, 2)
BIKES = sum(l[3] for l in LINES)

DOCUMENT = {
    "title": "Sales Order Confirmation",
    "eyebrow": "Copperline Bicycle Works · order SO-28-0142",
    "subtitle": f"{BIKES} bicycles for Spokes & Gears, Bristol · spring "
                "2028 stock order",
    "meta": [("Order", "SO-28-0142"), ("Date", "10 Jan 2028"),
             ("Bicycles", str(BIKES)), ("Total", gbp(TOTAL)),
             ("Deposit due", gbp(round(TOTAL * DEPOSIT, 2)))],
    "sections": [
        {"kind": "table", "look": "plain", "header": False, "whole": True,
         "weight": 0.05, "columns": [("", 1), ("", 1)],
         "rows": [["**Copperline Bicycle Works Ltd**",
                   "**Spokes & Gears Ltd**"],
                  ["Unit 3, Foundry Lane, Shrewsbury SY1 2QE",
                   "41 Gloucester Road, Bristol BS7 8AE"],
                  ["VAT GB 318 7720 45", "Dealer account D-0061"],
                  ["sales@copperline.example", "Your order ref.: SG-118"]]},
        {"heading": "Order", "kind": "table", "whole": True,
         "weight": 0.1,
         "columns": [("Model", 2.4), ("Sizes", 1.5), ("Colour", 1),
                     ("Qty", 0.5, "end"), ("Price", 0.9, "end"),
                     ("Amount", 1, "end")],
         "rows": [[m, s, c, str(q), gbp(p), gbp(q * p)]
                  for m, s, c, q, p in LINES]
         + [{"cells": ["Bicycles", "", "", str(BIKES), "", gbp(GOODS)],
             "style": "subtotal"},
            {"cells": ["Volume discount, 4 % on 40 bicycles or more", "",
                       "", "", "", gbp(-DISC)], "style": "muted"},
            {"cells": ["Delivery by pallet, two drops", "", "", "", "",
                       gbp(CARRIAGE)], "style": "indent"},
            {"cells": ["Net", "", "", "", "", gbp(NET)],
             "style": "subtotal"},
            {"cells": ["VAT at 20 %", "", "", "", "", gbp(TAX)],
             "style": "indent"},
            {"cells": ["Total", "", "", "", "", gbp(TOTAL)],
             "style": "total"}]},
        {"heading": "Payments", "kind": "table", "whole": True,
         "weight": 0.2,
         "columns": [("Instalment", 2.4), ("Due", 1.6),
                     ("Amount", 1, "end")],
         "rows": [["Deposit, 30 %", "by 24 Jan 2028",
                   gbp(round(TOTAL * DEPOSIT, 2))],
                  ["First delivery, balance of drop 1", "on delivery, "
                   "net 30", gbp(round(TOTAL * 0.35, 2))],
                  ["Second delivery, balance of drop 2", "on delivery, "
                   "net 30", gbp(round(TOTAL * 0.35, 2))]]},
        {"heading": "Build slots", "kind": "figure", "weight": 0.3,
         "height": {1: 120, 2: 140, 4: 150}, "charts": [{"type": "gantt",
          "columns": ["Jan", "Feb", "Mar", "Apr"],
          "groups": ["Frames", "Paint", "Assembly", "Delivery"],
          "today": 0.3, "today_label": "order",
          "tasks": [{"label": "Frames brazed, Ridgeline and Long Mynd",
                     "start": 0.5, "end": 1.4},
                    {"label": "Powder coating", "start": 1.2, "end": 1.8,
                     "group": 1},
                    {"label": "Assembly and test ride", "start": 1.6,
                     "end": 2.5, "group": 2},
                    {"label": "Drop 1: 24 bikes", "start": 2.2,
                     "milestone": True, "text": "7 Mar"},
                    {"label": "Drop 2: 16 bikes", "start": 3.1,
                     "milestone": True, "text": "4 Apr"}]}]},
        {"heading": "Specifications", "kind": "entries", "weight": 0.4,
         "step": 0.15, "inner": 0.05, "min_pages": 2, "entries": [
             {"title": "Ridgeline gravel", "fields": [
                 ("Frame", "Reynolds 853 steel, brazed in Shrewsbury"),
                 ("Tyres", "45 mm, tubeless ready"),
                 ("Warranty", "lifetime on the frame, 2 years on parts")]},
             {"title": "Harbour city", "fields": [
                 ("Frame", "4130 chromoly, mudguard and rack mounts"),
                 ("Gears", "8-speed hub, belt drive")]},
             {"title": "Long Mynd touring", "fields": [
                 ("Frame", "Reynolds 725, three bottle mounts"),
                 ("Racks", "front and rear, fitted")]},
         ]},
        {"heading": "Order mix", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": 140, "widths": [2, 3], "charts": [
             {"type": "donut", "title": "Value",
              "segments": [(m.split(",")[0], q * p)
                           for m, _, _, q, p in LINES],
              "format": "£{:,.0f}", "center": (f"£{GOODS / 1000:.1f}k",
                                               "list")},
             {"type": "bars", "title": "Bicycles by size",
              "stacked": True, "categories": ["S", "M", "L"],
              "series": [{"name": "Ridgeline", "values": [4, 12, 10]},
                         {"name": "Harbour", "color": 1,
                          "values": [3, 5, 2]},
                         {"name": "Long Mynd", "color": 2,
                          "values": [0, 2, 2]}]},
         ]},
        {"heading": "Terms of sale", "kind": "bullets", "weight": 0.6,
         "step": 0.1, "min_pages": 4, "items": [
             "Title stays with Copperline until the bicycles are paid "
             "for in full.",
             "Build slots are held for 14 days; they are confirmed when "
             "the deposit is received.",
             "Changes to colour or size are free until frames are "
             "brazed; after that, at cost.",
             "Damage in transit must be noted on the delivery note and "
             "reported within 48 hours.",
         ]},
        {"heading": "Your account", "kind": "table", "whole": True,
         "weight": 0.7, "min_pages": 4,
         "badges": {"Paid": "good", "Open": "warn"},
         "columns": [("Document", 1.6), ("Date", 1), ("Amount", 1, "end"),
                     ("", 0.8, "center")],
         "rows": [["INV-27-0911", "4 Sep 2027", "£18,420.00", "Paid"],
                  ["INV-27-1104", "12 Nov 2027", "£9,612.00", "Paid"],
                  ["SO-28-0142 deposit", "24 Jan 2028",
                   gbp(round(TOTAL * DEPOSIT, 2)), "Open"]]},
        {"heading": "Dealer support", "kind": "tags", "weight": 0.8,
         "step": 0.1, "min_pages": 4, "items": [
             ("Demo bikes", "two Ridgelines at 50 % for the spring"),
             ("Point of sale", "frame display and brochures included"),
             ("Training", "a workshop day in Shrewsbury for your "
                          "mechanics"),
             ("Contact", "Hannah Ward, dealer manager, 01743 555 0136"),
         ]},
        {"heading": "Your orders with us", "kind": "figure",
         "weight": 0.9, "min_pages": 4, "height": 140, "charts": [{
             "type": "bars", "subtitle": "bicycles a year",
             "categories": ["2024", "2025", "2026", "2027", "2028"],
             "series": [{"name": "Bicycles", "values": [12, 18, 26, 31,
                                                        BIKES],
                         "colors": [4, 4, 4, 4, 0]}]}]},
        {"heading": "Retail prices", "kind": "table", "whole": True,
         "weight": 1.0, "min_pages": 4,
         "columns": [("Model", 2.6), ("Dealer", 1, "end"),
                     ("Suggested retail", 1, "end"),
                     ("Dealer margin", 1, "end")],
         "rows": [[m.split(",")[0] + ("" if "," not in m else ", "
                                      + m.split(", ")[1]), gbp(p),
                   gbp(r), f"{(r / 1.2 - p) / (r / 1.2):.0%}"]
                  for (m, _, _, _, p), r in zip(
                      LINES, [1_745, 2_795, 1_095, 1_995])]},
        {"kind": "callout", "weight": 1.1, "tone": "info",
         "min_pages": 4, "label": "Please check",
         "text": "the sizes and colours above. Changes are free until "
                 "the frames are brazed in the week of 7 February."},
        {"heading": "Delivery plan", "kind": "table", "whole": True,
         "weight": 1.2, "min_pages": 4,
         "columns": [("Drop", 0.8), ("Date", 1.2), ("Bicycles", 3),
                     ("Pallets", 0.8, "end")],
         "rows": [["1", "7 Mar 2028", "18 Ridgeline 105, 6 Harbour city",
                   "3"],
                  ["2", "4 Apr 2028", "8 Ridgeline Di2, 4 Harbour city, "
                   "4 Long Mynd", "2"]]},
        {"heading": "Accepted", "kind": "table", "look": "plain",
         "header": False, "whole": True, "weight": 1.3, "min_pages": 4,
         "columns": [("", 1), ("", 1)],
         "rows": [["For Copperline: Hannah Ward ____________",
                   "For Spokes & Gears: ____________"],
                  ["Date: 10 January 2028", "Date: ____________"]]},
        {"heading": "Lead times", "kind": "figure", "weight": 1.4,
         "min_pages": 4, "height": 120, "charts": [{"type": "progress",
          "format": "{:.0f} weeks", "max": 12, "items": [
              {"label": "Ridgeline 105", "value": 8, "status": 0},
              {"label": "Ridgeline Di2", "value": 12, "status": "warn"},
              {"label": "Harbour city", "value": 6, "status": "good"},
              {"label": "Long Mynd", "value": 12, "status": "warn"}]}]},
    ],
}
