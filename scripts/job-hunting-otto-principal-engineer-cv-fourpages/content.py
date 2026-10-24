"""Curriculum Vitae of Otto Lindgren: who they are and everything the document
could say. The typesetting keeps what fits into four pages, the most important
first."""

PERSONA = {
    "name": "Otto Lindgren",
    "headline": "principal software engineer · databases, developer tools "
                "and maintaining things other people depend on",
    "contact": ["Helsinki", "otto@lindgren.example", "github.com/olindgren",
                "+358 40 555 1187"],
}


DOCUMENT = {
    "title": "Curriculum Vitae",
    "cv": True,
    "sections": [
        {"heading": "Summary", "kind": "text", "weight": 0.4, "step": 5,
         "paragraphs": [
             "Software engineer for twenty years, the last twelve on "
             "databases and developer tools. Maintainer of **pgshift**, "
             "a schema migration tool used by thousands of teams, and "
             "author of the boring parts of several systems you may "
             "have used. I like problems where correctness matters and "
             "users are other engineers.",
             "My career has gaps: a start-up that failed, and eighteen "
             "months sailing from Helsinki to the Azores and back. "
             "Looking for a principal engineer role where I can work on "
             "open source as part of the job, not on weekends.",
         ]},
        {"heading": "Experience", "kind": "entries", "weight": 1,
         "step": 1.2, "entries": [
             {"title": "Staff engineer", "org": "Kide Data",
              "dates": "2021 - now", "meta": "Helsinki | managed "
                                             "PostgreSQL platform",
              "items": [
                  "Tech lead for the storage layer of a managed "
                  "PostgreSQL service hosting 40,000 databases.",
                  "Designed zero-downtime major version upgrades; 12,000 "
                  "databases upgraded with a median pause of 1.8 "
                  "seconds.",
                  "Built the backup verification system that restores "
                  "every backup, every day, somewhere.",
                  "Mentored eleven engineers and wrote the company's "
                  "guide to design documents.",
              ],
              "story": [
                  "The upgrade project is the work I am proudest of. "
                  "Major PostgreSQL upgrades used to mean a maintenance "
                  "window and a nervous weekend; we built logical "
                  "replication into the control plane so that customers "
                  "now press a button on a Tuesday. It took eighteen "
                  "months and three rewrites of the cut-over logic, and "
                  "it has never lost a row.",
              ]},
             {"title": "Gap: sailing sabbatical", "dates": "2019 - 2020",
              "meta": "Helsinki to the Azores and back, 9,000 nautical "
                      "miles",
              "items": [
                  "Eighteen months on a 34-foot sailing boat with my "
                  "partner.",
                  "Maintained pgshift from harbours with bad Wi-Fi; "
                  "learned to write very careful pull request reviews "
                  "on a 2G connection.",
                  "Came back with a strong opinion on offline-first "
                  "software and weather APIs.",
              ]},
             {"title": "Senior engineer", "org": "Valo Software",
              "dates": "2017 - 2019", "meta": "Helsinki | developer "
                                              "tooling",
              "items": [
                  "Built the internal deployment platform for 300 "
                  "engineers.",
                  "Started pgshift as a weekend project; the company "
                  "let me open-source it.",
              ]},
             {"title": "Gap: after the start-up", "dates": "2017",
              "meta": "six months",
              "items": [
                  "Recovered, read, wrote a long post-mortem and decided "
                  "I am better at building tools than companies.",
              ]},
             {"title": "Co-founder and CTO", "org": "Tilda",
              "dates": "2015 - 2016", "meta": "Helsinki | analytics for "
                                              "small shops",
              "items": [
                  "Built the product with two co-founders; raised a "
                  "small seed round; 120 paying shops at the peak.",
                  "Shut it down in an orderly way, refunded every "
                  "customer and open-sourced the code.",
              ],
              "story": [
                  "Tilda failed for the most common reason: we built "
                  "something people liked but did not need enough to "
                  "pay for. I learned more about software in those two "
                  "years than in the five before, mostly about "
                  "everything that is not code: pricing, support, "
                  "saying no, and closing gracefully.",
              ]},
             {"title": "Software engineer", "org": "Nokia Siemens "
              "Networks", "dates": "2006 - 2014",
              "meta": "Espoo | network management systems",
              "items": [
                  "Eight years of Java, Oracle and very large XML files; "
                  "learned to love schemas and migrations.",
              ]},
         ]},
        {"heading": "Open Source", "kind": "bullets", "weight": 1.5,
         "step": 0.5, "items": [
             "**pgshift** - schema migrations for PostgreSQL with "
             "lock-safety checks; 9,400 stars, used by about 6,000 "
             "teams.",
             "**restore-or-it-didnt-happen** - continuous backup "
             "verification; 1,200 stars.",
             "**PostgreSQL** - patches to pg_upgrade and logical "
             "replication documentation, 2022 - 2025.",
             "**tidewatch** - offline tide and weather for sailors, "
             "written on the boat; 400 stars and many grateful emails.",
         ]},
        {"heading": "Skills", "kind": "tags", "weight": 1.8, "step": 0.5,
         "items": [
             ("languages", "Go, Rust, Python, SQL, Java (in recovery)"),
             ("databases", "PostgreSQL internals, replication, "
                           "migrations, backups"),
             ("platform", "Kubernetes, Terraform, AWS, GCP, bare metal"),
             ("practice", "design docs, code review, incident command, "
                          "maintaining communities"),
         ]},
        {"heading": "Education", "kind": "entries", "weight": 2.4,
         "step": 1, "entries": [
             {"title": "MSc Computer Science", "org": "Aalto University "
              "(then Helsinki University of Technology)",
              "dates": "2001 - 2006", "items": []},
         ]},
        {"heading": "Talks", "kind": "bullets", "weight": 3, "step": 0.4,
         "items": [
             "\"Upgrading 12,000 databases on a Tuesday\", PGConf.EU 2025.",
             "\"Migrations that do not take locks\", FOSDEM 2022.",
             "\"Maintaining open source from a sailing boat\", "
             "Disobey 2021.",
             "\"Post-mortem of my start-up\", Slush side event, 2017.",
         ]},
        {"heading": "Writing", "kind": "bullets", "weight": 3.6,
         "step": 0.4, "items": [
             "\"A boring guide to design documents\", 2023.",
             "\"Why Tilda closed\", 2017, still my most-read post.",
             "\"Lock levels, explained with a sailing boat\", 2021.",
         ]},
        {"heading": "Languages", "kind": "tags", "weight": 4.2, "step": 0.3,
         "items": [("finnish", "native"), ("swedish", "native"),
                   ("english", "fluent"), ("portuguese", "harbour-level")]},
        {"heading": "Maintainer Statistics", "kind": "tags", "weight": 5.2,
         "step": 0.3, "min_pages": 4, "items": [
             ("pull requests reviewed", "2,300 since 2018"),
             ("issues triaged", "4,100"),
             ("contributors", "310 people have a commit in pgshift"),
             ("co-maintainers", "four, in three countries"),
             ("releases", "62, none of them on a Friday"),
         ]},
        {"heading": "Selected Incidents", "kind": "entries", "weight": 5.6,
         "step": 0.6, "inner": 0.4, "min_pages": 4, "entries": [
             {"title": "The 2023 backup gap", "dates": "2023", "text": [
                 "Our verification system found that backups for 0.3 % "
                 "of databases could not be restored. No customer lost "
                 "data, because we found it first. That week justified "
                 "two years of work."]},
             {"title": "pgshift 4.0.0", "dates": "2022", "text": [
                 "A release that took an exclusive lock it should not "
                 "have. Fixed in four hours, with an apology, a "
                 "post-mortem and a test that would have caught it."]},
             {"title": "Tilda's last day", "dates": "2016", "text": [
                 "Exported every customer's data, refunded every "
                 "subscription and turned off the servers at midnight. "
                 "The most dignified deploy I have done."]},
         ]},
        {"heading": "Interests", "kind": "text", "weight": 6.5,
         "paragraphs": [
             "sailing, celestial navigation, sauna, writing long emails "
             "that should have been short, and repairing old marine "
             "diesel engines with the manual in one hand.",
         ]},
        {"heading": "References", "kind": "entries", "weight": 7,
         "min_pages": 4, "entries": [
             {"title": "Laura Niemi", "org": "CTO, Kide Data",
              "meta": "on request", "items": []},
             {"title": "Anders Holm", "org": "pgshift co-maintainer",
              "meta": "github.com/aholm", "items": []},
         ]},
    ],
}
