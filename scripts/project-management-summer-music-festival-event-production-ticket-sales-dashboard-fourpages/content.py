"""Ticket Sales Dashboard of Saltmarsh Sound Festival: the project and
everything the document could say. The typesetting keeps what fits into four
pages, the most important first."""

PROJECT = {
    "name": "Saltmarsh Sound Festival",
    "code": "SSF-27",
    "author": "Hana Sato, Head of Marketing",
}

WEEKS = ["−36", "−32", "−28", "−24", "−20", "−16", "−12", "−8", "−4",
         "0"]

DOCUMENT = {
    "title": "Ticket Sales Dashboard",
    "subtitle": "Twelve weeks to go · sales to Sunday 25 April 2027",
    "meta": [("Edition", "2027"), ("Week", "T−12"),
             ("Capacity", "60,000 tickets"), ("Sold", "41,200"),
             ("Status", "Ahead of plan")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "charts": [{"type": "kpis",
         "tiles": [
             {"label": "Sold", "value": "69 %", "delta": "+6 pts",
              "status": 2, "note": "41,200 of 60,000",
              "spark": [8, 15, 22, 30, 38, 47, 55, 63, 69]},
             {"label": "Revenue", "value": "€2.92m", "status": 0,
              "note": "net of fees and VAT"},
             {"label": "This week", "value": "1,840", "delta": "+22 %",
              "status": 1, "note": "after the Sunday line-up"},
             {"label": "Forecast", "value": "97 %", "status": 3,
              "note": "sell-through at the gate"},
         ]}]},
        {"heading": "Sales against plan", "kind": "figure", "weight": 0.2,
         "height": {1: 185, 2: 195, 4: 210}, "charts": [{"type": "line",
          "title": "Cumulative tickets sold", "subtitle": "thousands, "
          "weeks to the festival", "x": WEEKS, "format": "{:.0f}",
          "target": 60, "target_label": "capacity", "end_labels": True,
          "marks": [(3, "line-up"), (6, "Sunday headliner")],
          "series": [
              {"name": "2027", "area": True,
               "values": [4.8, 9.0, 13.2, 18.0, 22.8, 28.2, 41.2, None,
                          None, None]},
              {"name": "Plan", "dash": True, "color": 4,
               "values": [4.0, 8.0, 12.0, 16.5, 21.0, 26.0, 37.5, 47.0,
                          54.0, 58.0]},
              {"name": "2026", "color": 3,
               "values": [3.6, 7.2, 10.8, 14.4, 19.6, 24.0, 34.8, 44.4,
                          52.2, 57.6]}]}]},
        {"heading": "By ticket type", "kind": "figure", "weight": 0.3,
         "height": {1: 125, 2: 140, 4: 150}, "charts": [{"type": "bars",
          "horizontal": True, "stacked": True, "values": True,
          "format": "{:,.0f}",
          "categories": ["Weekend camping", "Weekend day", "Friday",
                         "Saturday", "Sunday", "Under 16s"],
          "series": [{"name": "Sold", "values": [14200, 9800, 4100, 6400,
                                                 4900, 1800]},
                     {"name": "Left", "color": 4,
                      "values": [800, 3200, 3900, 1600, 3100, 2200]}],
          "inside": True}]},
        {"heading": "Channels", "kind": "figure", "weight": 0.4,
         "min_pages": 2, "height": 155, "widths": [2, 3], "charts": [
             {"type": "donut", "title": "Where tickets were bought",
              "segments": [("Our website", 24100), ("Ticket partner",
                                                    9800),
                           ("App", 4600), ("Box office", 900),
                           ("Groups and schools", 1800)],
              "format": "{:,.0f}", "center": ("41,200", "tickets")},
             {"type": "funnel", "title": "Website, last 4 weeks",
              "format": "{:,.0f}",
              "stages": [("Visits to the tickets page", 182000),
                         ("Chose a ticket", 41000),
                         ("Started checkout", 14200),
                         ("Paid", 9100)]},
         ]},
        {"heading": "Where buyers live", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": 150, "charts": [{"type": "bars",
          "title": "Tickets by region", "subtitle": "thousands",
          "format": "{:.1f}",
          "categories": ["Within 30 km", "Rest of region", "Capital",
                         "North", "Rest of country", "Abroad"],
          "series": [{"name": "2026", "color": 4,
                      "values": [9.8, 8.4, 6.1, 3.2, 4.9, 2.4]},
                     {"name": "2027", "values": [10.4, 9.1, 8.9, 3.6,
                                                 5.8, 3.4]}]}]},
        {"heading": "What moved sales", "kind": "entries", "weight": 0.6,
         "step": 0.2, "inner": 0.1, "min_pages": 2, "entries": [
             {"title": "Sunday headliner announced", "dates": "T−16",
              "text": ["3,400 tickets in four days, the best week since "
                       "the early bird; Sunday day tickets doubled."]},
             {"title": "Payment plan in three instalments",
              "dates": "since T−30", "text": [
                  "Used by 22 % of weekend buyers, most of them under "
                  "25; no increase in failed payments."]},
             {"title": "Price step to tier 3", "dates": "T−20", "text": [
                 "The week before the step sold 2.3 times the average; "
                 "we will announce the next step two weeks ahead."]},
         ]},
        {"heading": "Marketing plan to sell-out", "kind": "figure",
         "weight": 0.8, "min_pages": 4, "height": 120, "charts": [{
             "type": "timeline", "start": -12, "end": 0,
             "label_width": 100,
             "ticks": [(-12, "T−12"), (-9, "T−9"), (-6, "T−6"),
                       (-3, "T−3"), (0, "festival")],
             "events": [
                 {"at": -11, "label": "Stage splits", "sub": "who plays "
                  "when", "status": "now"},
                 {"at": -9, "label": "Radio partnership", "sub": "4 "
                  "weeks"},
                 {"at": -7, "label": "Day tickets push", "sub": "social"},
                 {"at": -5, "label": "Final price step", "sub": "tier "
                  "4"},
                 {"at": -3, "label": "Last tickets email",
                  "sub": "to the waiting list"},
                 {"at": -1, "label": "Gate sale decision",
                  "sub": "if any left"},
             ]}]},
        {"heading": "Ticket prices", "kind": "table", "weight": 0.9,
         "step": 0.1, "min_pages": 4, "badges": {"Sold out": "bad",
                                                "On sale": "good",
                                                "Next": "neutral"},
         "columns": [("Tier", 1.4), ("Weekend camping", 1.3, "end"),
                     ("Weekend day", 1.3, "end"), ("Day", 1, "end"),
                     ("Status", 1.1, "center")],
         "rows": [
             ["Early bird", "€149", "€119", "—", "Sold out"],
             ["Tier 1", "€169", "€135", "€59", "Sold out"],
             ["Tier 2", "€185", "€149", "€65", "Sold out"],
             ["Tier 3", "€199", "€159", "€69", "On sale"],
             ["Tier 4", "€215", "€169", "€75", "Next"],
         ]},
        {"heading": "Audience", "kind": "figure", "weight": 1.0,
         "min_pages": 4, "height": 140, "widths": [1, 1], "charts": [
             {"type": "bars", "title": "Buyers by age",
              "format": "{:.0f}%",
              "categories": ["16–20", "21–25", "26–35", "36–45", "46–55",
                             "56+"],
              "series": [{"name": "Share", "values": [9, 22, 31, 19, 12,
                                                      7]}]},
             {"type": "progress", "title": "Returning buyers",
              "format": "{:.0f} %", "items": [
                  {"label": "First Saltmarsh", "value": 44, "status": 0},
                  {"label": "Came in 2026", "value": 41, "status": 2},
                  {"label": "Came 3+ times", "value": 23, "status": 1},
              ]},
         ]},
        {"heading": "Watch list", "kind": "bullets", "weight": 1.1,
         "step": 0.2, "min_pages": 4, "items": [
             "Friday is 51 % sold, the weakest day: the stage splits "
             "should help, since two bands from the capital play "
             "Friday.",
             "Under 16s tickets lag; schools are on holiday from 16 July "
             "this year, two days later than last year.",
             "Resale on the official exchange is low (310 tickets), "
             "which suggests demand is genuine.",
         ]},
        {"heading": "Campaign results", "kind": "figure", "weight": 1.05,
         "min_pages": 4, "height": 155, "widths": [3, 2], "charts": [
             {"type": "bars", "horizontal": True, "title": "Tickets by "
              "campaign", "format": "{:,.0f}",
              "categories": ["Line-up announcement", "Early bird email",
                             "Sunday headliner", "Radio partnership",
                             "Creators on social", "Payment plan ads"],
              "series": [{"name": "Tickets",
                          "values": [8200, 6100, 3400, 1900, 1600,
                                     1200]}]},
             {"type": "donut", "title": "Marketing spend",
              "segments": [("Social ads", 62), ("Radio", 38),
                           ("Posters", 24), ("Creators", 18),
                           ("Email", 4)],
              "format": "€{:.0f}k", "center": ("€146k", "to date")},
         ]},
        {"heading": "Weekly sales", "kind": "figure", "weight": 1.08,
         "min_pages": 4, "height": 140, "charts": [{"type": "bars",
          "title": "Tickets sold per week", "subtitle": "last 16 weeks",
          "values": False,
          "categories": ["−27", "−26", "−25", "−24", "−23", "−22", "−21",
                         "−20", "−19", "−18", "−17", "−16", "−15", "−14",
                         "−13", "−12"],
          "series": [{"name": "Tickets",
                      "values": [1100, 980, 1240, 1310, 1020, 1150, 1210,
                                 2380, 960, 1050, 1120, 3400, 1980,
                                 1460, 1510, 1840],
                      "colors": [4, 4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 0, 4,
                                 4, 4, 2]}]}]},
    ],
}
