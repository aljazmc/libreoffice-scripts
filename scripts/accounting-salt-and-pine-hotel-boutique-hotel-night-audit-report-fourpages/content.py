"""Night Audit of Salt & Pine Hotel: the business and everything the document
could say. The typesetting keeps what fits into four pages, the most
important first."""

BUSINESS = {
    "name": "Salt & Pine Hotel",
    "author": "Salt & Pine Hotel, night audit",
}

ROOMS = 42
OCCUPIED = 39
OOO = 1  # out of order
GUESTS = 74
# outlet, covers or count, revenue £ net of VAT
OUTLETS = [("Rooms", 39, 11_942.50), ("Restaurant", 86, 4_816.00),
           ("Bar and terrace", 0, 1_288.40), ("Room service", 9, 342.00),
           ("Spa", 14, 1_476.00), ("Shop", 0, 186.70)]
# tender, amount £ including VAT
TENDERS = [("Visa and Mastercard", 14_206.12), ("American Express",
                                                2_118.40),
           ("Cash", 312.00), ("Transfer to city ledger (accounts)",
                              2_604.00), ("Deposits applied", 1_480.00)]


def gbp(value):
    sign = "−" if value < 0 else ""
    return f"{sign}£{abs(value):,.2f}"


REVENUE = round(sum(o[2] for o in OUTLETS), 2)
GROSS = round(REVENUE * 1.2, 2)
TENDERED = round(sum(t[1] for t in TENDERS), 2)
ADR = OUTLETS[0][2] / OCCUPIED
OCC = OCCUPIED / (ROOMS - OOO)

DOCUMENT = {
    "title": "Night Audit",
    "eyebrow": "SALT & PINE · NIGHT AUDIT · BUSINESS DATE SAT 16 OCT 2027",
    "subtitle": "Day closed at 02:14 on 17 October by Tom Achterberg, "
                "night manager",
    "meta": [("Business date", "Sat 16 Oct 2027"),
             ("Occupancy", f"{OCC:.1%}"), ("ADR", gbp(ADR)),
             ("RevPAR", gbp(OUTLETS[0][2] / (ROOMS - OOO))),
             ("Revenue", gbp(REVENUE)),
             ("Unbalanced items", "0")],
    "sections": [
        {"heading": "Revenue by outlet", "kind": "table", "whole": True,
         "weight": 0.1,
         "columns": [("Outlet", 2), ("Covers or rooms", 1, "end"),
                     ("Net revenue", 1.1, "end"),
                     ("Budget", 1.1, "end"), ("Same day last year", 1.2,
                                              "end")],
         "rows": [[o, str(c) if c else "—", gbp(r), gbp(b), gbp(last)]
                  for (o, c, r), b, last in zip(
                      OUTLETS, [11_400, 5_100, 1_200, 300, 1_400, 150],
                      [10_620, 4_388, 1_190, 286, 1_204, 162])]
         + [{"cells": ["Total", "", gbp(REVENUE), gbp(19_550),
                       gbp(17_850)], "style": "total"}]},
        {"heading": "Settlement", "kind": "table", "whole": True,
         "weight": 0.2,
         "columns": [("Tender", 2.6), ("Amount", 1.1, "end")],
         "rows": [[t, gbp(a)] for t, a in TENDERS]
         + [{"cells": ["Total tendered", gbp(TENDERED)],
             "style": "subtotal"},
            {"cells": ["Revenue including VAT", gbp(GROSS)],
             "style": "indent"},
            {"cells": ["Movement on guest ledger (stays continuing)",
                       gbp(round(GROSS - TENDERED, 2))],
             "style": "indent"}]},
        {"heading": "Rooms", "kind": "figure", "weight": 0.3,
         "charts": [{"type": "kpis",
          "tiles": [
              {"label": "Occupied", "value": f"{OCCUPIED} / {ROOMS}",
               "status": 0, "note": f"{OOO} out of order (room 8, leak)"},
              {"label": "Guests", "value": str(GUESTS), "status": 1,
               "note": "in house tonight"},
              {"label": "Arrivals / departures", "value": "14 / 11",
               "status": 2, "note": "2 no-shows charged"},
              {"label": "Average rate", "value": gbp(ADR), "status": 3,
               "note": "net of VAT and breakfast"}]}]},
        {"heading": "Exceptions", "kind": "table", "whole": True,
         "weight": 0.4, "min_pages": 2,
         "badges": {"Resolved": "good", "For the morning": "warn"},
         "columns": [("Time", 0.7), ("Item", 3.6), ("By", 0.9),
                     ("Status", 1.2, "center")],
         "rows": [["21:40", "Room 21 bar charge posted to room 12, moved",
                   "TA", "Resolved"],
                  ["22:15", "Discount of 15 % on table 9: manager's "
                   "approval missing", "TA", "For the morning"],
                  ["00:30", "No-shows rooms 4 and 31 charged one night",
                   "TA", "Resolved"],
                  ["01:05", "Credit limit exceeded, room 17 (£1,840)",
                   "TA", "For the morning"],
                  ["01:50", "Card terminal 2 batch closed, totals agree",
                   "TA", "Resolved"]]},
        {"heading": "The day in numbers", "kind": "figure",
         "weight": 0.5, "min_pages": 2, "height": 150,
         "widths": [2, 3], "charts": [
             {"type": "donut", "title": "Revenue mix",
              "segments": [(o, r) for o, _, r in OUTLETS],
              "format": "£{:,.0f}", "center": (f"£{REVENUE / 1000:.1f}k",
                                               "net")},
             {"type": "bars", "title": "Restaurant covers by hour",
              "categories": ["18:00", "19:00", "20:00", "21:00",
                             "22:00"],
              "series": [{"name": "Covers", "values": [8, 22, 31, 19,
                                                       6]}]},
         ]},
        {"heading": "Guest ledger", "kind": "table", "whole": True,
         "weight": 0.6, "min_pages": 4,
         "columns": [("", 3.4), ("£", 1.1, "end")],
         "rows": [["Opening balance, in-house guests", "14,812.40"],
                  {"cells": ["Charges posted today", gbp(GROSS)],
                   "style": "indent"},
                  {"cells": ["Payments and transfers", gbp(-TENDERED)],
                   "style": "indent"},
                  {"cells": ["Closing balance", gbp(round(
                      14_812.40 + GROSS - TENDERED, 2))],
                   "style": "total"}]},
        {"heading": "Tomorrow", "kind": "table", "whole": True,
         "weight": 0.7, "min_pages": 4,
         "columns": [("", 2.4), ("Number", 1, "end"), ("Note", 3)],
         "rows": [["Arrivals", "9", "Two VIPs: anniversary, room 12"],
                  ["Departures", "23", "Coach party of 18 at 09:00"],
                  ["Occupancy forecast", "68 %", "Sunday rate £265"],
                  ["Restaurant bookings", "54", "Sunday lunch full"],
                  ["Spa bookings", "11", "Two therapists"]]},
        {"heading": "Checks completed", "kind": "bullets",
         "weight": 0.8, "step": 0.1, "min_pages": 4, "items": [
             "Room rates posted to every occupied room and checked "
             "against the booking.",
             "All outlet cashiers closed; point-of-sale totals agree to "
             "the property system.",
             "Card terminal batches settled and agree to the tenders.",
             "Backups run at 02:05; reports printed for the general "
             "manager.",
         ]},
        {"heading": "Occupancy this week", "kind": "figure",
         "weight": 0.9, "min_pages": 4, "height": 140, "charts": [{
             "type": "line", "subtitle": "% of available rooms",
             "x": ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
             "format": "{:.0f}", "zero": False,
             "series": [{"name": "This week", "values": [
                 71, 64, 69, 76, 88, 95, round(OCC * 100)]},
                        {"name": "Last year", "color": 4, "dash": True,
                         "values": [68, 60, 63, 70, 82, 91, 90]}]}]},
    ],
}
