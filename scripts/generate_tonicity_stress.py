import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from lib import generate_topic

OUT_PATH = os.path.join(SCRIPT_DIR, "..", "data", "tonicity-stress.json")

# Phrase content copied by hand from the "Tonicity: Stress Changes Meaning"
# topic (tier "presence" / nav tab "Voice & Presence") — sections P1.1-P1.4,
# V1.5. P1.1 (the classic "same 7 words, 7 meanings" sentence) is split into
# 7 finer single-phrase groups, one per word that can carry contrastive
# stress, since each is a genuinely distinct correction/implication and this
# lets the near-identical variants act as each other's distractors.
TIER_ID = "presence"
TIER_NAME = "Voice & Presence"

groups_def = [
    ("Correcting the speaker",
     "You want to make clear that someone else made a claim — not you — using stress alone.",
     "used to stress the subject 'I', implying someone else is the one who said it",
     [
        ("**I** didn't say he stole the money.",
         "**I** didn't say he stole the money — that was Mark, not me."),
     ]),
    ("Denying it outright",
     "You want to flatly deny that you ever made a claim at all, using stress alone.",
     "used to stress 'didn't', flatly denying the whole statement",
     [
        ("I **didn't** say he stole the money.",
         "I **didn't** say he stole the money — I never said anything like that."),
     ]),
    ("Correcting the verb",
     "You want to point out that you only implied something, without ever stating it outright.",
     "used to stress 'say', implying the point was suggested, not stated outright",
     [
        ("I didn't **say** he stole the money.",
         "I didn't **say** he stole the money — I just raised a question about the missing receipts."),
     ]),
    ("Correcting who",
     "You want to make clear a different person is responsible, not the one currently being blamed.",
     "used to stress 'he', implying someone else — not him — is responsible",
     [
        ("I didn't say **he** stole the money.",
         "I didn't say **he** stole the money — I think it was someone on the finance team."),
     ]),
    ("Correcting the action",
     "You want to acknowledge he took it, while rejecting the specific word used to describe it.",
     "used to stress 'stole', rejecting that specific word while accepting he took it",
     [
        ("I didn't say he **stole** the money.",
         "I didn't say he **stole** the money — I said he borrowed it without asking."),
     ]),
    ("Correcting the amount",
     "You want to clarify he took a different sum, not the specific amount in question.",
     "used to stress 'the', implying a different, specific sum is meant",
     [
        ("I didn't say he stole **the** money.",
         "I didn't say he stole **the** money — he took some other funds entirely."),
     ]),
    ("Correcting what",
     "You want to clarify he stole something else, not the money.",
     "used to stress 'money', implying something else was stolen instead",
     [
        ("I didn't say he stole the **money**.",
         "I didn't say he stole the **money** — he took the client list."),
     ]),
    ("Stressing new information",
     "You're answering or reacting to something already said, and want to naturally stress only the new information while gliding over what's already known.",
     "used to place stress on new information while gliding over what's already known — the default English stress rule",
     [
        ("It's a **book**.",
         'What\'s that?" — "It\'s a **book**, actually, not a folder.'),
        ("It's **my** book.",
         'Is that your book?" — "It\'s **my** book — I bought it yesterday.'),
        ("What **kind** of car?",
         'I bought a car." — "Nice! What **kind** of car did you get?'),
     ]),
    ("Contrastive correction",
     "You want to correct or contrast two things by stressing just the words that differ, without adding extra explanation.",
     "used to correct or contrast two ideas by stressing only the words that differ",
     [
        ("I said **Tues**day, not **Thurs**day.",
         'I said **Tues**day, not **Thurs**day — please check your calendar again.'),
        ("It's not a **budget** problem, it's a **timeline** problem.",
         "It's not a **budget** problem, it's a **timeline** problem — we have the money, just not the time."),
        ("I'm not saying it's **wrong** — I'm saying it's **incomplete**.",
         "I'm not saying it's **wrong** — I'm saying it's **incomplete**, so let's add the missing steps."),
        ("We **can** do it. The question is whether we **should**.",
         'We **can** do it. The question is whether we **should**, given the risk.'),
        ("That's what he **said**. It's not what he **meant**.",
         "That's what he **said**. It's not what he **meant** — read between the lines."),
        ("I didn't say it was **easy**. I said it was **possible**.",
         "I didn't say it was **easy**. I said it was **possible** — with the right resources."),
     ]),
    ("Tone-unit chunking",
     "You're about to say something important and want to break it into short deliberate chunks so it lands with weight.",
     "used to break speech into short tone units, each carrying its own stress, to sound deliberate and weighty",
     [
        ("The main issue | is that the data | doesn't reconcile | across systems.",
         'The main issue | is that the data | doesn\'t reconcile | across systems." — four short chunks, four stresses, easy to follow.'),
        ("This. Changes. Everything.",
         'This. Changes. Everything." — three blunt chunks land far harder than one flat sentence.'),
     ]),
    ("Contrastive correction (extra)",
     "You want to correct a specific detail someone got wrong, using stress on just the contrasting word — no extra explanation needed.",
     "used to correct a specific misunderstanding by stressing only the contrasting word",
     [
        ("I said **Tuesday**, not **Thursday**.",
         'I said **Tuesday**, not **Thursday** — you must have misheard me.'),
        ("It's not **my** decision, it's **hers**.",
         "It's not **my** decision, it's **hers** — she's the one who signs off."),
        ("I **asked** him — I didn't **tell** him.",
         "I **asked** him — I didn't **tell** him, so he was free to say no."),
        ("We need it **done**, not **perfect**.",
         "We need it **done**, not **perfect** — ship it and we'll iterate."),
        ("That's the **symptom**, not the **cause**.",
         "That's the **symptom**, not the **cause** — the real issue is upstream."),
        ("I'm not **against** it — I'm **cautious** about it.",
         "I'm not **against** it — I'm just **cautious** about it, given the cost."),
        ("It **works**. It just isn't **ready**.",
         "It **works**. It just isn't **ready** for a client demo yet."),
        ("**You** think that. **I** don't.",
         "**You** think that. **I** don't — and that's fine, we can disagree."),
     ]),
]

if __name__ == "__main__":
    generate_topic(
        out_path=OUT_PATH,
        exam_id="tonicity-stress",
        title="Chunk Atlas — Voice & Presence: Tonicity",
        tier_id=TIER_ID,
        tier_name=TIER_NAME,
        groups_def=groups_def,
    )
