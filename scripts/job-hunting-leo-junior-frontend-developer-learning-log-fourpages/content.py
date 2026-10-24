"""Learning Log of Leo Brandt: who they are and everything the document
could say. The typesetting keeps what fits into four pages, the most important
first."""

PERSONA = {
    "name": "Leo Brandt",
    "headline": "junior frontend developer · former carpenter · measures "
                "twice, deploys once",
    "contact": ["Leipzig", "leo@brandt.example", "+49 157 5550 4412",
                "github.com/leobrandt"],
}


DOCUMENT = {
    "title": "Learning Log",
    "subtitle": "every course, project and mistake since 2022, "
                "itemised",
    "sections": [
        {"kind": "text", "weight": 0.2, "step": 4, "paragraphs": [
            "I keep a log of what I learn, like a carpenter keeps "
            "receipts for materials. Hours are rounded. Mistakes are "
            "included at no extra charge.",
        ]},
        {"heading": "HTML and CSS", "kind": "entries", "weight": 0.5,
         "step": 1, "inner": 0.6, "entries": [
             {"title": "2022", "org": "160 h", "items": [
                 "freeCodeCamp responsive web design.",
                 "Rebuilt the Tischlerei Weber website, one-handed.",
                 "Mistake: used tables for layout. Once.",
             ]},
         ]},
        {"heading": "JavaScript", "kind": "entries", "weight": 1,
         "step": 1, "inner": 0.6, "entries": [
             {"title": "2022 - 2023", "org": "300 h", "items": [
                 "freeCodeCamp algorithms; Eloquent JavaScript.",
                 "Built Zuschnitt, a cut list optimiser.",
                 "Mistake: an infinite loop that froze a customer's "
                 "laptop during a demo.",
             ]},
         ]},
        {"heading": "Bootcamp", "kind": "entries", "weight": 1.6,
         "step": 1, "inner": 0.6, "entries": [
             {"title": "2023", "org": "640 h", "items": [
                 "React, Git, teamwork, code review.",
                 "Final project voted best of cohort.",
                 "Learned: reading other people's code is a skill.",
             ]},
         ]},
        {"heading": "TypeScript and tests", "kind": "entries",
         "weight": 2.2, "step": 1, "inner": 0.6, "entries": [
             {"title": "2024", "org": "280 h", "items": [
                 "Converted Termin to TypeScript.",
                 "Vitest and Playwright; 140 tests.",
                 "Learned: a test is a jig for code.",
             ]},
         ]},
        {"heading": "Termin", "kind": "entries", "weight": 2.8, "step": 1,
         "inner": 0.6, "entries": [
             {"title": "2024 - now", "org": "500 h", "items": [
                 "React, Supabase, email reminders.",
                 "14 workshops use it.",
                 "Mistake: sent 300 reminder emails at 3 am. Added "
                 "quiet hours.",
             ]},
         ]},
        {"heading": "Accessibility", "kind": "entries", "weight": 3.2,
         "step": 1, "inner": 0.6, "min_pages": 2, "entries": [
             {"title": "2024", "org": "60 h", "items": [
                 "W3C course; screen reader testing.",
                 "Fixed every site I had built so far.",
             ]},
         ]},
        {"heading": "Subtotal", "kind": "tags", "weight": 3.6,
         "step": 0.3, "min_pages": 2, "items": [
             ("hours", "about 2,100"),
             ("projects", "12"), ("users", "14 workshops"),
             ("tests", "140"), ("3 am emails", "300 (once)"),
         ]},
        {"heading": "CNC G-code", "kind": "entries", "weight": 2.0,
         "step": 1, "inner": 0.6, "min_pages": 2, "entries": [
             {"title": "2018", "org": "40 h", "items": [
                 "Programmed the workshop CNC router for kitchen "
                 "fronts.",
                 "My first code. I did not call it that.",
                 "Mistake: a missing minus sign cut through a sacrificial "
                 "board and into the table.",
             ]},
         ]},
        {"heading": "Git", "kind": "entries", "weight": 3.3, "step": 1,
         "inner": 0.6, "min_pages": 4, "entries": [
             {"title": "2023", "org": "30 h", "items": [
                 "Branches, rebasing, resolving conflicts.",
                 "Mistake: force-pushed over a teammate's work at the "
                 "bootcamp. Bought cake.",
             ]},
         ]},
        {"heading": "Figma", "kind": "entries", "weight": 3.4, "step": 1,
         "inner": 0.6, "min_pages": 4, "entries": [
             {"title": "2023", "org": "40 h", "items": [
                 "Enough to read designers' files and sketch my own.",
                 "Learned: drawing first saves building twice, like "
                 "in carpentry.",
             ]},
         ]},
        {"heading": "Supabase and SQL", "kind": "entries", "weight": 3.5,
         "step": 1, "inner": 0.6, "min_pages": 4, "entries": [
             {"title": "2024", "org": "90 h", "items": [
                 "Tables, row level security, simple queries.",
                 "Mistake: forgot security on one table; a customer "
                 "could see another's bookings for a day. Fixed, "
                 "apologised, wrote a test.",
             ]},
         ]},
        {"heading": "Performance", "kind": "entries", "weight": 3.7,
         "step": 1, "inner": 0.6, "min_pages": 4, "entries": [
             {"title": "2025", "org": "50 h", "items": [
                 "Lighthouse, image sizes, lazy loading.",
                 "Made the bakery site load in one second on a 3G phone.",
             ]},
         ]},
        {"heading": "Running a tiny business", "kind": "entries",
         "weight": 3.8, "step": 1, "inner": 0.6, "min_pages": 4,
         "entries": [
             {"title": "2024 - now", "org": "ongoing", "items": [
                 "Invoices, support calls, saying no to scope creep.",
                 "Learned: the customer is usually right about the "
                 "problem and usually wrong about the solution.",
             ]},
         ]},
        {"heading": "Books", "kind": "bullets", "weight": 3.9, "step": 0.3,
         "min_pages": 4, "items": [
             "Eloquent JavaScript - Marijn Haverbeke.",
             "Don't Make Me Think - Steve Krug.",
             "The Pragmatic Programmer - Hunt and Thomas.",
             "Inclusive Components - Heydon Pickering.",
             "Holzverbindungen - an old joinery manual, still useful.",
         ]},
        {"heading": "Mistakes, summed up", "kind": "bullets",
         "weight": 4.1, "step": 0.3, "min_pages": 4, "items": [
             "Tables for layout.",
             "An infinite loop in a demo.",
             "A force-push.",
             "A table without security.",
             "300 emails at 3 am.",
             "Each one has a test or a checklist now.",
         ]},
        {"heading": "Next", "kind": "bullets", "weight": 4, "step": 0.4,
         "min_pages": 4, "items": [
             "Offline-first web apps.",
             "Better CSS architecture.",
             "Working in a real team.",
         ]},
    ],
}
