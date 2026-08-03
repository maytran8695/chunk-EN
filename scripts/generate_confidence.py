import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from lib import generate_topic

OUT_PATH = os.path.join(SCRIPT_DIR, "..", "data", "confidence.json")

# Phrase content below is copied by hand from the "Confidence" topic
# (tier "growth" / nav tab "Confidence & Humour") in final_topics.json,
# sections C1.1-C8.4.
#
# This topic is overwhelmingly Vietnamese-language psychological/behavioural
# commentary (spotlight-effect research, safety-behaviour diagnostics,
# breathing mechanics, rumination loops, etc.) written FOR a Vietnamese
# reader ABOUT the technique, not actual English chunks to say or think.
# Of the 101 "i"-type items across 26 headers, only a small number are
# themselves genuine quotable English phrases; the rest ("Sự thật: người
# nghe chỉ thấy nét mặt...", the safety-behaviour list in C3.1, the
# breathing/body tips in C7.2/C7.3, the rumination-cutting steps in C8.1-
# C8.3, etc.) have nothing sayable in English and were dropped, mirroring
# how generate_emotional_attunement.py drops behavioural-cue description
# with "nothing sayable." Headers with zero surviving English phrases
# (C1.1, C2.1-C2.3, C3.1-C3.3, C4.1, C4.3, C5.1, C6.3-C6.4, C7.2-C7.3,
# C8.1-C8.4) are skipped entirely.
#
# C1.2 + C1.3 are merged: both are the same function (reassuring self-talk
# that counters the illusion that nervousness shows), each header only
# contributed a single usable English line on its own.
# C5.1's "c" comparison pair (host vs. guest framing) and C6's "c" pairs
# (the confident-phrasing-vs-hedge examples) are skipped per instructions
# (comparison blocks, not "i" items) even though some of that material
# would otherwise have been useful — only the two genuinely "i"-typed
# replacement lines in C6.1/C6.2 survive.
TIER_ID = "growth"
TIER_NAME = "Confidence & Humour"

groups_def = [
    ("Spotlight-effect reassurance",
     "You're seconds from walking into a meeting, certain everyone in the room will see exactly how nervous you are.",
     "used as calming self-talk right before a nerve-wracking moment, to counter the illusion that your anxiety is visible to everyone else",
     [
        ("Nobody is thinking about me as much as I am.", "Right before she opened the door, she reminded herself: nobody is thinking about me as much as I am."),
        ("Bear with me, this one matters to me.", "His voice started to shake, so he just said it out loud — bear with me, this one matters to me — and the tension dropped instantly."),
     ]),
    ("Reframing nerves as excitement",
     "Your heart is pounding and your hands are shaking right before you have to speak, and you want to use that energy instead of fighting it.",
     "used to relabel physical anxiety symptoms as excitement instead of trying to suppress them, since the two feel almost identical in the body",
     [
        ("I'm excited about this one.", "Instead of telling herself to calm down, she said out loud, I'm excited about this one, and let the adrenaline work for her."),
        ("This matters to me — that's why my body is doing this.", "He noticed his hands shaking and thought, this matters to me — that's why my body is doing this — instead of panicking about it."),
     ]),
    ("Reliable get-to-know-you questions",
     "You're in a conversation and want a dependable question ready so you never freeze up wondering what to ask next.",
     "used as a go-to question that reliably keeps a conversation moving, so you never have to think of something new on the spot",
     [
        ("What got you into this?", "She asked the new client, 'What got you into this?' and got a five-minute story that made the rest of the call easy."),
        ("What's the best thing about it?", "When the small talk stalled, he simply asked, 'What's the best thing about it?' and the conversation picked right back up."),
        ("What would you do differently?", "At the end of the debrief, she asked, 'What would you do differently?' and it opened up the most useful part of the chat."),
     ]),
    ("Automatic opening lines",
     "You're about to walk into a room, join a call, or sit down next to someone new, and you want an opener that comes out automatically so you're free to read the room instead of scrambling for words.",
     "used as a pre-loaded opening line for a specific situation, so the first words come out automatically instead of being improvised under pressure",
     [
        ("Hi — I don't think we've met. I'm [name].", "He walked up to the group and said, 'Hi — I don't think we've met. I'm Marco,' before he had time to overthink it."),
        ("Mind if I join you?", "She spotted a colleague sitting alone at lunch and just asked, 'Mind if I join you?'"),
        ("Is this seat taken?", "He gestured at the empty chair and asked, 'Is this seat taken?' instead of hovering awkwardly nearby."),
        ("How do you know [the organizer]?", "Stuck for an opener at the party, she asked, 'How do you know Priya?' and it carried the conversation for ten minutes."),
        ("Have you been to one of these before?", "As the room filled up, he turned to the person next to him and asked, 'Have you been to one of these before?'"),
        ("Morning — how's your week going?", "She opened the stand-up with a simple 'Morning — how's your week going?' before diving into the agenda."),
        ("Hi all — can you hear me okay?", "He unmuted and started the call with 'Hi all — can you hear me okay?' to buy himself a few seconds to settle in."),
     ]),
    ("Fallback lines when you're stuck for words",
     "The conversation has stalled and your mind has gone completely blank.",
     "used as a fallback line when you genuinely don't know what to say next, so the conversation never fully stalls",
     [
        ("You said [X] — tell me more about that.", "When the room went quiet, she picked up his earlier comment: 'You said the launch got delayed twice — tell me more about that.'"),
        ("I'm terrible at these things. What brings you here?", "Rather than freeze up, he admitted, 'I'm terrible at these things. What brings you here?' and it broke the ice instantly."),
        ("Lovely to meet you — I'm going to grab a drink.", "When she felt the conversation running dry, she smiled and said, 'Lovely to meet you — I'm going to grab a drink,' and exited gracefully."),
     ]),
    ("Confident replacements for apologetic hedges",
     "You're about to send a message or ask something, and your instinct is to open with a reflexive 'sorry' or a hedge that undersells you.",
     "used instead of a reflexive apology or hedge, to say the same thing without undercutting yourself",
     [
        ("Thanks for reading this through.", "Instead of 'Sorry for the long email,' she closed with, 'Thanks for reading this through.'"),
        ("What questions do you have?", "Instead of 'Does that make sense?' he ended his update with, 'What questions do you have?' — it assumed people were following, not confused."),
     ]),
]

if __name__ == "__main__":
    generate_topic(
        out_path=OUT_PATH,
        exam_id="confidence",
        title="Chunk Atlas — Confidence & Humour: Confidence",
        tier_id=TIER_ID,
        tier_name=TIER_NAME,
        groups_def=groups_def,
    )
