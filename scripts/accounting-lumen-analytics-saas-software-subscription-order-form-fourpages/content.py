"""Enterprise Order Form of Lumen Analytics: the business and everything the
document could say. The typesetting keeps what fits into four pages, the
most important first."""

BUSINESS = {
    "name": "Lumen Analytics",
    "author": "Lumen Analytics Inc., sales operations",
}

# seats, list price per seat per year, discount by contract year
YEARS = [("Year 1 · 2027", 180, 0.20), ("Year 2 · 2028", 240, 0.15),
         ("Year 3 · 2029", 300, 0.10)]
LIST = 960
PLATFORM = 24000


def usd(value):
    return f"${value:,.0f}"


LINES = []
for label, seats, discount in YEARS:
    seats_fee = seats * LIST * (1 - discount)
    LINES.append((label, seats, discount, seats_fee, PLATFORM,
                  seats_fee + PLATFORM))
TOTAL = sum(line[5] for line in LINES)

DOCUMENT = {
    "title": "Enterprise Order Form",
    "eyebrow": "Lumen Analytics · order LUM-Q-2026-0388",
    "subtitle": "Lumen Forecast Enterprise for Kestrel Retail Group · "
                "three-year subscription starting 1 January 2027",
    "meta": [("Order", "LUM-Q-2026-0388"), ("Customer", "Kestrel Retail "
                                                        "Group plc"),
             ("Term", "36 months"), ("Total contract value", usd(TOTAL)),
             ("Valid until", "20 Dec 2026")],
    "sections": [
        {"kind": "table", "look": "plain", "header": False, "whole": True,
         "weight": 0.05, "columns": [("", 1), ("", 1)],
         "rows": [["**Provider** Lumen Analytics Inc.",
                   "**Customer** Kestrel Retail Group plc"],
                  ["400 Brannan Street, San Francisco CA 94107",
                   "1 Kestrel Way, Leeds LS1 4AP, UK"],
                  ["Account executive: Dana Whitfield",
                   "Buyer: Priya Shah, Head of Planning"],
                  ["dana.whitfield@lumen.example",
                   "Billing: ap@kestrel.example"]]},
        {"heading": "Subscription", "kind": "table", "whole": True,
         "weight": 0.1,
         "columns": [("Period", 1.6), ("Seats", 0.7, "end"),
                     ("List per seat", 1, "end"),
                     ("Discount", 0.8, "end"), ("Seats fee", 1.1, "end"),
                     ("Platform", 1, "end"), ("Annual fee", 1.1, "end")],
         "rows": [[label, str(seats), usd(LIST), f"{discount:.0%}",
                   usd(fee), usd(platform), usd(annual)]
                  for label, seats, discount, fee, platform, annual
                  in LINES]
         + [{"cells": ["Total contract value", "", "", "", "", "",
                       usd(TOTAL)], "style": "total"}]},
        {"heading": "Billing schedule", "kind": "figure", "weight": 0.2,
         "height": {1: 120, 2: 140, 4: 150}, "widths": [3, 2],
         "charts": [
             {"type": "bars", "title": "Invoiced each January",
              "subtitle": "$k, annual in advance", "format": "{:,.0f}",
              "stacked": True,
              "categories": ["Jan 2027", "Jan 2028", "Jan 2029"],
              "series": [{"name": "Seats",
                          "values": [l[3] / 1000 for l in LINES]},
                         {"name": "Platform", "color": 1,
                          "values": [l[4] / 1000 for l in LINES]}]},
             {"type": "donut", "title": "Contract value",
              "segments": [(l[0][:6], l[5] / 1000) for l in LINES],
              "format": "${:,.0f}k",
              "center": (f"${TOTAL / 1000:,.0f}k", "36 months")},
         ]},
        {"heading": "Signatures", "kind": "table", "look": "plain",
         "header": False, "whole": True, "weight": 0.3,
         "columns": [("", 1), ("", 1)],
         "rows": [["**For Lumen Analytics Inc.**",
                   "**For Kestrel Retail Group plc**"],
                  ["Name: Maya Okafor, Chief Revenue Officer",
                   "Name: ______________________________"],
                  ["Signature: ___________________________",
                   "Signature: ___________________________"],
                  ["Date: ________________", "Date: ________________"]]},
        {"heading": "What is included", "kind": "bullets", "weight": 0.4,
         "step": 0.1, "min_pages": 2, "items": [
             "Lumen Forecast Enterprise: demand forecasting, scenario "
             "planning and the store-level replenishment module.",
             "Unlimited read-only viewers; seats are for users who edit "
             "plans.",
             "Single sign-on, audit log, and data residency in the EU "
             "(Frankfurt).",
             "Onboarding: 12 weeks with a named solutions engineer, and "
             "four training days on site in Leeds.",
             "Premium support: 24/7, response within 1 hour for "
             "severity 1.",
         ]},
        {"heading": "Payment terms", "kind": "tags", "weight": 0.5,
         "step": 0.1, "min_pages": 2, "items": [
             ("Invoicing", "annually in advance, each 1 January"),
             ("Payment", "net 45 days, by bank transfer in US dollars"),
             ("Extra seats", "pro-rated at the discounted price of the "
                             "current year"),
             ("Price protection", "the seat price may not rise by more "
                                  "than 5 % at renewal"),
             ("Taxes", "prices exclude VAT; the customer self-accounts "
                       "for UK VAT under the reverse charge"),
         ]},
        {"heading": "Seat ramp", "kind": "figure", "weight": 0.6,
         "min_pages": 2, "height": 130, "charts": [{"type": "line",
          "title": "Planned users", "x": ["Jan 27", "Jul 27", "Jan 28",
                                          "Jul 28", "Jan 29", "Jul 29"],
          "format": "{:.0f}", "series": [
              {"name": "Seats contracted", "values": [180, 180, 240, 240,
                                                      300, 300]},
              {"name": "Expected active users", "color": 1, "dash": True,
               "values": [60, 150, 210, 235, 280, 300]}]}]},
        {"heading": "Service levels", "kind": "table", "weight": 0.7,
         "whole": True, "min_pages": 4,
         "columns": [("Measure", 2.4), ("Commitment", 1.4),
                     ("Service credit", 2)],
         "rows": [
             ["Monthly availability", "99.9 %", "5 % of the monthly fee "
              "for each 0.1 % below"],
             ["Severity 1 response", "1 hour, 24/7", "2 % per breach"],
             ["Severity 2 response", "4 business hours", "—"],
             ["Forecast run completed", "by 06:00 local time",
              "1 % per late day"],
             ["Data export on request", "within 5 business days", "—"],
         ]},
        {"heading": "Data and security", "kind": "entries",
         "weight": 0.8, "step": 0.2, "inner": 0.1, "min_pages": 4,
         "entries": [
             {"title": "Data processing agreement", "text": [
                 "Lumen processes the customer's sales and stock data as "
                 "a processor under the attached DPA, with the EU "
                 "standard contractual clauses."]},
             {"title": "Certifications", "text": [
                 "SOC 2 Type II (report dated 30 September 2026) and ISO "
                 "27001; penetration test summary available on request."]},
             {"title": "End of contract", "text": [
                 "All customer data is returned in Parquet format and "
                 "deleted within 30 days, with a certificate of "
                 "deletion."]},
         ]},
        {"heading": "Terms", "kind": "text", "weight": 0.9, "step": 0.2,
         "min_pages": 4, "paragraphs": [
             "This order form is governed by the Lumen Master "
             "Subscription Agreement dated 4 November 2026 between the "
             "parties. If they conflict, this order form prevails for "
             "the matters it covers.",
             "The subscription renews for one year at the end of the "
             "term unless either party gives 90 days' written notice. "
             "Fees are non-cancellable and non-refundable except as "
             "stated in the agreement.",
         ]},
        {"heading": "Value to the customer", "kind": "figure",
         "weight": 1.0, "min_pages": 4, "height": 140, "charts": [{
             "type": "bars", "horizontal": True, "title": "Business case "
             "agreed with Kestrel", "subtitle": "$k a year from year 2",
             "format": "{:,.0f}",
             "categories": ["Less stock written off", "Fewer stock-outs",
                            "Planner hours saved", "Lumen fee"],
             "series": [{"name": "Value",
                         "values": [1450, 980, 310, -LINES[1][5] / 1000],
                         "colors": ["good", "good", "good", "bad"]}]}]},
        {"heading": "Onboarding plan", "kind": "figure", "weight": 1.1,
         "min_pages": 4, "height": 160, "charts": [{"type": "gantt",
          "columns": ["Jan", "Feb", "Mar", "Apr"],
          "groups": ["Lumen", "Kestrel", "Joint"],
          "tasks": [{"label": "Data connection and history load",
                     "start": 0, "end": 1.2},
                    {"label": "Store hierarchy and calendars", "start": 0.5,
                     "end": 1.5, "group": 1},
                    {"label": "Model training and back-test", "start": 1.2,
                     "end": 2.2},
                    {"label": "Planner training, Leeds", "start": 2,
                     "end": 2.6, "group": 2},
                    {"label": "Parallel run with the old tool",
                     "start": 2.2, "end": 3.0, "group": 2},
                    {"label": "Go-live", "start": 3.05, "milestone": True,
                     "text": "week 12"}]}]},
        {"heading": "Contacts", "kind": "tags", "weight": 1.2,
         "step": 0.1, "min_pages": 4, "items": [
             ("Account executive", "Dana Whitfield"),
             ("Solutions engineer", "Kofi Mensah"),
             ("Customer success", "Lena Brandt"),
             ("Billing", "billing@lumen.example"),
             ("Support", "support.lumen.example, 24/7"),
         ]},
        {"heading": "Price comparison", "kind": "figure", "weight": 1.3,
         "min_pages": 4, "height": 150, "charts": [{"type": "bars",
          "title": "Price per seat per year", "subtitle": "$ after "
          "discount", "format": "${:,.0f}",
          "categories": ["List", "Year 1", "Year 2", "Year 3",
                         "Typical enterprise"],
          "series": [{"name": "Per seat",
                      "values": [LIST, LIST * 0.8, LIST * 0.85,
                                 LIST * 0.9, LIST * 0.82],
                      "colors": [4, 0, 0, 0, 3]}]}]},
        {"heading": "Order checklist", "kind": "table", "whole": True,
         "weight": 1.4, "min_pages": 4,
         "badges": {"Done": "good", "Open": "warn"},
         "columns": [("Step", 4), ("Status", 0.9, "center")],
         "rows": [["Discount approved by the CRO (over 15 %)", "Done"],
                  ["Security questionnaire returned", "Done"],
                  ["DPA signed by both parties", "Open"],
                  ["Purchase order number received", "Open"],
                  ["Customer added to the billing system", "Open"]]},
    ],
}
