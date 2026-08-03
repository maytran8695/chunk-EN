import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from lib import generate_topic

OUT_PATH = os.path.join(SCRIPT_DIR, "..", "data", "voice-paralanguage.json")

# Phrase content copied by hand from the "Voice & Paralanguage" topic
# (tier "presence" / nav tab "Voice & Presence") — sections P4.5, V4.6 only.
# P4.1 (pitch range), P4.2 (vocal authority), P4.3 (pace/pausing) and P4.4
# (voice-quality markers like uptalk/vocal fry/breathiness/smile voice) are
# skipped entirely: every item in those sections is Vietnamese meta-advice
# describing a vocal technique in the abstract, with no actual quotable
# English chunk attached ("t":"c" comparison blocks were also skipped per
# spec). P4.5 and V4.6 do contain real spoken chunks (things you actually
# say out loud to control pace/energy on stage), so those are used, split
# by function. Three exact-duplicate lines shared between P4.5 and V4.6
# ("Here's the key point.", "[pause] Right. [pause]", "Full stop.") are
# kept only once, in their P4.5 group, to avoid a phrase appearing as the
# correct answer for two unrelated questions.
TIER_ID = "presence"
TIER_NAME = "Voice & Presence"

groups_def = [
    ("Signaling a slow-down",
     "You're about to say something dense or important, and want to signal out loud that you're slowing your pace on purpose.",
     "used to announce that you're deliberately slowing down because what comes next matters",
     [
        ("Let me slow down here.",
         'Let me slow down here — this next part is where people usually get lost.'),
        ("This bit matters, so bear with me.",
         'This bit matters, so bear with me — I want to get the numbers exactly right.'),
     ]),
    ("Flagging the key point",
     "You want to explicitly flag that the sentence coming next is the one thing worth remembering.",
     "used to explicitly flag the single most important point right before saying it",
     [
        ("Here's the key point.",
         "Here's the key point: we're three weeks behind, not one."),
        ("If you remember one thing...",
         'If you remember one thing from this meeting, remember this number.'),
        ("This is the crux.",
         "This is the crux: the two systems don't talk to each other."),
     ]),
    ("Building in a pause",
     "You've just made an important point and want to create silence around it so it registers, instead of rushing to the next sentence.",
     "used to create a deliberate silence around an important point so it has time to register",
     [
        ("[pause] Right. [pause]",
         "We're cutting the feature. [pause] Right. [pause] Let's talk about what replaces it."),
        ("Let that sit for a second.",
         'We lost our biggest client this quarter. Let that sit for a second.'),
     ]),
    ("Signaling a speed-up",
     "You're about to cover something minor or background, and want to signal out loud that you'll move through it fast.",
     "used to announce that you'll move quickly through minor or background material",
     [
        ("I'll whip through this bit.",
         "I'll whip through this bit — it's just background on how we got here."),
        ("This is just context, I'll be quick.",
         "This is just context, I'll be quick, then we'll get to the decision."),
     ]),
    ("Shifting energy",
     "You want to signal a clear change in energy or direction as you move to a new part of the conversation.",
     "used to signal a clear shift in energy or direction when moving to a new topic",
     [
        ("Okay — different gear now.",
         "Okay — different gear now. Let's talk about budget."),
        ("Let's switch tack.",
         "Let's switch tack and look at this from the customer's side."),
     ]),
    ("Ending decisively",
     "You're closing a point or a request and want it to land as final, with no trailing hedge.",
     "used to close a point or request decisively, with no trailing hedge",
     [
        ("And that's it.",
         "We ship Friday. And that's it."),
        ("Full stop.",
         "We're not extending the deadline again. Full stop."),
        ("That's the ask.",
         "We need two more engineers by June. That's the ask."),
     ]),
    ("Opening a talk",
     "You're about to start a presentation or talk and want to open it crisply, signaling you're ready to begin.",
     "used to open a talk or presentation crisply, signaling readiness to begin",
     [
        ("Right. Let's begin.",
         'Right. Let\'s begin." she said, closing her laptop lid halfway and looking up.'),
        ("Thanks for coming.",
         'Thanks for coming, especially on such short notice.'),
        ("Let's get into it.",
         "No more preamble — let's get into it."),
     ]),
    ("Flagging importance (extra)",
     "You want to verbally flag, in the moment, that what you're about to say deserves the listener's full attention.",
     "used to verbally flag, in the moment, that the coming sentence deserves full attention",
     [
        ("This is the bit that matters.",
         "This is the bit that matters: the client hasn't actually signed yet."),
        ("Listen to this.",
         'Listen to this — the numbers completely contradict what we assumed.'),
     ]),
    ("Transitioning",
     "You've finished one part of what you're saying and want a short, brisk signal that you're moving to the next part.",
     "used as a short, brisk signal that you're moving on to the next part",
     [
        ("Moving on.",
         "Moving on. Let's look at next quarter's targets."),
        ("Different gear now.",
         'Different gear now — this next part is more technical.'),
        ("Next.",
         "Next. Let's talk about staffing."),
     ]),
    ("Closing decisively (extra)",
     "You're finishing your part of the conversation and want to close it firmly, marking clearly that you're done.",
     "used to close firmly, marking clearly that you're finished speaking",
     [
        ("And that's the ask.",
         "We need sign-off by Friday. And that's the ask."),
        ("That's it from me.",
         "That's it from me — happy to take questions."),
     ]),
    ("Checking the audience",
     "You want to pause and check whether your listener or audience is still following before you continue.",
     "used to pause and check whether the listener or audience is still following",
     [
        ("Still with me?",
         'Still with me? I know that was a lot of numbers.'),
        ("Any questions so far?",
         'Any questions so far, before I move to the next section?'),
     ]),
]

if __name__ == "__main__":
    generate_topic(
        out_path=OUT_PATH,
        exam_id="voice-paralanguage",
        title="Chunk Atlas — Voice & Presence: Voice & Paralanguage",
        tier_id=TIER_ID,
        tier_name=TIER_NAME,
        groups_def=groups_def,
    )
