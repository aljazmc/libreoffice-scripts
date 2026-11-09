"""Invoice of Rye & Crumb Bakery: the business and everything the document
could say. The typesetting keeps what fits into four pages, the most
important first."""

BUSINESS = {
    "name": "Rye & Crumb Bakery",
    "author": "Rye & Crumb Ltd",
}

ITEMS = [("Item", 3), ("Qty", 0.7, "end"), ("Unit", 0.9, "end"),
         ("VAT", 0.6, "center"), ("Amount", 1, "end")]

DOCUMENT = {
    "title": "Invoice RC-2027-1186",
    "eyebrow": "Rye & Crumb Bakery · wholesale",
    "subtitle": "Bread and pastries delivered to Harbour Café in "
                "October 2027",
    "meta": [("Invoice date", "1 Nov 2027"), ("Due", "15 Nov 2027"),
             ("Account", "HC-014"), ("Amount due", "€3,912.47")],
    "sections": [
        {"kind": "table", "look": "plain", "header": False, "whole": True,
         "weight": 0.05, "columns": [("", 1), ("", 1)],
         "rows": [["**From** Rye & Crumb Ltd", "**To** Harbour Café"],
                  ["12 Mill Lane, Ashby AS1 4RT", "Attn. Sophie Laurent"],
                  ["VAT reg. GB 318 4402 17", "3 Quay Street, Ashby "
                                              "AS2 9QP"],
                  ["accounts@ryeandcrumb.example", "PO 2027-10"]]},
        {"heading": "Summary of deliveries", "kind": "table",
         "whole": True, "weight": 0.1, "columns": ITEMS,
         "rows": [
             ["Country sourdough, 800 g", "248", "€3.40", "0 %",
              "€843.20"],
             ["Seeded rye, 750 g", "112", "€3.80", "0 %", "€425.60"],
             ["Baguette", "496", "€1.15", "0 %", "€570.40"],
             ["Ciabatta rolls, tray of 12", "62", "€6.60", "0 %",
              "€409.20"],
             ["Butter croissant", "620", "€0.92", "20 %", "€570.40"],
             ["Pain au chocolat", "372", "€1.05", "20 %", "€390.60"],
             ["Cinnamon knot", "186", "€1.20", "20 %", "€223.20"],
             ["Delivery, 31 drops", "31", "€3.00", "20 %", "€93.00"],
             {"cells": ["Subtotal", "", "", "", "€3,525.60"],
              "style": "subtotal"},
             {"cells": ["Early payment discount 2 % on bread", "", "",
                        "", "−€44.97"], "style": "muted"},
             {"cells": ["VAT at 20 % on €1,277.20", "", "", "",
                        "€255.44"], "style": "indent"},
             {"cells": ["Brought forward, invoice RC-2027-1094", "", "",
                        "", "€176.40"], "style": "indent"},
             {"cells": ["Amount due", "", "", "", "€3,912.47"],
              "style": "total"},
         ]},
        {"heading": "How to pay", "kind": "callout", "weight": 0.2,
         "tone": "accent", "label": "Bank transfer",
         "text": "to Rye & Crumb Ltd · IBAN GB29 NWBK 6016 1331 9268 19 · "
                 "reference **RC-2027-1186** · by 15 November. The 2 % "
                 "discount on bread applies if paid by 8 November."},
        {"heading": "Deliveries by week", "kind": "figure",
         "weight": 0.3, "min_pages": 2, "height": 140, "widths": [3, 2],
         "charts": [
             {"type": "bars", "stacked": True, "title": "Value delivered",
              "subtitle": "€", "categories": ["Week 40", "Week 41",
                                               "Week 42", "Week 43",
                                               "Week 44"],
              "format": "{:,.0f}",
              "series": [{"name": "Bread", "values": [520, 548, 562, 531,
                                                      87]},
                         {"name": "Pastry", "values": [268, 281, 276, 296,
                                                       63]},
                         {"name": "Delivery", "color": 4,
                          "values": [21, 21, 21, 21, 9]}]},
             {"type": "donut", "title": "This invoice",
              "segments": [("Bread", 2248.4), ("Pastry", 1184.2),
                           ("Delivery", 93.0, 4)],
              "format": "€{:,.0f}", "center": ("€3,526", "before VAT")},
         ]},
        {"heading": "Delivery days", "kind": "table", "weight": 0.4,
         "step": 0.02, "min_pages": 2,
         "columns": [("Date", 0.9), ("Note", 0.9), ("Bread", 1.5),
                     ("Pastry", 1.5), ("Value", 0.9, "end")],
         "rows": [
             ["Wed 1 Oct", "DN 4410", "8 sourdough, 4 rye, 16 baguette",
              "20 croissant, 12 pain", "€129.00"],
             ["Thu 2 Oct", "DN 4422", "8 sourdough, 4 rye, 16 baguette",
              "20 croissant, 12 pain", "€129.00"],
             ["Fri 3 Oct", "DN 4437", "10 sourdough, 4 rye, 18 baguette, "
              "2 ciabatta", "24 croissant, 14 pain, 8 knots", "€171.11"],
             ["Sat 4 Oct", "DN 4451", "10 sourdough, 4 rye, 20 baguette, "
              "4 ciabatta", "28 croissant, 16 pain, 12 knots",
              "€208.07"],
             ["Sun 5 Oct", "DN 4463", "6 sourdough, 2 rye, 12 baguette, "
              "4 ciabatta", "26 croissant, 14 pain, 10 knots",
              "€160.10"],
             ["Mon 6 Oct to Fri 31 Oct", "26 notes", "on the attached "
              "delivery notes", "", "€2,728.32"],
         ]},
        {"heading": "Statement of account", "kind": "table",
         "weight": 0.6, "step": 0.05, "min_pages": 4,
         "badges": {"Paid": "good", "Part paid": "warn", "Open": "bad"},
         "columns": [("Date", 1), ("Document", 1.6), ("Charges", 1,
                                                      "end"),
                     ("Payments", 1, "end"), ("Balance", 1, "end"),
                     ("", 0.9, "center")],
         "rows": [
             ["1 Aug", "Invoice RC-2027-0902", "€3,614.20", "", "€3,614.20",
              "Paid"],
             ["14 Aug", "Payment, thank you", "", "€3,614.20", "€0.00",
              ""],
             ["1 Sep", "Invoice RC-2027-0998", "€3,702.55", "",
              "€3,702.55", "Paid"],
             ["12 Sep", "Payment, thank you", "", "€3,702.55", "€0.00",
              ""],
             ["1 Oct", "Invoice RC-2027-1094", "€3,876.40", "",
              "€3,876.40", "Part paid"],
             ["15 Oct", "Payment, thank you", "", "€3,700.00", "€176.40",
              ""],
             ["1 Nov", "Invoice RC-2027-1186", "€3,736.07", "",
              "€3,912.47", "Open"],
         ]},
        {"heading": "Account history", "kind": "figure", "weight": 0.7,
         "min_pages": 4, "height": 140, "charts": [{"type": "line",
          "title": "Monthly invoices", "subtitle": "€, 2027",
          "x": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
                "Sep", "Oct"], "format": "{:,.0f}",
          "series": [{"name": "Invoiced", "area": True,
                      "values": [2810, 2690, 3020, 3240, 3480, 3590, 3720,
                                 3614, 3703, 3736]}],
          "end_labels": True}]},
        {"heading": "Terms", "kind": "bullets", "weight": 0.8,
         "step": 0.1, "min_pages": 4, "items": [
             "Payment within 14 days of the invoice date. Late payments "
             "carry interest at 8 % above the base rate under the Late "
             "Payment of Commercial Debts Act.",
             "Bread is zero-rated for VAT; pastries, cakes sold hot and "
             "delivery are standard-rated.",
             "Shortages or damaged goods must be reported on the day of "
             "delivery; we credit them on the next invoice.",
             "Standing orders can be changed until 14:00 the day before "
             "delivery on 01234 567 890.",
         ]},
        {"heading": "Thank you", "kind": "motto", "weight": 0.9,
         "min_pages": 2, "text": "Baked overnight with organic flour from "
         "Ashby Mill, three miles from your café."},
        {"heading": "Your most ordered", "kind": "figure", "weight": 1.0,
         "min_pages": 4, "height": 130, "charts": [{"type": "bars",
          "horizontal": True, "title": "Units this year",
          "format": "{:,.0f}",
          "categories": ["Baguette", "Butter croissant",
                         "Pain au chocolat", "Country sourdough",
                         "Cinnamon knot", "Seeded rye"],
          "series": [{"name": "Units", "values": [4710, 5820, 3490, 2380,
                                                  1650, 1060]}]}]},
        {"heading": "Price list for November", "kind": "table",
         "weight": 1.1, "step": 0.05, "min_pages": 4,
         "columns": [("Product", 2.6), ("Price", 0.8, "end"),
                     ("Change", 0.8, "end"), ("Order by", 1.4)],
         "rows": [
             ["Country sourdough, 800 g", "€3.40", "—", "14:00 day before"],
             ["Seeded rye, 750 g", "€3.80", "—", "14:00 day before"],
             ["Baguette", "€1.15", "—", "14:00 day before"],
             ["Butter croissant", "€0.95", "+€0.03", "14:00 day before"],
             ["Stollen, 1 kg (Christmas)", "€12.50", "new",
              "1 December"],
             ["Panettone, 750 g (Christmas)", "€14.00", "new",
              "1 December"],
         ]},
        {"kind": "callout", "weight": 1.2, "tone": "info",
         "min_pages": 4, "label": "Butter:",
         "text": "the croissant price rises by 3 cents from 1 December, "
                 "the first change in eighteen months, after two butter "
                 "price rises from the creamery."},
    ],
}
