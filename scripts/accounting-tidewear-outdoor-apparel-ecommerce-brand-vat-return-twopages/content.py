"""VAT Return of Tidewear: the business and everything the document could say.
The typesetting keeps what fits into two pages, the most important first."""

BUSINESS = {
    "name": "Tidewear",
    "author": "Tidewear Outdoor Ltd, finance",
}

# net sales and VAT for the quarter (£), by kind
SALES = [("Web shop, UK customers", 612_400, 0.20),
         ("Marketplaces, UK customers", 238_900, 0.20),
         ("Wholesale, UK stockists", 196_300, 0.20),
         ("Children's clothing (zero-rated)", 21_600, 0.0),
         ("Exports outside the UK", 48_200, 0.0)]
PURCHASES = [("Imported goods, postponed VAT", 402_000, 0.20),
             ("Marketing and advertising", 141_800, 0.20),
             ("Fulfilment and postage", 63_400, 0.20),
             ("Rent and services", 52_000, 0.20),
             ("Software and other overheads", 38_600, 0.20),
             ("Insurance, wages and other exempt", 214_700, 0.0)]
BAD_DEBT_RELIEF = 640.00
ERROR_CORRECTION = -1_120.00   # under-declared VAT from last quarter


def gbp(value):
    sign = "−" if value < 0 else ""
    return f"{sign}£{abs(value):,.2f}"


BOX1 = round(sum(n * r for _, n, r in SALES)
             + 402_000 * 0.20 - ERROR_CORRECTION, 2)
BOX2 = 0.00
BOX3 = round(BOX1 + BOX2, 2)
BOX4 = round(sum(n * r for _, n, r in PURCHASES) + BAD_DEBT_RELIEF, 2)
BOX5 = round(BOX3 - BOX4, 2)
BOX6 = round(sum(n for _, n, _ in SALES))
BOX7 = round(sum(n for _, n, _ in PURCHASES))
BOX8 = 0
BOX9 = 0
BOXES = [("1", "VAT due on sales and other outputs", gbp(BOX1)),
         ("2", "VAT due on acquisitions from the EU (Northern "
               "Ireland only)", gbp(BOX2)),
         ("3", "Total VAT due (box 1 + box 2)", gbp(BOX3)),
         ("4", "VAT reclaimed on purchases and other inputs", gbp(BOX4)),
         ("5", "Net VAT to pay to HMRC (box 3 − box 4)", gbp(BOX5)),
         ("6", "Total value of sales, excluding VAT", f"£{BOX6:,}"),
         ("7", "Total value of purchases, excluding VAT", f"£{BOX7:,}"),
         ("8", "Supplies of goods to the EU (Northern Ireland only)",
          f"£{BOX8:,}"),
         ("9", "Acquisitions of goods from the EU (Northern Ireland "
               "only)", f"£{BOX9:,}")]

DOCUMENT = {
    "title": "VAT Return",
    "eyebrow": "Tidewear Outdoor Ltd · VAT registration GB 401 2288 61",
    "subtitle": "Period 08/27 · 1 August to 31 October 2027 · Making Tax "
                "Digital submission",
    "meta": [("VRN", "401 2288 61"), ("Period", "Aug – Oct 2027"),
             ("Net VAT due", gbp(BOX5)), ("Due", "7 Dec 2027"),
             ("Submitted", "29 Nov 2027")],
    "sections": [
        {"heading": "The return", "kind": "table", "whole": True,
         "weight": 0.1, "badges": {gbp(BOX5): "warn"},
         "columns": [("Box", 0.5), ("Description", 4),
                     ("Amount", 1.2, "end")],
         "rows": [list(b) if b[0] != "5" else
                  {"cells": list(b), "style": "total"} for b in BOXES]},
        {"heading": "Declaration", "kind": "callout", "weight": 0.2,
         "tone": "accent", "label": "Submitted through the software",
         "text": "by Nadia Okafor, financial controller, on 29 November "
                 "2027, with the declaration that the information is "
                 "true and complete. Payment by direct debit on 10 "
                 "December 2027."},
        {"heading": "Box 1 workings: VAT on sales", "kind": "table",
         "whole": True, "weight": 0.3,
         "columns": [("Supply", 3), ("Net", 1, "end"),
                     ("Rate", 0.6, "end"), ("VAT", 1, "end")],
         "rows": [[n, f"£{v:,}", f"{r:.0%}", gbp(v * r)]
                  for n, v, r in SALES]
         + [["Postponed import VAT (also reclaimed in box 4)",
             "£402,000", "20%", gbp(402_000 * 0.2)],
            ["Correction of an error in period 05/27", "", "",
             gbp(-ERROR_CORRECTION)],
            {"cells": ["Box 1", "", "", gbp(BOX1)],
             "style": "subtotal"}]},
        {"heading": "Box 4 workings: VAT on purchases", "kind": "table",
         "whole": True, "weight": 0.4, "min_pages": 2,
         "columns": [("Purchase", 3), ("Net", 1, "end"),
                     ("Rate", 0.6, "end"), ("VAT", 1, "end")],
         "rows": [[n, f"£{v:,}", f"{r:.0%}", gbp(v * r)]
                  for n, v, r in PURCHASES]
         + [["Bad debt relief, Fell Outdoors (in administration)", "",
             "", gbp(BAD_DEBT_RELIEF)],
            {"cells": ["Box 4", "", "", gbp(BOX4)],
             "style": "subtotal"}]},
        {"heading": "Where the VAT comes from", "kind": "figure",
         "weight": 0.5, "min_pages": 2, "height": 150, "charts": [{
             "type": "waterfall", "format": "£{:,.0f}k",
             "axis_format": "{:,.0f}", "total_color": 0,
             "steps": [("Output VAT, sales", round(sum(
                 n * r for _, n, r in SALES) / 1000, 1)),
                       ("Import VAT due", 80.4),
                       ("Correction", -ERROR_CORRECTION / 1000),
                       ("Import VAT reclaimed", -80.4),
                       ("Input VAT, costs", -round(
                           (BOX4 - 80_400 - BAD_DEBT_RELIEF) / 1000, 1)),
                       ("Bad debt relief", -BAD_DEBT_RELIEF / 1000),
                       ("To pay", None)]}]},
        {"heading": "Checks", "kind": "table", "whole": True,
         "weight": 0.6, "min_pages": 4, "badges": {"OK": "good",
                                                   "Note": "warn"},
         "columns": [("Check", 4), ("", 0.8, "center")],
         "rows": [["Box 6 agrees to the sales ledger for the quarter",
                   "OK"],
                  ["Postponed import VAT agrees to the monthly "
                   "statements from the customs service", "OK"],
                  ["Marketplace sales where the marketplace accounts "
                   "for VAT are excluded", "OK"],
                  ["Bad debt over six months old and written off",
                   "OK"],
                  ["Error under £10,000: corrected on this return, not "
                   "by separate disclosure", "Note"]]},
        {"heading": "VAT paid over the year", "kind": "figure",
         "weight": 0.7, "min_pages": 4, "height": 140, "charts": [{
             "type": "bars", "subtitle": "£k net VAT by quarter",
             "format": "{:,.1f}", "categories": ["11/26", "02/27", "05/27",
                                                 "08/27"],
             "series": [{"name": "Net VAT", "values": [
                 64.2, 31.8, 38.6, BOX5 / 1000],
                 "colors": [4, 4, 4, 0]}]}]},
        {"heading": "Rates applied", "kind": "tags", "weight": 0.8,
         "step": 0.1, "min_pages": 4, "items": [
             ("Standard 20 %", "adult clothing, accessories, postage"),
             ("Zero rate", "children's clothing for under-14 sizes; "
                           "exports with proof of export"),
             ("Outside the scope", "wages, insurance, bank charges"),
             ("Postponed accounting", "import VAT declared and reclaimed "
                                      "on the same return"),
         ]},
        {"heading": "Notes", "kind": "text", "weight": 0.9, "step": 0.3,
         "min_pages": 4, "paragraphs": [
             "The error in period 05/27 was a batch of web shop sales "
             "coded as children's clothing; the VAT of £1,120 is "
             "included in box 1 of this return. The coding rule in the "
             "shop platform was fixed on 12 September.",
         ]},
        {"heading": "Sales by rate", "kind": "figure", "weight": 1.0,
         "min_pages": 4, "height": 140, "widths": [2, 3], "charts": [
             {"type": "donut", "title": "Box 6",
              "segments": [("Standard rated", 1_047_600),
                           ("Zero rated", 21_600), ("Exports", 48_200)],
              "format": "£{:,.0f}", "center": ("£1.12m", "sales")},
             {"type": "bars", "title": "Output VAT by month", "subtitle":
              "£k", "format": "{:,.1f}",
              "categories": ["August", "September", "October"],
              "series": [{"name": "VAT", "values": [61.4, 66.0,
                                                    82.1]}]},
         ]},
        {"heading": "Calendar", "kind": "table", "whole": True,
         "weight": 1.1, "min_pages": 4,
         "columns": [("Period", 1.4), ("Ends", 1.2), ("File and pay by",
                                                      1.4)],
         "rows": [["08/27", "31 Oct 2027", "7 Dec 2027"],
                  ["11/27", "31 Jan 2028", "7 Mar 2028"],
                  ["02/28", "30 Apr 2028", "7 Jun 2028"]]},
        {"heading": "Payment", "kind": "table", "look": "plain",
         "header": False, "whole": True, "weight": 1.2, "min_pages": 4,
         "columns": [("", 1), ("", 1)],
         "rows": [["**Amount** " + gbp(BOX5),
                   "**Method** direct debit"],
                  ["**Collected** 10 December 2027",
                   "**Reference** 401228861A001"]]},
        {"heading": "Contacts", "kind": "tags", "weight": 1.3,
         "step": 0.1, "min_pages": 4, "items": [
             ("Prepared by", "Nadia Okafor, financial controller"),
             ("Reviewed by", "Tom Rowe, finance director"),
             ("Adviser", "Penhallow & Co, chartered accountants"),
         ]},
    ],
}
