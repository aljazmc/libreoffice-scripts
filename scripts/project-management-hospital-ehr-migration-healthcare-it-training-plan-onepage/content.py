"""Training Plan of St Brigid's EHR Migration: the project and everything the
document could say. The typesetting keeps what fits into one page, the most
important first."""

PROJECT = {
    "name": "St Brigid's EHR Migration",
    "code": "EHR-26",
    "author": "Grace Doyle, Training Lead",
}

WEEKS = ["31 Aug", "7 Sep", "14 Sep", "21 Sep", "28 Sep", "5 Oct",
         "12 Oct", "19 Oct", "26 Oct", "2 Nov"]

DOCUMENT = {
    "title": "Training Plan",
    "subtitle": "Training 4,300 staff to use Meridian EHR safely before "
                "go-live on 7 November 2026",
    "meta": [("Programme", "EHR-26"), ("Training lead", "Grace Doyle"),
             ("Learners", "4,300"), ("Courses", "14"),
             ("Window", "10 weeks")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "charts": [{"type": "kpis",
         "tiles": [
             {"label": "Learners", "value": "4,300", "status": 0,
              "note": "clinical and admin staff"},
             {"label": "Classroom hours", "value": "21,600",
              "status": 0, "note": "plus e-learning"},
             {"label": "Super users", "value": "280", "status": "good",
              "note": "1 per 15 staff"},
             {"label": "Pass mark", "value": "80 %", "status": "warn",
              "note": "proficiency check"},
         ]}]},
        {"heading": "Staff trained per week", "kind": "figure",
         "weight": 0.2, "height": {1: 175, 2: 185, 4: 200},
         "widths": [3, 2], "charts": [
             {"type": "bars", "title": "Learners completing training",
              "stacked": True, "values": False, "categories": WEEKS,
              "series": [
                  {"name": "Doctors", "values": [40, 80, 110, 120, 130,
                                                 130, 110, 80, 40, 20]},
                  {"name": "Nurses and midwives",
                   "values": [120, 210, 260, 280, 300, 300, 260, 180,
                              90, 40]},
                  {"name": "Allied health", "values": [30, 50, 60, 70, 70,
                                                       70, 60, 40, 20,
                                                       10]},
                  {"name": "Admin", "color": 4,
                   "values": [60, 90, 100, 100, 100, 90, 70, 50, 30,
                              10]}]},
             {"type": "line", "title": "Cumulative", "subtitle": "% of "
              "4,300", "x": ["31/8", "", "", "", "", "", "", "", "",
                             "2/11"],
              "format": "{:.0f}", "target": 90, "target_label": "go-live "
              "target", "markers": False,
              "series": [
                  {"name": "Plan", "dash": True, "color": 4,
                   "values": [6, 16, 28, 41, 55, 68, 80, 89, 94, 96]},
                  {"name": "Actual", "values": [6, 15, 27, 40, 53, 66,
                                                None, None, None,
                                                None]}]},
         ]},
        {"heading": "Courses by role", "kind": "table", "weight": 0.3,
         "step": 0.1, "columns": [("Role", 2), ("Courses", 3.4),
                                  ("Hours", 0.8, "center"),
                                  ("Learners", 1, "end")],
         "rows": [
             ["Consultants and registrars", "Physician core, orders and "
              "results, e-prescribing, notes", "8", "620"],
             ["Junior doctors", "Physician core, e-prescribing, "
              "discharge", "7", "410"],
             ["Ward nurses", "Nursing core, medication administration, "
              "observations", "6", "1,540"],
             ["Midwives", "Maternity, fetal monitoring", "8", "260"],
             ["Theatre staff", "Perioperative, anaesthesia record", "7",
              "340"],
             ["Allied health", "Allied health core, referrals", "4",
              "480"],
             ["Ward clerks and admin", "Registration, scheduling, "
              "back-entry", "5", "650"],
         ]},
        {"heading": "How people learn", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "charts": [{"type": "chevrons", "steps": [
             {"label": "E-learning", "status": "done",
              "sub": "45 minutes, before the class, the basics of "
                     "logging in and finding a patient."},
             {"label": "Classroom", "status": "now",
              "sub": "4 to 8 hours by role, in the training rooms, on "
                     "the training system."},
             {"label": "Proficiency", "sub": "A 20-minute check with "
                                            "realistic scenarios; 80 % "
                                            "to pass."},
             {"label": "Practice", "sub": "Playground system open 24/7 "
                                         "until go-live."},
             {"label": "At the elbow", "sub": "Super users on every "
                                             "ward, for two weeks."},
         ]}]},
        {"heading": "Proficiency results", "kind": "figure",
         "weight": 0.6, "min_pages": 2, "height": 150, "widths": [3, 2],
         "charts": [
             {"type": "bars", "horizontal": True, "title": "First-time "
              "pass rate", "format": "{:.0f}%", "target": 85,
              "target_label": "aim",
              "categories": ["Doctors", "Nurses", "Midwives", "Theatres",
                             "Allied health", "Admin"],
              "series": [{"name": "Pass", "values": [88, 91, 79, 74, 93,
                                                     95],
                          "colors": ["good", "good", "warn", "bad",
                                     "good", "good"]}]},
             {"type": "donut", "title": "Attempts to pass",
              "segments": [("First", 2380, "good"), ("Second", 290,
                                                     "warn"),
                           ("Third", 44, "bad")],
              "center": ("2,714", "passed"), "format": "{:,.0f}"},
         ]},
        {"heading": "Super users", "kind": "text", "weight": 0.7,
         "step": 0.3, "min_pages": 2, "paragraphs": [
             "Every ward has at least two super users on every shift for "
             "the first two weeks: nurses, doctors and clerks who had "
             "three extra days of training and helped test the build. "
             "They wear orange lanyards, solve 80 % of questions at the "
             "elbow and escalate the rest to the command centre.",
         ]},
        {"heading": "Rooms and capacity", "kind": "figure", "weight": 0.9,
         "min_pages": 4, "height": 150, "charts": [{"type": "heatmap",
          "rows": ["Room A (24 seats)", "Room B (24)", "Room C (16)",
                   "Library (12)", "Maternity unit (10)",
                   "Mobile cart (8)"],
          "cols": WEEKS,
          "values": [[60, 80, 95, 100, 100, 100, 95, 80, 60, 40],
                     [50, 75, 90, 100, 100, 100, 90, 75, 50, 30],
                     [40, 60, 80, 90, 95, 95, 85, 70, 40, 20],
                     [30, 50, 70, 80, 80, 80, 70, 60, 40, 20],
                     [0, 40, 60, 80, 90, 90, 90, 70, 50, 30],
                     [0, 0, 50, 60, 80, 90, 100, 100, 80, 60]],
          "format": "{:.0f}%", "labels": 0.22}]},
        {"heading": "Night and weekend staff", "kind": "bullets",
         "weight": 1.0, "step": 0.2, "min_pages": 4, "items": [
             "Classes at 07:00 and 20:00 on weekdays, and on two "
             "Saturdays, so night staff can attend in paid time.",
             "The mobile training cart visits ICU, ED and maternity "
             "during quiet hours.",
             "Agency and bank staff get a 90-minute essentials course "
             "and cannot work on a live ward without it.",
         ]},
        {"heading": "Risks", "kind": "table", "weight": 1.1, "step": 0.2,
         "min_pages": 4, "badges": {"High": "bad", "Medium": "warn",
                                    "Low": "good"},
         "columns": [("Risk", 3.4), ("Level", 0.9, "center"),
                     ("Response", 3.2)],
         "rows": [
             ["Theatre staff cannot be released from lists",
              "High", "Two lists a week cancelled for training in "
              "October"],
             ["Training system differs from the final build",
              "Medium", "Refreshed weekly from the build; changes "
              "listed in each class"],
             ["Staff forget before go-live", "Medium",
              "Playground system and ten-minute refreshers in week −1"],
             ["Trainers off sick", "Low", "Six super users certified "
              "as backup trainers"],
         ]},
        {"heading": "Budget", "kind": "figure", "weight": 1.2,
         "min_pages": 4, "height": 120, "charts": [{"type": "donut",
          "format": "€{:,.0f}k", "center": ("€1.42m", "total"),
          "segments": [("Backfill for staff in training", 860),
                       ("Trainers", 310), ("Super user time", 160),
                       ("Rooms and equipment", 60),
                       ("E-learning", 30)]}]},
        {"heading": "What learners say", "kind": "figure", "weight": 1.05,
         "min_pages": 4, "height": 150, "widths": [3, 2], "charts": [
             {"type": "bars", "horizontal": True, "title": "Agree or "
              "strongly agree", "format": "{:.0f}%",
              "categories": ["Trainer knew the system", "Pace was right",
                             "Scenarios felt real", "I could practise "
                             "enough", "I feel ready"],
              "series": [{"name": "Agree", "values": [94, 78, 85, 61,
                                                      72],
                          "colors": [0, 0, 0, "warn", "warn"]}]},
             {"type": "donut", "title": "Course rating",
              "segments": [("Excellent", 41, "good"), ("Good", 44, 0),
                           ("Fair", 12, "warn"), ("Poor", 3, "bad")],
              "format": "{:.0f}%", "center": ("4.2", "of 5")},
         ]},
        {"heading": "Milestones", "kind": "figure", "weight": 1.08,
         "min_pages": 4, "height": 120, "charts": [{"type": "timeline",
          "start": 0, "end": 10, "label_width": 105,
          "ticks": [(i, w) for i, w in enumerate(WEEKS)],
          "events": [
              {"at": 0, "label": "Super users certified", "sub": "31 Aug",
               "status": "done"},
              {"at": 2, "label": "All classes open for booking",
               "sub": "14 Sep", "status": "done"},
              {"at": 5, "label": "50 % trained", "sub": "5 Oct",
               "status": "now"},
              {"at": 7.5, "label": "90 % trained", "sub": "23 Oct"},
              {"at": 9.5, "label": "Go-live", "sub": "7 Nov"},
          ]}]},
        {"heading": "Course catalogue", "kind": "table", "weight": 1.15,
         "step": 0.05, "min_pages": 4,
         "columns": [("Course", 2.8), ("Length", 0.9, "center"),
                     ("Format", 1.2), ("For", 2.2)],
         "rows": [
             ["Meridian essentials", "45 min", "E-learning", "Everyone"],
             ["Physician core", "4 h", "Classroom", "All doctors"],
             ["E-prescribing", "2 h", "Classroom", "Prescribers"],
             ["Nursing core", "3 h", "Classroom", "Nurses, HCAs"],
             ["Medication administration", "2 h", "Classroom",
              "Nurses, midwives"],
             ["Maternity", "4 h", "Classroom", "Midwives, obstetricians"],
             ["Perioperative", "4 h", "Classroom", "Theatre staff"],
             ["Registration and scheduling", "3 h", "Classroom",
              "Clerks, receptionists"],
             ["Super user", "3 days", "Workshop", "280 super users"],
         ]},
    ],
}
