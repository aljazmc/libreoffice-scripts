"""Playtest Report of Keeper of the Last Light: the project and everything the
document could say. The typesetting keeps what fits into two pages, the most
important first."""

PROJECT = {
    "name": "Keeper of the Last Light",
    "code": "KLL",
    "author": "Sanne Visser, Designer, Tidepool Games",
}

ISLANDS = ["1 Harbour", "2 Gull Rock", "3 Fog Bank", "4 The Wreck",
           "5 Storm Isle", "6 Last Light"]

DOCUMENT = {
    "title": "Playtest Report 6",
    "subtitle": "Beta build 0.9.2 · 48 players, 90 minutes each, at home "
                "on Steam · 3 – 10 October 2026",
    "meta": [("Build", "0.9.2 beta"), ("Players", "48"),
             ("Sessions", "72 hours"), ("Rating", "8.1 / 10"),
             ("Designer", "Sanne Visser")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "charts": [{"type": "kpis",
         "tiles": [
             {"label": "Would buy", "value": "79 %", "status": 0,
              "delta": "+11", "note": "playtest 5: 68 %"},
             {"label": "Rating", "value": "8.1", "status": 1,
              "note": "of 10, average"},
             {"label": "Finished island 3", "value": "71 %", "status": 2,
              "note": "in 90 minutes"},
             {"label": "Crashes", "value": "4", "status": "bad",
              "note": "in 72 hours"},
         ]}]},
        {"heading": "Where players stopped", "kind": "figure",
         "weight": 0.2, "height": {1: 135, 2: 145, 4: 150},
         "charts": [{"type": "funnel", "format": "{:.0f}",
          "stages": [("Started", 48), ("Lit the first lamp", 47),
                     ("Rescued the first boat", 44),
                     ("Reached Fog Bank", 39),
                     ("Solved the foghorn puzzle", 34),
                     ("Reached The Wreck", 30)]}]},
        {"heading": "Findings", "kind": "bullets", "weight": 0.3,
         "step": 0.15, "items": [
             "**The foghorn puzzle loses one player in seven.** Most "
             "did not notice that the horn's pitch changes with the "
             "valves.",
             "**The night rescue is the best moment of the game.** 31 "
             "players named it when asked what they would tell a "
             "friend.",
             "**Inventory is confusing on a controller.** Players on a "
             "pad took twice as long to craft their first lens.",
         ]},
        {"heading": "Time on each island", "kind": "figure",
         "weight": 0.4, "min_pages": 2, "height": 155, "widths": [3, 2],
         "charts": [
             {"type": "bars", "title": "Minutes", "subtitle":
              "median, players who reached it",
              "categories": ["Harbour", "Gull", "Fog", "Wreck"],
              "series": [{"name": "Target", "color": 4,
                          "values": [15, 20, 25, 25]},
                         {"name": "Actual", "values": [14, 23, 34,
                                                       21]}]},
             {"type": "donut", "title": "Input device",
              "segments": [("Controller", 29), ("Mouse and keys", 19)],
              "center": ("48", "players")},
         ]},
        {"heading": "Ratings", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": 150, "charts": [{"type": "heatmap",
          "title": "Average rating by island and aspect", "subtitle":
          "1 to 10",
          "rows": ISLANDS[:4],
          "cols": ["Fun", "Clarity", "Mood", "Challenge"],
          "values": [[7.6, 8.8, 8.4, 5.2], [8.2, 8.1, 8.6, 6.4],
                     [7.1, 5.6, 9.1, 7.8], [8.4, 7.7, 8.8, 7.1]],
          "thresholds": [(0, "bad"), (6.5, "warn"), (8, "good")],
          "format": "{:.1f}", "labels": 0.22}]},
        {"heading": "What players said", "kind": "figure", "weight": 0.6,
         "min_pages": 2, "charts": [{"type": "board", "size": 6.8,
          "columns": [
              {"title": "Love", "tone": 0, "cards": [
                  ("“The storm rescue gave me chills.”", "player 12"),
                  ("“I just sat and watched the lamp turn.”",
                   "player 31")]},
              {"title": "Confused", "tone": 3, "cards": [
                  ("“Why does the horn sound different?”", "player 7"),
                  ("“Where did my lens go?”", "player 22")]},
              {"title": "Want", "tone": 2, "cards": [
                  ("“Let me name the boats I save.”", "player 40"),
                  ("“A map of the islands.”", "player 18")]},
          ]}]},
        {"heading": "Changes for the next build", "kind": "table",
         "weight": 0.7, "step": 0.1, "min_pages": 2,
         "badges": {"Must": "bad", "Should": "warn", "Could": "info"},
         "columns": [("Change", 4.2), ("Owner", 1.1),
                     ("Priority", 0.9, "center")],
         "rows": [
             ["Foghorn: show the pitch as rings on the water", "Sanne",
              "Must"],
             ["Controller crafting: radial menu instead of the grid",
              "Jae", "Must"],
             ["Fix the 4 crashes (all in the boat physics)", "Tomás",
              "Must"],
             ["Island map in the keeper's log", "Lena", "Should"],
             ["Name rescued boats", "Sanne", "Could"],
         ]},
        {"heading": "Who played", "kind": "figure", "weight": 0.8,
         "min_pages": 4, "height": 140, "widths": [1, 1], "charts": [
             {"type": "bars", "title": "Age", "categories": ["16–24",
                                                             "25–34",
                                                             "35–44",
                                                             "45+"],
              "series": [{"name": "Players", "values": [11, 19, 12, 6]}]},
             {"type": "progress", "title": "Play cosy games",
              "format": "{:.0f} %", "items": [
                  {"label": "Every week", "value": 54, "status": 0},
                  {"label": "Every month", "value": 31, "status": 2},
                  {"label": "Rarely", "value": 15, "status": 4},
              ]},
         ]},
        {"heading": "Bugs found", "kind": "figure", "weight": 0.9,
         "min_pages": 4, "height": 135, "charts": [{"type": "bars",
          "horizontal": True, "stacked": True, "title": "By area",
          "categories": ["Boat physics", "Inventory", "Weather", "UI",
                         "Audio", "Save"],
          "series": [{"name": "A", "color": "bad",
                      "values": [3, 0, 0, 0, 0, 1]},
                     {"name": "B", "color": "warn",
                      "values": [4, 5, 2, 3, 1, 0]},
                     {"name": "C", "color": 2,
                      "values": [6, 4, 5, 9, 4, 1]}], "inside": True}]},
        {"heading": "Method", "kind": "text", "weight": 1.0, "step": 0.3,
         "min_pages": 4, "paragraphs": [
             "Players were recruited from the Steam playtest sign-ups "
             "who had never played the game. Each played 90 minutes at "
             "home with the session recorded, then answered a survey. "
             "Twelve also joined a 20-minute call.",
             "The funnel and the times come from the game's own "
             "analytics events, which are switched off in the release "
             "build.",
         ]},
        {"heading": "Compared with playtest 5", "kind": "figure",
         "weight": 1.1, "min_pages": 4, "height": 140, "charts": [{
             "type": "line", "title": "Players still playing",
             "subtitle": "% by minute", "x": ["0", "15", "30", "45",
                                             "60", "75", "90"],
             "format": "{:.0f}",
             "series": [{"name": "Playtest 5", "color": 4, "dash": True,
                         "values": [100, 94, 83, 71, 62, 55, 50]},
                        {"name": "Playtest 6", "values": [100, 98, 92,
                                                          85, 79, 74,
                                                          70]}]}]},
        {"heading": "Accessibility", "kind": "figure", "weight": 1.15,
         "min_pages": 4, "height": 130, "charts": [{"type": "progress",
          "format": "{:.0f} %", "items": [
              {"label": "Used subtitles", "value": 64, "status": 0},
              {"label": "Changed text size", "value": 21, "status": 2},
              {"label": "Turned off screen shake", "value": 17,
               "status": 3},
              {"label": "Used the colour-blind lamp option", "value": 6,
               "status": 1},
          ]}]},
        {"heading": "Next playtest", "kind": "bullets", "weight": 1.2,
         "step": 0.2, "min_pages": 4, "items": [
             "Playtest 7 on build 0.9.4, 7 November, with 60 players, "
             "half of them on Switch dev kits at the publisher.",
             "Focus: the new foghorn rings, the radial crafting menu "
             "and islands 5 and 6.",
             "Success: 85 % finish island 3, under 10 % stuck on the "
             "foghorn.",
         ]},
    ],
}
