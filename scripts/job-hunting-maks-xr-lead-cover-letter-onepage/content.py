"""Cover Letter of Maks Kovač: who they are and everything the document
could say. The typesetting keeps what fits into one page, the most important
first."""

PERSONA = {
    "name": "Maks Kovač",
    "headline": "XR developer and former founder · virtual rooms where "
                "real hands learn real skills",
    "contact": ["Zagreb, Croatia", "maks@kovac.example",
                "+385 91 555 7403", "makskovac.xyz"],
}


DOCUMENT = {
    "title": "Cover Letter",
    "date": "Zagreb, 24 October 2026",
    "recipient": ["Dr. Lena Brandstätter", "Chief Medical Officer",
                  "Sutura VR GmbH", "Spitalgasse 23", "1090 Vienna, "
                  "Austria"],
    "subject": "XR Lead, surgical skills platform",
    "salutation": "Dear Dr. Brandstätter,",
    "signoff": "Best regards,",
    "sections": [
        {"kind": "text", "weight": 0, "step": 0.4, "paragraphs": [
            "My last company taught 3,000 people to weld in virtual "
            "reality and then went bankrupt. I learned two things from "
            "it: that skill training in VR works when the hands are "
            "taken seriously, and how much I still had to learn about "
            "everything else. I am applying for the XR Lead role at "
            "Sutura VR to bring the first lesson to surgery, and to "
            "keep learning the second inside a team that already knows "
            "its market.",
        ]},
        {"heading": "What I have built", "kind": "text", "weight": 1,
         "step": 3, "paragraphs": [
             "As co-founder and CTO of Halo XR I built a VR welding "
             "simulator with real torch controllers, used in fourteen "
             "vocational schools and two shipyards. In a shipyard pilot, "
             "trainees wasted 60 % less metal and reached certification "
             "faster. Since 2024 I have built medical XR as a contractor, "
             "most recently a central line insertion module with "
             "ultrasound guidance and force feedback, validated with "
             "forty residents and six consultants.",
             "Before that I spent three years building VR walkthroughs "
             "for architects and three as a gameplay programmer, where I "
             "learned about motion sickness by causing a great deal of "
             "it.",
         ]},
        {"heading": "Why surgery", "kind": "text", "weight": 1.4,
         "step": 3, "paragraphs": [
             "Surgical skills are hand skills learned under pressure, "
             "with too few chances to practise and real consequences "
             "for mistakes. That is exactly the problem VR is good at, "
             "if it respects the hands: the right resistance, the right "
             "angle, the right feedback at the right moment. Most "
             "medical VR I have tried is beautiful to look at and wrong "
             "to touch. Sutura's laparoscopy module is the exception, "
             "and the reason I am writing.",
         ]},
        {"heading": "About the failure", "kind": "text", "weight": 1.8,
         "step": 3, "paragraphs": [
             "Halo XR closed in 2023 when our third funding round fell "
             "through. Schools loved the product and could not afford "
             "it; shipyards could afford it but wanted custom versions "
             "faster than we could build them. We closed decently: "
             "every employee found a job, every supplier was paid and "
             "investors were informed every month until the end.",
             "I then took nine months off. I rested, wrote a long "
             "post-mortem and studied medical terminology and anatomy, "
             "because I had decided where I wanted to work next. I "
             "mention all this because a founder's failure is usually "
             "hidden in a CV, and I think it is the most useful thing in "
             "mine.",
         ]},
        {"heading": "What I would bring as XR Lead", "kind": "text",
         "weight": 2.4, "step": 3, "paragraphs": [
             "Technical leadership: I have led a team of eleven, hired "
             "most of them and shipped hardware and software together. "
             "I know the XR stack from OpenXR to custom haptic "
             "controllers and how to keep a simulation at ninety frames "
             "per second on a standalone headset.",
             "Validation habits: in welding and in medicine I have run "
             "studies with real learners and experts, and I believe a "
             "training simulator is only as good as its evidence.",
             "A founder's view of the business: I know what a sales "
             "cycle with hospitals looks like and why a feature that "
             "delights a surgeon may not help a procurement committee.",
         ]},
        {"heading": "A first prototype idea", "kind": "text",
         "weight": 3, "step": 3, "min_pages": 4, "paragraphs": [
             "I have been thinking about suturing. Most simulators "
             "teach the movement of the needle; few teach tension, the "
             "feel of a knot that is tight enough and not too tight. A "
             "low-cost haptic thread controller, combined with your "
             "existing hand tracking, could measure and teach exactly "
             "that. I have built a crude version on my desk and would "
             "love to show it to your clinical team, who will "
             "certainly improve it.",
         ]},
        {"heading": "Working with clinicians", "kind": "text",
         "weight": 3.4, "step": 3, "min_pages": 4, "paragraphs": [
             "I have learned to treat clinicians' time as the scarcest "
             "resource in a medical project. I prepare questions in "
             "advance, show prototypes rather than slides and record "
             "every decision with the reason behind it. When a "
             "consultant says a movement feels wrong, I ask them to do "
             "it on a model and film their hands; the video is worth "
             "hours of explanation.",
         ]},
        {"heading": "What failure taught me about products",
         "kind": "text", "weight": 3.5, "step": 3, "min_pages": 4,
         "paragraphs": [
             "At Halo XR I built the product before I understood how it "
             "would be bought. Our first prototype should have been a "
             "pricing conversation with twenty schools, not a torch "
             "controller. Today I ask who pays, from which budget and "
             "when, before I write a line of code, and I would bring "
             "that habit to Sutura's product discussions.",
             "I also learned that customisation is a trap for a small "
             "company. Every shipyard wanted its own version; each one "
             "made us a little more money and a lot slower. A platform "
             "with well-chosen configuration beats a hundred custom "
             "builds.",
         ]},
        {"heading": "Leading an XR team", "kind": "text", "weight": 3.6,
         "step": 3, "min_pages": 4, "paragraphs": [
             "As CTO I hired and led eleven people: developers, a 3D "
             "artist, a hardware engineer and a learning designer. I "
             "learned to protect deep work, to review code and designs "
             "every day and to make the hard calls early. Two of my "
             "former engineers now lead teams of their own.",
             "As XR Lead I would want a small, senior team that owns its "
             "modules end to end, works side by side with clinical "
             "educators and ships to real skills labs every few weeks.",
         ]},
        {"heading": "Comfort and safety", "kind": "text", "weight": 3.7,
         "step": 3, "min_pages": 4, "paragraphs": [
             "Surgeons will use VR between long shifts. Simulators must "
             "never make them sick, never strain their necks and never "
             "teach a movement that would be wrong in the real theatre. "
             "I keep the learner's body still, frame rates high and "
             "sessions short, and I treat any negative transfer of "
             "skill as a critical bug.",
         ]},
        {"heading": "Why I want to be employed again", "kind": "text",
         "weight": 3.75, "step": 3, "min_pages": 4, "paragraphs": [
             "People sometimes ask whether a former founder can be happy "
             "in someone else's company. I can, and I want to. Running "
             "Halo XR, I spent most of my time on fundraising, payroll "
             "and sales, and least on the thing I am best at: building "
             "simulations that teach hands. Sutura has a business that "
             "works and clinical partners who trust it. I would like to "
             "spend my energy where it helps most.",
             "I also miss having a boss who knows more than I do about "
             "something important. In surgical training, that is "
             "everyone with a medical degree, and I am looking forward "
             "to it.",
         ]},
        {"heading": "Hardware, honestly", "kind": "text", "weight": 3.77,
         "step": 3, "min_pages": 4, "paragraphs": [
             "Hardware is where VR training projects go to die. At Halo "
             "XR we built three generations of torch controller, and "
             "each taught us something about manufacturing, sterilising "
             "and shipping that no software project ever had. For "
             "surgery I would favour off-the-shelf haptic devices "
             "wherever possible, and custom hardware only where the "
             "skill truly depends on it, with the cleaning protocol "
             "designed before the shape.",
         ]},
        {"heading": "Questions for you", "kind": "bullets", "weight": 3.8,
         "step": 1, "min_pages": 4, "items": [
             "How are new modules validated before they are sold?",
             "Which skills do your clinical partners most want to "
             "simulate that you cannot yet?",
             "How large is the XR team, and how is it organised?",
             "What did Sutura learn from its last product that did not "
             "sell?",
         ]},
        {"heading": "Practical details", "kind": "text", "weight": 4.2,
         "step": 3, "min_pages": 2, "paragraphs": [
             "I would move to Vienna; my partner already works there "
             "half the week. I can start in January 2027.",
         ]},
        {"kind": "text", "weight": 0.2, "step": 6, "paragraphs": [
            "Thank you for reading. I would be glad to bring the central "
            "line module and the thread controller to Vienna, and to "
            "hear where your surgeons feel today's simulators lie to "
            "their hands.",
        ]},
    ],
}
