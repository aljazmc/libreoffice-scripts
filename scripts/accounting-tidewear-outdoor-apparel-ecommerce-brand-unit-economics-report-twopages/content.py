"""Unit Economics of Tidewear: the business and everything the document could
say. The typesetting keeps what fits into two pages, the most important
first."""

BUSINESS = {
    "name": "Tidewear",
    "author": "Ella Pengelly, head of e-commerce",
}

# one average web shop order, £ excluding VAT
ORDER = [("Average order value", 86.40),
         ("Returns and refunds", -11.30),
         ("Cost of goods", -30.20),
         ("Pick, pack and postage", -9.40),
         ("Payment fees", -1.70),
         ("Returns handling", -2.10)]
CAC = 38.50              # paid marketing per new customer
ORDERS_PER_YEAR = 1.6    # for repeat customers
RETENTION = [1.00, 0.42, 0.31, 0.25, 0.21]   # share still buying in year


def gbp(value):
    sign = "−" if value < 0 else ""
    return f"{sign}£{abs(value):,.2f}"


CONTRIBUTION = round(sum(v for _, v in ORDER), 2)
FIRST_YEAR = CONTRIBUTION * 1.2      # first year orders per new customer
LTV = round(FIRST_YEAR + sum(CONTRIBUTION * ORDERS_PER_YEAR * r
                             for r in RETENTION[1:]), 2)
PAYBACK_ORDERS = CAC / CONTRIBUTION

DOCUMENT = {
    "title": "Unit Economics",
    "subtitle": "What one web shop order and one new customer are worth "
                "· financial year 2027/28",
    "meta": [("Order value", gbp(ORDER[0][1])),
             ("Contribution", gbp(CONTRIBUTION)),
             ("Acquisition cost", gbp(CAC)),
             ("Lifetime value", gbp(LTV)),
             ("LTV ÷ CAC", f"{LTV / CAC:.1f}×")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "charts": [{"type": "kpis",
         "tiles": [
             {"label": "Contribution per order",
              "value": gbp(CONTRIBUTION), "status": 0,
              "note": f"{CONTRIBUTION / ORDER[0][1]:.0%} of order value",
              "delta": "+£2.10"},
             {"label": "Acquisition cost", "value": gbp(CAC),
              "status": "warn", "note": "per new customer",
              "delta": "+£4.20", "delta_status": "bad"},
             {"label": "Payback", "value": f"{PAYBACK_ORDERS:.1f} orders",
              "status": 1, "note": "about 11 months"},
             {"label": "LTV ÷ CAC", "value": f"{LTV / CAC:.1f}×",
              "status": "warn", "note": "aim for 3×"}]}]},
        {"heading": "One order", "kind": "figure", "weight": 0.2,
         "height": {1: 170, 2: 185, 4: 195}, "charts": [{
             "type": "waterfall", "format": "£{:.2f}",
             "axis_format": "{:.0f}", "invert": False, "total_color": 0,
             "steps": ORDER + [("Contribution", None)]}]},
        {"heading": "The order in detail", "kind": "table", "whole": True,
         "weight": 0.3, "columns": [("Per average order", 3),
                                    ("£", 1, "end"), ("Share", 0.8, "end")],
         "rows": [[n, gbp(v), f"{v / ORDER[0][1]:.0%}".replace("-", "−")]
                  for n, v in ORDER]
         + [{"cells": ["Contribution after variable costs",
                       gbp(CONTRIBUTION),
                       f"{CONTRIBUTION / ORDER[0][1]:.0%}"],
             "style": "total"}]},
        {"heading": "A customer over five years", "kind": "figure",
         "weight": 0.4, "min_pages": 2, "height": 165, "widths": [3, 2],
         "charts": [
             {"type": "line", "title": "Cumulative contribution "
              "per new customer", "subtitle": "£",
              "x": ["Acquired", "Year 1", "Year 2", "Year 3", "Year 4",
                    "Year 5"], "format": "{:.0f}", "zero": False,
              "target": 0, "target_label": "break-even",
              "series": [{"name": "Net of acquisition", "area": True,
                          "values": [round(v, 1) for v in [
                              -CAC, -CAC + FIRST_YEAR,
                              -CAC + FIRST_YEAR + CONTRIBUTION * 1.6
                              * RETENTION[1],
                              -CAC + FIRST_YEAR + CONTRIBUTION * 1.6
                              * sum(RETENTION[1:3]),
                              -CAC + FIRST_YEAR + CONTRIBUTION * 1.6
                              * sum(RETENTION[1:4]),
                              -CAC + LTV]]}]},
             {"type": "bars", "title": "Customers still buying",
              "format": "{:.0%}", "axis_format": "{:.0%}",
              "categories": ["Y1", "Y2", "Y3", "Y4", "Y5"],
              "series": [{"name": "Retention", "values": RETENTION}]},
         ]},
        {"heading": "By channel", "kind": "table", "whole": True,
         "weight": 0.5, "min_pages": 2,
         "badges": {"Grow": "good", "Hold": "warn", "Cut": "bad"},
         "columns": [("Acquisition channel", 2.2), ("CAC", 0.9, "end"),
                     ("First order", 0.9, "end"),
                     ("LTV", 0.9, "end"), ("LTV ÷ CAC", 0.9, "end"),
                     ("", 0.8, "center")],
         "rows": [["Organic search", "£6.20", "£84", "£112", "18.1×",
                   "Grow"],
                  ["Email and referrals", "£9.80", "£91", "£128", "13.1×",
                   "Grow"],
                  ["Paid search", "£34.10", "£88", "£96", "2.8×", "Hold"],
                  ["Social ads", "£52.60", "£79", "£74", "1.4×", "Cut"],
                  ["Creator partnerships", "£41.00", "£95", "£118",
                   "2.9×", "Hold"]]},
        {"heading": "Cohorts", "kind": "figure", "weight": 0.6,
         "min_pages": 4, "height": 155, "charts": [{"type": "heatmap",
          "title": "Repeat purchase rate by cohort",
          "subtitle": "% of customers ordering again in each quarter",
          "rows": ["Q1 2026", "Q2 2026", "Q3 2026", "Q4 2026", "Q1 2027",
                   "Q2 2027"],
          "cols": ["+1 quarter", "+2", "+3", "+4", "+5", "+6"],
          "values": [[22, 18, 15, 19, 12, 10], [24, 17, 21, 13, 11, ""],
                     [21, 26, 14, 12, "", ""], [31, 16, 13, "", "", ""],
                     [23, 19, "", "", "", ""], [25, "", "", "", "", ""]],
          "format": "{:.0f}%", "labels": 0.18}]},
        {"heading": "By product", "kind": "figure", "weight": 0.7,
         "min_pages": 4, "height": 150, "charts": [{"type": "quadrant",
          "x": "return rate", "y": "contribution per item",
          "quadrants": ["Stars", "Watch sizing", "Basics",
                        "Problem lines"],
          "points": [("Shoreline jacket", 6.5, 8.5, 0),
                     ("Tor fleece", 3, 6, 0), ("Base layers", 1.5, 4, 0),
                     ("Trousers", 7.5, 5.5, "warn"),
                     ("Insulated jacket", 4, 9, 0),
                     ("Kids' range", 2, 2.5, 1),
                     ("Clearance colours", 6, 1, "bad")]}]},
        {"heading": "Levers", "kind": "entries", "weight": 0.8,
         "step": 0.2, "inner": 0.1, "min_pages": 4, "entries": [
             {"title": "Free returns only to the shop or a locker",
              "dates": "+£1.10 an order", "text": [
                  "Home collections cost £5.80 a parcel; drop-off "
                  "returns cost £2.40."]},
             {"title": "Size guide with fit notes", "dates":
              "+£1.80 an order", "text": [
                  "Trousers and jackets are returned for size in two "
                  "cases out of three."]},
             {"title": "Move budget from social ads to email",
              "dates": "−£6 CAC", "text": [
                  "Social ads bring customers who rarely come back; "
                  "email and referrals bring the best ones."]},
         ]},
        {"heading": "Definitions", "kind": "tags", "weight": 0.9,
         "step": 0.1, "min_pages": 4, "items": [
             ("Contribution", "what an order leaves after every cost "
                              "that it causes"),
             ("CAC", "paid marketing ÷ new customers"),
             ("LTV", "contribution over five years, not discounted"),
             ("Payback", "orders needed to earn back the CAC"),
         ]},
        {"heading": "Order value", "kind": "figure", "weight": 1.0,
         "min_pages": 4, "height": 150, "widths": [3, 2], "charts": [
             {"type": "bars", "title": "Orders by basket size",
              "subtitle": "% of orders", "format": "{:.0f}%",
              "categories": ["Under £40", "£40 – £79", "£80 – £119",
                             "£120 – £199", "£200 and over"],
              "series": [{"name": "Orders", "values": [18, 34, 27, 15,
                                                       6]}]},
             {"type": "gauges", "items": [
                 {"label": "Free delivery threshold", "value": 75,
                  "max": 120, "target": 86, "status": 0,
                  "display": "£75", "note": "average order £86"}]},
         ]},
        {"heading": "What a returned item costs", "kind": "table",
         "whole": True, "weight": 1.1, "min_pages": 4,
         "columns": [("Step", 3), ("£ per item", 1, "end")],
         "rows": [["Return label", "£2.40"],
                  ["Inspection and repacking", "£1.30"],
                  ["Items that cannot be resold (8 %)", "£2.90"],
                  ["Refund payment fee", "£0.30"],
                  {"cells": ["Cost of one return", "£6.90"],
                   "style": "total"}]},
        {"heading": "Trend", "kind": "figure", "weight": 1.2,
         "min_pages": 4, "height": 150, "charts": [{"type": "line",
          "subtitle": "£ per order and per new customer, by quarter",
          "x": ["Q1 26", "Q2", "Q3", "Q4", "Q1 27", "Q2", "Q3", "Q4"],
          "format": "{:.0f}", "end_labels": True,
          "series": [{"name": "Contribution per order", "values": [
              27.1, 28.4, 29.0, 31.2, 29.6, 30.4, 31.1, CONTRIBUTION]},
                     {"name": "Acquisition cost", "color": 1,
                      "dash": True, "values": [31.2, 32.6, 33.8, 36.4,
                                               34.1, 35.9, 37.2,
                                               CAC]}]}]},
    ],
}
