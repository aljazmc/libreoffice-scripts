"""Monitoring and Evaluation Plan of Cold Chain for Every Child: the project
and everything the document could say. The typesetting keeps what fits into
four pages, the most important first."""

PROJECT = {
    "name": "Cold Chain for Every Child",
    "code": "CCEC",
    "author": "Joseph Otieno, Monitoring and Evaluation Lead",
}

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
          "Oct", "Nov", "Dec"]

DOCUMENT = {
    "title": "Monitoring and Evaluation Plan",
    "subtitle": "What we measure, how, how often, and who does it · "
                "2026 – 2028",
    "meta": [("Programme", "CCEC"), ("Indicators", "14"),
             ("Data sources", "6"), ("M&E budget", "US$ 410k"),
             ("Lead", "Joseph Otieno")],
    "sections": [
        {"heading": "How data flows", "kind": "figure", "weight": 0.1,
         "charts": [{"type": "chevrons", "steps": [
             {"label": "Facility", "status": "done",
              "sub": "Nurses record each dose in the registry; "
                     "fridges log temperatures"},
             {"label": "District", "status": "done",
              "sub": "M&E officer checks completeness by the 5th"},
             {"label": "Programme", "status": "now",
              "sub": "Dashboard updated by the 10th"},
             {"label": "Review", "sub": "Monthly district meeting acts "
                                       "on it"},
             {"label": "Ministry", "sub": "Data flows to the national "
                                         "system"},
         ]}]},
        {"heading": "Indicators", "kind": "table", "weight": 0.2,
         "step": 0.05, "badges": {"Monthly": "info", "Quarterly": "warn",
                                  "Yearly": "neutral", "Live": "good"},
         "columns": [("Indicator", 3), ("Source", 1.8),
                     ("Frequency", 1, "center"), ("Owner", 1.4)],
         "rows": [
             ["Children 12 – 23 months fully immunised",
              "Coverage survey", "Yearly", "Independent firm"],
             ["DTP3 doses given against target", "Registry",
              "Monthly", "District M&E"],
             ["Drop-out from DTP1 to DTP3", "Registry", "Monthly",
              "District M&E"],
             ["Fridges working", "Remote monitors", "Live",
              "Cold chain officer"],
             ["Temperature alarms per fridge", "Remote monitors",
              "Live", "Cold chain officer"],
             ["Doses wasted", "Stock reports", "Monthly",
              "District pharmacist"],
             ["Outreach sessions held", "Session reports", "Monthly",
              "District M&E"],
             ["Stock-outs at facilities", "Stock reports", "Monthly",
              "District pharmacist"],
             ["Reports on time and complete", "Registry", "Monthly",
              "Programme M&E"],
             ["Caregivers who know the schedule", "Household survey",
              "Yearly", "Community team"],
         ]},
        {"heading": "Calendar", "kind": "figure", "weight": 0.3,
         "height": {1: 135, 2: 150, 4: 160}, "charts": [{
             "type": "heatmap", "title": "2027",
             "rows": ["Registry review", "Data quality audit",
                      "District review meeting", "Supervision visits",
                      "Household survey", "Coverage survey",
                      "Learning workshop"],
             "cols": MONTHS,
             "values": [["Run"] * 12,
                        ["", "", "Run", "", "", "Run", "", "", "Run", "",
                         "", "Run"],
                        ["Run"] * 12,
                        ["", "Run", "", "Run", "", "Run", "", "Run", "",
                         "Run", "", "Run"],
                        ["", "", "", "", "", "", "Run", "Run", "", "", "",
                         ""],
                        ["", "", "", "", "", "", "", "", "", "Big", "Big",
                         ""],
                        ["", "", "", "", "", "Run", "", "", "", "", "",
                         "Run"]],
             "badges": {"Run": 0, "Big": "warn"}, "show": False,
             "labels": 0.24}]},
        {"heading": "Evaluation questions", "kind": "entries",
         "weight": 0.4, "step": 0.2, "inner": 0.1, "min_pages": 2,
         "entries": [
             {"title": "Did coverage rise because of the programme?",
              "text": ["Compare the four districts with three similar "
                       "districts without the programme, before and "
                       "after (difference in differences)."]},
             {"title": "Is the cold chain still working in 2030?",
              "text": ["Follow-up of fridge uptime and repair times two "
                       "years after handover."]},
             {"title": "Who is still left out?", "text": [
                 "Coverage by ward, by distance to the facility and by "
                 "household wealth, from the surveys."]},
             {"title": "What did it cost per child?", "text": [
                 "Cost per additional fully immunised child, with and "
                 "without the fridges' 15-year life."]},
         ]},
        {"heading": "Data quality", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": 150, "widths": [3, 2], "charts": [
             {"type": "bars", "title": "Audit results", "subtitle":
              "% of records matching the paper register",
              "format": "{:.0f}", "target": 90, "target_label": "aim",
              "categories": ["Baringo N.", "Lake Shore", "Highlands E.",
                             "Dry Plains"],
              "series": [{"name": "2025", "color": 4,
                          "values": [78, 84, 71, 66]},
                         {"name": "2026", "values": [91, 93, 86, 82]}]},
             {"type": "donut", "title": "Errors found",
              "segments": [("Missing doses", 46), ("Wrong dates", 28),
                           ("Duplicates", 17), ("Other", 9)],
              "format": "{:.0f}%", "center": ("1,240", "records")},
         ]},
        {"heading": "Roles", "kind": "tags", "weight": 0.6, "step": 0.1,
         "min_pages": 2, "items": [
             ("Programme M&E lead", "plan, dashboard, reports to the "
                                    "donor"),
             ("District M&E officers", "monthly checks, review "
                                       "meetings, supervision"),
             ("Cold chain officers", "temperature alarms and repairs"),
             ("Independent firm", "baseline, midline and endline "
                                  "surveys"),
             ("Ministry", "owns the registry and the national data"),
         ]},
        {"heading": "Budget", "kind": "figure", "weight": 0.8,
         "min_pages": 4, "height": 140, "charts": [{"type": "donut",
          "format": "US$ {:,.0f}k", "center": ("$410k", "M&E"),
          "segments": [("Coverage surveys", 180),
                       ("Household surveys", 70),
                       ("Data quality audits", 50),
                       ("Staff", 80), ("Learning and reports", 30)]}]},
        {"heading": "Targets", "kind": "figure", "weight": 0.9,
         "min_pages": 4, "height": 155, "charts": [{"type": "line",
          "title": "Main outcome indicators", "subtitle": "%",
          "x": ["2024", "2025", "2026", "2027", "2028"],
          "format": "{:.0f}",
          "series": [{"name": "Fully immunised", "values": [58, 64, 72,
                                                            79, 85]},
                     {"name": "Drop-out DTP1–3", "color": "bad",
                      "values": [18, 15, 11, 8, 6]},
                     {"name": "Doses wasted", "color": 1,
                      "values": [14, 11, 7, 6, 5]}]}]},
        {"heading": "Ethics and data protection", "kind": "bullets",
         "weight": 1.0, "step": 0.2, "min_pages": 4, "items": [
             "Surveys approved by the national research ethics "
             "committee; consent in the caregiver's language.",
             "Names never leave the registry; reports use counts only.",
             "Tablets are encrypted and wiped remotely if lost.",
             "Communities see their own results at a village meeting "
             "every year.",
         ]},
        {"heading": "Learning", "kind": "text", "weight": 1.1, "step": 0.3,
         "min_pages": 4, "paragraphs": [
             "Twice a year the district teams, the ministry and the "
             "programme meet for two days to look at what the data "
             "says and change what we do. The June 2026 workshop "
             "moved outreach in Dry Plains to market days, which "
             "raised attendance by a third.",
         ]},
        {"heading": "Reporting", "kind": "table", "weight": 1.2,
         "step": 0.1, "min_pages": 4,
         "columns": [("Report", 2.4), ("To", 1.8), ("When", 1.6)],
         "rows": [
             ["Monthly dashboard", "Districts, ministry", "By the 10th"],
             ["Quarterly update", "Northfield Foundation",
              "30 days after"],
             ["Annual report", "Foundation, ministry, public",
              "31 March"],
             ["Midline evaluation", "All partners", "March 2027"],
             ["Endline evaluation", "All partners", "June 2029"],
         ]},
        {"heading": "Dashboard", "kind": "figure", "weight": 1.25,
         "min_pages": 4, "charts": [{"type": "kpis", "tiles": [
             {"label": "Reports on time", "value": "91 %",
              "status": "good", "note": "last month",
              "spark": [47, 58, 66, 74, 81, 88, 91]},
             {"label": "Complete records", "value": "94 %",
              "status": "good", "note": "registry"},
             {"label": "Audit match", "value": "88 %", "status": "warn",
              "note": "target 90 %"},
             {"label": "Review meetings", "value": "12 / 12",
              "status": 0, "note": "held this year"},
         ]}]},
        {"heading": "Comparison districts", "kind": "figure",
         "weight": 1.3, "min_pages": 4, "height": 150, "charts": [{
             "type": "line", "title": "Fully immunised", "subtitle":
             "%, programme against comparison districts",
             "x": ["2024", "2025", "2026"], "zero": False,
             "format": "{:.0f}", "end_labels": True,
             "series": [{"name": "Programme districts",
                         "values": [58, 66, 71]},
                        {"name": "Comparison districts", "color": 4,
                         "dash": True, "values": [60, 62, 63]}]}]},
    ],
}
