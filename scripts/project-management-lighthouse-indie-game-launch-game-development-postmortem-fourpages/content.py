"""Postmortem of Keeper of the Last Light: the project and everything the
document could say. The typesetting keeps what fits into four pages, the
most important first."""

PROJECT = {
    "name": "Keeper of the Last Light",
    "code": "KLL",
    "author": "Mira Okonkwo, Producer, Tidepool Games",
}

DOCUMENT = {
    "title": "Postmortem",
    "subtitle": "What went right and what went wrong, three months after "
                "launch · June 2027",
    "meta": [("Launched", "12 Mar 2027"), ("Copies sold", "86,400"),
             ("Steam reviews", "94 % positive"),
             ("Recouped", "Week 5"), ("Author", "Mira Okonkwo")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "charts": [{"type": "kpis",
         "tiles": [
             {"label": "Copies", "value": "86,400", "status": 0,
              "note": "PC 61 %, Switch 39 %", "delta": "+44 %",
              "delta_status": "good"},
             {"label": "Net revenue", "value": "€1.18m", "status": 1,
              "note": "after stores and VAT"},
             {"label": "Reviews", "value": "94 %", "status": 2,
              "note": "3,210 on Steam"},
             {"label": "Refunds", "value": "3.1 %", "status": "good",
              "note": "genre average 6 %"},
         ]}]},
        {"heading": "What went right, what went wrong", "kind": "figure",
         "weight": 0.2, "charts": [{"type": "board", "size": 6.8,
          "columns": [
              {"title": "Right", "tone": 0, "cards": [
                  "The night rescue: in every review and every clip",
                  "Monthly Steam playtests from alpha",
                  "No crunch, and nobody left",
                  "Cutting the lightship island early"]},
              {"title": "Wrong", "tone": "bad", "cards": [
                  "Switch port started too late",
                  "Controller crafting found only at playtest 6",
                  "Letters system rewritten twice",
                  "Day-one patch of 1.2 GB on Switch"]},
          ]}]},
        {"heading": "Sales", "kind": "figure", "weight": 0.3,
         "height": {1: 150, 2: 160, 4: 170}, "widths": [3, 2],
         "charts": [
             {"type": "line", "title": "Copies sold", "subtitle":
              "thousands, cumulative, by week",
              "x": ["W1", "W2", "W3", "W4", "W6", "W8", "W10", "W13"],
              "format": "{:.0f}", "target": 41, "target_label":
              "break-even", "end_labels": True,
              "series": [{"name": "PC", "values": [16, 22, 26, 30, 35,
                                                   41, 46, 52.7]},
                         {"name": "Switch", "color": 1,
                          "values": [7, 11, 14, 17, 21, 25, 29, 33.7]}]},
             {"type": "donut", "title": "Revenue by store",
              "segments": [("Steam", 690), ("Nintendo eShop", 430),
                           ("GOG and itch", 60)],
              "format": "€{:,.0f}k", "center": ("€1.18m", "net")},
         ]},
        {"heading": "Lessons", "kind": "bullets", "weight": 0.4,
         "step": 0.15, "items": [
             "**Port early.** Start the Switch build at alpha, not beta; "
             "performance problems shape design.",
             "**Test with controllers from day one.** Two thirds of our "
             "players used one.",
             "**Write the systems before the words.** The letters were "
             "rewritten because the system changed under them.",
         ]},
        {"heading": "Timeline", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": 130, "charts": [{"type": "timeline",
          "start": 0, "end": 21, "label_width": 92,
          "ticks": [(0, "Oct 25"), (6, "Apr 26"), (12, "Oct 26"),
                    (17.4, "Mar 27"), (21, "Jun 27")],
          "events": [
              {"at": 1, "label": "Slice", "status": "done"},
              {"at": 4, "label": "Publisher", "status": "done"},
              {"at": 8, "label": "Alpha", "status": "done"},
              {"at": 12, "label": "Beta, port starts late",
               "status": "done"},
              {"at": 15.5, "label": "Gold, 2 weeks late",
               "status": "done"},
              {"at": 17.4, "label": "Launch", "status": "now"},
              {"at": 20, "label": "Fishing update", "status": "done"},
          ]}]},
        {"heading": "Plan against actual", "kind": "table", "weight": 0.6,
         "step": 0.1, "min_pages": 2, "badges": {"Better": "good",
                                                 "Worse": "bad",
                                                 "Same": "neutral"},
         "columns": [("Measure", 2.4), ("Plan", 1.2, "center"),
                     ("Actual", 1.2, "center"), ("", 0.9, "center")],
         "rows": [
             ["Budget", "€640k", "€668k", "Worse"],
             ["Gold master", "15 Jan", "29 Jan", "Worse"],
             ["Launch date", "12 Mar", "12 Mar", "Same"],
             ["Wishlists at launch", "150k", "171k", "Better"],
             ["Copies in 3 months", "60k", "86k", "Better"],
             ["Steam review score", "90 %", "94 %", "Better"],
         ]},
        {"heading": "Reviews", "kind": "figure", "weight": 0.7,
         "min_pages": 2, "height": 140, "charts": [{"type": "bars",
          "horizontal": True, "format": "{:.0f}%",
          "title": "What reviews mention", "subtitle": "% of Steam "
          "reviews",
          "categories": ["Atmosphere", "Music", "Night rescue",
                         "Relaxing", "Too short", "Crafting menu"],
          "series": [{"name": "Mentions", "values": [61, 44, 38, 35, 14,
                                                     7],
                      "colors": [0, 0, 0, 0, "warn", "bad"]}]}]},
        {"heading": "Team", "kind": "text", "weight": 0.9, "step": 0.3,
         "min_pages": 4, "paragraphs": [
             "Seven people made the game in seventeen months without a "
             "single weekend of crunch. The cost was two weeks of delay "
             "on gold and the fishing mini-game, which shipped six weeks "
             "after launch as a free update and brought a second wave "
             "of sales.",
             "Everyone who started the project is still at the studio.",
         ]},
        {"heading": "Where the time went", "kind": "figure",
         "weight": 1.0, "min_pages": 4, "height": 145, "widths": [2, 3],
         "charts": [
             {"type": "donut", "title": "Team months",
              "segments": [("Code", 41), ("Art", 30), ("Design and "
                                                       "writing", 19),
                           ("Audio", 6), ("QA and community", 12)],
              "center": ("108", "months")},
             {"type": "bars", "title": "Rework", "subtitle": "weeks "
              "spent redoing things", "horizontal": True,
              "categories": ["Letters system", "Switch performance",
                             "Crafting UI", "Boat physics"],
              "series": [{"name": "Weeks", "values": [9, 7, 4, 3],
                          "colors": ["bad", "bad", "warn", "warn"]}]},
         ]},
        {"heading": "What we do next", "kind": "entries", "weight": 1.1,
         "step": 0.2, "inner": 0.1, "min_pages": 4, "entries": [
             {"title": "The lightship", "dates": "DLC, autumn 2027",
              "text": ["The island we cut, now with the time to do it "
                       "properly: €4.99, four hours of play."]},
             {"title": "PlayStation and Xbox", "dates": "2028",
              "text": ["With a porting partner, started now, not "
                       "later."]},
             {"title": "The next game", "dates": "prototype in Q3",
              "text": ["Three one-week prototypes; the team votes."]},
         ]},
        {"heading": "Thanks", "kind": "motto", "weight": 1.2,
         "min_pages": 4, "text": "To the 4,200 people on our Discord who "
         "played every build, and to everyone who kept the light "
         "burning."},
        {"heading": "Players", "kind": "figure", "weight": 1.3,
         "min_pages": 4, "height": 130, "charts": [{"type": "funnel",
          "format": "{:,.0f}",
          "stages": [("Bought the game", 86400),
                     ("Finished island 1", 81200),
                     ("Finished island 3", 66900),
                     ("Reached the last light", 47300),
                     ("Found the keeper's secret", 21800)]}]},
        {"heading": "Updates after launch", "kind": "table",
         "weight": 1.35, "step": 0.1, "min_pages": 4,
         "columns": [("Version", 0.9), ("Date", 1), ("What", 4)],
         "rows": [
             ["1.0.1", "13 Mar", "Fix for a save bug on Switch sleep"],
             ["1.0.2", "20 Mar", "Crafting menu speed-up; 11 small "
              "fixes"],
             ["1.1", "23 Apr", "Fishing, photo mode filters, 2 new "
              "letters"],
             ["1.1.1", "14 May", "Steam Deck tweaks, Japanese text "
              "fixes"],
         ]},
    ],
}
