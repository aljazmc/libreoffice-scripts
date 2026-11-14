"""Manufacturing Account of Copperline Bicycle Works: the business and
everything the document could say. The typesetting keeps what fits into one
page, the most important first."""

BUSINESS = {
    "name": "Copperline Bicycle Works",
    "author": "Copperline Bicycle Works Ltd, finance",
}


def k(value):
    return f"({-value:,})" if value < 0 else f"{value:,}"


# £, year to 31 December 2027
RAW_OPENING, RAW_PURCHASES, RAW_CLOSING = 186_400, 1_412_800, -204_100
CARRIAGE_IN = 38_600
DIRECT_LABOUR = 642_300
DIRECT_EXPENSES = [("Powder coating, subcontract", 96_400),
                   ("Wheel building, subcontract", 52_800)]
OVERHEADS = [("Factory supervision", 118_000),
             ("Factory rent and rates", 96_000),
             ("Power and gas", 74_200),
             ("Depreciation of plant", 88_600),
             ("Repairs and maintenance", 31_400),
             ("Quality testing", 22_900),
             ("Factory insurance", 14_100)]
WIP_OPENING, WIP_CLOSING = 72_300, -81_600
BIKES = 3_420
SALES = 4_284_000
FG_OPENING, FG_CLOSING = 214_000, -246_500
SELLING = [("Dealer commission and marketing", -412_600),
           ("Distribution", -138_200),
           ("Administration", -364_800),
           ("Interest", -28_400)]

RAW_USED = RAW_OPENING + RAW_PURCHASES + CARRIAGE_IN + RAW_CLOSING
PRIME = RAW_USED + DIRECT_LABOUR + sum(v for _, v in DIRECT_EXPENSES)
OVERHEAD = sum(v for _, v in OVERHEADS)
FACTORY = PRIME + OVERHEAD
PRODUCTION = FACTORY + WIP_OPENING + WIP_CLOSING
COST_OF_SALES = FG_OPENING + PRODUCTION + FG_CLOSING
GROSS = SALES - COST_OF_SALES
NET = GROSS + sum(v for _, v in SELLING)


def line(name, value, style="indent", **extra):
    return {"cells": [name, k(value)], "style": style, **extra}


COLUMNS = [("£", 3.6), ("2027", 1.2, "end")]

DOCUMENT = {
    "title": "Manufacturing Account",
    "subtitle": "With the trading and profit and loss account · year ended "
                "31 December 2027",
    "meta": [("Bicycles made", f"{BIKES:,}"),
             ("Cost of production", f"£{PRODUCTION:,}"),
             ("Cost per bike", f"£{PRODUCTION / BIKES:,.0f}"),
             ("Gross margin", f"{GROSS / SALES:.1%}"),
             ("Net profit", f"£{NET:,}")],
    "sections": [
        {"heading": "Manufacturing account", "kind": "table",
         "whole": True, "weight": 0.1, "columns": COLUMNS,
         "rows": [{"cells": ["Raw materials", ""], "style": "section"},
                  line("Opening stock of steel, components and paint",
                       RAW_OPENING, min_pages=2),
                  line("Purchases", RAW_PURCHASES, min_pages=2),
                  line("Carriage inwards", CARRIAGE_IN, min_pages=2),
                  line("Closing stock", RAW_CLOSING, min_pages=2),
                  line("Raw materials used", RAW_USED, "subtotal"),
                  line("Direct labour: frame builders and assembly",
                       DIRECT_LABOUR)]
         + [line(n, v) for n, v in DIRECT_EXPENSES]
         + [line("Prime cost", PRIME, "subtotal"),
            {"cells": ["Factory overheads", ""], "style": "section",
             "min_pages": 2}]
         + [line(n, v, min_pages=2) for n, v in OVERHEADS]
         + [line("Factory overheads", OVERHEAD, max_pages=1),
            line("Total factory cost", FACTORY, "subtotal"),
            line("Work in progress at 1 January", WIP_OPENING),
            line("Work in progress at 31 December", WIP_CLOSING),
            line("Cost of production of 3,420 bicycles", PRODUCTION,
                 "total")]},
        {"heading": "Trading and profit and loss", "kind": "table",
         "whole": True, "weight": 0.2, "columns": COLUMNS,
         "rows": [line("Sales", SALES, "subtotal"),
                  line("Finished bicycles at 1 January", FG_OPENING),
                  line("Cost of production", PRODUCTION),
                  line("Finished bicycles at 31 December", FG_CLOSING),
                  line("Cost of sales", -COST_OF_SALES, "subtotal"),
                  line("Gross profit", GROSS, "highlight")]
         + [line(n, v) for n, v in SELLING]
         + [line("Net profit before tax", NET, "total")]},
        {"heading": "From steel to profit", "kind": "figure",
         "weight": 0.3, "min_pages": 2, "height": 200, "charts": [{
             "type": "sankey", "format": "£{:,.0f}k", "size": 6.8,
             "nodes": [{"id": "mat", "label": "Materials", "col": 0,
                        "color": 0},
                       {"id": "lab", "label": "Labour", "col": 0,
                        "color": 1},
                       {"id": "sub", "label": "Subcontract", "col": 0,
                        "color": 2},
                       {"id": "ovh", "label": "Overheads", "col": 0,
                        "color": 4},
                       {"id": "prod", "label": "Production", "col": 1,
                        "color": 0},
                       {"id": "cos", "label": "Bikes sold", "col": 2,
                        "color": 0},
                       {"id": "stk", "label": "Into stock", "col": 2,
                        "color": 4}],
             "links": [("mat", "prod", RAW_USED // 1000),
                       ("lab", "prod", DIRECT_LABOUR // 1000),
                       ("sub", "prod", 149), ("ovh", "prod",
                                              OVERHEAD // 1000),
                       ("prod", "cos", 2_628), ("prod", "stk", 41)]}]},
        {"heading": "Cost of a bicycle", "kind": "figure", "weight": 0.4,
         "min_pages": 2, "charts": [{"type": "kpis", "tiles": [
             {"label": "Materials", "value": f"£{RAW_USED / BIKES:,.0f}",
              "status": 0, "note": "per bike"},
             {"label": "Labour", "value": f"£{DIRECT_LABOUR / BIKES:,.0f}",
              "status": 1, "note": "11.2 hours"},
             {"label": "Subcontract", "value": f"£{149_200 / BIKES:,.0f}",
              "status": 2, "note": "coating and wheels"},
             {"label": "Overheads", "value": f"£{OVERHEAD / BIKES:,.0f}",
              "status": 3, "note": "per bike"}]}]},
        {"heading": "Notes", "kind": "entries", "weight": 0.5,
         "step": 0.2, "inner": 0.1, "min_pages": 4, "entries": [
             {"title": "Stock", "text": [
                 "Raw materials at cost, first in first out. Work in "
                 "progress and finished bicycles at the cost of "
                 "production: materials, labour and a share of the "
                 "factory overheads at normal output."]},
             {"title": "Overheads", "text": [
                 "Factory overheads are absorbed at £11.62 per direct "
                 "labour hour; the factory worked 11,840 hours more than "
                 "planned, so overheads per bike fell."]},
             {"title": "Subcontract work", "text": [
                 "Powder coating moves in house in 2028 if the investment "
                 "in the coating line is approved."]},
         ]},
        {"heading": "Three years", "kind": "figure", "weight": 0.6,
         "min_pages": 4, "height": 150, "charts": [{"type": "bars",
          "stacked": True, "subtitle": "£ per bicycle made",
          "format": "{:,.0f}", "categories": ["2025", "2026", "2027"],
          "series": [{"name": "Materials", "values": [398, 412,
                                                      round(RAW_USED
                                                            / BIKES)]},
                     {"name": "Labour", "color": 1, "values": [
                         201, 194, round(DIRECT_LABOUR / BIKES)]},
                     {"name": "Subcontract", "color": 2,
                      "values": [46, 45, round(149_200 / BIKES)]},
                     {"name": "Overheads", "color": 4,
                      "values": [148, 143, round(OVERHEAD / BIKES)]}]}]},
        {"heading": "Models made", "kind": "table", "whole": True,
         "weight": 0.7, "min_pages": 4,
         "columns": [("Model", 2.4), ("Made", 0.8, "end"),
                     ("Average price", 1, "end"),
                     ("Cost of production", 1.2, "end")],
         "rows": [["Ridgeline gravel", "1,460", "£1,390", "£882"],
                  ["Harbour city", "1,120", "£890", "£614"],
                  ["Long Mynd touring", "540", "£1,620", "£1,027"],
                  ["Frames only, custom", "300", "£1,140", "£443"],
                  {"cells": ["All", f"{BIKES:,}", "", ""],
                   "style": "total"}]},
        {"heading": "Basis", "kind": "text", "weight": 0.8, "step": 0.3,
         "min_pages": 4, "paragraphs": [
             "The manufacturing account shows what it cost to make the "
             "year's bicycles; the trading account shows what it cost "
             "to sell them. They differ by the change in the stock of "
             "finished bicycles, which grew by 32,500 as the Long Mynd "
             "was built ahead of the spring.",
         ]},
        {"heading": "Overheads", "kind": "figure", "weight": 0.9,
         "min_pages": 4, "height": 150, "charts": [{"type": "bars",
          "horizontal": True, "format": "£{:,.0f}k",
          "categories": [n for n, _ in OVERHEADS],
          "series": [{"name": "2027", "values": [
              round(v / 1000, 1) for _, v in OVERHEADS]}]}]},
        {"heading": "Stocks", "kind": "table", "whole": True,
         "weight": 1.0, "min_pages": 4,
         "columns": [("£", 2.6), ("1 Jan", 1, "end"),
                     ("31 Dec", 1, "end")],
         "rows": [["Raw materials", k(RAW_OPENING), k(-RAW_CLOSING)],
                  ["Work in progress", k(WIP_OPENING), k(-WIP_CLOSING)],
                  ["Finished bicycles", k(FG_OPENING), k(-FG_CLOSING)],
                  {"cells": ["Total", k(RAW_OPENING + WIP_OPENING
                                        + FG_OPENING),
                             k(-RAW_CLOSING - WIP_CLOSING - FG_CLOSING)],
                   "style": "total"}]},
    ],
}
