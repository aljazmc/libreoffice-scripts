"""Excise Duty Return of Hollow Oak Estate: the business and everything the
document could say. The typesetting keeps what fits into two pages, the most
important first."""

BUSINESS = {
    "name": "Hollow Oak Estate",
    "author": "Hollow Oak Estate Ltd, approved warehousekeeper",
}

RATE = 29.40  # € per litre of pure alcohol, wine 11.5 – 14.5 %

# wine released from the bonded cellar in September: litres and strength
RELEASES = [("Bacchus 2026, 75 cl", 2_160, 0.115),
            ("Pinot Noir Rosé 2026, 75 cl", 1_440, 0.12),
            ("Pinot Noir 2025, 75 cl", 1_080, 0.125),
            ("Classic Cuvée NV, 75 cl", 2_700, 0.12),
            ("Blanc de Blancs 2021, 75 cl", 540, 0.12),
            ("Magnums, Classic Cuvée, 150 cl", 180, 0.12)]


def eur(value):
    return f"€{value:,.2f}"


ROWS = [(name, litres, abv, round(litres * abv, 2),
         round(litres * abv * RATE, 2)) for name, litres, abv in RELEASES]
LITRES = sum(r[1] for r in ROWS)
LPA = round(sum(r[3] for r in ROWS), 2)
DUTY = round(sum(r[4] for r in ROWS), 2)
SMALL_RELIEF = round(DUTY * 0.13, 2)  # small producer relief
DUE = round(DUTY - SMALL_RELIEF, 2)

# bonded cellar account, litres of wine
BOND = [("Opening stock in bond, 1 September", 61_420),
        ("Produced: 2027 harvest pressed, first tanks", 9_800),
        ("Released for home use (this return)", -LITRES),
        ("Exported under bond to Belgium", -720),
        ("Losses: evaporation and sampling", -184)]
CLOSING = sum(b[1] for b in BOND)

DOCUMENT = {
    "title": "Excise Duty Return",
    "eyebrow": "Hollow Oak Estate · approved warehouse WK-DTB-00412",
    "subtitle": "Alcohol duty return for wine released from bond, "
                "September 2027",
    "meta": [("Period", "Sep 2027"), ("Warehouse", "WK-DTB-00412"),
             ("Litres released", f"{LITRES:,}"),
             ("Duty payable", eur(DUE)), ("Due", "25 Oct 2027")],
    "sections": [
        {"heading": "Part 1 · Wine released for home use", "kind": "table",
         "whole": True, "weight": 0.1,
         "columns": [("Product", 2.8), ("Litres", 0.8, "end"),
                     ("ABV", 0.6, "end"), ("Litres of alcohol", 1, "end"),
                     ("Duty", 1, "end")],
         "rows": [[name, f"{litres:,}", f"{abv:.1%}", f"{lpa:,.2f}",
                   eur(duty)] for name, litres, abv, lpa, duty in ROWS]
         + [{"cells": ["Total", f"{LITRES:,}", "", f"{LPA:,.2f}",
                       eur(DUTY)], "style": "subtotal"}]},
        {"heading": "Part 2 · Duty calculation", "kind": "table",
         "whole": True, "weight": 0.2,
         "columns": [("Box", 0.5), ("Description", 3.6),
                     ("Amount", 1, "end")],
         "rows": [["1", f"Duty at €{RATE:.2f} per litre of alcohol",
                   eur(DUTY)],
                  ["2", "Less small producer relief (13 %)",
                   f"({eur(SMALL_RELIEF)})"],
                  ["3", "Adjustments from earlier periods", "€0.00"],
                  {"cells": ["4", "Duty payable", eur(DUE)],
                   "style": "total"}]},
        {"heading": "Part 3 · Declaration", "kind": "callout",
         "weight": 0.3, "tone": "accent", "label": "I declare",
         "text": "that the information given in this return is true and "
                 "complete. Payment by direct debit on 25 October 2027. "
                 "— Clare Ashdown, for the warehousekeeper, 9 October "
                 "2027"},
        {"heading": "Part 4 · Bonded cellar account", "kind": "table",
         "whole": True, "weight": 0.4, "min_pages": 2,
         "columns": [("Movement", 3.6), ("Litres of wine", 1, "end")],
         "rows": [[name, f"{litres:,}"] for name, litres in BOND]
         + [{"cells": ["Closing stock in bond, 30 September",
                       f"{CLOSING:,}"], "style": "total"}]},
        {"heading": "Releases by wine", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": 150, "widths": [3, 2], "charts": [
             {"type": "bars", "horizontal": True, "title": "Duty by wine",
              "format": "€{:,.0f}",
              "categories": [r[0].split(",")[0] for r in ROWS],
              "series": [{"name": "Duty", "values": [r[4] for r in ROWS]}]},
             {"type": "donut", "title": "Still and sparkling",
              "segments": [("Still", sum(r[1] for r in ROWS[:3])),
                           ("Sparkling", sum(r[1] for r in ROWS[3:]))],
              "format": "{:,.0f} l", "center": (f"{LITRES:,}", "litres")},
         ]},
        {"heading": "Year to date", "kind": "figure", "weight": 0.6,
         "min_pages": 4, "height": 155, "charts": [{"type": "bars",
          "title": "Duty paid by month", "subtitle": "€, 2027",
          "format": "{:,.0f}", "values": False,
          "categories": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
                         "Aug", "Sep"],
          "series": [{"name": "Duty", "values": [9840, 7210, 11630, 14920,
                                                 18380, 22410, 19870,
                                                 17260, DUE],
                      "colors": [4, 4, 4, 4, 4, 4, 4, 4, 0]}]}]},
        {"heading": "Losses in bond", "kind": "table", "whole": True,
         "weight": 0.7, "min_pages": 4,
         "badges": {"Normal": "good", "Explain": "warn"},
         "columns": [("Cause", 2.6), ("Litres", 0.8, "end"),
                     ("Allowance", 1, "end"), ("", 0.9, "center")],
         "rows": [["Evaporation from barrels", "128", "150", "Normal"],
                  ["Laboratory samples", "21", "30", "Normal"],
                  ["Breakage on the bottling line", "35", "20",
                   "Explain"]]},
        {"heading": "Notes", "kind": "bullets", "weight": 0.8,
         "step": 0.1, "min_pages": 4, "items": [
             "Breakage on the bottling line was a faulty star wheel on "
             "18 September, replaced the same day; photographs and the "
             "engineer's report are kept with the cellar records.",
             "The export to Belgium travelled under an electronic "
             "administrative document, ARC 27BE0049812.",
             "Strength is the label strength, checked by the laboratory "
             "for each bottling run.",
         ]},
        {"heading": "Rates used", "kind": "tags", "weight": 0.9,
         "step": 0.1, "min_pages": 4, "items": [
             ("Wine 11.5 – 14.5 % ABV", f"€{RATE:.2f} per litre of "
                                        "alcohol"),
             ("Small producer relief", "13 %, for under 4,500 litres of "
                                       "alcohol a year"),
             ("Sparkling wine", "taxed at the same rate as still since "
                                "the 2023 reform"),
         ]},
        {"heading": "Checks", "kind": "table", "whole": True,
         "weight": 1.0, "min_pages": 4, "badges": {"Done": "good"},
         "columns": [("Check before submission", 4),
                     ("", 0.8, "center")],
         "rows": [["Releases agree to the dispatch notes", "Done"],
                  ["Stock in bond agrees to the cellar book", "Done"],
                  ["Strengths agree to the lab certificates", "Done"],
                  ["Reviewed by a second person (H. Marlow)", "Done"]]},
        {"heading": "Stock in bond by product", "kind": "table",
         "whole": True, "weight": 1.1, "min_pages": 4,
         "columns": [("Product", 2.8), ("Litres", 1, "end"),
                     ("Duty if released", 1.2, "end")],
         "rows": [["Wine in tank and barrel, 2026 vintage", "40,000",
                   eur(40_000 * 0.12 * RATE)],
                  ["Sparkling on lees, 2023 – 2025", "14,600",
                   eur(14_600 * 0.12 * RATE)],
                  ["Bottled, labelled, awaiting sale", "6,000",
                   eur(6_000 * 0.12 * RATE)],
                  ["New wine, 2027 harvest", "9,800",
                   eur(9_800 * 0.11 * RATE)],
                  {"cells": ["Total in bond", f"{CLOSING:,}", ""],
                   "style": "total"}]},
        {"heading": "Duty on a bottle", "kind": "figure", "weight": 1.2,
         "min_pages": 4, "height": 150, "charts": [{"type": "bars",
          "title": "Duty per 75 cl bottle", "subtitle": "€, after relief",
          "format": "€{:.2f}", "axis_format": "{:.1f}",
          "categories": [r[0].split(",")[0] for r in ROWS[:5]],
          "series": [{"name": "Duty", "values": [
              round(0.75 * abv * RATE * 0.87, 2)
              for _, _, abv in RELEASES[:5]]}]}]},
        {"heading": "Returns filed", "kind": "table", "whole": True,
         "weight": 1.3, "min_pages": 4, "badges": {"Paid": "good"},
         "columns": [("Period", 1), ("Filed", 1), ("Duty", 1, "end"),
                     ("", 0.8, "center")],
         "rows": [["June 2027", "8 Jul", "€22,410.00", "Paid"],
                  ["July 2027", "7 Aug", "€19,870.00", "Paid"],
                  ["August 2027", "9 Sep", "€17,260.00", "Paid"]]},
        {"heading": "Releases over the year", "kind": "figure",
         "weight": 1.4, "min_pages": 4, "height": 150, "charts": [{
             "type": "line", "title": "Litres released for home use",
             "x": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
                   "Sep"], "format": "{:,.0f}",
             "series": [{"name": "2027", "area": True,
                         "values": [3220, 2360, 3810, 4890, 6020, 7340,
                                    6510, 5650, LITRES]},
                        {"name": "2026", "dash": True, "color": 4,
                         "values": [2980, 2240, 3420, 4510, 5480, 6620,
                                    6050, 5310, 7240]}]}]},
        {"heading": "Contacts", "kind": "tags", "weight": 1.5,
         "step": 0.1, "min_pages": 4, "items": [
             ("Warehousekeeper", "Hollow Oak Estate Ltd"),
             ("Responsible person", "Clare Ashdown, 01273 555 0142"),
             ("Excise office", "Southern region, approval WK-DTB-00412"),
         ]},
    ],
}
