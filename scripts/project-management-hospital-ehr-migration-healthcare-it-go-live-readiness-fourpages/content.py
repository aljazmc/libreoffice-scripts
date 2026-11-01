"""Go-Live Readiness of St Brigid's EHR Migration: the project and everything
the document could say. The typesetting keeps what fits into four pages, the
most important first."""

PROJECT = {
    "name": "St Brigid's EHR Migration",
    "code": "EHR-26",
    "author": "Dr Niamh Kelly, Clinical Programme Director",
}

DEPARTMENTS = ["Emergency", "Acute medicine", "Surgery", "Theatres",
               "Maternity", "Paediatrics", "ICU", "Outpatients",
               "Pharmacy", "Radiology", "Laboratory"]

DOCUMENT = {
    "title": "Go-Live Readiness Assessment",
    "subtitle": "Four weeks before go-live · assessed 9 October 2026 by "
                "department and dimension",
    "meta": [("Programme", "EHR-26"), ("Go-live", "7 Nov 2026"),
             ("Assessment", "T−4 weeks"), ("Verdict", "Go, with "
                                                      "conditions")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "charts": [{"type": "kpis",
         "tiles": [
             {"label": "Overall", "value": "84 %", "delta": "+9",
              "status": "good", "note": "of criteria met",
              "spark": [52, 61, 68, 75, 84]},
             {"label": "Departments ready", "value": "7 / 11",
              "status": "warn", "note": "4 with conditions"},
             {"label": "Staff trained", "value": "91 %", "status": "good",
              "note": "target 90 % by T−2"},
             {"label": "Blockers", "value": "2", "status": "bad",
              "note": "Maternity, Theatres"},
         ]}]},
        {"heading": "Readiness by department", "kind": "figure",
         "weight": 0.2, "height": {1: 225, 2: 240, 4: 250},
         "charts": [{"type": "heatmap", "rows": DEPARTMENTS,
          "cols": ["People", "Process", "Technology", "Data",
                   "Devices", "Support"],
          "values": [[96, 90, 100, 95, 100, 92],
                     [92, 88, 100, 90, 85, 90],
                     [88, 80, 95, 85, 90, 88],
                     [70, 62, 80, 75, 55, 80],
                     [65, 58, 90, 70, 80, 75],
                     [94, 90, 100, 92, 95, 90],
                     [90, 85, 92, 88, 70, 92],
                     [85, 80, 100, 95, 100, 85],
                     [98, 95, 92, 100, 100, 95],
                     [90, 92, 85, 95, 100, 90],
                     [92, 95, 78, 90, 100, 88]],
          "thresholds": [(0, "bad"), (70, "warn"), (85, "good")],
          "format": "{:.0f}", "labels": 0.2}]},
        {"heading": "Verdict", "kind": "callout", "weight": 0.25,
         "tone": "good", "label": "Go, with conditions:",
         "text": "the programme board recommends go-live on 7 November if "
                 "Maternity and Theatres close their blockers by the T−2 "
                 "assessment on 23 October; otherwise both stay on paper "
                 "for two weeks after go-live."},
        {"heading": "Blockers and conditions", "kind": "table",
         "weight": 0.4, "step": 0.15, "min_pages": 2,
         "badges": {"Blocker": "bad", "Condition": "warn",
                    "Closed": "good"},
         "columns": [("Department", 1.3), ("Issue", 3.6), ("Owner", 1.3),
                     ("Due", 0.8), ("Type", 1, "center")],
         "rows": [
             ["Maternity", "Fetal monitoring interface fails under "
              "load; CTG traces not filed to the record", "Integration",
              "16 Oct", "Blocker"],
             ["Theatres", "Anaesthetic machines' device integration not "
              "certified", "Medical physics", "20 Oct", "Blocker"],
             ["Theatres", "Only 62 % of theatre staff trained",
              "Theatre manager", "23 Oct", "Condition"],
             ["ICU", "Infusion pump drug library not matched to the "
              "formulary", "Pharmacy", "23 Oct", "Condition"],
             ["Surgery", "Order sets for 4 procedures not built",
              "Clinical builders", "19 Oct", "Condition"],
             ["Laboratory", "Label printers in 3 wards misaligned",
              "IT field", "12 Oct", "Closed"],
         ]},
        {"heading": "Trend to go-live", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": 165, "widths": [3, 2], "charts": [
             {"type": "line", "title": "Criteria met",
              "subtitle": "% of 214", "format": "{:.0f}",
              "x": ["T−12", "T−10", "T−8", "T−6", "T−4", "T−2", "T−0"],
              "target": 95, "target_label": "go threshold",
              "series": [
                  {"name": "Actual", "values": [52, 61, 68, 75, 84, None,
                                                None]},
                  {"name": "Forecast", "dash": True, "color": 1,
                   "values": [None, None, None, None, 84, 92, 97]}]},
             {"type": "donut", "title": "Criteria",
              "segments": [("Met", 180, "good"), ("In progress", 26,
                                                  "warn"),
                           ("Not started", 8, "bad")],
              "center": ("214", "criteria")},
         ]},
        {"heading": "Dimensions", "kind": "tags", "weight": 0.7,
         "step": 0.1, "min_pages": 2, "items": [
             ("People", "trained, rostered, super users named"),
             ("Process", "new workflows agreed and rehearsed"),
             ("Technology", "devices, printers, interfaces tested"),
             ("Data", "migrated data validated by the department"),
             ("Devices", "medical devices integrated and certified"),
             ("Support", "floor walkers and escalation in place"),
         ]},
        {"heading": "Training by department", "kind": "figure",
         "weight": 0.9, "min_pages": 4, "height": 200, "charts": [{
             "type": "bars", "horizontal": True, "format": "{:.0f}%",
             "target": 90, "target_label": "target",
             "categories": DEPARTMENTS,
             "series": [{"name": "Trained", "values": [97, 94, 90, 62, 81,
                                                       95, 88, 92, 99, 94,
                                                       93],
                         "colors": ["good", "good", "good", "bad", "warn",
                                    "good", "warn", "good", "good",
                                    "good", "good"]}]}]},
        {"heading": "Dress rehearsals", "kind": "figure", "weight": 1.0,
         "min_pages": 4, "height": 150, "widths": [1, 1], "charts": [
             {"type": "bars", "title": "Rehearsal duration",
              "subtitle": "hours, extract to go/no-go 1",
              "format": "{:.1f}", "target": 10, "target_label": "window",
              "categories": ["Trial 1", "Trial 2", "Trial 3", "DR 1",
                             "DR 2"],
              "series": [{"name": "Hours",
                          "values": [16.5, 13.0, 11.2, 9.6, 8.8],
                          "colors": ["bad", "bad", "warn", "good",
                                     "good"]}]},
             {"type": "line", "title": "Reconciliation differences",
              "subtitle": "% of records", "format": "{:.2f}",
              "x": ["Trial 1", "Trial 2", "Trial 3", "DR 1", "DR 2"],
              "target": 0.1, "target_label": "limit",
              "series": [{"name": "Differences", "color": "bad",
                          "values": [1.8, 0.9, 0.31, 0.12, 0.06]}]},
         ]},
        {"heading": "How we assess", "kind": "text", "weight": 1.2,
         "step": 0.3, "min_pages": 4, "paragraphs": [
             "Each department is scored against 214 criteria in six "
             "dimensions by its own clinical lead and a programme "
             "assessor, walking the ward together. A score is the share "
             "of the criteria met in that dimension.",
             "A **blocker** is a criterion that, unmet, would put "
             "patients at risk on day one; one blocker stops the "
             "department going live. A **condition** must be met by "
             "the next assessment.",
         ]},
        {"heading": "Next assessments", "kind": "figure", "weight": 1.1,
         "min_pages": 4, "charts": [{"type": "chevrons", "steps": [
             {"label": "T−4 · 9 Oct", "status": "done",
              "sub": "Go with conditions"},
             {"label": "T−2 · 23 Oct", "status": "now",
              "sub": "Blockers must be closed"},
             {"label": "T−1 · 30 Oct", "sub": "Final go/no-go by the "
                                            "board"},
             {"label": "Go-live · 7 Nov", "sub": "Cutover weekend"},
             {"label": "T+30", "sub": "Post go-live review"},
         ]}]},
        {"heading": "Support on day one", "kind": "figure", "weight": 1.05,
         "min_pages": 4, "height": 160, "widths": [3, 2], "charts": [
             {"type": "bars", "title": "Super users per shift",
              "subtitle": "planned for the first week", "stacked": True,
              "categories": ["ED", "AMU", "Surgery", "Theatres",
                             "Maternity", "Paeds", "ICU"],
              "series": [{"name": "Day", "values": [6, 5, 5, 6, 4, 3, 4]},
                         {"name": "Evening", "values": [4, 3, 3, 2, 3, 2,
                                                        3]},
                         {"name": "Night", "values": [3, 2, 2, 1, 2, 2,
                                                      2]}]},
             {"type": "donut", "title": "Open issues",
              "segments": [("Severity 1", 2, "bad"),
                           ("Severity 2", 11, "warn"),
                           ("Severity 3", 46, 0),
                           ("Cosmetic", 31, 4)],
              "center": ("90", "open")},
         ]},
        {"heading": "Lessons from other hospitals", "kind": "bullets",
         "weight": 1.15, "step": 0.2, "min_pages": 4, "items": [
             "**Printers fail first.** Every ward printer is tested "
             "twice in the last week, with the labels it will print.",
             "**Theatres need longer.** Two hospitals delayed theatres by "
             "two weeks; we have planned for that option.",
             "**Night shifts feel abandoned.** Floor walkers work nights "
             "in the first week, with the same numbers as days.",
             "**Fatigue peaks on day four.** Extra breaks and a quiet "
             "room for staff from day three.",
         ]},
    ],
}
