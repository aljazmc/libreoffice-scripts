"""Revenue by Treatment of Bright Smile Dental: the business and everything the
document could say. The typesetting keeps what fits into one page, the most
important first."""

BUSINESS = {
    "name": "Bright Smile Dental",
    "author": "Dr Amina Yusuf, principal dentist",
}

# treatment, count in the half year, average fee £, chair minutes,
# direct cost per treatment £ (lab and materials)
TREATMENTS = [("Check-up and scale", 2_840, 62, 30, 4),
              ("Hygienist visit", 1_310, 75, 40, 5),
              ("White filling", 920, 145, 45, 14),
              ("Root canal", 140, 520, 90, 38),
              ("Crown", 210, 690, 75, 210),
              ("Implant (both stages)", 38, 2_650, 180, 820),
              ("Clear aligners", 46, 3_100, 150, 1_150),
              ("Whitening", 120, 320, 45, 70),
              ("Emergency appointment", 430, 85, 25, 6)]
CHAIR_RATE = 160  # £ per chair hour: dentist time and overheads

TREATMENTS = [(name, round(n * 0.55), fee, minutes, cost)
              for name, n, fee, minutes, cost in TREATMENTS]

ROWS = []
for name, n, fee, minutes, cost in TREATMENTS:
    revenue = n * fee
    margin = revenue - n * cost - n * minutes / 60 * CHAIR_RATE
    per_hour = (fee - cost) / (minutes / 60)
    ROWS.append((name, n, fee, revenue, margin, per_hour, minutes))
TOTAL = sum(r[3] for r in ROWS)
MARGIN = sum(r[4] for r in ROWS)


def gbp(value):
    sign = "−" if value < 0 else ""
    return f"{sign}£{abs(value):,.0f}"


DOCUMENT = {
    "title": "Revenue by Treatment",
    "subtitle": "Which treatments earn the practice its money · April to "
                "September 2027, private and plan patients",
    "meta": [("Period", "Apr – Sep 2027"),
             ("Treatments", f"{sum(r[1] for r in ROWS):,}"),
             ("Revenue", gbp(TOTAL)), ("Margin after chair time",
                                       gbp(MARGIN)),
             ("Chair cost", f"£{CHAIR_RATE} an hour")],
    "sections": [
        {"heading": "Revenue and margin", "kind": "table", "whole": True,
         "weight": 0.1,
         "columns": [("Treatment", 2.4), ("Count", 0.8, "end"),
                     ("Average fee", 0.9, "end"), ("Revenue", 1, "end"),
                     ("Share", 0.7, "end"), ("Margin", 1, "end"),
                     ("£ per chair hour", 1, "end")],
         "rows": [[n, f"{c:,}", gbp(f), gbp(r), f"{r / TOTAL:.0%}",
                   gbp(m), gbp(h)] for n, c, f, r, m, h, _ in ROWS]
         + [{"cells": ["Total", f"{sum(r[1] for r in ROWS):,}", "",
                       gbp(TOTAL), "100%", gbp(MARGIN), ""],
             "style": "total"}]},
        {"heading": "Where the money comes from", "kind": "figure",
         "weight": 0.2, "height": {1: 165, 2: 175, 4: 185},
         "widths": [2, 3], "charts": [
             {"type": "donut", "title": "Revenue",
              "segments": [(r[0], r[3]) for r in sorted(
                  ROWS, key=lambda r: -r[3])[:6]]
              + [("Other", TOTAL - sum(r[3] for r in sorted(
                  ROWS, key=lambda r: -r[3])[:6]), 4)],
              "format": "£{:,.0f}", "center": (f"£{TOTAL / 1000:.0f}k",
                                               "six months")},
             {"type": "bars", "horizontal": True, "title": "Earnings per "
              "chair hour", "subtitle": "fee less lab and materials",
              "format": "£{:,.0f}", "target": CHAIR_RATE,
              "target_label": "chair cost",
              "categories": [r[0] for r in sorted(ROWS,
                                                  key=lambda r: -r[5])],
              "series": [{"name": "£ per hour", "values": [
                  round(r[5]) for r in sorted(ROWS, key=lambda r: -r[5])],
                  "colors": ["good" if r[5] > CHAIR_RATE * 1.5 else 0
                             if r[5] > CHAIR_RATE else "bad"
                             for r in sorted(ROWS,
                                             key=lambda r: -r[5])]}]},
         ]},
        {"heading": "What it tells us", "kind": "bullets", "weight": 0.3,
         "step": 0.1, "items": [
             "**Aligners and implants are a quarter of the revenue** from "
             "2 % of the appointments, and earn the most per chair hour.",
             "**Check-ups lose money on their own** at £62, but bring "
             "in nearly every patient who later needs treatment.",
             "**Emergency slots barely cover the chair**; they are kept "
             "for patients' sake and to fill gaps.",
         ]},
        {"heading": "By dentist", "kind": "figure", "weight": 0.4,
         "min_pages": 2, "height": 170, "charts": [{"type": "heatmap",
          "title": "Revenue by dentist and treatment", "subtitle": "£k",
          "rows": ["Dr Yusuf", "Dr Hale", "Dr Nair", "Dr Novak",
                   "Dr Fischer", "Hygienists"],
          "cols": ["Check-up", "Filling", "Root canal", "Crown",
                   "Implant", "Aligners", "Whitening"],
          "values": [[21, 23, 12, 28, 0, 47, 7],
                     [23, 20, 10, 21, 0, 15, 5],
                     [21, 15, 12, 17, 0, 16, 5],
                     [20, 15, 6, 14, 0, 0, 4],
                     [0, 0, 0, 0, 55, 0, 0],
                     [12, 0, 0, 0, 0, 0, 0]],
          "format": "{:.0f}", "labels": 0.16}]},
        {"heading": "Months", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": 150, "charts": [{"type": "bars",
          "stacked": True, "subtitle": "£k per month", "format":
          "{:.0f}", "values": False,
          "categories": ["Apr", "May", "Jun", "Jul", "Aug", "Sep"],
          "series": [{"name": "Routine", "values": [32, 33, 34, 32, 29,
                                                    34]},
                     {"name": "Restorative", "values": [23, 24, 25, 22,
                                                        20, 26]},
                     {"name": "Implants and aligners", "color": 2,
                      "values": [21, 22, 24, 18, 16, 33]},
                     {"name": "Cosmetic", "color": 4,
                      "values": [3, 4, 4, 3, 3, 4]}]}]},
        {"heading": "Opportunities", "kind": "entries", "weight": 0.6,
         "step": 0.2, "inner": 0.1, "min_pages": 4, "entries": [
             {"title": "A second implant day", "text": [
                 "Dr Fischer's list is booked eleven weeks ahead. One "
                 "more day a month adds about £16k of revenue in six "
                 "months."]},
             {"title": "Hygienist-led check-ups", "text": [
                 "Routine checks for low-risk patients by the hygienist "
                 "free up 140 dentist hours in six months."]},
             {"title": "Price of emergency slots", "text": [
                 "Raise from £85 to £95 for non-plan patients: still "
                 "below the local average of £104."]},
         ]},
        {"heading": "Payer mix", "kind": "figure", "weight": 0.7,
         "min_pages": 4, "height": 150, "charts": [{"type": "bars",
          "horizontal": True, "stacked": True, "inside": True,
          "format": "{:.0f}%", "values": False,
          "categories": ["Check-up", "Filling", "Crown", "Implant",
                         "Aligners"],
          "series": [{"name": "Plan", "values": [58, 34, 22, 0, 0]},
                     {"name": "Private", "values": [32, 52, 66, 84, 96]},
                     {"name": "Insurance", "color": 2,
                      "values": [10, 14, 12, 16, 4]}]}]},
        {"heading": "Method", "kind": "text", "weight": 0.8, "step": 0.3,
         "min_pages": 4, "paragraphs": [
             "Treatments are taken from the practice software's fee "
             "report; lab and material costs from the lab invoices and "
             "the stock system. The chair hour of £160 is the cost of a "
             "surgery for an hour: the dentist's share of fees, the "
             "nurse, the premises and the equipment, divided by the "
             "booked hours.",
             "NHS treatment is paid by contract, not by treatment, and is "
             "left out.",
         ]},
        {"heading": "Chair time", "kind": "figure", "weight": 0.9,
         "min_pages": 4, "height": 160, "widths": [1, 1], "charts": [
             {"type": "donut", "title": "Share of chair hours",
              "segments": [(r[0], round(r[1] * r[6] / 60))
                           for r in ROWS[:6]]
              + [("Other", round(sum(r[1] * r[6] / 60
                                     for r in ROWS[6:])), 4)],
              "format": "{:,.0f} h", "center": (
                  f"{sum(r[1] * r[6] for r in ROWS) / 60:,.0f} h",
                  "booked")},
             {"type": "quadrant", "title": "Volume and value",
              "x": "how often", "y": "earnings per hour",
              "quadrants": ["Grow", "Protect", "Review", "Keep simple"],
              "points": [("Check-up", 9.5, 1.5, 0),
                         ("Hygienist", 7.5, 1.2, 0),
                         ("Filling", 6.5, 2.4, 0),
                         ("Root canal", 2.5, 4.5, 1),
                         ("Crown", 3, 5.2, 1), ("Implant", 1, 8.5, 2),
                         ("Aligners", 1.2, 9.6, 2),
                         ("Whitening", 2, 4.6, 3),
                         ("Emergency", 4.5, 2.6, "bad")]},
         ]},
        {"heading": "Fee list", "kind": "table", "whole": True,
         "weight": 1.0, "min_pages": 4,
         "columns": [("Treatment", 2.6), ("Fee today", 1, "end"),
                     ("Local average", 1, "end"),
                     ("Proposed 2028", 1, "end")],
         "rows": [["Check-up and scale", "£62", "£68", "£65"],
                  ["White filling", "£145", "£155", "£150"],
                  ["Crown", "£690", "£720", "£710"],
                  ["Implant, both stages", "£2,650", "£2,900", "£2,750"],
                  ["Clear aligners", "£3,100", "£3,300", "£3,200"],
                  ["Emergency appointment", "£85", "£104", "£95"]]},
        {"heading": "New patients and what they need", "kind": "figure",
         "weight": 1.1, "min_pages": 4, "height": 140, "charts": [{
             "type": "funnel", "format": "{:,.0f}",
             "stages": [("New patients", 312),
                        ("Treatment plan offered", 204),
                        ("Plan accepted", 145),
                        ("Treatment completed", 131),
                        ("Joined a membership plan", 88)]}]},
    ],
}
