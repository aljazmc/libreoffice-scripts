"""Showreel Breakdown of Kai Berg: who they are and everything the document
could say. The typesetting keeps what fits into one page, the most important
first."""

PERSONA = {
    "name": "Kai Berg",
    "headline": "3D environment artist · ten thousand square metres of "
                "places that never existed",
    "contact": ["Malmö, Sweden", "kai.berg@example.se", "+46 73 555 6620",
                "artstation.com/kaiberg"],
}


DOCUMENT = {
    "title": "Showreel Breakdown",
    "subtitle": "Two minutes and forty seconds, shot by shot: what I "
                "built, what I lit and what I borrowed",
    "sections": [
        {"kind": "text", "weight": 0.2, "step": 4, "paragraphs": [
            "A reel shows the result; this document shows the work. For "
            "each shot you will find the timecode, the context, exactly "
            "what I made myself and what came from others, the tools and "
            "one thing I would change today. Shots from games are "
            "marked with the studio's permission.",
        ]},
        {"heading": "Kvarteret Plommon", "kind": "entries", "weight": 0.5,
         "step": 1, "inner": 0.8, "entries": [
             {"title": "00:00 – 00:24", "org": "freelance, 2025",
              "fields": [
                  ("Shot", "a slow walk from the street through a "
                           "courtyard to a fourth-floor balcony at 4 pm "
                           "in October."),
                  ("Mine", "all lighting, materials, vegetation and the "
                           "camera; the building model came from the "
                           "architect's Revit file."),
                  ("Tools", "Unreal Engine 5, Lumen, Quixel, Blender for "
                            "cleanup."),
                  ("Change", "I would add people. Empty courtyards look "
                             "lonely, not peaceful."),
              ]},
         ]},
        {"heading": "Farmor's kitchen", "kind": "entries", "weight": 1,
         "step": 1, "inner": 0.8, "entries": [
             {"title": "00:24 – 00:46", "org": "personal, 2024",
              "fields": [
                  ("Shot", "morning light crossing a 1950s kitchen, dust "
                           "in the air, a kettle on the stove."),
                  ("Mine", "everything, modelled from twelve family "
                           "photographs and my mother's memory."),
                  ("Tools", "Blender, Cycles, Substance Painter."),
                  ("Change", "nothing; my grandmother cried, which is "
                             "the only review that matters."),
              ]},
         ]},
        {"heading": "The Ashen Ridge", "kind": "entries", "weight": 1.6,
         "step": 1, "inner": 0.8, "entries": [
             {"title": "00:46 – 01:18", "org": "Hollow Crown, Nordljus "
              "Games, 2023",
              "fields": [
                  ("Shot", "a flyover of a burnt village at dusk, ending "
                           "at a lit well."),
                  ("Mine", "layout, modular buildings, set dressing and "
                           "lighting; terrain by a colleague, characters "
                           "by the character team."),
                  ("Tools", "Unreal Engine 4, SpeedTree, Substance "
                            "Designer."),
                  ("Change", "fewer embers; I was proud of the particle "
                             "system and it shows."),
              ]},
         ]},
        {"heading": "School daylight study", "kind": "entries",
         "weight": 2.2, "step": 1, "inner": 0.8, "entries": [
             {"title": "01:18 – 01:40", "org": "competition, 2025",
              "fields": [
                  ("Shot", "a time-lapse of one classroom from 8 am to 3 "
                           "pm on 21 December."),
                  ("Mine", "daylight setup, materials and the time-lapse; "
                           "the design was the architects'."),
                  ("Result", "second prize; the jury mentioned the "
                             "daylight in their report."),
              ]},
         ]},
        {"heading": "Harbour level 88", "kind": "entries", "weight": 2.8,
         "step": 1, "inner": 0.8, "entries": [
             {"title": "01:40 – 01:52", "org": "Puzzlebox Studio, 2017",
              "fields": [
                  ("Shot", "a toy-like harbour seen from above, readable "
                           "at phone size."),
                  ("Mine", "the whole level, from paper sketch to final "
                           "art."),
                  ("Change", "it is in the reel to show where I come "
                             "from, not where I am going."),
              ]},
         ]},
        {"heading": "Timber kit", "kind": "entries", "weight": 3.2,
         "step": 1, "inner": 0.8, "min_pages": 2, "entries": [
             {"title": "01:52 – 02:14", "org": "Hollow Crown, 2021",
              "fields": [
                  ("Shot", "300 modular pieces assembling into a Nordic "
                           "farmhouse, a church and a mill."),
                  ("Mine", "the kit, its rules and the documentation "
                           "that let twelve artists build with it."),
                  ("Lesson", "a good kit is a language; the "
                             "documentation is its grammar."),
              ]},
         ]},
        {"heading": "Aarhus library study", "kind": "entries",
         "weight": 3.4, "step": 1, "inner": 0.8, "min_pages": 4,
         "entries": [
             {"title": "02:14 – 02:40", "org": "study, 2026",
              "fields": [
                  ("Shot", "a reading room with burnt-out windows and "
                           "deep, soft shadows."),
                  ("Mine", "a study rebuilt from published photographs "
                           "and plans, to learn how Lys & Linje lights."),
                  ("Lesson", "expose for the shadows; let the windows "
                             "go white."),
              ]},
         ]},
        {"heading": "Night market", "kind": "entries", "weight": 3.5,
         "step": 1, "inner": 0.8, "min_pages": 4, "entries": [
             {"title": "not in the reel, available on request",
              "org": "Hollow Crown, 2022",
              "fields": [
                  ("Context", "a lantern-lit market street that players "
                              "visit at night only."),
                  ("Mine", "lighting of 140 lanterns with a budget of "
                           "eight dynamic lights."),
                  ("Lesson", "fake light carefully and nobody notices; "
                             "fake it lazily and everybody does."),
              ]},
         ]},
        {"heading": "Process for a new shot", "kind": "entries",
         "weight": 3.6, "step": 0.6, "inner": 0.4, "min_pages": 2,
         "entries": [
             {"title": "1. Intention", "text": [
                 "One sentence from the architect: what should a viewer "
                 "feel and where should they look first."]},
             {"title": "2. Blockout and camera", "text": [
                 "Grey model, three camera options, sun studies for the "
                 "real location and date."]},
             {"title": "3. Materials", "text": [
                 "Measured or scanned materials, checked against "
                 "samples when possible."]},
             {"title": "4. Light and people", "text": [
                 "Light for truth first, mood second; people and "
                 "vegetation at the very end."]},
             {"title": "5. Test", "text": [
                 "Show it to someone who has never seen the project. Can "
                 "they find the entrance in three seconds?"]},
         ]},
        {"heading": "What changed from games", "kind": "tags",
         "weight": 3.7, "step": 0.3, "min_pages": 4, "items": [
             ("Light", "from dramatic to honest"),
             ("Sun", "from wherever it looks good to where it really is"),
             ("Materials", "from stylised to measured"),
             ("Camera", "from wide and low to eye height and quiet"),
             ("Audience", "from players to neighbours, clients and "
                          "juries"),
         ]},
        {"heading": "Malmö brutalism", "kind": "entries", "weight": 3.55,
         "step": 1, "inner": 0.8, "min_pages": 4, "entries": [
             {"title": "not in the reel, available on request",
              "org": "personal, 2025",
              "fields": [
                  ("Context", "three concrete buildings from the 1960s "
                              "that the city plans to demolish."),
                  ("Mine", "photogrammetry of the facades, interiors "
                           "rebuilt from archive drawings, light from "
                           "real sun positions."),
                  ("Result", "shown at a heritage evening; one building "
                             "is now being reconsidered for renovation."),
                  ("Lesson", "images change opinions faster than "
                             "arguments do, which is a responsibility."),
              ]},
         ]},
        {"heading": "Cut from the reel", "kind": "bullets", "weight": 3.8,
         "step": 0.5, "min_pages": 4, "items": [
             "A fantasy castle at sunset: beautiful, and irrelevant to "
             "architecture.",
             "A real-time car configurator for a client who never paid.",
             "A forest flythrough that looks like every other forest "
             "flythrough.",
             "My first Unreal scene from 2014, kept on my hard drive as "
             "a warning.",
         ]},
        {"heading": "Technical notes", "kind": "tags", "weight": 4.2,
         "step": 0.3, "min_pages": 2, "items": [
             ("Resolution", "4K masters, delivered in 1080p and 4K"),
             ("Rendering", "Lumen in real time; path tracing for stills "
                           "and two shots"),
             ("Colour", "ACES, graded in DaVinci Resolve"),
             ("Music", "licensed, Epidemic Sound"),
         ]},
    ],
}
