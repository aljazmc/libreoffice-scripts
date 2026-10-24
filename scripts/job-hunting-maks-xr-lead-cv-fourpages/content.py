"""Curriculum Vitae of Maks Kovač: who they are and everything the document
could say. The typesetting keeps what fits into four pages, the most important
first."""

PERSONA = {
    "name": "Maks Kovač",
    "headline": "XR developer and former founder · virtual rooms where "
                "real hands learn real skills",
    "contact": ["Zagreb, Croatia", "maks@kovac.example",
                "+385 91 555 7403", "makskovac.xyz"],
}


DOCUMENT = {
    "title": "Curriculum Vitae",
    "cv": True,
    "sections": [
        {"heading": "Profile", "kind": "text", "weight": 0.4, "step": 5,
         "paragraphs": [
             "XR developer with ten years in virtual and augmented "
             "reality: games, architecture walkthroughs and four years "
             "running my own VR training start-up, Halo XR, which "
             "trained 3,000 welders before it ran out of money. I build "
             "simulations where hands matter: grip, tremor, angle, "
             "pressure, and the moment a learner's body understands "
             "before their head does.",
             "After closing the company and nine months of rebuilding, "
             "I want to lead XR development for surgical training, "
             "where the hands are the whole point.",
         ]},
        {"heading": "Experience", "kind": "entries", "weight": 1,
         "step": 1.2, "entries": [
             {"title": "Senior XR developer, contract", "org": "Medilab "
              "Studios", "dates": "2024 – now", "meta": "remote // "
                                                          "medical XR",
              "items": [
                  "Built a VR module for central line insertion with "
                  "ultrasound guidance, used by two teaching hospitals.",
                  "Integrated haptic gloves and a needle controller with "
                  "force feedback.",
                  "Ran validation sessions with 40 residents and 6 "
                  "consultants.",
              ],
              "story": [
                  "My first medical project humbled me. In welding a "
                  "few millimetres do not matter; with a needle near a "
                  "jugular vein they are everything. I spent weeks in a "
                  "skills lab watching residents, and rebuilt the "
                  "interaction three times until a consultant said, "
                  "“that is how it feels”.",
              ]},
             {"title": "Gap: after the start-up", "dates": "2023 – 2024",
              "meta": "nine months",
              "items": [
                  "Closed Halo XR, found jobs for all eleven employees "
                  "and returned what was left to investors.",
                  "Rested, sailed, wrote a long post-mortem and learned "
                  "medical terminology on purpose.",
              ]},
             {"title": "Co-founder and CTO", "org": "Halo XR",
              "dates": "2019 – 2023", "meta": "Zagreb // VR training for "
                                              "welding and industry",
              "items": [
                  "Built a VR welding simulator with real torch "
                  "controllers; 3,000 trainees in 14 vocational schools "
                  "and two shipyards.",
                  "Raised €1.8 million in two rounds; grew the team to "
                  "eleven people.",
                  "Cut trainee scrap metal by 60 % in a shipyard pilot; "
                  "students reached certification faster.",
                  "Shut the company down in 2023 when the third round "
                  "fell through.",
              ],
              "story": [
                  "Halo XR worked for students and failed as a business. "
                  "Vocational schools loved the simulator and could not "
                  "afford it; shipyards could afford it and wanted "
                  "custom versions we could not build fast enough. I "
                  "learned what product-market fit means by not having "
                  "it, and I learned how to close a company decently: "
                  "every employee placed, every invoice paid.",
              ]},
             {"title": "VR developer", "org": "Arhitekt Vizual",
              "dates": "2016 – 2019", "meta": "Zagreb // architecture "
                                              "walkthroughs",
              "story": [
                  "Architects were my first demanding users. They "
                  "noticed a wall two centimetres too thick and a "
                  "shadow at the wrong angle, and they taught me that "
                  "credibility in a simulation comes from details "
                  "nobody consciously sees.",
              ],
              "items": [
                  "Real-time VR walkthroughs for 40 architecture and real "
                  "estate projects.",
                  "Built a multi-user review tool so architects and "
                  "clients could meet inside unbuilt buildings.",
              ]},
             {"title": "Gameplay programmer", "org": "Pixel Forge "
              "Zagreb", "dates": "2013 – 2016", "meta": "Zagreb",
              "items": [
                  "Gameplay systems for a first-person puzzle game and an "
                  "early VR prototype that made everyone sick.",
              ]},
         ]},
        {"heading": "Skills", "kind": "tags", "weight": 1.6, "step": 0.5,
         "items": [
             ("Engines", "Unity, Unreal, OpenXR, Meta and Pico SDKs"),
             ("Interaction", "hand tracking, haptics, custom "
                             "controllers, force feedback"),
             ("Code", "C#, C++, Python, shaders"),
             ("Product", "user research, validation studies, pricing, "
                         "fundraising, hiring"),
             ("Medical", "skills lab protocols, validity studies, "
                         "working with clinicians"),
         ]},
        {"heading": "Education", "kind": "entries", "weight": 2.2,
         "step": 1, "entries": [
             {"title": "MSc Computer Science", "org": "University of "
              "Zagreb, FER", "dates": "2008 – 2013", "items": []},
             {"title": "Medical terminology and anatomy for engineers",
              "org": "online, 60 hours", "dates": "2023", "items": []},
         ]},
        {"heading": "Recognition", "kind": "bullets", "weight": 2.8,
         "step": 0.4, "items": [
             "Halo XR: EU Horizon SME Instrument phase 1, 2020.",
             "Best XR Training Solution, AWE EU, 2022.",
             "Speaker at Laval Virtual and AWE EU.",
         ]},
        {"heading": "Languages", "kind": "tags", "weight": 3.4, "step": 0.3,
         "items": [("Croatian", "native"), ("English", "fluent"),
                   ("German", "good"), ("Slovenian", "understanding")]},
        {"heading": "Talks", "kind": "bullets", "weight": 4, "step": 0.4,
         "items": [
             "“Why my VR start-up died”, Shift Conference Split, 2024.",
             "“Hands first: designing VR skill training”, AWE EU, 2022.",
             "“Welding in VR”, Laval Virtual, 2021.",
         ]},
        {"heading": "Selected Builds", "kind": "entries", "weight": 5,
         "step": 0.6, "inner": 0.4, "min_pages": 4, "entries": [
             {"title": "Weld", "org": "Halo XR, 2019 – 2023", "text": [
                 "A VR welding simulator with a real torch controller, "
                 "sparks and heat shimmer, scoring angle, speed and "
                 "distance to a tenth of a millimetre."]},
             {"title": "Central line", "org": "Medilab, 2025", "text": [
                 "Ultrasound-guided needle insertion with force "
                 "feedback; residents' first-pass success in the skills "
                 "lab rose from 55 to 78 percent."]},
             {"title": "Meet inside", "org": "Arhitekt Vizual, 2018",
              "text": [
                  "Architects and clients as avatars inside an unbuilt "
                  "house, with a laser pointer and a measuring tape."]},
             {"title": "Nausea", "org": "Pixel Forge, 2015", "text": [
                 "An early VR prototype that taught me everything about "
                 "motion sickness by causing all of it."]},
         ]},
        {"heading": "Validation Studies", "kind": "bullets", "weight": 5.4,
         "step": 0.3, "min_pages": 4, "items": [
             "Shipyard pilot, 2021: 48 trainees, scrap metal −60 %, time "
             "to certification −25 %.",
             "Vocational schools, 2022: 300 students, VR plus workshop "
             "versus workshop only; equal outcomes at lower material "
             "cost.",
             "Central line, 2025: 40 residents, first-pass success 55 → "
             "78 % in the skills lab.",
         ]},
        {"heading": "Investors and Advisors", "kind": "bullets",
         "weight": 5.6, "step": 0.3, "min_pages": 4, "items": [
             "Raised €1.8 million from two regional funds and an angel "
             "group; all investors were informed monthly until the end.",
             "Advisory board included a welding instructor of 30 years "
             "and a vocational school director; both remain friends.",
         ]},
        {"heading": "Interests", "kind": "text", "weight": 6.5,
         "paragraphs": [
             "Synthwave, sailing on the Adriatic, repairing old arcade "
             "cabinets, and cooking for people who have just had bad "
             "news.",
         ]},
        {"heading": "References", "kind": "entries", "weight": 7,
         "min_pages": 4, "entries": [
             {"title": "Prof. dr. Ivana Horvat", "org": "Anaesthesiology, "
              "teaching hospital", "meta": "on request", "items": []},
             {"title": "Tomislav Babić", "org": "Co-founder, Halo XR",
              "meta": "on request", "items": []},
         ]},
    ],
}
