"""Curriculum Vitae of Kai Berg: who they are and everything the document
could say. The typesetting keeps what fits into one page, the most important
first."""

PERSONA = {
    "name": "Kai Berg",
    "headline": "3D environment artist · ten thousand square metres of "
                "places that never existed",
    "contact": ["Malmö, Sweden", "kai.berg@example.se", "+46 73 555 6620",
                "artstation.com/kaiberg"],
}


DOCUMENT = {
    "title": "Curriculum Vitae",
    "cv": True,
    "sections": [
        {"heading": "Profile", "kind": "text", "weight": 0.4, "step": 5,
         "paragraphs": [
             "Environment artist with eight years in games, from mobile "
             "puzzle worlds to a 40-hour open-world RPG. I build spaces "
             "that guide people without signs: light that pulls you to a "
             "door, materials that tell you how old a room is, "
             "silhouettes you can find again from a hilltop.",
             "Two studio closures and an eight-month gap later, I am "
             "moving into architectural visualisation, where the rooms "
             "are real, the light must be honest and people will one day "
             "live inside the images.",
         ]},
        {"heading": "Experience", "kind": "entries", "weight": 1,
         "step": 1.2, "entries": [
             {"title": "Freelance visualisation artist", "dates": "2025 – "
              "now", "meta": "Malmö · housing, interiors, competitions",
              "items": [
                  "Interiors and exteriors for six architecture offices "
                  "in Malmö and Copenhagen, in Unreal Engine 5 and "
                  "Blender.",
                  "Real-time walkthrough of a 120-apartment housing "
                  "project, used in public consultation by 800 future "
                  "neighbours.",
                  "Daylight studies for a school competition entry that "
                  "won second prize.",
              ],
              "story": [
                  "The first architect who hired me said my renders "
                  "looked “too much like a game”. She was right: I was "
                  "lighting for drama, not for truth. I spent a month "
                  "learning physically correct exposure, measured "
                  "materials and the boring beauty of an overcast "
                  "Scandinavian afternoon. Her next competition entry "
                  "used my images.",
              ]},
             {"title": "Gap: laid off", "dates": "Apr – Dec 2024",
              "meta": "studio-wide layoffs, 140 people",
              "items": [
                  "Eight months between jobs. Finished an "
                  "architectural visualisation course, rebuilt my "
                  "portfolio around real buildings and learned "
                  "Twinmotion and V-Ray.",
                  "Modelled my grandmother's 1950s kitchen from photos "
                  "as practice; it is now the most-viewed piece on my "
                  "ArtStation.",
              ]},
             {"title": "Senior environment artist", "org": "Nordljus "
              "Games", "dates": "2020 – 2024", "meta": "Malmö · open-world "
                                                       "RPG, 200 people",
              "items": [
                  "Owned the art of three regions of “Hollow Crown”, "
                  "about 4 km² of terrain, villages and ruins.",
                  "Built a modular kit of 300 assets for Nordic timber "
                  "buildings, reused across the whole game.",
                  "Led lighting for interiors; cut lighting build times "
                  "by half with a new light-baking workflow.",
                  "Mentored four junior artists and ran the weekly "
                  "environment art review.",
              ],
              "story": [
                  "Hollow Crown shipped to good reviews and decent "
                  "sales, and three months later the publisher closed "
                  "the studio's next project. I was one of 140 people "
                  "let go on a Tuesday morning call. I mention it not to "
                  "complain but because it is normal in games, and "
                  "because it made me think hard about the work I want "
                  "to do for the next twenty years.",
              ]},
             {"title": "Gap: studio closure", "dates": "Jan – Jun 2020",
              "meta": "studio closed during the pandemic",
              "items": [
                  "Five months between jobs; taught Blender online to "
                  "teenagers and built a small diorama series.",
              ]},
             {"title": "Environment artist", "org": "Puzzlebox Studio",
              "dates": "2016 – 2019", "meta": "Stockholm · mobile games",
              "story": [
                  "Puzzlebox taught me simplification: a harbour, a "
                  "garden or a castle had to be readable on a phone in "
                  "two seconds. It is the best training I know for "
                  "architectural images that a busy client glances at "
                  "for exactly that long.",
              ],
              "items": [
                  "Built 220 levels of cosy puzzle worlds for a game "
                  "with 12 million downloads.",
                  "Learned to make spaces readable at the size of a "
                  "phone screen.",
              ]},
         ]},
        {"heading": "Tools", "kind": "tags", "weight": 1.6, "step": 0.5,
         "items": [
             ("Real-time", "Unreal Engine 5, Lumen, Nanite, Twinmotion"),
             ("Modelling", "Blender, 3ds Max, ZBrush, SpeedTree"),
             ("Materials", "Substance Designer and Painter, photogrammetry "
                           "with RealityCapture"),
             ("Rendering", "V-Ray, Cycles, path tracing in Unreal"),
             ("Architecture", "reading plans and sections, Revit and "
                              "Rhino imports, daylight studies"),
         ]},
        {"heading": "Education", "kind": "entries", "weight": 2.2,
         "step": 1, "entries": [
             {"title": "BA Game Design and Graphics", "org": "Uppsala "
              "University, Campus Gotland", "dates": "2013 – 2016",
              "items": []},
             {"title": "Architectural Visualisation in Unreal",
              "org": "online course, 120 hours", "dates": "2024",
              "items": []},
         ]},
        {"heading": "Shipped Titles", "kind": "bullets", "weight": 2.8,
         "step": 0.4, "items": [
             "**Hollow Crown** (PC, PS5, Xbox), 2023 — environment art "
             "and interior lighting.",
             "**Puzzlebox Gardens** (iOS, Android), 2018 — 220 levels.",
             "**Puzzlebox Harbour** (iOS, Android), 2017 — 140 levels.",
         ]},
        {"heading": "Languages", "kind": "tags", "weight": 3.6, "step": 0.3,
         "items": [("Swedish", "native"), ("English", "fluent"),
                   ("Danish", "understanding well, speaking slowly")]},
        {"heading": "Recognition", "kind": "bullets", "weight": 4.2,
         "step": 0.4, "items": [
             "ArtStation front page, “Farmor's kitchen”, 2024.",
             "Hollow Crown: BAFTA Games Awards nomination, Artistic "
             "Achievement, 2024.",
             "Second prize, school competition with Arkitema-style "
             "daylight studies, 2025 (as visualiser).",
         ]},
        {"heading": "Selected Spaces", "kind": "entries", "weight": 5,
         "step": 0.6, "inner": 0.4, "min_pages": 4, "entries": [
             {"title": "The Ashen Ridge", "org": "Hollow Crown",
              "text": [
                  "A burnt village where every house tells you how long "
                  "ago the fire was. Players found the hidden well "
                  "without a single marker, because I lit it."]},
             {"title": "Farmor's kitchen", "org": "personal",
              "text": [
                  "My grandmother's 1950s kitchen in Lund, rebuilt from "
                  "family photos: linoleum, a Husqvarna stove and the "
                  "exact yellow of the morning light."]},
             {"title": "Kvarteret Plommon", "org": "freelance",
              "text": [
                  "A real-time model of 120 apartments for public "
                  "consultation; neighbours could stand on their future "
                  "balcony and see whether it blocked their view."]},
             {"title": "Harbour level 88", "org": "Puzzlebox",
              "text": [
                  "A whole harbour on a phone screen, readable in two "
                  "seconds. Still my best lesson in simplification."]},
         ]},
        {"heading": "Teaching", "kind": "bullets", "weight": 5.6,
         "step": 0.3, "min_pages": 4, "items": [
             "Blender for teenagers, online, 2020 — 60 students.",
             "Guest lecture, “Light as level design”, Malmö University, "
             "2023.",
             "Weekly environment art review at Nordljus, 2021 – 2024.",
         ]},
        {"heading": "Personal Projects", "kind": "bullets", "weight": 5.7,
         "step": 0.3, "min_pages": 4, "items": [
             "**Farmor's kitchen**, 2024 — a 1950s kitchen rebuilt from "
             "twelve family photographs.",
             "**Malmö brutalism**, 2025 — real-time studies of three "
             "concrete buildings threatened with demolition, shown at a "
             "local heritage evening.",
             "**Dioramas**, 2020 — twelve tiny rooms made during the "
             "first gap, one a week.",
             "**Light diary**, ongoing — a photo of the same window every "
             "day at 4 pm, now in its third year.",
         ]},
        {"heading": "Certificates", "kind": "bullets", "weight": 5.8,
         "step": 0.3, "min_pages": 4, "items": [
             "Unreal Engine for Architecture, Epic Games, 2024.",
             "V-Ray Professional, Chaos, 2024.",
             "Photogrammetry for real-time, RealityCapture workshop, "
             "2022.",
         ]},
        {"heading": "Interests", "kind": "text", "weight": 6.5,
         "paragraphs": [
             "Old kitchens, brutalist libraries, sketching buildings on "
             "the train to Copenhagen, sea swimming in Ribersborg all "
             "year and very slow photography with a 1970s camera.",
         ]},
        {"heading": "References", "kind": "entries", "weight": 7,
         "min_pages": 4, "entries": [
             {"title": "Maja Holm", "org": "Art director, Nordljus Games",
              "meta": "on request", "items": []},
             {"title": "Signe Thorsen", "org": "Architect, MAA",
              "meta": "on request", "items": []},
         ]},
    ],
}
