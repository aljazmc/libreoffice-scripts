"""Risk Burndown Report of FROSTBYTE-1 CubeSat: the project and everything the
document could say. The typesetting keeps what fits into one page, the most
important first."""

PROJECT = {
    "name": "FROSTBYTE-1 CubeSat",
    "code": "FB1",
    "author": "Dr Kaisa Virtanen, Project Manager",
}

MILESTONES = ["SRR", "PDR", "+3 mo", "+6 mo", "CDR", "+3 mo", "TRR",
              "FAR", "Launch"]

DOCUMENT = {
    "title": "Risk Burndown Report",
    "subtitle": "Technical risk on the way to launch · status at the "
                "critical design review",
    "meta": [("Mission", "FROSTBYTE-1"), ("Document", "FB1-PA-009"),
             ("Open risks", "17"), ("Retired", "23"),
             ("Risk score", "142 · plan 120")],
    "sections": [
        {"heading": "Burndown", "kind": "figure", "weight": 0.1,
         "height": {1: 170, 2: 180, 4: 190}, "charts": [{"type": "line",
          "title": "Total risk score", "subtitle": "sum of likelihood × "
          "consequence of the open risks", "x": MILESTONES,
          "format": "{:.0f}", "end_labels": True,
          "marks": [(4, "today")],
          "series": [{"name": "Plan", "dash": True, "color": 2,
                      "values": [310, 260, 220, 170, 120, 90, 60, 40,
                                 25]},
                     {"name": "Actual", "color": 1, "area": True,
                      "values": [310, 278, 241, 196, 142, None, None,
                                 None, None]},
                     {"name": "Forecast", "dash": True, "color": 1,
                      "values": [None, None, None, None, 142, 104, 70, 44,
                                 28]}]}]},
        {"heading": "Where the risk is", "kind": "figure", "weight": 0.2,
         "height": {1: 185, 2: 195}, "charts": [{"type": "risk",
          "risks": [
              ("T1", 4, 5, "Altimeter range noise misses 5 cm"),
              ("T2", 3, 4, "Antenna deployment fails in orbit"),
              ("T3", 3, 3, "Energy margin under 15 % in science mode"),
              ("T4", 2, 4, "Reaction wheel supplier late"),
              ("T5", 3, 2, "Thermal vacuum test slot moves"),
              ("T6", 2, 3, "Flight software not ready for TRR"),
          ],
          "residual": [("T1", 2, 4), ("T2", 1, 4), ("T3", 1, 3)]}]},
        {"heading": "Top risks", "kind": "table", "weight": 0.3,
         "step": 0.1, "badges": {"20": "bad", "16": "bad", "12": "warn",
                                 "9": "warn", "8": "warn", "6": "good",
                                 "down": "good", "up": "bad",
                                 "flat": "neutral"},
         "columns": [("ID", 0.5), ("Risk", 3), ("Score", 0.7, "center"),
                     ("Trend", 0.7, "center"), ("Retirement plan", 3)],
         "rows": [
             ["T1", "Altimeter range noise misses 5 cm", "20", "up",
              "Oven-controlled oscillator on the flight model; test in "
              "March"],
             ["T2", "Antenna deployment fails in orbit", "12", "down",
              "Deploy 20 times in thermal vacuum; second burn wire"],
             ["T3", "Energy margin under 15 %", "9", "up",
              "Fourth solar panel; duty-cycle the radar"],
             ["T4", "Reaction wheel supplier late", "8", "flat",
              "Second supplier qualified"],
             ["T6", "Flight software late for TRR", "6", "down",
              "Two students full time from January"],
         ]},
        {"heading": "Retired and new", "kind": "figure", "weight": 0.4,
         "min_pages": 2, "height": 155, "widths": [3, 2], "charts": [
             {"type": "bars", "title": "Risks per review period",
              "categories": MILESTONES[:5],
              "series": [{"name": "Retired", "color": "good",
                          "values": [0, 4, 6, 7, 6]},
                         {"name": "New", "color": "bad",
                          "values": [24, 5, 4, 3, 4]}]},
             {"type": "donut", "title": "Open by area",
              "segments": [("Payload", 6), ("Power", 3), ("ADCS", 3),
                           ("Software", 2), ("AIT and schedule", 3)],
              "center": ("17", "open")},
         ]},
        {"heading": "How risks are retired", "kind": "figure",
         "weight": 0.5, "min_pages": 2, "charts": [{"type": "chevrons",
          "steps": [
              {"label": "Identify", "status": "done",
               "sub": "Anyone, at any time, in the risk log"},
              {"label": "Score", "status": "done",
               "sub": "Likelihood and consequence, 1 to 5"},
              {"label": "Plan", "status": "now",
               "sub": "A test or analysis that will retire it"},
              {"label": "Retire", "sub": "When the evidence brings it "
                                        "under 6"},
              {"label": "Close", "sub": "Approved by the review board"},
          ]}]},
        {"heading": "T1 in depth", "kind": "text", "weight": 0.6,
         "step": 0.3, "min_pages": 2, "paragraphs": [
             "The altimeter's range noise is the one risk that could "
             "cost the mission its science. The engineering model "
             "measured 7.2 cm against 5 cm required. The fix, an oven-"
             "controlled oscillator, adds 40 g and 0.8 W; both fit "
             "within the margins, the power only just.",
             "If the flight model test in March still fails, we average "
             "over 2 Hz instead of 1 Hz: the sea-ice product loses "
             "half its along-track resolution but still meets the "
             "mission requirement.",
         ]},
        {"heading": "Risk by subsystem over time", "kind": "figure",
         "weight": 0.8, "min_pages": 4, "height": 150, "charts": [{
             "type": "bars", "stacked": True, "title": "Score by area",
             "categories": MILESTONES[:5],
             "series": [{"name": "Payload", "color": 1,
                         "values": [110, 104, 96, 82, 66]},
                        {"name": "Platform", "color": 0,
                         "values": [96, 84, 70, 58, 40]},
                        {"name": "Software", "color": 3,
                         "values": [44, 40, 34, 28, 16]},
                        {"name": "AIT and schedule", "color": 4,
                         "values": [60, 50, 41, 28, 20]}]}]},
        {"heading": "Retired since PDR", "kind": "bullets",
         "weight": 0.9, "step": 0.2, "min_pages": 4, "items": [
             "Structure first frequency: retired by the modal survey of "
             "the qualification model.",
             "S-band licence: granted by the regulator in May.",
             "Star tracker blinding by the antenna: retired by analysis "
             "and a new mounting angle.",
             "Ground station availability: second station contracted.",
         ]},
        {"heading": "Scoring", "kind": "tags", "weight": 1.0, "step": 0.1,
         "min_pages": 4, "items": [
             ("Likelihood", "1 rare, under 1 % · 5 likely, over 50 %"),
             ("Consequence", "1 nuisance · 5 loss of the mission"),
             ("Score", "likelihood × consequence; 15 and over is red"),
             ("Burndown", "the sum of the scores of all open risks"),
         ]},
        {"heading": "Board decision", "kind": "callout", "weight": 1.1,
         "tone": "warn", "min_pages": 4, "label": "Accepted:",
         "text": "the project continues to CDR close-out with T1 open, on "
                 "condition that the oscillator test result is reported "
                 "to the board before the flight model is integrated."},
        {"heading": "All open risks", "kind": "table", "weight": 1.15,
         "step": 0.05, "min_pages": 4, "badges": {"20": "bad",
                                                  "12": "warn",
                                                  "9": "warn",
                                                  "8": "warn",
                                                  "6": "good",
                                                  "4": "good",
                                                  "3": "good"},
         "columns": [("ID", 0.5), ("Risk", 3.6), ("Score", 0.7,
                                                  "center"),
                     ("Owner", 1.4)],
         "rows": [
             ["T1", "Altimeter range noise misses 5 cm", "20", "Payload"],
             ["T2", "Antenna deployment fails in orbit", "12", "RF"],
             ["T3", "Energy margin under 15 %", "9", "Systems"],
             ["T4", "Reaction wheel supplier late", "8", "ADCS"],
             ["T5", "Thermal vacuum test slot moves", "9", "AIT"],
             ["T6", "Flight software late for TRR", "6", "Software"],
             ["T7", "Harness mass grows", "6", "AIT"],
             ["T8", "Star tracker false locks near the pole", "6",
              "ADCS"],
             ["T9", "Launch slips into the polar night", "8", "PM"],
             ["T10", "Student team leaves after exams", "4", "PM"],
             ["T11", "Battery cells age in storage", "3", "Power"],
         ]},
    ],
}
