"""Curriculum Vitae of Inês Duarte: who they are and everything the document
could say. The typesetting keeps what fits into one page, the most important
first."""

PERSONA = {
    "name": "Inês Duarte",
    "headline": "pixel artist and indie game developer · 16×16 tiles, "
                "big feelings",
    "contact": ["Porto, Portugal", "ines@duarte.example",
                "+351 912 555 044", "inesduarte.itch.io"],
}


DOCUMENT = {
    "title": "Curriculum Vitae",
    "cv": True,
    "sections": [
        {"heading": "Player One", "kind": "text", "weight": 0.4, "step": 5,
         "paragraphs": [
             "Self-taught pixel artist who shipped a whole game alone: "
             "art, animation, UI and most of the code of “Saudade "
             "Station”, a small game about a night train through "
             "Portugal that 40,000 people have played. I love interface "
             "art most, the buttons, menus and tiny icons that players "
             "touch a thousand times and never think about.",
             "No degree, two years baking bread at four in the morning, "
             "and a portfolio that grew in the gaps. Looking for my "
             "first studio job as a UI artist.",
         ]},
        {"heading": "Experience", "kind": "entries", "weight": 1,
         "step": 1.2, "entries": [
             {"title": "Solo developer", "org": "Saudade Station",
              "dates": "2023 – 2025", "meta": "PC and Switch · Godot",
              "items": [
                  "Designed, drew and animated 1,400 sprites, 60 tilesets "
                  "and every menu, icon and font.",
                  "Shipped on Steam and Nintendo Switch with a small "
                  "publisher; 40,000 players and “Very Positive” "
                  "reviews.",
                  "Built the UI system in Godot: menus that work with "
                  "mouse, controller and touch.",
                  "Wrote a devlog every week for two years; 3,000 "
                  "followers.",
              ],
              "story": [
                  "Saudade Station began as a gift for my grandfather, "
                  "who worked on the night train from Porto to Lisbon "
                  "for thirty years. It became two years of evenings, "
                  "one breakdown and a game that made strangers write "
                  "to me about their own grandparents. I did "
                  "everything badly at first and most things better by "
                  "the end.",
              ]},
             {"title": "Freelance pixel artist", "dates": "2022 – now",
              "meta": "remote",
              "story": [
                  "Freelancing taught me to draw to a brief: a palette I "
                  "did not choose, a style guide written by someone else "
                  "and a deadline set by a studio on the other side of "
                  "the world. The best compliment I have received was a "
                  "lead artist saying they could not tell which icons "
                  "were mine and which were theirs.",
              ],
              "items": [
                  "Icons, UI kits and character sprites for eleven indie "
                  "games, from a farming game to a horror roguelike.",
                  "A 120-icon inventory set for a Brazilian studio's "
                  "survival game, delivered in three sizes.",
              ]},
             {"title": "Bonus stage: baker", "org": "Padaria Flor",
              "dates": "2020 – 2022", "meta": "Porto · 4 am shifts",
              "story": [
                  "Two years of night shifts at a bakery look like a gap "
                  "on paper. They were my art school: I drew on the bus "
                  "home at seven in the morning, every day, and posted "
                  "one piece of pixel art online for 700 days in a row. "
                  "The bakery owner hung my price boards in the window "
                  "and told every customer who drew them.",
              ],
              "items": [
                  "Baked 600 loaves a night, which taught me patience, "
                  "repetition and the joy of a thing done properly every "
                  "day.",
                  "Redesigned the bakery's price boards in pixel art; "
                  "customers took photos of them.",
              ]},
             {"title": "Gap: dropped out", "dates": "2019 – 2020",
              "meta": "BA Communication Design, ESAD Matosinhos, first "
                      "year",
              "items": [
                  "Left after a year; I was not ready and could not "
                  "afford it. Kept drawing every day.",
              ]},
         ]},
        {"heading": "Skills", "kind": "tags", "weight": 1.6, "step": 0.5,
         "items": [
             ("Art", "pixel art, animation, UI and HUD design, icon "
                     "design, bitmap fonts, palettes"),
             ("Tools", "Aseprite, Figma, Godot, a little Unity, Photoshop"),
             ("Code", "GDScript, enough C# to annoy a programmer"),
             ("UX", "controller and touch navigation, readable UI at 4K "
                    "and on a Switch in handheld mode"),
         ]},
        {"heading": "Games", "kind": "bullets", "weight": 2.2, "step": 0.4,
         "items": [
             "**Saudade Station** (2025) — solo developer; Steam and "
             "Switch.",
             "**Pão Quente** (2022) — a 48-hour jam game about baking at "
             "night; 2nd place, Lisbon Game Jam.",
             "**Rooftop Cats** (2021) — art and UI, with two friends; "
             "free on itch.io.",
             "Eleven freelance games, art and UI, 2022 – 2026.",
         ]},
        {"heading": "Education", "kind": "entries", "weight": 2.8,
         "step": 1, "entries": [
             {"title": "Self-taught", "dates": "2019 – now",
              "meta": "daily practice, 2,000+ pixel pieces, one game",
              "items": []},
             {"title": "Game UI design course", "org": "online, 40 hours",
              "dates": "2024", "items": []},
             {"title": "BA Communication Design, first year",
              "org": "ESAD Matosinhos", "dates": "2018 – 2019",
              "items": []},
         ]},
        {"heading": "Awards", "kind": "bullets", "weight": 3.4,
         "step": 0.4, "items": [
             "Best Visual Art, Indie X festival, Lisbon, 2025.",
             "Official selection, Day of the Devs, 2025.",
             "2nd place, Lisbon Game Jam, 2022.",
         ]},
        {"heading": "Languages", "kind": "tags", "weight": 4, "step": 0.3,
         "items": [("Portuguese", "native"), ("English", "fluent"),
                   ("Spanish", "good"), ("Japanese", "katakana only")]},
        {"heading": "Community", "kind": "bullets", "weight": 4.6,
         "step": 0.4, "items": [
             "Co-organiser of Pixel Porto, a monthly drawing night, 40 "
             "regulars.",
             "Free pixel art workshops for teenagers at the city library, "
             "2024 – 2025.",
         ]},
        {"heading": "Secret Levels", "kind": "entries", "weight": 5.2,
         "step": 0.6, "inner": 0.4, "min_pages": 4, "entries": [
             {"title": "The station clock", "org": "Saudade Station",
              "text": [
                  "A pause menu that is a station clock: the hands show "
                  "real playtime, and the departure board lists the "
                  "player's own saves as trains."]},
             {"title": "A font for my grandfather", "org": "personal",
              "text": [
                  "A 7-pixel bitmap font based on the handwriting in my "
                  "grandfather's train logbooks; now free on itch.io and "
                  "used in 30 games."]},
             {"title": "Bakery price boards", "org": "Padaria Flor",
              "text": [
                  "Prices drawn in pixel art on chalkboards; the bakery "
                  "kept them after I left."]},
             {"title": "Inventory set", "org": "freelance",
              "text": [
                  "120 survival-game icons readable at 16, 32 and 64 "
                  "pixels, which is three different drawings, not one "
                  "drawing three times."]},
         ]},
        {"heading": "Talks and Streams", "kind": "bullets", "weight": 5.6,
         "step": 0.3, "min_pages": 4, "items": [
             "“Menus are level design”, Indie X festival talk, 2025.",
             "Weekly pixel art streams on Twitch, 2023 – 2025, 600 "
             "followers.",
             "“Drawing at 16 pixels”, workshop for teenagers, Porto "
             "Municipal Library, 2024.",
         ]},
        {"heading": "Daily Practice", "kind": "bullets", "weight": 5.8,
         "step": 0.3, "min_pages": 4, "items": [
             "700 consecutive days of posting one pixel piece, 2020 – "
             "2022.",
             "A tiny icon every morning before work since 2023.",
             "One study of a favourite game UI every month.",
         ]},
        {"heading": "Interests", "kind": "text", "weight": 6.5,
         "paragraphs": [
             "Night trains, sourdough, old Game Boy games, azulejo tiles "
             "(the original pixel art) and drawing strangers' dogs.",
         ]},
        {"heading": "References", "kind": "entries", "weight": 7,
         "min_pages": 4, "entries": [
             {"title": "Rui Matos", "org": "Publisher, Lumo Games",
              "meta": "on request", "items": []},
             {"title": "Dona Flor", "org": "Padaria Flor",
              "meta": "will tell you I was never late", "items": []},
         ]},
    ],
}
