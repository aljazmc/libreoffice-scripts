"""Curriculum Vitae of Zara Haddad: who they are and everything the document
could say. The typesetting keeps what fits into one page, the most important
first."""

PERSONA = {
    "name": "Zara Haddad",
    "headline": "VFX compositor turning medical animator · fifteen years of "
                "invisible effects, now making the invisible visible",
    "contact": ["London, UK", "zara.haddad@example.co.uk",
                "+44 7700 900 731", "zarahaddad.film"],
}


DOCUMENT = {
    "title": "Curriculum Vitae",
    "cv": True,
    "sections": [
        {"heading": "Logline", "kind": "text", "weight": 0.4, "step": 5,
         "paragraphs": [
             "Senior compositor with fifteen years on feature films and "
             "series, from rain that never fell to cities that were "
             "never built. I make images that audiences believe without "
             "noticing, which is exactly the skill a medical animation "
             "needs: the viewer must believe the heart, not admire the "
             "effect.",
             "After two parental leaves, the 2023 strikes and a "
             "part-time master's in medical visualisation, I am moving "
             "into medical animation for surgical education and patient "
             "understanding.",
         ]},
        {"heading": "Credits", "kind": "entries", "weight": 1, "step": 1.2,
         "entries": [
             {"title": "Freelance medical animator", "dates": "2025 – now",
              "meta": "London · surgical education and patient films",
              "items": [
                  "A four-minute film on keyhole gallbladder surgery for "
                  "patients at a London teaching hospital, reviewed by "
                  "three surgeons.",
                  "Animated cross-sections for an NHS trust's patient "
                  "information on hip replacement.",
                  "Composited endoscopic footage with 3D anatomy for a "
                  "surgical training module.",
              ],
              "story": [
                  "My first medical client was a surgeon who said "
                  "patients understood her diagrams less than she "
                  "hoped. We made a film together that shows the "
                  "operation from the patient's point of view, calm and "
                  "honest, without a drop of blood the patient would "
                  "not see. She now shows it in every pre-operative "
                  "appointment.",
              ]},
             {"title": "Gap: the 2023 strikes and after", "dates": "2023 – "
              "2024", "meta": "the work stopped; the learning did not",
              "items": [
                  "Ten months with almost no film work during the "
                  "Hollywood strikes and their aftermath.",
                  "Started the part-time MSc in Medical Visualisation "
                  "and Human Anatomy.",
              ]},
             {"title": "Senior compositor, then compositing supervisor",
              "org": "Northlight VFX", "dates": "2016 – 2023",
              "meta": "London · feature films and high-end series",
              "items": [
                  "Senior compositor on eleven features and four series, "
                  "including two Oscar-nominated visual effects teams.",
                  "Compositing supervisor on a 900-shot fantasy series; "
                  "led a team of 22 across London and Mumbai.",
                  "Built the studio's deep compositing workflow for "
                  "volumetric smoke and crowds.",
                  "Ran the compositing training programme for "
                  "graduates; 30 people trained.",
              ],
              "story": [
                  "The shot I am proudest of is one nobody has noticed: "
                  "a twelve-second close-up in a war drama where an "
                  "actor's breath had to appear in a summer location "
                  "standing in for winter. I added the breath, the cold "
                  "light on the skin and a faint shiver of the camera. "
                  "Invisible work is the hardest, and the most honest.",
              ]},
             {"title": "Gap: parental leave", "dates": "2015, 2018",
              "meta": "two children, two years in total",
              "items": [
                  "Returned each time to a more senior role; learned to "
                  "work in focused hours, which made me faster.",
              ]},
             {"title": "Compositor", "org": "Lantern Post", "dates": "2010 "
              "– 2015", "meta": "London · commercials and features",
              "items": [
                  "Commercials for cars, perfume and a bank that wanted "
                  "rain to fall upwards.",
                  "Learned Nuke from the people who wrote the studio's "
                  "pipeline, and how to stay calm at 3 am before a "
                  "delivery.",
              ]},
             {"title": "Junior roto artist", "org": "Lantern Post",
              "dates": "2009 – 2010",
              "items": ["Rotoscoped hair, frame by frame, for a year."]},
         ]},
        {"heading": "Education", "kind": "entries", "weight": 1.6,
         "step": 1, "entries": [
             {"title": "MSc Medical Visualisation and Human Anatomy",
              "org": "University of Glasgow and Glasgow School of Art",
              "dates": "2023 – 2026", "meta": "part-time, distinction · "
              "dissertation on animating heart valve disease for patients",
              "items": []},
             {"title": "BA Film and Animation", "org": "University for the "
              "Creative Arts", "dates": "2006 – 2009", "items": []},
         ]},
        {"heading": "Craft", "kind": "tags", "weight": 1.8, "step": 0.5,
         "items": [
             ("Compositing", "Nuke, deep compositing, keying, colour "
                             "science, ACES"),
             ("3D", "Maya, Houdini for volumes, Blender, ZBrush basics"),
             ("Medical", "human anatomy, reading CT and MRI, segmentation "
                         "in 3D Slicer, working with clinicians"),
             ("Leadership", "teams of up to 22, reviews, bidding, "
                            "training"),
         ]},
        {"heading": "Selected Filmography", "kind": "bullets",
         "weight": 2.6, "step": 0.4, "items": [
             "*The Long Winter* (feature, 2022) · senior compositor.",
             "*Crown of Ash* (series, 2021 – 2023) · compositing "
             "supervisor, 900 shots.",
             "*Low Tide* (feature, 2020) · senior compositor.",
             "*The Glass House* (feature, 2018) · senior compositor.",
             "*Northern Lines* (series, 2017) · compositor.",
         ]},
        {"heading": "Awards", "kind": "bullets", "weight": 3.2,
         "step": 0.4, "items": [
             "VES Award nomination, Outstanding Compositing, *Crown of "
             "Ash*, 2022.",
             "Institute of Medical Illustrators, student award, 2026.",
         ]},
        {"heading": "Languages", "kind": "tags", "weight": 3.8, "step": 0.3,
         "items": [("English", "native"), ("Arabic", "fluent, Levantine"),
                   ("French", "good")]},
        {"heading": "Teaching and Talks", "kind": "bullets", "weight": 4.4,
         "step": 0.4, "items": [
             "“Invisible effects”, guest lecture, National Film and "
             "Television School, 2022.",
             "“From smoke to blood flow”, Medical Visualisation "
             "conference, Glasgow, 2025.",
             "Compositing training programme for graduates, Northlight, "
             "2018 – 2023.",
         ]},
        {"heading": "Medical Projects", "kind": "entries", "weight": 5.2,
         "step": 0.6, "inner": 0.4, "min_pages": 4, "entries": [
             {"title": "Aortic stenosis, explained", "org": "MSc "
              "dissertation", "dates": "2026", "text": [
                  "A three-minute patient film built from anonymised CT "
                  "data, tested with twenty patients; recall of key "
                  "facts rose from 40 to 85 percent."]},
             {"title": "Keyhole gallbladder surgery", "org": "London "
              "teaching hospital", "dates": "2025", "text": [
                  "A four-minute pre-operative film combining live "
                  "action, endoscopic footage and calm 3D anatomy."]},
             {"title": "Hip replacement cross-sections", "org": "NHS "
              "trust", "dates": "2025", "text": [
                  "Twelve animated stills for printed and online patient "
                  "information, in five languages."]},
             {"title": "Endoscopic overlay", "org": "surgical training "
              "module", "dates": "2026", "text": [
                  "Tracked 3D anatomy over real endoscopic footage so "
                  "trainees can see structures hidden behind fat and "
                  "tissue; compositing at its most useful."]},
         ]},
        {"heading": "Anatomy Training", "kind": "bullets", "weight": 5.4,
         "step": 0.3, "min_pages": 4, "items": [
             "Full-body dissection, Laboratory of Human Anatomy, "
             "University of Glasgow, 2024.",
             "Cardiac imaging short course, Royal Brompton, 2025.",
             "Observed eight procedures in the catheter lab and theatre, "
             "2025 – 2026.",
         ]},
        {"heading": "Memberships", "kind": "bullets", "weight": 5.6,
         "step": 0.3, "min_pages": 4, "items": [
             "Institute of Medical Illustrators, associate member.",
             "Visual Effects Society.",
             "Association of Medical Illustrators.",
         ]},
        {"heading": "Interests", "kind": "text", "weight": 6.5,
         "paragraphs": [
             "Old anatomy atlases, silent films, swimming at Hampstead "
             "ponds, teaching my children to draw hands, and the "
             "occasional night at the cinema counting the effects nobody "
             "else sees.",
         ]},
        {"heading": "References", "kind": "entries", "weight": 7,
         "min_pages": 4, "entries": [
             {"title": "Mr Daniel Osei FRCS", "org": "Consultant surgeon",
              "meta": "on request", "items": []},
             {"title": "Hannah Clarke", "org": "VFX supervisor, Northlight "
              "VFX", "meta": "on request", "items": []},
         ]},
    ],
}
