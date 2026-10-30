"""Product Roadmap of Pocket Bank App Relaunch: the project and everything the
document could say. The typesetting keeps what fits into two pages, the most
important first."""

PROJECT = {
    "name": "Pocket Bank App Relaunch",
    "code": "PB-5",
    "author": "Priya Raman, Head of Product, Pocket Bank",
}

DOCUMENT = {
    "title": "Product Roadmap",
    "subtitle": "From a banking app people tolerate to one they open "
                "because they want to · Q3 2026 to Q2 2027",
    "meta": [("Product", "Pocket Bank iOS + Android"),
             ("Owner", "Priya Raman"), ("Horizon", "4 quarters"),
             ("Updated", "1 Jul 2026")],
    "sections": [
        {"heading": "North star", "kind": "callout", "weight": 0.1,
         "tone": "accent", "label": "Weekly active customers",
         "text": "from **41 %** to **65 %** of account holders by June "
                 "2027, with an App Store rating of 4.6 or better."},
        {"heading": "Now, next, later", "kind": "figure", "weight": 0.2,
         "charts": [{"type": "board", "size": 7.2, "columns": [
             {"title": "Now · Q3", "tone": 0, "cards": [
                 ("New home screen: balance, spend and bills at a glance",
                  "outcome: +10 pts weekly active"),
                 ("Face and fingerprint login everywhere",
                  "outcome: login time under 2 s"),
                 ("Instant card freeze and replace",
                  "outcome: −30 % support calls on cards"),
             ]},
             {"title": "Next · Q4 – Q1", "tone": 1, "cards": [
                 ("Spaces: pots for saving with round-ups",
                  "bet: saving drives retention"),
                 ("Bill calendar with reminders", "bet: fewer overdraft "
                                                  "fees"),
                 ("In-app chat with a human", "bet: NPS +8"),
             ]},
             {"title": "Later · Q2 2027", "tone": 3, "cards": [
                 ("Shared spaces for couples and flatmates",
                  "to explore"),
                 ("Spending insights by category", "to explore"),
                 ("Open banking: see other accounts", "needs licence"),
             ]},
         ]}]},
        {"heading": "Release train", "kind": "figure", "weight": 0.4,
         "height": {1: 150, 2: 175, 4: 190}, "charts": [{"type": "gantt",
          "columns": ["Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan",
                      "Feb", "Mar", "Apr", "May", "Jun"],
          "groups": ["Core", "Money", "Help"], "today": 0.1,
          "tasks": [
              {"label": "5.0 New home + login", "start": 0, "end": 2.6,
               "text": "release 5.0"},
              {"label": "5.1 Card controls", "start": 2, "end": 3.6},
              {"label": "5.2 Spaces and round-ups", "start": 3.4,
               "end": 6.2, "group": 1},
              {"label": "5.3 Bill calendar", "start": 5.5, "end": 7.8,
               "group": 1},
              {"label": "5.4 Human chat", "start": 6, "end": 8.6,
               "group": 2},
              {"label": "6.0 Shared spaces", "start": 8.5, "end": 11.5,
               "group": 1, "progress": 0, "text": "to be confirmed"},
              {"label": "App Store feature pitch", "start": 2.6,
               "milestone": True, "text": "5.0 live"},
          ]}]},
        {"heading": "Outcomes by quarter", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": {2: 160, 4: 185}, "widths": [3, 2],
         "charts": [
             {"type": "line", "title": "Weekly active customers",
              "subtitle": "% of account holders", "format": "{:.0f}%",
              "x": ["Q1 26", "Q2", "Q3", "Q4", "Q1 27", "Q2"],
              "target": 65, "target_label": "north star",
              "series": [
                  {"name": "Actual", "values": [39, 41, None, None, None,
                                                None]},
                  {"name": "Plan", "dash": True, "color": 1,
                   "values": [None, 41, 48, 54, 60, 65]}]},
             {"type": "bars", "title": "App Store rating",
              "categories": ["Q1", "Q2", "Q3", "Q4", "Q1", "Q2"],
              "format": "{:.1f}", "target": 4.6, "target_label": "goal",
              "series": [{"name": "Rating",
                          "values": [3.4, 3.6, 4.0, 4.3, 4.5, 4.6],
                          "colors": [4, 4, 0, 0, 0, 0]}]},
         ]},
        {"heading": "Themes", "kind": "entries", "weight": 0.7,
         "step": 0.25, "inner": 0.1, "min_pages": 2, "entries": [
             {"title": "Effortless everyday banking", "dates": "40 % of "
              "capacity", "text": [
                  "Most sessions last 20 seconds: check the balance, see "
                  "what came out, leave. We make those 20 seconds "
                  "perfect before we add anything new."]},
             {"title": "Money that grows", "dates": "35 %", "text": [
                 "Customers who save with us stay three times longer. "
                 "Spaces and round-ups turn saving into a habit, not a "
                 "decision."]},
             {"title": "Help when it matters", "dates": "15 %", "text": [
                 "A frozen card at midnight abroad should be solved in "
                 "the app in one minute, or by a person in five."]},
             {"title": "Keeping the lights on", "dates": "10 %", "text": [
                 "Security patches, OS updates and regulatory change."]},
         ]},
        {"heading": "Capacity", "kind": "figure", "weight": 0.9,
         "min_pages": 4, "height": 150, "widths": [2, 3], "charts": [
             {"type": "donut", "title": "Squad time by theme",
              "segments": [("Everyday banking", 40), ("Money", 35),
                           ("Help", 15), ("Lights on", 10)],
              "format": "{:.0f}%", "center": ("6", "squads")},
             {"type": "bars", "title": "Engineers per squad",
              "stacked": True, "inside": True,
              "categories": ["Home", "Login", "Cards", "Spaces", "Bills",
                             "Chat"],
              "series": [{"name": "iOS", "values": [2, 1, 2, 2, 1, 1]},
                         {"name": "Android",
                          "values": [2, 1, 2, 2, 1, 1]},
                         {"name": "Backend",
                          "values": [2, 2, 3, 3, 2, 3]},
                         {"name": "Design", "color": 4,
                          "values": [1, 1, 1, 1, 1, 1]}]},
         ]},
        {"heading": "What customers tell us", "kind": "figure",
         "weight": 0.95, "min_pages": 4, "height": 160, "widths": [3, 2],
         "charts": [
             {"type": "bars", "horizontal": True, "title": "Top requests",
              "subtitle": "% of 2,400 survey answers", "format": "{:.0f}%",
              "categories": ["See spending at a glance", "Faster login",
                             "Save automatically", "Talk to a person",
                             "Know what bills are coming",
                             "Split bills with friends"],
              "series": [{"name": "Asked for",
                          "values": [46, 39, 31, 28, 24, 12]}]},
             {"type": "funnel", "title": "Why customers leave",
              "stages": [("Tried the app", 1000), ("Used it monthly",
                                                   720),
                         ("Used it weekly", 410),
                         ("Saved with us", 140)]},
         ]},
        {"heading": "Risks to the roadmap", "kind": "table",
         "weight": 0.97, "step": 0.15, "min_pages": 4,
         "badges": {"High": "bad", "Medium": "warn", "Low": "good"},
         "columns": [("Risk", 3.4), ("Level", 0.9, "center"),
                     ("What we do", 3)],
         "rows": [
             ["Savings approval slips past October", "High",
              "Product joins the savings committee; Spaces ships "
              "without interest first"],
             ["Chat vendor contract not signed", "High",
              "Second vendor shortlisted; escalate to the COO"],
             ["Android performance on old phones", "Medium",
              "Performance budget in the definition of done"],
             ["Key iOS engineers leave", "Low",
              "Pairing and rotation between squads"],
         ]},
        {"heading": "Dependencies", "kind": "table", "weight": 1.0,
         "step": 0.2, "min_pages": 4, "badges": {"On track": "good",
                                                "At risk": "warn",
                                                "Blocked": "bad"},
         "columns": [("Needs", 2.4), ("From", 1.6), ("For", 1.6),
                     ("By", 0.8), ("Status", 1, "center")],
         "rows": [
             ["Real-time card events API", "Card platform", "5.1 Card "
              "controls", "Aug", "On track"],
             ["Savings product approved", "Risk and compliance",
              "5.2 Spaces", "Oct", "At risk"],
             ["Bill data from direct debits", "Payments", "5.3 Bills",
              "Nov", "On track"],
             ["Chat vendor contract", "Procurement", "5.4 Chat", "Sep",
              "Blocked"],
             ["Open banking licence", "Legal", "Later", "Mar",
              "At risk"],
         ]},
        {"heading": "What we said no to", "kind": "bullets",
         "weight": 1.2, "step": 0.2, "min_pages": 4, "items": [
             "**Crypto trading.** Asked for by 3 % of customers, risky for "
             "all of them, and not our licence.",
             "**A redesigned web banking site.** Web is 6 % of sessions; "
             "it gets the new design system in 2027, not a rebuild.",
             "**Themes and dark mode customisation** beyond the system "
             "setting: nice, but no one leaves a bank over it.",
             "**Cashback offers.** Tried in 2024; usage was high, "
             "retention flat.",
         ]},
        {"heading": "How we decide", "kind": "text", "weight": 1.4,
         "step": 0.3, "min_pages": 4, "paragraphs": [
             "Every item on this roadmap is a bet on an outcome, not a "
             "promise of a feature. Squads own the outcome and choose "
             "the features; the roadmap is reviewed every quarter with "
             "the data from the last one.",
             "Items move from *later* to *next* only when we have seen "
             "the problem in research, sized the opportunity and found a "
             "squad with room.",
         ]},
        {"heading": "Where we bet", "kind": "figure", "weight": 1.1,
         "min_pages": 4, "height": 170, "charts": [{"type": "quadrant",
          "x": "effort", "y": "value to customers",
          "quadrants": ["Quick wins", "Big bets", "Fill-ins",
                        "Money pits"],
          "groups": ["Now", "Next", "Later"],
          "points": [("New home screen", 4, 9, 0),
                     ("Biometric login", 2, 7, 0),
                     ("Card freeze", 2, 8, 0),
                     ("Spaces", 6, 8.5, 1), ("Bill calendar", 5, 6.5, 1),
                     ("Human chat", 7, 7, 1),
                     ("Shared spaces", 8, 6, 2),
                     ("Insights", 6, 4.5, 2), ("Open banking", 9, 5, 2),
                     ("Crypto", 8.5, 1.5, 4)]}]},
    ],
}
