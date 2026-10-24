"""Curriculum Vitae of Felix Amadi: who they are and everything the document
could say. The typesetting keeps what fits into four pages, the most important
first."""

PERSONA = {
    "name": "Felix Amadi",
    "headline": "Motion designer / information designer / making numbers "
                "move so that people understand them",
    "contact": ["Zurich", "felix@amadi.example", "+41 79 555 31 08",
                "amadi.studio"],
}


DOCUMENT = {
    "title": "Curriculum Vitae",
    "cv": True,
    "sections": [
        {"heading": "Profile", "kind": "text", "weight": 0.4, "step": 5,
         "paragraphs": [
             "Motion designer with eleven years in broadcast, data "
             "journalism and explainer films. I turn statistics into "
             "animations that a tired person on a tram can understand "
             "in twenty seconds. During the pandemic my animated charts "
             "for Swiss television were watched by more than two million "
             "people.",
             "After a year of long COVID taught me what it means to need "
             "health information, I want to make it: clear, honest and "
             "for everyone. Looking for an information designer role in "
             "public health.",
         ]},
        {"heading": "Experience", "kind": "entries", "weight": 1,
         "step": 1.2, "entries": [
             {"title": "Freelance information designer",
              "dates": "2024 – now", "meta": "Zurich / NGOs, newsrooms, "
                                             "public bodies",
              "story": [
                  "Freelancing after illness meant choosing clients "
                  "carefully. I said yes only to work that explains "
                  "something people need, and no to most advertising. "
                  "It paid less and felt better, and it gave me the "
                  "portfolio for this application.",
              ],
              "items": [
                  "Animated explainers on heat waves and on vaccination "
                  "schedules for two cantonal health departments.",
                  "Data animations for an international NGO's annual "
                  "report on malaria, in six languages.",
                  "Workshops on charts for journalists at the Swiss "
                  "journalism school MAZ.",
              ]},
             {"title": "Gap: long COVID", "dates": "2022 – 2023",
              "meta": "eleven months unable to work",
              "items": [
                  "Fatigue, brain fog and a slow recovery with "
                  "rehabilitation at a clinic in Bern.",
                  "Read health leaflets, appointment letters and "
                  "dosage charts as a patient; most were unreadable.",
                  "Returned part-time in mid-2023 and fully in 2024.",
              ],
              "story": [
                  "I spent most of 2022 on a sofa, unable to read for "
                  "more than ten minutes. The letters from my insurer, "
                  "the clinic's leaflets and the instructions on my "
                  "medicine were the hardest things I read that year. I "
                  "kept a folder of them, redesigned a few when I could "
                  "concentrate again, and that folder is why I am "
                  "applying for this job.",
              ]},
             {"title": "Senior motion designer", "org": "SRF, Swiss "
              "public television", "dates": "2018 – 2022",
              "meta": "Zurich / news graphics",
              "items": [
                  "Designed the animated COVID-19 charts for the evening "
                  "news, broadcast daily for two years to more than two "
                  "million viewers.",
                  "Built a template system in After Effects and "
                  "Cavalry that turned new data into broadcast-ready "
                  "charts in 15 minutes.",
                  "Election night graphics for three national votes.",
                  "Led a team of four designers during the pandemic "
                  "years.",
              ],
              "story": [
                  "In March 2020 we had six hours to explain exponential "
                  "growth to the whole country. The chart we made that "
                  "afternoon, a single line on a logarithmic and a "
                  "linear scale side by side, was shown for two years. I "
                  "learned more about clarity in those six hours than in "
                  "the six years before.",
              ]},
             {"title": "Gap: Lagos", "dates": "2017",
              "meta": "six months with my father's family",
              "items": [
                  "Lived with relatives in Lagos for the first time; "
                  "designed a small campaign for a community clinic.",
              ]},
             {"title": "Motion designer", "org": "Neue Zürcher Zeitung",
              "dates": "2014 – 2017", "meta": "Zurich / data journalism "
                                              "desk",
              "story": [
                  "The NZZ data desk was six people who argued about "
                  "decimal places at lunch. I learned that a chart is a "
                  "promise of accuracy, that the axis is the most "
                  "political line on the page, and that a journalist's "
                  "best question is “so what?”.",
              ],
              "items": [
                  "Animated data stories for the website and social "
                  "media, from rents to glaciers.",
                  "First animated chart to win a European Newspaper "
                  "Award for the paper.",
              ]},
         ]},
        {"heading": "Skills", "kind": "tags", "weight": 1.6, "step": 0.5,
         "items": [
             ("Motion", "After Effects, Cavalry, Blender, Rive"),
             ("Data", "D3, Datawrapper, R and ggplot2, Excel"),
             ("Design", "typography, grid systems, Figma, Illustrator"),
             ("Communication", "plain language, accessible charts, "
                               "subtitles, sign language collaboration"),
         ]},
        {"heading": "Education", "kind": "entries", "weight": 2.2,
         "step": 1, "entries": [
             {"title": "BA Visual Communication", "org": "Zurich "
              "University of the Arts (ZHdK)", "dates": "2010 – 2014",
              "items": []},
             {"title": "CAS Health Communication", "org": "ZHAW",
              "dates": "2025", "meta": "certificate of advanced studies, "
                                       "15 ECTS", "items": []},
         ]},
        {"heading": "Awards", "kind": "bullets", "weight": 2.8,
         "step": 0.4, "items": [
             "Swiss Design Award nominee, 2021, for the pandemic charts.",
             "European Newspaper Award, 2016.",
             "Information is Beautiful Awards, shortlist, 2025, malaria "
             "report.",
         ]},
        {"heading": "Languages", "kind": "tags", "weight": 3.4, "step": 0.3,
         "items": [("German", "native, Swiss German"),
                   ("English", "fluent"), ("French", "good"),
                   ("Yoruba", "conversational")]},
        {"heading": "Teaching", "kind": "bullets", "weight": 4, "step": 0.4,
         "items": [
             "Charts for journalists, MAZ Lucerne, 2024 – now.",
             "Guest critic, Visual Communication, ZHdK, 2019 – 2022.",
         ]},
        {"heading": "Selected Work", "kind": "entries", "weight": 5,
         "step": 0.6, "inner": 0.4, "min_pages": 4, "entries": [
             {"title": "Exponential, explained", "org": "SRF, 2020",
              "text": [
                  "One line, two scales, twelve seconds. Shown daily on "
                  "the evening news for two years."]},
             {"title": "Hitze", "org": "cantonal health department, 2025",
              "text": [
                  "A 40-second animation for heat waves, aimed at older "
                  "people and their neighbours: drink, shade, check on "
                  "each other. Shown on trams and in pharmacies."]},
             {"title": "Malaria, in six languages", "org": "NGO annual "
              "report, 2025", "text": [
                  "Animated maps and charts in six languages, tested in "
                  "two countries before release."]},
             {"title": "Glacier retreat", "org": "NZZ, 2016",
              "text": [
                  "A century of the Aletsch glacier in thirty seconds; "
                  "my first animation that people shared without being "
                  "asked."]},
         ]},
        {"heading": "Health Communication Training", "kind": "bullets",
         "weight": 5.6, "step": 0.3, "min_pages": 4, "items": [
             "CAS Health Communication, ZHAW, 2025.",
             "Plain language course, Swiss Federal Chancellery "
             "guidelines, 2024.",
             "Accessible design for people with cognitive impairments, "
             "Pro Infirmis workshop, 2024.",
         ]},
        {"heading": "Clients", "kind": "bullets", "weight": 5.4,
         "step": 0.3, "min_pages": 4, "items": [
             "Two cantonal health departments: heat, vaccination, "
             "respiratory viruses.",
             "A global health NGO: malaria and maternal health reports.",
             "SRF, NZZ, Republik and Le Temps: data animations.",
             "Pro Senectute: an animated guide to online banking for "
             "people over seventy.",
             "A community clinic in Lagos: a hand-washing campaign "
             "painted on walls, 2017.",
         ]},
        {"heading": "Exhibitions", "kind": "bullets", "weight": 5.6,
         "step": 0.3, "min_pages": 4, "items": [
             "“Charts of the pandemic”, Museum für Gestaltung Zürich, "
             "group show, 2022.",
             "“Unreadable”, a wall of redesigned health letters, Basel "
             "design week, 2025.",
         ]},
        {"heading": "Talks", "kind": "bullets", "weight": 5.8, "step": 0.3,
         "min_pages": 4, "items": [
             "“Six hours to explain exponential growth”, Swiss Design "
             "Days, 2021.",
             "“Health letters, redesigned by a patient”, Design for "
             "Health conference, Basel, 2025.",
             "“The axis is political”, MAZ journalism school, 2024.",
         ]},
        {"heading": "Principles", "kind": "bullets", "weight": 6.0,
         "step": 0.3, "min_pages": 4, "items": [
             "One idea per chart; one chart per idea.",
             "Words and pictures designed together, never one after "
             "the other.",
             "Test with someone who has no reason to be polite.",
             "Slow is kind. Most animations are too fast.",
             "Red only for what matters most.",
         ]},
        {"heading": "Interests", "kind": "text", "weight": 6.5,
         "paragraphs": [
             "Swiss railway signage, Afrobeat records, slow walks (still "
             "the only kind), Lake Zurich swimming in summer and "
             "collecting badly designed medicine leaflets.",
         ]},
        {"heading": "References", "kind": "entries", "weight": 7,
         "min_pages": 4, "entries": [
             {"title": "Regula Baumann", "org": "Head of graphics, SRF",
              "meta": "on request", "items": []},
             {"title": "Dr. Kofi Mensah", "org": "Communications, global "
              "health NGO", "meta": "on request", "items": []},
         ]},
    ],
}
