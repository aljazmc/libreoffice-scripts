"""Data Migration Report of St Brigid's EHR Migration: the project and
everything the document could say. The typesetting keeps what fits into two
pages, the most important first."""

PROJECT = {
    "name": "St Brigid's EHR Migration",
    "code": "EHR-26",
    "author": "Owen Fitzgerald, Data Migration Lead",
}

DOCUMENT = {
    "title": "Data Migration Report",
    "subtitle": "Trial load 3 · 19 – 20 September 2026 · legacy PAS, "
                "LabLink and ePharm to Meridian EHR",
    "meta": [("Programme", "EHR-26"), ("Load", "Trial 3 of 3"),
             ("Records", "41.2 million"), ("Duration", "11 h 12 min"),
             ("Result", "Pass, 4 actions")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "charts": [{"type": "kpis",
         "tiles": [
             {"label": "Loaded", "value": "99.69 %", "status": "good",
              "delta": "+0.6", "note": "of in-scope records"},
             {"label": "Rejected", "value": "128k", "status": "warn",
              "delta": "▼ 61 %", "delta_status": "good",
              "note": "fixed in source or mapped"},
             {"label": "Clinical sample", "value": "498 / 500",
              "status": "good", "note": "patients matched exactly"},
             {"label": "Load time", "value": "11.2 h", "status": "warn",
              "note": "window is 10 h"},
         ]}]},
        {"heading": "From extract to record", "kind": "figure",
         "weight": 0.2, "height": {1: 120, 2: 125, 4: 135},
         "charts": [{"type": "funnel", "format": "{:,.1f}m",
          "stages": [("Extracted from legacy", 52.4),
                     ("In scope (last 8 years, active)", 41.2),
                     ("Passed validation", 41.07),
                     ("Loaded", 41.07),
                     ("Reconciled", 41.03)], "power": 3}]},
        {"heading": "By domain", "kind": "table", "weight": 0.3,
         "step": 0.1, "badges": {"Pass": "good", "Watch": "warn",
                                 "Fail": "bad"},
         "columns": [("Domain", 2), ("Records", 1.2, "end"),
                     ("Loaded", 1, "end"), ("Rejected", 1, "end"),
                     ("Result", 0.9, "center")],
         "rows": [
             ["Patients and demographics", "612,400", "100.00 %", "12",
              "Pass"],
             ["Encounters", "8,941,000", "99.92 %", "7,150", "Pass"],
             ["Lab results", "24,300,000", "99.71 %", "70,400", "Watch"],
             ["Radiology reports", "2,180,000", "99.98 %", "440", "Pass"],
             ["Medications", "3,920,000", "99.12 %", "34,500", "Watch"],
             ["Allergies", "211,000", "99.99 %", "21", "Pass"],
             ["Problems and diagnoses", "1,030,000", "98.90 %", "11,300",
              "Watch"],
             ["Scanned documents (index)", "5,600", "100.00 %", "0",
              "Pass"],
         ]},
        {"heading": "Errors by type", "kind": "figure", "weight": 0.4,
         "min_pages": 2, "height": 165, "widths": [2, 3], "charts": [
             {"type": "donut", "title": "Rejected records",
              "format": "{:,.0f}k", "center": ("128k", "rejected"),
              "segments": [("Unmapped lab code", 61),
                           ("Free-text dose", 31),
                           ("Retired diagnosis code", 11),
                           ("Missing encounter", 7),
                           ("Other", 18)]},
             {"type": "bars", "title": "Rejected by trial load",
              "subtitle": "thousands", "stacked": True,
              "categories": ["Trial 1", "Trial 2", "Trial 3"],
              "series": [{"name": "Lab", "values": [210, 120, 70]},
                         {"name": "Medication", "values": [90, 62, 35]},
                         {"name": "Problems", "values": [21, 15, 11]},
                         {"name": "Other", "color": 4,
                          "values": [11, 9, 12]}]},
         ]},
        {"heading": "Clinical validation", "kind": "text", "weight": 0.5,
         "step": 0.3, "min_pages": 2, "paragraphs": [
             "Twelve clinicians compared 500 randomly chosen inpatients "
             "side by side in the legacy systems and in Meridian: "
             "allergies, active medications, problems, the last three "
             "results and the last discharge letter. **498 matched "
             "exactly.** In two patients a free-text dose ('as "
             "directed') was loaded as a blank; both are fixed by the "
             "new mapping rule M-114.",
             "Pharmacy reviewed every one of the 34,500 rejected "
             "medication records: 96 % are for courses that ended more "
             "than a year ago and will be viewable in the legacy archive.",
         ]},
        {"heading": "Load times", "kind": "figure", "weight": 0.6,
         "min_pages": 2, "height": 150, "charts": [{"type": "gantt",
          "start": 0, "end": 12,
          "ticks": [(h, f"{h} h") for h in range(0, 13, 2)],
          "groups": ["Extract", "Transform", "Load", "Reconcile"],
          "tasks": [
              {"label": "Patients", "start": 0, "end": 0.6},
              {"label": "Encounters", "start": 0.4, "end": 3.1,
               "group": 1},
              {"label": "Lab results", "start": 1.0, "end": 8.2,
               "group": 2, "critical": True, "text": "7.2 h"},
              {"label": "Medications", "start": 3.1, "end": 6.0,
               "group": 2},
              {"label": "Problems", "start": 6.0, "end": 7.1,
               "group": 2},
              {"label": "Reconciliation", "start": 8.2, "end": 11.2,
               "group": 3, "text": "3.0 h"},
              {"label": "Window ends", "start": 10, "milestone": True,
               "text": "10 h"},
          ]}]},
        {"heading": "Actions before the dress rehearsal", "kind":
         "entries", "weight": 0.7, "step": 0.2, "inner": 0.1,
         "min_pages": 2, "entries": [
             {"title": "Parallel load of lab results", "dates": "Data "
              "team · 2 Oct", "text": [
                  "Split the lab load into four streams by year; tested "
                  "at 4.1 h instead of 7.2 h."]},
             {"title": "Map the remaining 212 local lab codes",
              "dates": "Lab · 30 Sep", "text": [
                  "Most are retired tests; each one is mapped or "
                  "archived with the agreement of the lab manager."]},
             {"title": "Free-text doses", "dates": "Pharmacy · 30 Sep",
              "text": [
                  "Rule M-114: free-text doses load as a comment on the "
                  "order and are flagged for review on first "
                  "prescribing."]},
             {"title": "Retired diagnosis codes", "dates": "Coding · "
              "7 Oct", "text": [
                  "Mapped to their current equivalent; 11,300 records."]},
         ]},
        {"heading": "Trend across trial loads", "kind": "figure",
         "weight": 0.9, "min_pages": 4, "height": 155, "widths": [1, 1],
         "charts": [
             {"type": "line", "title": "Records rejected",
              "subtitle": "% of in-scope", "format": "{:.2f}",
              "x": ["Trial 1", "Trial 2", "Trial 3", "Dress 1",
                    "Dress 2"],
              "target": 0.1, "target_label": "go threshold",
              "series": [
                  {"name": "Actual", "values": [0.81, 0.50, 0.31, None,
                                                None]},
                  {"name": "Forecast", "dash": True, "color": 1,
                   "values": [None, None, 0.31, 0.12, 0.08]}]},
             {"type": "bars", "title": "Load time", "subtitle": "hours",
              "format": "{:.1f}", "target": 10, "target_label": "window",
              "categories": ["Trial 1", "Trial 2", "Trial 3", "Dress 1",
                             "Dress 2"],
              "series": [{"name": "Hours", "values": [16.5, 13.0, 11.2,
                                                      8.5, 8.0],
                          "colors": ["bad", "bad", "warn", 4, 4]}]},
         ]},
        {"heading": "What stays in the legacy archive", "kind": "bullets",
         "weight": 1.0, "step": 0.2, "min_pages": 4, "items": [
             "Encounters older than eight years and patients with no "
             "activity since 2018 (9.6 million records).",
             "Lab results of retired tests that cannot be mapped.",
             "Scanned paper notes from before 2015: indexed in Meridian, "
             "opened in the archive viewer with one click.",
             "Audit trails of the legacy systems, kept for 25 years.",
         ]},
        {"heading": "Sign-off", "kind": "table", "weight": 1.1, "step": 0.1,
         "min_pages": 4, "badges": {"Signed": "good", "Pending": "warn"},
         "columns": [("Role", 2), ("Name", 2), ("Status", 1, "center")],
         "rows": [
             ["Chief clinical information officer", "Dr Aoife Ryan",
              "Signed"],
             ["Chief pharmacist", "Seán Walsh", "Signed"],
             ["Laboratory manager", "Dr Ruth Nolan", "Pending"],
             ["Head of health records", "Bríd Murphy", "Signed"],
             ["Data protection officer", "Ciara Lynch", "Signed"],
         ]},
        {"heading": "Reconciliation method", "kind": "text",
         "weight": 1.3, "step": 0.3, "min_pages": 4, "paragraphs": [
             "Every domain is reconciled three ways: counts per table "
             "and per year; checksums on key fields (patient number, "
             "dates, codes, values); and the 500-patient clinical "
             "sample. A difference is any record that fails one of the "
             "three; the threshold for go-live is 0.1 % per domain and "
             "zero for allergies.",
         ]},
        {"heading": "Quality by source system", "kind": "figure",
         "weight": 0.95, "min_pages": 4, "height": 140, "widths": [3, 2],
         "charts": [
             {"type": "heatmap", "title": "Records passing each check",
              "subtitle": "%", "rows": ["PAS", "LabLink", "ePharm",
                                        "RadNet", "Theatre system"],
              "cols": ["Complete", "Valid codes", "Dates", "Linked to "
                       "patient", "No duplicates"],
              "values": [[99.9, 99.8, 99.9, 100, 99.2],
                         [99.6, 98.9, 99.9, 99.8, 99.9],
                         [98.8, 99.1, 99.6, 99.9, 99.7],
                         [99.9, 99.9, 99.9, 99.9, 100],
                         [97.5, 98.2, 99.0, 99.6, 99.8]],
              "thresholds": [(0, "bad"), (99, "warn"), (99.5, "good")],
              "format": "{:.1f}"},
             {"type": "donut", "title": "Duplicate patients",
              "segments": [("Merged automatically", 3120, "good"),
                           ("Merged by records team", 860, 0),
                           ("Kept apart, different people", 210, 4)],
              "center": ("4,190", "pairs found"), "format": "{:,.0f}"},
         ]},
        {"heading": "Road to go-live", "kind": "figure", "weight": 0.97,
         "min_pages": 4, "charts": [{"type": "chevrons", "steps": [
             {"label": "Trial 1", "status": "done", "sub": "June · "
              "0.81 % rejected"},
             {"label": "Trial 2", "status": "done", "sub": "August · "
              "0.50 %"},
             {"label": "Trial 3", "status": "done", "sub": "September · "
              "0.31 %"},
             {"label": "Dress rehearsals", "status": "now",
              "sub": "October · full timing, real staff"},
             {"label": "Cutover", "sub": "6 November"},
         ]}]},
        {"heading": "Who checks what", "kind": "table", "weight": 1.05,
         "step": 0.1, "min_pages": 4,
         "columns": [("Check", 2.6), ("By", 2), ("When", 1.6)],
         "rows": [
             ["Counts per table and per year", "Data analysts",
              "During the load, automated"],
             ["Checksums on key fields", "Data analysts",
              "After each domain"],
             ["500-patient clinical sample", "12 clinicians",
              "Before go / no-go 1"],
             ["Medication and allergy sample", "Chief pharmacist",
              "Before go / no-go 1"],
             ["Spot checks on the wards", "Super users",
              "After go-live, first 48 hours"],
         ]},
    ],
}
