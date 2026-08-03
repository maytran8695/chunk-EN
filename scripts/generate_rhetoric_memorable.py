import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from lib import generate_topic

OUT_PATH = os.path.join(SCRIPT_DIR, "..", "data", "rhetoric-memorable.json")

# Phrase content below is copied by hand from the "Rhetoric & Memorable
# Language" topic (tier "presence" / nav tab "Voice & Presence") in
# final_topics.json, sections P6.1-P6.7 (V6.7).
#
# P6.1/P6.2/P6.3 map directly to groups 1-3 (tricolon / antithesis /
# repetition-and-rhetorical-question), one group per header, since each is
# already a single distinct device.
# P6.4 ("Cụ thể thắng trừu tượng") only yields its metaphor/analogy
# examples as "i" items (the "c" comparison blocks were skipped per spec).
# P6.6 ("Thêm: kho câu đáng nhớ dùng ngay") is a grab-bag whose items are
# each explicitly labelled by the SAME function already covered elsewhere
# (Đóng khung lại = framing, Cụ thể hoá = concreteness, Đơn giản hoá =
# simplifying, Tương phản = contrast, Bộ ba = tricolon, Ẩn dụ = metaphor,
# Chốt = closing line) — rather than making a redundant catch-all group,
# each item was folded into the matching functional group (P6.1 tricolon,
# P6.2 contrast, P6.4 concrete/metaphor, P6.5 framing, P6.7 closing lines),
# with "Đơn giản hoá" (simplifying) kept as its own small new group since
# no earlier group covers that function. Near-duplicate phrasings that
# would otherwise repeat an existing phrase almost verbatim (e.g. P6.6's
# "I'd feel the same" vs its own "I hear you" type overlaps — here,
# P6.6's "Let's not ask..." vs P6.5's identical line) were kept only once.
# P6.7 duplicates two P6.6 lines exactly ("So the choice is simple: [A] or
# [B]." and "Cheap now, expensive later.") — each kept once, in the group
# that fits it best (closing lines, contrast).
TIER_ID = "presence"
TIER_NAME = "Voice & Presence"

groups_def = [
    ("Rule of three (tricolon)",
     "You want to end your point with a punchy list of three that people will actually remember.",
     "used to give a point rhythm and staying power by packaging it as a list of three",
     [
        ("Faster, cheaper, better.", "The new process is faster, cheaper, better — that's the whole pitch in three words."),
        ("Simple, clear, honest.", "That's all I want the onboarding email to be: simple, clear, honest."),
        ("It's not about X. It's not about Y. It's about Z.", "It's not about the budget. It's not about the timeline. It's about trust between the teams."),
        ("We tried it. We measured it. We learned from it.", "We tried it. We measured it. We learned from it — and now we're doing it properly."),
        ("Three things: [A], [B], [C].", "Three things: fix the login bug, ship the report, brief the client."),
        ("What we know, what we assume, what we're guessing.", "Let's separate what we know, what we assume, and what we're guessing before we commit to a plan."),
     ]),
    ("Antithesis & contrast (not X, but Y)",
     "You want to sharpen your point by directly contrasting it with what it is NOT.",
     "used to sharpen a point by directly contrasting it with what it is not",
     [
        ("It's not a technology problem, it's a people problem.", "The rollout keeps stalling — it's not a technology problem, it's a people problem."),
        ("We don't need more data. We need better questions.", "We've run five surveys already — we don't need more data, we need better questions."),
        ("The goal isn't to be busy. The goal is to be effective.", "Everyone's in back-to-back meetings, but the goal isn't to be busy. The goal is to be effective."),
        ("Ask not what X... but what Y...", "Ask not what the client can give us, but what we can build for them."),
        ("Cheap now, expensive later.", "Skipping the code review is cheap now, expensive later."),
        ("Slow is smooth, smooth is fast.", "Take your time on the handover doc — slow is smooth, smooth is fast."),
     ]),
    ("Repetition & rhetorical questions",
     "You want your point to have rhythm and stick in people's heads through deliberate repetition.",
     "used to make a point stick through deliberate repetition or a pointed rhetorical question",
     [
        ("We can do this. We should do this. We will do this.", "We can do this. We should do this. We will do this — starting Monday."),
        ("Built for speed. Priced for speed. Designed for speed.", "This plan is built for speed. Priced for speed. Designed for speed."),
        ("Plan the work, work the plan.", "No more scope changes mid-sprint — plan the work, work the plan."),
        ("Quality isn't an act, it's a habit.", "We don't do one big QA push at the end — quality isn't an act, it's a habit."),
        ("So where does that leave us?", "The vendor just pulled out — so where does that leave us?"),
     ]),
    ("Making the abstract concrete",
     "You want to replace a vague, abstract statement with a specific number, image, or picture people can actually act on.",
     "used to replace a vague, abstract statement with something specific and vivid people can picture or act on",
     [
        ("We're building the plane while flying it.", "Nobody signed off on a full spec — we're building the plane while flying it."),
        ("That's a band-aid on a broken leg.", "Restarting the server every night isn't a fix, that's a band-aid on a broken leg."),
        ("Think of it like a queue at a coffee shop — one slow order blocks everyone.", "Think of it like a queue at a coffee shop — one slow order blocks everyone, and that's exactly what's happening in our review process."),
        ("We're paying rent on a house we don't live in.", "We're still paying for that license nobody uses — we're paying rent on a house we don't live in."),
        ("That's a sticking plaster.", "Adding another approval step isn't a real fix, that's a sticking plaster."),
        ("Let me put a number on that.", "Let me put a number on that: it's costing us about four hours a week."),
        ("What does that look like on Monday morning?", "Say we approve this today — what does that look like on Monday morning for the support team?"),
     ]),
    ("Reframing (choosing the frame)",
     "You want to control how people perceive an issue by changing the frame around it before they form their own opinion.",
     "used to control how people perceive an issue by changing the frame around it before they form their own opinion",
     [
        ("This isn't a cost — it's an investment.", "This isn't a cost — it's an investment in not losing customers to downtime."),
        ("We're not cutting scope. We're sequencing it.", "We're not cutting scope. We're sequencing it — the reporting feature just moves to phase two."),
        ("The question isn't whether we can afford to do it. It's whether we can afford not to.", "The question isn't whether we can afford the security audit. It's whether we can afford not to."),
        ("Let's not ask what it costs. Let's ask what it saves.", "Let's not ask what the migration costs. Let's ask what it saves us in support tickets."),
        ("The real question is...", "The real question is whether we can support this at scale, not whether we can build it."),
        ("That's the symptom, not the cause.", "Slow load times are the symptom, not the cause — the real issue is the database design."),
     ]),
    ("Simplifying the point",
     "You want to cut through complexity and reduce your point to its simplest, most digestible form.",
     "used to cut through complexity and reduce a point to its simplest, most digestible form",
     [
        ("Strip it back and it's just...", "Strip it back and it's just a form with three fields."),
        ("At its simplest...", "At its simplest, this is a scheduling problem, not a technology one."),
     ]),
    ("Memorable closing lines",
     "You're wrapping up and want your closing line to be the one part people actually remember and repeat afterwards.",
     "used as a closing line designed to be the one part people remember and repeat afterwards",
     [
        ("So the choice is simple: [A] or [B].", "So the choice is simple: we delay the launch, or we ship with known bugs."),
        ("If we do nothing, [X]. That's the decision we're making by default.", "If we do nothing, the contract lapses in March. That's the decision we're making by default."),
        ("We can have it fast, cheap, or good. Pick two.", "We can have it fast, cheap, or good. Pick two — that's the trade-off on the table."),
        ("That's not a plan, that's a hope.", "Hoping the team catches up next sprint isn't a plan, that's a hope."),
        ("We're treating the symptom, not the cause.", "Adding more support staff means we're treating the symptom, not the cause."),
        ("The cost of waiting is higher than the cost of acting.", "Every week we delay, churn goes up — the cost of waiting is higher than the cost of acting."),
        ("Let's not confuse activity with progress.", "We've had ten meetings about this and shipped nothing — let's not confuse activity with progress."),
     ]),
]

if __name__ == "__main__":
    generate_topic(
        out_path=OUT_PATH,
        exam_id="rhetoric-memorable",
        title="Chunk Atlas — Voice & Presence: Rhetoric & Memorable Language",
        tier_id=TIER_ID,
        tier_name=TIER_NAME,
        groups_def=groups_def,
    )
