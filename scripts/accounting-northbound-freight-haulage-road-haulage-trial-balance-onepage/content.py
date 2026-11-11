"""Trial Balance of Northbound Freight: the business and everything the
document could say. The typesetting keeps what fits into one page, the most
important first."""

BUSINESS = {
    "name": "Northbound Freight",
    "author": "Northbound Freight Ltd, accounts office",
}

# code, account, group, debit (+) or credit (−) balance, £
ACCOUNTS = [
    ("0010", "Tractor units, cost", "Fixed assets", 1_284_000),
    ("0011", "Tractor units, depreciation", "Fixed assets", -512_400),
    ("0020", "Trailers, cost", "Fixed assets", 386_000),
    ("0021", "Trailers, depreciation", "Fixed assets", -171_200),
    ("0030", "Yard and workshop equipment", "Fixed assets", 92_600),
    ("0031", "Yard equipment, depreciation", "Fixed assets", -48_900),
    ("1100", "Trade debtors", "Current assets", 618_300),
    ("1110", "Bad debt provision", "Current assets", -14_200),
    ("1200", "Bank: current account", "Current assets", 87_450),
    ("1210", "Bank: fuel card account", "Current assets", 12_000),
    ("1300", "Diesel and AdBlue in tank", "Current assets", 21_380),
    ("1310", "Tyres and parts in stores", "Current assets", 34_700),
    ("1400", "Prepayments: insurance", "Current assets", 46_200),
    ("2100", "Trade creditors", "Liabilities", -284_600),
    ("2200", "VAT", "Liabilities", -71_830),
    ("2210", "PAYE and National Insurance", "Liabilities", -48_920),
    ("2300", "Accruals", "Liabilities", -39_100),
    ("2400", "Asset finance: tractor units", "Liabilities", -648_000),
    ("2410", "Bank loan: yard", "Liabilities", -142_500),
    ("3000", "Share capital", "Equity", -100_000),
    ("3100", "Retained earnings brought forward", "Equity", -200_790),
    ("4000", "Haulage revenue: contract", "Revenue", -3_418_000),
    ("4010", "Haulage revenue: spot", "Revenue", -706_400),
    ("4020", "Fuel surcharge recovered", "Revenue", -284_100),
    ("5000", "Drivers' wages", "Direct costs", 1_486_200),
    ("5010", "Diesel and AdBlue", "Direct costs", 1_126_400),
    ("5020", "Tyres, repairs and maintenance", "Direct costs", 286_900),
    ("5030", "Tolls, ferries and crossings", "Direct costs", 114_300),
    ("5040", "Subcontract hauliers", "Direct costs", 298_700),
    ("6000", "Office and transport managers", "Overheads", 248_600),
    ("6010", "Vehicle insurance", "Overheads", 138_400),
    ("6020", "Yard rent and rates", "Overheads", 72_000),
    ("6030", "Telematics and software", "Overheads", 31_200),
    ("6040", "Depreciation charge", "Overheads", 231_600),
    ("6050", "Finance interest", "Overheads", 43_800),
    ("6060", "Other overheads", "Overheads", 30_210),
]


def gbp(value):
    return f"{value:,.2f}" if value else ""


DEBITS = sum(a[3] for a in ACCOUNTS if a[3] > 0)
CREDITS = -sum(a[3] for a in ACCOUNTS if a[3] < 0)
GROUPS = []
for _, _, group, _ in ACCOUNTS:
    if group not in GROUPS:
        GROUPS.append(group)


def group_rows(group):
    rows = [{"cells": ["", group, "", ""], "style": "section"}]
    for code, name, g, value in ACCOUNTS:
        if g == group:
            rows.append({"cells": [code, name, gbp(max(value, 0)),
                                   gbp(max(-value, 0))],
                         "style": "indent"})
    return rows


REVENUE = -sum(a[3] for a in ACCOUNTS if a[2] == "Revenue")
COSTS = sum(a[3] for a in ACCOUNTS if a[2] in ("Direct costs",
                                               "Overheads"))

DOCUMENT = {
    "title": "Trial Balance",
    "eyebrow": "NORTHBOUND FREIGHT LTD · NOMINAL LEDGER",
    "subtitle": "At 31 March 2028, after year-end adjustments · "
                "36 accounts",
    "meta": [("Period", "FY 2027/28"), ("Debits", f"£{DEBITS:,.2f}"),
             ("Credits", f"£{CREDITS:,.2f}"),
             ("Difference", f"£{DEBITS - CREDITS:,.2f}"),
             ("Run", "08 Apr 2028 09:14")],
    "sections": [
        {"heading": "Balances by group", "kind": "table", "whole": True,
         "weight": 0.1, "max_pages": 1,
         "columns": [("Group", 3.6), ("Debit £", 1.2, "end"),
                     ("Credit £", 1.2, "end")],
         "rows": [[g, gbp(max(sum(a[3] for a in ACCOUNTS if a[2] == g), 0)),
                   gbp(max(-sum(a[3] for a in ACCOUNTS if a[2] == g), 0))]
                  for g in GROUPS]
         + [{"cells": ["Totals", gbp(sum(max(sum(
             a[3] for a in ACCOUNTS if a[2] == g), 0) for g in GROUPS)),
                       gbp(sum(max(-sum(a[3] for a in ACCOUNTS
                                        if a[2] == g), 0)
                               for g in GROUPS))], "style": "total"}]},
        {"heading": "Balances", "kind": "table", "whole": True,
         "weight": 0.1, "min_pages": 2,
         "columns": [("Code", 0.6), ("Account", 3), ("Debit £", 1.2,
                                                     "end"),
                     ("Credit £", 1.2, "end")],
         "rows": [row for g in GROUPS for row in group_rows(g)]
         + [{"cells": ["", "Totals", gbp(DEBITS), gbp(CREDITS)],
             "style": "total"}]},
        {"kind": "callout", "weight": 0.2, "tone": "good",
         "label": "Balanced:",
         "text": f"debits and credits both total £{DEBITS:,.2f}. The "
                 f"ledger shows a profit before tax of "
                 f"£{REVENUE - COSTS:,.0f} for the year."},
        {"heading": "Ledger by group", "kind": "figure", "weight": 0.3,
         "height": 165, "charts": [{"type": "bars",
          "horizontal": True, "format": "£{:,.0f}k",
          "subtitle": "net balance by group, £k",
          "categories": GROUPS,
          "series": [{"name": "Net balance", "values": [
              round(abs(sum(a[3] for a in ACCOUNTS if a[2] == g)) / 1000)
              for g in GROUPS],
              "colors": ["info", "info", "warn", "warn", "good", "bad",
                         "bad"]}]}]},
        {"heading": "Year-end journals", "kind": "table", "whole": True,
         "weight": 0.4, "min_pages": 2,
         "columns": [("Ref", 0.6), ("Journal", 3), ("Debit", 1.2,
                                                     "end"),
                     ("Credit", 1.2, "end")],
         "rows": [["J41", "Depreciation for the year: 6040 / 0011, 0021, "
                   "0031", "231,600.00", "231,600.00"],
                  ["J42", "Insurance prepaid for April – June: 1400 / "
                   "6010", "46,200.00", "46,200.00"],
                  ["J43", "Fuel in tank at the count: 1300 / 5010",
                   "21,380.00", "21,380.00"],
                  ["J44", "Accrued tolls and subcontract invoices: "
                   "5030, 5040 / 2300", "39,100.00", "39,100.00"],
                  ["J45", "Bad debt provision, Medway Foods: 6060 / 1110",
                   "14,200.00", "14,200.00"]]},
        {"heading": "Where revenue goes", "kind": "figure",
         "weight": 0.5, "min_pages": 2, "height": 170, "charts": [{
             "type": "sankey", "format": "£{:,.0f}k", "size": 6.5,
             "nodes": [{"id": "c", "label": "Contract", "col": 0,
                        "color": 0},
                       {"id": "s", "label": "Spot", "col": 0, "color": 2},
                       {"id": "f", "label": "Fuel surcharge", "col": 0,
                        "color": 1},
                       {"id": "r", "label": "Revenue", "col": 1,
                        "color": 0},
                       {"id": "d", "label": "Drivers", "col": 2,
                        "color": 0},
                       {"id": "fu", "label": "Fuel", "col": 2, "color": 1},
                       {"id": "v", "label": "Vehicles", "col": 2,
                        "color": 2},
                       {"id": "o", "label": "Overheads", "col": 2,
                        "color": 4},
                       {"id": "p", "label": "Profit", "col": 2,
                        "color": "good"}],
             "links": [("c", "r", 3418), ("s", "r", 706), ("f", "r", 284),
                       ("r", "d", 1486), ("r", "fu", 1126),
                       ("r", "v", 1114), ("r", "o", 382),
                       ("r", "p", REVENUE // 1000 - 4108)]}]},
        {"heading": "Control accounts", "kind": "table", "whole": True,
         "weight": 0.6, "min_pages": 4,
         "badges": {"Agreed": "good"},
         "columns": [("Control account", 2.6), ("Ledger", 1.2, "end"),
                     ("Sub-ledger or statement", 1.4, "end"),
                     ("", 0.9, "center")],
         "rows": [["1100 Trade debtors", "618,300.00", "618,300.00",
                   "Agreed"],
                  ["2100 Trade creditors", "284,600.00", "284,600.00",
                   "Agreed"],
                  ["1200 Bank current account", "87,450.00",
                   "87,450.00", "Agreed"],
                  ["2200 VAT", "71,830.00", "71,830.00", "Agreed"],
                  ["2210 PAYE and NI", "48,920.00", "48,920.00",
                   "Agreed"],
                  ["2400 Asset finance", "648,000.00", "648,000.00",
                   "Agreed"]]},
        {"heading": "Checks", "kind": "bullets", "weight": 0.7,
         "step": 0.1, "min_pages": 4, "items": [
             "Suspense account 9999 is nil.",
             "Bank accounts reconciled to statements at 31 March.",
             "Fixed asset register agrees to accounts 0010 to 0031.",
             "VAT account agrees to the return for the quarter to "
             "31 March.",
             "Fuel card account 1210 agrees to the card statement.",
         ]},
        {"heading": "Costs per mile from the ledger", "kind": "figure",
         "weight": 0.8, "min_pages": 4, "height": 150, "charts": [{
             "type": "donut", "format": "£{:,.0f}k",
             "segments": [("Drivers", 1486), ("Fuel", 1126),
                          ("Subcontract", 299), ("Repairs and tyres",
                                                 287),
                          ("Depreciation and interest", 275),
                          ("Insurance", 138), ("Other", 496)],
             "center": (f"£{COSTS / 1e6:.2f}m", "costs")}]},
        {"heading": "Notes", "kind": "text", "weight": 0.9, "step": 0.3,
         "min_pages": 4, "paragraphs": [
             "Debit balances are assets and expenses, credit balances "
             "liabilities, equity and income. This trial balance is "
             "after the year-end journals J41 to J45 and before the "
             "tax charge, which the accountants will add.",
         ]},
    ],
}
