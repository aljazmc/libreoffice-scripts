"""Cover Letter of Kai Berg: who they are and everything the document
could say. The typesetting keeps what fits into one page, the most important
first."""

PERSONA = {
    "name": "Kai Berg",
    "headline": "3D environment artist · ten thousand square metres of "
                "places that never existed",
    "contact": ["Malmö, Sweden", "kai.berg@example.se", "+46 73 555 6620",
                "artstation.com/kaiberg"],
}


DOCUMENT = {
    "title": "Cover Letter",
    "date": "Malmö, 24 October 2026",
    "recipient": ["Mette Lykke", "Studio Director", "Lys & Linje "
                  "Visualisering ApS", "Refshalevej 163A",
                  "1432 Copenhagen K, Denmark"],
    "subject": "Visualisation Artist, real-time and stills",
    "salutation": "Dear Mette,",
    "signoff": "Best regards,",
    "sections": [
        {"kind": "text", "weight": 0, "step": 0.4, "paragraphs": [
            "For eight years I built places that do not exist: villages "
            "for an open-world RPG, harbours for a puzzle game, a burnt "
            "ridge players still talk about online. I am applying for "
            "the Visualisation Artist position at Lys & Linje because I "
            "want to spend the next eight building images of places "
            "that will.",
        ]},
        {"heading": "What I bring from games", "kind": "text",
         "weight": 1, "step": 3, "paragraphs": [
             "Games taught me how people move through space. A player "
             "has no architect beside them, so the environment must "
             "explain itself: light pulls them towards the entrance, "
             "materials tell them what is old and what is new, and a "
             "view through a window promises something worth walking "
             "to. Good architectural images do the same for a client "
             "who cannot read plans.",
             "I am fast in Unreal Engine 5, comfortable with path "
             "tracing and Lumen, and I build my own materials in "
             "Substance and from photogrammetry. I owned three regions "
             "of Hollow Crown, built a modular kit of 300 assets and "
             "led interior lighting for the whole game.",
         ]},
        {"heading": "What I have learned since", "kind": "text",
         "weight": 1.4, "step": 3, "paragraphs": [
             "In 2024 my studio laid off 140 people, including me. I "
             "spent the following eight months learning architectural "
             "visualisation properly: physically correct exposure, "
             "measured materials, reading plans and sections, and the "
             "quiet light of a Danish afternoon instead of the dramatic "
             "sunsets of fantasy games.",
             "Since 2025 I have worked freelance for six architecture "
             "offices. My real-time model of a 120-apartment project "
             "was used in public consultation by 800 future neighbours, "
             "and my daylight studies helped a school competition entry "
             "win second prize.",
         ]},
        {"heading": "Why Lys & Linje", "kind": "text", "weight": 1.8,
         "step": 3, "paragraphs": [
             "Your images are the ones I study when I want to understand "
             "restraint. The library you visualised for Aarhus does not "
             "have a single lens flare, yet I wanted to be inside it. I "
             "would like to learn that restraint from the people who "
             "practise it every day.",
             "I am also excited by your real-time work for public "
             "consultation. Letting future neighbours stand on a balcony "
             "that does not exist yet is the most meaningful thing I "
             "have done with a game engine, and I would love to do more "
             "of it.",
         ]},
        {"heading": "Light, honestly", "kind": "text", "weight": 2.0,
         "step": 3, "paragraphs": [
             "The biggest change from games to architecture is honesty. "
             "In a game I could add a light anywhere to guide a player; "
             "in a visualisation every lamp must exist in the drawings, "
             "and the sun must stand where it will stand on that "
             "afternoon in that city. At first this felt like a cage. It "
             "now feels like the most interesting constraint I have "
             "worked with.",
             "I have learned to use real sun positions, measured "
             "reflectance values for materials and camera settings a "
             "photographer would recognise. My images are quieter than "
             "they used to be, and I think they are better.",
             "I still bring one habit from games: I test every image on "
             "people who have never seen the project. If they cannot tell "
             "me where the entrance is within three seconds, the image is "
             "not finished.",
         ]},
        {"heading": "What I would like to learn", "kind": "text",
         "weight": 2.2, "step": 3, "paragraphs": [
             "I would like to learn from visualisers who have worked "
             "with architects for years: how to read a client's nerves "
             "in a feedback round, how to choose the one view that wins "
             "a competition, and how to say no to a lens flare politely.",
             "I would also like to understand construction better. I "
             "can model a timber facade, but I want to know why it is "
             "detailed the way it is, so that my images never show "
             "something that cannot be built.",
         ]},
        {"heading": "About the gaps", "kind": "text", "weight": 2.4,
         "step": 3, "min_pages": 2, "paragraphs": [
             "My CV shows two gaps: five months in 2020, when my "
             "studio closed during the pandemic, and eight months in "
             "2024, after a round of layoffs. Both are common in games, "
             "and I used both to learn. The second gap is the reason I "
             "am writing to you: it gave me time to decide what I want "
             "to build for the rest of my career.",
         ]},
        {"heading": "A first study", "kind": "text", "weight": 3,
         "step": 3, "min_pages": 4, "paragraphs": [
             "Before writing, I rebuilt one of your published interiors, "
             "the reading room of the Aarhus library, from the "
             "photographs and the competition plans, to understand how "
             "you light. I learned that you expose for the shadows and "
             "let the windows burn slightly, which is the opposite of "
             "what games do. I would be glad to show you the study and "
             "the mistakes I made along the way.",
             "I also tested a real-time version of the same room on a "
             "laptop with a mid-range graphics card, the kind a client "
             "might bring to a meeting. It ran at forty frames per second "
             "with path-traced reflections turned off, which suggests "
             "that consultation models could be lighter than we think.",
         ]},
        {"heading": "How I work with architects", "kind": "text",
         "weight": 3.4, "step": 3, "min_pages": 4, "paragraphs": [
             "I start with the architect's intention, not the camera. "
             "What should a client feel when they first see the image? "
             "Where should their eye go? Which material are you proudest "
             "of? Only then do I choose the view, the time of day and the "
             "weather.",
             "I am used to feedback rounds, late changes to the model and "
             "the moment when someone moves a wall two days before the "
             "deadline. Games trained me to keep scenes organised so that "
             "changes are cheap.",
         ]},
        {"heading": "Real-time for consultation", "kind": "text",
         "weight": 3.6, "step": 3, "min_pages": 4, "paragraphs": [
             "The Kvarteret Plommon model taught me how powerful a "
             "real-time walkthrough is in a public meeting. Neighbours "
             "who would never read a section drawing stood on their "
             "future balconies, checked their view of the park and "
             "argued about the colour of the bricks. One older man "
             "walked to the place where his allotment used to be and was "
             "quietly pleased that a tree would stand there.",
             "I would love to help Lys & Linje grow this kind of work: "
             "light models that run on ordinary laptops, simple controls "
             "for people who have never held a game controller and "
             "honest daylight, so that nobody is promised a sun that will "
             "not shine on their window.",
             "It is also, I think, a market that will grow. Municipalities "
             "want consultation that people actually attend, and "
             "architects want their projects understood before they are "
             "built.",
         ]},
        {"heading": "Working in a team again", "kind": "text",
         "weight": 3.8, "step": 3, "min_pages": 4, "paragraphs": [
             "Freelancing has taught me to deliver alone, but I miss a "
             "studio: colleagues who look over my shoulder, critiques "
             "where someone better than me says the image is flat, and "
             "the shared pride of a competition win. At Nordljus I ran "
             "the weekly environment art review and mentored four "
             "juniors, and I would happily take part in the same rituals "
             "at Lys & Linje.",
             "I keep scenes clean, name things properly and document my "
             "setups, because I know someone else will open the file "
             "at eleven at night before a deadline.",
         ]},
        {"heading": "Questions I would ask", "kind": "bullets",
         "weight": 3.9, "step": 1, "min_pages": 4, "items": [
             "How do you divide work between stills and real-time, and "
             "is the balance changing?",
             "How early are visualisers involved in a competition?",
             "Which of your images are you proudest of, and which do you "
             "wish you could redo?",
             "How do you keep your images honest when a client asks for "
             "more sun?",
         ]},
        {"heading": "Practical details", "kind": "text", "weight": 4,
         "step": 3, "min_pages": 2, "paragraphs": [
             "I live in Malmö and commute easily over the bridge; I am "
             "available from January 2027, full-time, and would be happy "
             "to work in your studio on Refshaleøen every day.",
         ]},
        {"kind": "text", "weight": 0.2, "step": 6, "paragraphs": [
            "Thank you for considering a games artist for a real-world "
            "job. I would love to show you my reel and the library "
            "study, and to hear which of your rooms you would light "
            "differently today.",
        ]},
    ],
}
