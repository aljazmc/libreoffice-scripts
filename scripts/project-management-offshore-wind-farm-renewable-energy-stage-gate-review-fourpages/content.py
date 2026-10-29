"""Stage Gate Review of Northgate Offshore Wind: the project and everything the
document could say. The typesetting keeps what fits into four pages, the
most important first."""

PROJECT = {
    "name": "Northgate Offshore Wind",
    "code": "NOW-1",
    "author": "Gate review panel, Group Capital Projects",
}

RESULT = {"Met": "good", "Partly": "warn", "Not met": "bad"}

DOCUMENT = {
    "title": "Stage Gate 3 Review",
    "subtitle": "From development to execution · panel review of 21 – 23 "
                "April 2026, before the final investment decision",
    "meta": [("Project", "NOW-1"), ("Gate", "3 · Execute"),
             ("Panel chair", "Dr Henrik Aalto"),
             ("Recommendation", "Pass with 4 conditions")],
    "sections": [
        {"heading": "Where we are", "kind": "figure", "weight": 0.1,
         "charts": [{"type": "chevrons", "steps": [
             {"label": "Gate 0 · Identify", "status": "done",
              "sub": "2019 · lease won"},
             {"label": "Gate 1 · Assess", "status": "done",
              "sub": "2021 · concept chosen"},
             {"label": "Gate 2 · Select", "status": "done",
              "sub": "2023 · consent applied"},
             {"label": "Gate 3 · Execute", "status": "now",
              "sub": "2026 · this review, then FID"},
             {"label": "Gate 4 · Operate", "sub": "2030 · handover"},
         ]}]},
        {"heading": "Verdict", "kind": "callout", "weight": 0.15,
         "tone": "good", "label": "Pass with conditions.",
         "text": "The project is ready for the final investment decision "
                 "once the four conditions below are met. None of them "
                 "changes the economics; two are about how ready we are "
                 "to manage the contractors."},
        {"heading": "Criteria", "kind": "figure", "weight": 0.2,
         "height": {1: 165, 2: 180, 4: 190}, "charts": [{
             "type": "heatmap", "rows": ["Strategy and value",
                                         "Commercial", "Technical",
                                         "Schedule", "Cost estimate",
                                         "Consents and environment",
                                         "Organisation", "HSE",
                                         "Stakeholders"],
             "cols": ["Evidence", "Maturity", "Risk", "Overall"],
             "values": [["Met", "Met", "Met", "Met"],
                        ["Met", "Partly", "Met", "Partly"],
                        ["Met", "Met", "Partly", "Met"],
                        ["Met", "Partly", "Partly", "Partly"],
                        ["Met", "Met", "Met", "Met"],
                        ["Met", "Met", "Met", "Met"],
                        ["Partly", "Not met", "Partly", "Partly"],
                        ["Met", "Met", "Met", "Met"],
                        ["Met", "Met", "Partly", "Met"]],
             "badges": RESULT, "labels": 0.3}]},
        {"heading": "Conditions", "kind": "table", "weight": 0.3,
         "step": 0.1, "columns": [("No.", 0.5), ("Condition", 4),
                                  ("Owner", 1.4), ("By", 0.9)],
         "rows": [
             ["C1", "Appoint the package managers for cables and "
              "substations, and fill 90 % of the owner's team",
              "Project director", "FID"],
             ["C2", "Sign the vessel charter for the 2028 foundation "
              "season, with the option for 2029", "Commercial",
              "FID"],
             ["C3", "Integrate the four contractors' schedules into one "
              "baseline and run a schedule risk analysis", "Planning",
              "FID + 3 mo"],
             ["C4", "Agree the interface agreement between the turbine "
              "and foundation contractors", "Engineering",
              "FID + 2 mo"],
         ]},
        {"heading": "Maturity by discipline", "kind": "figure",
         "weight": 0.4, "min_pages": 2, "height": 165, "charts": [{
             "type": "progress", "format": "{:.0f} %", "items": [
                 {"label": "Engineering design", "value": 82,
                  "target": 70, "status": "good", "note": "FEED "
                  "complete, detailed design started"},
                 {"label": "Contracts", "value": 76, "target": 80,
                  "status": "warn", "note": "4 of 6 major contracts "
                  "ready to sign"},
                 {"label": "Schedule", "value": 64, "target": 75,
                  "status": "warn", "note": "contractor schedules not "
                  "yet integrated"},
                 {"label": "Owner's team", "value": 58, "target": 90,
                  "status": "bad", "note": "41 of 71 roles filled"},
                 {"label": "Consents", "value": 100, "target": 100,
                  "status": "good", "note": "all granted; 2 conditions "
                  "to discharge"},
             ]}]},
        {"heading": "Cost and schedule confidence", "kind": "figure",
         "weight": 0.5, "min_pages": 2, "height": 160, "widths": [1, 1],
         "charts": [
             {"type": "bars", "title": "Cost estimate", "subtitle":
              "€bn, by confidence level", "format": "{:.2f}",
              "categories": ["P10", "P50", "P80", "P90"],
              "target": 3.9, "target_label": "budget",
              "series": [{"name": "Capex",
                          "values": [3.62, 3.78, 3.94, 4.06],
                          "colors": [4, 0, "warn", "bad"]}]},
             {"type": "bars", "title": "First power", "subtitle":
              "months after FID, by confidence", "format": "{:.0f}",
              "categories": ["P10", "P50", "P80", "P90"],
              "target": 40, "target_label": "plan",
              "series": [{"name": "Months",
                          "values": [37, 39, 42, 44],
                          "colors": [4, 0, "warn", "bad"]}]},
         ]},
        {"heading": "Panel observations", "kind": "bullets",
         "weight": 0.6, "step": 0.15, "min_pages": 2, "items": [
             "The development team has done exceptional work on the "
             "consents and the seabed: no open issue there.",
             "The owner's team is too thin for a four-contract strategy; "
             "the interfaces between contractors are where projects of "
             "this kind lose time.",
             "The P80 cost is just above the budget; the panel accepts "
             "this because the contingency is held at group level.",
             "The vessel market is the largest single risk to the "
             "schedule and should be closed before FID.",
         ]},
        {"heading": "Panel", "kind": "tags", "weight": 0.8, "step": 0.1,
         "min_pages": 4, "items": [
             ("Chair", "Dr Henrik Aalto, Group Capital Projects"),
             ("Engineering", "Sofia Marques, independent"),
             ("Commercial", "James Whitlock, Group Procurement"),
             ("Finance", "Mei Tanaka, Group Finance"),
             ("HSE", "Olu Adeyemi, Group HSE"),
         ]},
        {"heading": "Previous gate actions", "kind": "table",
         "weight": 0.9, "step": 0.1, "min_pages": 4, "badges": {
             "Closed": "good", "Open": "warn"},
         "columns": [("Action from Gate 2", 4), ("Status", 1, "center")],
         "rows": [
             ["Complete the geophysical survey of all positions",
              "Closed"],
             ["Decide between 15 and 18 MW turbines", "Closed"],
             ["Secure the grid connection date in writing", "Closed"],
             ["Build the owner's team for execution", "Open"],
             ["Agree the port for marshalling", "Closed"],
         ]},
        {"heading": "Plan to Gate 4", "kind": "figure", "weight": 1.0,
         "min_pages": 4, "height": 200, "charts": [{"type": "gantt",
          "columns": ["2026", "2027", "2028", "2029", "2030"],
          "groups": ["Engineering", "Manufacture", "Offshore"],
          "today": 0.35,
          "tasks": [
              {"label": "Detailed design", "start": 0.3, "end": 1.5},
              {"label": "Onshore substation", "start": 1, "end": 2.6,
               "group": 1},
              {"label": "Monopiles and transition pieces", "start": 1.2,
               "end": 2.5, "group": 1},
              {"label": "Turbines", "start": 1.8, "end": 3.4,
               "group": 1},
              {"label": "Foundations installed", "start": 2.3,
               "end": 2.9, "group": 2, "critical": True},
              {"label": "Cables laid", "start": 2.5, "end": 3.3,
               "group": 2},
              {"label": "Turbines installed", "start": 3.2, "end": 4.2,
               "group": 2, "critical": True},
              {"label": "First power", "start": 3.55, "milestone": True},
              {"label": "Gate 4", "start": 4.4, "milestone": True},
          ]}]},
        {"heading": "Method", "kind": "text", "weight": 1.2, "step": 0.3,
         "min_pages": 4, "paragraphs": [
             "The panel read 64 documents, interviewed 22 people over "
             "three days and visited the marshalling port. Each "
             "criterion was rated on the evidence, the maturity of the "
             "work against what is expected at this gate, and the risk "
             "that remains.",
         ]},
        {"heading": "Readiness to execute", "kind": "figure",
         "weight": 1.05, "min_pages": 4, "height": 160, "widths": [3, 2],
         "charts": [
             {"type": "bars", "title": "Owner's team", "subtitle":
              "roles filled by function", "stacked": True,
              "categories": ["Engineering", "Construction", "Commercial",
                             "HSE", "Planning", "Quality"],
              "series": [{"name": "Filled", "color": "good",
                          "values": [14, 9, 6, 5, 3, 4]},
                         {"name": "Open", "color": "bad",
                          "values": [4, 12, 3, 2, 4, 5]}], "inside": True},
             {"type": "donut", "title": "Interviews", "subtitle":
              "who the panel met",
              "segments": [("Project team", 12), ("Contractors", 5),
                           ("Group functions", 3), ("Regulators", 2)],
              "center": ("22", "people")},
         ]},
        {"heading": "Conditions from the panel's view", "kind": "entries",
         "weight": 1.1, "step": 0.2, "inner": 0.1, "min_pages": 4,
         "entries": [
             {"title": "Why the owner's team matters", "text": [
                 "Four contractors share the seabed, the port and the "
                 "weather windows. Somebody has to own every interface "
                 "between them, every day, and that somebody is us."]},
             {"title": "Why the vessel cannot wait", "text": [
                 "Two other projects in the same sea want the same heavy "
                 "lift vessel for 2028. Without the charter, the 2028 "
                 "foundation season is a hope, not a plan."]},
         ]},
    ],
}
