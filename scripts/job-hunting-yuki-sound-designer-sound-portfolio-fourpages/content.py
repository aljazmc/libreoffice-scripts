"""Sound Portfolio of Yuki Mori: who they are and everything the document
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
    "title": "Sound Portfolio",
    "subtitle": "A tracklist of sounds, with how each was made and why "
                "it sounds the way it does",
    "sections": [
        {"kind": "text", "weight": 0.2, "step": 4, "paragraphs": [
            "Sound is hard to show on paper, so this portfolio is a "
            "tracklist with liner notes. Each track can be heard at "
            "yukimori.audio. The notes describe the problem, the "
            "recipe and what I would change. Please listen with "
            "headphones, and then once more through a laptop speaker, "
            "because that is how most people will hear it.",
        ]},
        {"heading": "Electric, approaching", "kind": "entries",
         "weight": 0.5, "step": 1, "inner": 0.8, "entries": [
             {"title": "Autobahn Nights, 2025", "org": "0:42",
              "fields": [
                  ("Problem", "players could not hear electric cars "
                              "approaching from behind and crashed into "
                              "them."),
                  ("Recipe", "the car's recorded inverter whine, "
                             "pitch-tracked to speed, plus two soft sine "
                             "partials a fifth and an octave above; "
                             "Doppler and distance filtering in Wwise."),
                  ("Result", "rated most realistic EV sound by players; "
                             "rear-end crashes in the beta fell by a "
                             "third."),
                  ("Change", "less brightness above 4 kHz; it tired the "
                             "ear on long drives."),
              ]},
         ]},
        {"heading": "Eighteen surfaces", "kind": "entries", "weight": 1,
         "step": 1, "inner": 0.8, "entries": [
             {"title": "Shrine of Ash, 2019", "org": "1:20",
              "fields": [
                  ("Problem", "footsteps all sounded the same, so "
                              "players could not feel where they were."),
                  ("Recipe", "eighteen surfaces, four shoe types, "
                             "speed-dependent heel and toe layers; 1,100 "
                             "recordings."),
                  ("Result", "players found hidden paths by listening, "
                             "which became a design feature."),
              ]},
         ]},
        {"heading": "Okaasan no machi", "kind": "entries", "weight": 1.6,
         "step": 1, "inner": 0.8, "entries": [
             {"title": "personal album, 2021", "org": "38:00",
              "fields": [
                  ("Context", "a year caring for my mother in Kyoto."),
                  ("Recipe", "binaural recordings of her neighbourhood: "
                             "the tofu seller's horn, the level crossing, "
                             "rain on a tin roof."),
                  ("Why here", "it taught me how a street sounds at every "
                               "hour, which is what an urban vehicle "
                               "sound must fit into."),
              ]},
         ]},
        {"heading": "Locked door", "kind": "entries", "weight": 2.2,
         "step": 1, "inner": 0.8, "entries": [
             {"title": "Ronin Run, 2017", "org": "0:03",
              "fields": [
                  ("Problem", "players kept trying locked doors."),
                  ("Recipe", "a dry wooden knock with a short metallic "
                             "rattle, under 300 milliseconds."),
                  ("Lesson", "a sound can say “no” more kindly than a "
                             "message on screen."),
              ]},
         ]},
        {"heading": "A piano, slightly wrong", "kind": "entries",
         "weight": 2.8, "step": 1, "inner": 0.8, "entries": [
             {"title": "study, 2015", "org": "2:10",
              "fields": [
                  ("Context", "a recording from my tuning years: the "
                              "same chord before and after tuning."),
                  ("Why here", "it shows what I listen for: the beating "
                               "that makes a sound restless or calm."),
              ]},
         ]},
        {"heading": "Brand sound sketch", "kind": "entries", "weight": 3.2,
         "step": 1, "inner": 0.8, "min_pages": 2, "entries": [
             {"title": "for Kessler, 2026", "org": "1:30",
              "fields": [
                  ("Idea", "the drive's own whine as the root, two quiet "
                           "partials as a chord, rising with speed and "
                           "fading above 30 km/h."),
                  ("Constraints", "UN R138 minimum levels, detectability "
                                  "for blind pedestrians, no beeps."),
                  ("Status", "a sketch; it would need testing in real "
                             "streets."),
              ]},
         ]},
        {"heading": "Tyres on wet cobblestones", "kind": "entries",
         "weight": 3.3, "step": 1, "inner": 0.8, "min_pages": 4,
         "entries": [
             {"title": "Autobahn Nights, 2024", "org": "0:55",
              "fields": [
                  ("Problem", "tyre sounds were looped samples that "
                              "repeated noticeably on long drives."),
                  ("Recipe", "a Wwise plug-in that synthesises tyre "
                             "noise from slip and surface data, layered "
                             "with short recorded grains."),
                  ("Result", "no audible loops; memory use down by 40 % "
                             "on consoles."),
              ]},
         ]},
        {"heading": "Indicator", "kind": "entries", "weight": 3.4,
         "step": 1, "inner": 0.8, "min_pages": 4, "entries": [
             {"title": "study, 2026", "org": "0:20",
              "fields": [
                  ("Problem", "most indicator clicks are either too "
                              "quiet for older drivers or irritating on "
                              "long drives."),
                  ("Recipe", "a wooden tick and a softer tock, recorded "
                             "from a metronome and a temple block, with "
                             "level that follows cabin noise."),
                  ("Status", "a study for my application, tested with "
                             "five drivers of different ages."),
              ]},
         ]},
        {"heading": "Night street, Degerloch", "kind": "entries",
         "weight": 3.5, "step": 1, "inner": 0.8, "min_pages": 4,
         "entries": [
             {"title": "field recording, 2025", "org": "5:00",
              "fields": [
                  ("Context", "a quiet residential street at 23:00, with "
                              "three electric cars passing at 15 km/h."),
                  ("Why here", "you can hear which alerting sounds "
                               "disturb and which blend in; one of them "
                               "is Kessler's."),
              ]},
         ]},
        {"heading": "Liner notes on listening", "kind": "bullets",
         "weight": 3.6, "step": 0.4, "min_pages": 2, "items": [
             "Listen at low volume first; most sounds are heard quietly.",
             "Then on a phone speaker, where bass disappears.",
             "Then in a noisy room; a good sound survives.",
             "Then once more after a day; annoyance takes time.",
         ]},
        {"heading": "Sounds that were cut", "kind": "bullets", "weight": 4,
         "step": 0.4, "min_pages": 4, "items": [
             "A spaceship-like EV sound that players loved for a minute "
             "and hated after ten.",
             "Thunder recorded in Kyoto, replaced by a library sound "
             "because the real one sounded fake.",
             "A footstep on snow that was in fact cornflour in a bag; "
             "too good, it distracted the testers.",
         ]},
        {"heading": "Collaborators", "kind": "bullets", "weight": 4.2,
         "step": 0.4, "min_pages": 4, "items": [
             "Jan Becker, audio director, who taught me to mix for the "
             "worst speaker first.",
             "The test drivers at Contidrom, who let me tape microphones "
             "to their cars and their patience.",
             "A group of blind pedestrians in Stuttgart who tested my "
             "alerting sketches and told me exactly what they heard.",
         ]},
        {"heading": "Equipment", "kind": "tags", "weight": 4.4, "step": 0.3,
         "min_pages": 4, "items": [
             ("Microphones", "Sennheiser MKH 8040 pair, DPA 4060 for "
                             "engine bays, contact microphones"),
             ("Recorder", "Sound Devices MixPre-10 II"),
             ("Software", "Reaper, Wwise, FMOD, iZotope RX"),
             ("Tuning", "a tuning hammer from my teacher in Kyoto"),
         ]},
        {"heading": "What I listen for", "kind": "text", "weight": 4.8,
         "step": 3, "min_pages": 4, "paragraphs": [
             "When I evaluate a sound I ask three questions, in order. "
             "Is it understood: does a listener know what is happening "
             "without looking? Is it bearable: would you still like it "
             "after a hundred repetitions? Is it ours: could it belong "
             "to any other product?",
             "Most sounds fail the second question. That is where the "
             "piano tuner in me helps the most.",
         ]},
    ],
}
