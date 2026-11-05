"""Work Breakdown Structure of FROSTBYTE-1 CubeSat: the project and everything
the document could say. The typesetting keeps what fits into two pages, the
most important first."""

PROJECT = {
    "name": "FROSTBYTE-1 CubeSat",
    "code": "FB1",
    "author": "Dr Kaisa Virtanen, Project Manager",
}

DOCUMENT = {
    "title": "Work Breakdown Structure",
    "subtitle": "A 6U CubeSat measuring Arctic sea-ice thickness with a "
                "radar altimeter · FB1-PM-002",
    "meta": [("Mission", "FROSTBYTE-1"), ("Document", "FB1-PM-002"),
             ("Revision", "C"), ("Work packages", "31"),
             ("Approved", "K. Virtanen")],
    "sections": [
        {"heading": "Breakdown", "kind": "figure", "weight": 0.1,
         "charts": [{"type": "tree", "size": 6.5, "root": {
             "label": "FROSTBYTE-1 mission", "code": "1.0",
             "children": [
                 {"label": "Management", "code": "1.1", "children": [
                     {"label": "Planning and control", "code": "1.1.1"},
                     {"label": "Risk", "code": "1.1.2"},
                     {"label": "Product assurance", "code": "1.1.3"},
                     {"label": "Reviews", "code": "1.1.4"}]},
                 {"label": "Payload", "code": "1.2", "children": [
                     {"label": "Radar altimeter", "code": "1.2.1",
                      "status": "bad"},
                     {"label": "Antenna", "code": "1.2.2"},
                     {"label": "Payload computer", "code": "1.2.3"},
                     {"label": "Calibration", "code": "1.2.4"}]},
                 {"label": "Platform", "code": "1.3", "children": [
                     {"label": "Structure", "code": "1.3.1"},
                     {"label": "Power", "code": "1.3.2"},
                     {"label": "ADCS", "code": "1.3.3"},
                     {"label": "On-board computer", "code": "1.3.4"},
                     {"label": "Radio, S and UHF", "code": "1.3.5"},
                     {"label": "Thermal", "code": "1.3.6"}]},
                 {"label": "AIT", "code": "1.4", "children": [
                     {"label": "Integration", "code": "1.4.1"},
                     {"label": "Environmental tests", "code": "1.4.2"},
                     {"label": "Flight software", "code": "1.4.3"}]},
                 {"label": "Ground and ops", "code": "1.5", "children": [
                     {"label": "Ground station", "code": "1.5.1"},
                     {"label": "Mission control", "code": "1.5.2"},
                     {"label": "Data processing", "code": "1.5.3"},
                     {"label": "Launch and LEOP", "code": "1.5.4"}]},
             ]}}]},
        {"heading": "Effort by work package", "kind": "figure",
         "weight": 0.2, "height": {1: 150, 2: 165, 4: 175},
         "widths": [3, 2], "charts": [
             {"type": "bars", "horizontal": True, "stacked": True,
              "title": "Person-months", "categories": ["1.1 Management",
                                                       "1.2 Payload",
                                                       "1.3 Platform",
                                                       "1.4 AIT",
                                                       "1.5 Ground and "
                                                       "ops"],
              "series": [{"name": "Staff", "color": 0,
                          "values": [14, 32, 26, 18, 16]},
                         {"name": "Students", "color": 3,
                          "values": [2, 10, 14, 8, 12]},
                         {"name": "Contractors", "color": 1,
                          "values": [0, 8, 4, 6, 3]}],
              "inside": True},
             {"type": "donut", "title": "Budget", "format": "€{:,.0f}k",
              "center": ("€3.1m", "total"),
              "segments": [("Payload", 1120), ("Platform", 760),
                           ("AIT", 420), ("Ground and ops", 310),
                           ("Launch", 360), ("Management", 130)]},
         ]},
        {"heading": "Dictionary", "kind": "table", "weight": 0.3,
         "step": 0.08, "min_pages": 2,
         "columns": [("WP", 0.6), ("Work package", 1.8),
                     ("Deliverable", 2.8), ("Owner", 1.4),
                     ("PM", 0.6, "end")],
         "rows": [
             ["1.2.1", "Radar altimeter", "Flight model, tested to "
              "qualification levels", "Arctic Radar Lab", "18"],
             ["1.2.2", "Antenna", "Deployable reflectarray, 2 × "
              "flight + 1 spare", "RF group", "8"],
             ["1.2.3", "Payload computer", "FPGA board with on-board "
              "processing", "Avionics", "10"],
             ["1.2.4", "Calibration", "Transponder campaign plan and "
              "results", "Science team", "6"],
             ["1.3.2", "Power", "Solar arrays, battery, power board",
              "Supplier", "7"],
             ["1.3.3", "ADCS", "Reaction wheels, star tracker, "
              "pointing to 0.1°", "Supplier", "9"],
             ["1.3.5", "Radio", "S-band downlink at 2 Mbit/s, UHF "
              "telecommand", "RF group", "8"],
             ["1.4.2", "Environmental tests", "Vibration, thermal "
              "vacuum, EMC reports", "AIT lead", "8"],
             ["1.5.3", "Data processing", "Sea-ice thickness product, "
              "level 2", "Science team", "11"],
         ]},
        {"heading": "Deliverables over time", "kind": "figure",
         "weight": 0.4, "min_pages": 2, "height": 120, "charts": [{
             "type": "timeline", "start": 0, "end": 30,
             "label_width": 90,
             "phases": [(0, 8, "Phase B"), (8, 20, "Phase C/D"),
                        (20, 30, "Phase E")],
             "ticks": [(0, "Jan 26"), (12, "Jan 27"), (24, "Jan 28")],
             "events": [
                 {"at": 3, "label": "PDR", "status": "done"},
                 {"at": 9, "label": "CDR", "status": "now"},
                 {"at": 15, "label": "Flight model"},
                 {"at": 18, "label": "Test review"},
                 {"at": 20, "label": "Launch"},
                 {"at": 23, "label": "First ice map"},
             ]}]},
        {"heading": "Rules of the WBS", "kind": "bullets", "weight": 0.5,
         "step": 0.15, "min_pages": 2, "items": [
             "Every work package has one owner, one deliverable and a "
             "budget; nothing is in two packages.",
             "The 100 % rule: the children of a package add up to all "
             "of its work, no more and no less.",
             "Work packages are small enough to plan, between two and "
             "twenty person-months.",
         ]},
        {"heading": "Interfaces", "kind": "figure", "weight": 0.7,
         "min_pages": 4, "height": 160, "charts": [{"type": "heatmap",
          "title": "Interface control documents between work packages",
          "rows": ["Radar", "Antenna", "Payload computer", "Power",
                   "ADCS", "OBC", "Radio", "Structure"],
          "cols": ["Radar", "Antenna", "PL comp.", "Power", "ADCS",
                   "OBC", "Radio", "Structure"],
          "values": [["", "ICD", "ICD", "ICD", "", "", "", "ICD"],
                     ["ICD", "", "", "", "ICD", "", "", "ICD"],
                     ["ICD", "", "", "ICD", "", "ICD", "", "ICD"],
                     ["ICD", "", "ICD", "", "ICD", "ICD", "ICD", "ICD"],
                     ["", "ICD", "", "ICD", "", "ICD", "", "ICD"],
                     ["", "", "ICD", "ICD", "ICD", "", "ICD", "ICD"],
                     ["", "", "", "ICD", "", "ICD", "", "ICD"],
                     ["ICD", "ICD", "ICD", "ICD", "ICD", "ICD", "ICD",
                      ""]],
          "badges": {"ICD": 1}, "labels": 0.16}]},
        {"heading": "Owners", "kind": "table", "weight": 0.8, "step": 0.1,
         "min_pages": 4,
         "columns": [("Organisation", 2), ("Packages", 2.6),
                     ("Person-months", 1, "end")],
         "rows": [
             ["University space lab", "1.1, 1.3.1, 1.3.4, 1.4, 1.5.1, "
              "1.5.2", "64"],
             ["Arctic Radar Lab", "1.2.1, 1.2.4", "24"],
             ["RF group", "1.2.2, 1.3.5", "16"],
             ["Polar science institute", "1.5.3", "14"],
             ["Suppliers", "1.3.2, 1.3.3, 1.3.6", "18"],
             ["Launch broker", "1.5.4", "4"],
         ]},
        {"heading": "Status of the packages", "kind": "figure",
         "weight": 0.9, "min_pages": 4, "height": 140, "charts": [{
             "type": "progress", "format": "{:.0f} %", "items": [
                 {"label": "1.1 Management", "value": 38, "target": 35,
                  "status": "good"},
                 {"label": "1.2 Payload", "value": 41, "target": 50,
                  "status": "bad"},
                 {"label": "1.3 Platform", "value": 55, "target": 50,
                  "status": "good"},
                 {"label": "1.4 AIT", "value": 12, "target": 15,
                  "status": "warn"},
                 {"label": "1.5 Ground and ops", "value": 30,
                  "target": 30, "status": "good"},
             ]}]},
        {"heading": "Notes", "kind": "text", "weight": 1.0, "step": 0.3,
         "min_pages": 4, "paragraphs": [
             "The radar altimeter (1.2.1) is the only package on the "
             "critical path that depends on a partner rather than a "
             "contract. Its milestones are tied to the partnership "
             "agreement and reviewed monthly by both directors.",
             "Students work on every package under a named staff "
             "mentor; their effort is planned at half the rate of staff "
             "for the same work.",
         ]},
        {"heading": "Effort over time", "kind": "figure", "weight": 1.1,
         "min_pages": 4, "height": 150, "charts": [{"type": "bars",
          "title": "Person-months per quarter", "stacked": True,
          "categories": ["Q1 26", "Q2", "Q3", "Q4", "Q1 27", "Q2", "Q3",
                         "Q4"],
          "series": [{"name": "Payload", "values": [6, 8, 9, 8, 7, 6, 4,
                                                   2]},
                     {"name": "Platform", "values": [5, 7, 8, 7, 6, 5, 3,
                                                     2]},
                     {"name": "AIT", "values": [0, 1, 2, 4, 7, 9, 6, 3]},
                     {"name": "Management and ground", "color": 4,
                      "values": [4, 4, 4, 5, 5, 6, 7, 7]}]}]},
        {"heading": "Deliverables list", "kind": "table", "weight": 1.15,
         "step": 0.05, "min_pages": 4,
         "columns": [("Code", 0.7), ("Deliverable", 3.4), ("Due", 1)],
         "rows": [
             ["D-01", "System requirements document", "PDR"],
             ["D-04", "Interface control documents", "CDR"],
             ["D-07", "Flight model altimeter", "Mar 27"],
             ["D-09", "Integrated satellite, tested", "Jul 27"],
             ["D-11", "Flight software release 1.0", "TRR"],
             ["D-14", "Ground segment ready", "Aug 27"],
             ["D-16", "Level 2 sea-ice thickness product", "L+3 mo"],
         ]},
    ],
}
