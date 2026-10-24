"""Cover Letter of Inês Duarte: who they are and everything the document
could say. The typesetting keeps what fits into two pages, the most important
first."""

PERSONA = {
    "name": "Inês Duarte",
    "headline": "pixel artist and indie game developer · 16×16 tiles, "
                "big feelings",
    "contact": ["Porto, Portugal", "ines@duarte.example",
                "+351 912 555 044", "inesduarte.itch.io"],
}


DOCUMENT = {
    "title": "Cover Letter",
    "date": "Porto, 24 October 2026",
    "recipient": ["Joana Pires", "Art Director", "Moonfish Games",
                  "Rua da Boavista 12", "1200-066 Lisboa"],
    "subject": "UI Artist (junior)",
    "salutation": "Olá Joana,",
    "signoff": "Até breve,",
    "sections": [
        {"kind": "text", "weight": 0, "step": 0.4, "paragraphs": [
            "The first thing I noticed in “Tidepool Tales” was not the "
            "fish but the inventory: a little net that fills up as you "
            "collect shells, with a wobble when it is almost full. I "
            "replayed the first hour just to watch it. I am applying "
            "for the junior UI Artist role at Moonfish because I want "
            "to make the small things players touch a thousand times.",
        ]},
        {"heading": "What I have made", "kind": "text", "weight": 1,
         "step": 3, "paragraphs": [
             "I made “Saudade Station” alone over two years: 1,400 "
             "sprites, 60 tilesets and every menu, icon and font. It is a "
             "small game about a night train through Portugal, played by "
             "40,000 people on Steam and Switch, and it won Best Visual "
             "Art at Indie X last year. The part I am proudest of is the "
             "pause menu, a station clock whose departure board shows "
             "your save files as trains.",
             "I have also drawn UI kits, icons and sprites as a freelancer "
             "for eleven indie games, including 120 inventory icons for "
             "a survival game, each redrawn by hand for three sizes.",
         ]},
        {"heading": "Why UI", "kind": "text", "weight": 1.4, "step": 3,
         "paragraphs": [
             "Characters and landscapes get the attention, but players "
             "spend hours in menus. A good interface is clear in a "
             "second, works with a controller, a mouse and a finger, and "
             "still feels like it belongs to its world. That combination "
             "of craft and usefulness is what I love most.",
             "I learned it the hard way. Saudade Station's first menus "
             "were beautiful and nobody could find the settings. I "
             "rebuilt them three times after watching friends play, and "
             "I have tested every interface I have made since with "
             "someone who has never seen it.",
         ]},
        {"heading": "About my path", "kind": "text", "weight": 1.8,
         "step": 3, "paragraphs": [
             "I do not have a degree. I left design school after a year "
             "because I could not afford it and was not ready, and then "
             "I baked bread at four in the morning for two years. I "
             "drew every afternoon, and the bakery's price boards became "
             "my first public pixel art.",
             "I think the bakery made me a better artist. Six hundred "
             "loaves a night teaches patience, repetition and pride in "
             "doing small things properly, which is most of UI work.",
         ]},
        {"heading": "Why Moonfish", "kind": "text", "weight": 2.4,
         "step": 3, "min_pages": 2, "paragraphs": [
             "Your games are cosy without being sugary, and your "
             "interfaces are part of the world rather than on top of it. "
             "I would like to learn from a team that cares about that, "
             "and from an art director whose talk at Indie X about "
             "readable pixel art I watched three times.",
             "I am also excited that you are a small studio. I want to "
             "sit next to programmers and designers, see how my icons "
             "end up in the build and fix them the same afternoon.",
         ]},
        {"heading": "A small redesign", "kind": "text", "weight": 3,
         "step": 3, "min_pages": 4, "paragraphs": [
             "To show how I think, I redrew one screen from Tidepool "
             "Tales: the crafting menu. I kept your palette and style, "
             "but grouped recipes by the shell they need rather than "
             "alphabetically, added a tiny preview of the crafted item "
             "and made the controller cursor snap in a way that feels "
             "like a fish darting. I tested it with three friends; they "
             "crafted their first item about twice as fast.",
             "I know I am missing your design reasons and your data, and "
             "I would love to hear where I am wrong.",
         ]},
        {"heading": "What I still need to learn", "kind": "text",
         "weight": 3.4, "step": 3, "min_pages": 4, "paragraphs": [
             "I have never worked in a team larger than three people, "
             "with version control for art, task boards and feedback "
             "from someone who is not my friend. I would like to learn "
             "studio habits properly, and I take feedback well; two "
             "years of strangers reviewing my game on Steam made sure "
             "of that.",
             "I would also like to learn localisation: how menus survive "
             "German words and Japanese characters without losing their "
             "charm.",
         ]},
        {"heading": "How I work", "kind": "text", "weight": 3.5,
         "step": 3, "min_pages": 4, "paragraphs": [
             "I start every interface on paper, at real size, with a "
             "thumb next to it. Then I block it out in Figma, test it in "
             "the engine as soon as possible and only then draw the "
             "final pixels. Drawing beautiful buttons before you know "
             "where they go is the most expensive mistake in UI art, and "
             "I have made it.",
             "I keep palettes and sizes in a small style guide from the "
             "first day, so that the hundredth icon matches the first. "
             "On Saudade Station the guide was two pages; it saved me "
             "weeks.",
         ]},
        {"heading": "Accessibility", "kind": "text", "weight": 3.6,
         "step": 3, "min_pages": 4, "paragraphs": [
             "Pixel art can be hard to read for players with low vision "
             "or colour blindness. Saudade Station has a large-UI mode, "
             "a high-contrast palette and icons that never rely on colour "
             "alone. A player with colour blindness wrote to say it was "
             "the first pixel game whose inventory he could read, and I "
             "keep that email next to my monitor.",
         ]},
        {"heading": "What I would bring besides pixels", "kind": "text",
         "weight": 3.7, "step": 3, "min_pages": 4, "paragraphs": [
             "Having made a whole game alone, I know what programmers "
             "need from an artist: sprite sheets named consistently, "
             "nine-slice borders that stretch properly and animations "
             "that loop without a hiccup. I can also open the engine, "
             "check my own work in context and fix small things without "
             "waiting for someone else.",
             "And I can write a little. My devlog taught me to explain "
             "decisions in plain words, which I hope will help in "
             "reviews.",
         ]},
        {"heading": "Questions for you", "kind": "bullets", "weight": 3.8,
         "step": 1, "min_pages": 4, "items": [
             "How do UI art and UI programming work together at Moonfish?",
             "How do you test menus with players before release?",
             "What would a junior UI artist own in their first six "
             "months?",
         ]},
        {"heading": "Practical things", "kind": "text", "weight": 4.2,
         "step": 3, "min_pages": 2, "paragraphs": [
             "I can move to Lisbon in January, or work remotely from "
             "Porto and come to the studio every week. I would bring my "
             "own Aseprite licence and, if allowed, bread on Mondays.",
         ]},
        {"kind": "text", "weight": 0.2, "step": 6, "paragraphs": [
            "Thank you for reading. My portfolio and the Tidepool "
            "redesign are at inesduarte.itch.io, and I would love to "
            "show you the station clock in motion.",
        ]},
    ],
}
