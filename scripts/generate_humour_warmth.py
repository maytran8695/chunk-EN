import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from lib import generate_topic

OUT_PATH = os.path.join(SCRIPT_DIR, "..", "data", "humour-warmth.json")

# Phrase content below is copied by hand from the "Humour & Warmth" topic
# (tier "growth" / nav tab "Confidence & Humour") in final_topics.json,
# sections H1.1-H8.4.
#
# Like Confidence, this topic is written as Vietnamese commentary ABOUT
# humour technique, but — unlike Confidence — most headers embed a rich
# set of actual quotable English one-liners inside that commentary, so
# most headers survive with real content.
#
# Headers with no surviving English phrases (pure mechanism/rule/culture
# commentary, nothing sayable) are skipped entirely: H2.1 (four levels of
# getting a joke), H2.3 (empty), H2.4 (laughter-as-social-signal theory),
# H3.1 (empty), H4.1 (safety rules for teasing), H5.3 (email-vs-chat
# sarcasm rule — only a bare/emoji contrast, nothing to select as its own
# chunk), H7.1-H7.5 (British/American/Australian/Vietnamese cultural
# comparison + workplace-boundary rules), and H8.4 (a risk-ladder roadmap
# that just re-cites phrases already captured under their own headers).
#
# Several headers bundle multiple distinct functions and were split,
# mirroring the H14 5-way split in generate_core_patterns.py:
#   - H2.2 ("response toolkit, mild to strong") -> 3 groups: laughing
#     along, complimenting the joke directly, and empathising with a
#     shared-pain joke.
#   - H3.2 ("self-deprecation bank") -> 2 groups: everyday quips vs.
#     lines for after a mistake/mediocre outcome (distinct trigger
#     situations).
#   - H4.2 ("safe teasing bank") -> 5 groups by target (late / boasting /
#     mistake / bad idea / talking too much), same shape as core H14.
#   - H4.3 ("receiving a tease") -> 2 groups: accepting gracefully vs.
#     firing back lightly.
#   - H6.1 ("playful register") -> 2 groups: mock-seriousness/exaggeration
#     sentences vs. single playful vocabulary words.
# H5.1 and H5.2 are merged (both are "signal it's sarcasm, aimed at the
# situation not a person" — H5.1 alone only contributed 2 lines).
# H5.4: only the two lines that are things YOU would say ("Are you being
# sarcastic?", "Ha.") are kept; "Brilliant." and "How lovely for you." are
# examples of what someone else says sarcastically, not a chunk to select
# as your own answer in this quiz's question format, so they're dropped.
# H8.2: "I was only joking" and "it's fine" are explicitly flagged in the
# source as lines NOT to say / said by the other person, so they're
# dropped; only the four genuine repair lines are kept.
TIER_ID = "growth"
TIER_NAME = "Confidence & Humour"

groups_def = [
    ("Reacting to what just happened in the room",
     "The projector just died mid-presentation, or you're in the fourth meeting this month about the same unresolved issue, and you want a witty in-the-moment remark, not a rehearsed joke.",
     "used as a witty reaction to something that just happened in the room, rather than a prepared joke or story",
     [
        ("Well, this is going brilliantly.", "The projector froze for the third time and she just said, 'Well, this is going brilliantly,' and the room relaxed."),
        ("Same time next week?", "As the fourth meeting on the same topic wrapped up with nothing resolved, he deadpanned, 'Same time next week?'"),
     ]),
    ("Mock-serious humour: build-up, then undercut",
     "You want to set something up as if it's important or dramatic, then deflate it with a plain, deadpan twist.",
     "used to build something up seriously — as a system, an achievement, or a formal claim — then undercut it with a plain, deadpan twist",
     [
        ("We have a robust risk framework. It's called hoping.", "When someone asked about contingency planning, she said, 'We have a robust risk framework. It's called hoping.'"),
        ("After twenty years in this industry, I have learned... absolutely nothing.", "He opened his retirement speech with, 'After twenty years in this industry, I have learned... absolutely nothing,' and got the biggest laugh of the night."),
        ("I have reviewed the biscuit situation. It is dire.", "Someone asked if the kitchen needed restocking, and she replied, 'I have reviewed the biscuit situation. It is dire.'"),
        ("It's been a challenging week.", "The entire project had collapsed, so he just told the team, 'It's been a challenging week,' and everyone laughed at the understatement."),
        ("I've read that email four hundred times.", "Waiting for the client to reply, she joked, 'I've read that email four hundred times,' checking her phone again."),
     ]),
    ("Callback humour",
     "Someone made a joke earlier in the conversation or meeting, and you want to bring it back later — it shows you were genuinely listening, which lands as both funny and warm.",
     "used to bring back an earlier joke or detail later in the conversation, which shows you were genuinely listening and lands as both funny and warm",
     [
        ("Well, at least it's better than the coffee.", "Someone had joked about the terrible coffee at 10am; at 3pm, when a report came back mediocre, she said, 'Well, at least it's better than the coffee.'"),
        ("...much like [X].", "Reviewing a second failed prototype, he said, '...much like the biscuit situation earlier,' and the room groaned and laughed."),
        ("Second only to [X].", "She rated the new coffee machine, 'Second only to the biscuit incident, this is the best thing that's happened all week.'"),
        ("Right — and on that note, someone please fix the coffee.", "As the meeting wrapped up, he closed with, 'Right — and on that note, someone please fix the coffee,' tying it back to the morning's running joke."),
     ]),
    ("Laughing along / verbal appreciation",
     "A colleague just made a joke and you want to show you found it genuinely funny, without necessarily topping it.",
     "used to show you found something genuinely funny, as a light verbal response rather than a full laugh or a joke of your own",
     [
        ("Ha!", "He read her one-line reply to the group chat and just typed back, 'Ha!'"),
        ("That's brilliant.", "When his colleague delivered the punchline, she laughed and said, 'That's brilliant.'"),
        ("Ha, very good.", "He smirked at the pun and said, 'Ha, very good,' before getting back to the agenda."),
        ("I like that.", "She chuckled at his description of the project and said, 'I like that.'"),
        ("That's a good one.", "He grinned and said, 'That's a good one,' after her quick comeback."),
     ]),
    ("Complimenting someone's joke directly",
     "Someone's just been on a roll with the jokes and you want to acknowledge it directly, not just laugh.",
     "used to directly compliment someone for being funny, rather than just laughing along",
     [
        ("You're on form today.", "After his third good line in a row, she said, 'You're on form today.'"),
        ("Nice.", "He nodded appreciatively at her joke and said, 'Nice.'"),
        ("Quality.", "She looked over at him after the punchline and just said, 'Quality.'"),
     ]),
    ("Empathizing with a shared-pain joke",
     "Someone just made a joke about a shared frustration — a bad commute, a broken system, an annoying process — and you want to signal 'me too' rather than solve it.",
     "used to signal shared frustration after someone jokes about a common pain point, rather than offering a solution",
     [
        ("Tell me about it.", "When he joked about the Monday inbox pile-up, she sighed, 'Tell me about it.'"),
        ("You and me both.", "He complained jokingly about the broken coffee machine, and she said, 'You and me both.'"),
        ("Don't. Just don't.", "Someone brought up the failed system migration as a joke, and he groaned, 'Don't. Just don't.'"),
     ]),
    ("Self-deprecating quips (everyday)",
     "You want to poke gentle fun at your own small, everyday habits to keep things light and relatable.",
     "used to make light of your own small, everyday habits or quirks, to stay relatable rather than defensive",
     [
        ("I have the attention span of a goldfish.", "She laughed and admitted, 'I have the attention span of a goldfish,' after losing her train of thought mid-sentence."),
        ("My inbox is a crime scene.", "He opened his laptop and muttered, 'My inbox is a crime scene,' before diving in."),
        ("That's very on brand for me.", "She spilled coffee on her notes and said, 'That's very on brand for me.'"),
        ("Classic me.", "He showed up five minutes late again and said, 'Classic me,' with a grin."),
        ("I peaked early today.", "By 11am he was already exhausted and joked, 'I peaked early today.'"),
        ("I'm told I'm an adult, but I have my doubts.", "She laughed off forgetting her badge again with, 'I'm told I'm an adult, but I have my doubts.'"),
     ]),
    ("Self-deprecating humor after a mistake or mediocre outcome",
     "Something you did just went wrong, or turned out only mediocre, and you want to acknowledge it lightly instead of getting defensive.",
     "used to acknowledge a mistake or a mediocre outcome lightly, without getting defensive or over-explaining",
     [
        ("I'd love to say that was planned.", "The demo crashed at exactly the wrong moment and she laughed, 'I'd love to say that was planned.'"),
        ("I have no idea what I'm doing, but I'm doing it confidently.", "He fumbled through the new software live and joked, 'I have no idea what I'm doing, but I'm doing it confidently.'"),
        ("Well, that went about as well as expected.", "The pitch flopped and she said dryly, 'Well, that went about as well as expected.'"),
        ("Don't ask me how I managed that.", "He somehow broke the printer again and sighed, 'Don't ask me how I managed that.'"),
        ("In my defence... I have no defence.", "Caught double-booking the meeting room, she said, 'In my defence... I have no defence.'"),
        ("I'll be honest, I did not think this through.", "He realized mid-sentence his plan had a hole in it and admitted, 'I'll be honest, I did not think this through.'"),
     ]),
    ("Deflecting a compliment warmly",
     "Someone just praised your work and you want to accept it graciously without sounding falsely modest or boastful.",
     "used to accept a compliment gracefully with a light joke, instead of either denying it or sounding boastful",
     [
        ("Thanks — even a broken clock is right twice a day.", "When her colleague praised the forecast she'd nailed, she smiled, 'Thanks — even a broken clock is right twice a day.'"),
        ("Thanks! Don't worry, normal service will resume shortly.", "After a rare flawless presentation, he laughed, 'Thanks! Don't worry, normal service will resume shortly.'"),
        ("I'll take it. Don't look too closely.", "Praised for the tidy report, she grinned, 'I'll take it. Don't look too closely.'"),
        ("Thanks — the team did the heavy lifting, I just showed up.", "When the client praised the launch, he said, 'Thanks — the team did the heavy lifting, I just showed up.'"),
     ]),
    ("Teasing someone who's late",
     "A close colleague or friend finally walks in after everyone else has arrived, and you want to tease them warmly about it.",
     "used to affectionately tease someone close for arriving late, once they've clearly teased you before too",
     [
        ("Ah, look who decided to join us.", "As he slipped into his seat ten minutes late, she grinned, 'Ah, look who decided to join us.'"),
        ("We saved you a seat. It's in the corridor.", "When she rushed in last, he deadpanned, 'We saved you a seat. It's in the corridor.'"),
     ]),
    ("Teasing someone who's boasting",
     "A close colleague is clearly pleased with themselves about something and you want to tease them gently for it, warmly, not cruelly.",
     "used to gently tease someone close who's visibly pleased with themselves, to keep the mood light rather than to put them down",
     [
        ("Steady on.", "He started listing his wins for the week and she laughed, 'Steady on.'"),
        ("Don't let it go to your head.", "After his idea got praised in the all-hands, she smiled, 'Don't let it go to your head.'"),
        ("Alright, Einstein.", "He explained the obvious a bit too proudly and his friend said, 'Alright, Einstein.'"),
     ]),
    ("Teasing about a mistake, affectionately",
     "A close colleague just made a small mistake and you want to rib them about it lightly, in a way that reads as affectionate, not judgmental.",
     "used to rib someone close about a small mistake in a way that reads as affectionate, not judgmental",
     [
        ("I'll allow it.", "He mislabeled the file again and she sighed with a smile, 'I'll allow it.'"),
        ("I won't hold it against you.", "After he mixed up the client names, she laughed, 'I won't hold it against you.'"),
        ("Noted. Filed. Never forgotten.", "He apologized for the typo and she said, 'Noted. Filed. Never forgotten.'"),
     ]),
    ("Teasing a bad idea, fondly",
     "A close colleague just floated an idea that's clearly a bit much, and you want to tease them about it without shutting it down.",
     "used to fondly tease a bold or slightly ridiculous idea, without shutting it down outright",
     [
        ("Bold.", "He proposed launching without any testing and she just said, 'Bold.'"),
        ("That's certainly a choice.", "He suggested presenting in a costume and she smirked, 'That's certainly a choice.'"),
        ("Love the confidence.", "He said he'd wing the whole presentation and she laughed, 'Love the confidence.'"),
     ]),
    ("Teasing someone who won't stop talking",
     "A close colleague or friend has been going on for a while, and you want to gently prod them to wrap up without shutting them down.",
     "used to gently prod someone close to wrap up when they've been talking for a while, without shutting them down harshly",
     [
        ("Are you nearly done? I've aged.", "He was ten minutes into a story with no end in sight, and she grinned, 'Are you nearly done? I've aged.'"),
        ("Feel free to stop any time.", "As his explanation ran long, his colleague said with a smile, 'Feel free to stop any time.'"),
     ]),
    ("Accepting a tease gracefully",
     "Someone just teased you and you want to take it well, without either getting defensive or over-apologizing.",
     "used to accept being teased gracefully, without getting defensive or over-apologizing",
     [
        ("Fair.", "She got teased for showing up late and just said, 'Fair.'"),
        ("Fair enough.", "When his colleague pointed out the obvious mistake, he laughed, 'Fair enough.'"),
        ("You're not wrong.", "Teased about his messy desk, he shrugged, 'You're not wrong.'"),
        ("I walked into that one.", "After setting up the joke against himself perfectly, he laughed, 'I walked into that one.'"),
        ("Late? I'm practically early — by tomorrow's standards.", "Teased for being late again, she grinned, 'Late? I'm practically early — by tomorrow's standards.'"),
     ]),
    ("Firing back lightly when teased",
     "Someone just teased you and, rather than just accepting it, you want to lightly bat it back.",
     "used to lightly return a tease rather than simply accepting it, keeping the exchange playful",
     [
        ("Alright, alright.", "After a round of teasing about his typo, he laughed, 'Alright, alright.'"),
        ("Says the man who...", "Teased about being late, she shot back, 'Says the man who was late to his own wedding.'"),
        ("Coming from you, that's rich.", "When he teased her about being disorganized, she smiled, 'Coming from you, that's rich.'"),
     ]),
    ("Ending a teasing exchange",
     "A round of playful teasing has gone on for a bit and you want to land it gracefully — either winding down naturally or correcting course if it went a step too far.",
     "used to land a teasing exchange gracefully, either winding it down naturally or correcting course if it went a step too far",
     [
        ("Right, I'll leave you alone now.", "After a few rounds of ribbing, she smiled, 'Right, I'll leave you alone now.'"),
        ("Okay, I'm done.", "He raised his hands after the third tease and laughed, 'Okay, I'm done.'"),
        ("Sorry — too far, that was on me.", "He noticed his joke had actually landed badly and said immediately, 'Sorry — too far, that was on me.'"),
     ]),
    ("Dry sarcasm about a bad situation",
     "Something has just gone wrong — a plan fell through, a meeting dragged on, a system broke — and you want a dry, sarcastic remark about the situation itself, not about a person.",
     "used as a dry, sarcastic remark about a bad situation itself (never about a person), always clearly signalled as sarcasm",
     [
        ("Well, that's just perfect.", "The server crashed five minutes before the demo and she muttered, 'Well, that's just perfect.'"),
        ("This is fine.", "As three things broke at once, he said flatly, 'This is fine,' and kept working."),
        ("Love that for me.", "Her flight got delayed again and she sighed, 'Love that for me.'"),
        ("Sure, why not.", "Another last-minute change landed on his desk and he said, 'Sure, why not.'"),
        ("What could possibly go wrong?", "They agreed to skip testing before launch and she said, 'What could possibly go wrong?'"),
        ("Famous last words.", "He said the deployment would be quick and easy, and she muttered, 'Famous last words.'"),
        ("That went well.", "The pitch ended in awkward silence and he said, 'That went well,' walking out."),
        ("Couldn't have gone better, really.", "The client call dropped twice mid-presentation and she said, 'Couldn't have gone better, really.'"),
        ("Oh good, another meeting about the meeting.", "The invite for a pre-meeting sync landed in his inbox and he groaned, 'Oh good, another meeting about the meeting.'"),
        ("I mean, technically you're not wrong.", "He pointed out a painfully obvious flaw in the plan and she said, 'I mean, technically you're not wrong.'"),
        ("Greeeeat.", "Hearing the deadline had moved up again, he said, 'Greeeeat,' drawing the word out flat."),
        ("Oh, only three hours late. Practically punctual.", "The delivery finally showed up and she said, 'Oh, only three hours late. Practically punctual.'"),
     ]),
    ("Checking whether someone was being sarcastic",
     "You're not sure if someone's over-the-top praise was genuine or sarcastic, and want a safe way to check or react either way.",
     "used to check whether someone was being sarcastic, or to react safely in a way that works whether they were or weren't",
     [
        ("Are you being sarcastic?", "His tone was oddly flat after the compliment, so she just asked, 'Are you being sarcastic?'"),
        ("Ha.", "Unsure if the remark was genuine or not, he just said, 'Ha,' and moved on."),
     ]),
    ("Playful register: mock-seriousness and exaggeration",
     "You want to talk about something completely trivial as if it were a matter of real importance, to keep the mood light.",
     "used to talk about something trivial in a mock-serious or playfully exaggerated way, to keep the mood light",
     [
        ("I have thoughts about this biscuit.", "He picked up the last biscuit from the tray and announced, 'I have thoughts about this biscuit.'"),
        ("This is a matter of national importance.", "The team debated where to order lunch from and she declared, 'This is a matter of national importance.'"),
        ("I've been waiting for this coffee since roughly the Ice Age.", "The barista finally called her name and she said, 'I've been waiting for this coffee since roughly the Ice Age.'"),
        ("My laptop has decided today is not the day.", "His screen froze for the third time and he sighed, 'My laptop has decided today is not the day.'"),
        ("So I open the file. The file laughs at me.", "She described the broken spreadsheet: 'So I open the file. The file laughs at me.'"),
     ]),
    ("Playful vocabulary for light chaos or hassle",
     "You want a fun, light-touch word for a bit of minor chaos or hassle instead of a flat, formal description.",
     "used as a light, playful word for minor chaos or hassle, instead of a flat formal description",
     [
        ("shenanigans", "He glanced at the tangled cables under the desk and said, 'What shenanigans happened here?'"),
        ("faff", "She sighed at the approval process and said, 'What a faff just to book a room.'"),
        ("kerfuffle", "There was a whole kerfuffle over who'd booked the meeting room twice."),
        ("a bit of a palaver", "Getting the visa sorted turned into a bit of a palaver."),
     ]),
    ("Naming an awkward moment out loud",
     "A silence has gone on too long, or something confusing just happened, and you want to name the awkwardness directly instead of pretending it isn't there.",
     "used to name an awkward moment out loud instead of pretending it isn't happening, which usually breaks the tension",
     [
        ("Well, this is awkward.", "The call went silent for ten seconds and she laughed, 'Well, this is awkward.'"),
        ("That was a very long silence.", "After the question hung unanswered for a while, he said, 'That was a very long silence.'"),
        ("I feel like we're all pretending we understood that.", "Nobody responded to the technical explanation, so she admitted, 'I feel like we're all pretending we understood that.'"),
        ("Someone has to say it, so: what are we actually doing here?", "After twenty minutes of vague discussion, he finally said, 'Someone has to say it, so: what are we actually doing here?'"),
        ("I'll be the one to ask the obvious question.", "Everyone looked confused but silent, so she said, 'I'll be the one to ask the obvious question.'"),
        ("The classic Zoom standoff. I'll go.", "Two people started talking at once on the call and he laughed, 'The classic Zoom standoff. I'll go.'"),
     ]),
    ("Warmth: giving credit and showing genuine interest",
     "You want to build warmth with someone by giving them visible credit or by showing real interest in something personal to them, not just being polite.",
     "used to build warmth by giving someone visible credit or showing genuine interest in something personal to them",
     [
        ("That was [name]'s idea — credit where it's due.", "When the plan succeeded, she told the group, 'That was Diego's idea — credit where it's due.'"),
        ("[Name] knows this better than anyone.", "He introduced his colleague to the client: 'Sara knows this better than anyone.'"),
        ("What made you go into this line of work?", "Over coffee, she asked the new hire, 'What made you go into this line of work?'"),
        ("How did the move go?", "He remembered she'd been relocating and asked, 'How did the move go?'"),
        ("Did your daughter get the place?", "She recalled his daughter's university application and asked, 'Did your daughter get the place?'"),
        ("Thanks for making time — I know your week is brutal.", "Before the call, he said, 'Thanks for making time — I know your week is brutal.'"),
     ]),
    ("Showing measured vulnerability",
     "You want to admit you found something difficult, confusing, or nerve-wracking, in a way that builds warmth without oversharing.",
     "used to admit something was difficult, confusing, or nerve-wracking, in a measured way that builds warmth without oversharing",
     [
        ("I'll be honest, I found that confusing too.", "After the dense explanation, she said, 'I'll be honest, I found that confusing too.'"),
        ("I had to look that up before this meeting.", "He admitted, 'I had to look that up before this meeting,' when asked about the term."),
        ("I'm nervous about this one — it matters to me.", "Before the pitch, she told her teammate, 'I'm nervous about this one — it matters to me.'"),
        ("I got that completely wrong last time, so bear with me.", "Starting the retry, he said, 'I got that completely wrong last time, so bear with me.'"),
     ]),
    ("Recovering when a joke falls flat",
     "You just told a joke and it landed with silence, and you want a quick, light way to move past it instead of over-explaining.",
     "used to recover quickly and lightly when a joke lands with silence, instead of over-explaining or apologizing for it",
     [
        ("That was funnier in my head.", "The joke landed with silence and he laughed at himself, 'That was funnier in my head.'"),
        ("Tough crowd.", "Nobody reacted to her joke, so she smiled, 'Tough crowd.'"),
        ("I'll see myself out.", "The pun fell completely flat and he said, 'I'll see myself out.'"),
        ("Right, moving on.", "She let the silence sit for a second, then said, 'Right, moving on,' and continued."),
        ("Wow. Nothing. Noted.", "The room stayed silent after his joke and he said, 'Wow. Nothing. Noted.'"),
        ("I'll stick to the day job.", "Her joke got a polite half-smile at best, and she said, 'I'll stick to the day job.'"),
     ]),
    ("Repairing a joke that went too far",
     "A joke you made landed badly and actually hurt someone, and you want to repair it properly instead of brushing it off.",
     "used to repair a joke that actually landed badly and hurt someone, rather than brushing it off or over-explaining",
     [
        ("Sorry — that was too far.", "He noticed her face fall and said immediately, 'Sorry — that was too far.'"),
        ("That was out of order, I apologise.", "Realizing the joke had crossed a line, she said, 'That was out of order, I apologise.'"),
        ("I've been thinking about what I said — I got that wrong. Sorry.", "The next day, he came back to her and said, 'I've been thinking about what I said — I got that wrong. Sorry.'"),
        ("I don't think it is — and that's on me.", "When he said 'it's fine' but clearly wasn't, she replied, 'I don't think it is — and that's on me.'"),
     ]),
    ("Admitting you didn't get the joke",
     "Everyone else just laughed at something and you have no idea why, and you want to admit it without killing the mood.",
     "used to admit you didn't understand a joke, without killing the mood or making it awkward",
     [
        ("Okay, I'm missing something — explain it to me.", "Everyone laughed except her, so she said, 'Okay, I'm missing something — explain it to me.'"),
        ("That's one for the locals. What am I missing?", "He didn't get the local reference and smiled, 'That's one for the locals. What am I missing?'"),
        ("I'm going to laugh, but I want you to know I have no idea why.", "She joined in the laughter and admitted, 'I'm going to laugh, but I want you to know I have no idea why.'"),
        ("Is that a pun? I refuse to reward that.", "He groaned at the wordplay and said, 'Is that a pun? I refuse to reward that.'"),
     ]),
]

if __name__ == "__main__":
    generate_topic(
        out_path=OUT_PATH,
        exam_id="humour-warmth",
        title="Chunk Atlas — Confidence & Humour: Humour & Warmth",
        tier_id=TIER_ID,
        tier_name=TIER_NAME,
        groups_def=groups_def,
    )
