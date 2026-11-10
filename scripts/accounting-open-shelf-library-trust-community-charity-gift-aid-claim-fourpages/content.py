"""Gift Aid Claim of Open Shelf Library Trust: the business and everything the
document could say. The typesetting keeps what fits into four pages, the
most important first."""

BUSINESS = {
    "name": "Open Shelf Library Trust",
    "author": "Raj Patel, treasurer",
}

RATE = 0.25  # Gift Aid adds 25p to every £1 donated
# donor ref, title, first name, surname, house, postcode, date, amount
DONATIONS = [
    ("D0012", "Mrs", "Edith", "Ainsworth", "14", "HU5 2LP", "03/04/27", 50.00),
    ("D0031", "Mr", "Kwame", "Boateng",
     "Flat 2", "HU1 3RT", "05/04/27", 25.00),
    ("D0047", "Dr", "Helen", "Ashworth", "The Old Rectory", "HU16 4BX",
     "12/04/27", 250.00),
    ("D0088", "Ms", "Priya", "Desai", "71", "HU3 6QD", "19/04/27", 20.00),
    ("D0102", "Mr", "Tom", "Fletcher", "8", "HU9 1JS", "30/04/27", 100.00),
    ("D0115", "Mrs", "Anne", "Gallagher", "22", "HU6 7PL", "02/05/27", 15.00),
    ("D0131", "Mr", "Lukas", "Hoffmann", "5", "HU10 6AB", "14/05/27", 60.00),
    ("D0156", "Ms", "Grace", "Igwe", "Flat 9", "HU2 8DS", "21/05/27", 10.00),
    ("D0177", "Mr", "Oliver", "Jensen", "40", "HU5 3HQ", "28/05/27", 500.00),
    ("D0189", "Mrs", "Sarah", "Khan", "17", "HU8 9TT", "03/06/27", 30.00),
    ("D0203", "Mr", "David", "Lowe", "2", "HU12 8AE", "11/06/27", 40.00),
    ("D0219", "Ms", "Mei", "Lin", "63", "HU4 7NR", "18/06/27", 75.00),
    ("D0230", "Mr", "Patrick", "Murphy", "9", "HU7 4XZ", "25/06/27", 20.00),
]
AGGREGATED = [("Collection boxes, Northgate library", 412.60),
              ("Collection boxes, mobile library", 186.30)]
REGULAR = (214, 4_318.00)   # monthly donors and their gifts, quarter


def gbp(value):
    return f"£{value:,.2f}"


LISTED = round(sum(d[7] for d in DONATIONS), 2)
AGG = round(sum(a for _, a in AGGREGATED), 2)
TOTAL = round(LISTED + AGG + REGULAR[1], 2)
CLAIM = round(TOTAL * RATE, 2)

DOCUMENT = {
    "title": "Gift Aid Claim",
    "eyebrow": "Open Shelf Library Trust · HMRC charity ref. XT41827",
    "subtitle": "Claim 27-1 · donations received 1 April to 30 June 2027",
    "meta": [("Charity ref.", "XT41827"), ("Period", "Apr – Jun 2027"),
             ("Donations", gbp(TOTAL)), ("Tax claimed", gbp(CLAIM)),
             ("Submitted", "8 Jul 2027")],
    "sections": [
        {"heading": "Claim summary", "kind": "table", "whole": True,
         "weight": 0.1,
         "columns": [("Line", 0.5), ("Description", 3.4),
                     ("Amount", 1, "end")],
         "rows": [["1", f"Regular monthly donors ({REGULAR[0]} people)",
                   gbp(REGULAR[1])],
                  ["2", f"One-off donations listed below "
                        f"({len(DONATIONS)} donors)", gbp(LISTED)],
                  ["3", "Small cash donations (under £30, GASDS)",
                   gbp(AGG)],
                  {"cells": ["4", "Total donations", gbp(TOTAL)],
                   "style": "subtotal"},
                  {"cells": ["5", "Gift Aid claimed at 25 %", gbp(CLAIM)],
                   "style": "total"}]},
        {"heading": "Declaration", "kind": "callout", "weight": 0.15,
         "tone": "accent", "label": "The authorised official declares",
         "text": "that every donor has made a valid Gift Aid declaration, "
                 "that no donor received benefits above the limits, and "
                 "that records will be kept for six years. — Raj Patel, "
                 "treasurer"},
        {"heading": "Schedule of donations", "kind": "table",
         "weight": 0.2, "step": 0.02,
         "columns": [("Ref", 0.6), ("Title", 0.5), ("First name", 0.9),
                     ("Surname", 1), ("House", 1.1), ("Postcode", 0.8),
                     ("Date", 0.8), ("Amount", 0.8, "end")],
         "rows": [[r, t, f, s, h, p, d, gbp(a)]
                  for r, t, f, s, h, p, d, a in DONATIONS]},
        {"heading": "Aggregated donations", "kind": "table",
         "whole": True, "weight": 0.3, "min_pages": 2,
         "columns": [("Source", 3.4), ("Amount", 1, "end")],
         "rows": [[n, gbp(a)] for n, a in AGGREGATED]
         + [{"cells": ["Total", gbp(AGG)], "style": "subtotal"}]},
        {"heading": "The quarter in numbers", "kind": "figure",
         "weight": 0.4, "min_pages": 2, "height": 140, "widths": [2, 3],
         "charts": [
             {"type": "donut", "title": "Donations",
              "segments": [("Monthly donors", REGULAR[1]),
                           ("One-off", LISTED), ("Small cash", AGG)],
              "format": "£{:,.0f}", "center": (gbp(TOTAL)[:-3], "given")},
             {"type": "bars", "title": "Gift Aid by quarter",
              "subtitle": "£", "format": "{:,.0f}",
              "categories": ["Q1 26", "Q2 26", "Q3 26", "Q4 26",
                             "Q1 27"],
              "series": [{"name": "Claimed", "values": [1_386, 1_412,
                                                        1_655, 2_204,
                                                        CLAIM],
                          "colors": [4, 4, 4, 4, 0]}]},
         ]},
        {"heading": "Declarations check", "kind": "figure",
         "weight": 0.5, "min_pages": 4, "height": 120, "charts": [{
             "type": "progress", "format": "{:.0f} %", "items": [
                 {"label": "Donors with a declaration on file",
                  "value": 100, "status": "good"},
                 {"label": "Declarations with a full address",
                  "value": 97, "target": 100, "status": "warn",
                  "note": "7 monthly donors asked to update"},
                 {"label": "Donors who are UK taxpayers (confirmed)",
                  "value": 100, "status": "good"},
                 {"label": "New declarations this quarter", "value": 38,
                  "status": 0, "display": "38"}]}]},
        {"heading": "Excluded from the claim", "kind": "table",
         "whole": True, "weight": 0.6, "min_pages": 4,
         "columns": [("Donation", 2.6), ("Amount", 1, "end"),
                     ("Why excluded", 2.6)],
         "rows": [["Book sale proceeds", "£1,840.00",
                   "Payment for goods, not a gift"],
                  ["Friends' membership with free café drink", "£360.00",
                   "Benefit above the limit"],
                  ["Company donation, Harbour Print Ltd", "£500.00",
                   "Companies cannot use Gift Aid"],
                  ["Two donors without declarations", "£45.00",
                   "Declaration requested"]]},
        {"heading": "Rules we follow", "kind": "bullets", "weight": 0.7,
         "step": 0.1, "min_pages": 4, "items": [
             "Gift Aid is claimed only on gifts of the donor's own money "
             "from UK taxpayers who have made a declaration.",
             "Benefits to donors (a mug, a café voucher) must stay "
             "within the HMRC limits.",
             "Small cash donations under £30 are claimed under the Gift "
             "Aid Small Donations Scheme, up to £8,000 a year.",
             "Claims are made quarterly, within four years of the end of "
             "the financial year of the donation.",
         ]},
        {"heading": "Monthly donors", "kind": "figure", "weight": 0.8,
         "min_pages": 4, "height": 140, "charts": [{"type": "line",
          "subtitle": "number of people giving monthly",
          "x": ["Jul 26", "Sep", "Nov", "Jan 27", "Mar", "May", "Jun"],
          "format": "{:.0f}", "end_labels": True,
          "series": [{"name": "Monthly donors", "area": True,
                      "values": [168, 174, 181, 196, 203, 209,
                                 REGULAR[0]]}]}]},
        {"heading": "Donations by size", "kind": "figure", "weight": 0.9,
         "min_pages": 4, "height": 150, "widths": [3, 2], "charts": [
             {"type": "bars", "title": "One-off donations",
              "subtitle": "number of gifts", "format": "{:.0f}",
              "categories": ["Under £25", "£25 – £49", "£50 – £99",
                             "£100 – £249", "£250 and over"],
              "series": [{"name": "Gifts", "values": [
                  sum(1 for d in DONATIONS if d[7] < 25),
                  sum(1 for d in DONATIONS if 25 <= d[7] < 50),
                  sum(1 for d in DONATIONS if 50 <= d[7] < 100),
                  sum(1 for d in DONATIONS if 100 <= d[7] < 250),
                  sum(1 for d in DONATIONS if d[7] >= 250)]}]},
             {"type": "gauges", "items": [
                 {"label": "GASDS used this year", "value": AGG,
                  "max": 8000, "status": 0,
                  "display": f"£{AGG:,.0f}", "note": "limit £8,000"}]},
         ]},
        {"heading": "Claim history", "kind": "table", "whole": True,
         "weight": 1.0, "min_pages": 4,
         "badges": {"Paid": "good", "Pending": "warn"},
         "columns": [("Claim", 0.8), ("Period", 1.6),
                     ("Donations", 1, "end"), ("Tax claimed", 1, "end"),
                     ("", 0.8, "center")],
         "rows": [["26-1", "Apr – Jun 2026", "£5,544.00", "£1,386.00",
                   "Paid"],
                  ["26-2", "Jul – Sep 2026", "£5,648.00", "£1,412.00",
                   "Paid"],
                  ["26-3", "Oct – Dec 2026", "£6,620.00", "£1,655.00",
                   "Paid"],
                  ["26-4", "Jan – Mar 2027", "£8,816.00", "£2,204.00",
                   "Paid"],
                  ["27-1", "Apr – Jun 2027", gbp(TOTAL), gbp(CLAIM),
                   "Pending"]]},
        {"heading": "Audit trail", "kind": "text", "weight": 1.1,
         "step": 0.2, "min_pages": 4, "paragraphs": [
             "Each donation in this claim can be traced from the bank "
             "statement to the donor record and the declaration. Monthly "
             "donors are listed in the separate schedule uploaded with "
             "the claim, as HMRC allows for claims of over 1,000 lines.",
         ]},
        {"heading": "Where donors live", "kind": "figure", "weight": 1.2,
         "min_pages": 4, "height": 140, "charts": [{"type": "bars",
          "horizontal": True, "title": "Donors by postcode district",
          "format": "{:.0f}",
          "categories": ["HU5", "HU6", "HU3", "HU8", "HU16", "HU10",
                         "Elsewhere"],
          "series": [{"name": "Donors", "values": [48, 39, 31, 27, 22, 19,
                                                   41]}]}]},
    ],
}
