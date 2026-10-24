"""Curriculum Vitae of Yuki Mori: who they are and everything the document
could say. The typesetting keeps what fits into one page, the most important
first."""

PERSONA = {
    "name": "Yuki Mori",
    "headline": "Sound designer and audio programmer · twelve years of "
                "footsteps, engines and the silence between them",
    "contact": ["Stuttgart, Germany", "yuki.mori@example.de",
                "+49 176 5550 2291", "yukimori.audio"],
}


DOCUMENT = {
    "title": "Curriculum Vitae",
    "cv": True,
    "sections": [
        {"heading": "Overture", "kind": "text", "weight": 0.4, "step": 5,
         "paragraphs": [
             "Sound designer and audio programmer with twelve years in "
             "games, from a mobile racing game to a large open-world "
             "title. I design sounds that tell people what is happening "
             "before they look: a footstep that says “ice”, an engine "
             "that says “too fast”, a door that says “locked”. I also "
             "write the systems that play them, in Wwise, FMOD and C++.",
             "Before games I spent two years as a piano tuner in Kyoto, "
             "and in 2021 a year caring for my mother. I am now moving "
             "into automotive sound, where electric cars need a voice "
             "that is safe, pleasant and unmistakably theirs.",
         ]},
        {"heading": "Experience", "kind": "entries", "weight": 1,
         "step": 1.2, "entries": [
             {"title": "Senior sound designer and audio programmer",
              "org": "Rheinwerk Interactive", "dates": "2022 – now",
              "meta": "Stuttgart · open-world driving game",
              "items": [
                  "Lead for vehicle audio: 64 cars, each with a granular "
                  "engine model built from on-board recordings.",
                  "Designed the electric vehicle sounds of the game, "
                  "which players rated the most realistic in a survey "
                  "of 12,000.",
                  "Wrote a Wwise plug-in for tyre and road surface "
                  "sounds driven by real friction data.",
                  "Cut audio memory use by 40 % on consoles with a new "
                  "streaming strategy.",
              ],
              "story": [
                  "Recording cars for the game took me to test tracks "
                  "all over Germany, with microphones taped to exhausts, "
                  "engine bays and the inside of door panels. The most "
                  "interesting recordings were the electric cars: quiet "
                  "at first, and then full of tiny sounds no one had "
                  "designed, inverters whining, relays clicking, tyres "
                  "hissing. That is when I started to think about "
                  "designing them properly.",
              ]},
             {"title": "Rest: caring for my mother", "dates": "2021",
              "meta": "Kyoto · one year",
              "items": [
                  "Returned to Japan to care for my mother after a "
                  "stroke; she recovered well.",
                  "Recorded the sounds of her neighbourhood for a "
                  "personal archive, which became a small album.",
              ]},
             {"title": "Sound designer", "org": "Kumo Games",
              "dates": "2016 – 2020", "meta": "Tokyo · console action "
                                              "games",
              "story": [
                  "At Kumo I learned foley properly: celery for bones, "
                  "leather gloves for wings, a week of dawns at a "
                  "mountain shrine for one ambience. My lead taught me "
                  "that a sound is a promise to the player and must "
                  "never lie about what happened.",
              ],
              "items": [
                  "Footsteps, cloth, weapons and creatures for two action "
                  "games; 3,000 sounds in total.",
                  "Built a footstep system with 18 surfaces and 4 "
                  "shoe types that adapts to the character's speed.",
                  "Recorded foley in the studio and in the field, "
                  "including a week in a Shinto shrine at dawn.",
              ]},
             {"title": "Rest: piano tuner", "dates": "2014 – 2016",
              "meta": "Kyoto · apprenticeship and work",
              "items": [
                  "Left my first job and trained as a piano tuner with a "
                  "master in Kyoto; tuned about 900 pianos.",
                  "Learned to hear beats between frequencies, which is "
                  "the most useful skill I have.",
              ],
              "story": [
                  "I left my first games job exhausted and unsure. My "
                  "uncle knew an old piano tuner who needed an "
                  "apprentice, and for two years I drove around Kyoto "
                  "listening to the beating of slightly wrong strings. "
                  "When I returned to sound design, I could hear things "
                  "other designers could not, and I was much calmer.",
              ]},
             {"title": "Junior sound designer", "org": "Pocket Velocity",
              "dates": "2012 – 2014", "meta": "Tokyo · mobile racing",
              "story": [
                  "My first job: tiny engines for tiny speakers. A phone "
                  "cannot play bass, so I learned to suggest a big "
                  "engine with harmonics alone, a trick I still use.",
              ],
              "items": [
                  "Engine and UI sounds for a mobile racing game with 20 "
                  "million downloads.",
              ]},
         ]},
        {"heading": "Craft", "kind": "tags", "weight": 1.6, "step": 0.5,
         "items": [
             ("Sound design", "vehicles, foley, UI, ambiences, creatures"),
             ("Middleware", "Wwise, FMOD, Unreal MetaSounds"),
             ("Programming", "C++, Python, DSP basics, Wwise plug-ins"),
             ("Recording", "field and vehicle recording, foley, "
                           "binaural"),
             ("Listening", "tuning, psychoacoustics, loudness standards"),
         ]},
        {"heading": "Education", "kind": "entries", "weight": 2.2,
         "step": 1, "entries": [
             {"title": "BA Musical Creativity and the Environment",
              "org": "Tokyo University of the Arts", "dates": "2008 – "
              "2012", "items": []},
             {"title": "Piano tuning apprenticeship", "org": "Kyoto",
              "dates": "2014 – 2016", "items": []},
             {"title": "Automotive acoustics short course", "org": "TU "
              "Berlin", "dates": "2025", "meta": "NVH and AVAS regulations",
              "items": []},
         ]},
        {"heading": "Credits", "kind": "bullets", "weight": 2.8,
         "step": 0.4, "items": [
             "*Autobahn Nights* (PC, consoles), 2025 · vehicle audio "
             "lead.",
             "*Shrine of Ash* (PS4), 2019 · sound designer.",
             "*Ronin Run* (PS4, Switch), 2017 · sound designer.",
             "*Pocket Velocity GT* (mobile), 2013 · junior sound "
             "designer.",
         ]},
        {"heading": "Awards", "kind": "bullets", "weight": 3.4,
         "step": 0.4, "items": [
             "Game Audio Network Guild, Best Sound Design nomination, "
             "*Autobahn Nights*, 2026.",
             "Japan Game Awards, sound category, *Shrine of Ash*, "
             "finalist, 2019.",
         ]},
        {"heading": "Languages", "kind": "tags", "weight": 4, "step": 0.3,
         "items": [("Japanese", "native"), ("English", "fluent"),
                   ("German", "B2, improving at the test track")]},
        {"heading": "Recordings", "kind": "bullets", "weight": 5,
         "step": 0.4, "min_pages": 4, "items": [
             "*Okaasan no machi* (2021), an album of the sounds of my "
             "mother's neighbourhood in Kyoto.",
             "A library of 40 electric vehicles recorded inside and out, "
             "2023 – 2025.",
             "Dawn at Fushimi Inari, 3 hours binaural, 2018.",
         ]},
        {"heading": "Talks", "kind": "bullets", "weight": 5.4, "step": 0.3,
         "min_pages": 4, "items": [
             "“The sound of electric silence”, GDC audio summit, 2025.",
             "“What a piano tuner hears”, Audiokinetic Wwise Tour, 2023.",
             "“Footsteps on 18 surfaces”, CEDEC Yokohama, 2018.",
         ]},
        {"heading": "Regulations and Standards", "kind": "bullets",
         "weight": 5.8, "step": 0.3, "min_pages": 4, "items": [
             "UN Regulation 138 (AVAS) and EU 540/2014, studied in the TU "
             "Berlin course.",
             "Loudness: EBU R128 and ITU-R BS.1770 for game mixes.",
             "Accessibility guidance for sound in games, Game "
             "Accessibility Guidelines.",
         ]},
        {"heading": "Teaching", "kind": "bullets", "weight": 6.0,
         "step": 0.3, "min_pages": 4, "items": [
             "Guest lecturer, game audio, Hochschule der Medien "
             "Stuttgart, 2023 – now.",
             "Mentor, Game Audio Network Guild mentorship programme, "
             "2024.",
         ]},
        {"heading": "Interests", "kind": "text", "weight": 6.5,
         "paragraphs": [
             "Tuning old pianos for friends, recording rain on different "
             "roofs, Swabian bakeries, long train journeys with "
             "headphones and the sound of the Stuttgart funicular.",
         ]},
        {"heading": "References", "kind": "entries", "weight": 7,
         "min_pages": 4, "entries": [
             {"title": "Jan Becker", "org": "Audio director, Rheinwerk "
              "Interactive", "meta": "on request", "items": []},
             {"title": "Hiroshi Tanabe", "org": "Piano tuner, Kyoto",
              "meta": "my teacher; speaks Japanese only", "items": []},
         ]},
    ],
}
