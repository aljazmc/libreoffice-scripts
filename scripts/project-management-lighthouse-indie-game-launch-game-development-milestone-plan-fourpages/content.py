"""Milestone Plan of Keeper of the Last Light: the project and everything the
document could say. The typesetting keeps what fits into four pages, the
most important first."""

PROJECT = {
    "name": "Keeper of the Last Light",
    "code": "KLL",
    "author": "Mira Okonkwo, Producer, Tidepool Games",
}

DOCUMENT = {
    "title": "Milestone Plan",
    "subtitle": "A cosy lighthouse game for PC and Switch, from vertical "
                "slice to launch day",
    "meta": [("Studio", "Tidepool Games"), ("Team", "7 people"),
             ("Budget", "€640k"), ("Launch", "12 Mar 2027"),
             ("Producer", "Mira Okonkwo")],
    "sections": [
        {"heading": "Road to launch", "kind": "figure", "weight": 0.1,
         "height": {1: 125, 2: 135, 4: 140}, "charts": [{
             "type": "timeline", "start": 0, "end": 18,
             "label_width": 95,
             "phases": [(0, 4, "Pre-prod"), (4, 13, "Production"),
                        (13, 18, "Polish + launch")],
             "ticks": [(0, "Oct 25"), (6, "Apr 26"), (12, "Oct 26"),
                       (17.4, "Mar 27")],
             "events": [
                 {"at": 1, "label": "Vertical slice", "sub": "Nov 25",
                  "status": "done"},
                 {"at": 4, "label": "Publisher deal", "sub": "Feb 26",
                  "status": "done"},
                 {"at": 8, "label": "Alpha", "sub": "Jun 26",
                  "status": "done"},
                 {"at": 12, "label": "Beta", "sub": "Oct 26",
                  "status": "now"},
                 {"at": 15, "label": "Gold master", "sub": "Jan 27"},
                 {"at": 17.4, "label": "Launch", "sub": "12 Mar 27"},
             ]}]},
        {"heading": "Milestones", "kind": "table", "weight": 0.2,
         "step": 0.1, "badges": {"Done": "good", "Now": "warn",
                                 "Next": "neutral"},
         "columns": [("Milestone", 1.4), ("Exit criteria", 4),
                     ("Date", 1), ("", 0.8, "center")],
         "rows": [
             ["Alpha", "All 6 islands playable start to finish; every "
              "system in, even if ugly", "30 Jun 26", "Done"],
             ["Beta", "Content complete; no blocker bugs; Switch build "
              "runs at 30 fps on the busiest island", "30 Oct 26",
              "Now"],
             ["Gold", "Zero A bugs, under 20 B bugs; certification "
              "passed on Switch; store pages approved", "15 Jan 27",
              "Next"],
             ["Launch", "Day-one patch ready; press keys sent; "
              "community team on shift", "12 Mar 27", "Next"],
         ]},
        {"heading": "Features", "kind": "figure", "weight": 0.3,
         "height": {1: 150, 2: 160, 4: 170}, "charts": [{
             "type": "heatmap", "title": "Feature status by milestone",
             "rows": ["Lighthouse keeping", "Boats and rescue",
                      "Islands (6)", "Weather system", "Crafting",
                      "Village and letters", "Photo mode", "Switch port"],
             "cols": ["Slice", "Alpha", "Beta", "Gold"],
             "values": [["Done", "Done", "Done", "Done"],
                        ["Rough", "Done", "Done", "Done"],
                        ["1", "6", "6", "6"],
                        ["Rough", "Rough", "Done", "Done"],
                        ["", "Rough", "Done", "Done"],
                        ["", "Rough", "Late", "Done"],
                        ["", "", "Rough", "Done"],
                        ["", "Rough", "Late", "Done"]],
             "badges": {"Done": "good", "Rough": "warn", "Late": "bad",
                        "1": "warn", "6": "good"},
             "labels": 0.3}]},
        {"heading": "Team", "kind": "figure", "weight": 0.4,
         "min_pages": 2, "height": 155, "widths": [3, 2], "charts": [
             {"type": "bars", "title": "People per month", "stacked": True,
              "categories": ["Oct", "Dec", "Feb", "Apr", "Jun", "Aug",
                             "Oct", "Dec", "Feb"],
              "series": [{"name": "Code", "values": [2, 2, 2, 3, 3, 3, 3,
                                                     3, 2]},
                         {"name": "Art", "values": [1, 2, 2, 2, 2, 2, 2,
                                                    1, 1]},
                         {"name": "Design and audio", "values": [1, 1,
                                                                 1, 1, 1,
                                                                 2, 2, 1,
                                                                 1]},
                         {"name": "QA and community", "color": 3,
                          "values": [0, 0, 0, 0, 0, 0, 1, 2, 3]}]},
             {"type": "donut", "title": "Budget", "format": "€{:,.0f}k",
              "center": ("€640k", "total"),
              "segments": [("Salaries", 452), ("Contractors", 68),
                           ("Audio and music", 34), ("Porting and QA",
                                                     41),
                           ("Marketing", 45)]},
         ]},
        {"heading": "Runway", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": 150, "charts": [{"type": "line",
          "title": "Cash in the bank", "subtitle": "€k",
          "x": ["Oct 25", "Jan 26", "Apr", "Jul", "Oct", "Jan 27",
                "Apr", "Jul"],
          "format": "{:,.0f}", "target": 60, "target_label": "minimum",
          "series": [{"name": "Plan", "area": True,
                      "values": [180, 410, 330, 250, 220, 140, 300,
                                 420]},
                     {"name": "Without launch revenue", "dash": True,
                      "color": 1, "values": [180, 410, 330, 250, 220,
                                             140, 70, 0]}],
          "marks": [(3.9, "publisher milestone"), (5.5, "launch")]}]},
        {"heading": "Risks", "kind": "table", "weight": 0.6, "step": 0.1,
         "min_pages": 2, "badges": {"High": "bad", "Medium": "warn",
                                    "Low": "good"},
         "columns": [("Risk", 3.4), ("Level", 0.9, "center"),
                     ("Plan", 3)],
         "rows": [
             ["Switch performance on the storm island", "High",
              "Porting contractor from November; cut particles if "
              "needed"],
             ["Letters system late", "Medium", "Writer full-time until "
              "December"],
             ["Launch clashes with a big release", "Medium",
              "Date confirmed only in December"],
             ["Burnout before gold", "Medium", "No weekend crunch; "
              "scope cut list ready"],
         ]},
        {"heading": "Scope cut list", "kind": "bullets", "weight": 0.8,
         "step": 0.15, "min_pages": 4, "items": [
             "Fishing mini-game (two weeks of work) moves to a free "
             "update.",
             "Second photo mode filter set.",
             "The seventh island, the lightship, becomes DLC.",
             "Full voice acting for the village: keep the barks, cut "
             "the lines.",
         ]},
        {"heading": "Production rhythm", "kind": "figure", "weight": 0.9,
         "min_pages": 4, "charts": [{"type": "chevrons", "steps": [
             {"label": "Plan", "status": "done",
              "sub": "Two-week sprints, planned on Monday"},
             {"label": "Build", "status": "done",
              "sub": "Nightly builds on both platforms"},
             {"label": "Play", "status": "now",
              "sub": "Friday team playtest, an hour"},
             {"label": "Review", "sub": "Milestone review with the "
                                       "publisher"},
             {"label": "Ship", "sub": "Steam playtest builds monthly"},
         ]}]},
        {"heading": "Publisher deal", "kind": "tags", "weight": 1.0,
         "step": 0.1, "min_pages": 4, "items": [
             ("Advance", "€380k in five milestone payments"),
             ("Revenue share", "70 / 30 for the studio after recoup"),
             ("Publisher does", "Switch certification, PR, store "
                                "featuring"),
             ("We keep", "the IP and the PC community"),
         ]},
        {"heading": "Burn by milestone", "kind": "figure", "weight": 1.1,
         "min_pages": 4, "height": 140, "charts": [{"type": "bars",
          "title": "Spend", "subtitle": "€k", "format": "{:,.0f}",
          "categories": ["Slice", "Pre-prod", "Alpha", "Beta", "Gold",
                         "Launch"],
          "series": [{"name": "Budget", "color": 4,
                      "values": [60, 90, 190, 150, 100, 50]},
                     {"name": "Actual", "values": [64, 88, 204, 132,
                                                   None, None]}]}]},
        {"heading": "Definition of done", "kind": "text", "weight": 1.2,
         "step": 0.3, "min_pages": 4, "paragraphs": [
             "A feature is done when it works on both platforms, has "
             "its sounds, its localisation strings and its accessibility "
             "options, and has survived a Friday playtest without a "
             "single person asking what to do next.",
         ]},
        {"heading": "Velocity", "kind": "figure", "weight": 1.25,
         "min_pages": 4, "height": 140, "charts": [{"type": "line",
          "title": "Tasks closed per sprint", "x": ["S1", "S4", "S8",
                                                    "S12", "S16", "S20",
                                                    "S24", "S28"],
          "format": "{:.0f}",
          "series": [{"name": "Closed", "area": True,
                      "values": [18, 26, 31, 34, 29, 36, 41, 38]},
                     {"name": "Bugs found", "color": "bad", "dash": True,
                      "values": [2, 4, 9, 12, 18, 22, 31, 27]}]}]},
        {"heading": "Platforms", "kind": "tags", "weight": 1.3,
         "step": 0.1, "min_pages": 4, "items": [
             ("PC", "Steam, GOG and itch.io; Steam Deck verified"),
             ("Switch", "with the publisher, physical edition later"),
             ("Languages", "English, French, German, Spanish, Italian, "
                           "Portuguese, Japanese, Korean, Chinese"),
             ("Price", "€19.99, 10 % launch discount"),
         ]},
    ],
}
