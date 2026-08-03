import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from lib import generate_topic

OUT_PATH = os.path.join(SCRIPT_DIR, "..", "data", "gesture-gaze-presence.json")

# Phrase content below is copied by hand from the "Gesture, Gaze & Presence"
# topic (tier "presence" / nav tab "Voice & Presence") in final_topics.json,
# sections P5.1-P5.6.
#
# P5.1 ("Cử chỉ giúp CHÍNH CHỊ nói trôi hơn") is skipped entirely: every "i"
# item there is a pure behavioural instruction ("if you're stuck, gesture",
# "don't cross your arms") with nothing actually sayable in it.
# P5.3 ("Ánh mắt (gaze) — điều tiết lượt nói") is skipped entirely for the
# same reason: all items describe what gaze behaviour signals, not
# something a speaker would say out loud.
# P5.2 ("Bốn loại cử chỉ") mostly labels gesture *types* (beat/deictic/
# iconic/metaphoric) with theory, not chunks — only the two embedded quoted
# examples ("This option here, that one there." / "It went up sharply.")
# are genuinely sayable, so they were pulled out and merged with P5.5
# (which is the same underlying function: language that naturally pulls
# your hands into the explanation) into one group. The metaphoric example
# in P5.2 ("On one hand... on the other...") duplicates P5.5's fuller
# "On the one hand... on the other hand...", so only the P5.5 version was
# kept.
# P5.4 ("Video call — sân khấu khác") is mostly stage direction (look at
# the camera, frame your chest, nod more) with two exceptions where it
# gives actual quoted lines to compensate for lost signal ("I'm nodding
# along" / "That got a laugh from me.") — those two were extracted and
# merged with P5.6's own lost-signal line into their own group, separate
# from P5.6's purely technical/logistics lines (screen share, mute, chat,
# turn-taking), since those are a clearly distinct function.
TIER_ID = "presence"
TIER_NAME = "Voice & Presence"

groups_def = [
    ("Spatial & structural gesture language",
     "You're explaining something and want language that naturally pulls your hands into the explanation — pointing, showing movement, or laying out structure in space.",
     "used to accompany an explanation with natural hand gestures — pointing, showing movement, or organizing ideas in space",
     [
        ("This option here, that one there.", "This option here, that one there — pick whichever works better for your team."),
        ("It went up sharply.", "Just look at this chart — it went up sharply the moment we changed the pricing."),
        ("On the one hand... on the other hand...", "On the one hand, the new tool is faster; on the other hand, it's a lot more expensive."),
        ("It went from here... to here.", "Our headcount went from here... to here in just six months."),
        ("There are three parts: this, this, and this.", "There are three parts to the proposal: this, this, and this."),
        ("It's about this big.", "The prototype is about this big — small enough to fit in a bag."),
        ("Roughly this far apart.", "The two racks need to sit roughly this far apart for the cabling to reach."),
        ("We're here, and we need to get here.", "On the roadmap, we're here, and we need to get here by the end of Q3."),
        ("Big picture... versus the detail.", "Let's zoom out — big picture... versus the detail we've been stuck on all morning."),
        ("Let me draw this for you.", "It's easier to show than explain — let me draw this for you."),
     ]),
    ("Video call logistics & connection checks",
     "You're on a video call and need to sort out a technical hiccup — screen sharing, audio, or who talks next.",
     "used to handle technical logistics on a video call — screen sharing, audio issues, or handing off the floor",
     [
        ("Can everyone see my screen?", "Can everyone see my screen? I want to make sure the slides are showing."),
        ("Am I coming through okay?", "Am I coming through okay? My connection's been patchy today."),
        ("I'll stop sharing.", "I'll stop sharing so we can all see each other again."),
        ("Let me put that on screen.", "Let me put that on screen so everyone can follow along."),
        ("Sorry, you're on mute.", "Sorry, you're on mute — we couldn't hear the last bit."),
        ("I think we lost you there.", "I think we lost you there for a second, could you repeat that?"),
        ("I'll drop it in the chat.", "I'll drop it in the chat so you all have the link afterwards."),
        ("Have a look at the chat.", "Have a look at the chat, I've pasted the doc link there."),
        ("Go ahead — no, you go.", "Go ahead — no, you go, we started talking over each other."),
        ("Sorry, we talked over each other.", "Sorry, we talked over each other there — could you go first?"),
     ]),
    ("Compensating for lost non-verbal signals on video",
     "You're on a video call and want to put into words a reaction that would normally just show on your face.",
     "used on a video call to say out loud a reaction that would normally just show on your face, since video weakens those signals",
     [
        ("I'm nodding along, for what it's worth.", "I'm nodding along, for what it's worth, since you can barely see me in this tiny window."),
        ("Just so you know I'm still here — that all makes sense.", "Just so you know I'm still here — that all makes sense, keep going."),
        ("That got a laugh from me.", "That got a laugh from me, even though my camera's off right now."),
     ]),
]

if __name__ == "__main__":
    generate_topic(
        out_path=OUT_PATH,
        exam_id="gesture-gaze-presence",
        title="Chunk Atlas — Voice & Presence: Gesture, Gaze & Presence",
        tier_id=TIER_ID,
        tier_name=TIER_NAME,
        groups_def=groups_def,
    )
