"""Cutover Runbook of St Brigid's EHR Migration: the project and everything the
document could say. The typesetting keeps what fits into one page, the most
important first."""

PROJECT = {
    "name": "St Brigid's EHR Migration",
    "code": "EHR-26",
    "author": "Dr Niamh Kelly, Clinical Programme Director",
}

HOURS = ["Fr 18", "20", "22", "Sa 00", "02", "04", "06", "08", "10", "12",
         "14", "16", "18", "20", "22", "Su 00", "02", "04", "06"]

DOCUMENT = {
    "title": "Cutover Runbook",
    "subtitle": "Go-live weekend · Friday 6 November 18:00 to Sunday "
                "8 November 08:00 · legacy PAS and paper to Meridian EHR",
    "meta": [("Programme", "EHR-26"), ("Cutover lead", "Marcus Byrne"),
             ("Clinical lead", "Dr Niamh Kelly"),
             ("Downtime", "18:00 Fri – 06:00 Sat"),
             ("Version", "Runbook v7 · final")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "height": {1: 285, 2: 300,
                                                       4: 320},
         "charts": [{"type": "gantt", "start": 0, "end": 38,
          "ticks": [(i * 2, h) for i, h in enumerate(HOURS)],
          "groups": ["Technical", "Data", "Clinical", "Go/no-go"],
          "labels": 0.22,
          "tasks": [
              {"label": "Freeze", "section": True, "start": 0, "end": 4},
              {"label": "Legacy PAS read-only", "start": 0, "end": 0.5},
              {"label": "Downtime procedures on wards", "start": 0,
               "end": 12, "group": 2, "text": "paper and downtime "
               "viewer"},
              {"label": "Final extract", "start": 0.5, "end": 3.5,
               "group": 1},
              {"label": "Load", "section": True, "start": 3.5, "end": 11},
              {"label": "Load patients, encounters, orders", "start": 3.5,
               "end": 8, "group": 1, "critical": True},
              {"label": "Reconciliation", "start": 8, "end": 10,
               "group": 1, "critical": True},
              {"label": "Go / no-go 1: data", "start": 10,
               "milestone": True, "text": "04:00 Sat"},
              {"label": "Switch-on", "section": True, "start": 10,
               "end": 16},
              {"label": "Interfaces on: lab, radiology, pharmacy",
               "start": 10, "end": 11.5, "critical": True},
              {"label": "Smoke tests by super users", "start": 11,
               "end": 12, "group": 2},
              {"label": "Go / no-go 2: clinical", "start": 12,
               "milestone": True, "text": "06:00 Sat · go live"},
              {"label": "Back-entry of paper records", "start": 12,
               "end": 20, "group": 2},
              {"label": "Stabilise", "section": True, "start": 12,
               "end": 38},
              {"label": "Command centre, 24/7", "start": 12, "end": 38,
               "group": 3, "text": "floor walkers on every ward"},
              {"label": "Go / no-go 3: rollback window closes",
               "start": 24, "milestone": True, "text": "18:00 Sat"},
          ], "deps": [(3, 5), (5, 6), (6, 7), (7, 9), (9, 11)]}]},
        {"heading": "Go / no-go criteria", "kind": "table", "weight": 0.3,
         "step": 0.12, "columns": [
             ("Checkpoint", 1.4), ("Criterion", 3.6), ("Owner", 1.2),
             ("If not met", 2.4)],
         "rows": [
             ["1 · Data, 04:00", "All patients with an active encounter "
              "loaded; reconciliation differences under 0.1 %",
              "Data lead", "Extend load by 1 h; then roll back"],
             ["1 · Data, 04:00", "Allergies and medications match for "
              "100 % of 500 sampled inpatients", "Chief pharmacist",
              "Fix in place if under 5 records; else roll back"],
             ["2 · Clinical, 06:00", "Lab, radiology and pharmacy "
              "interfaces pass the smoke tests", "Integration lead",
              "Stay on paper for that service"],
             ["2 · Clinical, 06:00", "Super users sign off on every "
              "ward", "Clinical lead", "Ward stays on downtime "
              "procedures"],
             ["3 · Rollback, 18:00", "No unresolved patient safety "
              "incident caused by the system", "Medical director",
              "Roll back to PAS, back-enter on paper"],
         ]},
        {"heading": "Roles in the command centre", "kind": "figure",
         "weight": 0.5, "min_pages": 2, "charts": [{"type": "tree",
          "root": {"label": "Cutover lead", "note": "Marcus Byrne, "
                   "decides go/no-go with the clinical lead",
                   "children": [
              {"label": "Technical bridge", "note": "room 2.14",
               "children": [
                   {"label": "Infrastructure on call"},
                   {"label": "Integration engineers × 3"},
                   {"label": "Vendor team, remote"}]},
              {"label": "Data team", "note": "room 2.16", "children": [
                  {"label": "Migration lead"},
                  {"label": "Reconciliation analysts × 4"},
                  {"label": "Chief pharmacist on site"}]},
              {"label": "Clinical command", "note": "room 2.10",
               "children": [
                   {"label": "Clinical lead"},
                   {"label": "Super users, 2 per ward"},
                   {"label": "Patient safety officer",
                    "status": "bad"}]},
              {"label": "Communications", "note": "room 2.10",
               "children": [
                   {"label": "Hourly bulletin to all staff"},
                   {"label": "Switchboard script"}]},
          ]}}]},
        {"heading": "Downtime procedures", "kind": "bullets",
         "weight": 0.6, "step": 0.15, "min_pages": 2, "items": [
             "From 18:00 Friday every ward works on paper: the downtime "
             "packs are in the blue boxes at each nurses' station.",
             "Results are phoned to wards by the lab and printed on the "
             "ward printer; radiology reports by fax.",
             "Medication charts printed at 17:00 Friday from the legacy "
             "system are the source of truth until back-entry.",
             "Emergency department uses the downtime viewer for history "
             "(read-only copy refreshed at 17:45).",
         ]},
        {"heading": "Step by step", "kind": "table", "weight": 0.8,
         "step": 0.06, "min_pages": 4, "badges": {"Critical": "bad",
                                                 "Check": "warn"},
         "columns": [("Time", 0.9), ("Step", 4), ("Who", 1.5),
                     ("Type", 0.9, "center")],
         "rows": [
             ["18:00", "Announce downtime on all channels; PAS read-only",
              "Comms, infra", "Check"],
             ["18:15", "Last legacy backup verified and copied off site",
              "Infrastructure", "Critical"],
             ["18:30", "Final extract starts: patients, encounters, "
              "orders, results", "Data team", "Critical"],
             ["21:30", "Extract counts checked against legacy reports",
              "Data team", "Check"],
             ["21:30", "Load into Meridian production", "Vendor, data",
              "Critical"],
             ["02:00", "Automated reconciliation and 500-patient sample",
              "Analysts, pharmacy", "Check"],
             ["04:00", "Go / no-go 1", "Cutover lead", "Critical"],
             ["04:15", "Interfaces switched on, queued messages released",
              "Integration", "Critical"],
             ["05:00", "Smoke tests: admit, order, result, prescribe, "
              "discharge", "Super users", "Check"],
             ["06:00", "Go / no-go 2; system live", "Cutover and "
              "clinical leads", "Critical"],
             ["06:00", "Back-entry of paper records starts, ED first",
              "Ward clerks", "Check"],
             ["18:00", "Go / no-go 3; rollback window closes",
              "Medical director", "Critical"],
         ]},
        {"heading": "Rollback", "kind": "entries", "weight": 0.9,
         "step": 0.2, "inner": 0.1, "min_pages": 4, "entries": [
             {"title": "Before 06:00 Saturday", "dates": "2 hours",
              "text": ["PAS is switched back to read-write; nothing was "
                       "entered in Meridian, so no back-entry is "
                       "needed."]},
             {"title": "06:00 to 18:00 Saturday", "dates": "4 hours",
              "text": ["Meridian is frozen; everything entered since "
                       "06:00 is printed by ward and back-entered in "
                       "PAS by the clerks."]},
             {"title": "After 18:00 Saturday", "dates": "no rollback",
              "text": ["We fix forward. The vendor's priority support "
                       "is on site until Friday 13 November."]},
         ]},
        {"heading": "Readiness at T−1", "kind": "figure", "weight": 1.0,
         "min_pages": 4, "height": 120, "charts": [{"type": "progress",
          "format": "{:.0f} %", "items": [
              {"label": "Dress rehearsal 2 completed", "value": 100,
               "status": "good"},
              {"label": "Staff trained", "value": 94, "target": 90,
               "status": "good"},
              {"label": "Downtime packs on wards", "value": 100,
               "status": "good"},
              {"label": "Interfaces tested end to end", "value": 88,
               "target": 100, "status": "warn"},
          ]}]},
        {"heading": "Contacts", "kind": "tags", "weight": 1.2, "step": 0.1,
         "min_pages": 4, "items": [
             ("Command centre", "ext. 4400, room 2.10"),
             ("Technical bridge", "ext. 4410, dial-in 0800 555 0199"),
             ("Vendor escalation", "Meridian Health, 24/7 line"),
             ("Patient safety", "bleep 2121"),
         ]},
    ],
}
