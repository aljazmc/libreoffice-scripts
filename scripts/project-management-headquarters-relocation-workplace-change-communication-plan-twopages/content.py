"""Communication Plan of Wharf Street HQ Move: the project and everything the
document could say. The typesetting keeps what fits into two pages, the most
important first."""

PROJECT = {
    "name": "Wharf Street HQ Move",
    "code": "WS-HQ",
    "author": "Nadia Benali, Change Lead",
}

MONTHS = ["Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov",
          "Dec"]

DOCUMENT = {
    "title": "Communication Plan",
    "subtitle": "Who hears what, when and how, from the announcement to "
                "the first months at Wharf Street · 2027",
    "meta": [("Project", "WS-HQ"), ("Audiences", "8"),
             ("Channels", "9"), ("Touchpoints", "64"),
             ("Owner", "Nadia Benali")],
    "sections": [
        {"heading": "Calendar", "kind": "figure", "weight": 0.1,
         "height": {1: 200, 2: 210, 4: 220}, "charts": [{
             "type": "heatmap", "rows": ["All staff", "Managers",
                                         "Change champions",
                                         "Labs team", "New starters",
                                         "Clients", "Neighbours",
                                         "Press"],
             "cols": MONTHS,
             "values": [["Town hall", "Email", "Tours", "Email", "Guide",
                         "Desk app", "Wave", "Wave", "Pulse", "Pulse"],
                        ["Briefing", "Pack", "Briefing", "Pack",
                         "Briefing", "Briefing", "Daily", "Daily",
                         "Review", ""],
                        ["", "Kick-off", "Monthly", "Monthly", "Monthly",
                         "Weekly", "Daily", "Daily", "Monthly", ""],
                        ["Meeting", "", "Meeting", "", "Meeting",
                         "Visit", "", "Meeting", "Wave", "Pulse"],
                        ["", "", "", "", "", "Guide", "Guide", "Guide",
                         "Guide", "Guide"],
                        ["", "", "", "Letter", "", "", "Email", "", "",
                         "Invite"],
                        ["", "", "Letter", "", "", "Letter", "Letter",
                         "Letter", "", ""],
                        ["Release", "", "", "", "", "", "", "", "Story",
                         ""]],
             "badges": {"Town hall": "accent", "Wave": "bad",
                        "Daily": "warn", "Weekly": "warn",
                        "Briefing": 1, "Pulse": "good"},
             "show": True, "size": 6.5, "labels": 0.16}]},
        {"heading": "Key messages", "kind": "entries", "weight": 0.2,
         "step": 0.2, "inner": 0.1, "entries": [
             {"title": "Why we are moving", "text": [
                 "One home instead of three, built for how we work now: "
                 "together on some days, focused on others."]},
             {"title": "What it means for you", "text": [
                 "Your team zone, your locker, a desk you book; more "
                 "rooms to meet and places to think."]},
             {"title": "What we need from you", "text": [
                 "Clear 60 % of your paper, pack your crate, try the "
                 "booking app, and tell us what is not working."]},
         ]},
        {"heading": "Audiences", "kind": "table", "weight": 0.3,
         "step": 0.1,
         "columns": [("Audience", 1.6), ("Size", 0.7, "end"),
                     ("Needs to know", 2.8), ("Channel", 2)],
         "rows": [
             ["All staff", "1,240", "Dates, desks, how things work",
              "Town halls, email, intranet"],
             ["Managers", "140", "How to lead their team through it",
              "Briefings, manager pack"],
             ["Change champions", "43", "Everything, a week early",
              "Weekly call, chat channel"],
             ["Labs team", "40", "Instruments, commute, shuttle",
              "Monthly meeting with the director"],
             ["Clients", "220", "New address, visitor parking",
              "Account managers, letter"],
             ["Neighbours", "300 homes", "Move dates and lorries",
              "Letters, a number to call"],
         ]},
        {"heading": "Channels", "kind": "figure", "weight": 0.4,
         "min_pages": 2, "height": 155, "widths": [3, 2], "charts": [
             {"type": "bars", "horizontal": True, "title": "How people "
              "prefer to hear", "subtitle": "% of survey answers",
              "format": "{:.0f}%",
              "categories": ["Their manager", "Email", "Town hall",
                             "Intranet", "Chat channel", "Posters"],
              "series": [{"name": "Prefer", "values": [64, 51, 38, 22,
                                                       19, 6]}]},
             {"type": "donut", "title": "Touchpoints planned",
              "segments": [("Email", 18), ("Meetings", 16),
                           ("Intranet", 12), ("Events", 8),
                           ("Print", 10)],
              "center": ("64", "touchpoints")},
         ]},
        {"heading": "Feedback", "kind": "bullets", "weight": 0.5,
         "step": 0.15, "min_pages": 2, "items": [
             "Questions to move@company, answered within two working "
             "days and added to the FAQ.",
             "A pulse survey of five questions every two months.",
             "Champions bring what they hear to the weekly call; the "
             "top three issues get an answer at the next town hall.",
         ]},
        {"heading": "Phases", "kind": "figure", "weight": 0.7,
         "min_pages": 4, "height": 120, "charts": [{"type": "timeline",
          "start": 0, "end": 10, "label_width": 100,
          "phases": [(0, 3, "Announce"), (3, 6, "Prepare"),
                     (6, 9, "Move"), (9, 10, "Settle")],
          "ticks": [(i, m) for i, m in enumerate(MONTHS)],
          "events": [
              {"at": 0.2, "label": "Announcement", "status": "done"},
              {"at": 2.2, "label": "Floor tours open", "status": "done"},
              {"at": 4.5, "label": "Desk booking pilot", "status": "now"},
              {"at": 6.5, "label": "Wave 1"},
              {"at": 8.5, "label": "Wave 4"},
              {"at": 9.5, "label": "Open house"},
          ]}]},
        {"heading": "Measures", "kind": "figure", "weight": 0.8,
         "min_pages": 4, "height": 140, "charts": [{"type": "progress",
          "format": "{:.0f} %", "items": [
              {"label": "Staff who know their move date", "value": 92,
               "target": 95, "status": "good"},
              {"label": "Opened the move guide", "value": 71,
               "target": 80, "status": "warn"},
              {"label": "Booked a floor tour", "value": 58, "target": 60,
               "status": "good"},
              {"label": "Feel well informed (pulse)", "value": 63,
               "target": 75, "status": "warn"},
          ]}]},
        {"heading": "FAQ", "kind": "entries", "weight": 0.9, "step": 0.2,
         "inner": 0.1, "min_pages": 4, "entries": [
             {"title": "Will I have my own desk?", "text": [
                 "Only if your role needs one (about 15 % of people). "
                 "Everyone has a team zone and a locker."]},
             {"title": "Can I park?", "text": [
                 "There are 120 spaces, for blue badge holders, car "
                 "sharers and people on call. Bike parking for 400."]},
             {"title": "What if the desks run out?", "text": [
                 "Each floor has touchdown desks and the café; if a "
                 "floor is full three days running, we change the "
                 "anchor days."]},
         ]},
        {"heading": "Tone", "kind": "motto", "weight": 1.0,
         "min_pages": 4, "text": "Tell people early, tell them twice, "
         "and tell them what we don't know yet."},
        {"heading": "Approvals", "kind": "tags", "weight": 1.1,
         "step": 0.1, "min_pages": 4, "items": [
             ("All-staff messages", "COO, two days before"),
             ("Client letters", "Commercial director"),
             ("Press", "Head of communications"),
             ("Neighbours", "Facilities, with the council"),
         ]},
        {"heading": "Message map", "kind": "figure", "weight": 1.15,
         "min_pages": 4, "charts": [{"type": "board", "columns": [
             {"title": "Why", "tone": 0, "cards": [
                 "One home instead of three",
                 "Built for working together and focusing",
                 "Cheaper to run and greener"]},
             {"title": "What", "tone": 1, "cards": [
                 "Team zones, booked desks, lockers",
                 "84 focus booths and 72 meeting rooms",
                 "A café and event space on the ground floor"]},
             {"title": "When", "tone": 3, "cards": [
                 "Four waves, September to October",
                 "Your wave date five weeks before",
                 "Your desk number five days before"]},
         ]}]},
        {"heading": "Responsibilities", "kind": "table", "weight": 1.2,
         "step": 0.1, "min_pages": 4,
         "columns": [("Who", 1.8), ("Does", 4)],
         "rows": [
             ["Change lead", "Owns the plan, writes all-staff messages, "
              "runs the pulse survey"],
             ["Internal comms", "Intranet, email, posters, the move "
              "guide"],
             ["Managers", "Team sessions, answers, first-day presence"],
             ["Champions", "Floor tours, feedback, peer help"],
             ["Facilities", "Neighbours, lorries, building signage"],
         ]},
        {"heading": "Reach so far", "kind": "figure", "weight": 1.25,
         "min_pages": 4, "height": 140, "charts": [{"type": "line",
          "title": "Staff reached by month", "subtitle": "% opened or "
          "attended at least one", "x": MONTHS[:6], "format": "{:.0f}",
          "series": [{"name": "Reached", "area": True,
                      "values": [88, 76, 81, 69, 74, 92]}]}]},
    ],
}
