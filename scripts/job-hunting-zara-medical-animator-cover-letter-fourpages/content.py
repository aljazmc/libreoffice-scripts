"""Cover Letter of Zara Haddad: who they are and everything the document
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
    "title": "Cover Letter",
    "date": "London, 24 October 2026",
    "recipient": ["Professor Fiona MacLeod", "Director",
                  "Halden Centre for Medical Visualisation",
                  "Little France Crescent", "Edinburgh EH16 4SB"],
    "subject": "Senior Medical Animator",
    "salutation": "Dear Professor MacLeod,",
    "signoff": "With warm regards,",
    "sections": [
        {"kind": "text", "weight": 0, "step": 0.4, "paragraphs": [
            "In 2019 my father had a heart valve replaced. The night "
            "before the operation, the surgeon showed him a diagram, and "
            "my father, an engineer, nodded politely and understood "
            "nothing. I had spent ten years making audiences believe in "
            "dragons, and I could not help him believe in his own "
            "heart. I am applying for the Senior Medical Animator post "
            "because I have spent the years since learning how.",
        ]},
        {"heading": "Fifteen years of invisible work", "kind": "text",
         "weight": 1, "step": 3, "paragraphs": [
             "I have worked in film visual effects since 2009, as a "
             "compositor, senior compositor and compositing supervisor, "
             "on eleven features and four series. My job was to make "
             "images that viewers believe without noticing: breath in "
             "cold air, rain on glass, light that matches. That is the "
             "same skill a good medical animation needs. The viewer "
             "must believe the anatomy and never be distracted by the "
             "effect.",
             "As compositing supervisor on a 900-shot series I led a team "
             "of 22 across two countries, built review processes that "
             "kept quality steady over two years and trained thirty "
             "graduates. I know how to deliver complex work on time, with "
             "people, and how to give feedback that helps.",
         ]},
        {"heading": "Learning medicine", "kind": "text", "weight": 1.4,
         "step": 3, "paragraphs": [
             "In 2023, when the strikes stopped film work, I started the "
             "part-time MSc in Medical Visualisation and Human Anatomy in "
             "Glasgow. I dissected, learned to read CT and MRI, segmented "
             "anatomy in 3D Slicer and worked with surgeons and patients. "
             "My dissertation, an animation explaining aortic valve "
             "disease to patients, received a distinction and a student "
             "award from the Institute of Medical Illustrators.",
             "Since 2025 I have made patient films and surgical training "
             "material as a freelancer, including a film on keyhole "
             "gallbladder surgery now shown in every pre-operative "
             "appointment at a London teaching hospital.",
         ]},
        {"heading": "Why the Halden Centre", "kind": "text",
         "weight": 1.8, "step": 3, "paragraphs": [
             "Your Centre is one of very few places where animators, "
             "anatomists and clinicians sit in the same room, and where "
             "films are tested with patients before they are finished. "
             "Your study on animated consent information, which showed "
             "that patients remembered twice as much after watching a "
             "film, is the reason I believe this work matters.",
             "I would bring a production discipline from film that I "
             "think a research centre can use: shot breakdowns, review "
             "rounds with clear notes, colour pipelines that keep the "
             "same heart the same red in every shot, and the habit of "
             "delivering.",
         ]},
        {"heading": "What film can give medicine", "kind": "text",
         "weight": 2.2, "step": 3, "min_pages": 2, "paragraphs": [
             "Film is very good at three things medicine needs: "
             "directing attention, controlling time and calming "
             "emotion. A good shot tells the eye where to look; a good "
             "edit slows down the moment that matters and skips the "
             "rest; a good soundtrack lowers a heart rate. Patient films "
             "can use all three, honestly.",
             "Film also has habits medicine may find useful: the "
             "animatic that lets everyone agree on a story before the "
             "expensive work, and review notes that name a frame and a "
             "problem rather than a feeling.",
         ]},
        {"heading": "What medicine has taught me", "kind": "text",
         "weight": 3.2, "step": 3, "min_pages": 4, "paragraphs": [
             "Dissection taught me that bodies are messier, more varied "
             "and more beautiful than any model. No two hearts I saw "
             "looked like the textbook. My animations now include a "
             "little of that variation, so that patients do not think "
             "something is wrong with them when their own scan looks "
             "different.",
             "Patients taught me the rest. In my dissertation screenings, "
             "a woman of eighty asked me to slow down the moment the "
             "valve opened, because she wanted to see it twice. We "
             "added a gentle repeat, and every later viewer remembered "
             "that moment best.",
         ]},
        {"heading": "Leading people", "kind": "text", "weight": 3.6,
         "step": 3, "min_pages": 4, "paragraphs": [
             "As a compositing supervisor I led 22 artists in two "
             "countries. I learned that most problems in a team are "
             "unclear notes and unspoken deadlines, and that a "
             "supervisor's best tool is a calm daily review where every "
             "artist knows what good looks like.",
             "At the Centre I would be glad to mentor junior animators "
             "and students, and to bring some of the production "
             "structure of film to projects that run alongside research.",
         ]},
        {"heading": "Questions I would ask", "kind": "bullets",
         "weight": 3.8, "step": 1, "min_pages": 4, "items": [
             "How do clinicians and animators share decisions when "
             "accuracy and clarity pull in different directions?",
             "How are films tested with patients, and who decides when "
             "a film is finished?",
             "Which of the Centre's films are you proudest of, and "
             "which would you remake?",
             "Is there room for live action alongside 3D animation?",
         ]},
        {"heading": "About the gaps", "kind": "text", "weight": 2.4,
         "step": 3, "min_pages": 2, "paragraphs": [
             "My CV has three gaps: two parental leaves in 2015 and "
             "2018, and most of 2023, when the strikes in the United "
             "States stopped much of the work in London. Each time I came "
             "back changed. After the children I worked in shorter, more "
             "focused hours; after the strikes, I changed fields. I do "
             "not hide these years, because they explain who I am now.",
         ]},
        {"heading": "Accuracy and humility", "kind": "text", "weight": 3,
         "step": 3, "min_pages": 4, "paragraphs": [
             "Film taught me to make things look right. Medicine has "
             "taught me that looking right is not enough. In my first "
             "patient film I animated a gallbladder a little too "
             "beautifully, and a surgeon pointed out that real ones are "
             "rarely that colour and never that clean. I changed it. I "
             "now ask clinicians to review every anatomical shot twice: "
             "once for accuracy and once for what a frightened patient "
             "might misunderstand.",
             "I also know the limits of what I know. I am not a "
             "clinician, and my job is to serve their knowledge, not to "
             "replace it.",
         ]},
        {"heading": "A first idea", "kind": "text", "weight": 3.4,
         "step": 3, "min_pages": 4, "paragraphs": [
             "I have attached a treatment for a short patient film, “A "
             "Valve, Replaced”, about transcatheter aortic valve "
             "implantation. It follows a patient from the waiting room to "
             "the first walk after the procedure and shows the valve "
             "travelling to the heart in a way that is accurate, calm "
             "and, I hope, a little beautiful. It is written for my "
             "father, who would have understood it.",
             "I would of course develop it only with your clinicians and "
             "patients, and only if it fits the Centre's priorities.",
         ]},
        {"heading": "Practical details", "kind": "text", "weight": 4,
         "step": 3, "min_pages": 2, "paragraphs": [
             "We are ready to move to Edinburgh as a family, and the "
             "children have already chosen a favourite hill. I can start "
             "in March 2027.",
         ]},
        {"kind": "text", "weight": 0.2, "step": 6, "paragraphs": [
            "Thank you for considering my application. I would love to "
            "show you my dissertation film and the gallbladder film, and "
            "to hear how the Centre decides which stories to tell next.",
        ]},
    ],
}
