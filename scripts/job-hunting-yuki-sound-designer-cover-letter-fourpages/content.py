"""Cover Letter of Yuki Mori: who they are and everything the document
could say. The typesetting keeps what fits into four pages, the most important
first."""

PERSONA = {
    "name": "Yuki Mori",
    "headline": "Sound designer and audio programmer · twelve years of "
                "footsteps, engines and the silence between them",
    "contact": ["Stuttgart, Germany", "yuki.mori@example.de",
                "+49 176 5550 2291", "yukimori.audio"],
}


DOCUMENT = {
    "title": "Cover Letter",
    "date": "Stuttgart, 24 October 2026",
    "recipient": ["Dr. Katrin Vogt", "Head of Sound and Acoustics",
                  "Kessler Automobilwerke AG", "Mercedesstraße 120",
                  "70372 Stuttgart"],
    "subject": "Sound Designer, Acoustic Vehicle Alerting and Brand Sound",
    "salutation": "Dear Dr. Vogt,",
    "signoff": "With kind regards,",
    "sections": [
        {"kind": "text", "weight": 0, "step": 0.4, "paragraphs": [
            "An electric car at walking speed must make a sound, by law, "
            "so that a blind pedestrian knows it is there. That sound is "
            "heard by more people than any jingle and is designed by very "
            "few. I am applying for the Sound Designer position in your "
            "acoustics team because I want to design it: a sound that is "
            "safe, kind to the city and recognisably Kessler.",
        ]},
        {"heading": "What I bring", "kind": "text", "weight": 1,
         "step": 3, "paragraphs": [
             "I have designed sound for games for twelve years, the last "
             "four as vehicle audio lead on an open-world driving game "
             "with 64 cars. I recorded engines on test tracks, built "
             "granular engine models and designed the game's electric "
             "vehicle sounds, which players rated the most realistic in "
             "a survey of twelve thousand.",
             "I am also an audio programmer. I write Wwise plug-ins and "
             "C++ systems that make sounds react to speed, load and road "
             "surface in real time, which is exactly what an acoustic "
             "vehicle alerting system must do, with stricter rules.",
         ]},
        {"heading": "Why automotive", "kind": "text", "weight": 1.4,
         "step": 3, "paragraphs": [
             "Games are wonderful, but their sounds live inside "
             "headphones. A car's alerting sound lives in streets, among "
             "children, cyclists and people who cannot see. I find that "
             "responsibility exciting. The sound must be detectable "
             "without being aggressive, must meet UN regulation 138 and "
             "must still feel like it belongs to the brand.",
             "Last year I completed a short course in automotive "
             "acoustics at TU Berlin, covering NVH, AVAS regulations and "
             "measurement, and I have recorded forty electric vehicles "
             "for my own library.",
         ]},
        {"heading": "The rests in my score", "kind": "text", "weight": 1.8,
         "step": 3, "paragraphs": [
             "My CV has two pauses. From 2014 to 2016 I trained and "
             "worked as a piano tuner in Kyoto, after leaving my first "
             "games job exhausted. In 2021 I spent a year caring for my "
             "mother after her stroke.",
             "The first pause gave me my ears. Tuning nine hundred pianos "
             "taught me to hear beating between frequencies and the "
             "smallest roughness in a tone, which is precisely what "
             "makes an alerting sound pleasant or annoying. The second "
             "taught me to listen to a city slowly, street by street, "
             "which I think every designer of urban sounds should do.",
         ]},
        {"heading": "Why Kessler", "kind": "text", "weight": 2.4,
         "step": 3, "min_pages": 2, "paragraphs": [
             "Your new electric saloon is the quietest car I have "
             "recorded, and its alerting sound is the most considerate "
             "I have heard: it rises gently, never beeps and almost "
             "disappears above thirty kilometres an hour. I would love to "
             "work with the team that made it, and to help shape what "
             "comes next.",
         ]},
        {"heading": "A first sketch", "kind": "text", "weight": 3,
         "step": 3, "min_pages": 4, "paragraphs": [
             "For a brand sound I would start from the fundamental of "
             "the car's own electric drive, the whine its inverter makes "
             "anyway, and build a chord on it with two quiet partials "
             "that change with speed. It would be harmonic rather than "
             "noisy, which makes it easier to locate, and tuned slightly "
             "away from the common frequencies of other brands, so that "
             "a street full of electric cars does not become one big "
             "drone.",
             "I would test early prototypes with blind and partially "
             "sighted pedestrians, with cyclists and in a real street at "
             "night, not only in an anechoic chamber.",
         ]},
        {"heading": "How I work with engineers", "kind": "text",
         "weight": 3.4, "step": 3, "min_pages": 4, "paragraphs": [
             "In games I sat between composers and programmers; I speak "
             "both languages. I am comfortable with measurements, "
             "spectrograms and regulations, and I enjoy explaining to an "
             "engineer why a sound that meets every number can still be "
             "unpleasant, and then finding a version that is both.",
         ]},
        {"heading": "Listening to cities", "kind": "text", "weight": 2.0,
         "step": 3, "paragraphs": [
             "A vehicle sound does not live alone. It joins buses, "
             "trams, birds, building sites and other cars. In 2021 I "
             "recorded my mother's Kyoto neighbourhood at every hour of "
             "the day, and since moving to Stuttgart I have recorded "
             "twenty streets at walking speed, from Königstraße at noon "
             "to a quiet residential street in Degerloch at night. The "
             "differences are enormous, and they matter for how a car "
             "should sound.",
             "I believe the best alerting sound is the quietest one that "
             "is still reliably detected, and that it should adapt to "
             "its surroundings within the limits of the regulation.",
         ]},
        {"heading": "Safety first, then character", "kind": "text",
         "weight": 2.2, "step": 3, "paragraphs": [
             "An alerting sound has a hierarchy of duties. First, a "
             "pedestrian must hear it, locate it and judge its speed. "
             "Second, it must not add to the noise of a city or wake "
             "anyone at night. Only third should it carry the brand. I "
             "would design in that order, and test in that order.",
             "Games taught me how much information a sound can carry: "
             "speed, direction, weight, even mood. Used carefully, that "
             "same richness can make a car easier to understand for a "
             "blind pedestrian, not only nicer for its driver.",
         ]},
        {"heading": "Inside the car", "kind": "text", "weight": 3.5,
         "step": 3, "min_pages": 4, "paragraphs": [
             "I would also love to work on interior sounds: indicator "
             "clicks, warning chimes and the sounds of the interface. In "
             "games I designed hundreds of interface sounds that players "
             "heard thousands of times; the lessons transfer directly. "
             "A warning should be urgent without being frightening, and "
             "an indicator should be heard but never noticed.",
         ]},
        {"heading": "Questions I would ask", "kind": "bullets",
         "weight": 3.6, "step": 1, "min_pages": 4, "items": [
             "How are alerting sounds tested with blind and partially "
             "sighted pedestrians today?",
             "How do sound design and NVH engineering share decisions?",
             "How much should a brand sound change between models?",
             "Which sound in your current cars would you most like to "
             "redo?",
         ]},
        {"heading": "Practical details", "kind": "text", "weight": 3.8,
         "step": 3, "min_pages": 2, "paragraphs": [
             "I live in Stuttgart, can start in February 2027 and hold a "
             "permanent residence permit. My German is good enough for "
             "test tracks and improving for meetings.",
         ]},
        {"kind": "text", "weight": 0.2, "step": 6, "paragraphs": [
            "Thank you for listening, so to speak. I would be glad to "
            "play you my electric vehicle recordings and the first sketch "
            "of a brand sound, ideally through good speakers and then "
            "through a real street.",
        ]},
    ],
}
