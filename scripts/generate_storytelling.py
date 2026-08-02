import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from lib import generate_topic

OUT_PATH = os.path.join(SCRIPT_DIR, "..", "data", "storytelling.json")

# Phrase content below is copied by hand from the "Conversational
# Storytelling" topic (tier "fluency" / F7) in the source content set —
# sections F7.1-F7.6. F7.5 and F7.6 are supplementary "kho" (repository)
# lists that mostly repeat F7.1-F7.4 verbatim; only their NEW, non-duplicate
# phrasings were folded into the matching functional group below. F7.3 and
# F7.4 are each split into finer sub-groups since they bundle distinct
# functions (checking-in vs. building suspense; acknowledging vs. sharing
# your own story), mirroring how generate_core_patterns.py split H14.
TIER_ID = "fluency"
TIER_NAME = "Real-Time Fluency"

groups_def = [
    ("Asking for the floor to tell a story",
     "You have a story you want to tell and need to signal you're about to take a longer turn, not just make small talk.",
     "used to signal you're about to take a longer turn and tell a story",
     [
        ("Did I tell you about...?", "Did I tell you about the time the client showed up to the demo an hour early?"),
        ("You'll never guess what happened.", "You'll never guess what happened at the airport on my way back."),
        ("The funniest thing happened yesterday.", "The funniest thing happened yesterday — our internet went down mid-presentation."),
        ("Something weird happened this morning.", "Something weird happened this morning, right before the standup."),
        ("Oh, this is a good one.", "Oh, this is a good one — you're going to love how this ends."),
        ("Right, so you know [X]?", "Right, so you know our old manager? Well, you'll never guess who I ran into."),
        ("Can I tell you something ridiculous?", "Can I tell you something ridiculous that happened on my commute this morning?"),
        ("So, funny story...", "So, funny story — I actually locked myself out of the office this morning."),
        ("Okay so picture this...", "Okay so picture this: three of us, one broken elevator, and a client waiting upstairs."),
        ("Right, so this happened yesterday...", "Right, so this happened yesterday, and I still can't quite believe it."),
     ]),
    ("Setting the scene",
     "You're starting to tell a story and need to establish the time, place, or situation before the action begins.",
     "used to establish the time, place, or situation before a story's action begins",
     [
        ("So basically...", "So basically, I was the only one left in the office when the fire alarm went off."),
        ("So I was at...", "So I was at the client's office, waiting for the meeting to start."),
        ("This was back when...", "This was back when we still used the old ticketing system."),
        ("So I'm sat there...", "So I'm sat there, laptop open, completely unaware of what's coming."),
        ("We're halfway through when...", "We're halfway through when the whole screen just froze."),
        ("It's about 6am and...", "It's about 6am and I'm already on a call with the US team."),
        ("Now, you have to picture this.", "Now, you have to picture this — the whole room went dead silent."),
        ("Bear in mind, this is at 6am.", "Bear in mind, this is at 6am, so nobody's brain was really working yet."),
     ]),
    ("Setting up an expectation before the twist",
     "You're telling a story and want to state what you expected to happen, right before revealing it went differently.",
     "used to state what you expected, right before revealing it went differently",
     [
        ("I thought it would be fine.", "I thought it would be fine — it was just meant to be a routine deployment."),
        ("I assumed...", "I assumed the meeting had been cancelled, since nobody joined the call."),
     ]),
    ("Introducing the twist",
     "You're telling a story and have reached the point where everything suddenly changed.",
     "used to mark the point in a story where everything suddenly changed",
     [
        ("And then...", "And then, right as I hit send, I realized it went to the wrong client."),
        ("But here's the thing...", "But here's the thing — the bug had been sitting there for six months."),
        ("Turns out...", "Turns out, the whole outage was caused by one missing semicolon."),
        ("And then, out of nowhere...", "And then, out of nowhere, the CEO joined the call."),
        ("Next thing I know...", "Next thing I know, my laptop just shut itself off mid-demo."),
        ("Long story short...", "Long story short, we ended up rebuilding the whole thing overnight."),
     ]),
    ("Narrating the climax vividly",
     "You've reached the most dramatic moment of your story and want to narrate it as if it's happening right now.",
     "used to narrate a story's most dramatic moment vividly, often in present tense",
     [
        ("So there I am, [doing something]...", "So there I am, sharing my screen, and I've got the wrong tab open."),
        ("So I walk in, and he's just standing there.", "So I walk in, and he's just standing there, staring at a blank whiteboard."),
        ("And he just...", "And he just looks at me and says nothing for a full ten seconds."),
        ("She literally...", "She literally froze mid-sentence when she saw the numbers."),
        ("It completely...", "It completely threw the whole room off — nobody knew what to say."),
     ]),
    ("Ending the story with a punchline",
     "You're finishing a story and want a punchy closing line instead of just trailing off.",
     "used as a punchy closing line to finish a story instead of trailing off",
     [
        ("...and that was that.", "We rescheduled the whole meeting — and that was that."),
        ("...so yeah, lesson learned.", "I triple-check my recipients now — so yeah, lesson learned."),
        ("...I've never lived it down.", "They still bring it up in every retro — I've never lived it down."),
        ("...never again.", "We tried a live demo with no backup plan — never again."),
        ("...still not over it.", "The whole team saw it happen live — I'm still not over it."),
        ("...would not recommend.", "Presenting a demo with 2% battery left — would not recommend."),
        ("...ten out of ten, no notes.", "The client loved the fix so much — ten out of ten, no notes."),
        ("...anyway, I live here now.", "I basically moved my whole desk setup into that meeting room — anyway, I live here now."),
        ("...and the rest is history.", "We shipped the fix that same night, and the rest is history."),
        ("...never spoken of again.", "That deployment is never spoken of again on this team."),
        ("...and that's why I don't do that anymore.", "I skipped the staging test just once — and that's why I don't do that anymore."),
     ]),
    ("Checking the listener is following",
     "You're partway through a story or explanation and want to make sure the listener is still following before continuing.",
     "used to check the listener is still following before you continue",
     [
        ("Are you with me?", "That's the third handoff in the process — are you with me so far?"),
        ("Does that make sense so far?", "We rerouted the whole request through the new service — does that make sense so far?"),
     ]),
    ("Pulling the listener in / building suspense",
     "You're telling a story and want to build suspense and pull the listener further in before the reveal.",
     "used to build suspense and pull the listener in before a reveal",
     [
        ("You know what he said?", "You know what he said when I told him the deadline had moved up?"),
        ("Guess what she did.", "Guess what she did when she found out the ticket got reassigned."),
        ("Guess what happened next.", "Guess what happened next — the client actually thanked us for the delay."),
        ("And it gets worse.", "And it gets worse — the backup server was down too."),
        ("That's not even the best bit.", "That's not even the best bit — wait until you hear what happened after."),
        ("Wait, there's more.", "Wait, there's more — turns out the fix broke something else entirely."),
     ]),
    ("Emphasizing it's true",
     "You're telling a story so surprising that you need to emphasize it's genuinely true.",
     "used to emphasize that a surprising story is genuinely true",
     [
        ("I kid you not.", "The meeting ran for three hours — I kid you not."),
        ("Honest to God.", "He fell asleep on camera, honest to God."),
        ("Swear down.", "She predicted the exact bug before we even ran the tests, swear down."),
        ("No word of a lie.", "The whole system crashed the second I said 'it's stable' — no word of a lie."),
        ("Hand on heart.", "Hand on heart, I didn't touch that config file."),
        ("I swear.", "I swear, the demo worked perfectly five minutes before we went live."),
     ]),
    ("Quoting what people said",
     "You're retelling a conversation and want to quote what someone actually said, to make the story vivid.",
     "used to quote what someone actually said, to make a story vivid",
     [
        ("And she goes, \"...\"", "And she goes, \"wait, this was supposed to go live yesterday?\""),
        ("And I'm like, \"...\"", "And I'm like, \"please tell me you're joking.\""),
        ("He turns round and says...", "He turns round and says, \"I thought you were handling that.\""),
     ]),
    ("Acknowledging their story before responding",
     "A colleague just finished telling you a story and you need to react before saying anything about yourself.",
     "used to react to someone's story before responding with anything of your own",
     [
        ("That's brilliant.", "That's brilliant — I can't believe he actually said yes."),
        ("Oh that's awful.", "Oh that's awful, no wonder you were exhausted after that call."),
     ]),
    ("Sharing your own related story and handing the turn back",
     "Someone just told you a story and you want to share a similar one of your own, then hand the conversation back to them.",
     "used to share a related story of your own, then hand the conversation back",
     [
        ("Something similar happened to me —", "Something similar happened to me — same client, different disaster."),
        ("That's just like when I...", "That's just like when I locked myself out of the deployment pipeline."),
        ("...anyway, sorry — go on, what happened next?", "...anyway, sorry — go on, what happened next with the client?"),
     ]),
]

if __name__ == "__main__":
    generate_topic(
        out_path=OUT_PATH,
        exam_id="storytelling",
        title="Chunk Atlas — Real-Time Fluency: Conversational Storytelling",
        tier_id=TIER_ID,
        tier_name=TIER_NAME,
        groups_def=groups_def,
    )
