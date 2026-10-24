"""Saudade Station · Devlog of Inês Duarte: who they are and everything the document
could say. The typesetting keeps what fits into four pages, the most important
first."""

PERSONA = {
    "name": "Inês Duarte",
    "headline": "pixel artist and indie game developer · 16×16 tiles, "
                "big feelings",
    "contact": ["Porto, Portugal", "ines@duarte.example",
                "+351 912 555 044", "inesduarte.itch.io"],
}


DOCUMENT = {
    "title": "Saudade Station · Devlog",
    "subtitle": "Two years of making a game alone, in dated entries · "
                "selected from 104 weekly posts",
    "sections": [
        {"kind": "text", "weight": 0.2, "step": 4, "paragraphs": [
            "I wrote a devlog every Sunday for two years, mostly so that "
            "I would not quit. These are the entries I still think "
            "about, lightly edited. The game is about a night train from "
            "Porto to Lisbon, and about my grandfather, who worked on it "
            "for thirty years.",
        ]},
        {"heading": "Week 1 · a train in 16 pixels", "kind": "entries",
         "weight": 0.5, "step": 1, "inner": 0.7, "entries": [
             {"title": "March 2023", "text": [
                 "Drew a train carriage at 16 pixels high. It looked "
                 "like a loaf of bread. Drew it again at 24. Better. "
                 "Decided the whole game would be at this scale, which "
                 "turned out to be the most important decision of the "
                 "project."],
              "items": [
                  "Made: one carriage, one window, one sleeping "
                  "passenger.",
                  "Learned: scale is a design decision, not an art one.",
              ]},
         ]},
        {"heading": "Week 9 · the menu nobody could use", "kind": "entries",
         "weight": 1, "step": 1, "inner": 0.7, "entries": [
             {"title": "May 2023", "text": [
                 "Watched three friends play. All three got lost in the "
                 "settings menu. One gave up and played with the sound "
                 "at full volume for an hour rather than ask me. "
                 "Rebuilt the menu from scratch."],
              "items": [
                  "Made: menu v2, with fewer options and bigger targets.",
                  "Learned: watch people play; do not explain.",
              ]},
         ]},
        {"heading": "Week 31 · the station clock", "kind": "entries",
         "weight": 1.6, "step": 1, "inner": 0.7, "entries": [
             {"title": "October 2023", "text": [
                 "Turned the pause menu into a station clock. The hands "
                 "show real playtime; save files appear as departures on "
                 "the board. It took nine days. It is the thing every "
                 "review mentions."],
              "items": [
                  "Made: clock face, 12 animation frames, departure "
                  "board font.",
                  "Learned: UI can be the most memorable part of a game.",
              ]},
         ]},
        {"heading": "Week 52 · nearly quitting", "kind": "entries",
         "weight": 2.2, "step": 1, "inner": 0.7, "entries": [
             {"title": "March 2024", "text": [
                 "A year in, half done, working nights at the bakery and "
                 "evenings on the game. Stopped for a month. Did not "
                 "post. Slept. Came back because 300 people had written "
                 "to ask if I was fine."],
              "items": [
                  "Made: nothing, which was the point.",
                  "Learned: rest is part of the schedule.",
              ]},
         ]},
        {"heading": "Week 78 · a publisher", "kind": "entries",
         "weight": 2.8, "step": 1, "inner": 0.7, "entries": [
             {"title": "September 2024", "text": [
                 "Lumo Games offered to publish and port to Switch. "
                 "Learned what a lot-check is, and redrew every button "
                 "prompt for Nintendo's guidelines."],
              "items": [
                  "Made: 64 controller prompts in three styles.",
                  "Learned: platform rules are UI constraints too.",
              ]},
         ]},
        {"heading": "Week 104 · launch", "kind": "entries", "weight": 3.2,
         "step": 1, "inner": 0.7, "min_pages": 2, "entries": [
             {"title": "March 2025", "text": [
                 "Launched on a Thursday. Watched the first review come "
                 "in at 17:04: a man in Brazil whose grandfather also "
                 "worked on trains. Cried in the bakery's back room."],
              "items": [
                  "Made: a game.",
                  "Learned: small games can reach far.",
              ]},
         ]},
        {"heading": "Numbers", "kind": "tags", "weight": 3.6, "step": 0.3,
         "min_pages": 2, "items": [
             ("Sprites", "1,400"), ("Tilesets", "60"),
             ("Menu redesigns", "4"), ("Players", "40,000"),
             ("Devlog posts", "104"), ("Loaves baked meanwhile", "≈ 300,000"),
         ]},
        {"heading": "Week 60 · a font from a logbook", "kind": "entries",
         "weight": 3.8, "step": 1, "inner": 0.7, "min_pages": 4,
         "entries": [
             {"title": "May 2024", "text": [
                 "Found my grandfather's train logbooks in a drawer: "
                 "thirty years of departures in tidy capitals. Drew a "
                 "7-pixel font from his handwriting for the departure "
                 "board. Released it for free; thirty games use it now."],
              "items": [
                  "Learned: personal details make UI warm.",
              ]},
         ]},
        {"heading": "Week 88 · localisation pain", "kind": "entries",
         "weight": 4.0, "step": 1, "inner": 0.7, "min_pages": 4,
         "entries": [
             {"title": "November 2024", "text": [
                 "German text broke every button. Japanese needed a "
                 "second font at the same pixel height. Rebuilt the UI "
                 "with flexible containers and learned to design for the "
                 "longest language first."],
              "items": [
                  "Made: UI that stretches without losing its pixels.",
                  "Learned: design in German, not in English.",
              ]},
         ]},
        {"heading": "Week 70 · Switch handheld", "kind": "entries",
         "weight": 4.1, "step": 1, "inner": 0.7, "min_pages": 4,
         "entries": [
             {"title": "July 2024", "text": [
                 "Saw the game on a Switch in handheld mode for the first "
                 "time. Every icon was too small. Spent three weeks "
                 "redrawing the HUD at a larger scale for handheld only, "
                 "with an automatic switch when the console leaves the "
                 "dock."],
              "items": [
                  "Learned: test on the smallest screen first.",
              ]},
         ]},
        {"heading": "Week 95 · the trailer", "kind": "entries",
         "weight": 4.2, "step": 1, "inner": 0.7, "min_pages": 4,
         "entries": [
             {"title": "January 2025", "text": [
                 "Made the launch trailer myself in a week, from gameplay "
                 "captures and a song by a friend's band. It reached "
                 "200,000 views, most of them from a single repost by a "
                 "Japanese pixel artist I admire."],
              "items": [
                  "Learned: show the menus in the trailer; people loved "
                  "the clock.",
              ]},
         ]},
        {"heading": "Tools and pipeline", "kind": "tags", "weight": 4.3,
         "step": 0.3, "min_pages": 4, "items": [
             ("Drawing", "Aseprite, one palette of 32 colours"),
             ("Layout", "Figma for menus before pixels"),
             ("Engine", "Godot 4, custom UI theme"),
             ("Version control", "Git with LFS, after week 40"),
             ("Devlog", "itch.io and a mailing list"),
         ]},
        {"heading": "What I would tell week 1", "kind": "bullets",
         "weight": 4.4, "step": 0.5, "min_pages": 4, "items": [
             "Watch people play from the first week.",
             "Design menus early; they are not an afterthought.",
             "Use version control for art. Lost two weeks of tiles to a "
             "corrupted file.",
             "Take the month off before you need it.",
             "Write the devlog. It kept me going.",
         ]},
    ],
}
