import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from lib import generate_topic

OUT_PATH = os.path.join(SCRIPT_DIR, "..", "data", "words-fail.json")

# Phrase content below is copied by hand from the "When Words Fail:
# Communication Strategies" topic (tier "fluency" / F2) in the source
# content set. A few near-duplicate phrasings that recur across F2.1-F2.5
# (the source repeats itself in its "extra bank" sections) were folded
# together rather than duplicated. F2.5 (the extra bank) bundles several
# distinct functions and is split into three sub-groups accordingly.
TIER_ID = "fluency"
TIER_NAME = "Real-Time Fluency"

groups_def = [
    ("Circumlocution — Describing What You Mean",
     "You can't remember the English word for something, so you need to describe it instead.",
     "used to describe or work around a word you can't remember, instead of freezing",
     [
        ("It's the thing you use to...", "It's the thing you use to... staple papers together — I can't remember the word."),
        ("It's a kind of...", "It's a kind of... device that boosts the wifi signal, I think it's called a repeater."),
        ("It's like a... but...", "It's like a... spreadsheet, but simpler — more like a checklist."),
        ("It's what happens when...", "It's what happens when... you keep putting off a task you know you should do."),
        ("It's the word for when someone...", "It's the word for when someone... suddenly changes their mind at the last minute."),
        ("I don't know the exact word, but it's basically...", "I don't know the exact word, but it's basically a formal complaint you file with HR."),
        ("You know when...? That.", "You know when you forward an email to the wrong person? That."),
     ]),
    ("Approximation & All-Purpose Words",
     "You can't think of the precise word, so you reach for a rough substitute or a generic filler word instead of freezing.",
     "used as a generic, rough substitute for a precise word you can't recall",
     [
        ("thing", "Can you pass me that thing — the one that holds the papers together?"),
        ("stuff", "We still need to sort out the stuff for the client presentation."),
        ("a kind of", "It's a kind of software that tracks everyone's time off."),
        ("sort of", "It's sort of a middle-ground solution — not perfect, but it works."),
        ("the thing that...", "Hand me the thing that connects the laptop to the projector."),
        ("the stuff we use for...", "Where's the stuff we use for printing the badges?"),
        ("one of those...", "It's one of those... forms you fill out before traveling for work."),
        ("something along those lines", "We're looking for a fix, or something along those lines."),
        ("or whatever the technical term is", "We need to update the firmware, or whatever the technical term is."),
     ]),
    ("Appealing for Help Professionally",
     "You've hit a word you don't know and want to ask the other person for it, without losing your confidence.",
     "used to ask the other person for a missing word without sounding lost or embarrassed",
     [
        ("What's the word I'm looking for?", "What's the word I'm looking for... when you delay something on purpose?"),
        ("What do you call it again?", "What do you call it again — the thing you swipe to unlock the door?"),
        ("How do you say it in English?", "How do you say it in English? We just call it 'nhậu' in Vietnamese."),
        ("Is there a word for that?", "Is there a word for that — when a meeting could've been an email?"),
        ("Help me out here — the thing that...", "Help me out here — the thing that... measures how fast the page loads?"),
        ("You know what I mean?", "It's not exactly a bug, more like a design flaw — you know what I mean?"),
        ("You know the one?", "It's that tool everyone uses for video calls — you know the one?"),
        ("Right — exactly.", "\"Deprecated?\" \"Right — exactly, that's the word I was looking for.\""),
     ]),
    ("Never Abandon the Message",
     "You're mid-sentence, the sentence is falling apart, and you need to land it somehow instead of trailing off.",
     "used to land a collapsing sentence and keep going, instead of trailing off into silence",
     [
        ("...anyway, the point is...", "It's not just about the delay, the client, the — anyway, the point is, we need more time."),
        ("...but you get the idea.", "It's kind of like a stripped-down version of the old system, but you get the idea."),
        ("...I'm not explaining this well. Let me start again.", "...I'm not explaining this well. Let me start again from the beginning."),
        ("...what I'm trying to say is...", "...what I'm trying to say is, we're not ready to launch yet."),
     ]),
    ("More Circumlocution Frames",
     "You need another way to describe something you can't name, without pausing too long.",
     "used as another framing device to describe something you can't name",
     [
        ("It's the thing that...", "It's the thing that... reminds you when a meeting's about to start."),
        ("It's like a... but for...", "It's like a... calendar, but for tracking who's out of the office."),
        ("It's what you call it when...", "It's what you call it when... two systems can't read each other's data."),
        ("There's a word for it — I can't think of it.", "There's a word for it — I can't think of it, but it's basically job-hopping."),
        ("You use it to...", "You use it to... compress files before sending them."),
        ("It's for when you need to...", "It's for when you need to... restore a file you accidentally deleted."),
        ("It's similar to...", "It's similar to... a checklist, but it's automated."),
        ("Think... but smaller.", "Think a full audit... but smaller — more like a quick sanity check."),
     ]),
    ("More Ways to Ask for Help & Move On",
     "You're stuck on a word mid-conversation and want a quick way to ask for it and keep the conversation moving.",
     "used to quickly ask for a missing word and keep the conversation moving without losing the floor",
     [
        ("What's the word?", "What's the word... for someone who always finds a reason to complain?"),
        ("Help me out.", "Help me out — what do you call the person who runs the meeting?"),
        ("What do you call it?", "What do you call it when a project just quietly dies without anyone canceling it?"),
        ("I'll come back to the word. Anyway —...", "I'll come back to the word. Anyway — the main issue is the timeline, not the name."),
        ("Let me say it in simpler terms.", "Let me say it in simpler terms: we're spending more than we make."),
     ]),
    ("Informal All-Purpose Words (UK/Casual)",
     "You're in a casual conversation and can't recall the exact word, so you reach for a light, informal placeholder.",
     "used casually, especially in British English, as a placeholder for a word you can't recall",
     [
        ("whatsit", "Can you grab the whatsit — the thing that holds the cables together?"),
        ("doodah", "Where's the little doodah that connects to the projector?"),
        ("thingy", "Pass me that thingy on the desk, the one with the buttons."),
     ]),
]

if __name__ == "__main__":
    generate_topic(
        out_path=OUT_PATH,
        exam_id="words-fail",
        title="Chunk Atlas — Real-Time Fluency: When Words Fail: Communication Strategies",
        tier_id=TIER_ID,
        tier_name=TIER_NAME,
        groups_def=groups_def,
    )
