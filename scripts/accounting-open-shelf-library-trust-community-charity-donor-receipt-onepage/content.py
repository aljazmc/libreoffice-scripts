"""Donation Receipt of Open Shelf Library Trust: the business and everything
the document could say. The typesetting keeps what fits into one page, the
most important first."""

BUSINESS = {
    "name": "Open Shelf Library Trust",
    "author": "Open Shelf Library Trust",
}

GIFTS = [("15 Apr 2026", "Monthly gift, April – March (12 × £25)", 300.00,
          True),
         ("2 Sep 2026", "Summer reading challenge appeal", 150.00, True),
         ("10 Dec 2026", "Christmas appeal for the mobile library van",
          250.00, True),
         ("8 Mar 2027", "Second-hand books donated and sold", 64.00,
          False)]
CASH = sum(a for _, _, a, ga in GIFTS if ga)
GIFT_AID = round(CASH * 0.25, 2)


def gbp(value):
    return f"£{value:,.2f}"


DOCUMENT = {
    "title": "Thank You",
    "eyebrow": "Open Shelf Library Trust · donation receipt",
    "subtitle": "Your gifts in the year 1 April 2026 to 31 March 2027",
    "meta": [("Donor", "Mr Tom Fletcher"), ("Supporter no.", "D0102"),
             ("Given", gbp(CASH)), ("Gift Aid added", gbp(GIFT_AID)),
             ("Receipt", "R-2027-0102")],
    "sections": [
        {"kind": "text", "weight": 0.05, "paragraphs": [
             "Dear Tom,",
             "Thank you. This year you gave the trust "
             f"**{gbp(CASH)}**, and because you are a UK taxpayer who "
             f"made a Gift Aid declaration, the government added "
             f"**{gbp(GIFT_AID)}**. Together that is "
             f"{gbp(CASH + GIFT_AID)} for the libraries of Hull. This "
             "receipt lists your gifts for your records and your tax "
             "return.",
         ]},
        {"heading": "Your gifts", "kind": "table", "whole": True,
         "weight": 0.1,
         "badges": {"Yes": "good", "No": "neutral"},
         "columns": [("Date", 1), ("Gift", 3), ("Amount", 1, "end"),
                     ("Gift Aid", 0.8, "center")],
         "rows": [[d, g, gbp(a), "Yes" if ga else "No"]
                  for d, g, a, ga in GIFTS]
         + [{"cells": ["", "Cash gifts eligible for Gift Aid", gbp(CASH),
                       ""], "style": "subtotal"},
            {"cells": ["", "Gift Aid claimed by the trust",
                       gbp(GIFT_AID), ""], "style": "indent"},
            {"cells": ["", "Total value to the trust",
                       gbp(CASH + GIFT_AID + 64), ""],
             "style": "total"}]},
        {"heading": "For your tax return", "kind": "callout",
         "weight": 0.2, "tone": "accent", "label": "Higher-rate taxpayer?",
         "text": f"You can claim back the difference between the higher "
                 f"and the basic rate on your gross gifts of "
                 f"{gbp(CASH + GIFT_AID)}: up to "
                 f"{gbp((CASH + GIFT_AID) * 0.2)} at 40 %. Enter "
                 f"{gbp(CASH)} as Gift Aid payments on your Self "
                 "Assessment return."},
        {"heading": "What your gifts did", "kind": "figure",
         "weight": 0.3, "min_pages": 2, "height": 130, "charts": [{
             "type": "kpis", "tiles": [
                 {"label": "Books", "value": "68", "status": 0,
                  "note": "new children's books"},
                 {"label": "Reading sessions", "value": "9",
                  "status": 1, "note": "for a class of 30"},
                 {"label": "Van fund", "value": "£312", "status": 2,
                  "note": "with Gift Aid"},
                 {"label": "Hours open", "value": "21",
                  "status": 3, "note": "of a Saturday library"}]}]},
        {"heading": "Where every pound goes", "kind": "figure",
         "weight": 0.4, "min_pages": 2, "height": 140, "charts": [{
             "type": "donut", "segments": [("Libraries and reading "
                                            "rooms", 59),
                                           ("Children's reading", 21),
                                           ("Digital classes", 10),
                                           ("Raising funds", 10)],
             "format": "{:.0f}p", "center": ("£1", "donated")}]},
        {"kind": "text", "weight": 0.5, "min_pages": 2, "paragraphs": [
             "With warm thanks,",
             "**Sophie Marlowe**, director, and everyone at Open Shelf",
         ]},
        {"heading": "The trust's year", "kind": "table", "whole": True,
         "weight": 0.6, "min_pages": 4,
         "columns": [("", 3), ("2026/27", 1, "end")],
         "rows": [["Income", "£467,000"], ["Spent on the libraries and "
                                           "reading", "£359,800"],
                  ["Spent on raising funds", "£38,400"],
                  ["Volunteers", "212 people, 18,400 hours"],
                  ["Visits to the libraries", "96,300"]]},
        {"heading": "Visits", "kind": "figure", "weight": 0.7,
         "min_pages": 4, "height": 140, "charts": [{"type": "bars",
          "title": "Library visits", "subtitle": "thousands",
          "format": "{:.1f}", "categories": ["2023", "2024", "2025",
                                              "2026", "2027"],
          "series": [{"name": "Visits", "values": [71.2, 78.4, 84.1, 89.0,
                                                   96.3],
                      "colors": [4, 4, 4, 4, 0]}]}]},
        {"heading": "The mobile library van", "kind": "text",
         "weight": 0.8, "step": 0.3, "min_pages": 4, "paragraphs": [
             "Your Christmas gift went to the van appeal. The old van, "
             "bought in 2009, visits fourteen villages and two care homes "
             "every fortnight; it failed its last inspection twice. We "
             "have raised £14,900 of the £42,000 needed and will order "
             "the new van once the appeal reaches £35,000.",
         ]},
        {"heading": "Your declaration", "kind": "tags", "weight": 0.9,
         "step": 0.1, "min_pages": 4, "items": [
             ("Made on", "12 March 2019, online"),
             ("Covers", "all gifts from that date until you tell us"),
             ("Please tell us if", "you stop paying enough income or "
                                   "capital gains tax, or move house"),
         ]},
        {"heading": "Contact", "kind": "tags", "weight": 1.0, "step": 0.1,
         "min_pages": 4, "items": [
             ("Supporter care", "01482 555 0164, Monday to Friday"),
             ("Email", "hello@openshelf.example"),
             ("Charity", "registered charity 1187342"),
         ]},
        {"heading": "Your giving over the years", "kind": "figure",
         "weight": 1.1, "min_pages": 4, "height": 150, "charts": [{
             "type": "bars", "stacked": True, "subtitle": "£ a year",
             "format": "£{:,.0f}",
             "categories": ["2019/20", "2020/21", "2021/22", "2022/23",
                            "2023/24", "2024/25", "2025/26", "2026/27"],
             "series": [{"name": "Your gifts", "values": [
                 120, 240, 300, 300, 420, 450, 500, CASH]},
                        {"name": "Gift Aid", "color": 1, "values": [
                            30, 60, 75, 75, 105, 112.5, 125, GIFT_AID]}]}]},
        {"heading": "Three ways to give more without spending more",
         "kind": "entries", "weight": 1.2, "step": 0.2, "inner": 0.1,
         "min_pages": 4, "entries": [
             {"title": "Ask your employer to match", "text": [
                 "Many employers match gifts to charities pound for "
                 "pound; Harbour Print and the council both do."]},
             {"title": "Give through payroll", "text": [
                 "Payroll giving comes out before tax, so a £10 gift "
                 "costs a basic-rate taxpayer £8."]},
             {"title": "Remember us in your will", "text": [
                 "Gifts to charity are free of inheritance tax; Mrs "
                 "Marsh's legacy furnished the children's library at "
                 "Northgate."]},
         ]},
        {"heading": "Our promise", "kind": "bullets", "weight": 1.3,
         "step": 0.1, "min_pages": 4, "items": [
             "We will never sell or swap your details.",
             "We spend restricted gifts only on what you gave them for.",
             "We publish our accounts every year at openshelf.example.",
             "You can change how we contact you at any time.",
         ]},
        {"heading": "Libraries you help to keep open", "kind": "table",
         "whole": True, "weight": 1.4, "min_pages": 4,
         "columns": [("Library", 1.8), ("Open", 2.2),
                     ("Visits a year", 1, "end")],
         "rows": [["Northgate", "Mon – Sat, 9:30 – 18:00", "38,200"],
                  ["Westfield", "Tue – Sat, 10:00 – 17:00", "24,600"],
                  ["Marfleet reading room", "Mon – Fri, 15:00 – 18:00",
                   "6,700"],
                  ["Mobile library", "14 villages, every fortnight",
                   "11,900"]]},
        {"kind": "motto", "weight": 1.5, "min_pages": 4,
         "text": "A library is the one place in town where you are "
                 "welcome without spending money. Thank you for keeping "
                 "it that way."},
    ],
}
