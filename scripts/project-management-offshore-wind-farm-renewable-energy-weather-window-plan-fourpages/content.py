"""Weather Window Plan of Northgate Offshore Wind: the project and everything
the document could say. The typesetting keeps what fits into four pages, the
most important first."""

PROJECT = {
    "name": "Northgate Offshore Wind",
    "code": "NOW-1",
    "author": "Lars Henriksen, Offshore Installation Manager",
}

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
          "Oct", "Nov", "Dec"]

DOCUMENT = {
    "title": "Weather Window Plan",
    "subtitle": "When the sea lets us work: workability and the offshore "
                "installation campaign for 2028 and 2029",
    "meta": [("Project", "NOW-1"), ("Data", "22 years of hindcast"),
             ("Vessels", "5 main"), ("Campaign", "Apr 2028 – Oct 2029"),
             ("Owner", "Lars Henriksen")],
    "sections": [
        {"heading": "Workability by month", "kind": "figure",
         "weight": 0.1, "height": {1: 170, 2: 180, 4: 190}, "charts": [{
             "type": "heatmap", "rows": ["Jack-up, turbines (Hs 2.0 m, "
                                         "wind 12 m/s)",
                                         "Heavy lift, monopiles (Hs 1.5 m)",
                                         "Cable lay (Hs 2.5 m)",
                                         "Crew transfer (Hs 1.5 m)",
                                         "Walk-to-work vessel (Hs 3.0 m)"],
             "cols": MONTHS,
             "values": [[22, 28, 41, 62, 74, 81, 84, 80, 61, 42, 27, 20],
                        [14, 19, 30, 51, 66, 74, 78, 72, 50, 31, 18, 12],
                        [35, 40, 55, 72, 83, 88, 90, 87, 73, 56, 39, 33],
                        [16, 22, 33, 54, 68, 75, 79, 74, 53, 35, 21, 15],
                        [48, 54, 66, 80, 89, 92, 94, 92, 82, 68, 52, 46]],
             "thresholds": [(0, "bad"), (40, "warn"), (65, "good")],
             "format": "{:.0f}%", "labels": 0.32}]},
        {"heading": "Campaign", "kind": "figure", "weight": 0.2,
         "height": {1: 150, 2: 170, 4: 185}, "charts": [{"type": "gantt",
          "columns": ["Q2 28", "Q3", "Q4", "Q1 29", "Q2", "Q3", "Q4"],
          "groups": ["Foundations", "Cables", "Turbines", "Commission"],
          "tasks": [
              {"label": "UXO clearance and boulders", "start": 0,
               "end": 0.8},
              {"label": "Monopiles, 80 + 2", "start": 0.5, "end": 2.4,
               "critical": True, "text": "heavy lift vessel"},
              {"label": "Winter: no heavy lift", "start": 2.6, "end": 3.9,
               "group": 4, "text": "workability under 30 %"},
              {"label": "Export cables", "start": 1, "end": 2.2,
               "group": 1},
              {"label": "Array cables", "start": 1.5, "end": 4.6,
               "group": 1},
              {"label": "Turbines, 80", "start": 3.8, "end": 6.4,
               "group": 2, "critical": True, "text": "two jack-ups"},
              {"label": "Commissioning", "start": 4.2, "end": 6.9,
               "group": 3},
              {"label": "First power", "start": 4.4, "milestone": True},
          ]}]},
        {"heading": "Limits by operation", "kind": "table", "weight": 0.3,
         "step": 0.1, "columns": [("Operation", 2.6), ("Vessel", 1.8),
                                  ("Wave Hs", 0.9, "center"),
                                  ("Wind", 0.9, "center"),
                                  ("Duration", 1, "center")],
         "rows": [
             ["Monopile lift and pile", "Heavy lift vessel", "1.5 m",
              "15 m/s", "28 h"],
             ["Transition piece", "Heavy lift vessel", "1.5 m", "15 m/s",
              "12 h"],
             ["Export cable lay", "Cable lay vessel", "2.5 m", "20 m/s",
              "6 days"],
             ["Array cable lay and burial", "Cable lay vessel", "2.5 m",
              "20 m/s", "18 h"],
             ["Turbine install", "Jack-up", "2.0 m", "12 m/s", "36 h"],
             ["Technician transfer", "Crew transfer vessel", "1.5 m",
              "18 m/s", "1 h"],
         ]},
        {"heading": "Expected waiting on weather", "kind": "figure",
         "weight": 0.5, "min_pages": 2, "height": 165, "widths": [3, 2],
         "charts": [
             {"type": "bars", "title": "Days by operation",
              "stacked": True, "subtitle": "P50",
              "categories": ["Monopiles", "Transition pieces",
                             "Export cable", "Array cable", "Turbines"],
              "series": [{"name": "Working", "values": [96, 42, 30, 74,
                                                        120]},
                         {"name": "Waiting on weather", "color": "bad",
                          "values": [41, 16, 9, 22, 58]}],
              "inside": True},
             {"type": "donut", "title": "Campaign days", "center":
              ("508", "days, P50"),
              "segments": [("Working", 362, 0), ("Weather", 146, "bad")]},
         ]},
        {"heading": "Why this sequence", "kind": "text", "weight": 0.6,
         "step": 0.3, "min_pages": 2, "paragraphs": [
             "Monopiles go in during the 2028 summer, when the heavy lift "
             "vessel can work three days out of four. Starting them in "
             "April gives a month of buffer before the September decline; "
             "every pile left for 2029 costs €1.4m in a second "
             "mobilisation.",
             "Turbines are installed from March 2029 with two jack-ups "
             "working in parallel, so that the slow months are spent on "
             "the turbines nearest the port.",
         ]},
        {"heading": "Weather risk", "kind": "figure", "weight": 0.8,
         "min_pages": 4, "height": 160, "charts": [{"type": "line",
          "title": "Monopiles installed, 2028", "subtitle": "of 82, by "
          "week, P10 / P50 / P90 weather",
          "x": ["W14", "W18", "W22", "W26", "W30", "W34", "W38", "W42",
                "W46"],
          "target": 82, "target_label": "all piles",
          "series": [{"name": "P10", "color": "good", "dash": True,
                      "values": [0, 6, 18, 33, 49, 64, 77, 82, 82]},
                     {"name": "P50", "values": [0, 5, 15, 28, 42, 56, 68,
                                                78, 82]},
                     {"name": "P90", "color": "bad", "dash": True,
                      "values": [0, 3, 11, 22, 34, 46, 57, 66, 72]}]}]},
        {"heading": "Contingency", "kind": "entries", "weight": 0.9,
         "step": 0.2, "inner": 0.1, "min_pages": 4, "entries": [
             {"title": "Monopiles left over at the end of 2028",
              "text": ["If more than 6 piles remain on 1 October, the "
                       "heavy lift vessel stays for October on a day "
                       "rate of €310k; above 15, they move to April "
                       "2029."]},
             {"title": "Second jack-up in 2029", "text": [
                 "An option for a second jack-up from June 2029 recovers "
                 "up to six weeks of turbine installation."]},
             {"title": "Cable faults", "text": [
                 "Spare export cable of 3 km stored at the port; repair "
                 "vessel on a call-off contract."]},
         ]},
        {"heading": "Vessel spread", "kind": "table", "weight": 1.0,
         "step": 0.1, "min_pages": 4,
         "columns": [("Vessel", 2), ("Type", 2), ("On site", 2),
                     ("Day rate", 1, "end")],
         "rows": [
             ["Orion Lift", "Heavy lift, 5,000 t", "Apr – Sep 2028",
              "€310k"],
             ["Nexus Layer", "Cable lay", "Jun 2028 – May 2029",
              "€140k"],
             ["Seajack Tern", "Jack-up", "Mar – Oct 2029", "€220k"],
             ["Seajack Gull", "Jack-up (option)", "Jun – Sep 2029",
              "€230k"],
             ["Northgate W2W", "Walk-to-work", "Jan 2029 onward", "€38k"],
         ]},
        {"heading": "Forecasting on site", "kind": "bullets",
         "weight": 1.1, "step": 0.2, "min_pages": 4, "items": [
             "Site-specific forecasts four times a day from two "
             "providers, checked against the wave buoy at the centre "
             "of the site.",
             "Go / no-go for every lift at 18:00 the day before, by the "
             "marine coordinator and the vessel master.",
             "Weather downtime logged by the hour for the contractual "
             "weather risk sharing.",
         ]},
        {"heading": "Wave climate", "kind": "figure", "weight": 1.2,
         "min_pages": 4, "height": 150, "charts": [{"type": "line",
          "title": "Significant wave height", "subtitle": "m, monthly "
          "mean and 90th percentile", "x": MONTHS, "format": "{:.1f}",
          "series": [{"name": "Mean", "area": True,
                      "values": [2.4, 2.2, 1.9, 1.5, 1.2, 1.0, 0.9, 1.0,
                                 1.4, 1.8, 2.2, 2.5]},
                     {"name": "90th percentile", "color": 1, "dash": True,
                      "values": [3.9, 3.6, 3.2, 2.6, 2.1, 1.8, 1.6, 1.8,
                                 2.5, 3.1, 3.6, 4.0]}],
          "target": 1.5, "target_label": "heavy lift limit"}]},
        {"heading": "Turbine installation rate", "kind": "figure",
         "weight": 1.25, "min_pages": 4, "height": 160, "widths": [3, 2],
         "charts": [
             {"type": "bars", "title": "Turbines installed per month, "
              "2029", "subtitle": "P50",
              "categories": ["Mar", "Apr", "May", "Jun", "Jul", "Aug",
                             "Sep", "Oct"],
              "series": [{"name": "Jack-up 1", "values": [4, 6, 8, 9, 9,
                                                         9, 7, 4]},
                         {"name": "Jack-up 2 (option)", "color": 1,
                          "values": [0, 0, 0, 6, 8, 8, 2, 0]}],
              "stacked": True},
             {"type": "progress", "title": "Weather risk owned",
              "format": "{:.0f} %", "items": [
                  {"label": "Us (owner)", "value": 60, "status": 0},
                  {"label": "Foundation contractor", "value": 25,
                   "status": 1},
                  {"label": "Turbine contractor", "value": 15,
                   "status": 3},
              ]},
         ]},
        {"heading": "Port", "kind": "text", "weight": 1.3, "step": 0.3,
         "min_pages": 4, "paragraphs": [
             "All components are marshalled in Eastport, 70 nautical "
             "miles from the site: ten hours for the jack-up in good "
             "weather. The port can store 24 monopiles and 16 turbine "
             "sets; the plan keeps two vessel loads ready at all times "
             "so that no window is lost waiting for components.",
         ]},
    ],
}
