"""Payslip of Bright Smile Dental: the business and everything the document
could say. The typesetting keeps what fits into two pages, the most
important first."""

BUSINESS = {
    "name": "Bright Smile Dental",
    "author": "Bright Smile Dental Ltd, payroll",
}

HOURS, RATE = 151.67, 14.20          # contracted monthly hours
OVERTIME_HOURS, OVERTIME_RATE = 6.0, 21.30
CPD_ALLOWANCE = 40.00
BASIC = round(HOURS * RATE, 2)
OVERTIME = round(OVERTIME_HOURS * OVERTIME_RATE, 2)
GROSS = round(BASIC + OVERTIME + CPD_ALLOWANCE, 2)
PENSION = round(GROSS * 0.05, 2)                 # salary sacrifice off
TAXABLE = round(GROSS - PENSION, 2)
ALLOWANCE = round(12570 / 12, 2)                 # 1257L monthly
TAX = round(max(TAXABLE - ALLOWANCE, 0) * 0.20, 2)
NI = round(max(GROSS - 1048, 0) * 0.08, 2)
STUDENT = round(max(GROSS - 2274, 0) * 0.09, 2)  # plan 2
DEDUCTIONS = round(PENSION + TAX + NI + STUDENT, 2)
NET = round(GROSS - DEDUCTIONS, 2)
EMPLOYER_NI = round(max(GROSS - 758, 0) * 0.15, 2)
EMPLOYER_PENSION = round(GROSS * 0.03, 2)
MONTH = 6


def gbp(value):
    return f"£{value:,.2f}"


DOCUMENT = {
    "title": "Payslip",
    "eyebrow": "Bright Smile Dental Ltd · PAYE ref. 123/BS45678",
    "subtitle": "September 2027 · paid 30 September 2027 · tax month 6",
    "meta": [("Employee", "Chloe Bennett"), ("Role", "Dental nurse"),
             ("Employee no.", "0047"), ("Tax code", "1257L"),
             ("NI number", "QQ 12 34 56 C")],
    "sections": [
        {"heading": "Payments", "kind": "table", "whole": True,
         "weight": 0.1,
         "columns": [("Description", 2.6), ("Units", 0.8, "end"),
                     ("Rate", 0.8, "end"), ("Amount", 1, "end")],
         "rows": [["Basic pay", f"{HOURS:.2f} h", gbp(RATE), gbp(BASIC)],
                  ["Overtime, Saturday clinic", f"{OVERTIME_HOURS:.2f} h",
                   gbp(OVERTIME_RATE), gbp(OVERTIME)],
                  ["CPD allowance", "", "", gbp(CPD_ALLOWANCE)],
                  {"cells": ["Gross pay", "", "", gbp(GROSS)],
                   "style": "subtotal"}]},
        {"heading": "Deductions", "kind": "table", "whole": True,
         "weight": 0.15,
         "columns": [("Description", 3.4), ("Amount", 1, "end")],
         "rows": [["Pension, 5 % (net pay arrangement)", gbp(PENSION)],
                  ["Income tax", gbp(TAX)],
                  ["National Insurance, category A", gbp(NI)],
                  ["Student loan, plan 2", gbp(STUDENT)],
                  {"cells": ["Total deductions", gbp(DEDUCTIONS)],
                   "style": "subtotal"},
                  {"cells": ["Net pay", gbp(NET)], "style": "total"}]},
        {"kind": "callout", "weight": 0.2, "tone": "good",
         "label": f"Net pay {gbp(NET)}",
         "text": "paid by bank transfer to account ending 4471, sort code "
                 "20-00-00, on 30 September 2027."},
        {"heading": "Where the gross pay goes", "kind": "figure",
         "weight": 0.3, "height": {1: 120, 2: 130, 4: 140}, "charts": [{
             "type": "bars", "horizontal": True, "stacked": True,
             "inside": True, "format": "£{:,.0f}", "values": False,
             "categories": ["September"],
             "series": [{"name": "Net pay", "color": 0, "values": [NET]},
                        {"name": "Tax", "color": 2, "values": [TAX]},
                        {"name": "NI", "color": 1, "values": [NI]},
                        {"name": "Pension", "color": 3,
                         "values": [PENSION]},
                        {"name": "Student loan", "color": 4,
                         "values": [STUDENT]}], "row": 40}]},
        {"heading": "Year to date", "kind": "table", "whole": True,
         "weight": 0.4, "min_pages": 2,
         "columns": [("", 2.6), ("This month", 1, "end"),
                     ("Year to date", 1, "end")],
         "rows": [["Gross pay", gbp(GROSS), gbp(GROSS * MONTH - 212.40)],
                  ["Taxable pay", gbp(TAXABLE),
                   gbp(TAXABLE * MONTH - 201.78)],
                  ["Income tax", gbp(TAX), gbp(TAX * MONTH - 40.36)],
                  ["National Insurance", gbp(NI), gbp(NI * MONTH - 16.99)],
                  ["Pension, employee", gbp(PENSION),
                   gbp(PENSION * MONTH - 10.62)],
                  ["Student loan", gbp(STUDENT),
                   gbp(STUDENT * MONTH - 19.12)],
                  {"cells": ["Net pay", gbp(NET),
                             gbp(NET * MONTH - 125.31)],
                   "style": "total"}]},
        {"heading": "Paid by the practice on top", "kind": "table",
         "whole": True, "weight": 0.5, "min_pages": 2,
         "columns": [("Employer cost", 3.4), ("Amount", 1, "end")],
         "rows": [["Employer's National Insurance", gbp(EMPLOYER_NI)],
                  ["Employer's pension, 3 %", gbp(EMPLOYER_PENSION)],
                  {"cells": ["Total cost of employment",
                             gbp(GROSS + EMPLOYER_NI + EMPLOYER_PENSION)],
                   "style": "total"}]},
        {"heading": "Leave", "kind": "figure", "weight": 0.6,
         "min_pages": 2, "height": 110, "charts": [{"type": "progress",
          "format": "{:.0f} days", "max": 28, "items": [
              {"label": "Annual leave entitlement", "value": 28,
               "status": 4, "note": "including bank holidays"},
              {"label": "Taken", "value": 13, "status": 0},
              {"label": "Booked", "value": 5, "status": 1},
              {"label": "Remaining", "value": 10, "status": "good"}]}]},
        {"heading": "Monthly pay this year", "kind": "figure",
         "weight": 0.7, "min_pages": 4, "height": 150, "charts": [{
             "type": "bars", "stacked": True, "format": "£{:,.0f}",
             "values": False, "subtitle": "£",
             "categories": ["Apr", "May", "Jun", "Jul", "Aug", "Sep"],
             "series": [{"name": "Net pay", "values": [
                 NET - 21, NET - 30, NET - 14, NET - 40, NET - 20, NET]},
                        {"name": "Deductions", "color": 1, "values": [
                            DEDUCTIONS - 5, DEDUCTIONS - 8,
                            DEDUCTIONS - 3, DEDUCTIONS - 10,
                            DEDUCTIONS - 5, DEDUCTIONS]}]}]},
        {"heading": "Pension", "kind": "table", "whole": True,
         "weight": 0.8, "min_pages": 4,
         "columns": [("Bright Smile workplace pension", 3.2),
                     ("This month", 1, "end"),
                     ("Since joining", 1, "end")],
         "rows": [["Your contribution, 5 %", gbp(PENSION), "£2,431.80"],
                  ["Practice contribution, 3 %", gbp(EMPLOYER_PENSION),
                   "£1,459.08"],
                  ["Tax relief included", gbp(PENSION * 0.2), "£486.36"],
                  {"cells": ["Total paid in", gbp(PENSION
                                                  + EMPLOYER_PENSION),
                             "£3,890.88"], "style": "total"}]},
        {"heading": "Your tax code", "kind": "text", "weight": 0.9,
         "step": 0.3, "min_pages": 4, "paragraphs": [
             "1257L is the standard code: you can earn £12,570 in the tax "
             "year before paying income tax, which is £1,047.50 a month. "
             "Income tax is 20 % of what you earn above that, after your "
             "pension.",
             "If you have a second job or taxable benefits, your code may "
             "change; HMRC will tell us and you.",
         ]},
        {"heading": "Pay calendar", "kind": "figure", "weight": 1.0,
         "min_pages": 4, "height": 115, "charts": [{"type": "timeline",
          "start": 0, "end": 12, "label_width": 80,
          "ticks": [(i, m) for i, m in enumerate(
              ["Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov",
               "Dec", "Jan", "Feb", "Mar", "Apr"])],
          "events": [{"at": 5.9, "label": "This payslip", "sub": "30 Sep",
                      "status": "now"},
                     {"at": 6.9, "label": "Pay rise 3 %", "sub": "Oct"},
                     {"at": 8.6, "label": "Christmas pay date",
                      "sub": "19 Dec"},
                     {"at": 11.2, "label": "P60", "sub": "by 31 May"}]}]},
        {"heading": "Questions", "kind": "tags", "weight": 1.1,
         "step": 0.1, "min_pages": 4, "items": [
             ("Payroll", "Hannah Price, practice manager"),
             ("Pension provider", "NEST, member 0047-BSD"),
             ("Keep this payslip", "for at least a year; you may need it "
                                   "for a loan or a mortgage"),
         ]},
        {"heading": "Hours this month", "kind": "figure", "weight": 1.2,
         "min_pages": 4, "height": 140, "charts": [{"type": "bars",
          "title": "Hours worked by week", "stacked": True,
          "categories": ["1 – 7 Sep", "8 – 14", "15 – 21", "22 – 28",
                         "29 – 30"],
          "series": [{"name": "Contracted", "values": [35, 35, 35, 35,
                                                       11.67]},
                     {"name": "Overtime", "color": 1,
                      "values": [0, 3, 0, 3, 0]}]}]},
        {"heading": "Your benefits", "kind": "bullets", "weight": 1.3,
         "step": 0.1, "min_pages": 4, "items": [
             "Free dental treatment at the practice, lab fees only.",
             "£250 a year for CPD courses, paid monthly with your pay.",
             "Uniform provided and laundered.",
             "Birthday off, on full pay.",
         ]},
    ],
}
