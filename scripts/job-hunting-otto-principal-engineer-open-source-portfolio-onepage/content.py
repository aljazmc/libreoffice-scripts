"""Open Source Portfolio of Otto Lindgren: who they are and everything the document
could say. The typesetting keeps what fits into one page, the most important
first."""

PERSONA = {
    "name": "Otto Lindgren",
    "headline": "principal software engineer · databases, developer tools "
                "and maintaining things other people depend on",
    "contact": ["Helsinki", "otto@lindgren.example", "github.com/olindgren",
                "+358 40 555 1187"],
}


DOCUMENT = {
    "title": "Open Source Portfolio",
    "subtitle": "Projects I started, maintain, contributed to, or "
                "handed over · with the numbers and the lessons",
    "sections": [
        {"kind": "text", "weight": 0.2, "step": 4, "paragraphs": [
            "Open source is the most honest record of my work: every "
            "line, review and mistake is public. This document is a map "
            "of it, with the context that a commit history does not "
            "show: why each project exists, who uses it, what "
            "maintaining it has cost and taught, and what I would do "
            "differently.",
        ]},
        {"heading": "pgshift", "kind": "entries", "weight": 0.5,
         "step": 1, "inner": 0.8, "entries": [
             {"title": "creator and lead maintainer", "dates": "2018 - now",
              "meta": "Go | 9,400 stars | ~6,000 teams | 310 contributors",
              "fields": [
                  ("why", "migrations that silently took exclusive locks "
                          "kept taking down production at work."),
                  ("what", "a migration tool that refuses to run a "
                           "change that would lock a busy table, and "
                           "explains a safer way."),
                  ("users", "start-ups, two banks, a national "
                            "statistics office and a lot of side "
                            "projects."),
                  ("cost", "about eight hours a week for eight years; "
                           "much of it reviews and issues."),
                  ("learned", "the hardest part is saying no to good "
                              "ideas that would make the tool harder "
                              "to trust."),
              ],
              "items": [
                  "Governance document and four co-maintainers since "
                  "2022, so the project does not depend on me.",
                  "Release process with a public checklist; 62 releases, "
                  "never on a Friday.",
                  "One bad release, 4.0.0, fixed in four hours with a "
                  "public post-mortem.",
              ]},
         ]},
        {"heading": "restore-or-it-didnt-happen", "kind": "entries",
         "weight": 1, "step": 1, "inner": 0.8, "entries": [
             {"title": "creator", "dates": "2023 - now",
              "meta": "Go | 1,200 stars",
              "fields": [
                  ("why", "a backup you have not restored is a hope, not "
                          "a backup."),
                  ("what", "restores PostgreSQL backups on a schedule, "
                           "runs checks and reports drift."),
                  ("learned", "open-sourcing internal tools is half the "
                              "work and double the documentation."),
              ]},
         ]},
        {"heading": "PostgreSQL", "kind": "entries", "weight": 1.6,
         "step": 1, "inner": 0.8, "entries": [
             {"title": "contributor", "dates": "2022 - 2025",
              "meta": "C | 7 patches committed",
              "fields": [
                  ("what", "small fixes to pg_upgrade checks and better "
                           "documentation of logical replication "
                           "limits."),
                  ("learned", "patience; the review culture of "
                              "PostgreSQL is the best I know, and the "
                              "slowest."),
              ]},
         ]},
        {"heading": "tidewatch", "kind": "entries", "weight": 2.2,
         "step": 1, "inner": 0.8, "entries": [
             {"title": "creator", "dates": "2019 - now",
              "meta": "Rust | 400 stars | written on a boat",
              "fields": [
                  ("why", "weather and tide apps that stop working the "
                          "moment you leave the harbour."),
                  ("what", "tide predictions and cached forecasts that "
                           "work offline for weeks."),
                  ("learned", "offline-first changes every design "
                              "decision, and it should be the default "
                              "more often."),
              ]},
         ]},
        {"heading": "Tilda", "kind": "entries", "weight": 2.8,
         "step": 1, "inner": 0.8, "entries": [
             {"title": "archived", "dates": "2016",
              "meta": "Python | the start-up, open-sourced at shutdown",
              "fields": [
                  ("why", "when we closed, our customers deserved to "
                          "keep using it if they wanted."),
                  ("learned", "archive clearly; three shops still run "
                              "it, and I still answer one email a year."),
              ]},
         ]},
        {"heading": "Handed over", "kind": "entries", "weight": 3.4,
         "step": 1, "inner": 0.8, "min_pages": 2, "entries": [
             {"title": "sqlfmt-fi", "dates": "2014 - 2020",
              "meta": "a SQL formatter, now maintained by someone better",
              "fields": [
                  ("why handed over", "I stopped using it; a contributor "
                                      "cared more than I did."),
                  ("how", "six months of co-maintaining, then a public "
                          "announcement and the keys."),
                  ("learned", "handing over is a maintainer's last and "
                              "most important job."),
              ]},
         ]},
        {"heading": "How I maintain", "kind": "bullets", "weight": 3.8,
         "step": 0.5, "items": [
             "answer every new issue within a week, even if the answer "
             "is \"not now\".",
             "review the pull request, not the person.",
             "write down decisions in the repository, not in chat.",
             "a governance document before the project needs one.",
             "rest. A tired maintainer is the biggest risk to a project.",
         ]},
        {"heading": "Funding", "kind": "text", "weight": 4.2, "step": 3,
         "min_pages": 4, "paragraphs": [
             "pgshift is funded by 38 individual sponsors and three "
             "companies, which pays for CI, a domain and, once a year, a "
             "weekend in which the four maintainers meet in person. It "
             "has never paid for maintenance time, which is the honest "
             "reason I am looking for a job where that is the work.",
         ]},
        {"heading": "Talks about maintaining", "kind": "bullets",
         "weight": 4.6, "step": 0.4, "min_pages": 4, "items": [
             "\"Maintaining open source from a sailing boat\", Disobey "
             "2021.",
             "\"The last job of a maintainer: handing over\", FOSDEM "
             "2024, community devroom.",
             "\"Saying no kindly\", PGConf.EU 2023 lightning talk.",
         ]},
        {"heading": "Roadmap I would like to work on", "kind": "bullets",
         "weight": 5.0, "step": 0.4, "min_pages": 4, "items": [
             "lock-safety analysis shared between migration tools, as a "
             "library instead of five reimplementations.",
             "dry-run migrations against a copy of production statistics, "
             "so that tools can predict how long a change will take.",
             "documentation written from user incidents, not from the "
             "code.",
         ]},
        {"heading": "Numbers", "kind": "tags", "weight": 4.4, "step": 0.3,
         "min_pages": 2, "items": [
             ("stars across projects", "about 11,000"),
             ("pull requests reviewed", "2,300"),
             ("issues triaged", "4,100"),
             ("releases", "62 of pgshift, 14 of restore"),
             ("sponsors", "38 individuals, 3 companies"),
         ]},
        {"heading": "What I would do differently", "kind": "bullets",
         "weight": 4.8, "step": 0.5, "min_pages": 4, "items": [
             "add co-maintainers to pgshift two years earlier.",
             "write the contribution guide before the first contributor "
             "arrives, not after the tenth confused one.",
             "say no faster; a slow maybe is worse than a quick no.",
             "keep a changelog by hand; generated ones help nobody.",
         ]},
        {"heading": "Contributors who taught me things", "kind": "bullets",
         "weight": 5.2, "step": 0.5, "min_pages": 4, "items": [
             "**aholm**, who rewrote the lock analysis and showed me how "
             "much I did not know about PostgreSQL's lock manager.",
             "**mpereira**, a student from Recife whose first pull "
             "request was the best documentation we have.",
             "**kz-dev**, who reported 4.0.0 within twenty minutes and "
             "stayed up with me to fix it.",
         ]},
    ],
}
