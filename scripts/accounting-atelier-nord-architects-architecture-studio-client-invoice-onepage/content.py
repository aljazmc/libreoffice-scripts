"""Invoice 2027-041 of Atelier Nord: the business and everything the document
could say. The typesetting keeps what fits into one page, the most important
first."""

BUSINESS = {
    "name": "Atelier Nord",
    "author": "Atelier Nord Architects LLP",
}

FEE = 186_000.0          # agreed fixed fee, stages 0 – 7
STAGES = [("0 – 1 Strategic definition and brief", 0.05, 1.00),
          ("2 Concept design", 0.15, 1.00),
          ("3 Spatial coordination", 0.20, 1.00),
          ("4 Technical design", 0.25, 0.60),
          ("5 Manufacturing and construction", 0.25, 0.00),
          ("6 – 7 Handover and in use", 0.10, 0.00)]
PREVIOUSLY = 186_000 * (0.05 + 0.15 + 0.20 + 0.25 * 0.30)
EXPENSES = [("Printing, stage 4 drawings", 214.60),
            ("Site visits, 6 × 84 miles at £0.45", 226.80),
            ("Planning condition fees", 116.00)]
VAT = 0.20


def gbp(value):
    return f"£{value:,.2f}"


EARNED = sum(FEE * w * done for _, w, done in STAGES)
THIS_FEE = round(EARNED - PREVIOUSLY, 2)
EXP = round(sum(a for _, a in EXPENSES), 2)
NET = round(THIS_FEE + EXP, 2)
TAX = round(NET * VAT, 2)
TOTAL = round(NET + TAX, 2)

TIMESHEET = [("Ingrid Lund", "Partner", 14, 145), ("Oskar Berg",
                                                   "Associate", 46, 110),
             ("Mia Holm", "Architect", 88, 85),
             ("Leo Strand", "Part 2 assistant", 104, 60),
             ("Ana Sousa", "Technologist", 62, 75)]

DOCUMENT = {
    "title": "Invoice 2027-041",
    "eyebrow": "Atelier Nord Architects LLP",
    "subtitle": "Ashby Library extension · fees for RIBA stage 4, "
                "technical design, to 30 September 2027",
    "meta": [("Invoice", "2027-041"), ("Date", "1 Oct 2027"),
             ("Project", "AN-2318"), ("Due", "31 Oct 2027"),
             ("Amount due", gbp(TOTAL))],
    "sections": [
        {"kind": "table", "look": "plain", "header": False, "whole": True,
         "weight": 0.05, "columns": [("", 1), ("", 1)],
         "rows": [["**Atelier Nord Architects LLP**",
                   "**Ashby Town Council**"],
                  ["Studio 4, Rope Walk, Hull HU1 2PD",
                   "Property Services, Town Hall, Ashby AS1 1AA"],
                  ["VAT GB 287 6613 05", "For the attention of "
                                         "Mr Daniel Frost"],
                  ["accounts@ateliernord.example",
                   "Purchase order 4500118842"]]},
        {"heading": "Fees", "kind": "table", "whole": True, "weight": 0.1,
         "columns": [("Description", 3.4), ("Amount", 1, "end")],
         "rows": [["Stage 4 technical design, 60 % complete "
                   "(30 % previously invoiced)", gbp(THIS_FEE)]]
         + [[f"Expense: {n}", gbp(a)] for n, a in EXPENSES]
         + [{"cells": ["Net", gbp(NET)], "style": "subtotal"},
            {"cells": ["VAT at 20 %", gbp(TAX)], "style": "indent"},
            {"cells": ["Total due", gbp(TOTAL)], "style": "total"}]},
        {"kind": "callout", "weight": 0.15, "tone": "accent",
         "label": "Please pay",
         "text": f"{gbp(TOTAL)} by 31 October 2027 to Atelier Nord "
                 "Architects LLP, sort code 30-90-21, account 41820037, "
                 "quoting **2027-041**."},
        {"heading": "Fee account", "kind": "table", "whole": True,
         "weight": 0.2,
         "columns": [("RIBA stage", 3), ("Share", 0.7, "end"),
                     ("Fee", 1, "end"), ("Complete", 0.8, "end"),
                     ("Earned", 1, "end")],
         "rows": [[n, f"{w:.0%}", gbp(FEE * w), f"{d:.0%}",
                   gbp(FEE * w * d)] for n, w, d in STAGES]
         + [{"cells": ["Total fee", "100%", gbp(FEE), "",
                       gbp(EARNED)], "style": "subtotal"},
            {"cells": ["Invoiced previously", "", "", "",
                       f"({gbp(PREVIOUSLY)})"], "style": "indent"},
            {"cells": ["This invoice", "", "", "", gbp(THIS_FEE)],
             "style": "total"}]},
        {"heading": "Progress", "kind": "figure", "weight": 0.3,
         "min_pages": 2, "height": 130, "charts": [{"type": "progress",
          "format": "{:.0f} %", "items": [
              {"label": n,
               "value": d * 100, "status": "good" if d == 1 else
               "accent" if d else "grid"} for n, w, d in STAGES]}]},
        {"heading": "Timesheet appendix", "kind": "table", "whole": True,
         "weight": 0.5, "min_pages": 4,
         "columns": [("Name", 1.6), ("Role", 1.6), ("Hours", 0.8, "end"),
                     ("Rate", 0.8, "end"), ("Value", 1, "end")],
         "rows": [[n, r, str(h), f"£{rate}", gbp(h * rate)]
                  for n, r, h, rate in TIMESHEET]
         + [{"cells": ["Total", "", str(sum(t[2] for t in TIMESHEET)),
                       "", gbp(sum(t[2] * t[3] for t in TIMESHEET))],
             "style": "total"}]},
        {"kind": "text", "weight": 0.55, "step": 0.2, "min_pages": 4,
         "paragraphs": [
             "The fee is fixed; the timesheet is shown for "
             "transparency. Time spent on stage 4 so far is worth "
             f"{gbp(sum(t[2] * t[3] for t in TIMESHEET))} at our hourly "
             f"rates, against {gbp(THIS_FEE + 186_000 * 0.25 * 0.30)} "
             "of stage 4 fees earned."]},
        {"heading": "Hours by week", "kind": "figure", "weight": 0.6,
         "min_pages": 4, "height": 150, "charts": [{"type": "bars",
          "stacked": True, "subtitle": "September, stage 4",
          "categories": ["1 – 5 Sep", "8 – 12", "15 – 19", "22 – 26",
                         "29 – 30"],
          "series": [{"name": t[0], "values": [round(t[2] * f) for f in
                                               (0.22, 0.24, 0.22, 0.24,
                                                0.08)]}
                     for t in TIMESHEET]}]},
        {"heading": "Work done this month", "kind": "bullets",
         "weight": 0.7, "step": 0.1, "min_pages": 4, "items": [
             "Structural coordination of the cross-laminated timber "
             "frame with Halden Engineers; clash report closed.",
             "Façade details for the reading room glazing and the brick "
             "plinth; sample panel approved by the planners.",
             "Specification sections for joinery, finishes and "
             "accessible WCs.",
             "Two design team meetings and one client review.",
         ]},
        {"heading": "Terms", "kind": "tags", "weight": 0.8, "step": 0.1,
         "min_pages": 4, "items": [
             ("Appointment", "RIBA Professional Services Contract 2020, "
                             "dated 3 March 2026"),
             ("Payment", "within 30 days of the invoice date"),
             ("Late payment", "interest at 8 % above base rate"),
             ("Disputes", "notify within 14 days; undisputed amounts "
                          "remain payable"),
         ]},
        {"heading": "Invoices on this project", "kind": "table",
         "whole": True, "weight": 0.9, "min_pages": 4,
         "badges": {"Paid": "good", "Due": "warn"},
         "columns": [("Invoice", 1.1), ("Date", 1), ("For", 2.4),
                     ("Net", 1, "end"), ("", 0.8, "center")],
         "rows": [["2026-018", "1 Apr 2026", "Stages 0 – 1",
                   gbp(FEE * 0.05), "Paid"],
                  ["2026-047", "1 Jul 2026", "Stage 2, concept design",
                   gbp(FEE * 0.15), "Paid"],
                  ["2026-081", "1 Dec 2026", "Stage 3, spatial "
                   "coordination", gbp(FEE * 0.20), "Paid"],
                  ["2027-022", "1 Jun 2027", "Stage 4, 30 %",
                   gbp(FEE * 0.25 * 0.30), "Paid"],
                  ["2027-041", "1 Oct 2027", "Stage 4 to 60 %, expenses",
                   gbp(NET), "Due"]]},
        {"heading": "Fees still to come", "kind": "figure",
         "weight": 1.0, "min_pages": 4, "height": 150, "charts": [{
             "type": "bars", "title": "Forecast invoices", "subtitle":
             "£k, net", "format": "{:,.1f}",
             "categories": ["Dec 27", "Mar 28", "Jun 28", "Sep 28",
                            "Dec 28", "Jun 29"],
             "series": [{"name": "Fees", "values": [18.6, 11.6, 15.5,
                                                    15.5, 15.5, 18.6]}]}]},
        {"heading": "Programme", "kind": "figure", "weight": 1.1,
         "min_pages": 4, "height": 140, "charts": [{"type": "gantt",
          "columns": ["2026", "2027", "2028", "2029"],
          "groups": ["Design", "Construction", "Handover"],
          "today": 1.75, "today_label": "this invoice",
          "tasks": [{"label": "Stages 0 – 3", "start": 0.25, "end": 1.0,
                     "progress": 1},
                    {"label": "Stage 4 technical design", "start": 1.0,
                     "end": 2.0, "progress": 0.6},
                    {"label": "Tender", "start": 1.9, "end": 2.2,
                     "group": 1},
                    {"label": "Construction", "start": 2.2, "end": 3.3,
                     "group": 1},
                    {"label": "Handover and in use", "start": 3.3,
                     "end": 3.9, "group": 2}]}]},
        {"heading": "Project team", "kind": "tags", "weight": 1.2,
         "step": 0.1, "min_pages": 4, "items": [
             ("Partner in charge", "Ingrid Lund RIBA"),
             ("Project architect", "Mia Holm"),
             ("Structural engineer", "Halden Engineers"),
             ("Cost consultant", "Rowe Quantity Surveyors"),
             ("Client project manager", "Daniel Frost"),
         ]},
    ],
}
