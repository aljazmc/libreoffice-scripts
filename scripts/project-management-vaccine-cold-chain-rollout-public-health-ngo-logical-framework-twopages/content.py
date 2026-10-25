"""Logical Framework of Cold Chain for Every Child: the project and everything
the document could say. The typesetting keeps what fits into two pages, the
most important first."""

PROJECT = {
    "name": "Cold Chain for Every Child",
    "code": "CCEC",
    "author": "Amani Mwangi, Programme Manager",
}

DOCUMENT = {
    "title": "Logical Framework",
    "subtitle": "Solar cold chain and outreach for routine immunisation in "
                "four districts · 2025 – 2028",
    "meta": [("Programme", "CCEC"), ("Districts", "4"),
             ("Budget", "US$ 6.8m"), ("Period", "Jan 2025 – Dec 2028"),
             ("Version", "Logframe v3")],
    "sections": [
        {"heading": "Theory of change", "kind": "figure", "weight": 0.1,
         "charts": [{"type": "chevrons", "steps": [
             {"label": "Inputs", "status": "done",
              "sub": "Solar fridges, motorbikes, training, data "
                     "system, US$ 6.8m"},
             {"label": "Activities", "status": "done",
              "sub": "Install, train, run outreach, monitor "
                     "temperatures"},
             {"label": "Outputs", "status": "now",
              "sub": "Working cold chain in 212 facilities; 640 "
                     "outreach sessions a month"},
             {"label": "Outcome", "status": "now",
              "sub": "More children fully immunised, fewer doses "
                     "wasted"},
             {"label": "Goal", "sub": "Fewer children die of "
                                     "vaccine-preventable disease"},
         ]}]},
        {"heading": "The framework", "kind": "table", "weight": 0.2,
         "step": 0.05, "columns": [("Level", 1), ("Summary", 2.4),
                                   ("Indicator", 2.4),
                                   ("Baseline", 0.8, "center"),
                                   ("Target", 0.8, "center")],
         "rows": [
             ["Goal", "Reduced under-five deaths from measles, "
              "pneumonia and diarrhoea", "Under-five mortality per "
              "1,000 live births", "68", "55"],
             ["Outcome", "Children in the four districts are fully "
              "immunised by their first birthday", "Children 12 – 23 "
              "months fully immunised", "58 %", "85 %"],
             ["Outcome", "", "Gap in coverage between the richest and "
              "poorest wards", "31 pts", "10 pts"],
             ["Output 1", "Every health facility stores vaccines safely",
              "Facilities with a working solar fridge", "34 %", "95 %"],
             ["Output 1", "", "Fridges with no temperature alarm in the "
              "month", "41 %", "90 %"],
             ["Output 2", "Outreach reaches remote villages every "
              "month", "Planned outreach sessions held", "52 %", "90 %"],
             ["Output 3", "Health workers plan and track with data",
              "Facilities reporting stock and coverage on time",
              "47 %", "90 %"],
             ["Output 4", "Communities ask for vaccination",
              "Caregivers who know the schedule", "39 %", "75 %"],
         ]},
        {"heading": "Where we are against targets", "kind": "figure",
         "weight": 0.3, "height": {1: 150, 2: 165, 4: 175},
         "charts": [{"type": "progress", "format": "{:.0f} %",
          "items": [
              {"label": "Fully immunised children", "value": 71,
               "target": 85, "status": "warn",
               "note": "baseline 58 %"},
              {"label": "Facilities with a working fridge", "value": 88,
               "target": 95, "status": "good", "note": "baseline 34 %"},
              {"label": "Fridges with no alarm", "value": 79,
               "target": 90, "status": "warn", "note": "baseline 41 %"},
              {"label": "Outreach sessions held", "value": 82,
               "target": 90, "status": "warn", "note": "baseline 52 %"},
              {"label": "On-time reporting", "value": 91, "target": 90,
               "status": "good", "note": "baseline 47 %"},
              {"label": "Caregivers who know the schedule", "value": 58,
               "target": 75, "status": "bad", "note": "baseline 39 %"},
          ]}]},
        {"heading": "Assumptions", "kind": "bullets", "weight": 0.4,
         "step": 0.15, "items": [
             "The national vaccine supply reaches district stores on "
             "time at least nine months in ten.",
             "Health workers stay in post; turnover below 15 % a year.",
             "Roads to the most remote facilities stay passable by "
             "motorbike outside the long rains.",
             "No major outbreak diverts the district teams for more than "
             "a month.",
         ]},
        {"heading": "Means of verification", "kind": "table",
         "weight": 0.5, "step": 0.1, "min_pages": 2,
         "columns": [("Indicator", 2.6), ("Source", 2.2),
                     ("How often", 1.1), ("Who", 1.3)],
         "rows": [
             ["Fully immunised children", "Coverage survey with "
              "cards and recall", "Year 0, 2, 4", "Independent firm"],
             ["Working fridges", "Remote temperature monitors",
              "Live", "Cold chain officer"],
             ["Outreach sessions", "Session reports in the data "
              "system", "Monthly", "District M&E officer"],
             ["On-time reporting", "Data system timestamps", "Monthly",
              "District M&E officer"],
             ["Caregiver knowledge", "Household survey", "Yearly",
              "Community health team"],
         ]},
        {"heading": "Activities and inputs", "kind": "entries",
         "weight": 0.6, "step": 0.2, "inner": 0.1, "min_pages": 2,
         "entries": [
             {"title": "Output 1 · Safe storage", "dates": "US$ 3.1m",
              "items": [
                  "Install 212 solar direct-drive fridges with remote "
                  "temperature monitors.",
                  "Train two staff per facility in daily checks and "
                  "basic repair.",
                  "Four district technicians on motorbikes."]},
             {"title": "Output 2 · Outreach", "dates": "US$ 1.6m",
              "items": [
                  "120 motorbikes and fuel for monthly outreach.",
                  "Cold boxes and vaccine carriers for every session."]},
             {"title": "Output 3 · Data", "dates": "US$ 0.9m",
              "items": [
                  "Tablets and the electronic immunisation registry.",
                  "Monthly data review meetings in each district."]},
             {"title": "Output 4 · Demand", "dates": "US$ 0.6m",
              "items": [
                  "Community health workers trained in counselling.",
                  "Radio spots and SMS reminders in two languages."]},
         ]},
        {"heading": "Budget by output", "kind": "figure", "weight": 0.8,
         "min_pages": 4, "height": 150, "widths": [2, 3], "charts": [
             {"type": "donut", "format": "US$ {:.1f}m",
              "center": ("$6.8m", "four years"),
              "segments": [("Safe storage", 3.1), ("Outreach", 1.6),
                           ("Data", 0.9), ("Demand", 0.6),
                           ("Management and M&E", 0.6)]},
             {"type": "bars", "title": "Spend by year", "subtitle":
              "US$ m", "stacked": True, "format": "{:.1f}",
              "categories": ["2025", "2026", "2027", "2028"],
              "series": [{"name": "Storage", "values": [1.9, 0.8, 0.2,
                                                        0.2]},
                         {"name": "Outreach", "values": [0.5, 0.4, 0.4,
                                                         0.3]},
                         {"name": "Data", "values": [0.4, 0.2, 0.2,
                                                     0.1]},
                         {"name": "Demand and other", "color": 4,
                          "values": [0.3, 0.3, 0.3, 0.3]}]},
         ]},
        {"heading": "Targets by year", "kind": "figure", "weight": 0.9,
         "min_pages": 4, "height": 155, "charts": [{"type": "line",
          "title": "Children fully immunised", "subtitle": "%",
          "x": ["2024", "2025", "2026", "2027", "2028"], "zero": False,
          "format": "{:.0f}", "end_labels": True,
          "series": [{"name": "Target", "dash": True, "color": 4,
                      "values": [58, 64, 72, 79, 85]},
                     {"name": "Actual", "values": [58, 66, 71, None,
                                                   None]}]}]},
        {"heading": "Risks to the logic", "kind": "table", "weight": 1.0,
         "step": 0.1, "min_pages": 4, "badges": {"High": "bad",
                                                "Medium": "warn",
                                                "Low": "good"},
         "columns": [("If this assumption fails", 3.4),
                     ("Likelihood", 1, "center"), ("We would", 3)],
         "rows": [
             ["Vaccine stock-outs at the district", "Medium",
              "Borrow from neighbouring districts under the regional "
              "agreement"],
             ["Health workers leave", "High", "Train three per "
              "facility, not two; refresher every six months"],
             ["Long rains close roads", "Medium", "Front-load outreach "
              "in the dry months"],
             ["Outbreak response", "Low", "Use the cold chain for the "
              "response; resume outreach within six weeks"],
         ]},
        {"heading": "Sustainability", "kind": "text", "weight": 1.1,
         "step": 0.3, "min_pages": 4, "paragraphs": [
             "Solar fridges have no running cost and a 15-year life. From "
             "2027 the district health budgets take over fuel and "
             "maintenance, starting at 25 % and reaching 100 % in 2029, "
             "as agreed in the memorandum with the ministry.",
             "The data system belongs to the ministry from day one and "
             "runs on its national servers.",
         ]},
        {"heading": "Districts", "kind": "figure", "weight": 1.2,
         "min_pages": 4, "height": 130, "charts": [{"type": "heatmap",
          "rows": ["Baringo North", "Lake Shore", "Highlands East",
                   "Dry Plains"],
          "cols": ["Population (k)", "Facilities", "Births per year",
                   "Remote villages", "Baseline coverage %"],
          "values": [[310, 54, 11800, 46, 61], [420, 68, 15900, 22, 66],
                     [260, 41, 9300, 61, 52], [190, 49, 7600, 84, 44]],
          "format": "{:,.0f}", "labels": 0.2}]},
    ],
}
