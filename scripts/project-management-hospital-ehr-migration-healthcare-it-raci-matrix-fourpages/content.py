"""RACI Matrix of St Brigid's EHR Migration: the project and everything the
document could say. The typesetting keeps what fits into four pages, the
most important first."""

PROJECT = {
    "name": "St Brigid's EHR Migration",
    "code": "EHR-26",
    "author": "Marcus Byrne, Programme Manager",
}

RACI = {"R": "info", "A": "accent", "A/R": "accent", "C": "warn",
        "I": "neutral"}

ROLES = [("Deliverable", 2.6), ("SRO", 0.7, "center"),
         ("PM", 0.7, "center"), ("CCIO", 0.75, "center"),
         ("IT", 0.7, "center"), ("Data", 0.75, "center"),
         ("Wards", 0.8, "center"), ("Vendor", 0.9, "center")]

DOCUMENT = {
    "title": "RACI Matrix",
    "subtitle": "Who is responsible, accountable, consulted and informed "
                "for the deliverables of the EHR programme",
    "meta": [("Programme", "EHR-26"), ("Owner", "Marcus Byrne"),
             ("Deliverables", "24"), ("Roles", "7"),
             ("Approved", "Programme board, 2 Jun 2026")],
    "sections": [
        {"heading": "Key", "kind": "figure", "weight": 0.1,
         "height": 42, "charts": [{"type": "heatmap",
          "rows": ["Meaning"], "cols": ["R · does the work",
                                        "A · owns the outcome, signs off",
                                        "C · asked before",
                                        "I · told after"],
          "values": [["R", "A", "C", "I"]], "header": 18,
          "badges": RACI, "labels": 0.12, "bold": True}]},
        {"heading": "Plan and govern", "kind": "table", "weight": 0.2,
         "step": 0.05, "badges": RACI, "columns": ROLES,
         "rows": [
             ["Business case and funding", "A", "R", "C", "C", "I", "I",
              "I"],
             ["Programme plan and budget", "A", "R", "C", "C", "C", "I",
              "C"],
             ["Clinical safety case (DCB0160)", "I", "C", "A/R", "C",
              "C", "C", "C"],
             ["Risk and issue management", "I", "A/R", "C", "R", "R",
              "C", "R"],
         ]},
        {"heading": "Build and test", "kind": "table", "weight": 0.3,
         "step": 0.05, "badges": RACI, "columns": ROLES,
         "rows": [
             ["Clinical workflows and order sets", "I", "C", "A", "C",
              "I", "R", "R"],
             ["System configuration", "I", "C", "C", "A", "I", "C",
              "R"],
             ["Interfaces (lab, radiology, pharmacy)", "I", "C", "C",
              "A/R", "C", "I", "R"],
             ["Medical device integration", "I", "C", "C", "A", "I", "C",
              "R"],
             ["Testing and defect fixing", "I", "A", "C", "R", "R", "C",
              "R"],
         ]},
        {"heading": "Migrate and go live", "kind": "table",
         "weight": 0.4, "step": 0.05, "badges": RACI, "columns": ROLES,
         "rows": [
             ["Data mapping and cleansing", "I", "C", "C", "C", "A/R",
              "C", "R"],
             ["Trial loads and reconciliation", "I", "I", "C", "R",
              "A/R", "I", "R"],
             ["Training of staff", "I", "A", "C", "I", "I", "R", "C"],
             ["Go-live readiness assessment", "I", "R", "A", "C", "C",
              "R", "I"],
             ["Cutover and go/no-go", "A", "R", "R", "R", "R", "C",
              "R"],
             ["Hypercare and command centre", "I", "A", "R", "R", "C",
              "R", "R"],
         ]},
        {"heading": "Close and benefit", "kind": "table", "weight": 0.6,
         "step": 0.05, "min_pages": 2, "badges": RACI, "columns": ROLES,
         "rows": [
             ["Benefits tracking", "A", "R", "C", "I", "C", "C", "I"],
             ["Decommission legacy systems", "I", "A", "C", "R", "R",
              "I", "C"],
             ["Lessons learned and closure", "A", "R", "C", "C", "C", "C",
              "C"],
         ]},
        {"heading": "Load by role", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": 155, "widths": [3, 2], "charts": [
             {"type": "bars", "title": "Assignments per role",
              "stacked": True, "inside": True,
              "categories": ["SRO", "PM", "CCIO", "IT", "Data", "Wards",
                             "Vendor"],
              "series": [{"name": "A", "color": "accent",
                          "values": [4, 5, 3, 4, 2, 0, 0]},
                         {"name": "R", "color": "info",
                          "values": [0, 5, 3, 7, 5, 5, 10]},
                         {"name": "C", "color": "warn",
                          "values": [2, 7, 10, 6, 6, 7, 4]},
                         {"name": "I", "color": "neutral",
                          "values": [11, 2, 0, 1, 4, 5, 3]}]},
             {"type": "donut", "title": "Accountability",
              "segments": [("SRO", 4), ("PM", 5), ("CCIO", 3),
                           ("IT", 4), ("Data", 2)],
              "center": ("18", "deliverables")},
         ]},
        {"heading": "Rules", "kind": "bullets", "weight": 0.7, "step": 0.2,
         "min_pages": 2, "items": [
             "Exactly one **A** per deliverable. The A signs off and "
             "answers for the result, even when others do the work.",
             "At least one **R** per deliverable; an A can also be the R.",
             "Consult before the decision, inform after it: a C has a "
             "say, an I has the news.",
             "Anything clinical has the CCIO as A or C. Nothing clinical "
             "is signed off by the vendor.",
         ]},
        {"heading": "Roles", "kind": "tags", "weight": 0.9, "step": 0.1,
         "min_pages": 4, "items": [
             ("SRO", "senior responsible owner, the chief operating "
                     "officer, Helen Quinn"),
             ("PM", "programme manager, Marcus Byrne"),
             ("CCIO", "chief clinical information officer, Dr Aoife "
                      "Ryan"),
             ("IT", "head of IT, Declan Moore, and his teams"),
             ("Data", "data migration lead, Owen Fitzgerald"),
             ("Wards", "ward managers and clinical leads of each "
                       "department"),
             ("Vendor", "Meridian Health, the EHR supplier"),
         ]},
        {"heading": "Decision rights", "kind": "figure", "weight": 1.0,
         "min_pages": 4, "charts": [{"type": "tree", "root": {
             "label": "Hospital board", "note": "funding over €2m",
             "children": [
                 {"label": "Programme board", "note": "SRO chairs, "
                  "monthly", "children": [
                      {"label": "Budget changes up to €2m"},
                      {"label": "Go-live date"},
                      {"label": "Scope changes"}]},
                 {"label": "Clinical design authority", "note": "CCIO "
                  "chairs, weekly", "children": [
                      {"label": "Workflows and order sets"},
                      {"label": "Clinical safety hazards",
                       "status": "bad"},
                      {"label": "Data migration rules"}]},
                 {"label": "Technical design authority", "note": "head "
                  "of IT chairs", "children": [
                      {"label": "Architecture and interfaces"},
                      {"label": "Security and access"},
                      {"label": "Devices"}]},
                 {"label": "Programme manager", "note": "day to day",
                  "children": [
                      {"label": "Plan within tolerance"},
                      {"label": "Risks and issues"},
                      {"label": "Resources"}]},
             ]}}]},
        {"heading": "Escalation", "kind": "figure", "weight": 1.1,
         "min_pages": 4, "charts": [{"type": "chevrons", "steps": [
             {"label": "Workstream lead", "status": "done",
              "sub": "Solves within 2 days, inside tolerance"},
             {"label": "Programme manager", "status": "done",
              "sub": "Within a week; can move resources"},
             {"label": "Design authority", "status": "now",
              "sub": "Clinical or technical choices"},
             {"label": "Programme board", "sub": "Time, cost or scope "
                                               "beyond tolerance"},
             {"label": "Hospital board", "sub": "Funding and strategy"},
         ]}]},
        {"heading": "Changes since the last version", "kind": "bullets",
         "weight": 1.2, "step": 0.2, "min_pages": 4, "items": [
             "Medical device integration moved from the vendor to IT as "
             "A, after the theatres certification issue.",
             "Ward managers are now R for the readiness assessment, not "
             "only C.",
             "Benefits tracking added, with the SRO as A.",
         ]},
        {"heading": "Forums", "kind": "table", "weight": 1.05, "step": 0.1,
         "min_pages": 4, "columns": [("Forum", 2), ("Chair", 1.4),
                                     ("When", 1.2), ("Decides", 3)],
         "rows": [
             ["Programme board", "SRO", "Monthly", "Budget, date, scope "
              "within the business case"],
             ["Clinical design authority", "CCIO", "Weekly",
              "Workflows, order sets, safety hazards"],
             ["Technical design authority", "Head of IT", "Fortnightly",
              "Architecture, interfaces, security"],
             ["Cutover steering", "Programme manager", "Daily from "
              "T−2 weeks", "Readiness actions, go / no-go preparation"],
             ["Change advisory board", "IT service manager", "Weekly",
              "Changes to live systems"],
         ]},
        {"heading": "Coverage check", "kind": "figure", "weight": 1.08,
         "min_pages": 4, "height": 115, "charts": [{"type": "progress",
          "format": "{:.0f} %", "items": [
              {"label": "Deliverables with exactly one A", "value": 100,
               "status": "good"},
              {"label": "Deliverables with at least one R", "value": 100,
               "status": "good"},
              {"label": "Clinical deliverables with the CCIO as A or C",
               "value": 100, "status": "good"},
              {"label": "Roles confirmed by the person named",
               "value": 86, "target": 100, "status": "warn",
               "display": "6 of 7"},
          ]}]},
        {"heading": "Who works with whom", "kind": "figure",
         "weight": 1.1, "min_pages": 4, "height": 150, "charts": [{
             "type": "heatmap", "title": "Deliverables shared by two "
             "roles", "subtitle": "count of deliverables where both are "
             "R, A or C",
             "rows": ["SRO", "PM", "CCIO", "IT", "Data", "Wards",
                      "Vendor"],
             "cols": ["SRO", "PM", "CCIO", "IT", "Data", "Wards",
                      "Vendor"],
             "values": [["", 6, 5, 4, 2, 1, 2],
                        [6, "", 15, 13, 9, 9, 11],
                        [5, 15, "", 12, 10, 11, 12],
                        [4, 13, 12, "", 10, 8, 13],
                        [2, 9, 10, 10, "", 5, 8],
                        [1, 9, 11, 8, 5, "", 8],
                        [2, 11, 12, 13, 8, 8, ""]],
             "format": "{:.0f}", "labels": 0.12}]},
        {"kind": "callout", "weight": 1.12, "tone": "info",
         "min_pages": 4, "label": "Reading the matrix:",
         "text": "the CCIO and the programme manager share fifteen "
                 "deliverables, more than any other pair, which is why "
                 "they meet every Monday before the clinical design "
                 "authority."},
    ],
}
