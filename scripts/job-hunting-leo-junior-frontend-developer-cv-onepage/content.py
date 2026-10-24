"""Curriculum Vitae of Leo Brandt: who they are and everything the document
could say. The typesetting keeps what fits into one page, the most important
first."""

PERSONA = {
    "name": "Leo Brandt",
    "headline": "junior frontend developer · former carpenter · measures "
                "twice, deploys once",
    "contact": ["Leipzig", "leo@brandt.example", "+49 157 5550 4412",
                "github.com/leobrandt"],
}


DOCUMENT = {
    "title": "Curriculum Vitae",
    "cv": True,
    "sections": [
        {"heading": "Summary", "kind": "text", "weight": 0.4, "step": 5,
         "paragraphs": [
             "Carpenter for seven years, web developer for three. "
             "After a hand injury in 2022 I taught myself to code, "
             "finished a bootcamp and built websites and a booking "
             "tool for craftspeople I know. I bring the habits of the "
             "workshop to code: measure twice, keep the bench clean, "
             "finish the job properly.",
             "Looking for my first job as a junior frontend developer, "
             "ideally on software for people who work with their hands.",
         ]},
        {"heading": "Code", "kind": "entries", "weight": 1, "step": 1.2,
         "entries": [
             {"title": "Freelance web developer", "dates": "2024 - now",
              "meta": "Leipzig",
              "items": [
                  "Answer support calls myself; most are fixed the same "
                  "day.",
                  "Built 9 websites for carpenters, a plumber, a bakery "
                  "and a cello maker.",
                  "Built Termin, a booking tool for small workshops in "
                  "React and Supabase; 14 businesses use it daily.",
                  "Lighthouse scores above 95 on every site; all pass "
                  "WCAG AA checks.",
              ],
              "story": [
                  "My first client was my old master carpenter. He "
                  "wanted customers to book site visits without calling "
                  "him on a roof. Termin started as his booking page "
                  "and now runs fourteen workshops. Every feature came "
                  "from a phone call with someone holding a tool.",
              ]},
             {"title": "Gap: job hunting", "dates": "2024",
              "meta": "6 months",
              "items": [
                  "Applied to 80 junior roles, built projects in "
                  "between, learned TypeScript and testing properly.",
              ]},
             {"title": "Frontend bootcamp", "org": "CodeWerk Leipzig",
              "dates": "2023", "meta": "16 weeks, full-time",
              "story": [
                  "I was the oldest in the cohort and the only one who "
                  "had used a table saw. Pair programming felt like "
                  "working with an apprentice, in both directions.",
              ],
              "items": [
                  "HTML, CSS, JavaScript, React, Git; final project a "
                  "material calculator for carpenters, voted best of "
                  "the cohort.",
              ]},
             {"title": "Gap: hand injury", "dates": "2022",
              "meta": "4 months",
              "items": [
                  "Injured my left hand on a table saw; recovered well, "
                  "but not enough for full-time carpentry.",
                  "Started learning to code with free courses, one hand "
                  "at first.",
              ]},
         ]},
        {"heading": "Wood", "kind": "entries", "weight": 1.4, "step": 1.2,
         "entries": [
             {"title": "Carpenter (Tischler)", "org": "Tischlerei Weber",
              "dates": "2016 - 2022", "meta": "Leipzig",
              "items": [
                  "Built kitchens, stairs and shopfittings from drawing "
                  "to installation.",
                  "Programmed the workshop's CNC router; my first code, "
                  "though I did not know it then.",
                  "Trained two apprentices.",
              ],
              "story": [
                  "Six years of kitchens taught me that customers "
                  "remember the drawer that sticks, not the beautiful "
                  "worktop. I think about software the same way now: "
                  "the small things people touch every day matter "
                  "most.",
              ]},
             {"title": "Gap: travelling", "dates": "2019",
              "meta": "4 months",
              "items": [
                  "Worked my way through Norway and Scotland on boat "
                  "repairs and timber frames.",
              ]},
             {"title": "Apprenticeship, carpentry", "org": "Tischlerei "
              "Weber", "dates": "2013 - 2016",
              "items": ["Journeyman certificate (Gesellenbrief), 2016."]},
         ]},
        {"heading": "Skills", "kind": "tags", "weight": 1.7, "step": 0.5,
         "items": [
             ("frontend", "HTML, CSS, JavaScript, TypeScript, React, "
                          "Next.js"),
             ("backend", "Supabase, PostgreSQL basics, Node"),
             ("tools", "Git, Vitest, Playwright, Figma"),
             ("quality", "accessibility, performance, tests"),
             ("wood", "joinery, CNC, technical drawing"),
         ]},
        {"heading": "Projects", "kind": "bullets", "weight": 2.4,
         "step": 0.5, "items": [
             "**Termin** - booking for workshops; 14 users.",
             "**Zuschnitt** - cut list optimiser for sheet material; "
             "saves about 12 % of plywood.",
             "**Holzpreis** - timber price tracker from public data.",
         ]},
        {"heading": "Education", "kind": "entries", "weight": 3,
         "step": 1, "entries": [
             {"title": "Frontend Bootcamp", "org": "CodeWerk Leipzig",
              "dates": "2023", "items": []},
             {"title": "Gesellenbrief, Tischler", "org": "HWK Leipzig",
              "dates": "2016", "items": []},
             {"title": "Realschulabschluss", "dates": "2013",
              "items": []},
         ]},
        {"heading": "Languages", "kind": "tags", "weight": 3.6, "step": 0.3,
         "items": [("german", "native"), ("english", "good"),
                   ("norwegian", "boat-repair level")]},
        {"heading": "Certificates", "kind": "bullets", "weight": 5,
         "step": 0.4, "min_pages": 2, "items": [
             "freeCodeCamp Responsive Web Design, 2022.",
             "freeCodeCamp JavaScript Algorithms, 2023.",
             "Web Accessibility, W3C on edX, 2024.",
         ]},
        {"heading": "Clients", "kind": "bullets", "weight": 5.2,
         "step": 0.3, "min_pages": 4, "items": [
             "Tischlerei Weber - website and Termin.",
             "Geigenbau Lindner - cello maker, gallery site.",
             "Baeckerei Kurz - opening hours that update themselves.",
             "Sanitaer Meyer - emergency call button that works.",
             "Five more carpenters, one roofer.",
         ]},
        {"heading": "Talks", "kind": "bullets", "weight": 5.3,
         "step": 0.3, "min_pages": 4, "items": [
             "\"A test is a jig\", Leipzig Frontend Meetup, 2025.",
             "\"Software for dusty fingers\", Handwerkskammer "
             "digital day, 2025.",
         ]},
        {"heading": "Community", "kind": "bullets", "weight": 5.4,
         "step": 0.4, "min_pages": 4, "items": [
             "Co-organiser, Leipzig Frontend Meetup, 2025.",
             "Code club for apprentices at the Handwerkskammer, monthly.",
         ]},
        {"heading": "Interests", "kind": "text", "weight": 6.5,
         "paragraphs": [
             "Wooden boats, bouldering, making spoons, and reading old "
             "carpentry manuals for ideas about software.",
         ]},
        {"heading": "References", "kind": "entries", "weight": 7,
         "min_pages": 4, "entries": [
             {"title": "Meister Klaus Weber", "org": "Tischlerei Weber",
              "meta": "on request", "items": []},
             {"title": "Sara Yilmaz", "org": "Bootcamp mentor",
              "meta": "on request", "items": []},
         ]},
    ],
}
