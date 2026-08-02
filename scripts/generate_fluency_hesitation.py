import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from lib import generate_topic

OUT_PATH = os.path.join(SCRIPT_DIR, "..", "data", "fluency-hesitation.json")

# Phrase content below is copied by hand from the "Fluency & Hesitation
# Management" topic (tier "fluency" / F1) in the source content set.
# F1.1 is skipped entirely: it's pure meta-advice about WHERE to pause
# (a principle + a practice exercise), with no actual quotable chunks.
# F1.2-F1.6 are each split into finer sub-groups since they bundle several
# distinct stalling functions (mid-utterance fillers vs. sentence-openers vs.
# vocal stalling; acknowledging a question vs. framing the answer's
# structure; personal-opinion frames vs. explaining/hedging frames; asking
# for time vs. deferring/clarifying).
TIER_ID = "fluency"
TIER_NAME = "Real-Time Fluency"

groups_def = [
    ("Fillers Instead of Um (Mid-Utterance)",
     "You're mid-sentence, searching for your next word, and want to avoid a bare \"um\" or \"uh\".",
     "used mid-utterance to hold the floor naturally while you find your next word, instead of a bare \"um\"",
     [
        ("I mean...", "It's — I mean... it's not really about the budget, it's about trust."),
        ("you know...", "The whole approach is, you know... a bit outdated at this point."),
        ("let's see...", "The number we need is, let's see... around twelve thousand."),
        ("how do I put this...", "How do I put this... the client isn't exactly thrilled with the draft."),
        ("right...", "So the plan is, right... we ship Friday and patch over the weekend."),
     ]),
    ("Sentence-Opening Fillers",
     "You need a beat before you even start your sentence, without opening with a bare \"um\".",
     "used as a natural opener to buy a half-second before the sentence itself begins",
     [
        ("Well, ...", "Well, I think we should just push the deadline back a week."),
        ("So, ...", "So, the short version is: the vendor missed the deadline again."),
        ("Look, ...", "Look, I know this isn't what you wanted to hear, but the numbers don't lie."),
        ("Actually, ...", "Actually, I think we're overcomplicating this whole thing."),
     ]),
    ("Stalling by Elongation & Repetition",
     "You need an extra second mid-sentence and want to stall smoothly, without breaking your flow.",
     "used to draw out a word or briefly repeat it to buy thinking time without resorting to \"um\"",
     [
        ("It's... a really good question.", "It's... a really good question. Give me a second to think it through."),
        ("I think — I think what matters is...", "I think — I think what matters is whether the client trusts us again."),
     ]),
    ("Buying Time — Acknowledging the Question",
     "You've just been asked a tough question and want a beat before diving into the actual answer.",
     "used to acknowledge a tough question and buy a moment before answering it properly",
     [
        ("That's a really good question.", "That's a really good question — let me think about how to explain it."),
        ("That's an interesting way to put it.", "That's an interesting way to put it. Let me answer that properly."),
        ("Good question.", "Good question. Give me a moment to think that through."),
        ("Interesting question.", "Interesting question — nobody's asked me that before."),
        ("I want to make sure I answer that properly.", "I want to make sure I answer that properly, so bear with me a second."),
        ("Let me get this right.", "Let me get this right before I respond — you're asking about the whole team, not just my project?"),
        ("I want to give you a proper answer, not a quick one.", "I want to give you a proper answer, not a quick one, so let me think for a second."),
     ]),
    ("Buying Time — Framing the Answer's Structure",
     "You want to show you're organizing your thoughts before you actually deliver the answer.",
     "used to signal you're structuring your answer before actually giving it",
     [
        ("It depends, really.", "It depends, really — on whether finance approves the extra budget."),
        ("There are a couple of ways to look at it.", "There are a couple of ways to look at it, so let me walk through both."),
        ("So there are two things going on here.", "So there are two things going on here: the delay, and who's responsible for it."),
        ("Let me break that into two parts.", "Let me break that into two parts — the technical issue and the client relationship."),
        ("Before I answer that, let me just say...", "Before I answer that, let me just say the whole team worked really hard on this."),
        ("Can I come at that from a different angle?", "Can I come at that from a different angle? It might make more sense that way."),
        ("Funnily enough, I was thinking about this the other day.", "Funnily enough, I was thinking about this the other day, after our last call."),
     ]),
    ("Buying Time — Extra Framing & Thinking Out Loud",
     "You're working through a question in real time and want the listener to follow your thinking as you go.",
     "used to show you're actively working through a question in real time, rather than staying silent",
     [
        ("There are two ways to look at this.", "There are two ways to look at this — from the client's side and from ours."),
        ("It depends on...", "It depends on... how much risk we're willing to take this quarter."),
        ("Short answer or long answer?", "Short answer or long answer? Because the long one has a lot of caveats."),
        ("My starting point would be...", "My starting point would be to check what the client actually signed off on."),
        ("Let me start with what I know.", "Let me start with what I know, and I'll flag anything I'm unsure of."),
        ("I'm thinking out loud here...", "I'm thinking out loud here, but maybe we split this into two releases."),
        ("Let me work through this...", "Let me work through this — okay, if we cut scope, we could still hit Friday."),
     ]),
    ("Automatic Frames — Personal Take",
     "You're about to give your personal opinion and want a ready-made phrase to launch straight into it.",
     "used as a ready-made opener to launch straight into a personal opinion",
     [
        ("The thing is, ...", "The thing is, we already promised this feature to the client."),
        ("The way I see it, ...", "The way I see it, we're better off delaying than shipping something broken."),
        ("What I'd say is, ...", "What I'd say is, the risk is small compared to the upside."),
        ("If I'm honest, ...", "If I'm honest, I don't think the current plan is realistic."),
        ("If I had to pick, ...", "If I had to pick, I'd go with the cheaper vendor."),
        ("If it were up to me, ...", "If it were up to me, we'd cancel the feature entirely."),
     ]),
    ("Automatic Frames — Explaining & Hedging",
     "You want to illustrate or explain something but aren't fully certain yet, and need a launching frame.",
     "used to launch into an explanation or illustration while signaling some uncertainty",
     [
        ("It's a bit like...", "It's a bit like debugging blind — you don't know what's wrong until you dig in."),
        ("Think of it this way: ...", "Think of it this way: every delay here costs us a day downstream too."),
        ("To give you an example, ...", "To give you an example, our biggest client hit this exact bug last month."),
        ("I'm not sure, but my sense is...", "I'm not sure, but my sense is the outage was on their end, not ours."),
        ("I'd have to check, but I think...", "I'd have to check, but I think the contract renews in October."),
        ("There's a short answer and a long answer. The short one is...", "There's a short answer and a long answer. The short one is: not yet."),
     ]),
    ("Asking for More Time",
     "You genuinely need a few extra seconds mid-conversation and want to ask for them directly.",
     "used to directly ask for a few extra seconds mid-conversation",
     [
        ("Give me a second.", "Give me a second — I want to check the numbers before I answer."),
        ("Bear with me.", "Bear with me, I'm trying to remember exactly how we phrased it."),
        ("Hold that thought.", "Hold that thought — let me just finish this calculation first."),
        ("Let me think.", "Let me think... okay, I believe the fix went out on Tuesday."),
        ("Give me a sec.", "Give me a sec, I need to pull up the email thread."),
        ("Hang on a moment.", "Hang on a moment, I want to get this exactly right."),
     ]),
    ("Deferring, Clarifying & Coming Back to It",
     "You're being rushed for an answer, or the question is too broad to answer immediately.",
     "used to defer an answer briefly, or narrow down a broad question, without losing the floor",
     [
        ("Let me finish the thought.", "Let me finish the thought — I promise I'm getting to the point."),
        ("I'm getting there.", "I'm getting there — just laying out the context first."),
        ("Can I come back to that?", "Can I come back to that once I've checked the actual figures?"),
        ("Let me park that and think.", "Let me park that and think — I don't want to give you a rushed answer."),
        ("What specifically are you asking about?", "What specifically are you asking about — the timeline, or the budget?"),
        ("In what context?", "In what context? That changes how I'd answer."),
     ]),
]

if __name__ == "__main__":
    generate_topic(
        out_path=OUT_PATH,
        exam_id="fluency-hesitation",
        title="Chunk Atlas — Real-Time Fluency: Fluency & Hesitation Management",
        tier_id=TIER_ID,
        tier_name=TIER_NAME,
        groups_def=groups_def,
    )
