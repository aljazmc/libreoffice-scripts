"""Cover Letter of Nika Zupan: who they are and everything the document
could say. The typesetting keeps what fits into four pages, the most important
first."""

PERSONA = {
    "name": "Nika Zupan",
    "headline": "creative coder · generative systems, light and the "
                "occasional runaway particle",
    "contact": ["Ljubljana", "nika@zupan.example", "+386 31 555 904",
                "nikazupan.art"],
}


DOCUMENT = {
    "title": "Cover Letter",
    "date": "Ljubljana, 24 October 2026",
    "recipient": ["Dr. Eva Hrovat", "Head of Exhibitions",
                  "Hiša eksperimentov", "Trubarjeva cesta 39",
                  "1000 Ljubljana"],
    "subject": "Creative Technologist, new permanent exhibition on light",
    "salutation": "Dear Dr. Hrovat,",
    "signoff": "exit 0, and kind regards,",
    "sections": [
        {"kind": "text", "weight": 0, "step": 0.4, "paragraphs": [
            "The first installation I ever finished was a lamp that "
            "brightened when you spoke to it. I built it for my thesis, "
            "and the visitor who loved it most was a seven-year-old who "
            "spent twenty minutes trying to make it angry. I am applying "
            "for the Creative Technologist position because I want to "
            "build things for that seven-year-old, every day, in a place "
            "where the installation also has to be true.",
        ]},
        {"heading": "What I make", "kind": "text", "weight": 1,
         "step": 3, "paragraphs": [
             "For nine years I have built interactive installations: "
             "projections that follow river data, rooms that breathe "
             "with visitors and floors that scatter fish when children "
             "step on them. I write the code, wire the sensors and stay "
             "on site until things run without me. Breathing Room "
             "received an honorary mention at Prix Ars Electronica last "
             "year; the aquarium floor in Piran has run eleven hours a "
             "day for almost two years.",
             "At Studio Lumina I led the development of fourteen "
             "projection shows and rebuilt the studio's pipeline from "
             "pre-rendered video to real-time graphics. That is where I "
             "learned to work with producers, budgets and opening "
             "nights that do not move.",
         ]},
        {"heading": "Why a science museum", "kind": "text", "weight": 1.4,
         "step": 3, "paragraphs": [
             "Art festivals let me make beautiful things. A science "
             "museum would ask me to make beautiful things that are "
             "also correct, and I find that constraint exciting. When I "
             "built Tidal from hydrology data, the best moment was not "
             "the applause but a hydrologist telling me that the light "
             "rose a day before the river, exactly as it should.",
             "Your new exhibition on light is the subject I have spent "
             "my career on. I know how LEDs lie about colour, how "
             "projectors fail in sunlight and how a child's hand can "
             "become a lens. I would love to turn that knowledge into "
             "exhibits that teach optics without a single paragraph of "
             "wall text.",
         ]},
        {"heading": "About the gaps", "kind": "text", "weight": 1.8,
         "step": 3, "paragraphs": [
             "My CV has two gaps, and both were deliberate. In 2017 and "
             "2018 I spent nine months in residencies in Rijeka and "
             "Linz, building my first sensor installations. In 2022 I "
             "took a year off after burning out at the end of two years "
             "of seventy-hour weeks.",
             "The second gap taught me more than any job. I came back "
             "with honest estimates, a habit of documenting everything "
             "and the conviction that a reliable installation is "
             "designed in the calm weeks, not fixed in the panicked "
             "nights. I mention it because I think a museum, which needs "
             "exhibits that work for ten years, should know that I "
             "learned it the hard way.",
         ]},
        {"heading": "How I build things that last", "kind": "text",
         "weight": 2.4, "step": 3, "paragraphs": [
             "Every installation I ship has a watchdog that restarts it, "
             "a remote log I can read from my phone, a hidden power "
             "switch and a one-page manual for the person who opens the "
             "room in the morning. I test with real visitors, especially "
             "children, before opening night, and I design every "
             "interaction to survive being hit, licked and ignored.",
             "I also believe exhibits should be repairable by your own "
             "technicians. I prefer common hardware, open software and "
             "documentation written for someone who has never met me.",
         ]},
        {"heading": "A first idea", "kind": "text", "weight": 3,
         "step": 3, "min_pages": 2, "paragraphs": [
             "One exhibit I would love to build with your team: a dark "
             "room with a single beam of light and a table of objects, "
             "lenses, prisms, water and a child's own hand, where a "
             "camera above shows the beam's path as a glowing line. "
             "Visitors would see refraction instead of reading about it, "
             "and the line would stay on the wall for a minute after they "
             "leave, so the next visitor can follow it.",
             "It is only a sketch, and your educators will know better "
             "which questions children actually ask. I would start by "
             "spending days on your exhibition floor, listening to them.",
         ]},
        {"heading": "Working with educators", "kind": "text",
         "weight": 3.4, "step": 3, "min_pages": 4, "paragraphs": [
             "I have taught creative coding to four hundred students and "
             "teachers, and last year I ran a course for science "
             "teachers at the National Education Institute. Teachers "
             "taught me that a good exhibit has one idea, one action and "
             "one surprise; anything more is for the next room.",
             "I would like to work with your educators from the first "
             "sketch, not after the exhibit is built, and to test "
             "prototypes with school groups on the floor every week.",
         ]},
        {"heading": "The first year", "kind": "text", "weight": 3.8,
         "step": 3, "min_pages": 4, "paragraphs": [
             "In the first three months I would learn your existing "
             "exhibits from the inside: how they fail, who repairs them "
             "and what visitors do with them. I would also build a "
             "simple monitoring system so that we know which exhibit "
             "is broken before a visitor tells us.",
             "In the rest of the year I would prototype the light "
             "exhibits in the open, on a cart on the exhibition floor, "
             "with visitors as co-designers. By the opening, every "
             "exhibit should have been broken by at least a hundred "
             "children and fixed so that it does not break again.",
         ]},
        {"heading": "Accessibility", "kind": "text", "weight": 4.0,
         "step": 3, "min_pages": 4, "paragraphs": [
             "Light exhibits can exclude people quietly: visitors with low "
             "vision, with epilepsy, in wheelchairs that cannot reach the "
             "sweet spot of a sensor. I design for them from the first "
             "sketch, with flash limits below the guidelines, sound "
             "alongside light, and interactions that work at every "
             "height.",
             "Breathing Room has a version for visitors who cannot wear "
             "the chest band, which reads breathing from a small "
             "microphone instead. It was the version most people chose.",
         ]},
        {"heading": "Why now", "kind": "text", "weight": 4.1, "step": 3,
         "min_pages": 4, "paragraphs": [
             "Freelancing has given me freedom and variety, but every "
             "project ends at the opening night, just when I start to "
             "learn how people really use it. I want to stay for the "
             "second year of an exhibit, and the fifth, and to improve it "
             "from what visitors teach us. A museum is the only place "
             "where installations live that long.",
         ]},
        {"heading": "Questions I would ask you", "kind": "bullets",
         "weight": 4.2, "step": 1, "min_pages": 4, "items": [
             "Which current exhibit breaks most often, and why?",
             "How do educators and the technical team work together "
             "today?",
             "How long should a new exhibit last, and who maintains it "
             "after opening?",
             "What do visitors ask about light that your exhibits do not "
             "answer yet?",
         ]},
        {"heading": "What I ask", "kind": "text", "weight": 4.4,
         "step": 3, "min_pages": 2, "paragraphs": [
             "Full-time, from January 2027. After years of freelancing I "
             "would love a team, a workshop and colleagues to argue with "
             "about colour temperature.",
         ]},
        {"kind": "text", "weight": 0.2, "step": 6, "paragraphs": [
            "Thank you for reading. I would be glad to show you Breathing "
            "Room on my laptop, or better, to bring the lamp from my "
            "thesis, which still brightens when you talk to it and still "
            "cannot be made angry.",
        ]},
    ],
}
