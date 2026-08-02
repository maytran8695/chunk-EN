import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from lib import generate_topic

OUT_PATH = os.path.join(SCRIPT_DIR, "..", "data", "misunderstanding.json")

# Phrase content below is copied by hand from the "Misunderstanding, Both
# Ways" topic (tier "fluency" / F9-F10) in the source content set. F9.6 is
# a supplementary "kho" (repository) list that mostly repeats the earlier
# sections verbatim; only its NEW, non-duplicate phrasings were folded into
# the matching functional group below (e.g. "My fault — let me rephrase."
# into group 1; "So, just to be clear, you're saying...?" and "Let me play
# that back." into the escalation-ladder group, since both are further
# confirmation steps on that same ladder).
TIER_ID = "fluency"
TIER_NAME = "Real-Time Fluency"

groups_def = [
    ("Fixing it when they misunderstood you",
     "You just said something and the listener clearly took it the wrong way — you need to fix it fast without making them feel bad.",
     "used to fix a misunderstanding by taking the blame yourself, without making the listener feel bad",
     [
        ("No no — I think I said that badly. What I meant was...", "No no — I think I said that badly. What I meant was we should pause the feature, not cancel it."),
        ("Sorry, that's my fault — let me be clearer.", "Sorry, that's my fault — let me be clearer about which environment I mean."),
        ("I don't think I explained that well. Let me try again.", "I don't think I explained that well. Let me try again, more slowly this time."),
        ("That's not quite what I meant. I meant [X], not [Y].", "That's not quite what I meant. I meant the staging server, not production."),
        ("Ah, I see the confusion — I wasn't clear about [X].", "Ah, I see the confusion — I wasn't clear about which ticket I was referring to."),
        ("Let me put it differently...", "Let me put it differently — we're not cutting the feature, just delaying it."),
        ("My fault — let me rephrase.", "My fault — let me rephrase: I meant next week, not this week."),
     ]),
    ("Realizing you misunderstood and answered the wrong question",
     "You've been answering for a while and just realized you misunderstood the question entirely.",
     "used when you realize partway through that you misunderstood the question",
     [
        ("Sorry — I don't think I'm answering what you actually asked.", "Sorry — I don't think I'm answering what you actually asked. Could you say it again?"),
        ("Hang on, did you mean [X] or [Y]?", "Hang on, did you mean the frontend bug or the backend one?"),
        ("I may have misread your question. Could you say it again?", "I may have misread your question. Could you say it again, please?"),
        ("Let me back up — what were you actually asking?", "Let me back up — what were you actually asking about the rollout?"),
        ("Ah — you meant [X]. I was answering a different question entirely.", "Ah — you meant the client's budget. I was answering a different question entirely."),
     ]),
    ("Asking someone to repeat themselves, more specifically each time",
     "You didn't catch what someone said and need to ask them to repeat it — more specifically than just saying 'Sorry?' again.",
     "used to ask someone to repeat or clarify something, with increasing specificity each time",
     [
        ("Sorry?", "Sorry? I didn't quite catch that last part."),
        ("Come again?", "Come again? The line cut out for a second."),
        ("Say that again?", "Say that again? I missed the number you mentioned."),
        ("Sorry, you lost me after [X].", "Sorry, you lost me after 'the second endpoint' — could you continue from there?"),
        ("The last bit?", "The last bit? I caught everything except that."),
        ("Did you say [X]?", "Did you say fifteen or fifty?"),
        ("Sorry — [X]?", "Sorry — Q3, not Q2?"),
        ("Sorry, could you rephrase that?", "Sorry, could you rephrase that? I'm not sure I followed the logic."),
        ("In other words?", "In other words? I think I lost you somewhere in the middle."),
        ("Could you drop that in the chat?", "Could you drop that in the chat? I want to make sure I get the exact wording."),
        ("How do you spell that?", "How do you spell that? I've never heard that term before."),
        ("So, just to be clear, you're saying...?", "So, just to be clear, you're saying we should push the release, not cancel it?"),
        ("Let me play that back.", "Let me play that back to make sure I got it: we're moving the deadline to Friday."),
     ]),
    ("Admitting you truly can't understand, after repeated tries",
     "You genuinely can't make out what someone is saying, even after asking a couple of times, and need to find another way through.",
     "used when you genuinely can't understand someone even after asking a couple of times",
     [
        ("Sorry — I'm struggling with the line, not with you.", "Sorry — I'm struggling with the line, not with you. Can you try again?"),
        ("I want to make sure I get this right — could you type it?", "I want to make sure I get this right — could you type the figure in the chat?"),
        ("Let's do this: send me a message and I'll pick it up after.", "Let's do this: send me a message and I'll pick it up after the call."),
        ("I'll be honest, I didn't catch that at all. One more time, slowly?", "I'll be honest, I didn't catch that at all. One more time, slowly?"),
     ]),
    ("Getting a mispronounced word understood",
     "You said a word and the other person clearly didn't catch it — repeating it louder isn't helping.",
     "used to get a mispronounced or unfamiliar word understood, without just repeating it louder",
     [
        ("It's [X] — spelled out letter by letter.", "It's Kubernetes — spelled out letter by letter: K-U-B-E-R-N-E-T-E-S."),
        ("[X] — you know, the thing we use for...", "Kanban — you know, the thing we use for tracking tickets on a board."),
        ("Sorry — let me use another word for that.", "Sorry — let me use another word for that: I meant the deadline, not the due date."),
        ("My accent's doing me no favours today.", "My accent's doing me no favours today — let me try that word again."),
        ("How do you say it?", "How do you say it? I've only ever seen it written down."),
        ("Am I saying that right?", "Am I saying that right? I always mix up the pronunciation of that tool's name."),
     ]),
]

if __name__ == "__main__":
    generate_topic(
        out_path=OUT_PATH,
        exam_id="misunderstanding",
        title="Chunk Atlas — Real-Time Fluency: Misunderstanding, Both Ways",
        tier_id=TIER_ID,
        tier_name=TIER_NAME,
        groups_def=groups_def,
    )
