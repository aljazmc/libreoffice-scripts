"""Statement of Financial Activities of Open Shelf Library Trust: the business
and everything the document could say. The typesetting keeps what fits into
two pages, the most important first."""

BUSINESS = {
    "name": "Open Shelf Library Trust",
    "author": "Open Shelf Library Trust, the trustees",
}


def k(value):
    return f"({-value:,})" if value < 0 else f"{value:,}" if value else "—"


# £: unrestricted, restricted, endowment; prior year total
INCOME = [("Donations and legacies", 148_200, 22_000, 0, 131_400),
          ("Grants", 18_000, 196_500, 0, 172_800),
          ("Library memberships and room hire", 41_600, 0, 0, 38_900),
          ("Café and second-hand book sales", 33_900, 0, 0, 30_200),
          ("Investment income", 6_800, 0, 0, 5_900)]
SPEND = [("Raising funds", -38_400, 0, 0, -35_100),
         ("Libraries and reading rooms", -96_300, -138_200, 0, -221_700),
         ("Reading programmes for children", -21_800, -61_400, 0,
          -74_600),
         ("Digital inclusion classes", -14_200, -27_900, 0, -38_300)]
GAINS = [("Gains on investments", 9_400, 0, 3_100, 4_800)]
TRANSFERS = [("Transfer to fund the reading room roof", -12_000, 12_000,
              0, 0)]
OPENING = [312_400, 84_600, 150_000, 532_700]


def col(lines, i):
    return sum(line[i] for line in lines)


TI = [col(INCOME, i) for i in range(1, 5)]
TS = [col(SPEND, i) for i in range(1, 5)]
G = [col(GAINS, i) for i in range(1, 5)]
TR = [col(TRANSFERS, i) for i in range(1, 5)]
NET = [TI[i] + TS[i] + G[i] + TR[i] for i in range(4)]
CLOSING = [OPENING[i] + NET[i] for i in range(4)]


def total_row(label, values, style):
    current = sum(values[:3])
    return {"cells": [label] + [k(v) for v in values[:3]] + [k(current),
                                                            k(values[3])],
            "style": style}


def line(name, *values):
    return {"cells": [name] + [k(v) for v in values[:3]]
            + [k(sum(values[:3])), k(values[3])], "style": "indent"}


COLUMNS = [("£", 2.0), ("Unrestricted", 1.2, "end"),
           ("Restricted", 1.05, "end"), ("Endowment", 1.05, "end"),
           ("Total 2027", 1, "end"), ("Total 2026", 1, "end")]

DOCUMENT = {
    "title": "Statement of Financial Activities",
    "subtitle": "For the year ended 31 March 2027 · including the income "
                "and expenditure account",
    "meta": [("Charity no.", "1187342"),
             ("Income", f"£{sum(TI[:3]):,}"),
             ("Spending", f"£{-sum(TS[:3]):,}"),
             ("Total funds", f"£{sum(CLOSING[:3]):,}"),
             ("Examined", "Independently")],
    "sections": [
        {"heading": "Statement", "kind": "table", "whole": True,
         "weight": 0.1, "columns": COLUMNS,
         "rows": [{"cells": ["Income from", "", "", "", "", ""],
                   "style": "section"}]
         + [line(n, *v) for n, *v in INCOME]
         + [total_row("Total income", TI, "subtotal"),
            {"cells": ["Expenditure on", "", "", "", "", ""],
             "style": "section"}]
         + [line(n, *v) for n, *v in SPEND]
         + [total_row("Total expenditure", TS, "subtotal")]
         + [line(n, *v) for n, *v in GAINS]
         + [line(n, *v) for n, *v in TRANSFERS]
         + [total_row("Net movement in funds", NET, "highlight"),
            total_row("Funds at 1 April 2026", OPENING, "indent"),
            total_row("Funds at 31 March 2027", CLOSING, "total")]},
        {"heading": "Where the money came from and went", "kind": "figure",
         "weight": 0.2, "height": {1: 170, 2: 200, 4: 220}, "charts": [{
             "type": "sankey", "format": "£{:,.0f}k",
             "nodes": [{"id": "don", "label": "Donations", "col": 0,
                        "color": 0},
                       {"id": "gra", "label": "Grants", "col": 0,
                        "color": 1},
                       {"id": "tra", "label": "Memberships, café, shop",
                        "col": 0, "color": 2},
                       {"id": "inv", "label": "Investments", "col": 0,
                        "color": 4},
                       {"id": "inc", "label": "Income", "col": 1,
                        "color": 0},
                       {"id": "lib", "label": "Libraries", "col": 2,
                        "color": 0},
                       {"id": "chi", "label": "Children's reading",
                        "col": 2, "color": 1},
                       {"id": "dig", "label": "Digital classes",
                        "col": 2, "color": 2},
                       {"id": "rai", "label": "Fundraising", "col": 2,
                        "color": 4},
                       {"id": "sur", "label": "Surplus", "col": 2,
                        "color": "good"}],
             "links": [("don", "inc", 170), ("gra", "inc", 215),
                       ("tra", "inc", 75), ("inv", "inc", 7),
                       ("inc", "lib", 235), ("inc", "chi", 83),
                       ("inc", "dig", 42), ("inc", "rai", 38),
                       ("inc", "sur", 69)]}]},
        {"heading": "Charitable spending", "kind": "figure",
         "weight": 0.3, "min_pages": 2, "charts": [{"type": "kpis",
          "tiles": [
              {"label": "Spent on the cause", "value":
               f"{(sum(TS[:3]) - SPEND[0][1]) / sum(TS[:3]):.0%}",
               "status": 0, "note": "of every pound spent"},
              {"label": "Fundraising ratio", "value":
               f"£{-SPEND[0][1] / sum(INCOME[0][1:4]):.2f}",
               "status": 1, "note": "to raise £1 of donations"},
              {"label": "Free reserves", "value": "7.4 months",
               "status": "good", "note": "policy 6 months"},
              {"label": "Volunteers", "value": "212", "status": 2,
               "note": "18,400 hours given"}]}]},
        {"heading": "Notes", "kind": "entries", "weight": 0.4,
         "step": 0.15, "inner": 0.05, "min_pages": 2, "entries": [
             {"title": "1. Grants", "text": [
                 "£196,500 of restricted grants: the Reading Rooms grant "
                 "from the Northfield Foundation (£120,000), the Town "
                 "Council's library service agreement (£52,500) and the "
                 "Digital Skills Fund (£24,000)."]},
             {"title": "2. Legacies", "text": [
                 "A legacy of £22,000 from Mrs Edith Marsh is restricted "
                 "to the children's library at Northgate."]},
             {"title": "3. Transfer", "text": [
                 "The trustees moved £12,000 of unrestricted funds to the "
                 "roof fund, which the Heritage Grant did not fully "
                 "cover."]},
             {"title": "4. Endowment", "text": [
                 "The Arthur Pell endowment of £150,000 is invested; only "
                 "its income may be spent."]},
         ]},
        {"heading": "Funds", "kind": "figure", "weight": 0.5,
         "min_pages": 4, "height": 160, "widths": [3, 2], "charts": [
             {"type": "bars", "title": "Funds at 31 March", "subtitle":
              "£k", "stacked": True, "format": "{:,.0f}",
              "categories": ["2023", "2024", "2025", "2026", "2027"],
              "series": [{"name": "Unrestricted", "values": [
                  241, 262, 288, 312, CLOSING[0] / 1000]},
                         {"name": "Restricted", "color": 1, "values": [
                             61, 72, 79, 85, CLOSING[1] / 1000]},
                         {"name": "Endowment", "color": 4, "values": [
                             150, 150, 150, 150, CLOSING[2] / 1000]}]},
             {"type": "donut", "title": "Spending by purpose",
              "segments": [(n.split(" for")[0], -sum(v[:3]))
                           for n, *v in SPEND],
              "format": "£{:,.0f}", "center": (f"£{-sum(TS[:3]) / 1000:.0f}k",
                                               "spent")},
         ]},
        {"heading": "Staff and trustees", "kind": "table", "whole": True,
         "weight": 0.6, "min_pages": 4,
         "columns": [("", 3), ("2027", 1, "end"), ("2026", 1, "end")],
         "rows": [["Average staff, full-time equivalent", "8.4", "8.1"],
                  ["Staff costs", "£212,600", "£201,300"],
                  ["Employees paid over £60,000", "0", "0"],
                  ["Trustees' remuneration", "£0", "£0"],
                  ["Trustees' expenses reimbursed (2 trustees)", "£318",
                   "£276"]]},
        {"heading": "Structure", "kind": "text", "weight": 0.7,
         "step": 0.3, "min_pages": 4, "paragraphs": [
             "The trust is a charitable incorporated organisation that "
             "runs three community libraries, a reading room and a "
             "mobile library in the Hull area, with eight staff and over "
             "two hundred volunteers.",
             "These accounts follow the Charities SORP (FRS 102). "
             "Restricted funds may only be spent on the purpose the donor "
             "gave them for; unrestricted funds on any of the trust's "
             "purposes; endowment capital may not be spent at all.",
         ]},
        {"heading": "Approved by the trustees", "kind": "table",
         "look": "plain", "header": False, "whole": True,
         "weight": 0.8, "min_pages": 4, "columns": [("", 1), ("", 1)],
         "rows": [["Dr Helen Ashworth, chair", "Raj Patel, treasurer"],
                  ["14 July 2027", "14 July 2027"]]},
        {"heading": "Income over five years", "kind": "figure",
         "weight": 0.75, "min_pages": 4, "height": 150, "charts": [{
             "type": "line", "subtitle": "£k", "format": "{:,.0f}",
             "x": ["2023", "2024", "2025", "2026", "2027"],
             "end_labels": True,
             "series": [{"name": "Income", "values": [318, 342, 361, 379,
                                                      sum(TI[:3]) / 1000]},
                        {"name": "Expenditure", "color": 1,
                         "values": [301, 330, 352, 370,
                                    -sum(TS[:3]) / 1000]}]}]},
    ],
}
