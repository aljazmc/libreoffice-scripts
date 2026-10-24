"""Cover Letter of Leo Brandt: who they are and everything the document
could say. The typesetting keeps what fits into two pages, the most important
first."""

PERSONA = {
    "name": "Leo Brandt",
    "headline": "junior frontend developer · former carpenter · measures "
                "twice, deploys once",
    "contact": ["Leipzig", "leo@brandt.example", "+49 157 5550 4412",
                "github.com/leobrandt"],
}


DOCUMENT = {
    "title": "Cover Letter",
    "date": "Leipzig, 24.10.2026",
    "recipient": ["Werkbank GmbH", "Hiring Team", "Karl-Heine-Strasse 93",
                  "04229 Leipzig"],
    "subject": "Junior Frontend Developer",
    "salutation": "Hello Werkbank team,",
    "signoff": "Best,",
    "sections": [
        {"kind": "text", "weight": 0, "step": 0.4, "paragraphs": [
            "I used your app for two years before I knew how to build "
            "one. As a carpenter I wrote quotes in it on the van "
            "between jobs. I am applying for the Junior Frontend "
            "Developer role because I want to make it better for the "
            "people I used to work beside.",
        ]},
        {"heading": "From wood to code", "kind": "text", "weight": 1,
         "step": 3, "paragraphs": [
             "I was a carpenter for seven years. In 2022 a table saw "
             "injured my left hand. It healed, but not enough for full "
             "days at the bench. I started to learn to code with free "
             "courses, then did a sixteen-week bootcamp, and since 2024 "
             "I have built websites and a booking tool for craftspeople "
             "in Leipzig.",
             "The booking tool, Termin, is used by fourteen workshops "
             "every day. It is small, but it is real software with real "
             "users who call me when something breaks.",
         ]},
        {"heading": "Why Werkbank", "kind": "text", "weight": 1.4,
         "step": 3, "paragraphs": [
             "Your users are people like my old colleagues: busy, "
             "practical and impatient with software that wastes their "
             "time. I know how they hold a phone with dusty fingers, "
             "where they lose signal and which words they use. I can "
             "bring that to your team.",
             "I also like that you are in Leipzig and that your "
             "developers visit customers' workshops. I would love to.",
         ]},
        {"heading": "About the gaps", "kind": "text", "weight": 1.8,
         "step": 3, "paragraphs": [
             "My CV has a few: four months travelling in 2019, four "
             "months recovering in 2022 and six months of job hunting "
             "in 2024. I used the last one to learn TypeScript and "
             "testing, and to build Termin. I am still learning every "
             "day, and I know how much I do not know yet.",
         ]},
        {"heading": "What I would bring", "kind": "text", "weight": 2.4,
         "step": 3, "min_pages": 2, "paragraphs": [
             "Workshop habits: I measure before I cut, I keep my bench "
             "clean and I finish things. In code that means tests, "
             "small pull requests and cleaning up after myself.",
             "User knowledge: I have written hundreds of quotes and "
             "invoices on a phone. I know where the pain is.",
         ]},
        {"heading": "A first look", "kind": "text", "weight": 3,
         "step": 3, "min_pages": 4, "paragraphs": [
             "One thing I would love to work on: the material list in "
             "your quote screen. On a phone with gloves, the plus and "
             "minus buttons are too small, and there is no way to scan "
             "a barcode from a supplier's label. I built a small "
             "prototype of bigger controls and a scanner with a free "
             "library; it is on my GitHub.",
             "I might be wrong about what your users need most. I would "
             "start by asking them.",
         ]},
        {"heading": "Learning plan", "kind": "bullets", "weight": 3.4,
         "step": 1, "min_pages": 4, "items": [
             "First month: read the codebase, fix small bugs, visit "
             "three customers.",
             "First quarter: own one small feature end to end.",
             "First year: get good at testing, accessibility and "
             "offline support.",
         ]},
        {"heading": "What I learned on site", "kind": "text",
         "weight": 2.6, "step": 3, "min_pages": 4, "paragraphs": [
             "On a building site nothing waits for you. The plasterer "
             "comes on Tuesday whether your door frames are in or not. "
             "I learned to plan, to say early when something will be "
             "late, and to ask the old hands before I cut. I think "
             "those habits are rarer in junior developers than they "
             "should be.",
             "I also learned to work in a team of trades who each "
             "think their job is the most important. Developers, "
             "designers and product people are not so different.",
         ]},
        {"heading": "What I do not know yet", "kind": "text",
         "weight": 2.8, "step": 3, "min_pages": 4, "paragraphs": [
             "I have never worked in a large codebase, with code review "
             "from senior developers, CI pipelines and a release "
             "process. I have read about all of it and practised some "
             "of it on Termin, but I know a real team will teach me "
             "much more. I am good at being taught: I was an "
             "apprentice for three years.",
             "I also know my computer science is thin. I am working "
             "through a book on algorithms in the evenings, slowly.",
         ]},
        {"heading": "Termin, in more detail", "kind": "text",
         "weight": 3.2, "step": 3, "min_pages": 4, "paragraphs": [
             "Termin lets customers book site visits with small "
             "workshops. It sends reminders, syncs with the workshop's "
             "calendar and works on old phones. It is built in React "
             "and TypeScript with Supabase, has 140 tests and costs "
             "each workshop five euros a month, which pays my server "
             "bill and buys a coffee.",
             "The best feature came from a roofer: a button that "
             "says \"it is raining, move my visits\". It moves every "
             "outdoor appointment of the day and sends a polite "
             "message. He uses it twice a week.",
         ]},
        {"heading": "Questions", "kind": "bullets", "weight": 3.6,
         "step": 1, "min_pages": 4, "items": [
             "How often do developers visit customers?",
             "How do juniors get feedback?",
             "What breaks most on site: signal, gloves or patience?",
         ]},
        {"heading": "Practical", "kind": "text", "weight": 3.8, "step": 3,
         "min_pages": 2, "paragraphs": [
             "I live in Plagwitz, ten minutes by bike from your office, "
             "and can start in December.",
         ]},
        {"kind": "text", "weight": 0.2, "step": 6, "paragraphs": [
            "Thanks for reading. I would be happy to show you Termin "
            "and the prototype, or to build something small for you "
            "as a test.",
        ]},
    ],
}
