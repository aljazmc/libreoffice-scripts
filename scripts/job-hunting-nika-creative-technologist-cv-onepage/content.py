"""Curriculum Vitae of Nika Zupan: who they are and everything the document
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
    "title": "Curriculum Vitae",
    "cv": True,
    "sections": [
        {"heading": "README", "kind": "text", "weight": 0.4, "step": 5,
         "paragraphs": [
             "Creative coder with nine years of making software that "
             "people walk through, touch and shout at: light "
             "installations, interactive projections and generative "
             "visuals for festivals, theatres and one very patient "
             "aquarium. I write the code, solder the sensors and stay "
             "until the last visitor leaves.",
             "My path has gaps, and I log them like everything else: two "
             "art residencies, a year of recovery from burnout and a "
             "season of building boats. I am now looking for a creative "
             "technologist role in a science museum, where installations "
             "have to explain something true and survive ten thousand "
             "children a week.",
         ]},
        {"heading": "Experience", "kind": "entries", "weight": 1,
         "step": 1.2, "entries": [
             {"title": "Freelance creative coder", "dates": "2023 – now",
              "meta": "installations, projections, workshops",
              "items": [
                  "**Tidal**, a 40-metre projection on the Ljubljanica "
                  "embankment driven by live river level data; 120,000 "
                  "visitors at Festival of Lights 2024.",
                  "**Breathing Room**, a room of 300 LEDs that follows "
                  "the breathing of visitors through a chest sensor; "
                  "toured to Graz, Zagreb and Linz.",
                  "Interactive floor for the children's wing of an "
                  "aquarium in Piran; runs eleven hours a day without "
                  "crashing, which is the real achievement.",
                  "Workshops in TouchDesigner and p5.js for 400 students "
                  "and teachers.",
              ],
              "story": [
                  "Freelance life taught me to write software that "
                  "nobody will restart. Every installation now ships "
                  "with a watchdog, a remote log and a one-page manual "
                  "for the person who unlocks the room in the morning. "
                  "The aquarium floor has been running for 700 days; its "
                  "only outage was a cleaner unplugging it to charge a "
                  "phone.",
              ]},
             {"title": "Gap: recovery", "dates": "2022",
              "meta": "process idle, by choice",
              "items": [
                  "A year off after burnout. Learned to say no, to "
                  "estimate honestly and to build boats with my uncle in "
                  "Izola.",
                  "Came back with fewer projects, better contracts and "
                  "a sleep schedule.",
              ]},
             {"title": "Creative technologist", "org": "Studio Lumina",
              "dates": "2019 – 2021", "meta": "Ljubljana · "
                                              "projection mapping studio",
              "items": [
                  "Lead developer on 14 projection shows for brands, "
                  "museums and the opening of a concert hall.",
                  "Built the studio's real-time pipeline in "
                  "TouchDesigner and Unreal, replacing pre-rendered "
                  "video.",
                  "Shipped the National Gallery's 150th anniversary "
                  "facade show to 60,000 people in three nights.",
                  "Worked 70-hour weeks for two years, which is how the "
                  "next entry happened.",
              ],
              "story": [
                  "Lumina was where I learned the craft at full speed: a "
                  "facade show for 60,000 people, rehearsed at three in "
                  "the morning in the rain, with a client on the phone "
                  "and a projector overheating on a roof. It was also "
                  "where I learned that speed without rest has a price, "
                  "and that I was the one paying it.",
              ]},
             {"title": "Gap: residencies", "dates": "2017 – 2018",
              "meta": "Rijeka and Linz",
              "items": [
                  "Six months at a media art residency in Rijeka and "
                  "three at Ars Electronica's Futurelab in Linz.",
                  "Built my first sensor installations and learned that "
                  "galleries are hostile to cables.",
              ],
              "story": [
                  "Rijeka gave me a studio in a former paper factory and "
                  "no deadlines; Linz gave me engineers who asked why my "
                  "sensor readings drifted. Between the two I learned to "
                  "make things that are both strange and reliable.",
              ]},
             {"title": "Junior web developer", "org": "Agencija Kocka",
              "dates": "2016 – 2017", "meta": "Ljubljana",
              "items": [
                  "Websites and banner animations for local brands; "
                  "learned JavaScript properly by breaking it.",
              ]},
         ]},
        {"heading": "Stack", "kind": "tags", "weight": 1.6, "step": 0.5,
         "items": [
             ("creative", "TouchDesigner, p5.js, three.js, GLSL, Unreal "
                          "Engine, openFrameworks"),
             ("code", "JavaScript, TypeScript, Python, C++, a little "
                      "Rust"),
             ("hardware", "Arduino, ESP32, DMX, LED pixel mapping, depth "
                          "cameras, LiDAR"),
             ("ops", "watchdogs, remote logging, Raspberry Pi kiosks, "
                     "the fine art of the hidden power switch"),
         ]},
        {"heading": "Education", "kind": "entries", "weight": 2.2,
         "step": 1, "entries": [
             {"title": "BA New Media", "org": "Academy of Fine Arts and "
              "Design, Ljubljana", "dates": "2012 – 2016",
              "meta": "thesis: “Light that listens”, a reactive lamp",
              "items": []},
             {"title": "Exchange semester, Interface Cultures",
              "org": "Kunstuniversität Linz", "dates": "2015",
              "items": []},
         ]},
        {"heading": "Exhibitions", "kind": "bullets", "weight": 2.8,
         "step": 0.4, "items": [
             "Festival of Lights Ljubljana, 2019, 2021, 2024.",
             "Ars Electronica Festival, Linz, 2018 and 2025.",
             "Zagreb Light Festival, 2023.",
             "Kapelica Gallery, solo show “Idle Process”, 2023, about "
             "the year I did not work.",
         ]},
        {"heading": "Awards", "kind": "bullets", "weight": 3.2,
         "step": 0.4, "items": [
             "Prix Ars Electronica, honorary mention, Interactive Art+, "
             "2025, for Breathing Room.",
             "Best young artist, Slovenian Art Prize for New Media, 2019.",
         ]},
        {"heading": "Teaching", "kind": "bullets", "weight": 3.8,
         "step": 0.4, "items": [
             "Guest lecturer, creative coding, Academy of Fine Arts and "
             "Design, 2024 – now.",
             "TouchDesigner summer school for teenagers, Kino Šiška, 2023 "
             "– 2025.",
             "Creative coding for science teachers, National Education "
             "Institute, 2025.",
         ]},
        {"heading": "Languages", "kind": "tags", "weight": 4.2, "step": 0.3,
         "items": [("slovenian", "native"), ("english", "fluent"),
                   ("german", "good"), ("croatian", "good"),
                   ("glsl", "conversational")]},
        {"heading": "Selected Installations", "kind": "entries",
         "weight": 5.2, "step": 0.6, "inner": 0.4, "min_pages": 4,
         "entries": [
             {"title": "Tidal", "dates": "2024", "text": [
                 "River level, flow and temperature from the national "
                 "hydrology service turned into slow waves of light on "
                 "the embankment. When it rained in the Alps, the "
                 "projection rose a day before the river did."]},
             {"title": "Breathing Room", "dates": "2023", "text": [
                 "Visitors wear a soft chest band; 300 LEDs breathe with "
                 "them, and when several people synchronise, the room "
                 "turns gold. Most people try to hold their breath "
                 "together. Most fail, laughing."]},
             {"title": "Aquarium floor", "dates": "2024", "text": [
                 "A projected tide pool that scatters when children step "
                 "in. Fish return when the floor is quiet, which turned "
                 "out to be the best way to calm a school class."]},
             {"title": "Idle Process", "dates": "2023", "text": [
                 "A solo show about my year off: a computer that renders "
                 "one frame a day, and a wall of the frames it rendered "
                 "while I was not working."]},
         ]},
        {"heading": "Talks", "kind": "bullets", "weight": 5.8, "step": 0.3,
         "min_pages": 4, "items": [
             "“Software nobody restarts”, Creative Coding Ljubljana, 2025.",
             "“Idle process: a year without work”, Kapelica Gallery "
             "artist talk, 2023.",
             "“Light that listens”, Ars Electronica Futurelab, 2018.",
             "“Rivers as data, data as light”, Open Data Day, 2024.",
         ]},
        {"heading": "Interests", "kind": "text", "weight": 6.5,
         "paragraphs": [
             "wooden boats, night swimming, slime moulds as computers, "
             "modular synthesizers and fixing other people's broken "
             "lamps.",
         ]},
        {"heading": "References", "kind": "entries", "weight": 7,
         "min_pages": 4, "entries": [
             {"title": "Tanja Rihtar", "org": "Festival of Lights",
              "meta": "artistic director · on request", "items": []},
             {"title": "Dr. Martin Koller", "org": "Ars Electronica "
              "Futurelab", "meta": "on request", "items": []},
         ]},
    ],
}
