"""Cover Letter of Otto Lindgren: who they are and everything the document
could say. The typesetting keeps what fits into two pages, the most important
first."""

PERSONA = {
    "name": "Otto Lindgren",
    "headline": "principal software engineer · databases, developer tools "
                "and maintaining things other people depend on",
    "contact": ["Helsinki", "otto@lindgren.example", "github.com/olindgren",
                "+358 40 555 1187"],
}


DOCUMENT = {
    "title": "Cover Letter",
    "date": "Helsinki, 2026-10-24",
    "recipient": ["Ingrid Halvorsen", "VP Engineering", "Fjord Labs AS",
                  "Akersgata 32", "0180 Oslo, Norway"],
    "subject": "Principal Engineer, open-source database tooling",
    "salutation": "Hi Ingrid,",
    "signoff": "Thanks for reading,",
    "sections": [
        {"kind": "text", "weight": 0, "step": 0.4, "paragraphs": [
            "I am applying for the Principal Engineer role on your "
            "open-source database tooling team. The short version: I "
            "have maintained pgshift, a PostgreSQL migration tool used "
            "by about six thousand teams, for eight years, mostly on "
            "evenings and weekends. Your job description is the first "
            "I have seen that makes maintaining open source the job "
            "itself, and I would like to do it properly.",
        ]},
        {"heading": "Context", "kind": "text", "weight": 1, "step": 3,
         "paragraphs": [
             "I am a staff engineer at Kide Data, where I lead the "
             "storage layer of a managed PostgreSQL service with forty "
             "thousand databases. My team built zero-downtime major "
             "version upgrades, which have moved twelve thousand "
             "databases with a median pause under two seconds, and a "
             "backup verification system that restores every backup, "
             "every day.",
             "Before that I co-founded a start-up that failed, worked on "
             "developer tooling at Valo Software and spent eight years "
             "writing network management software at Nokia Siemens "
             "Networks, which is where I learned to respect schemas.",
         ]},
        {"heading": "Motivation", "kind": "text", "weight": 1.4,
         "step": 3, "paragraphs": [
             "Your tools sit in the same place as pgshift: between a "
             "developer's intention and a production database that must "
             "not go down. I use two of them every week, and I have "
             "filed issues against one of them, politely I hope. I "
             "believe that this layer of software is where small "
             "improvements prevent the largest number of bad nights.",
             "I also like how you run your projects. Your public "
             "roadmap, your response times on issues and the way your "
             "maintainers say no without making anyone feel stupid are "
             "things I have tried to do in pgshift with less time and "
             "less help.",
         ]},
        {"heading": "The gaps, for the reviewer", "kind": "text",
         "weight": 1.8, "step": 3, "paragraphs": [
             "My CV has two gaps. In 2017, after closing my start-up, I "
             "took six months off to recover and to write an honest "
             "post-mortem. In 2019 and 2020 my partner and I sailed from "
             "Helsinki to the Azores and back, eighteen months and nine "
             "thousand nautical miles. I kept maintaining pgshift from "
             "harbours, and the experience of reviewing pull requests on "
             "a 2G connection made me a much more careful reviewer.",
             "I mention the gaps because I think they are part of why I "
             "can do this job for a long time. I know what burnout looks "
             "like and how to avoid it, for myself and for the "
             "contributors I work with.",
         ]},
        {"heading": "What I would do", "kind": "text", "weight": 2.4,
         "step": 3, "min_pages": 2, "paragraphs": [
             "In the first months I would read every open issue of the "
             "projects I would work on, and answer as many as I can. It "
             "is the fastest way to learn a codebase and its users, and "
             "it tells a community that someone is listening.",
             "After that I would like to work on the problems that cause "
             "the most pain and the fewest bug reports: migrations that "
             "take locks without warning, rollbacks that do not roll "
             "back and documentation that assumes too much.",
         ]},
        {"heading": "RFC: my first six months", "kind": "entries",
         "weight": 3, "step": 0.8, "inner": 0.5, "min_pages": 4,
         "entries": [
             {"title": "Month 1 - read", "text": [
                 "Every open issue, every design document and the last "
                 "year of incident reports from your users. Pair with "
                 "each maintainer for a day."]},
             {"title": "Month 2 - answer", "text": [
                 "Take a share of issue triage; write down the three "
                 "most common problems users hit and the three most "
                 "common reasons contributors give up."]},
             {"title": "Months 3 - 4 - fix", "text": [
                 "Ship one improvement to lock safety and one to "
                 "documentation, both small, both measured."]},
             {"title": "Months 5 - 6 - propose", "text": [
                 "Write an RFC for the next large change, reviewed in "
                 "public, with a migration path for every existing "
                 "user."]},
         ]},
        {"heading": "On pgshift", "kind": "text", "weight": 3.4,
         "step": 3, "min_pages": 4, "paragraphs": [
             "If you hire me, pgshift will not be abandoned. It has four "
             "co-maintainers in three countries, a governance document "
             "and a release process that does not depend on me. I would "
             "continue to contribute, and I would be happy to discuss "
             "whether it should live closer to your tools or stay "
             "independent.",
         ]},
        {"heading": "Known limitations", "kind": "text", "weight": 3.5,
         "step": 3, "min_pages": 4, "paragraphs": [
             "Every good README lists them, so here are mine. I am slow "
             "to start large rewrites, which is usually right and "
             "occasionally expensive. I write long messages when short "
             "ones would do; colleagues have taught me to put the "
             "conclusion first. And I am not a natural at conference "
             "networking, though I enjoy the hallway conversations once "
             "someone else has started them.",
             "I am working on all three, and I am happy for a manager to "
             "tell me when they show.",
         ]},
        {"heading": "On sustainability", "kind": "text", "weight": 3.6,
         "step": 3, "min_pages": 4, "paragraphs": [
             "Open source runs on tired people. I have seen excellent "
             "maintainers disappear after a hostile issue thread or a "
             "year of unpaid weekends, and I came close myself in 2018. "
             "Part of the job, as I see it, is to make the projects "
             "survivable: co-maintainers, clear contribution paths, "
             "release processes that do not depend on one person, and "
             "a culture where saying no is normal.",
             "If Fjord Labs pays people to maintain open source, the "
             "best use of that money is to make sure the volunteers "
             "around them do not burn out.",
         ]},
        {"heading": "Open questions", "kind": "bullets", "weight": 3.7,
         "step": 1, "min_pages": 4, "items": [
             "How do you decide which features stay open source and which "
             "go into the paid product?",
             "Who has the final say on a contested design: maintainers, "
             "product or the community?",
             "How much of a principal engineer's week is expected to be "
             "community work?",
             "What happened the last time a release broke users, and "
             "what changed afterwards?",
         ]},
        {"heading": "How I work", "kind": "text", "weight": 3.8,
         "step": 3, "min_pages": 4, "paragraphs": [
             "I write design documents before code, review pull "
             "requests the same day when I can, and release only on "
             "Tuesdays and Wednesdays. I prefer asynchronous work and "
             "long-form writing, but I also enjoy a whiteboard and a "
             "colleague who disagrees with me.",
             "I am happy to work remotely from Helsinki and to visit "
             "Oslo every month; the ferry is slow, and I like it.",
         ]},
        {"kind": "text", "weight": 0.2, "step": 6, "paragraphs": [
            "Happy to walk you through pgshift's lock-safety checks, the "
            "upgrade system at Kide, or the tide tables I wrote on the "
            "boat. Whichever is most useful.",
        ]},
    ],
}
