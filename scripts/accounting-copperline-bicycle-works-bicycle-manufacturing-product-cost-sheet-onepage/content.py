"""Product Cost Sheet of Copperline Bicycle Works: the business and everything
the document could say. The typesetting keeps what fits into one page, the
most important first."""

BUSINESS = {
    "name": "Copperline Bicycle Works",
    "author": "Copperline Bicycle Works Ltd, production and finance",
}

# bill of materials for one Ridgeline gravel, 105 groupset: part,
# supplier, quantity, unit cost £
BOM = [("Frame tubeset, Reynolds 853", "Reynolds", 1, 96.00),
       ("Dropouts, head tube, bottom bracket shell", "Paragon", 1, 24.00),
       ("Brazing rod and flux", "stores", 1, 6.20),
       ("Steel fork, flat mount", "Copperline", 1, 38.00),
       ("Shimano 105 groupset, hydraulic", "Madison", 1, 198.00),
       ("Wheelset, 700c tubeless", "own build", 1, 86.00),
       ("Tyres, 45 mm × 2", "Schwalbe", 2, 14.00),
       ("Handlebar, stem, seatpost", "Deda", 1, 32.00),
       ("Saddle and bar tape", "Brooks", 1, 22.00),
       ("Headset and bottom bracket", "Hope", 1, 28.00),
       ("Cables, bolts, grease, decals", "stores", 1, 12.80),
       ("Packaging and manual", "stores", 1, 9.50)]
# operation, minutes, rate £ per hour (labour)
ROUTING = [("Cut and mitre tubes", 35, 26.0),
           ("Jig and braze frame", 150, 32.0),
           ("Clean and inspect", 25, 26.0),
           ("Powder coat (subcontract, per frame)", 0, 0.0),
           ("Build wheels", 45, 26.0),
           ("Assemble and adjust", 120, 26.0),
           ("Test ride and pack", 30, 26.0)]
COATING = 28.00
OVERHEAD_RATE = 11.62      # £ per direct labour hour
PRICE_DEALER = 1_046.00
PRICE_RETAIL = 1_745.00    # including VAT


def gbp(value):
    return f"£{value:,.2f}"


MATERIALS = round(sum(q * c for _, _, q, c in BOM), 2)
HOURS = sum(m for _, m, _ in ROUTING) / 60
LABOUR = round(sum(m / 60 * r for _, m, r in ROUTING), 2)
OVERHEAD = round(HOURS * OVERHEAD_RATE, 2)
COST = round(MATERIALS + LABOUR + COATING + OVERHEAD, 2)
MARGIN = PRICE_DEALER - COST

DOCUMENT = {
    "title": "Product Cost Sheet",
    "eyebrow": "COPPERLINE · COST SHEET CS-RL-105 · REV 4",
    "subtitle": "Ridgeline gravel, Shimano 105, size M · standard cost "
                "for 2028",
    "meta": [("Model", "Ridgeline 105"), ("Materials", gbp(MATERIALS)),
             ("Labour hours", f"{HOURS:.1f}"), ("Standard cost", gbp(COST)),
             ("Dealer margin", f"{MARGIN / PRICE_DEALER:.0%}")],
    "sections": [
        {"heading": "Cost summary", "kind": "table", "whole": True,
         "weight": 0.1, "columns": [("", 3.2), ("Per bike", 1, "end"),
                                    ("Share", 0.8, "end")],
         "rows": [[n, gbp(v), f"{v / COST:.0%}"] for n, v in (
             ("Materials", MATERIALS), ("Direct labour", LABOUR),
             ("Powder coating, subcontract", COATING),
             (f"Factory overhead, {HOURS:.1f} h × £{OVERHEAD_RATE}",
              OVERHEAD))]
         + [{"cells": ["Standard cost", gbp(COST), "100%"],
             "style": "total"}]},
        {"heading": "What the bike is made of", "kind": "figure",
         "weight": 0.2, "height": {1: 160, 2: 170, 4: 180},
         "widths": [3, 2], "charts": [
             {"type": "waterfall", "format": "£{:,.0f}",
              "axis_format": "{:,.0f}", "total_color": 0,
              "subtitle": "from dealer price to margin",
              "steps": [("Dealer price", PRICE_DEALER),
                        ("Materials", -MATERIALS), ("Labour", -LABOUR),
                        ("Coating", -COATING), ("Overhead", -OVERHEAD),
                        ("Margin", None)]},
             {"type": "donut", "title": "Cost",
              "segments": [("Groupset", 198), ("Frame and fork", 164.2),
                           ("Wheels and tyres", 114),
                           ("Other parts", 104.3), ("Labour", LABOUR),
                           ("Coating and overhead", COATING + OVERHEAD)],
              "format": "£{:,.0f}", "center": (f"£{COST:,.0f}", "cost")},
         ]},
        {"heading": "Bill of materials", "kind": "table", "whole": True,
         "weight": 0.3,
         "columns": [("Part", 3), ("Supplier", 1.2),
                     ("Qty", 0.5, "end"), ("Unit", 0.9, "end"),
                     ("Cost", 0.9, "end")],
         "rows": [[p, s, str(q), gbp(c), gbp(q * c)]
                  for p, s, q, c in BOM]
         + [{"cells": ["Materials", "", "", "", gbp(MATERIALS)],
             "style": "total"}]},
        {"heading": "Routing", "kind": "table", "whole": True,
         "weight": 0.4, "min_pages": 2,
         "columns": [("Operation", 3), ("Minutes", 0.8, "end"),
                     ("Rate £/h", 0.8, "end"), ("Cost", 0.9, "end")],
         "rows": [[o, str(m) if m else "—", f"{r:.2f}" if r else "—",
                   gbp(m / 60 * r) if m else gbp(COATING)]
                  for o, m, r in ROUTING]
         + [{"cells": ["Labour and coating", str(sum(
             m for _, m, _ in ROUTING)), "", gbp(LABOUR + COATING)],
             "style": "total"}]},
        {"heading": "Price points", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": 140, "charts": [{"type": "bars",
          "horizontal": True, "stacked": True, "inside": True,
          "format": "£{:,.0f}", "values": False,
          "categories": ["Retail price, incl. VAT"],
          "series": [{"name": "Our cost", "values": [COST]},
                     {"name": "Our margin", "color": "good",
                      "values": [MARGIN]},
                     {"name": "Dealer margin", "color": 1,
                      "values": [round(PRICE_RETAIL / 1.2
                                       - PRICE_DEALER, 2)]},
                     {"name": "VAT", "color": 4,
                      "values": [round(PRICE_RETAIL / 6, 2)]}],
          "row": 50}]},
        {"heading": "Labour by operation", "kind": "figure",
         "weight": 0.6, "min_pages": 4, "height": 150, "charts": [{
             "type": "bars", "horizontal": True, "format": "{:.0f} min",
             "categories": [o for o, m, _ in ROUTING if m],
             "series": [{"name": "Minutes", "values": [
                 m for _, m, _ in ROUTING if m]}]}]},
        {"heading": "Other sizes and builds", "kind": "table",
         "whole": True, "weight": 0.7, "min_pages": 4,
         "columns": [("Build", 2.6), ("Standard cost", 1, "end"),
                     ("Dealer price", 1, "end"), ("Margin", 0.8, "end")],
         "rows": [["Ridgeline 105, size S", gbp(COST - 6), "£1,046.00",
                   f"{(PRICE_DEALER - COST + 6) / PRICE_DEALER:.0%}"],
                  ["Ridgeline 105, size L", gbp(COST + 7), "£1,046.00",
                   f"{(PRICE_DEALER - COST - 7) / PRICE_DEALER:.0%}"],
                  ["Ridgeline GRX Di2", gbp(COST + 412), "£1,710.00",
                   f"{(1710 - COST - 412) / 1710:.0%}"],
                  ["Frameset only", gbp(164.2 + 28 + 68), "£740.00",
                   f"{(740 - 260.2) / 740:.0%}"]]},
        {"heading": "Cost changes since rev 3", "kind": "entries",
         "weight": 0.8, "step": 0.2, "inner": 0.1, "min_pages": 4,
         "entries": [
             {"title": "Groupset +£14", "text": [
                 "Shimano's price list of October 2027; hedged at this "
                 "price for 600 groupsets."]},
             {"title": "Brazing time −15 minutes", "text": [
                 "The new frame jig saves a quarter of an hour on every "
                 "frame."]},
             {"title": "Overhead rate −£0.40", "text": [
                 "More hours worked in 2027 spread the factory overheads "
                 "thinner."]},
         ]},
        {"heading": "Approved", "kind": "table", "look": "plain",
         "header": False, "whole": True, "weight": 0.9, "min_pages": 4,
         "columns": [("", 1), ("", 1)],
         "rows": [["Production: Pete Tranter, 8 Jan 2028",
                   "Finance: Ruth Sandell, 9 Jan 2028"]]},
        {"heading": "Standard against actual", "kind": "figure",
         "weight": 1.0, "min_pages": 4, "height": 150, "charts": [{
             "type": "bars", "subtitle": "£ per bike, last batch of 60",
             "format": "£{:,.0f}",
             "categories": ["Materials", "Labour", "Coating", "Overhead"],
             "series": [{"name": "Standard", "color": 4, "values": [
                 MATERIALS, LABOUR, COATING, OVERHEAD]},
                        {"name": "Actual", "values": [
                            MATERIALS + 11, LABOUR - 7, COATING,
                            OVERHEAD - 2]}]}]},
        {"heading": "Notes", "kind": "bullets", "weight": 1.1,
         "step": 0.1, "min_pages": 4, "items": [
             "Standard costs are set each January and used to value "
             "stock and to quote dealers.",
             "Labour rates include employer's National Insurance and "
             "pension.",
             "Variances over 5 % are reviewed at the monthly production "
             "meeting.",
         ]},
        {"heading": "Where the parts come from", "kind": "figure",
         "weight": 1.2, "min_pages": 4, "height": 140, "charts": [{
             "type": "donut", "format": "£{:,.0f}",
             "segments": [("UK suppliers", 96 + 24 + 22 + 28 + 38),
                          ("Europe", 14 * 2 + 32),
                          ("Japan (Shimano)", 198),
                          ("Made in house", 86 + 12.8 + 9.5 + 6.2)],
             "center": (f"£{MATERIALS:,.0f}", "materials")}]},
    ],
}
