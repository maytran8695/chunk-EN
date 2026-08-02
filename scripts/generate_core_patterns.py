import json, os, random

random.seed(42)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_PATH = os.path.join(SCRIPT_DIR, "..", "data", "core-patterns.json")

# Phrase content below is copied by hand from the "Core Patterns" topic
# (tier "core" / nav tab "Situations") in ChunkAtlas_EN.jsx — sections
# H1-H14 (H15 skipped: it's meta-advice, not a distinct phrase set).
# H14 is split into 5 finer sub-groups since it bundles 5 unrelated
# functions (structuring / opinion / hedging-degree / contrast / cause-effect).
#
# Filtering/scoring in the app is done at TIER level (the 5 big nav tabs of
# ChunkAtlas_EN.jsx: Situations / Real-Time Fluency / Voice & Presence /
# Language Systems / Confidence & Humour) — NOT at this fine function-group
# level, per explicit request ("too many sub-tabs" for a filter). The fine
# group name below is only used inside the English explanation text, for
# learning value, not as a separate filterable field.
TIER_ID = "core"
TIER_NAME = "Situations"

# (function_label, context_en, [phrases])
groups_def = [
    ("Opening",
     "You've just joined a meeting and need to open it so people get started.",
     ["Thanks everyone for joining.", "Let's get started.", "Let's take a quick look at the agenda.",
      "The goal of this meeting is...", "Today I'd like to discuss...", "Let me start with a quick overview.",
      "I'll briefly walk through...", "Let's begin with the key issue.", "Before we dive in, a quick update."]),
    ("Framing the main point",
     "You want to highlight the single most important point before saying anything else.",
     ["The key point is...", "The main issue is...", "The real question is...", "The core problem is...",
      "The main takeaway is...", "What really matters here is...", "The big picture is...",
      "The short/simple answer is...", "The bottom line is..."]),
    ("Organizing ideas",
     "You want to signal upfront that you'll present your ideas in a clear, multi-part structure.",
     ["There are three things to consider.", "There are two main reasons.", "Let's break this down.",
      "Let's look at this step by step.", "Let's go through them one by one.",
      "We can think about this in two ways.", "This can be divided into two parts.",
      "On the one hand... on the other hand..."]),
    ("Explaining",
     "You need to explain the reason or cause behind something you just mentioned.",
     ["This happens because...", "The reason is...", "One explanation is...", "Another factor is...",
      "This leads to...", "As a result...", "That's why...", "In other words...", "Put simply..."]),
    ("Giving examples",
     "You want to illustrate your point with a specific example.",
     ["For example...", "For instance...", "A good example is...", "Let me give you an example.",
      "Take the case of...", "This is similar to...", "This reminds me of..."]),
    ("Clarifying",
     "The listener seems to have misunderstood you — you need to restate it more clearly.",
     ["Let me clarify that.", "Just to clarify...", "What I mean is...", "Let me rephrase that.",
      "To put it another way...", "Let me be more specific.", "Let me expand on that."]),
    ("Asking questions",
     "You've just finished presenting and want to ask the listener what they think.",
     ["What do you think?", "How do you see this?", "Does that make sense?",
      "Could you elaborate on that?", "Can you walk me through that?", "What's your take on this?"]),
    ("Disagreeing politely",
     "You disagree with an opinion just raised, but want to push back politely, without creating tension.",
     ["I see your point, but...", "I'm not sure I agree.", "I see it slightly differently.",
      "That might be true, but...", "I'm not convinced yet.", "I would challenge that assumption."]),
    ("Steering the conversation",
     "The meeting is drifting off-topic — you want to pull everyone back to the main issue.",
     ["Let's step back for a moment.", "Let's focus on the main issue.",
      "Maybe we should look at the bigger picture.", "Let's not lose sight of the goal.",
      "Let's come back to the key question.", "Let's take a closer look."]),
    ("Concluding",
     "You're wrapping up your presentation and want to summarize the main point.",
     ["So to summarize...", "To wrap up...", "The key takeaway is...", "In summary...", "Overall...",
      "So the conclusion is...", "What we learned is...", "So moving forward..."]),
    ("Decision making",
     "You want to propose a specific direction or decision for the group.",
     ["We should probably...", "The best option is...", "I suggest we...",
      "One possible solution is...", "The next step is...", "Let's agree on...", "We should prioritize..."]),
    ("Buying thinking time",
     "You've just been asked a tough question and need a moment to think before answering.",
     ["That's a good question.", "Let me think about that.", "Give me a second.", "Let me consider that.",
      "Let me check if I understand.", "Let me think this through.", "Let me get back to that."]),
    ("Cutting the list short",
     "You've already covered everything necessary and want to wrap up without rambling further.",
     ["That's all. Anything else is noise.", "Look, the rest doesn't matter — those three cover it.",
      "First, second... and that's it. Okay, stop. The point's clear."]),
    ("Structuring (extended)",
     "You want to signal upfront that you'll make several structured points.",
     ["There are three main points I'd like to make.", "What this really comes down to is...",
      "If we break it down..."]),
    ("Giving opinions",
     "You want to state your personal opinion or belief about an issue.",
     ["I tend to believe that...", "I'm inclined to think that...", "I would argue that...",
      "I have mixed feelings about..."]),
    ("Hedging / degree",
     "You want to say something without stating it as an absolute — adding a degree of caution.",
     ["To some extent...", "It depends on...", "It's more complicated than it appears.",
      "Generally speaking..."]),
    ("Contrast",
     "You want to raise a contrasting point or downside compared to what was just said.",
     ["On the other hand...", "That being said...", "Having said that...", "By contrast...",
      "The downside is...", "A major advantage is..."]),
    ("Cause & effect (formal)",
     "You want to explain why something happened, in a more formal register than a plain \"because\".",
     ["The reason for this is...", "This is mainly because...", "Consequently...",
      "This can be attributed to..."]),
]

# sanity: unique phrases within each group, and build a global phrase->group map
all_phrases = []
for name, ctx, phrases in groups_def:
    for p in phrases:
        all_phrases.append((name, p))

def build_question(qid, name, ctx, phrases, used_correct):
    # pick a correct phrase not yet used for this group if possible
    candidates = [p for p in phrases if p not in used_correct.get(name, set())]
    if not candidates:
        candidates = phrases
    correct_phrase = random.choice(candidates)
    used_correct.setdefault(name, set()).add(correct_phrase)

    # distractors: 3 phrases from OTHER groups, no repeats
    other_pool = [(n, p) for n, p in all_phrases if n != name]
    random.shuffle(other_pool)
    distractors = []
    for n, p in other_pool:
        if p == correct_phrase:
            continue
        if len(distractors) < 3:
            distractors.append(p)
    distractors = distractors[:3]

    options_pool = [correct_phrase] + distractors
    random.shuffle(options_pool)
    letters = ["A", "B", "C", "D"]
    options = {letters[i]: options_pool[i] for i in range(4)}
    correct_letter = [l for l, v in options.items() if v == correct_phrase][0]

    explanation = (
        f'This chunk belongs to the "{name}" function — {ctx[0].lower()}{ctx[1:]} '
        f'The correct chunk is: "{correct_phrase}". The other options are valid chunks too, '
        f'but they belong to a different communicative function, so they don\'t fit this context.'
    )

    return {
        "id": qid,
        "ka": TIER_ID,
        "kaName": TIER_NAME,
        "question": ctx + " Which chunk fits best?",
        "options": options,
        "correct": correct_letter,
        "explanation": explanation,
    }

questions = []
qid = 1
used_correct = {}
# generate ~3 questions per group (or len(phrases) if fewer), capped at 4
for name, ctx, phrases in groups_def:
    n = min(4, max(2, len(phrases) // 2))
    for _ in range(n):
        questions.append(build_question(qid, name, ctx, phrases, used_correct))
        qid += 1

print("total questions:", len(questions))
out = {
    "examId": "core",
    "title": "Chunk Atlas — Situations: Core Patterns",
    "questions": questions,
}
with open(OUT_PATH, 'w') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("wrote", OUT_PATH)
