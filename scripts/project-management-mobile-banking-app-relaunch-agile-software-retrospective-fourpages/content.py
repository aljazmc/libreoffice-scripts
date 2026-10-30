"""Retrospective of Pocket Bank App Relaunch: the project and everything the
document could say. The typesetting keeps what fits into four pages, the
most important first."""

PROJECT = {
    "name": "Pocket Bank App Relaunch",
    "code": "PB-5",
    "author": "Jonas Weber, Scrum Master, Home squad",
}

DOCUMENT = {
    "title": "Sprint 14 Retrospective",
    "subtitle": "Home squad · 29 August 2026 · 7 people, 60 minutes, "
                "format: start, stop, continue",
    "meta": [("Squad", "Home"), ("Facilitator", "Jonas Weber"),
             ("Mood", "3.9 / 5"), ("Actions", "2 new, 1 closed")],
    "sections": [
        {"heading": "The board", "kind": "figure", "weight": 0.1,
         "charts": [{"type": "board", "size": 7.2, "columns": [
             {"title": "Start", "tone": "good", "cards": [
                 ("Pairing with Compliance on copy before the sprint",
                  "5 votes"),
                 ("A shared test phone shelf, not personal phones",
                  "3 votes"),
                 ("Demo to the customer panel every second sprint",
                  "2 votes"),
             ]},
             {"title": "Stop", "tone": "bad", "cards": [
                 ("Pulling bugs in mid-sprint without the PO", "6 votes"),
                 ("Stand-ups that turn into design reviews", "4 votes"),
                 ("Merging on Friday afternoon", "2 votes"),
             ]},
             {"title": "Continue", "tone": "info", "cards": [
                 ("Splitting stories to protect the goal", "5 votes"),
                 ("Accessibility in the definition of done", "4 votes"),
                 ("Thursday bug bash with snacks", "3 votes"),
             ]},
         ]}]},
        {"heading": "Actions", "kind": "table", "weight": 0.2, "step": 0.1,
         "badges": {"New": "info", "Done": "good", "Open": "warn",
                    "Dropped": "neutral"},
         "columns": [("Action", 4), ("Owner", 1.2), ("Due", 1),
                     ("Status", 1, "center")],
         "rows": [
             ["Bugs found mid-sprint go to the PO first; only S1 bugs "
              "enter the sprint", "Mia", "S15 day 1", "New"],
             ["Design topics leave stand-up for a 15-minute huddle "
              "straight after", "Jonas", "S15 day 1", "New"],
             ["Compliance copy review moved to refinement (from S13)",
              "Mia", "S14", "Done"],
             ["Two shared test phones per platform (from S12)", "Leo",
              "S15", "Open"],
         ]},
        {"heading": "Mood", "kind": "figure", "weight": 0.3,
         "height": {1: 135, 2: 150, 4: 180}, "widths": [3, 2], "charts": [
             {"type": "line", "title": "Team mood over the sprints",
              "subtitle": "average of 1 to 5", "zero": False,
              "format": "{:.1f}",
              "x": ["S8", "S9", "S10", "S11", "S12", "S13", "S14"],
              "series": [{"name": "Mood", "area": True,
                          "values": [3.2, 3.0, 3.4, 3.6, 3.3, 3.7,
                                     3.9]}],
              "end_labels": True},
             {"type": "bars", "title": "This sprint",
              "subtitle": "votes", "values": True,
              "categories": ["1", "2", "3", "4", "5"],
              "series": [{"name": "Votes", "values": [0, 0, 2, 4, 1],
                          "colors": ["bad", "warn", 4, 0, "good"]}]},
         ]},
        {"heading": "Sprint timeline", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": 125, "charts": [{"type": "timeline",
          "start": 1, "end": 10, "label_width": 95,
          "ticks": [(1, "D1"), (3, "D3"), (5, "D5"), (7, "D7"),
                    (9, "D9"), (10, "D10")],
          "events": [
              {"at": 1, "label": "Planning went fast", "sub": "mood: high",
               "status": "done"},
              {"at": 4, "label": "Pending bug from beta", "sub": "low",
               "status": "now"},
              {"at": 5.5, "label": "Story split", "sub": "relief",
               "status": "done"},
              {"at": 7, "label": "Logos landed", "sub": "high",
               "status": "done"},
              {"at": 8.5, "label": "Perf target met", "sub": "high",
               "status": "done"},
              {"at": 10, "label": "Demo day", "sub": "proud",
               "status": "done"},
          ]}]},
        {"heading": "Themes", "kind": "entries", "weight": 0.6,
         "step": 0.25, "inner": 0.1, "min_pages": 2, "entries": [
             {"title": "Protecting the sprint", "dates": "11 votes",
              "text": [
                  "The pending payments bug was the right thing to fix, "
                  "but it entered the sprint through a direct message, "
                  "not through the product owner. Two people lost a "
                  "day to context switching."]},
             {"title": "Stand-up length", "dates": "4 votes", "text": [
                 "Stand-ups averaged 24 minutes this sprint. Most of the "
                 "overrun was the logo layout discussion, which deserved "
                 "its own meeting."]},
             {"title": "Working with Compliance", "dates": "5 votes",
              "text": [
                  "Last sprint's action worked: Compliance read the copy "
                  "in refinement, and nothing came back at the review."]},
         ]},
        {"heading": "Sprint in numbers", "kind": "figure", "weight": 0.85,
         "min_pages": 4, "charts": [{"type": "kpis", "tiles": [
             {"label": "Goal", "value": "Met", "status": "good",
              "note": "spending on home"},
             {"label": "Velocity", "value": "31", "delta": "+1",
              "status": 0, "note": "points",
              "spark": [22, 26, 29, 27, 30, 31]},
             {"label": "Stand-up", "value": "24 min", "status": "bad",
              "note": "target 15"},
             {"label": "Interruptions", "value": "6", "status": "warn",
              "note": "messages that became work"},
         ]}]},
        {"heading": "Health check", "kind": "figure", "weight": 0.88,
         "min_pages": 4, "height": 150, "charts": [{"type": "heatmap",
          "rows": ["Delivering value", "Speed", "Fun", "Learning",
                   "Mission", "Codebase health", "Support from others"],
          "cols": ["S10", "S11", "S12", "S13", "S14"],
          "values": [["Good", "Good", "Good", "Good", "Good"],
                     ["Some", "Good", "Some", "Good", "Good"],
                     ["Some", "Some", "Poor", "Some", "Good"],
                     ["Good", "Good", "Some", "Some", "Some"],
                     ["Good", "Good", "Good", "Good", "Good"],
                     ["Poor", "Some", "Some", "Some", "Good"],
                     ["Some", "Some", "Poor", "Some", "Good"]],
          "badges": {"Good": "good", "Some": "warn", "Poor": "bad"}}]},
        {"heading": "Previous actions", "kind": "entries", "weight": 0.95,
         "step": 0.2, "inner": 0.1, "min_pages": 4, "entries": [
             {"title": "Compliance reads copy in refinement",
              "dates": "S13 · done", "text": [
                  "Worked: zero copy changes at this review, against "
                  "five in sprint 12."]},
             {"title": "Shared test phones", "dates": "S12 · open",
              "text": [
                  "Two Android phones arrived; the iPhones are waiting "
                  "for a purchase order. Leo chases procurement."]},
             {"title": "No meetings on Wednesday mornings",
              "dates": "S11 · done", "text": [
                  "Kept for three sprints; the team wants to keep it."]},
         ]},
        {"heading": "Votes by theme", "kind": "figure", "weight": 0.9,
         "min_pages": 4, "height": 140, "charts": [{"type": "bars",
          "horizontal": True, "stacked": True,
          "categories": ["Sprint protection", "Compliance", "Stand-ups",
                         "Testing devices", "Bug bash", "Fridays"],
          "series": [{"name": "Start", "color": "good",
                      "values": [0, 5, 0, 3, 0, 0]},
                     {"name": "Stop", "color": "bad",
                      "values": [6, 0, 4, 0, 0, 2]},
                     {"name": "Continue", "color": "info",
                      "values": [5, 0, 0, 0, 3, 0]}]}]},
        {"heading": "Action follow-through", "kind": "figure",
         "weight": 1.0, "min_pages": 4, "height": 140, "widths": [3, 2],
         "charts": [
             {"type": "bars", "title": "Retro actions by sprint",
              "stacked": True,
              "categories": ["S9", "S10", "S11", "S12", "S13", "S14"],
              "series": [{"name": "Done", "color": "good",
                          "values": [2, 1, 3, 2, 2, 1]},
                         {"name": "Open", "color": "warn",
                          "values": [0, 0, 0, 1, 0, 1]},
                         {"name": "Dropped", "color": 4,
                          "values": [1, 1, 0, 0, 0, 0]}]},
             {"type": "donut", "title": "Since S9",
              "segments": [("Done", 11, "good"), ("Open", 2, "warn"),
                           ("Dropped", 2, 4)],
              "center": ("73 %", "done")},
         ]},
        {"heading": "Format", "kind": "text", "weight": 1.2, "step": 0.3,
         "min_pages": 4, "paragraphs": [
             "Five minutes of check-in with a mood vote, fifteen minutes "
             "of silent writing on the board, fifteen minutes to group "
             "and vote with three dots each, twenty minutes on the top "
             "three themes and five minutes to agree the actions.",
             "Next sprint's retro will use the *sailboat* format: wind, "
             "anchors, rocks and the island, suggested by Leo.",
         ]},
        {"heading": "Kudos", "kind": "bullets", "weight": 1.3, "step": 0.2,
         "min_pages": 4, "items": [
             "**Aisha** for the 800 ms home screen on a five-year-old "
             "phone.",
             "**Leo** for chasing every logo licence by hand.",
             "**Mia** for splitting the story without drama on day 6.",
         ]},
        {"kind": "motto", "weight": 1.4, "min_pages": 4,
         "text": "Regardless of what we discover, we understand and truly "
                 "believe that everyone did the best job they could."},
    ],
}
