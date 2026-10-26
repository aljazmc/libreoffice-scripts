"""Production Budget of Saltmarsh Sound Festival: the project and everything
the document could say. The typesetting keeps what fits into two pages, the
most important first."""

PROJECT = {
    "name": "Saltmarsh Sound Festival",
    "code": "SSF-27",
    "author": "Rosa Lindqvist, Festival Director",
}

DOCUMENT = {
    "title": "Production Budget",
    "subtitle": "Saltmarsh Sound 2027 · three days, 20,000 a day · "
                "budget v4 for the board, 3 March 2027",
    "meta": [("Edition", "2027"), ("Capacity", "20,000 / day"),
             ("Costs", "€4.62m"), ("Income", "€4.95m"),
             ("Margin", "+€330k · 6.7 %")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "charts": [{"type": "kpis",
         "tiles": [
             {"label": "Total cost", "value": "€4.62m", "delta": "+8 %",
              "delta_status": "bad", "status": 0, "note": "vs 2026 "
              "outturn"},
             {"label": "Total income", "value": "€4.95m", "delta": "+11 %",
              "status": 2, "note": "vs 2026"},
             {"label": "Break-even", "value": "81 %", "status": 1,
              "note": "of tickets sold"},
             {"label": "Contingency", "value": "€230k", "status": 3,
              "note": "5 % of costs"},
         ]}]},
        {"heading": "Where the money goes", "kind": "figure",
         "weight": 0.2, "height": {1: 165, 2: 175, 4: 190},
         "widths": [1, 1], "charts": [
             {"type": "donut", "title": "Costs", "format": "€{:,.0f}k",
              "center": ("€4.62m", "costs"),
              "segments": [("Artists", 1650), ("Production", 1120),
                           ("Site and infrastructure", 760),
                           ("Staff and crew", 520),
                           ("Marketing", 180), ("Other and contingency",
                                                390)]},
             {"type": "donut", "title": "Income", "format": "€{:,.0f}k",
              "center": ("€4.95m", "income"),
              "segments": [("Tickets", 3720), ("Bars", 610),
                           ("Food concessions", 240),
                           ("Sponsors", 280), ("Merch", 60),
                           ("Grants", 40)]},
         ]},
        {"heading": "By department", "kind": "table", "weight": 0.3,
         "step": 0.08, "badges": {"Over": "bad", "Under": "good",
                                  "On": "neutral"},
         "columns": [("Department", 2.6), ("2026 actual", 1.1, "end"),
                     ("2027 budget", 1.1, "end"), ("Change", 0.9, "end"),
                     ("Owner", 1.3)],
         "rows": [
             ["Artist fees and riders", "€1,510k", "€1,650k", "+9 %",
              "Booking"],
             ["Stages, sound, light, video", "€1,040k", "€1,120k", "+8 %",
              "Production"],
             ["Fencing, toilets, power, water", "€690k", "€760k",
              "+10 %", "Site"],
             ["Security and stewards", "€310k", "€330k", "+6 %",
              "Safety"],
             ["Crew, staff and volunteers", "€180k", "€190k", "+6 %",
              "Production"],
             ["Marketing", "€170k", "€180k", "+6 %", "Marketing"],
             ["Licences, insurance, medical", "€140k", "€160k", "+14 %",
              "Director"],
             ["Contingency", "€0k", "€230k", "new", "Director"],
         ]},
        {"heading": "From last year to this year", "kind": "figure",
         "weight": 0.4, "min_pages": 2, "height": 175, "charts": [{
             "type": "waterfall", "format": "€{:,.0f}k",
             "axis_format": "{:,.0f}", "invert": True,
             "steps": [("2026 costs", 4280), ("Artist fees", 140),
                       ("Production", 80), ("Site", 70),
                       ("Insurance", 20), ("Contingency", 230),
                       ("Savings: own power", -120),
                       ("Savings: reusable cups", -80),
                       ("2027 costs", None)]}]},
        {"heading": "Break-even", "kind": "figure", "weight": 0.5,
         "min_pages": 2, "height": 165, "charts": [{"type": "line",
          "title": "Profit or loss by tickets sold", "subtitle": "€k",
          "x": ["50 %", "60 %", "70 %", "80 %", "90 %", "100 %"],
          "format": "{:,.0f}", "marks": [(3.1, "break-even 81 %")],
          "series": [
              {"name": "Base case", "values": [-1470, -1020, -560, -60,
                                               300, 330]},
              {"name": "Wet weekend (bars −25 %)", "color": 1,
               "dash": True, "values": [-1620, -1170, -710, -210, 150,
                                        180]}]}]},
        {"heading": "Assumptions", "kind": "bullets", "weight": 0.6,
         "step": 0.15, "min_pages": 2, "items": [
             "Average ticket price of €71 net of fees and VAT, across "
             "weekend, day and concession tickets.",
             "96 % sell-through, as in 2025 and 2026.",
             "Bar spend of €11 per person per day; €8 on a wet day.",
             "Headliner fees agreed in euros; no exposure to the pound "
             "or the dollar this year.",
         ]},
        {"heading": "Scenarios", "kind": "figure", "weight": 0.8,
         "min_pages": 4, "height": 160, "widths": [3, 2], "charts": [
             {"type": "bars", "title": "Result by scenario",
              "subtitle": "€k", "format": "{:+,.0f}",
              "axis_format": "{:,.0f}",
              "categories": ["Sell-out", "Base", "Wet weekend",
                             "Headliner cancels", "85 % sold"],
              "series": [{"name": "Result",
                          "values": [470, 330, 180, -140, 40],
                          "colors": ["good", "good", "warn", "bad",
                                     "warn"]}]},
             {"type": "progress", "title": "Covered by insurance",
              "format": "{:.0f} %", "items": [
                  {"label": "Cancellation", "value": 100,
                   "status": "good"},
                  {"label": "Headliner no-show", "value": 80,
                   "status": "good"},
                  {"label": "Adverse weather", "value": 40,
                   "status": "warn"},
                  {"label": "Low sales", "value": 0, "status": "bad"},
              ]},
         ]},
        {"heading": "Cash flow", "kind": "figure", "weight": 0.9,
         "min_pages": 4, "height": 160, "charts": [{"type": "bars",
          "title": "Cash in and out by month", "subtitle": "€k",
          "format": "{:,.0f}", "values": False,
          "categories": ["Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr",
                         "May", "Jun", "Jul", "Aug"],
          "series": [
              {"name": "In", "color": 2,
               "values": [420, 380, 610, 290, 240, 260, 280, 330, 520,
                          1480, 140]},
              {"name": "Out", "color": 0,
               "values": [120, 180, 260, 210, 240, 380, 420, 560, 900,
                          1100, 250]}]}]},
        {"heading": "Savings we are testing", "kind": "entries",
         "weight": 1.0, "step": 0.2, "inner": 0.1, "min_pages": 4,
         "entries": [
             {"title": "Our own battery and solar power", "dates":
              "−€120k", "text": [
                  "Replaces six diesel generators for the small stages "
                  "and the camping; pays for itself in two years."]},
             {"title": "Reusable cups with a €2 deposit", "dates": "−€80k",
              "text": ["Fewer bins, fewer litter pickers, a cleaner "
                       "marsh; the deposit covers the washing."]},
             {"title": "Shared stage with the jazz weekend",
              "dates": "−€45k", "text": [
                  "Under discussion: the Saltwater Stage stays up for "
                  "the town's jazz weekend a week later."]},
         ]},
        {"heading": "Decisions for the board", "kind": "callout",
         "weight": 0.7, "tone": "warn", "min_pages": 2,
         "label": "Approve:", "text": "the budget of €4.62m with a "
         "contingency of €230k, and a headliner offer of up to €420k "
         "for Sunday, which is the line that sells the last 4 % of "
         "tickets."},
        {"heading": "Artist fees by day", "kind": "figure", "weight": 1.05,
         "min_pages": 4, "height": 150, "widths": [3, 2], "charts": [
             {"type": "bars", "title": "Fees", "subtitle": "€k",
              "stacked": True, "format": "{:,.0f}",
              "categories": ["Friday", "Saturday", "Sunday"],
              "series": [{"name": "Headliner", "values": [310, 380, 420]},
                         {"name": "Main stage", "values": [120, 140, 110]},
                         {"name": "Other stages", "values": [60, 55, 55]}]},
             {"type": "progress", "title": "Contracts signed",
              "format": "{:.0f}", "max": 124, "items": [
                  {"label": "Friday", "value": 40, "display": "40 / 41",
                   "status": "good"},
                  {"label": "Saturday", "value": 38, "display": "38 / 42",
                   "status": "warn"},
                  {"label": "Sunday", "value": 34, "display": "34 / 41",
                   "status": "warn"},
              ]},
         ]},
        {"heading": "Payment terms", "kind": "table", "weight": 1.1,
         "step": 0.1, "min_pages": 4,
         "columns": [("Supplier", 2.4), ("Deposit", 1, "center"),
                     ("Balance", 1.6), ("Risk", 2.4)],
         "rows": [
             ["Headline artists", "50 %", "On the day", "Fees in euros, "
              "insured against no-show"],
             ["Stages and sound", "30 %", "30 days after", "Fixed price "
              "for three years"],
             ["Fencing and toilets", "20 %", "30 days after",
              "Fuel surcharge capped at 5 %"],
             ["Security", "0 %", "14 days after", "Hourly rates; "
              "overtime approved by safety only"],
             ["Bars operator", "none", "Takes 22 % of bar sales",
              "Minimum guarantee of €480k"],
         ]},
    ],
}
