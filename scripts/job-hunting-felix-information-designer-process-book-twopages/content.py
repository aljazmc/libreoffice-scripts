"""Process Book of Felix Amadi: who they are and everything the document
could say. The typesetting keeps what fits into two pages, the most important
first."""

PERSONA = {
    "name": "Felix Amadi",
    "headline": "Motion designer / information designer / making numbers "
                "move so that people understand them",
    "contact": ["Zurich", "felix@amadi.example", "+41 79 555 31 08",
                "amadi.studio"],
}


DOCUMENT = {
    "title": "Process Book",
    "subtitle": "“How a Virus Travels” · a 90-second explainer for "
                "school classes, from brief to broadcast",
    "sections": [
        {"heading": "Brief", "kind": "text", "weight": 0.1, "step": 4,
         "paragraphs": [
             "A cantonal health department asked for a short animation "
             "explaining how respiratory viruses spread, for children "
             "aged nine to twelve and their teachers, to be shown in "
             "classrooms before the winter season. Budget: four weeks. "
             "Constraint: no fear, no blame, no medical jargon.",
         ]},
        {"heading": "Questions", "kind": "bullets", "weight": 0.5,
         "step": 0.5, "items": [
             "What do children already believe about germs?",
             "What can a child actually do differently tomorrow?",
             "How do we show something invisible without making it "
             "scary?",
             "How do we make teachers want to show it twice?",
         ]},
        {"heading": "Research", "kind": "entries", "weight": 1, "step": 1,
         "inner": 0.6, "entries": [
             {"title": "Week 1", "fields": [
                 ("Classroom visits", "three classes drew “what a germ "
                                      "looks like”; every drawing was a "
                                      "green monster."),
                 ("Experts", "two epidemiologists and a school nurse; "
                             "agreed on three messages only."),
                 ("Insight", "children understand travel: buses, trains, "
                             "holidays. A virus is a traveller without a "
                             "ticket."),
             ]},
         ]},
        {"heading": "Sketches", "kind": "entries", "weight": 1.6,
         "step": 1, "inner": 0.6, "entries": [
             {"title": "Week 2", "fields": [
                 ("Draft A", "germs as monsters: rejected; teachers said "
                             "children would be afraid of each other."),
                 ("Draft B", "germs as dots on a map: accurate, but "
                             "boring for nine year olds."),
                 ("Draft C", "a tiny traveller hopping between people "
                             "on a tram; kept."),
                 ("Test", "shown as paper storyboards to one class; they "
                          "explained it back correctly."),
             ]},
         ]},
        {"heading": "Animation", "kind": "entries", "weight": 2.2,
         "step": 1, "inner": 0.6, "entries": [
             {"title": "Week 3", "fields": [
                 ("Style", "flat shapes, the Swiss tram colours, one "
                           "accent red for the traveller."),
                 ("Pacing", "slow; one idea every fifteen seconds; no "
                            "text on screen while the narrator speaks."),
                 ("Sound", "a children's choir humming, recorded at a "
                           "school in Winterthur."),
             ]},
         ]},
        {"heading": "Testing and release", "kind": "entries",
         "weight": 2.8, "step": 1, "inner": 0.6, "entries": [
             {"title": "Week 4", "fields": [
                 ("Test", "four classes, before and after; 80 % could "
                          "name the three actions a week later."),
                 ("Changes", "slowed the hand-washing scene; added the "
                             "word “sneeze” in all three languages."),
                 ("Release", "shown in 900 classrooms; a teacher's guide "
                             "of one page."),
             ]},
         ]},
        {"heading": "Three messages", "kind": "bullets", "weight": 3.2,
         "step": 0.4, "min_pages": 2, "items": [
             "Sneeze into your elbow.",
             "Wash your hands when you come in.",
             "Stay home when you feel ill; it is kind, not weak.",
         ]},
        {"heading": "Grid and type", "kind": "tags", "weight": 3.6,
         "step": 0.3, "min_pages": 2, "items": [
             ("Grid", "12 columns, 16:9, generous margins for "
                      "classroom projectors"),
             ("Type", "Helvetica-like grotesque, never smaller than 48 "
                      "px on screen"),
             ("Colour", "black, white, tram blue, one red"),
         ]},
        {"heading": "Storyboard", "kind": "entries", "weight": 3.0,
         "step": 0.6, "inner": 0.4, "entries": [
             {"title": "0:00 – 0:15 / the tram", "text": [
                 "A busy tram in the morning. Everyone is going "
                 "somewhere. A tiny red traveller, no bigger than a "
                 "full stop, sits on a child's sleeve."]},
             {"title": "0:15 – 0:35 / the sneeze", "text": [
                 "A sneeze. The traveller jumps to the next seat, and the "
                 "next. Children in the test laughed here, then went "
                 "quiet."]},
             {"title": "0:35 – 0:55 / the elbow", "text": [
                 "Rewind. The same sneeze into an elbow. The traveller "
                 "stays put, looking cross."]},
             {"title": "0:55 – 1:15 / the hands", "text": [
                 "The child arrives at school and washes their hands. "
                 "The traveller slides down the drain with a small "
                 "splash."]},
             {"title": "1:15 – 1:30 / staying home", "text": [
                 "A child in bed with a book, friends waving through a "
                 "window. “Staying home is kind.”"]},
         ]},
        {"heading": "Accessibility", "kind": "bullets", "weight": 3.4,
         "step": 0.4, "min_pages": 2, "items": [
             "Subtitles in German, French and Italian, burned in and "
             "optional.",
             "A Swiss German sign language version with an interpreter "
             "in the frame, not in a corner.",
             "No flashing; a slower version for children with attention "
             "difficulties.",
             "Audio description for children with visual impairments.",
         ]},
        {"heading": "Tools", "kind": "tags", "weight": 3.8, "step": 0.3,
         "min_pages": 2, "items": [
             ("Sketching", "paper, Procreate"),
             ("Animation", "After Effects, Cavalry"),
             ("Sound", "Reaper, a school choir and a borrowed "
                       "microphone"),
             ("Testing", "printed storyboards, a projector, a "
                         "questionnaire with smiley faces"),
         ]},
        {"heading": "What failed", "kind": "bullets", "weight": 4,
         "step": 0.4, "min_pages": 4, "items": [
             "The monster draft, which tested well with adults and "
             "terribly with children.",
             "A version with on-screen text; children read instead of "
             "listening and missed the point.",
             "A clever ending with a statistic; nine year olds do not "
             "care about percentages, they care about their friends.",
         ]},
        {"heading": "Teacher's guide", "kind": "text", "weight": 4.2,
         "step": 3, "min_pages": 4, "paragraphs": [
             "One page, folded once: three questions to ask before "
             "watching, three to ask after, and a five-minute activity "
             "with glitter that shows how far a sneeze travels. Teachers "
             "told us the glitter was the most memorable part of the "
             "lesson, and that their classrooms still sparkle.",
             "We wrote the guide with two teachers and tested it in the "
             "same four classes. It is available in three languages and "
             "in simple language.",
         ]},
        {"heading": "Timeline", "kind": "tags", "weight": 4.3, "step": 0.3,
         "min_pages": 4, "items": [
             ("Week 1", "research, classroom visits, expert interviews"),
             ("Week 2", "three drafts, storyboard test"),
             ("Week 3", "animation, choir recording, sound"),
             ("Week 4", "testing, changes, translation, release"),
         ]},
        {"heading": "Reception", "kind": "bullets", "weight": 4.35,
         "step": 0.3, "min_pages": 4, "items": [
             "Shown in 900 classrooms in the first winter; requested by "
             "two more cantons.",
             "A teacher in Uster reported that her class now says "
             "“traveller” instead of “germ”.",
             "Shortlisted at the Swiss Design Awards, communication "
             "category, 2026.",
             "One complaint: a parent who thought the traveller was too "
             "cute. We kept it.",
         ]},
        {"heading": "Credits", "kind": "tags", "weight": 4.4, "step": 0.3,
         "min_pages": 4, "items": [
             ("Concept, design, animation", "Felix Amadi"),
             ("Experts", "two epidemiologists, one school nurse"),
             ("Choir", "Schulhaus Altstadt, Winterthur"),
             ("Testers", "four classes and their very honest pupils"),
         ]},
        {"heading": "What I learned", "kind": "text", "weight": 4.8,
         "step": 3, "min_pages": 4, "paragraphs": [
             "Children are the best testers I have worked with: they "
             "say exactly what they understood and nothing else. I now "
             "test every health animation with someone who has no "
             "reason to be polite.",
             "And the most important design decision was the one I made "
             "last: cutting the statistic. Information design is mostly "
             "deciding what not to say.",
         ]},
    ],
}
