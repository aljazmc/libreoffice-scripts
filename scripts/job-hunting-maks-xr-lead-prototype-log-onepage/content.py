"""Prototype Log of Maks Kovač: who they are and everything the document
could say. The typesetting keeps what fits into one page, the most important
first."""

PERSONA = {
    "name": "Maks Kovač",
    "headline": "XR developer and former founder · virtual rooms where "
                "real hands learn real skills",
    "contact": ["Zagreb, Croatia", "maks@kovac.example",
                "+385 91 555 7403", "makskovac.xyz"],
}


DOCUMENT = {
    "title": "Prototype Log",
    "subtitle": "Ten years of XR prototypes: the hypothesis, the build, "
                "the verdict · including the ones that killed the company",
    "sections": [
        {"kind": "text", "weight": 0.2, "step": 4, "paragraphs": [
            "I keep a log of every prototype: what I believed, what I "
            "built to test it, and what happened. It has stopped me from "
            "repeating mistakes, mostly. These are the entries I would "
            "want a future colleague to read before working with me.",
        ]},
        {"heading": "Torch", "kind": "entries", "weight": 0.5, "step": 1,
         "inner": 0.8, "entries": [
             {"title": "Halo XR, 2019", "fields": [
                 ("Hypothesis", "welding students learn faster if the "
                                "controller weighs and feels like a real "
                                "torch."),
                 ("Build", "a 3D-printed torch with a weight, a trigger "
                           "and an optical tracker; two weeks."),
                 ("Verdict", "true; instructors stopped calling it a "
                             "game the moment they held it."),
             ]},
         ]},
        {"heading": "Sparks", "kind": "entries", "weight": 1, "step": 1,
         "inner": 0.8, "entries": [
             {"title": "Halo XR, 2019", "fields": [
                 ("Hypothesis", "visual realism matters for learning."),
                 ("Build", "sparks, heat shimmer and a glowing weld "
                           "pool."),
                 ("Verdict", "mostly false for learning, true for "
                             "selling; students learned the same with "
                             "simple visuals, but buyers wanted sparks."),
             ]},
         ]},
        {"heading": "School pricing", "kind": "entries", "weight": 1.6,
         "step": 1, "inner": 0.8, "entries": [
             {"title": "Halo XR, 2021", "fields": [
                 ("Hypothesis", "vocational schools will pay a yearly "
                                "subscription."),
                 ("Build", "a pricing page and twenty sales calls."),
                 ("Verdict", "false; budgets are yearly grants for "
                             "equipment, not subscriptions. The prototype "
                             "that should have come first."),
             ]},
         ]},
        {"heading": "Shipyard custom", "kind": "entries", "weight": 2.2,
         "step": 1, "inner": 0.8, "entries": [
             {"title": "Halo XR, 2022", "fields": [
                 ("Hypothesis", "shipyards will pay for custom training "
                                "scenarios."),
                 ("Build", "one custom hull-section scenario in eight "
                           "weeks."),
                 ("Verdict", "true, and fatal; every shipyard wanted its "
                             "own, and we could not build them fast "
                             "enough to survive."),
             ]},
         ]},
        {"heading": "Needle", "kind": "entries", "weight": 2.8, "step": 1,
         "inner": 0.8, "entries": [
             {"title": "Medilab, 2025", "fields": [
                 ("Hypothesis", "force feedback at the needle tip "
                                "improves first-pass success."),
                 ("Build", "a modified haptic stylus with a needle "
                           "attachment; ultrasound simulated from CT "
                           "data."),
                 ("Verdict", "true; 55 to 78 % first-pass success in the "
                             "skills lab. Consultants asked for it "
                             "again."),
             ]},
         ]},
        {"heading": "Thread", "kind": "entries", "weight": 3.2, "step": 1,
         "inner": 0.8, "min_pages": 2, "entries": [
             {"title": "personal, 2026", "fields": [
                 ("Hypothesis", "knot tension can be taught with a cheap "
                                "haptic thread."),
                 ("Build", "a spool, a load cell and a small motor on my "
                           "desk."),
                 ("Verdict", "unknown; needs surgeons. That is why I am "
                             "applying."),
             ]},
         ]},
        {"heading": "Tremor", "kind": "entries", "weight": 3.3, "step": 1,
         "inner": 0.8, "min_pages": 2, "entries": [
             {"title": "Medilab, 2025", "fields": [
                 ("Hypothesis", "measuring hand tremor helps residents "
                                "see their own progress."),
                 ("Build", "tremor amplitude from controller data, "
                           "shown after each attempt as a simple line."),
                 ("Verdict", "true, with care; residents were motivated, "
                             "but we hid the number during the attempt "
                             "because it made them more nervous."),
             ]},
         ]},
        {"heading": "Theatre noise", "kind": "entries", "weight": 3.4,
         "step": 1, "inner": 0.8, "min_pages": 4, "entries": [
             {"title": "Medilab, 2026", "fields": [
                 ("Hypothesis", "realistic theatre sound and "
                                "interruptions prepare residents for "
                                "real pressure."),
                 ("Build", "monitors, a scrub nurse's questions and a "
                           "pager at random moments."),
                 ("Verdict", "partly true; useful for advanced "
                             "residents, overwhelming for beginners. Now "
                             "a difficulty setting."),
             ]},
         ]},
        {"heading": "Headset hygiene", "kind": "entries", "weight": 3.45,
         "step": 1, "inner": 0.8, "min_pages": 4, "entries": [
             {"title": "Halo XR, 2020", "fields": [
                 ("Hypothesis", "schools will share headsets between "
                                "classes without problems."),
                 ("Build", "nothing; we just shipped."),
                 ("Verdict", "false; the pandemic arrived and every "
                             "school asked how to clean them. We added "
                             "washable covers and a UV cabinet. For "
                             "hospitals, hygiene is the first "
                             "requirement, not the last."),
             ]},
         ]},
        {"heading": "Instructor dashboard", "kind": "entries",
         "weight": 3.5, "step": 1, "inner": 0.8, "min_pages": 4,
         "entries": [
             {"title": "Halo XR, 2021", "fields": [
                 ("Hypothesis", "instructors want detailed analytics of "
                                "every student."),
                 ("Build", "a dashboard with twenty charts."),
                 ("Verdict", "false; they wanted one list: who needs "
                             "help today. We deleted nineteen charts "
                             "and usage tripled."),
             ]},
         ]},
        {"heading": "Rules from the log", "kind": "bullets", "weight": 3.6,
         "step": 0.4, "min_pages": 2, "items": [
             "Prototype the business before the product.",
             "Hands first, pixels later.",
             "One hypothesis per prototype.",
             "Write the verdict before you start; then check it "
             "honestly.",
             "Keep the prototypes that failed; they are the cheapest "
             "lessons.",
         ]},
        {"heading": "Nausea", "kind": "entries", "weight": 3.0, "step": 1,
         "inner": 0.8, "min_pages": 2, "entries": [
             {"title": "Pixel Forge, 2015", "fields": [
                 ("Hypothesis", "players will tolerate smooth locomotion "
                                "in VR."),
                 ("Build", "a corridor and a joystick."),
                 ("Verdict", "false; half the testers had to lie down. "
                             "Every simulator I have built since keeps "
                             "the learner's body still."),
             ]},
         ]},
        {"heading": "Meet inside", "kind": "entries", "weight": 4.2,
         "step": 1, "inner": 0.8, "min_pages": 4, "entries": [
             {"title": "Arhitekt Vizual, 2018", "fields": [
                 ("Hypothesis", "clients decide faster when they stand "
                                "inside a design with the architect."),
                 ("Build", "a multi-user walkthrough with avatars, a "
                           "laser pointer and a tape measure."),
                 ("Verdict", "true; review meetings shortened by half, "
                             "and two clients changed their kitchens "
                             "before construction instead of after."),
             ]},
         ]},
        {"heading": "Ghost hand", "kind": "entries", "weight": 4.4,
         "step": 1, "inner": 0.8, "min_pages": 4, "entries": [
             {"title": "Halo XR, 2020", "fields": [
                 ("Hypothesis", "showing the instructor's recorded hand "
                                "as a ghost helps students copy the "
                                "movement."),
                 ("Build", "motion capture of three instructors, played "
                           "back as a translucent hand."),
                 ("Verdict", "true for beginners, distracting for "
                             "advanced students; we made it fade out as "
                             "scores improved."),
             ]},
         ]},
    ],
}
