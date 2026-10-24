"""A Valve, Replaced of Zara Haddad: who they are and everything the document
could say. The typesetting keeps what fits into four pages, the most important
first."""

PERSONA = {
    "name": "Zara Haddad",
    "headline": "VFX compositor turning medical animator · fifteen years of "
                "invisible effects, now making the invisible visible",
    "contact": ["London, UK", "zara.haddad@example.co.uk",
                "+44 7700 900 731", "zarahaddad.film"],
}


DOCUMENT = {
    "title": "A Valve, Replaced",
    "subtitle": "Treatment for a four-minute patient film about "
                "transcatheter aortic valve implantation (TAVI)",
    "sections": [
        {"heading": "Logline", "kind": "text", "weight": 0.1, "step": 4,
         "paragraphs": [
             "A retired engineer about to have his heart valve replaced "
             "follows a tiny folded valve on its journey from his leg to "
             "his heart, and discovers that the operation he feared is "
             "smaller, gentler and more ingenious than he imagined.",
         ]},
        {"heading": "Waiting room", "kind": "entries", "weight": 0.5,
         "step": 1, "inner": 0.6, "entries": [
             {"title": "0:00 – 0:30", "text": [
                 "Live action, soft and quiet. JOSEPH, 78, sits with his "
                 "daughter. His hand rests on his chest. A nurse calls "
                 "his name. As he stands, the camera drifts towards his "
                 "chest and the image dissolves into a translucent "
                 "heart, beating slowly, slightly too loudly."],
              "items": [
                  "Audience learns: this film is about him, and about "
                  "them.",
                  "Accuracy note: heart rate 72, slightly irregular "
                  "sound only, no arrhythmia shown.",
              ]},
         ]},
        {"heading": "The narrow door", "kind": "entries", "weight": 1,
         "step": 1, "inner": 0.6, "entries": [
             {"title": "0:30 – 1:10", "text": [
                 "Inside the heart. The aortic valve, three leaflets, "
                 "stiff and crusted with calcium, opens only halfway. "
                 "Blood squeezes through. A simple graphic shows the "
                 "opening shrinking from a coin to a button. Narration "
                 "explains, in one sentence, why Joseph gets tired on "
                 "the stairs."],
              "items": [
                  "Audience learns: what aortic stenosis is, without the "
                  "word until the end of the scene.",
                  "Accuracy note: calcification pattern from the CT of "
                  "an anonymised patient, approved by a cardiologist.",
              ]},
         ]},
        {"heading": "A small door in the leg", "kind": "entries",
         "weight": 1.6, "step": 1, "inner": 0.6, "entries": [
             {"title": "1:10 – 1:50", "text": [
                 "The catheter lab, stylised and calm. A thin tube enters "
                 "an artery at the top of the leg. We follow a folded "
                 "valve, crimped onto a balloon, as it travels up the "
                 "aorta like a small boat against a gentle current. "
                 "Joseph is awake, lightly sedated, talking to the "
                 "nurse."],
              "items": [
                  "Audience learns: no open chest, usually no general "
                  "anaesthetic, a small cut in the groin.",
                  "Accuracy note: catheter path checked against "
                  "fluoroscopy footage; scale exaggerated twice and "
                  "flagged on screen as “not to scale”.",
              ]},
         ]},
        {"heading": "The new valve opens", "kind": "entries",
         "weight": 2.2, "step": 1, "inner": 0.6, "entries": [
             {"title": "1:50 – 2:40", "text": [
                 "The valve reaches the old one. The balloon inflates; "
                 "the new valve unfolds like a flower and pushes the old "
                 "leaflets aside. The first beat: blood flows freely, the "
                 "sound of the heart softens. The only moment of music "
                 "in the film."],
              "items": [
                  "Audience learns: the old valve stays; the new one "
                  "works inside it.",
                  "Accuracy note: deployment timing and rapid pacing "
                  "simplified, reviewed by an interventional "
                  "cardiologist.",
              ]},
         ]},
        {"heading": "The first walk", "kind": "entries", "weight": 2.8,
         "step": 1, "inner": 0.6, "entries": [
             {"title": "2:40 – 3:30", "text": [
                 "Live action again, the next morning. Joseph walks down "
                 "the ward corridor with a physiotherapist. He takes the "
                 "stairs, slowly, and laughs. His daughter films him on "
                 "her phone."],
              "items": [
                  "Audience learns: most patients walk within a day and "
                  "go home within a few days.",
                  "Accuracy note: recovery times from the hospital's own "
                  "data, with a line saying everyone is different.",
              ]},
         ]},
        {"heading": "What to ask", "kind": "entries", "weight": 3.2,
         "step": 1, "inner": 0.6, "min_pages": 2, "entries": [
             {"title": "3:30 – 4:00", "text": [
                 "Simple titles on a calm background: three questions "
                 "patients may want to ask their team, and where to find "
                 "more information. No logos until the last second."]},
         ]},
        {"heading": "Characters", "kind": "entries", "weight": 3.4,
         "step": 0.6, "inner": 0.4, "min_pages": 4, "entries": [
             {"title": "Joseph, 78", "text": [
                 "Retired engineer, curious, polite, frightened. He wants "
                 "to understand how the thing works more than he wants "
                 "reassurance."]},
             {"title": "Amira, his daughter", "text": [
                 "The person who will watch this film at home with him. "
                 "She asks the questions he does not."]},
             {"title": "The nurse, our narrator", "text": [
                 "A real cardiac nurse, never seen on camera, speaking "
                 "the way she speaks to patients every day."]},
         ]},
        {"heading": "Research", "kind": "bullets", "weight": 3.5,
         "step": 0.4, "min_pages": 4, "items": [
             "Interviews with six patients after TAVI: what they feared, "
             "what surprised them, what they wish they had known.",
             "Two days observing the catheter lab and the ward.",
             "Anonymised CT data for anatomy, approved for teaching use.",
             "Existing leaflets and their reading age (most score at 14 "
             "or above; the film aims for 9).",
         ]},
        {"heading": "Style", "kind": "bullets", "weight": 3.6,
         "step": 0.5, "min_pages": 2, "items": [
             "Anatomy translucent and warm, never gory; no blood outside "
             "vessels.",
             "One colour for the patient's own tissue, one for the "
             "device, used consistently.",
             "Live action shot handheld but steady; natural light.",
             "Narration by a nurse, not an actor; plain words, short "
             "sentences.",
             "Subtitles in English, Polish, Urdu and Gaelic from the "
             "start.",
         ]},
        {"heading": "Review plan", "kind": "entries", "weight": 4,
         "step": 0.6, "inner": 0.4, "min_pages": 4, "entries": [
             {"title": "Clinical review", "text": [
                 "An interventional cardiologist and a cardiac nurse "
                 "review the animatic and every anatomical shot."]},
             {"title": "Patient review", "text": [
                 "Two screenings with patients waiting for TAVI and "
                 "their families; we measure what they remember a week "
                 "later."]},
             {"title": "Accessibility review", "text": [
                 "Checked for subtitles, audio description and colour "
                 "contrast before final delivery."]},
         ]},
        {"heading": "Schedule", "kind": "tags", "weight": 4.4, "step": 0.3,
         "min_pages": 4, "items": [
             ("Weeks 1 – 2", "research, script, clinical interviews"),
             ("Weeks 3 – 5", "storyboard and animatic; first clinical "
                             "review"),
             ("Weeks 6 – 10", "animation, live action shoot, "
                              "compositing"),
             ("Weeks 11 – 12", "patient screenings, revisions, "
                               "subtitles, delivery"),
         ]},
        {"heading": "Alternatives considered", "kind": "bullets",
         "weight": 4.6, "step": 0.4, "min_pages": 4, "items": [
             "A fully animated film: cheaper, but patients said they "
             "wanted to see a real person walking afterwards.",
             "A film from the surgeon's point of view: accurate, but "
             "frightening; kept as a separate film for trainees.",
             "An ending with statistics: replaced by the stairs, which "
             "every patient understood immediately.",
         ]},
        {"heading": "Budget", "kind": "tags", "weight": 4.7, "step": 0.3,
         "min_pages": 4, "items": [
             ("Animation and compositing", "eight weeks, one senior and "
                                           "one junior animator"),
             ("Live action", "one day, small crew, the hospital's own "
                             "ward"),
             ("Sound and narration", "two days"),
             ("Translation and subtitles", "four languages"),
         ]},
        {"heading": "Why this film", "kind": "text", "weight": 4.8,
         "step": 3, "min_pages": 4, "paragraphs": [
             "Patients waiting for TAVI are often old, frightened and "
             "given leaflets written for younger readers. A short film "
             "they can watch at home, with their family, at their own "
             "pace, can change how they arrive on the day.",
             "And for me, it is the film I could not show my father.",
         ]},
    ],
}
