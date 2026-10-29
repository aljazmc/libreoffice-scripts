"""HSE Dashboard of Northgate Offshore Wind: the project and everything the
document could say. The typesetting keeps what fits into four pages, the
most important first."""

PROJECT = {
    "name": "Northgate Offshore Wind",
    "code": "NOW-1",
    "author": "Olu Adeyemi, HSE Manager",
}

MONTHS = ["Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep"]

DOCUMENT = {
    "title": "HSE Dashboard",
    "subtitle": "Health, safety and environment · September 2028 · "
                "offshore construction, month 6 of the campaign",
    "meta": [("Project", "NOW-1"), ("Month", "Sep 2028"),
             ("Hours worked", "412,000"), ("People offshore", "640 peak"),
             ("Owner", "Olu Adeyemi")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "charts": [{"type": "kpis",
         "tiles": [
             {"label": "LTIF", "value": "0.38", "status": "good",
              "note": "lost-time injuries per million h", "delta": "▼0.1",
              "delta_status": "good", "spark": [0.6, 0.55, 0.5, 0.45,
                                                0.48, 0.42, 0.38]},
             {"label": "TRIR", "value": "1.9", "status": "warn",
              "note": "recordable injuries per million h",
              "delta": "▲0.2", "delta_status": "bad"},
             {"label": "Days without LTI", "value": "87",
              "status": "good", "note": "since 4 June"},
             {"label": "Safety walks", "value": "142", "status": 0,
              "note": "by managers this month", "delta": "+18"},
         ]}]},
        {"heading": "Leading and lagging", "kind": "figure",
         "weight": 0.2, "height": {1: 165, 2: 170, 4: 185},
         "widths": [3, 2], "charts": [
             {"type": "bars", "title": "Observations and incidents",
              "subtitle": "per month", "categories": MONTHS,
              "values": False,
              "series": [{"name": "Safety observations", "color": 0,
                          "values": [120, 140, 135, 150, 180, 210, 260,
                                     320, 380, 410, 395, 430]},
                         {"name": "Near misses ×10", "color": "warn",
                          "values": [60, 50, 70, 40, 90, 110, 140, 150,
                                     180, 160, 170, 150]}]},
             {"type": "funnel", "title": "Safety pyramid", "subtitle":
              "this campaign", "shares": False, "power": 0.4,
              "stages": [("Lost-time injuries", 1, "bad"),
                         ("Recordable injuries", 5, "warn"),
                         ("First aid cases", 38, 1),
                         ("Near misses", 214, 0),
                         ("Observations", 3130, 3)]},
         ]},
        {"heading": "Incidents this month", "kind": "table",
         "weight": 0.3, "step": 0.1, "badges": {"High": "bad",
                                                 "Medium": "warn",
                                                 "Low": "good"},
         "columns": [("Date", 0.8), ("What happened", 3.6),
                     ("Potential", 0.9, "center"), ("Action", 2.4)],
         "rows": [
             ["3 Sep", "Dropped object: a 2 kg shackle fell 14 m on the "
              "heavy lift vessel deck; no one in the zone", "High",
              "Tool tethering audit of all lifting crews"],
             ["11 Sep", "Hand injury during sea fastening release; "
              "recordable, back at work next day", "Medium",
              "Task risk assessment revised"],
             ["19 Sep", "Hydraulic oil leak of 20 l from the jack-up "
              "crane, contained on deck", "Medium", "Hose inspection "
              "interval halved"],
             ["24 Sep", "Crew transfer in 1.7 m waves, over the limit",
              "High", "Stop work; masters re-briefed"],
         ]},
        {"heading": "Environment", "kind": "figure", "weight": 0.4,
         "min_pages": 2, "height": 155, "widths": [1, 1], "charts": [
             {"type": "line", "title": "Piling noise at 750 m",
              "subtitle": "dB SEL, limit 160", "zero": False,
              "format": "{:.0f}", "x": ["P41", "P45", "P49", "P53",
                                        "P57", "P61", "P65"],
              "target": 160, "target_label": "licence limit",
              "series": [{"name": "With bubble curtain",
                          "values": [152, 154, 151, 153, 156, 152,
                                     150]}]},
             {"type": "progress", "title": "Environmental controls",
              "format": "{:.0f} %", "items": [
                  {"label": "Marine mammal watches done", "value": 100,
                   "status": "good"},
                  {"label": "Soft starts on every pile", "value": 100,
                   "status": "good"},
                  {"label": "Waste segregated offshore", "value": 92,
                   "target": 95, "status": "warn"},
                  {"label": "Fuel use vs plan", "value": 104,
                   "display": "104 %", "target": 100, "max": 120,
                   "status": "warn"},
              ]},
         ]},
        {"heading": "Health", "kind": "bullets", "weight": 0.5,
         "step": 0.15, "min_pages": 2, "items": [
             "Fatigue: two crews worked more than 14 days offshore; the "
             "rotation rule of 14 on, 14 off is now enforced by the "
             "marine coordination centre.",
             "Seasickness on crew transfer vessels fell after the switch "
             "to the walk-to-work vessel for long shifts.",
             "Mental health first aiders now on every vessel with more "
             "than 30 people.",
         ]},
        {"heading": "By contractor", "kind": "figure", "weight": 0.7,
         "min_pages": 4, "height": 160, "charts": [{"type": "heatmap",
          "rows": ["Steelbridge (foundations)", "Baltic Cable",
                   "Nordvind (turbines)", "Marine services",
                   "Port and logistics"],
          "cols": ["Hours (k)", "LTI", "Recordables", "Near misses",
                   "Observations", "Audit score"],
          "values": [[148, 1, 2, 76, 980, 88], [96, 0, 1, 52, 760, 91],
                     [64, 0, 1, 31, 540, 94], [58, 0, 1, 34, 470, 86],
                     [46, 0, 0, 21, 380, 90]],
          "format": "{:.0f}", "color": 0, "labels": 0.28}]},
        {"heading": "Focus for October", "kind": "entries", "weight": 0.8,
         "step": 0.2, "inner": 0.1, "min_pages": 4, "entries": [
             {"title": "Dropped objects", "dates": "campaign",
              "text": ["Two high-potential dropped objects in two months. "
                       "Every crew does a tethering check before each "
                       "shift; zones under lifts are marked and "
                       "guarded."]},
             {"title": "Autumn weather", "dates": "from 1 Oct",
              "text": ["Transfer limits will be tested more often; "
                       "masters have full authority to stop and are "
                       "backed every time they do."]},
         ]},
        {"heading": "Audits", "kind": "figure", "weight": 0.9,
         "min_pages": 4, "height": 140, "widths": [3, 2], "charts": [
             {"type": "bars", "title": "Audit findings by month",
              "stacked": True,
              "categories": ["Apr", "May", "Jun", "Jul", "Aug", "Sep"],
              "series": [{"name": "Major", "color": "bad",
                          "values": [2, 1, 1, 0, 1, 0]},
                         {"name": "Minor", "color": "warn",
                          "values": [9, 11, 7, 6, 8, 5]},
                         {"name": "Observations", "color": 3,
                          "values": [14, 18, 16, 12, 15, 13]}]},
             {"type": "donut", "title": "Findings closed",
              "segments": [("On time", 71, "good"), ("Late", 12, "warn"),
                           ("Open", 9, "bad")],
              "center": ("92", "findings")},
         ]},
        {"heading": "Definitions", "kind": "tags", "weight": 1.0,
         "step": 0.1, "min_pages": 4, "items": [
             ("LTIF", "lost-time injuries per million hours worked"),
             ("TRIR", "recordable injuries (lost time, restricted work, "
                      "medical treatment) per million hours"),
             ("High potential", "an event that could have caused a "
                                "fatality or life-changing injury"),
         ]},
        {"heading": "Trend", "kind": "figure", "weight": 1.05,
         "min_pages": 4, "height": 165, "widths": [1, 1], "charts": [
             {"type": "line", "title": "Rolling 12-month frequency",
              "subtitle": "per million hours", "x": MONTHS,
              "format": "{:.1f}",
              "series": [{"name": "TRIR", "color": "warn",
                          "values": [2.6, 2.5, 2.4, 2.3, 2.1, 2.0, 1.9,
                                     1.8, 1.8, 1.7, 1.7, 1.9]},
                         {"name": "LTIF", "color": 0,
                          "values": [0.9, 0.85, 0.8, 0.7, 0.66, 0.6,
                                     0.55, 0.5, 0.45, 0.48, 0.42,
                                     0.38]}]},
             {"type": "bars", "title": "Hours worked", "subtitle":
              "thousands", "categories": MONTHS, "values": False,
              "series": [{"name": "Onshore", "color": 3,
                          "values": [80, 84, 70, 78, 82, 90, 96, 98, 96,
                                     92, 90, 88]},
                         {"name": "Offshore", "values": [10, 12, 8, 14,
                                                        40, 120, 210,
                                                        260, 300, 320,
                                                        318, 324]}],
              "stacked": True},
         ]},
        {"heading": "Training and competence", "kind": "figure",
         "weight": 1.1, "min_pages": 4, "height": 115, "charts": [{
             "type": "progress", "format": "{:.0f} %", "items": [
                 {"label": "Offshore survival (GWO) in date",
                  "value": 99, "target": 100, "status": "good"},
                 {"label": "Working at height in date", "value": 97,
                  "target": 100, "status": "good"},
                 {"label": "Lifting supervisors certified", "value": 88,
                  "target": 100, "status": "warn"},
                 {"label": "Site induction within 24 h of arrival",
                  "value": 100, "status": "good"},
             ]}]},
        {"heading": "Good catches", "kind": "bullets", "weight": 1.15,
         "step": 0.2, "min_pages": 4, "items": [
             "A deckhand on the cable vessel stopped a pull-in when he "
             "saw the winch wire fraying; the wire was replaced, no "
             "damage.",
             "A crane operator refused a lift in a gusting wind that the "
             "forecast had missed; the gust reached 21 m/s ten minutes "
             "later.",
             "The port team spotted a forklift with a disabled seat "
             "switch during the morning check.",
         ]},
    ],
}
