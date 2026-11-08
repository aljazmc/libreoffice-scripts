"""Annual Operating Budget of Salt & Pine Hotel: the business and everything
the document could say. The typesetting keeps what fits into one page, the
most important first."""

BUSINESS = {
    "name": "Salt & Pine Hotel",
    "author": "Salt & Pine Hotel Ltd, general manager and finance",
}

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
          "Oct", "Nov", "Dec"]
DAYS = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
ROOMS = 42
OCCUPANCY = [0.52, 0.58, 0.66, 0.78, 0.86, 0.91, 0.95, 0.96, 0.88, 0.80,
             0.64, 0.70]
ADR = [205, 210, 225, 255, 285, 315, 335, 345, 300, 270, 225, 260]
ROOM_REV = [round(ROOMS * d * o * a / 1000, 1)
            for d, o, a in zip(DAYS, OCCUPANCY, ADR)]
FB_REV = [round(r * f, 1) for r, f in zip(ROOM_REV, [0.62, 0.6, 0.58,
                                                     0.57, 0.56, 0.56,
                                                     0.56, 0.56, 0.57,
                                                     0.58, 0.62, 0.78])]
SPA_REV = [round(r * 0.15, 1) for r in ROOM_REV]
REVENUE = [round(a + b + c, 1) for a, b, c in zip(ROOM_REV, FB_REV,
                                                  SPA_REV)]
PAYROLL = [round(95 + 0.2 * r, 1) for r in REVENUE]
OTHER_DEPT = [round(0.14 * r, 1) for r in REVENUE]
UNDIST = [round(60 + 0.05 * r, 1) for r in REVENUE]
FIXED = [70.0] * 12
EBITDA = [round(r - p - o - u - f, 1) for r, p, o, u, f in
          zip(REVENUE, PAYROLL, OTHER_DEPT, UNDIST, FIXED)]


def k(value):
    return f"({-value:,.0f})" if value < 0 else f"{value:,.0f}"


def row(label, values, style="indent", sign=1, **extra):
    return {"cells": [label] + [k(sign * v) for v in values]
            + [k(sign * sum(values))], "style": style, **extra}


COLUMNS = [("£k", 1.6)] + [(m, 0.55, "end") for m in MONTHS] + [
    ("Year", 0.7, "end")]
TOTAL = sum(REVENUE)
NIGHTS = sum(ROOMS * d * o for d, o in zip(DAYS, OCCUPANCY))
YEAR_OCC = sum(o * d for o, d in zip(OCCUPANCY, DAYS)) / 366
YEAR_ADR = (sum(a * o * d for a, o, d in zip(ADR, OCCUPANCY, DAYS))
            / sum(o * d for o, d in zip(OCCUPANCY, DAYS)))

DOCUMENT = {
    "title": "Annual Operating Budget 2028",
    "subtitle": "Month by month, with the drivers behind it · for the "
                "board meeting of 25 November 2027 · £ thousands",
    "meta": [("Revenue", f"£{TOTAL / 1000:.2f}m"),
             ("EBITDA", f"£{sum(EBITDA) / 1000:.2f}m"),
             ("Margin", f"{sum(EBITDA) / TOTAL:.1%}"),
             ("Occupancy", f"{YEAR_OCC:.0%}"),
             ("Average rate", f"£{YEAR_ADR:.0f}")],
    "sections": [
        {"heading": "Budget", "kind": "table", "whole": True,
         "weight": 0.1, "columns": COLUMNS,
         "rows": [row("Rooms", ROOM_REV, min_pages=2),
                  row("Food and beverage", FB_REV, min_pages=2),
                  row("Spa", SPA_REV, min_pages=2),
                  row("Revenue", REVENUE, "subtotal"),
                  row("Payroll", PAYROLL, sign=-1),
                  row("Other departmental costs", OTHER_DEPT, sign=-1),
                  row("Undistributed costs", UNDIST, sign=-1),
                  row("Rent, insurance, fees", FIXED, sign=-1),
                  row("EBITDA", EBITDA, "total")]},
        {"heading": "The shape of the year", "kind": "figure",
         "weight": 0.2, "height": {1: 150, 2: 170, 4: 180},
         "widths": [3, 2], "charts": [
             {"type": "bars", "stacked": True, "values": False,
              "subtitle": "revenue by department, £k",
              "format": "{:,.0f}", "categories": MONTHS,
              "series": [{"name": "Rooms", "values": ROOM_REV},
                         {"name": "Food and beverage", "color": 1,
                          "values": FB_REV},
                         {"name": "Spa", "color": 2,
                          "values": SPA_REV}]},
             {"type": "line", "subtitle": "EBITDA, £k", "x": MONTHS,
              "format": "{:,.0f}", "zero": False, "target": 0,
              "target_label": "break-even",
              "series": [{"name": "EBITDA", "area": True,
                          "values": EBITDA}]},
         ]},
        {"heading": "Drivers", "kind": "table", "whole": True,
         "weight": 0.3, "min_pages": 2, "columns": COLUMNS[:-1] + [
             ("Year", 0.7, "end")],
         "rows": [{"cells": ["Occupancy"] + [f"{o:.0%}" for o in
                                             OCCUPANCY]
                   + [f"{YEAR_OCC:.0%}"],
                   "style": "indent"},
                  {"cells": ["Average rate £"] + [str(a) for a in ADR]
                   + [""], "style": "indent"},
                  {"cells": ["Room nights"] + [
                      f"{round(ROOMS * d * o):,}"
                      for d, o in zip(DAYS, OCCUPANCY)]
                   + [f"{round(NIGHTS):,}"],
                   "style": "indent"}]},
        {"heading": "Assumptions", "kind": "bullets", "weight": 0.4,
         "step": 0.1, "min_pages": 2, "items": [
             "Rates rise by 4 % on 2027; occupancy stays at 2027 levels "
             "except January to March, where the new winter breaks add "
             "four points.",
             "Payroll includes the 6.7 % rise in the national living "
             "wage from April and two new chefs.",
             "Energy is fixed for the year at 18p per kWh under the new "
             "contract.",
         ]},
        {"heading": "Capital plan", "kind": "table", "whole": True,
         "weight": 0.5, "min_pages": 4,
         "columns": [("Project", 2.6), ("Month", 0.8),
                     ("Cost £k", 0.8, "end"), ("Why", 3)],
         "rows": [["Refurbish rooms 1 – 8", "Jan – Feb", "184",
                   "Last done in 2017; rates there lag by £30"],
                  ["Terrace canopy", "Mar", "62",
                   "Keeps the terrace open in the rain"],
                  ["Kitchen extraction", "Nov", "48",
                   "Required by the insurer"],
                  ["Electric vehicle chargers × 6", "Apr", "21",
                   "Guests ask for them"],
                  {"cells": ["Total", "", "315", ""],
                   "style": "total"}]},
        {"heading": "Risks", "kind": "table", "whole": True,
         "weight": 0.6, "min_pages": 4,
         "badges": {"High": "bad", "Medium": "warn", "Low": "good"},
         "columns": [("Risk", 3), ("Level", 0.8, "center"),
                     ("Effect on EBITDA", 1.2, "end"), ("Response", 3)],
         "rows": [["Wet summer", "Medium", "−£60k",
                   "Indoor packages, spa offers"],
                  ["Chef shortage", "High", "−£40k",
                   "Retention bonus, apprentices"],
                  ["Rate resistance above £340", "Medium", "−£35k",
                   "Value-add packages instead of discounts"],
                  ["Refurbishment overruns", "Low", "−£20k",
                   "Fixed-price contract"]]},
        {"heading": "Against 2027", "kind": "figure", "weight": 0.7,
         "min_pages": 4, "height": 150, "charts": [{"type": "waterfall",
          "format": "£{:,.0f}k", "axis_format": "{:,.0f}",
          "total_color": 0,
          "steps": [("2027 forecast", round(sum(EBITDA)) - 148),
                    ("Room rates +4 %", 152), ("Winter breaks", 61),
                    ("Food and beverage", 38), ("Wage rise", -84),
                    ("Energy", 22), ("New chefs", -41),
                    ("2028 budget", None)]}]},
        {"heading": "Approval", "kind": "text", "weight": 0.8,
         "step": 0.3, "min_pages": 4, "paragraphs": [
             "The board is asked to approve the operating budget and the "
             "capital plan of £315k, funded from cash. Results are "
             "reported against this budget every month, and the "
             "forecast is reviewed each quarter.",
         ]},
    ],
}
