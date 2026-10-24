"""Cover Letter of Ruth Okonkwo-Lane: who they are and everything the document
could say. The typesetting keeps what fits into four pages, the most important
first."""

PERSONA = {
    "name": "Ruth Okonkwo-Lane",
    "headline": "illustrator and concept artist · twenty-five years of "
                "drawing worlds for children, mostly digitally, always "
                "by hand",
    "contact": ["Bristol, UK", "ruth@okonkwolane.example",
                "+44 7700 900 288", "okonkwolane.art"],
}


DOCUMENT = {
    "title": "Cover Letter",
    "date": "Bristol, 24 October 2026",
    "recipient": ["Priya Sandhu", "Publishing Director", "Bramble & Quill "
                  "Books", "Paintworks, Bath Road", "Bristol BS4 3EH"],
    "subject": "Art Director, picture books",
    "salutation": "Dear Priya,",
    "signoff": "With warmest wishes,",
    "sections": [
        {"kind": "text", "weight": 0, "step": 0.4, "paragraphs": [
            "On my studio wall there are forty children's drawings of "
            "their grandmothers' kitchens, sent by a teacher in Leeds "
            "after her class read a book I illustrated. I look at them "
            "every morning. I am applying for the Art Director role at "
            "Bramble & Quill because I want to spend the next part of my "
            "career helping other illustrators make books that children "
            "answer with drawings of their own.",
        ]},
        {"heading": "What I bring", "kind": "text", "weight": 1,
         "step": 3, "paragraphs": [
             "I have illustrated 34 picture books, two of them "
             "longlisted for the Kate Greenaway Medal, and written and "
             "drawn a graphic novel. I have worked as a concept artist "
             "for children's television, drawn for educational "
             "publishers and designed covers for thirty novels. I know "
             "picture book production from the first rough to the "
             "printer's proof, and I know what it feels like to receive "
             "a brief, good or bad.",
             "I have also started to direct other artists: an anthology "
             "of three debut illustrators for a small press, and twenty "
             "students a year as a visiting tutor at Cambridge. Watching "
             "someone else's book become better because of a note I "
             "gave has become one of my favourite feelings.",
         ]},
        {"heading": "Why Bramble & Quill", "kind": "text", "weight": 1.4,
         "step": 3, "paragraphs": [
             "Your list is the one I would most like to have drawn for. "
             "You publish debut illustrators next to established ones, "
             "you give books time and you choose stories set in the "
             "Britain children actually live in. “The Market on Saturday” "
             "is the book I give to every new parent I know.",
             "I am also drawn by your commitment to human illustration. "
             "Your statement last year, that every picture in your books "
             "is drawn by a person who is paid properly, is the clearest "
             "any publisher has made, and it is one I would be proud to "
             "help keep.",
         ]},
        {"heading": "The gaps in my story", "kind": "text", "weight": 1.8,
         "step": 3, "paragraphs": [
             "My career is not a straight line. From 2010 to 2012 I "
             "stopped work while my son was seriously ill; he is now "
             "twenty and plays the double bass. In 2019 I took a year "
             "with no commissions to draw my graphic novel. And in 2023, "
             "when image generators arrived, my commissions fell by two "
             "thirds. I spent that year teaching, finishing my book and "
             "working with the Society of Authors on contracts that "
             "protect illustrators.",
             "Each gap made me more sure of what matters: children, "
             "stories, the people who draw them and the time they need.",
         ]},
        {"heading": "How I would art-direct", "kind": "text",
         "weight": 2.4, "step": 3, "paragraphs": [
             "I would give illustrators the brief I always wanted: the "
             "story, the reader, the format and the budget, and then the "
             "freedom to surprise us. Notes would be specific and kind, "
             "and given early, at the rough stage, when changes are "
             "cheap.",
             "I would also look after the parts illustrators rarely see: "
             "colour proofs, paper, the order of spreads in the print "
             "run, and the small production decisions that decide "
             "whether a picture glows or turns muddy.",
         ]},
        {"heading": "What bad briefs taught me", "kind": "text",
         "weight": 2.6, "step": 3, "min_pages": 2, "paragraphs": [
             "In twenty-five years I have received perhaps three hundred "
             "briefs. The worst described the pictures; the best "
             "described the child who would read the book. The worst "
             "came with a deadline and no budget; the best explained "
             "both and asked what I needed. I would like every "
             "illustrator who works with Bramble & Quill to receive the "
             "second kind.",
             "I have also learned that silence is the most expensive "
             "note. When an editor waits until final art to say that a "
             "character looks too old, everyone loses weeks. I give my "
             "difficult notes at the rough stage, and I give them in "
             "person when I can.",
         ]},
        {"heading": "Authors and illustrators", "kind": "text",
         "weight": 2.8, "step": 3, "min_pages": 4, "paragraphs": [
             "Picture books are a conversation between words and "
             "pictures, but often the author and illustrator never "
             "meet. I would like to introduce them early, at least once, "
             "so that the pictures can say what the words leave out and "
             "the words can stop describing what the pictures already "
             "show.",
             "I know from experience that this needs a careful art "
             "director in the middle: protecting the illustrator's "
             "freedom while making sure the author feels heard.",
         ]},
        {"heading": "Production matters", "kind": "text", "weight": 3.2,
         "step": 3, "min_pages": 4, "paragraphs": [
             "Some of my books have been printed beautifully and some "
             "have not, and the difference was rarely the illustration. "
             "It was paper, colour proofs, the press check and someone "
             "who cared. For “Night Bus to the Sea” I spent two days at "
             "the printer matching forty shades of blue; the book has "
             "sold for eight years partly because the night looks right.",
             "As art director I would want to be at press checks for "
             "our most important books, and to build a relationship with "
             "printers that makes illustrators' colours survive.",
         ]},
        {"heading": "Questions I would ask", "kind": "bullets",
         "weight": 3.6, "step": 1, "min_pages": 4, "items": [
             "How do editorial and design decide which illustrator to "
             "approach for a text?",
             "How many books a year would the art director oversee?",
             "How are illustrators paid, and could advances be staged "
             "differently?",
             "Which of your recent books would you print differently?",
         ]},
        {"heading": "The first list", "kind": "text", "weight": 3,
         "step": 3, "min_pages": 4, "paragraphs": [
             "In my first year I would like to meet every illustrator on "
             "your list, look at every book in production and understand "
             "how decisions are made between editorial, design and "
             "sales. I would change very little before I understood "
             "why things are as they are.",
             "Then I would like to start a small scheme for debut "
             "illustrators from backgrounds that rarely reach "
             "publishing: a paid portfolio review each spring, and one "
             "commission a year from among them. My own career began "
             "because someone took a chance on a portfolio of drawings "
             "of Bristol buses.",
         ]},
        {"heading": "On machines", "kind": "text", "weight": 3.4,
         "step": 3, "min_pages": 4, "paragraphs": [
             "I am not against technology; I have drawn digitally for "
             "twenty years. But I believe picture books should be drawn "
             "by people, because children learn to look by looking at "
             "what people saw. As art director I would make sure "
             "contracts, briefs and production keep that promise, and "
             "that illustrators are credited and paid properly.",
         ]},
        {"heading": "Practical details", "kind": "text", "weight": 3.8,
         "step": 3, "min_pages": 2, "paragraphs": [
             "I live fifteen minutes' walk from Paintworks. I can start "
             "in January and would like to keep a small amount of my own "
             "illustration work, with your agreement, as it keeps my "
             "hand and my eye honest.",
         ]},
        {"kind": "text", "weight": 0.2, "step": 6, "paragraphs": [
            "Thank you for reading. I would love to bring my sketchbooks "
            "and the forty kitchens, and to hear which books you wish "
            "you had published.",
        ]},
    ],
}
