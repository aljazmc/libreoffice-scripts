"""Change Order Log of Harbour Bridge Retrofit: the project and everything the
document could say. The typesetting keeps what fits into one page, the most
important first."""

PROJECT = {
    "name": "Harbour Bridge Retrofit",
    "code": "HBR-24",
    "author": "Ana Novak, Project Manager, Port Aldwick City Works",
}

STATUS = {"Approved": "good", "Pending": "warn", "Rejected": "bad",
          "Withdrawn": "neutral"}

DOCUMENT = {
    "title": "Change Order Log",
    "subtitle": "Compensation events under the NEC4 contract, to 31 August "
                "2026",
    "meta": [("Project", "HBR-24"), ("Contract", "NEC4 ECC Option C"),
             ("Change orders", "27"), ("Net value", "+€2.38m"),
             ("Updated", "4 Sep 2026")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "charts": [{"type": "kpis",
         "tiles": [
             {"label": "Approved", "value": "€1.96m", "status": "good",
              "note": "19 change orders"},
             {"label": "Pending", "value": "€0.62m", "status": "warn",
              "note": "5 awaiting a decision"},
             {"label": "Rejected", "value": "€0.41m", "status": "bad",
              "note": "3 not compensation events"},
             {"label": "Time added", "value": "+19 days", "status": 0,
              "note": "to the completion date"},
         ]}]},
        {"heading": "Value by month", "kind": "figure", "weight": 0.2,
         "height": {1: 150, 2: 165, 4: 190}, "widths": [3, 2], "charts": [
             {"type": "bars", "stacked": True, "subtitle": "€k",
              "title": "Change orders by month", "values": False,
              "categories": ["Mar 25", "May", "Jul", "Sep", "Nov",
                             "Jan 26", "Mar", "May", "Jul", "Aug"],
              "series": [
                  {"name": "Approved", "color": "good",
                   "values": [40, 120, 85, 210, 160, 390, 240, 310, 280,
                              125]},
                  {"name": "Pending", "color": "warn",
                   "values": [0, 0, 0, 0, 0, 0, 0, 90, 210, 320]},
                  {"name": "Rejected", "color": "bad",
                   "values": [0, 60, 0, 0, 140, 0, 210, 0, 0, 0]}]},
             {"type": "donut", "title": "By cause", "format": "€{:,.0f}k",
              "center": ("€2.58m", "approved + pending"),
              "segments": [("Hidden condition", 1210),
                           ("Client change", 640),
                           ("Design error", 330),
                           ("Third party", 250),
                           ("Weather", 150)]},
         ]},
        {"heading": "Change orders", "kind": "table", "weight": 0.3,
         "step": 0.08, "badges": STATUS, "columns": [
             ("No.", 0.6), ("Change", 3.6), ("Cause", 1.4),
             ("Value", 1, "end"), ("Days", 0.6, "center"),
             ("Status", 1.1, "center")],
         "rows": [
             ["CE-27", "Extra plating to cross-girders XG-41 to XG-46",
              "Hidden condition", "€212k", "4", "Pending"],
             ["CE-26", "Friday night possessions, nine weeks",
              "Client change", "€45k", "0", "Pending"],
             ["CE-25", "Redesign of the pier 3 jacking frames",
              "Design error", "€118k", "6", "Pending"],
             ["CE-24", "Heated enclosures for winter painting",
              "Weather", "€150k", "0", "Approved"],
             ["CE-23", "Bearing B4-6 seized, cut out", "Hidden condition",
              "€96k", "3", "Approved"],
             ["CE-22", "Cycle lane widened during works", "Client change",
              "€74k", "0", "Approved"],
             ["CE-21", "Second paint crew, south span", "Client change",
              "€180k", "−10", "Approved"],
             ["CE-20", "Gas main lowered at the north abutment",
              "Third party", "€165k", "5", "Approved"],
             ["CE-19", "Fatigue cracks at welds W-112 and W-118",
              "Hidden condition", "€88k", "2", "Approved"],
             ["CE-18", "Night working to protect the falcon nest",
              "Third party", "€85k", "0", "Approved"],
             ["CE-17", "Contractor's own scaffold redesign",
              "Contractor risk", "€210k", "0", "Rejected"],
             ["CE-16", "Corrosion of north span lower chord beyond survey",
              "Hidden condition", "€540k", "6", "Approved"],
             ["CE-15", "Additional lead sampling", "Hidden condition",
              "€22k", "0", "Approved"],
             ["CE-14", "Paint colour changed to heritage green",
              "Client change", "€36k", "0", "Approved"],
             ["CE-13", "Temporary bus stop on Quay Road", "Client change",
              "€18k", "0", "Approved"],
             ["CE-12", "Asbestos in the old joint packing",
              "Hidden condition", "€64k", "2", "Approved"],
             ["CE-11", "Standing time in storm Isha", "Weather", "€140k",
              "3", "Rejected"],
             ["CE-10", "Telecom duct diverted by its owner", "Third party",
              "€0k", "0", "Withdrawn"],
             ["CE-09", "Wrong bearing type in the drawings",
              "Design error", "€212k", "4", "Approved"],
             ["CE-08", "Additional welfare cabins", "Contractor risk",
              "€60k", "0", "Rejected"],
             ["CE-07", "Extra traffic counts for the council",
              "Client change", "€12k", "0", "Approved"],
             ["CE-06", "Survey of the pier 2 foundations",
              "Client change", "€46k", "0", "Approved"],
             ["CE-05", "Hidden voids in the north abutment",
              "Hidden condition", "€130k", "3", "Approved"],
         ]},
        {"heading": "Budget impact", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": 165, "charts": [{"type": "waterfall",
          "format": "€{:.2f}m", "axis_format": "{:.0f}", "invert": True,
          "steps": [("Original target", 41.70), ("Hidden conditions", 0.96),
                    ("Client changes", 0.37), ("Design errors", 0.12),
                    ("Third parties", 0.25), ("Weather", 0.15),
                    ("Pending", 0.62), ("Current target", None)]}]},
        {"heading": "Process", "kind": "figure", "weight": 0.6,
         "min_pages": 2, "charts": [{"type": "chevrons", "steps": [
             {"label": "Notified", "status": "done",
              "sub": "Contractor or PM notifies within 8 weeks of "
                     "becoming aware."},
             {"label": "Quotation", "status": "done",
              "sub": "Contractor quotes cost and time within 3 weeks."},
             {"label": "Assessed", "status": "now",
              "sub": "PM and quantity surveyor check the quote within 2 "
                     "weeks."},
             {"label": "Decided", "sub": "PM up to €100k; board above "
                                         "that."},
             {"label": "Implemented", "sub": "Target cost and programme "
                                             "updated."},
         ]}]},
        {"heading": "Change against contingency", "kind": "figure",
         "weight": 0.85, "min_pages": 4, "height": 170, "widths": [3, 2],
         "charts": [
             {"type": "line", "title": "Cumulative value", "subtitle":
              "€m", "format": "{:.1f}", "end_labels": True,
              "x": ["Mar 25", "May", "Jul", "Sep", "Nov", "Jan 26", "Mar",
                    "May", "Jul", "Aug"],
              "series": [
                  {"name": "Approved + pending", "color": "accent",
                   "area": True, "values": [0.04, 0.16, 0.25, 0.46, 0.62,
                                            1.01, 1.25, 1.65, 2.14,
                                            2.58]},
                  {"name": "Contingency used", "color": 0, "dash": True,
                   "values": [0.0, 0.1, 0.2, 0.4, 0.6, 0.9, 1.3, 1.7, 2.1,
                              2.4]}]},
             {"type": "bars", "horizontal": True, "stacked": True,
              "title": "By package", "subtitle": "€k", "values": False,
              "categories": ["Steel", "Paint", "Bearings", "Deck",
                             "Traffic"],
              "series": [
                  {"name": "Approved", "color": "good",
                   "values": [828, 330, 308, 194, 300]},
                  {"name": "Pending", "color": "warn",
                   "values": [212, 0, 118, 0, 45]}]},
         ]},
        {"heading": "Pending decisions", "kind": "entries",
         "weight": 0.95, "step": 0.2, "inner": 0.05, "min_pages": 4,
         "entries": [
             {"title": "CE-27 Extra plating to cross-girders",
              "dates": "€212k · 4 days", "fields": [
                  ("Why", "Section loss of 35 % found on six "
                          "cross-girders once blasted."),
                  ("Recommendation", "Approve; the quote matches the "
                                     "contract rates for plating."),
                  ("Decision by", "Project board, 17 September."),
              ]},
             {"title": "CE-25 Pier 3 jacking frames redesigned",
              "dates": "€118k · 6 days", "fields": [
                  ("Why", "The pier 4 frames deflected under loads 30 % "
                          "over the design."),
                  ("Recommendation", "Approve at €118k, not the €160k "
                                     "quoted: reuse of the pier 4 "
                                     "frames was not priced."),
                  ("Decision by", "Project manager, 11 September."),
              ]},
             {"title": "CE-26 Friday night possessions",
              "dates": "€45k · 0 days", "fields": [
                  ("Why", "To recover the paint programme before "
                          "winter."),
                  ("Recommendation", "Approve; the bus diversion is the "
                                     "only cost."),
              ]},
         ]},
        {"heading": "Time to decide", "kind": "figure", "weight": 0.9,
         "min_pages": 4, "height": 150, "widths": [1, 1], "charts": [
             {"type": "bars", "horizontal": True, "title": "Days from "
              "notice to decision", "format": "{:.0f}", "target": 35,
              "target_label": "contract limit",
              "categories": ["Hidden condition", "Client change",
                             "Design error", "Third party", "Weather"],
              "series": [{"name": "Days", "values": [31, 18, 42, 27, 12],
                          "colors": [0, 0, "bad", 0, 0]}]},
             {"type": "line", "title": "Pending value", "subtitle": "€k",
              "x": ["Mar", "Apr", "May", "Jun", "Jul", "Aug"],
              "series": [{"name": "Pending", "color": "warn", "area": True,
                          "values": [0, 120, 90, 160, 210, 620]}]},
         ]},
        {"heading": "What the changes tell us", "kind": "text",
         "weight": 1.0, "step": 0.3, "min_pages": 2, "paragraphs": [
             "**Half of the value comes from what we could not see.** "
             "Corrosion, seized bearings and cracks behind paint account "
             "for €1.21m. The 2023 survey sampled 4 % of the steel; on "
             "the next bridge we will pay for a deeper survey of the "
             "areas that trap water.",
             "**Our own changes are cheap but frequent.** Eight client "
             "changes added €0.64m, most of them to keep the city "
             "moving. Each was worth it; together they deserve a line in "
             "the budget, not the contingency.",
             "**Decisions on design errors take too long.** The average "
             "of 42 days is over the contract limit, because each one "
             "needs the check engineer. From October the check engineer "
             "joins the weekly change meeting.",
         ]},
        {"heading": "Rejected and withdrawn", "kind": "entries",
         "weight": 1.2, "step": 0.3, "inner": 0.2, "min_pages": 4,
         "entries": [
             {"title": "CE-17 Scaffold redesign", "dates": "€210k",
              "text": ["The redesign followed the contractor's own "
                       "scaffold failing its inspection; a contractor's "
                       "risk under the contract."]},
             {"title": "CE-11 Standing time in storm Isha",
              "dates": "€140k", "text": ["The weather was within the "
                                         "ten-year return limits in the "
                                         "contract data."]},
             {"title": "CE-08 Additional welfare cabins",
              "dates": "€60k", "text": ["Shown in the contractor's own "
                                        "site layout at tender."]},
         ]},
        {"heading": "Rules for change", "kind": "bullets", "weight": 1.4,
         "step": 0.2, "min_pages": 4, "items": [
             "Every change has a number before any work starts, even in "
             "an emergency.",
             "The PM decides up to €100k and 5 days; the board decides "
             "above that, within a week.",
             "Changes are priced with the contract rates first, and "
             "agreed in advance whenever possible.",
             "Any change that touches traffic is agreed with Highways "
             "before it is instructed.",
         ]},
    ],
}
