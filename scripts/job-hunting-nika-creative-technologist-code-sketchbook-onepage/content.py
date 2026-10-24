"""Code Sketchbook of Nika Zupan: who they are and everything the document
could say. The typesetting keeps what fits into one page, the most important
first."""

PERSONA = {
    "name": "Nika Zupan",
    "headline": "creative coder · generative systems, light and the "
                "occasional runaway particle",
    "contact": ["Ljubljana", "nika@zupan.example", "+386 31 555 904",
                "nikazupan.art"],
}


DOCUMENT = {
    "title": "Code Sketchbook",
    "subtitle": "small programs that draw, listen and misbehave · seeds "
                "included",
    "sections": [
        {"kind": "text", "weight": 0.2, "step": 4, "paragraphs": [
            "Every installation I have built began as a sketch of fewer "
            "than two hundred lines, written at night, usually to answer "
            "a single question. This is a selection of them, each with "
            "its question, its seed, what it taught me and where it went "
            "next. Some crashed. Those taught the most.",
        ]},
        {"heading": "light that listens", "kind": "entries", "weight": 0.5,
         "step": 1, "inner": 0.8, "entries": [
             {"title": "2015", "org": "Processing, Arduino",
              "fields": [
                  ("question", "can a lamp feel like it is paying "
                               "attention?"),
                  ("seed", "a microphone, an envelope follower and a "
                           "brightness curve that lags half a second "
                           "behind the voice."),
                  ("learned", "the lag is the personality; without it "
                              "the lamp felt like a VU meter."),
                  ("went", "my thesis, and every installation since has "
                           "a little lag somewhere."),
              ]},
         ]},
        {"heading": "river as wave", "kind": "entries", "weight": 1,
         "step": 1, "inner": 0.8, "entries": [
             {"title": "2023", "org": "p5.js, open hydrology data",
              "fields": [
                  ("question", "what does a river look like if you only "
                               "know its numbers?"),
                  ("seed", "hourly level and flow of the Ljubljanica, "
                           "mapped to the amplitude and speed of a "
                           "single sine wave."),
                  ("learned", "real data is boring for days and dramatic "
                              "for hours; I compressed quiet days and "
                              "kept the floods in real time."),
                  ("went", "Tidal, a 40-metre projection on the "
                           "embankment."),
              ]},
         ]},
        {"heading": "breath sync", "kind": "entries", "weight": 1.6,
         "step": 1, "inner": 0.8, "entries": [
             {"title": "2022", "org": "TouchDesigner, ESP32",
              "fields": [
                  ("question", "can strangers breathe together without "
                               "being told to?"),
                  ("seed", "chest bands streaming over Wi-Fi; a gold "
                           "colour when two breath curves stay within "
                           "ten percent of each other."),
                  ("learned", "people find each other within a minute, "
                              "and then laugh, which breaks the sync."),
                  ("went", "Breathing Room, Prix Ars Electronica "
                           "honorary mention."),
              ]},
         ]},
        {"heading": "idle process", "kind": "entries", "weight": 2.2,
         "step": 1, "inner": 0.8, "entries": [
             {"title": "2022", "org": "Python, a Raspberry Pi",
              "fields": [
                  ("question", "what did my computer do in the year I "
                               "did not work?"),
                  ("seed", "one frame a day of a slow reaction-diffusion "
                           "pattern, seeded by the date."),
                  ("learned", "doing very little, every day, adds up to "
                              "something; this was also therapy."),
                  ("went", "a solo show at Kapelica Gallery."),
              ]},
         ]},
        {"heading": "scatter", "kind": "entries", "weight": 2.8,
         "step": 1, "inner": 0.8, "entries": [
             {"title": "2024", "org": "three.js, depth camera",
              "fields": [
                  ("question", "how do you make children walk slowly?"),
                  ("seed", "boids that flee from feet and return only "
                           "when the floor has been still for five "
                           "seconds."),
                  ("learned", "reward stillness, not motion; the room "
                              "went quiet."),
                  ("went", "the aquarium floor in Piran."),
              ]},
         ]},
        {"heading": "pendulum wave", "kind": "entries", "weight": 3.0,
         "step": 1, "inner": 0.8, "min_pages": 2, "entries": [
             {"title": "2020", "org": "GLSL",
              "fields": [
                  ("question", "can a shader teach a physics lesson?"),
                  ("seed", "fifteen pendulums with lengths chosen so "
                           "that they realign every sixty seconds."),
                  ("learned", "patterns that return are deeply "
                              "satisfying; visitors waited for the "
                              "minute to end."),
                  ("went", "a loop for a school's science week, and an "
                           "idea for the museum."),
              ]},
         ]},
        {"heading": "slime router", "kind": "entries", "weight": 3.2,
         "step": 1, "inner": 0.8, "min_pages": 4, "entries": [
             {"title": "2021", "org": "Python, Physarum simulation",
              "fields": [
                  ("question", "would a slime mould design a better tram "
                               "network for Ljubljana?"),
                  ("seed", "food sources at the city's busiest stops and "
                           "an agent-based Physarum model."),
                  ("learned", "it rediscovered two existing lines and "
                              "proposed one the city once rejected; "
                              "planners were delighted."),
                  ("went", "a print series and a talk at Open Data "
                           "Day."),
              ]},
         ]},
        {"heading": "shadow choir", "kind": "entries", "weight": 3.3,
         "step": 1, "inner": 0.8, "min_pages": 4, "entries": [
             {"title": "2025", "org": "TouchDesigner, LiDAR",
              "fields": [
                  ("question", "can a crowd sing with its shadows?"),
                  ("seed", "eight beams of light across a hall; every "
                           "shadow that crosses a beam sings one note "
                           "of a chord."),
                  ("learned", "people form choirs with strangers within "
                              "minutes if the reward is immediate."),
                  ("went", "a prototype for the museum's light "
                           "exhibition, if you will have it."),
              ]},
         ]},
        {"heading": "crashes worth keeping", "kind": "bullets",
         "weight": 3.4, "step": 0.5, "items": [
             "**memory leak, 2019** · a particle system that never "
             "freed its dead; the facade show slowed to a crawl at 23:40 "
             "on opening night. Now every sketch has a particle budget.",
             "**infinite feedback, 2018** · a camera pointed at its own "
             "projection; beautiful for nine seconds, then white. Kept "
             "the nine seconds as a piece.",
             "**sunlight, 2021** · a projection that worked at dusk and "
             "vanished at 6 pm in June. I now check sunset times before "
             "anything else.",
             "**cleaner, 2025** · not a bug, a person, unplugging the "
             "aquarium floor to charge a phone. Added a sign and a "
             "socket.",
         ]},
        {"heading": "rules I sketch by", "kind": "bullets", "weight": 4,
         "step": 0.5, "min_pages": 2, "items": [
             "one question per sketch.",
             "under two hundred lines, or it is not a sketch.",
             "a seed you can write on a napkin.",
             "keep the version that crashed.",
             "show it to a child before showing it to a curator.",
         ]},
        {"heading": "sketches for a museum", "kind": "entries",
         "weight": 4.4, "step": 0.8, "inner": 0.5, "min_pages": 4,
         "entries": [
             {"title": "beam path", "text": [
                 "A camera traces a beam of light through lenses and "
                 "water as a glowing line that stays on the wall for a "
                 "minute. Refraction without wall text."]},
             {"title": "colour lies", "text": [
                 "A white wall lit by three LEDs; visitors move sliders "
                 "and discover that “white” is a negotiation between "
                 "red, green and blue, and between their eyes and the "
                 "room."]},
             {"title": "slow camera", "text": [
                 "A mirror that shows you as you were five seconds ago. "
                 "An exhibit about the speed of light, at a speed people "
                 "can feel."]},
             {"title": "shadow orchestra", "text": [
                 "Shadows of visitors play notes where they cross beams; "
                 "a lesson about light paths that children will not "
                 "realise is a lesson."]},
         ]},
        {"heading": "seeds", "kind": "tags", "weight": 4.8, "step": 0.2,
         "min_pages": 4, "items": [
             ("light that listens", "lag = 0.5 s"),
             ("river as wave", "amplitude = level / 40 cm"),
             ("breath sync", "gold if |a − b| < 10 %"),
             ("idle process", "seed = yyyymmdd"),
             ("scatter", "return after 5 s of stillness"),
             ("pendulum wave", "realign every 60 s"),
         ]},
        {"heading": "tools", "kind": "tags", "weight": 5, "step": 0.3,
         "min_pages": 2, "items": [
             ("sketching", "p5.js, Processing, TouchDesigner"),
             ("shipping", "three.js, Unreal, openFrameworks, C++"),
             ("sensing", "depth cameras, LiDAR, chest bands, river "
                         "gauges"),
         ]},
    ],
}
