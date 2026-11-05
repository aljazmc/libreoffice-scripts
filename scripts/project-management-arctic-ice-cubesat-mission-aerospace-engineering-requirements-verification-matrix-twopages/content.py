"""Requirements Verification Matrix of FROSTBYTE-1 CubeSat: the project and
everything the document could say. The typesetting keeps what fits into two
pages, the most important first."""

PROJECT = {
    "name": "FROSTBYTE-1 CubeSat",
    "code": "FB1",
    "author": "Jonas Berg, Systems Engineer",
}

STATUS = {"Closed": "good", "Open": "warn", "Failed": "bad",
          "Waiver": "info"}
METHOD = {"T": 0, "A": 1, "I": 3, "R": 4}

DOCUMENT = {
    "title": "Requirements Verification Matrix",
    "subtitle": "System requirements and how each one is verified · "
                "status at the test readiness review",
    "meta": [("Mission", "FROSTBYTE-1"), ("Document", "FB1-SE-014"),
             ("Requirements", "142"), ("Closed", "97 · 68 %"),
             ("Revision", "D")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "height": {1: 130, 2: 140},
         "widths": [2, 3], "charts": [
             {"type": "donut", "title": "Closure",
              "segments": [("Closed", 97, "good"), ("Open", 39, "warn"),
                           ("Waiver", 4, "info"), ("Failed", 2, "bad")],
              "center": ("142", "requirements")},
             {"type": "bars", "horizontal": True, "stacked": True,
              "title": "By subsystem", "values": False,
              "categories": ["Mission", "Payload", "Power", "ADCS",
                             "Comms", "OBC and software", "Structure "
                             "and thermal"],
              "series": [{"name": "Closed", "color": "good",
                          "values": [6, 14, 16, 12, 15, 18, 16]},
                         {"name": "Open", "color": "warn",
                          "values": [2, 12, 2, 6, 4, 9, 4]},
                         {"name": "Waiver or failed", "color": "bad",
                          "values": [0, 3, 0, 1, 1, 1, 0]}]},
         ]},
        {"heading": "Key requirements", "kind": "table", "weight": 0.2,
         "step": 0.05, "badges": {**STATUS, "T": "accent", "A": "info",
                                  "I": "neutral", "R": "neutral"},
         "columns": [("ID", 0.9), ("Requirement", 3.6),
                     ("Method", 0.8, "center"), ("Evidence", 1.6),
                     ("Status", 0.9, "center")],
         "rows": [
             ["SYS-001", "Measure sea-ice freeboard to 3 cm or better "
              "over 25 km", "A", "Perf. analysis", "Open"],
             ["SYS-004", "Cover the Arctic above 60° N every 30 days",
              "A", "Orbit analysis", "Closed"],
             ["SYS-010", "Total mass under 12 kg", "T", "Mass "
              "measurement", "Closed"],
             ["PL-012", "Altimeter range noise under 5 cm at 1 Hz",
              "T", "Bench test", "Failed"],
             ["PWR-003", "Positive energy balance in every mode", "A",
              "Power budget", "Closed"],
             ["ADCS-002", "Point the antenna to nadir within 0.1°", "T",
              "Air-bearing test", "Open"],
             ["COM-005", "Downlink 1.2 GB a day", "T", "RF test",
              "Closed"],
             ["STR-007", "Survive the launch vibration levels", "T",
              "Vibration test", "Open"],
             ["ENV-002", "Deorbit within 5 years of end of mission",
              "A", "Lifetime analysis", "Closed"],
             ["SW-018", "Recover from a single event upset in 10 s",
              "T", "Fault injection", "Waiver"],
         ]},
        {"heading": "Closure trend", "kind": "figure", "weight": 0.3,
         "height": {1: 140, 2: 155, 4: 165}, "charts": [{"type": "line",
          "title": "Requirements closed", "x": ["PDR", "+2 mo", "+4 mo",
                                                 "CDR", "+2 mo", "+4 mo",
                                                 "TRR", "+2 mo", "FRR"],
          "target": 142, "target_label": "all", "end_labels": True,
          "series": [{"name": "Actual", "area": True,
                      "values": [8, 15, 26, 41, 58, 79, 97, None, None]},
                     {"name": "Plan", "dash": True, "color": 1,
                      "values": [10, 18, 30, 45, 62, 84, 104, 126,
                                 142]}]}]},
        {"heading": "Verification methods", "kind": "figure",
         "weight": 0.4, "min_pages": 2, "height": 120, "widths": [2, 3],
         "charts": [
             {"type": "donut", "title": "By method",
              "segments": [("Test", 71), ("Analysis", 42),
                           ("Inspection", 18), ("Review of design", 11)],
              "center": ("142", "")},
             {"type": "heatmap", "title": "Method by verification level",
              "rows": ["Unit", "Subsystem", "System"],
              "cols": ["Test", "Analysis", "Inspection", "Review"],
              "values": [[24, 6, 5, 2], [29, 14, 7, 4], [18, 22, 6, 5]],
              "format": "{:.0f}", "color": 0},
         ]},
        {"heading": "The failed requirement", "kind": "text",
         "weight": 0.5, "step": 0.3, "min_pages": 2, "paragraphs": [
             "PL-012 failed on the bench: the altimeter's range noise is "
             "7.2 cm at 1 Hz against 5 cm required. The cause is clock "
             "jitter on the engineering model's oscillator. The flight "
             "model uses an oven-controlled oscillator; if it still "
             "fails, averaging over 2 Hz meets SYS-001 at the cost of "
             "along-track resolution.",
         ]},
        {"heading": "Waivers", "kind": "entries", "weight": 0.6,
         "step": 0.2, "inner": 0.1, "min_pages": 2, "entries": [
             {"title": "SW-018 · upset recovery in 10 s",
              "dates": "granted", "text": [
                  "Measured 14 s; accepted because no science is lost "
                  "in under 30 s."]},
             {"title": "STR-011 · first frequency above 100 Hz",
              "dates": "requested", "text": [
                  "Analysis gives 94 Hz; the launch provider accepts "
                  "above 90 Hz."]},
         ]},
        {"heading": "Open by owner", "kind": "figure", "weight": 0.8,
         "min_pages": 4, "height": 140, "charts": [{"type": "bars",
          "title": "Open requirements by owner", "stacked": True,
          "categories": ["Payload team", "Systems", "Avionics", "AIT",
                         "Suppliers"],
          "series": [{"name": "Test pending", "values": [8, 2, 6, 9, 3]},
                     {"name": "Analysis pending", "values": [4, 5, 2, 0,
                                                             1]},
                     {"name": "Evidence to review", "color": 4,
                      "values": [2, 1, 1, 2, 1]}]}]},
        {"heading": "Tests to come", "kind": "table", "weight": 0.9,
         "step": 0.1, "min_pages": 4,
         "columns": [("Test", 2.4), ("Closes", 2.4), ("Date", 1)],
         "rows": [
             ["Flight model altimeter bench test", "PL-012, PL-013, "
              "PL-015", "Mar 27"],
             ["System vibration", "STR-007, STR-009, STR-011", "May 27"],
             ["Thermal vacuum, 8 cycles", "THM-001 to THM-006", "Jun 27"],
             ["End-to-end radio test with the ground station",
              "COM-001 to COM-009", "Jun 27"],
             ["Day in the life, 72 hours", "SYS-020 to SYS-024",
              "Jul 27"],
         ]},
        {"heading": "Definitions", "kind": "tags", "weight": 1.0,
         "step": 0.1, "min_pages": 4, "items": [
             ("T · Test", "measured on hardware, against a procedure"),
             ("A · Analysis", "shown by calculation or simulation"),
             ("I · Inspection", "checked by looking or measuring"),
             ("R · Review", "shown by the design documents"),
             ("Closed", "evidence reviewed and accepted by systems"),
         ]},
        {"heading": "Traceability", "kind": "figure", "weight": 1.1,
         "min_pages": 4, "height": 120, "charts": [{"type": "funnel",
          "format": "{:.0f}", "shares": False,
          "stages": [("Mission objectives", 4),
                     ("System requirements", 31),
                     ("Subsystem requirements", 111),
                     ("Verification procedures", 64)],
          "power": 0.6}]},
        {"heading": "Requirements by level", "kind": "figure",
         "weight": 1.15, "min_pages": 4, "height": 140, "charts": [{
             "type": "heatmap", "rows": ["Mission", "System", "Payload",
                                         "Platform", "Ground"],
             "cols": ["Closed", "Open", "Waiver", "Failed"],
             "values": [[3, 1, 0, 0], [22, 7, 1, 1], [14, 12, 2, 1],
                        [44, 15, 1, 0], [14, 4, 0, 0]],
             "format": "{:.0f}", "color": 0, "labels": 0.18}]},
        {"heading": "Review board", "kind": "tags", "weight": 1.2,
         "step": 0.1, "min_pages": 4, "items": [
             ("Chair", "Prof. Anders Lund, external"),
             ("Systems", "Jonas Berg"),
             ("Product assurance", "Ritva Salo"),
             ("Payload", "Dr Elin Haug, Arctic Radar Lab"),
             ("Launch provider", "Interface manager, as observer"),
         ]},
    ],
}
