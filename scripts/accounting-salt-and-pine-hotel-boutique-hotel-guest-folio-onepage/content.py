"""Guest Folio of Salt & Pine Hotel: the business and everything the document
could say. The typesetting keeps what fits into one page, the most important
first."""

BUSINESS = {
    "name": "Salt & Pine Hotel",
    "author": "Salt & Pine Hotel, front office",
}

NIGHTS = ["Thu 14 Oct", "Fri 15 Oct", "Sat 16 Oct", "Sun 17 Oct"]
RATES = [295.00, 345.00, 345.00, 265.00]
# date, outlet, description, amount incl. VAT
CHARGES = [("14 Oct", "Restaurant", "Dinner for two, table 7", 148.50),
           ("14 Oct", "Bar", "Two glasses of English sparkling", 26.00),
           ("15 Oct", "Spa", "Seaweed wrap and massage, 2 × 60 min",
            230.00),
           ("15 Oct", "Restaurant", "Tasting menu with wine pairing × 2",
            310.00),
           ("16 Oct", "Picnic", "Beach picnic hamper", 64.00),
           ("16 Oct", "Bar", "Cocktails on the terrace", 38.50),
           ("17 Oct", "Restaurant", "Dinner for two", 132.00),
           ("17 Oct", "Shop", "Salt & Pine bath salts", 18.00)]
CITY_TAX = 2.50 * 2 * 4       # per person per night



def gbp(value):
    sign = "−" if value < 0 else ""
    return f"{sign}£{abs(value):,.2f}"


ROOMS = sum(RATES)
EXTRAS = round(sum(c[3] for c in CHARGES), 2)
TOTAL = round(ROOMS + EXTRAS + CITY_TAX, 2)
BALANCE_PAID = round(TOTAL - 295.00, 2)
VAT = round((ROOMS + EXTRAS) / 6, 2)

DOCUMENT = {
    "title": "Guest Folio",
    "eyebrow": "Salt & Pine · a hotel by the dunes",
    "subtitle": "Mr and Mrs E. Okonkwo · Dune Suite 12 · 14 – 18 October "
                "2027 · four nights",
    "meta": [("Folio", "F-27-10418"), ("Room", "Dune Suite 12"),
             ("Arrival", "14 Oct 2027"), ("Departure", "18 Oct 2027"),
             ("Balance", "£0.00")],
    "sections": [
        {"heading": "Accommodation", "kind": "table", "whole": True,
         "weight": 0.1,
         "columns": [("Night", 1.2), ("Room and rate", 3),
                     ("Amount", 1, "end")],
         "rows": [[n, "Dune Suite, bed and breakfast for two", gbp(r)]
                  for n, r in zip(NIGHTS, RATES)]
         + [{"cells": ["", "Accommodation", gbp(ROOMS)],
             "style": "subtotal"}]},
        {"heading": "Charges", "kind": "table", "whole": True,
         "weight": 0.2,
         "columns": [("Date", 0.8), ("Outlet", 1.1), ("Description", 2.6),
                     ("Amount", 1, "end")],
         "rows": [[d, o, t, gbp(a)] for d, o, t, a in CHARGES]
         + [{"cells": ["", "", "Charges", gbp(EXTRAS)],
             "style": "subtotal"}]},
        {"heading": "Summary", "kind": "table", "whole": True,
         "weight": 0.3, "columns": [("", 3.6), ("Amount", 1, "end")],
         "rows": [["Accommodation", gbp(ROOMS)],
                  ["Food, drink, spa and shop", gbp(EXTRAS)],
                  ["Visitor levy, £2.50 per person per night",
                   gbp(CITY_TAX)],
                  {"cells": ["Total", gbp(TOTAL)], "style": "subtotal"},
                  {"cells": ["Deposit paid 12 August", gbp(-295.00)],
                   "style": "indent"},
                  {"cells": ["Paid on departure, card ending 4412",
                             gbp(-BALANCE_PAID)], "style": "indent"},
                  {"cells": ["Balance", "£0.00"], "style": "total"},
                  {"cells": [f"VAT at 20 % included: {gbp(VAT)}", ""],
                   "style": "muted"}]},
        {"kind": "motto", "weight": 0.4, "min_pages": 2,
         "text": "Thank you for staying with us. The tide tables for "
                 "your next visit are on our website."},
        {"heading": "Your stay", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": 150, "widths": [2, 3], "charts": [
             {"type": "donut", "title": "Where it went",
              "segments": [("Suite", ROOMS), ("Restaurant", 590.50),
                           ("Spa", 230.00), ("Bar", 64.50),
                           ("Picnic and shop", 82.00)],
              "format": "£{:,.0f}", "center": (gbp(TOTAL)[:-3], "stay")},
             {"type": "bars", "title": "By night", "stacked": True,
              "format": "£{:,.0f}", "values": False,
              "categories": [n.split()[0] for n in NIGHTS],
              "series": [{"name": "Room", "values": RATES},
                         {"name": "Extras", "color": 1,
                          "values": [174.50, 540.00, 102.50, 150.00]}]},
         ]},
        {"heading": "Rates explained", "kind": "bullets", "weight": 0.6,
         "step": 0.1, "min_pages": 2, "items": [
             "Friday and Saturday nights are charged at the weekend "
             "rate of £345.",
             "Sunday night is at the 'stay longer' rate of £265.",
             "Breakfast for two is included in every room rate.",
             "The visitor levy goes to the council for the dunes and "
             "the beach.",
         ]},
        {"heading": "Payments", "kind": "table", "whole": True,
         "weight": 0.7, "min_pages": 4,
         "columns": [("Date", 1), ("Method", 2.6), ("Amount", 1, "end")],
         "rows": [["12 Aug", "Deposit, card ending 4412, on booking",
                   gbp(295.00)],
                  ["18 Oct", "Card ending 4412, chip and PIN, 10:42",
                   gbp(BALANCE_PAID)],
                  {"cells": ["", "Total paid", gbp(TOTAL)],
                   "style": "total"}]},
        {"heading": "VAT analysis", "kind": "table", "whole": True,
         "weight": 0.8, "min_pages": 4,
         "columns": [("Rate", 1.6), ("Net", 1, "end"), ("VAT", 1, "end"),
                     ("Gross", 1, "end")],
         "rows": [["Standard 20 %", gbp(ROOMS + EXTRAS - VAT), gbp(VAT),
                   gbp(ROOMS + EXTRAS)],
                  ["Outside the scope (levy)", gbp(CITY_TAX), "£0.00",
                   gbp(CITY_TAX)],
                  {"cells": ["Total", gbp(TOTAL - VAT), gbp(VAT),
                             gbp(TOTAL)], "style": "total"}]},
        {"heading": "From your hosts", "kind": "text", "weight": 0.9,
         "step": 0.3, "min_pages": 4, "paragraphs": [
             "We hope the sea air did you good. Your dietary notes and "
             "your preference for a room facing the dunes are on our "
             "records, with your permission, for your next stay.",
             "Returning guests receive a bottle of Hollow Oak sparkling "
             "and late checkout, subject to availability.",
         ]},
        {"heading": "Hotel details", "kind": "tags", "weight": 1.0,
         "step": 0.1, "min_pages": 4, "items": [
             ("Address", "Salt & Pine Hotel, Dune Road, Holkham NR23 1RQ"),
             ("Telephone", "01328 555 0170"),
             ("VAT", "GB 299 1046 82"),
             ("Company", "Salt & Pine Hotel Ltd, no. 09482211"),
         ]},
        {"heading": "Rate calendar", "kind": "figure", "weight": 1.1,
         "min_pages": 4, "height": 140, "charts": [{"type": "line",
          "subtitle": "Dune Suite, £ a night, autumn 2027",
          "x": ["Sep", "Oct", "Nov", "Dec", "Jan", "Feb"],
          "format": "{:.0f}",
          "series": [{"name": "Weekday", "values": [310, 295, 245, 265,
                                                    215, 225]},
                     {"name": "Weekend", "color": 1,
                      "values": [365, 345, 285, 330, 255, 265]}]}]},
        {"heading": "Your feedback", "kind": "figure", "weight": 1.2,
         "min_pages": 4, "height": 140, "charts": [{"type": "progress",
          "format": "{:.0f} / 10", "max": 10, "items": [
              {"label": "Room", "value": 10, "status": "good"},
              {"label": "Breakfast", "value": 9, "status": "good"},
              {"label": "Dinner", "value": 9, "status": "good"},
              {"label": "Spa", "value": 10, "status": "good"},
              {"label": "Value for money", "value": 8, "status": 0}]}]},
        {"heading": "Next time", "kind": "entries", "weight": 1.3,
         "step": 0.2, "inner": 0.1, "min_pages": 4, "entries": [
             {"title": "Winter breaks", "text": [
                 "Three nights for the price of two with dinner, "
                 "November to March, booked direct."]},
             {"title": "The seal trips", "text": [
                 "Boats from Morston to Blakeney Point; we book the "
                 "morning tide for you."]},
         ]},
        {"heading": "Your loyalty", "kind": "figure", "weight": 1.4,
         "min_pages": 4, "height": 140, "charts": [{"type": "bars",
          "subtitle": "nights stayed with us each year",
          "categories": ["2023", "2024", "2025", "2026", "2027"],
          "series": [{"name": "Nights", "values": [2, 3, 3, 5, 4],
                      "colors": [4, 4, 4, 4, 0]}]}]},
    ],
}
