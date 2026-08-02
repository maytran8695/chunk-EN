import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from lib import generate_topic

OUT_PATH = os.path.join(SCRIPT_DIR, "..", "data", "damage-control.json")

# Phrase content below is copied by hand from the "Damage Control: When You
# Got It Wrong" topic (tier "fluency" / F12) in the source content set —
# sections F12.1-F12.6. F12.7 ("Nguyen tac chung cua chua chay") is skipped:
# it's a numbered list of meta-advice principles about damage control in
# general, not actual chunks — the same exception generate_core_patterns.py
# made for H15. F11.8 is a supplementary "kho" (repository) list that
# mostly repeats F12.1-F12.6 verbatim, so it contributed no new phrases.
TIER_ID = "fluency"
TIER_NAME = "Real-Time Fluency"

groups_def = [
    ("Correcting a wrong fact or number on the spot",
     "You just realized you said the wrong number or fact, seconds after saying it.",
     "used to correct a wrong fact or number immediately, without dwelling on it",
     [
        ("Sorry — 15%, not 50%. Let me say that again: 15%.", "Sorry — 15%, not 50%. Let me say that again: 15%, that's the actual conversion rate."),
        ("Correction: that's Q3, not Q2.", "Correction: that's Q3, not Q2 — I misspoke a second ago."),
        ("Let me correct that figure — it's actually [X].", "Let me correct that figure — it's actually 42, not 24."),
        ("I misspoke — [X], not [Y].", "I misspoke — Friday, not Thursday."),
        ("Going back a slide — I gave you the wrong number earlier. It's [X].", "Going back a slide — I gave you the wrong number earlier. It's actually $12,000, not $1,200."),
        ("I think that's right, but let me verify and confirm after.", "I think that's right, but let me verify and confirm after the call."),
     ]),
    ("Walking back a promise you shouldn't have made",
     "You just promised something in the moment that you're not actually sure you can deliver.",
     "used to walk back a promise you shouldn't have made, before it becomes a broken commitment",
     [
        ("Actually, let me walk that back — I need to check capacity first.", "Actually, let me walk that back — I need to check capacity with the team first."),
        ("Actually, I shouldn't commit to that until I've spoken to the team.", "Actually, I shouldn't commit to that until I've spoken to the team about bandwidth."),
        ("Let me revise that: I can commit to [X], but not [Y].", "Let me revise that: I can commit to the design by Friday, but not the full build."),
        ("I've had a think — I was too optimistic on the timeline. Here's what's realistic.", "I've had a think — I was too optimistic on the timeline. Here's what's realistic."),
        ("That works, assuming [condition]. If not, we'd need to revisit.", "That works, assuming the vendor delivers on time. If not, we'd need to revisit."),
     ]),
    ("Recovering from a comment that came out wrong",
     "Something you said came out sounding harsher or ruder than you intended.",
     "used to recover quickly from a comment that came out harsher than intended",
     [
        ("Sorry, that came out wrong.", "Sorry, that came out wrong — I didn't mean it as a criticism."),
        ("That sounded harsher than I meant it.", "That sounded harsher than I meant it — I was just frustrated with the delay."),
        ("Let me rephrase that — I didn't mean it the way it sounded.", "Let me rephrase that — I didn't mean it the way it sounded."),
        ("That was a poor choice of words.", "That was a poor choice of words on my part."),
        ("I apologise — that was out of line.", "I apologise — that comment about the QA team was out of line."),
        ("I think I said that badly — are we okay?", "I think I said that badly earlier — are we okay?"),
     ]),
    ("Recovering from a joke that fell flat",
     "You made a joke and it landed with dead silence.",
     "used to recover gracefully when a joke falls flat, instead of explaining it",
     [
        ("Tough crowd.", "Tough crowd. Okay, let's get back to the roadmap."),
        ("Okay, moving on.", "Okay, moving on — next slide."),
        ("That was funnier in my head.", "That was funnier in my head. Anyway, moving on."),
        ("I'll see myself out.", "I'll see myself out. Anyway, back to the numbers."),
        ("Wow, nothing. Noted.", "Wow, nothing. Noted. Moving on."),
        ("Right, I'll stick to the day job.", "Right, I'll stick to the day job — back to the roadmap."),
     ]),
    ("Correcting your tone or register mid-conversation",
     "You realize you just used the wrong tone or register for the audience you're talking to.",
     "used to correct your tone or register mid-conversation, without making a big deal of it",
     [
        ("Sorry — that was flippant. To be serious for a moment...", "Sorry — that was flippant. To be serious for a moment, this actually is a real risk."),
        ("...sorry, that sounded like a press release. What I mean is...", "...sorry, that sounded like a press release. What I mean is: we're behind."),
        ("Let me put that more plainly.", "Let me put that more plainly: we're behind schedule."),
        ("Sorry, that's internal jargon — [explanation].", "Sorry, that's internal jargon — I meant our ticket triage process."),
     ]),
    ("Recovering when you forget a name or term",
     "You're in the middle of introducing someone and suddenly forget their name.",
     "used to recover honestly when you forget a name or term mid-introduction",
     [
        ("I'm so sorry — your name has completely gone.", "I'm so sorry — your name has completely gone, and I feel terrible."),
        ("Have you two met?", "Have you two met? You're both on the platform team, right?"),
        ("Sorry, remind me of your name — I'm terrible with names, it's not personal.", "Sorry, remind me of your name — I'm terrible with names, it's not personal."),
        ("What's the official term for this? I've blanked.", "What's the official term for this process? I've completely blanked."),
        ("The... you know the one — [description]. Help me out.", "The... you know the one — the tool we use for tracking releases. Help me out."),
     ]),
]

if __name__ == "__main__":
    generate_topic(
        out_path=OUT_PATH,
        exam_id="damage-control",
        title="Chunk Atlas — Real-Time Fluency: Damage Control",
        tier_id=TIER_ID,
        tier_name=TIER_NAME,
        groups_def=groups_def,
    )
