"""Harvest Cost Allocation of Hollow Oak Estate: the business and everything
the document could say. The typesetting keeps what fits into one page, the
most important first."""

BUSINESS = {
    "name": "Hollow Oak Estate",
    "author": "Clare Ashdown, finance, with Sam Okoro, cellar master",
}

WINES = ["Bacchus", "Rosé", "Pinot Noir", "Classic Cuvée",
         "Blanc de Blancs"]
# driver quantities per wine
HECTARES = [4.0, 1.6, 4.4, 2.4, 1.6]        # vineyard area harvested
LITRES = [18_400, 9_600, 21_600, 22_800, 9_400]  # wine made
BARREL_MONTHS = [0, 0, 11 * 96, 0, 0]       # barrel-months
TIRAGE = [0, 0, 0, 30_400, 12_500]          # bottles on lees
BOTTLES = [24_500, 12_800, 28_800, 30_400, 12_500]

# cost pools (€) and how each is shared
POOLS = [("Vineyard labour and spraying", 214_000, HECTARES),
         ("Harvest pickers", 58_000, HECTARES),
         ("Winemaking: labour and energy", 96_000, LITRES),
         ("Barrel depreciation and cellar", 41_000, BARREL_MONTHS),
         ("Sparkling: tirage, riddling, disgorging", 63_000, TIRAGE),
         ("Bottling and dry goods", 88_000, BOTTLES)]


def share(amount, driver):
    total = sum(driver)
    return [amount * d / total if total else 0 for d in driver]


ALLOC = [share(amount, driver) for _, amount, driver in POOLS]
BY_WINE = [sum(a[i] for a in ALLOC) for i in range(len(WINES))]
PER_BOTTLE = [c / b for c, b in zip(BY_WINE, BOTTLES)]
PRICES = [16.5, 17.0, 29.0, 31.0, 42.0]   # cellar door, excluding VAT
TOTAL = sum(p[1] for p in POOLS)


def eur(value):
    return f"€{value:,.0f}"


DOCUMENT = {
    "title": "Harvest Cost Allocation",
    "subtitle": "What each wine of the 2026 vintage cost to grow and make, "
                "and what it earns",
    "meta": [("Vintage", "2026"), ("Costs allocated", eur(TOTAL)),
             ("Bottles", f"{sum(BOTTLES):,}"),
             ("Average cost", f"€{TOTAL / sum(BOTTLES):.2f} a bottle"),
             ("Method", "Activity drivers")],
    "sections": [
        {"heading": "Cost per bottle", "kind": "table", "whole": True,
         "weight": 0.1,
         "columns": [("Wine", 2), ("Bottles", 1, "end"),
                     ("Total cost", 1, "end"),
                     ("Cost per bottle", 1, "end"),
                     ("Cellar door price", 1, "end"),
                     ("Margin", 0.8, "end")],
         "rows": [[w, f"{b:,}", eur(c), f"€{pb:.2f}", f"€{p:.2f}",
                   f"{(p - pb) / p:.0%}"]
                  for w, b, c, pb, p in zip(WINES, BOTTLES, BY_WINE,
                                            PER_BOTTLE, PRICES)]
         + [{"cells": ["Vintage", f"{sum(BOTTLES):,}", eur(TOTAL),
                       f"€{TOTAL / sum(BOTTLES):.2f}", "", ""],
             "style": "total"}]},
        {"heading": "What a bottle is made of", "kind": "figure",
         "weight": 0.2, "height": {1: 165, 2: 190, 4: 210}, "charts": [{
             "type": "bars", "horizontal": True, "stacked": True,
             "inside": True, "format": "€{:.2f}", "values": True,
             "subtitle": "cost per bottle by cost pool",
             "categories": WINES,
             "series": [{"name": name.split(":")[0].replace(
                             "Vineyard labour and spraying", "Vineyard"),
                         "color": i if i < 5 else "info",
                         "values": [round(ALLOC[i][j] / BOTTLES[j], 2)
                                    for j in range(len(WINES))]}
                        for i, (name, _, _) in enumerate(POOLS)]}]},
        {"heading": "Margins", "kind": "figure", "weight": 0.3,
         "min_pages": 2, "height": 160, "charts": [{"type": "bars",
          "title": "Cost and price per bottle", "subtitle": "€",
          "format": "{:.2f}", "axis_format": "{:.0f}",
          "categories": WINES,
          "series": [{"name": "Cost", "color": 1,
                      "values": [round(p, 2) for p in PER_BOTTLE]},
                     {"name": "Cellar door price", "color": 0,
                      "values": PRICES}]}]},
        {"heading": "Drivers", "kind": "table", "whole": True,
         "weight": 0.4, "min_pages": 2,
         "columns": [("Cost pool", 2.6), ("Amount", 1, "end"),
                     ("Shared by", 2.2)],
         "rows": [[name, eur(amount),
                   ["hectares harvested", "hectares harvested",
                    "litres of wine made", "barrel-months",
                    "bottles en tirage", "bottles filled"][i]]
                  for i, (name, amount, _) in enumerate(POOLS)]
         + [{"cells": ["Total", eur(TOTAL), ""], "style": "total"}]},
        {"heading": "Findings", "kind": "bullets", "weight": 0.5,
         "step": 0.15, "min_pages": 2, "items": [
             "**Sparkling wines carry the heaviest cost**: tirage, "
             "riddling and two years on lees, before any storage cost.",
             "**Pinot Noir earns its barrels.** Eleven months in oak add "
             "about €1.40 a bottle, and the price covers it twice.",
             "**Rosé is the cheapest to make** and the quickest to sell: "
             "it is in the shop by May.",
         ]},
        {"heading": "Allocation in full", "kind": "table", "whole": True,
         "weight": 0.6, "min_pages": 4,
         "columns": [("€", 2.4)] + [(w, 1, "end") for w in WINES],
         "rows": [[name.split(":")[0]] + [eur(a) for a in ALLOC[i]]
                  for i, (name, _, _) in enumerate(POOLS)]
         + [{"cells": ["Total"] + [eur(c) for c in BY_WINE],
             "style": "total"}]},
        {"heading": "Vineyard blocks", "kind": "figure", "weight": 0.7,
         "min_pages": 4, "height": 150, "widths": [2, 3], "charts": [
             {"type": "donut", "title": "Hectares harvested",
              "segments": list(zip(WINES, HECTARES)), "format":
              "{:.1f} ha", "center": (f"{sum(HECTARES):.0f} ha",
                                      "harvested")},
             {"type": "bars", "title": "Yield", "subtitle": "tonnes per "
              "hectare", "format": "{:.1f}",
              "categories": WINES,
              "series": [{"name": "2025", "color": 4,
                          "values": [7.2, 6.8, 5.4, 6.1, 5.9]},
                         {"name": "2026", "values": [7.9, 7.3, 6.0, 6.6,
                                                     6.2]}]},
         ]},
        {"heading": "Method", "kind": "text", "weight": 0.8, "step": 0.3,
         "min_pages": 4, "paragraphs": [
             "Each cost of the vintage is put in a pool and shared among "
             "the wines by the activity that drives it: vineyard costs by "
             "the hectares each wine came from, cellar costs by the "
             "litres made, barrel costs by the months in oak, sparkling "
             "costs by the bottles laid down on lees.",
             "Costs after bottling (storage, sales, marketing) are not "
             "included. Prices are cellar door prices excluding VAT; "
             "trade prices are about 40 % lower.",
         ]},
        {"heading": "What changes for 2027", "kind": "entries",
         "weight": 0.9, "step": 0.2, "inner": 0.1, "min_pages": 4,
         "entries": [
             {"title": "Price of Blanc de Blancs", "text": [
                 "Raise to €46 for the 2022 release: demand outran stock "
                 "by October."]},
             {"title": "Track picking hours by block", "text": [
                 "Harvest pickers are shared by hectares today; recording "
                 "hours per block would show the true cost of the steep "
                 "Pinot Noir slopes."]},
         ]},
        {"heading": "Cost per bottle over three vintages", "kind": "figure",
         "weight": 1.0, "min_pages": 4, "height": 155, "charts": [{
             "type": "line", "subtitle": "€", "format": "{:.2f}",
             "x": ["2024", "2025", "2026"], "end_labels": True,
             "series": [{"name": w, "color": i,
                         "values": [round(PER_BOTTLE[i] * f, 2)
                                    for f in (1.12, 1.07, 1.0)]}
                        for i, w in enumerate(WINES)]}]},
        {"heading": "If the price moves", "kind": "table", "whole": True,
         "weight": 1.1, "min_pages": 4,
         "columns": [("Wine", 2), ("Margin today", 1, "end"),
                     ("Price −10 %", 1, "end"), ("Cost +10 %", 1, "end")],
         "rows": [[w, f"{(p - c) / p:.0%}",
                   f"{(p * 0.9 - c) / (p * 0.9):.0%}",
                   f"{(p - c * 1.1) / p:.0%}"]
                  for w, c, p in zip(WINES, PER_BOTTLE, PRICES)]},
        {"heading": "Gross margin by wine", "kind": "figure",
         "weight": 1.2, "min_pages": 4, "charts": [{"type": "gauges",
          "items": [{"label": w, "value": round((p - c) / p * 100),
                     "max": 100, "target": 70, "status": i,
                     "display": f"{(p - c) / p:.0%}"}
                    for i, (w, c, p) in enumerate(zip(WINES, PER_BOTTLE,
                                                      PRICES))]}]},
    ],
}
