"""Fixed Asset Register of Hollow Oak Estate: the business and everything the
document could say. The typesetting keeps what fits into two pages, the most
important first."""

BUSINESS = {
    "name": "Hollow Oak Estate",
    "author": "Hollow Oak Estate Ltd, finance",
}

YEAR_END = 2027  # year to 30 June 2027

# ref, asset, class, acquired (financial year), cost €, life in years
# (0 = not depreciated)
ASSETS = [
    ("L01", "Freehold land, 34 ha", "Land", 2009, 1_150_000, 0),
    ("B01", "Winery building and barrel hall", "Buildings", 2012,
     1_480_000, 50),
    ("B02", "Tasting room and shop", "Buildings", 2019, 420_000, 50),
    ("V01", "Vines: Chardonnay and Pinot Noir, 9 ha", "Vineyards", 2011,
     318_000, 30),
    ("V02", "Vines: Bacchus, 4 ha", "Vineyards", 2016, 142_000, 30),
    ("V03", "Vines: Pinot Noir, 2.1 ha (immature)", "Vineyards", 2024,
     96_000, 0),
    ("V04", "Trellis and posts, all blocks", "Vineyards", 2018, 164_000,
     20),
    ("E01", "Pneumatic press, 50 hl", "Equipment", 2020, 148_000, 15),
    ("E02", "Stainless tanks, 14", "Equipment", 2014, 226_000, 20),
    ("E03", "Bottling line (shared ownership 50 %)", "Equipment", 2022,
     212_000, 10),
    ("E04", "Riddling machines, 4 gyropalettes", "Equipment", 2021,
     68_000, 10),
    ("E05", "Barrels, 2023 to 2026 purchases", "Equipment", 2025,
     124_000, 5),
    ("E06", "Cold store and refrigeration", "Equipment", 2017, 96_000,
     15),
    ("T01", "Vineyard tractor, narrow", "Vehicles", 2023, 74_000, 8),
    ("T02", "Delivery van, electric", "Vehicles", 2026, 52_000, 6),
    ("T03", "Quad bike and sprayer", "Vehicles", 2021, 31_000, 6),
]


def eur(value):
    return f"€{value:,.0f}"


ROWS = []
for ref, name, cls, year, cost, life in ASSETS:
    used_before = max(0, min(YEAR_END - 1 - year, life)) if life else 0
    charge = round(cost / life) if life and YEAR_END - year <= life else 0
    bf = round(cost / life * used_before) if life else 0
    nbv = cost - bf - charge
    ROWS.append((ref, name, cls, year, cost, life, bf, charge, nbv))

CLASSES = {}
for row in ROWS:
    c = CLASSES.setdefault(row[2], [0, 0, 0])
    c[0] += row[4]
    c[1] += row[7]
    c[2] += row[8]
TOTAL = [sum(r[i] for r in ROWS) for i in (4, 6, 7, 8)]
COLUMNS = [("Ref", 0.5), ("Asset", 3), ("Class", 1.1),
           ("Acquired", 0.8, "center"), ("Cost", 1, "end"),
           ("Life", 0.6, "center"), ("Depreciation b/f", 1.1, "end"),
           ("Charge 2027", 1, "end"), ("Book value", 1, "end")]

DOCUMENT = {
    "title": "Fixed Asset Register",
    "subtitle": "Hollow Oak Estate Ltd · year ended 30 June 2027 · "
                "straight-line depreciation",
    "meta": [("Assets", str(len(ROWS))), ("Cost", eur(TOTAL[0])),
             ("Charge for the year", eur(TOTAL[2])),
             ("Book value", eur(TOTAL[3])), ("Checked", "Jul 2027")],
    "sections": [
        {"heading": "Register", "kind": "table", "whole": True,
         "weight": 0.1, "columns": COLUMNS,
         "rows": [[ref, name, cls, f"{year}/{(year + 1) % 100:02d}",
                   eur(cost), f"{life} y" if life else "—", eur(bf),
                   eur(charge), eur(nbv)]
                  for ref, name, cls, year, cost, life, bf, charge, nbv
                  in ROWS]
         + [{"cells": ["", "Total", "", "", eur(TOTAL[0]), "",
                       eur(TOTAL[1]), eur(TOTAL[2]), eur(TOTAL[3])],
             "style": "total"}]},
        {"heading": "By class", "kind": "figure", "weight": 0.2,
         "min_pages": 2, "height": 160, "widths": [3, 2], "charts": [
             {"type": "bars", "horizontal": True, "stacked": True,
              "title": "Cost and book value", "subtitle": "€k",
              "format": "{:,.0f}", "values": False,
              "categories": list(CLASSES),
              "series": [{"name": "Book value", "values": [
                  v[2] / 1000 for v in CLASSES.values()]},
                         {"name": "Depreciated", "color": 4, "values": [
                             (v[0] - v[2]) / 1000
                             for v in CLASSES.values()]}]},
             {"type": "donut", "title": "Charge for the year",
              "segments": [(c, v[1] / 1000) for c, v in CLASSES.items()
                           if v[1]],
              "format": "€{:,.1f}k",
              "center": (f"€{TOTAL[2] / 1000:,.0f}k", "depreciation")},
         ]},
        {"heading": "Policies", "kind": "table", "whole": True,
         "weight": 0.3, "min_pages": 2,
         "columns": [("Class", 1.2), ("Life", 1), ("Policy", 4.6)],
         "rows": [["Land", "—", "Not depreciated."],
                  ["Buildings", "50 years", "Straight line from the year "
                   "of completion; revalued every five years."],
                  ["Vineyards", "20 – 30 years", "Vines are bearer plants; "
                   "depreciation starts with the first commercial "
                   "harvest. Trellis over 20 years."],
                  ["Equipment", "5 – 20 years", "Straight line; barrels "
                   "over five years, as they lose their oak."],
                  ["Vehicles", "6 – 8 years", "Straight line to nil."]]},
        {"heading": "Additions and disposals", "kind": "table",
         "whole": True, "weight": 0.5, "min_pages": 4,
         "columns": [("Date", 0.9), ("Asset", 3), ("Movement", 1.2),
                     ("Amount", 1, "end")],
         "rows": [["Aug 2026", "Delivery van, electric (T02)", "Addition",
                   "€52,000"],
                  ["Oct 2026", "Old delivery van, diesel", "Disposal",
                   "€6,500 proceeds"],
                  ["Jan 2027", "Barrels, 20 new (E05)", "Addition",
                   "€19,600"],
                  ["Mar 2027", "Barrels, 16 retired to planters",
                   "Disposal", "€0, fully written off"]]},
        {"heading": "Age of the equipment", "kind": "figure",
         "weight": 0.6, "min_pages": 4, "height": 160, "charts": [{
             "type": "progress", "format": "{:.0f} %", "items": [
                 {"label": r[1].split(",")[0].split(" (")[0],
                  "value": round(100 * (r[6] + r[7]) / r[4]),
                  "status": "bad" if (r[6] + r[7]) / r[4] > 0.75 else
                  "warn" if (r[6] + r[7]) / r[4] > 0.5 else "good",
                  "note": f"{r[5]}-year life, bought {r[3]}"}
                 for r in ROWS if r[2] in ("Equipment", "Vehicles")]}]},
        {"heading": "Replacement plan", "kind": "entries", "weight": 0.7,
         "step": 0.2, "inner": 0.1, "min_pages": 4, "entries": [
             {"title": "Stainless tanks", "dates": "2030 – 2032",
              "text": ["Fully depreciated by 2034 but in good condition; "
                       "two tanks with pitted welds to be replaced in "
                       "2030."]},
             {"title": "Quad bike and sprayer", "dates": "2027/28",
              "text": ["Reaches the end of its life next year; a "
                       "replacement sprayer with drift reduction is in "
                       "the capital budget at €38,000."]},
             {"title": "Pneumatic press", "dates": "2035",
              "text": ["Serviced every winter; no change planned."]},
         ]},
        {"heading": "Verification", "kind": "bullets", "weight": 0.8,
         "step": 0.1, "min_pages": 4, "items": [
             "Every asset was seen on 4 July 2027 and tagged; the "
             "barrels were counted in the hall (E05: 66 barrels).",
             "The register agrees to the fixed asset accounts in the "
             "ledger and to the balance sheet.",
             "Insured values were updated for the new van and barrels.",
         ]},
        {"heading": "Depreciation ahead", "kind": "figure", "weight": 0.9,
         "min_pages": 4, "height": 150, "charts": [{"type": "bars",
          "title": "Charge by year, on today's assets", "subtitle": "€k",
          "format": "{:,.0f}", "stacked": True,
          "categories": ["2028", "2029", "2030", "2031", "2032"],
          "series": [{"name": "Buildings", "values": [38, 38, 38, 38, 38]},
                     {"name": "Vineyards", "values": [23, 26, 26, 26,
                                                      26]},
                     {"name": "Equipment", "color": 2,
                      "values": [72, 66, 49, 40, 25]},
                     {"name": "Vehicles", "color": 4,
                      "values": [23, 18, 18, 18, 9]}]}]},
    ],
}
