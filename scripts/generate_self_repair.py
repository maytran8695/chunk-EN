import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from lib import generate_topic

OUT_PATH = os.path.join(SCRIPT_DIR, "..", "data", "self-repair.json")

# Phrase content below is copied by hand from the "Self-Repair & Recovery"
# topic (tier "fluency" / F3) in the source content set. F3.2 ("Don't
# apologize for your English") is skipped entirely: it only contains
# comparison ("good vs. bad") blocks and prose notes, no standalone
# quotable chunks. F3.5 and F3.6 are the source's own "extra bank"
# sections; each is split into finer sub-groups, and phrasings that exactly
# duplicate an earlier section (e.g. "Sorry, I mean...", "What I should
# have said is...", "Is that the right word?") were folded rather than
# repeated.
TIER_ID = "fluency"
TIER_NAME = "Real-Time Fluency"

groups_def = [
    ("Fluent Self-Repair (Mid-Sentence)",
     "You just said the wrong word mid-sentence and need to correct it smoothly, without stopping to apologize.",
     "used to smoothly correct a slip mid-sentence, without stopping to apologize",
     [
        ("Sorry, I mean...", "We finished Monday — sorry, I mean Tuesday."),
        ("Or rather...", "The client agreed — or rather, they agreed in principle, not in writing."),
        ("That is...", "We need sign-off from legal — that is, from the compliance team specifically."),
        ("Let me rephrase that.", "Let me rephrase that — I meant the checkout page, not the whole site."),
        ("Let me say that better.", "Let me say that better: it's not broken, it's just slower than usual."),
        ("Actually, scratch that.", "We could ship Friday — actually, scratch that, QA needs the extra day."),
        ("Actually, that's not quite right.", "The bug started last week — actually, that's not quite right, it was two weeks ago."),
        ("...well, not exactly — more like...", "It's a bug — well, not exactly — more like a design flaw."),
        ("What I should have said is...", "What I should have said is that the delay is on our side, not the vendor's."),
     ]),
    ("Own-Accuracy Check",
     "You just used a word you're not fully sure is correct and want to check it in the moment.",
     "used to check a word you're unsure of right after saying it",
     [
        ("Is that the right word?", "We should deprecate the old endpoint — is that the right word?"),
        ("Am I using that correctly?", "I called it a 'blocker' — am I using that correctly?"),
        ("\"Deprecated\" — is that what you'd call it?", "We stopped supporting the old API — \"deprecated\" — is that what you'd call it?"),
        ("Correct me if that's the wrong term.", "I'll call it 'churn' — correct me if that's the wrong term."),
        ("I think that's the term — you'd know better.", "I think that's the term — you'd know better, you've been on this project longer."),
     ]),
    ("Restarting Without Losing Face",
     "Your explanation is getting tangled and you need to restart it cleanly, without an awkward apology.",
     "used to cleanly restart an explanation that's getting tangled, without an awkward apology",
     [
        ("Let me start over.", "Let me start over — I think I explained that in the wrong order."),
        ("Let me back up a second.", "Let me back up a second, because the context matters here."),
        ("Actually, let me give you the context first.", "Actually, let me give you the context first, then the numbers will make sense."),
        ("Hmm, I'm overcomplicating this. Simply put: ...", "Hmm, I'm overcomplicating this. Simply put: we're behind schedule."),
        ("Right — let me try that again, more clearly.", "Right — let me try that again, more clearly this time."),
     ]),
    ("More Instant Corrections — Restating",
     "You need to quickly restate something you just said, in a cleaner or more precise way.",
     "used to quickly restate what you just said in a cleaner or more precise way",
     [
        ("I meant to say...", "I said Q2 — I meant to say Q3."),
        ("Rather...", "It's not cancelled, rather, it's postponed."),
        ("Let me rephrase.", "Let me rephrase — I'm not saying it's your fault, just that it happened on your team."),
        ("Let me try that again.", "Let me try that again, because that came out confusing."),
        ("Let me be precise.", "Let me be precise: it's a 12% drop, not a 20% drop."),
        ("Correction: ...", "Correction: the deadline is next Friday, not this one."),
        ("To be accurate: ...", "To be accurate: we lost two clients, not three."),
        ("More precisely: ...", "More precisely: the outage lasted forty minutes, not an hour."),
        ("The better way to put it is...", "The better way to put it is: we're cautious, not opposed."),
     ]),
    ("More Instant Corrections — Flagging the Error",
     "You realize mid-sentence that what you just said was wrong and need to flag it fast.",
     "used to flag mid-sentence that what you just said was wrong, before correcting it",
     [
        ("Strike that.", "The launch is delayed — strike that, it's actually back on track."),
        ("Scratch that.", "We're going with vendor A — scratch that, we picked vendor B."),
        ("Ignore that.", "The report's ready — ignore that, I sent you an old draft."),
        ("I misspoke.", "I said the budget was cut in half — I misspoke, it was cut by a third."),
        ("I got that backwards.", "I said the client called us — I got that backwards, we called them."),
        ("I had that the wrong way round.", "I said Dev handles it before QA — I had that the wrong way round."),
        ("Sorry, wrong word.", "It's a 'feature', sorry, wrong word — it's actually a bug."),
        ("That's not the word I wanted.", "It's 'ambitious' — no, that's not the word I wanted, more like 'unrealistic'."),
        ("Actually, no —...", "Actually, no — the meeting's at three, not two."),
        ("Hang on, that's wrong.", "Hang on, that's wrong — the invoice went out last week, not this week."),
     ]),
    ("More Self-Checks & Confirmations",
     "You've just used a term you're unsure about and want to quickly confirm it with the other person.",
     "used to quickly confirm a term with the other person right after using it",
     [
        ("Am I saying that right?", "I called it 'ubiquitous' — am I saying that right?"),
        ("Is that how you say it?", "The word is 'niche' — is that how you say it?"),
        ("Correct me if that's wrong.", "I think the merger closes in June — correct me if that's wrong."),
        ("Tell me if I've got the term wrong.", "We call it 'technical debt' — tell me if I've got the term wrong."),
        ("Does that sound right to you?", "I'd call this a 'soft launch' — does that sound right to you?"),
        ("Is that the term you use?", "We say 'onboarding' for this step — is that the term you use?"),
        ("I might have the wrong word — I mean...", "I might have the wrong word — I mean the person who approves the budget."),
        ("Sorry, is it \"X\" or \"Y\"?", "Sorry, is it \"affect\" or \"effect\" in this sentence?"),
        ("What's the proper term for it?", "We just call it 'the handoff' — what's the proper term for it?"),
     ]),
]

if __name__ == "__main__":
    generate_topic(
        out_path=OUT_PATH,
        exam_id="self-repair",
        title="Chunk Atlas — Real-Time Fluency: Self-Repair & Recovery",
        tier_id=TIER_ID,
        tier_name=TIER_NAME,
        groups_def=groups_def,
    )
