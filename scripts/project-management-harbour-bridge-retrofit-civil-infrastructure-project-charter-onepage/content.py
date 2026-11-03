"""Project Charter of Harbour Bridge Retrofit: the project and everything the
document could say. The typesetting keeps what fits into one page, the most
important first."""

PROJECT = {
    "name": "Harbour Bridge Retrofit",
    "code": "HBR-24",
    "author": "Ana Novak, Project Manager, Port Aldwick City Works",
}


DOCUMENT = {
    "title": "Project Charter",
    "subtitle": "Strengthening and repainting the 1962 Harbour Bridge while "
                "it stays open to traffic",
    "meta": [("Project", "HBR-24"), ("Sponsor", "Dir. of City Works"),
             ("Manager", "Ana Novak"), ("Version", "1.2 · approved"),
             ("Date", "14 Jan 2025")],
    "sections": [
        {"kind": "figure", "weight": 0.1, "charts": [{"type": "kpis",
         "tiles": [
             {"label": "Budget", "value": "€45.8m", "note": "incl. €4.1m "
              "contingency", "status": "accent"},
             {"label": "Duration", "value": "24 mo", "note": "Feb 2025 – "
              "Jan 2027", "status": 0},
             {"label": "Design life", "value": "+50 yr", "note": "to "
              "2077", "status": "good"},
             {"label": "Lanes open", "value": "2+", "note": "of 4, at all "
              "times", "status": "warn"},
         ]}]},
        {"heading": "Purpose", "kind": "text", "weight": 0.2, "step": 2,
         "paragraphs": [
             "The Harbour Bridge carries 38,000 vehicles and 4,200 cyclists "
             "a day across the inner harbour. The 2023 principal inspection "
             "found section loss of up to 30 % in the lower chord of the "
             "north span, failed bearings at piers 3 and 4 and paint at the "
             "end of its life. A weight limit of 18 tonnes has applied "
             "since March 2024. **This project restores the bridge to full "
             "load capacity and extends its life by fifty years**, while "
             "keeping it open.",
             "Doing nothing is not an option: the engineer's assessment is "
             "that the weight limit would have to drop to 7.5 tonnes by "
             "2027, which would send every bus and lorry on a 14 km detour "
             "through the old town.",
         ]},
        {"heading": "Objectives", "kind": "figure", "weight": 0.3,
         "charts": [{"type": "progress", "format": "{}", "max": 100,
          "items": [
              {"label": "Lift the weight limit", "value": 100,
               "display": "44 t", "note": "full highway loading by Jan "
               "2027", "status": 0},
              {"label": "Keep traffic moving", "value": 85,
               "display": "6 min", "note": "average added delay in the "
               "peak", "status": 0},
              {"label": "Stay within budget", "value": 92,
               "display": "€45.8m", "note": "outturn within the approved "
               "budget", "status": 0},
              {"label": "Zero harm", "value": 100, "display": "0 RIDDOR",
               "note": "no reportable injuries", "status": "good"},
          ]}]},
        {"heading": "Scope", "kind": "figure", "weight": 0.5, "min_pages": 2,
         "charts": [{"type": "board", "columns": [
             {"title": "In scope", "tone": "good", "cards": [
                 "Strengthen the lower chord of the north span with bolted "
                 "plates",
                 "Replace 16 bearings at piers 3 and 4",
                 "Blast and repaint 41,000 m² of steelwork",
                 "Renew the deck waterproofing and surfacing",
                 "Replace the expansion joints at both abutments",
             ]},
             {"title": "Out of scope", "tone": "bad", "cards": [
                 "Widening the bridge or adding a lane",
                 "The approach viaducts (separate scheme, 2028)",
                 "Lighting, other than temporary works lighting",
                 "The swing mechanism of the old bascule",
             ]},
             {"title": "Assumptions", "tone": "info", "cards": [
                 "Night possessions from 22:00 to 05:30, Sun – Thu",
                 "Harbour authority allows a 20 m exclusion zone",
                 "No lead found beyond the 2023 survey samples",
             ]},
         ]}]},
        {"kind": "bullets", "weight": 0.55, "step": 0.2, "max_pages": 1,
         "heading": "Scope", "items": [
             "**In:** strengthening of the north span, 16 bearings, "
             "41,000 m² of repainting, deck surfacing and joints.",
             "**Out:** widening, the approach viaducts, the old bascule "
             "mechanism.",
         ]},
        {"heading": "Milestones", "kind": "figure", "weight": 0.4,
         "height": {1: 118, 2: 128}, "charts": [{"type": "timeline",
          "start": 0, "end": 24,
          "phases": [(0, 5, "Design"), (5, 21, "Construction"),
                     (21, 24, "Close")],
          "ticks": [(0, "Feb 25"), (6, "Aug 25"), (12, "Feb 26"),
                    (18, "Aug 26"), (24, "Feb 27")],
          "events": [
              {"at": 1, "label": "Contract award", "sub": "Mar 2025"},
              {"at": 5, "label": "Design frozen", "sub": "Jul 2025"},
              {"at": 9, "label": "North span plated", "sub": "Nov 2025"},
              {"at": 14, "label": "Bearings replaced", "sub": "Apr 2026"},
              {"at": 20, "label": "Load test", "sub": "Oct 2026"},
              {"at": 23, "label": "Weight limit lifted", "sub": "Jan 2027",
               "status": "now"},
          ]}]},
        {"heading": "Budget", "kind": "figure", "weight": 0.7,
         "height": {1: 120, 2: 140}, "widths": [5, 4], "charts": [
             {"type": "donut", "title": "Budget by package",
              "format": "€{:.1f}m", "center": ("€45.8m", "total"),
              "segments": [("Steel strengthening", 13.5),
                           ("Protective coating", 11.2),
                           ("Bearings and joints", 6.8),
                           ("Deck and surfacing", 5.4),
                           ("Traffic management", 4.8),
                           ("Contingency", 4.1)]},
             {"type": "bars", "title": "Spend profile", "subtitle": "€m",
              "categories": ["Q1 25", "Q2", "Q3", "Q4", "Q1 26", "Q2",
                             "Q3", "Q4"],
              "series": [{"name": "Spend",
                          "values": [1.2, 3.4, 6.8, 8.1, 8.6, 7.9, 6.0,
                                     3.8]}],
              "format": "{:.1f}", "axis_format": "{:.0f}"},
         ]},
        {"heading": "Summary schedule", "kind": "figure", "weight": 1.5,
         "min_pages": 4, "charts": [{"type": "gantt", "row": 14,
          "columns": ["Q1 25", "Q2", "Q3", "Q4", "Q1 26", "Q2", "Q3", "Q4",
                      "Q1 27"],
          "groups": ["Design", "Works", "Close"],
          "tasks": [
              {"label": "Surveys and design", "start": 0, "end": 2},
              {"label": "Category III check", "start": 1.5, "end": 2.3},
              {"label": "Containment north span", "start": 2, "end": 3,
               "group": 1},
              {"label": "Plating lower chord", "start": 2.5, "end": 4.2,
               "group": 1, "critical": True},
              {"label": "Blast and paint", "start": 3, "end": 7, "group": 1},
              {"label": "Bearings piers 3 and 4", "start": 4.2, "end": 5.5,
               "group": 1, "critical": True},
              {"label": "Expansion joints", "start": 5.5, "end": 6.5,
               "group": 1},
              {"label": "Deck waterproofing and surfacing", "start": 6,
               "end": 7.5, "group": 1, "critical": True},
              {"label": "Load test", "start": 7.6, "milestone": True,
               "text": "Oct 2026"},
              {"label": "Handover and closure", "start": 7.7, "end": 9,
               "group": 2},
          ], "deps": [(0, 2), (3, 5), (5, 7)]}]},
        {"heading": "Delivery approach", "kind": "text", "weight": 1.55,
         "step": 0.3, "min_pages": 4, "paragraphs": [
             "The works are let as one NEC4 Option C target cost contract "
             "to Ferrand Civils, with Halden Engineers as designer "
             "under a separate professional services contract. A target "
             "cost shares the pain and the gain of the corrosion we cannot "
             "see yet, which is the largest uncertainty of the project.",
             "Work over the carriageway happens at night in possessions; "
             "work under the deck happens by day from a fully enclosed "
             "platform that hangs from the bridge and never touches the "
             "water. The north span is finished before the south span is "
             "started, so only one half of the bridge is ever under "
             "scaffold.",
         ]},
        {"heading": "Key roles", "kind": "table", "weight": 1.7, "step": 0.2,
         "min_pages": 4, "columns": [("Role", 1.6), ("Name", 1.4),
                                     ("Responsible for", 3.4)],
         "rows": [
             ["Sponsor", "Dir. of City Works", "The business case, the "
              "budget, decisions beyond tolerance"],
             ["Project manager", "Ana Novak", "Delivery, reporting, "
              "change, risk and the contract"],
             ["Senior user", "Head of Highways", "Traffic management, "
              "acceptance of the bridge"],
             ["Designer", "Halden Engineers", "Design, site queries, the "
              "load test"],
             ["Contractor", "Ferrand Civils", "Construction, safety on "
              "site, the programme"],
             ["Communications", "Lena Ortiz", "Residents, press, the "
              "weekly bulletin"],
         ]},
        {"heading": "Governance", "kind": "figure", "weight": 0.9,
         "min_pages": 2, "charts": [{"type": "tree", "root": {
             "label": "City Works Board", "note": "approves budget and "
             "changes over €250k", "children": [
                 {"label": "Project Board", "note": "monthly",
                  "children": [
                      {"label": "Sponsor: Director of City Works"},
                      {"label": "Senior user: Head of Highways"},
                      {"label": "Senior supplier: Ferrand Civils"},
                  ]},
                 {"label": "Project Manager", "note": "Ana Novak",
                  "children": [
                      {"label": "Design lead: Halden Engineers"},
                      {"label": "Site manager: Ferrand Civils"},
                      {"label": "NEC supervisor", "status": "info"},
                  ]},
                 {"label": "Assurance", "note": "independent",
                  "children": [
                      {"label": "Check engineer (Cat III)"},
                      {"label": "CDM principal designer"},
                      {"label": "Internal audit, quarterly"},
                  ]},
             ]}}]},
        {"heading": "Tolerances", "kind": "table", "weight": 1.0,
         "step": 0.3, "min_pages": 2, "columns": [
             ("Measure", 2), ("Manager may", 2), ("Board may", 2),
             ("Escalate", 1.4)],
         "rows": [
             ["Time", "± 2 weeks on a milestone", "± 6 weeks",
              "City Works Board"],
             ["Cost", "± €100k per package", "± €1m overall",
              "City Works Board"],
             ["Scope", "Change within a package", "Move work between "
              "packages", "Any removal"],
             ["Lane closures", "Planned nights only", "One weekend per "
              "month", "Any daytime closure"],
             ["Risk", "Risks scoring under 10", "Risks up to 15",
              "Anything over 15"],
         ]},
        {"heading": "Constraints", "kind": "bullets", "weight": 1.2,
         "step": 0.25, "min_pages": 2, "items": [
             "At least two lanes, one in each direction, open from 05:30 "
             "to 22:00 every day, and the cycle lane open at all times.",
             "No work over the navigation channel during the tall ships "
             "festival, 10 – 16 August 2025 and 2026.",
             "Blast media and paint fully contained: the harbour is a "
             "designated bathing water.",
             "Peregrine falcons nest under pier 4 from March to June; no "
             "work within 50 m of the nest during that time.",
         ]},
        {"heading": "Work breakdown", "kind": "figure", "weight": 1.6,
         "min_pages": 4, "charts": [{"type": "tree", "size": 6.6,
          "root": {"label": "HBR-24 Harbour Bridge Retrofit", "code": "1",
                   "children": [
              {"label": "Design", "code": "1.1", "children": [
                  {"label": "Surveys", "code": "1.1.1"},
                  {"label": "Strengthening design", "code": "1.1.2"},
                  {"label": "Temporary works", "code": "1.1.3"},
                  {"label": "Category III check", "code": "1.1.4"}]},
              {"label": "Steelwork", "code": "1.2", "children": [
                  {"label": "Containment", "code": "1.2.1"},
                  {"label": "Plating", "code": "1.2.2"},
                  {"label": "Blast and paint", "code": "1.2.3"}]},
              {"label": "Bearings and joints", "code": "1.3", "children": [
                  {"label": "Jacking", "code": "1.3.1"},
                  {"label": "Bearing swap", "code": "1.3.2"},
                  {"label": "Expansion joints", "code": "1.3.3"}]},
              {"label": "Deck", "code": "1.4", "children": [
                  {"label": "Waterproofing", "code": "1.4.1"},
                  {"label": "Surfacing", "code": "1.4.2"},
                  {"label": "Lining", "code": "1.4.3"}]},
              {"label": "Traffic and public", "code": "1.5", "children": [
                  {"label": "Traffic management", "code": "1.5.1"},
                  {"label": "Communications", "code": "1.5.2"},
                  {"label": "Load test", "code": "1.5.3"}]},
          ]}}]},
        {"heading": "Stakeholders", "kind": "figure", "weight": 1.8,
         "min_pages": 4, "height": 170, "widths": [3, 2], "charts": [
             {"type": "quadrant", "x": "interest", "y": "influence",
              "quadrants": ["Keep satisfied", "Manage closely", "Monitor",
                            "Keep informed"],
              "points": [("City council", 7, 9, "accent"),
                         ("Harbour authority", 6, 8, "accent"),
                         ("Bus operator", 8, 6, 0),
                         ("Residents' association", 9, 4, 0),
                         ("Cycling campaign", 8, 2.5, 0),
                         ("Ferry company", 4, 5, 2),
                         ("Utilities", 3, 7, 2),
                         ("Local press", 5, 3, 2)]},
             {"type": "heatmap", "title": "Engagement",
              "rows": ["Council", "Harbour", "Buses", "Residents",
                       "Cyclists"],
              "cols": ["Brief", "Consult", "Agree"],
              "values": [["Monthly", "Plans", "Budget"],
                         ["Weekly", "Method", "Permits"],
                         ["Weekly", "Diversions", ""],
                         ["Newsletter", "Night works", ""],
                         ["Social", "Cycle route", ""]],
              "badges": {"Monthly": "info", "Weekly": "accent"},
              "size": 6.8},
         ]},
        {"heading": "Initial risks", "kind": "table", "weight": 2.0,
         "step": 0.3, "min_pages": 4, "columns": [
             ("Risk", 3.2), ("Score", 0.8, "center"), ("Response", 3.2)],
         "badges": {"20": "bad", "16": "bad", "12": "warn", "9": "warn"},
         "rows": [
             ["Corrosion worse than the survey found once the paint is "
              "off", "20", "Provisional sum of €1.2m; plate designs for "
              "40 % loss ready"],
             ["Night possessions refused during events", "16",
              "Calendar agreed with the council a year ahead"],
             ["Steel prices rise", "12", "Steel bought at contract "
              "award, priced in"],
             ["Lead paint beyond the samples", "12", "Full containment "
              "class A from day one"],
             ["Bearing supplier late", "9", "Two suppliers qualified"],
         ]},
        {"heading": "Approval", "kind": "callout", "weight": 1.4,
         "tone": "good", "min_pages": 2, "label": "Approved",
         "text": "by the City Works Board on 14 January 2025, minute "
                 "CWB/25/07, with the condition that the board sees the "
                 "detailed design before the steel is ordered."},
        {"heading": "Success criteria", "kind": "bullets", "weight": 2.3,
         "step": 0.2, "min_pages": 4, "items": [
             "The bridge passes its load test and the weight limit is "
             "lifted by 31 January 2027.",
             "Average peak delay stays under six minutes, measured by the "
             "journey time sensors on both approaches.",
             "No pollution incident reported to the environment agency.",
             "Outturn cost at or below €45.8m, contingency included.",
             "Residents' satisfaction with how they were kept informed "
             "of at least 70 % in the closing survey.",
         ]},
    ],
}
