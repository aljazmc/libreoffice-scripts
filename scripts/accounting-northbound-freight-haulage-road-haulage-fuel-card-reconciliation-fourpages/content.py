"""Fuel Card Reconciliation of Northbound Freight: the business and everything
the document could say. The typesetting keeps what fits into four pages, the
most important first."""

BUSINESS = {
    "name": "Northbound Freight",
    "author": "Northbound Freight Ltd, transport office",
}

PRICE = 1.214   # average £ per litre, excluding VAT, February
# truck, driver, litres on card, telematics litres used, miles
TRUCKS = [("NB18 DAF XF", "M. Kowalski", 3_412, 3_390, 6_420),
          ("NB19 DAF XF", "S. Patel", 3_268, 3_255, 6_110),
          ("NB20 Volvo FH", "A. Reid", 3_590, 3_402, 6_380),
          ("NB21 Volvo FH", "J. Doyle", 2_946, 2_931, 5_560),
          ("NB22 Scania R", "K. Asante", 3_105, 3_098, 5_900),
          ("NB23 Scania R", "P. Byrne", 3_384, 3_376, 6_470),
          ("NB24 DAF XF", "T. Lund", 2_812, 2_809, 5_150),
          ("NB25 Volvo FH", "R. Hughes", 3_250, 3_046, 5_520)]
TOLERANCE = 0.02   # 2 % between card and telematics


def gbp(value):
    sign = "−" if value < 0 else ""
    return f"{sign}£{abs(value):,.2f}"


ROWS = []
for truck, driver, card, used, miles in TRUCKS:
    diff = card - used
    mpg = miles / (used / 4.546)
    flag = "Check" if diff / used > TOLERANCE else "OK"
    ROWS.append((truck, driver, card, used, diff, miles, mpg, flag))
LITRES = sum(r[2] for r in ROWS)
STATEMENT = round(LITRES * PRICE, 2)
UNEXPLAINED = [r for r in ROWS if r[7] == "Check"]

DOCUMENT = {
    "title": "Fuel Card Reconciliation",
    "eyebrow": "NORTHBOUND FREIGHT · FUEL CONTROL · FORM FC-3",
    "subtitle": "February 2028 · Keyfuels statement 0228-4417 · the 8 "
                "tractor units on the long-distance fleet",
    "meta": [("Month", "Feb 2028"), ("Litres on cards", f"{LITRES:,}"),
             ("Statement", gbp(STATEMENT)),
             ("Exceptions", str(len(UNEXPLAINED))),
             ("Checked by", "L. Grant")],
    "sections": [
        {"heading": "1. Statement to ledger", "kind": "table",
         "whole": True, "weight": 0.1,
         "columns": [("", 3.4), ("£", 1.2, "end")],
         "rows": [["Fuel card statement, February (excluding VAT)",
                   gbp(STATEMENT)],
                  ["Posted to 5010 Diesel and AdBlue", gbp(STATEMENT)],
                  {"cells": ["Difference", "£0.00"], "style": "total"}]},
        {"heading": "2. Cards against telematics", "kind": "table",
         "whole": True, "weight": 0.2,
         "badges": {"OK": "good", "Check": "bad"},
         "columns": [("Truck", 1.4), ("Driver", 1.2),
                     ("Card litres", 0.9, "end"),
                     ("Used litres", 0.9, "end"),
                     ("Difference", 0.9, "end"), ("mpg", 0.6, "end"),
                     ("", 0.7, "center")],
         "rows": [[t, d, f"{c:,}", f"{u:,}", f"{df:+,}", f"{m:.1f}", f]
                  for t, d, c, u, df, mi, m, f in ROWS]
         + [{"cells": ["Fleet", "", f"{LITRES:,}",
                       f"{sum(r[3] for r in ROWS):,}",
                       f"{sum(r[4] for r in ROWS):+,}", "", ""],
             "style": "total"}]},
        {"heading": "3. Exceptions", "kind": "entries", "weight": 0.3,
         "step": 0.15, "inner": 0.05, "entries": [
             {"title": f"{r[0]} · {r[4]:+,} litres "
                       f"({r[4] / r[3]:.1%})", "text": [t]}
             for r, t in zip(UNEXPLAINED, [
                 "Card used twice at Doncaster services on 14 Feb within "
                 "ten minutes; the second fill of 180 litres does not "
                 "appear in the tank sensor. Card stopped, receipt "
                 "requested from the site.",
                 "Tank sensor fault reported on 19 Feb; the workshop "
                 "replaced it on 22 Feb. Telematics under-reads for three "
                 "days; no further action."])]},
        {"heading": "4. Sign-off", "kind": "table", "look": "plain",
         "header": False, "whole": True, "weight": 0.35,
         "columns": [("", 1), ("", 1)],
         "rows": [["Reconciled: L. Grant, transport office, 4 Mar",
                   "Approved: R. Mehta, finance director, 6 Mar"]]},
        {"heading": "Fuel economy", "kind": "figure", "weight": 0.4,
         "min_pages": 2, "height": 160, "charts": [{"type": "bars",
          "horizontal": True, "format": "{:.1f} mpg",
          "subtitle": "miles per gallon, from telematics", "target": 8.5,
          "target_label": "fleet target",
          "categories": [r[0] for r in ROWS],
          "series": [{"name": "mpg", "values": [round(r[6], 1)
                                                for r in ROWS],
                      "colors": ["good" if r[6] >= 8.5 else "warn"
                                 for r in ROWS]}]}]},
        {"heading": "Where the fuel was bought", "kind": "figure",
         "weight": 0.5, "min_pages": 2, "height": 140, "widths": [2, 3],
         "charts": [
             {"type": "donut", "title": "Litres by site",
              "segments": [("Own yard tank", 10_838),
                           ("Keyfuels network", 12_960),
                           ("Motorway services", 1_830),
                           ("Continental (Rotterdam)", 139)],
              "format": "{:,.0f} l", "center": (f"{LITRES:,}", "litres")},
             {"type": "bars", "title": "Price paid", "subtitle":
              "£ per litre ex VAT", "format": "£{:.3f}",
              "axis_format": "{:.2f}",
              "categories": ["Yard tank", "Keyfuels", "Services",
                             "Rotterdam"],
              "series": [{"name": "Price", "values": [1.182, 1.209,
                                                      1.412, 1.256],
                          "colors": ["good", 0, "bad", 0]}]},
         ]},
        {"heading": "Fuel over the year", "kind": "figure",
         "weight": 0.6, "min_pages": 4, "height": 150, "charts": [{
             "type": "line", "subtitle": "£k per month on the eight cards",
             "x": ["Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct",
                   "Nov", "Dec", "Jan", "Feb"], "format": "{:.0f}",
             "series": [{"name": "Fuel cost, £k", "area": True,
                         "values": [30, 29, 31, 29, 28, 27, 30, 31, 32,
                                    27, 30, round(STATEMENT / 1000)]}]}]},
        {"heading": "Rules for fuel cards", "kind": "bullets",
         "weight": 0.7, "step": 0.1, "min_pages": 4, "items": [
             "One card per truck, kept in the cab; the PIN is the "
             "driver's own.",
             "Fill at the yard tank whenever the route passes the depot.",
             "Motorway services only in an emergency, with the reason "
             "on the daily sheet.",
             "Differences over 2 % between the card and the tank sensor "
             "are explained within a week.",
         ]},
        {"heading": "Driver league", "kind": "table", "whole": True,
         "weight": 0.8, "min_pages": 4,
         "columns": [("Position", 0.8, "center"), ("Driver", 1.6),
                     ("mpg", 0.8, "end"), ("Idling", 0.8, "end"),
                     ("Harsh braking", 1, "end")],
         "rows": [[str(i + 1), r[1], f"{r[6]:.1f}", f"{4 + i}%",
                   str(2 + i)] for i, r in enumerate(
                       sorted(ROWS, key=lambda r: -r[6]))]},
        {"heading": "Fill-ups by day", "kind": "figure", "weight": 0.9,
         "min_pages": 4, "height": 150, "charts": [{"type": "heatmap",
          "subtitle": "litres bought on the cards, February",
          "rows": [r[0] for r in ROWS],
          "cols": ["W1", "W2", "W3", "W4"],
          "values": [[860, 840, 870, 842], [820, 810, 830, 808],
                     [880, 870, 1_060, 780], [740, 730, 750, 726],
                     [780, 770, 790, 765], [850, 840, 860, 834],
                     [700, 710, 702, 700], [800, 780, 990, 680]],
          "format": "{:,.0f}", "labels": 0.2}]},
        {"heading": "Actions", "kind": "table", "whole": True,
         "weight": 1.0, "min_pages": 4,
         "badges": {"Done": "good", "Open": "warn"},
         "columns": [("Action", 3.4), ("Owner", 1.2), ("", 0.8,
                                                       "center")],
         "rows": [["Stop the NB20 card and issue a new one", "L. Grant",
                   "Done"],
                  ["Ask Doncaster services for the CCTV and receipts",
                   "L. Grant", "Open"],
                  ["Interview the NB20 driver with the union rep",
                   "Transport manager", "Open"],
                  ["Replace the NB25 tank sensor", "Workshop", "Done"]]},
        {"heading": "Prices at the pump", "kind": "figure", "weight": 1.1,
         "min_pages": 4, "height": 140, "charts": [{"type": "line",
          "subtitle": "£ per litre excluding VAT, weekly",
          "x": ["W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8"],
          "format": "{:.3f}", "zero": False,
          "series": [{"name": "Yard tank (bulk)", "values": [
              1.176, 1.179, 1.181, 1.180, 1.184, 1.182, 1.186, 1.185]},
                     {"name": "Keyfuels", "color": 1, "values": [
                         1.198, 1.202, 1.207, 1.205, 1.211, 1.209, 1.214,
                         1.212]},
                     {"name": "Motorway services", "color": "bad",
                      "dash": True, "values": [1.389, 1.394, 1.401,
                                               1.398, 1.412, 1.408,
                                               1.419, 1.415]}]}]},
        {"heading": "Cost per truck", "kind": "figure", "weight": 1.2,
         "min_pages": 4, "height": 150, "charts": [{"type": "bars",
          "horizontal": True, "format": "£{:,.0f}",
          "subtitle": "fuel bought on the card, February",
          "categories": [r[0] for r in ROWS],
          "series": [{"name": "Fuel", "values": [round(r[2] * PRICE)
                                                 for r in ROWS],
                      "colors": ["bad" if r[7] == "Check" else 0
                                 for r in ROWS]}]}]},
    ],
}
