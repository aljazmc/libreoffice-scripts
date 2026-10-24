"""Curriculum Vitae of Ruth Okonkwo-Lane: who they are and everything the document
could say. The typesetting keeps what fits into one page, the most important
first."""

PERSONA = {
    "name": "Ruth Okonkwo-Lane",
    "headline": "illustrator and concept artist · twenty-five years of "
                "drawing worlds for children, mostly digitally, always "
                "by hand",
    "contact": ["Bristol, UK", "ruth@okonkwolane.example",
                "+44 7700 900 288", "okonkwolane.art"],
}


DOCUMENT = {
    "title": "Curriculum Vitae",
    "cv": True,
    "sections": [
        {"heading": "Hello", "kind": "text", "weight": 0.4, "step": 5,
         "paragraphs": [
             "Illustrator and concept artist with twenty-five years of "
             "work for children: 34 picture books, concept art for four "
             "animated series and a graphic novel that took me six years. "
             "I draw digitally, in Procreate and Photoshop, but every "
             "line starts with a hand and a pencil, and I believe "
             "children can tell.",
             "My career has gaps, for my son, for my own book and for "
             "the year commissions dried up. I would now like to bring "
             "everything I know to a publisher's list as art director, "
             "and to help other illustrators make their best books.",
         ]},
        {"heading": "Work", "kind": "entries", "weight": 1, "step": 1.2,
         "entries": [
             {"title": "Freelance illustrator", "dates": "2013 – now",
              "meta": "Bristol ~ picture books, covers, animation",
              "items": [
                  "Illustrated 21 picture books for six UK publishers, "
                  "translated into 17 languages; two Kate Greenaway "
                  "longlistings.",
                  "Concept art and colour scripts for two preschool "
                  "animated series broadcast on CBeebies.",
                  "Covers for 30 middle-grade novels.",
                  "Art-directed three debut illustrators on a shared "
                  "anthology for a small press.",
              ],
              "story": [
                  "The book I am proudest of is “Grandma's Kitchen "
                  "Drum”, written by a Nigerian-British author and set "
                  "in a Bristol kitchen that could be my mother's. A "
                  "teacher sent me forty drawings her class made of "
                  "their own grandmothers' kitchens after reading it. "
                  "That pile of drawings is on my studio wall, and it "
                  "is why I want to help make more books like it.",
              ]},
             {"title": "Gap: the year the machines came", "dates": "2023",
              "meta": "commissions fell by two thirds",
              "items": [
                  "Image generators arrived and cover commissions "
                  "dried up. I taught, finished my graphic novel and "
                  "worked with the Society of Authors on contracts that "
                  "protect illustrators.",
              ]},
             {"title": "Gap: my own book", "dates": "2019",
              "meta": "a sabbatical year",
              "items": [
                  "A year with no commissions to draw “The Long Way "
                  "Round”, a graphic novel about a girl walking from "
                  "Lagos to Bristol in her grandmother's stories; "
                  "published 2024.",
              ]},
             {"title": "Concept artist", "org": "Aardvark Animation",
              "dates": "2006 – 2010", "meta": "Bristol ~ children's "
                                              "television",
              "story": [
                  "Animation taught me to draw a world rather than a "
                  "picture: a town that works from every angle, a "
                  "character who can turn round, a colour script that "
                  "carries a mood across eleven minutes. It also taught "
                  "me to work in a team of thirty, and to love notes.",
              ],
              "items": [
                  "Visual development for two animated series: "
                  "characters, locations and colour scripts.",
                  "Moved the studio's background painting from paper "
                  "to Photoshop without losing the paper.",
              ]},
             {"title": "Gap: caring", "dates": "2010 – 2012",
              "meta": "for my son",
              "items": [
                  "Two years at home while my son was seriously ill; "
                  "he is now twenty and studies music. Drew every day "
                  "in hospital corridors.",
              ]},
             {"title": "Junior illustrator", "org": "Mulberry Press",
              "dates": "2000 – 2006", "meta": "Bath ~ educational "
                                              "publishing",
              "story": [
                  "Six years of educational publishing were my "
                  "apprenticeship: forty drawings a week, a briefing "
                  "every Monday and an art editor who sent everything "
                  "back with a red pen. I learned speed, accuracy and "
                  "humility, and I have been grateful to her ever "
                  "since.",
              ],
              "items": [
                  "Drew for reading schemes, atlases and maths books; "
                  "learned to draw anything, quickly, to a brief.",
              ]},
         ]},
        {"heading": "Books", "kind": "bullets", "weight": 1.6, "step": 0.4,
         "items": [
             "*Grandma's Kitchen Drum* (2021) · Kate Greenaway "
             "longlist.",
             "*The Long Way Round* (2024) · graphic novel, author and "
             "illustrator.",
             "*Night Bus to the Sea* (2018) · Kate Greenaway longlist.",
             "*Twelve Small Foxes* (2016) · 200,000 copies sold.",
             "30 more picture books and 30 middle-grade covers, list on "
             "request.",
         ]},
        {"heading": "Tools", "kind": "tags", "weight": 2.2, "step": 0.5,
         "items": [
             ("drawing", "pencil, ink, gouache, Procreate, Photoshop"),
             ("animation", "colour scripts, visual development, Toon "
                           "Boom basics"),
             ("print", "picture book production, colour proofs, CMYK, "
                       "special finishes"),
             ("people", "art direction, briefing, giving notes that "
                        "help"),
         ]},
        {"heading": "Education", "kind": "entries", "weight": 2.8,
         "step": 1, "entries": [
             {"title": "MA Children's Book Illustration", "org": "Cambridge "
              "School of Art", "dates": "1998 – 2000", "items": []},
             {"title": "BA Illustration", "org": "University of the West "
              "of England", "dates": "1995 – 1998", "items": []},
         ]},
        {"heading": "Teaching", "kind": "bullets", "weight": 3.4,
         "step": 0.4, "items": [
             "Visiting tutor, MA Children's Book Illustration, Cambridge "
             "School of Art, 2018 – now.",
             "School visits: about 300 schools since 2005.",
             "Mentor, Illustrators of Colour mentoring scheme, 2021 – now.",
         ]},
        {"heading": "Awards", "kind": "bullets", "weight": 4, "step": 0.4,
         "items": [
             "Kate Greenaway Medal longlist, 2019 and 2022.",
             "Bristol Festival of Literature, illustrator in residence, "
             "2023.",
         ]},
        {"heading": "Advocacy", "kind": "bullets", "weight": 4.6,
         "step": 0.4, "items": [
             "Society of Authors, illustrators' group committee, 2023 – "
             "now: contract clauses on AI training and generation.",
             "Talks on fair pay for illustrators at the Bologna "
             "Children's Book Fair, 2024.",
         ]},
        {"heading": "More Picture Books", "kind": "bullets", "weight": 5.2,
         "step": 0.2, "min_pages": 4, "items": [
             "*The Allotment Year* (2023), *Rain on the Harbour* (2020), "
             "*Mo and the Moon* (2019).",
             "*A Bus Called Bessie* (2015), *Little Owl Can't Sleep* "
             "(2014), *Where Is Lola's Shoe?* (2013).",
             "*Fox Under the Floorboards* (2012), *The Swimming Lesson* "
             "(2009), *My Brother the Dragon* (2007).",
             "Reading scheme illustration, Mulberry Press, about 400 "
             "titles, 2000 – 2006.",
         ]},
        {"heading": "Art Direction So Far", "kind": "entries",
         "weight": 5.25, "step": 0.4, "inner": 0.3, "min_pages": 4,
         "entries": [
             {"title": "“First Light” anthology", "org": "Tangerine Press",
              "dates": "2025", "text": [
                  "Briefed and art-directed three debut illustrators on "
                  "a shared picture book anthology; one has since signed "
                  "a two-book deal."]},
             {"title": "MA tutoring", "org": "Cambridge School of Art",
              "dates": "2018 – now", "text": [
                  "Weekly crits for twenty students a year, from first "
                  "thumbnails to dummy books shown at Bologna."]},
             {"title": "Colour scripts", "org": "Aardvark Animation",
              "dates": "2008 – 2010", "text": [
                  "Directed the background painters' colour across 52 "
                  "episodes, with one-page notes per episode."]},
         ]},
        {"heading": "School Visits", "kind": "bullets", "weight": 5.3,
         "step": 0.3, "min_pages": 4, "items": [
             "About 300 schools since 2005, from Penzance to Inverness.",
             "A drawing workshop called “Draw your kitchen from the "
             "floor”, used by teachers since 2021.",
             "World Book Day author-illustrator, 2019 and 2022.",
         ]},
        {"heading": "Exhibitions", "kind": "bullets", "weight": 5.4,
         "step": 0.3, "min_pages": 4, "items": [
             "“Kitchens”, original artwork, Seven Stories, Newcastle, "
             "2022.",
             "“The Long Way Round”, pages and sketchbooks, Spike Island, "
             "Bristol, 2024.",
             "House of Illustration, group show, 2017.",
         ]},
        {"heading": "Interests", "kind": "text", "weight": 6.5,
         "paragraphs": [
             "zines, allotment gardening, Nigerian highlife records, "
             "swimming in the lido and drawing people on the number 72 "
             "bus without them noticing.",
         ]},
        {"heading": "References", "kind": "entries", "weight": 7,
         "min_pages": 4, "entries": [
             {"title": "Clare Whitfield", "org": "Publisher, Kestrel "
              "Children's Books", "meta": "on request", "items": []},
             {"title": "Martin Ursell", "org": "Course leader, MA "
              "Children's Book Illustration", "meta": "on request",
              "items": []},
         ]},
    ],
}
