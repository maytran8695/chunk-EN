import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from lib import generate_topic

OUT_PATH = os.path.join(SCRIPT_DIR, "..", "data", "collaboration-levels.json")

# Phrase content below is copied by hand from the "Collaboration Across
# Levels" topic (tier "core" / nav tab "Situations") — sections O1-O8.
# O1 ("Register-shifting") bundles 5 unrelated message contents (disagree /
# need time / didn't understand / impressed / change direction) across 3
# formality levels (casual peer / neutral cross-team / executive). It is
# split by REGISTER LEVEL into 3 groups, since the tested function here is
# "which formality level fits this audience", not the underlying message —
# mirrors how generate_core_patterns.py split H14 by distinct function.
# O8 ("Everyday executive presence") includes three "Thay 'X' -> 'Y'"
# substitution lines; only the recommended replacement (the Y side) is kept
# as the usable chunk.
TIER_ID = "core"
TIER_NAME = "Situations"

groups_def = [
    ("Speaking Casually With a Peer (Register)",
     "You're chatting informally with a close peer or teammate and need to express something naturally, without sounding stiff or overly formal.",
     "used in casual, peer-to-peer conversation — relaxed wording appropriate for someone you know well",
     [
        ("Hmm, I'm not sold on that — feels a bit risky to me.", "Hmm, I'm not sold on that — feels a bit risky to me. Can we look at another option?"),
        ("Can you give me till tomorrow? Brain's fried today.", "Can you give me till tomorrow? Brain's fried today, I need to look at this with fresh eyes."),
        ("Wait, you lost me — run that by me again?", "Wait, you lost me — run that by me again? I zoned out on the last part."),
        ("Okay this is actually really good.", "Okay this is actually really good — way better than the first draft."),
        ("Honestly, I think we should scrap this and rethink.", "Honestly, I think we should scrap this and rethink — the current plan just isn't working."),
     ]),
    ("Speaking Neutrally With a Client or Cross-Team Peer (Register)",
     "You're talking with someone from another team or a client — not a close friend, but not a senior executive either — and need a professional but approachable tone.",
     "used in neutral, professional register — appropriate for clients or people outside your immediate team",
     [
        ("I have some reservations about this approach — can I share a concern?", "I have some reservations about this approach — can I share a concern before we finalize the design?"),
        ("I'd like to give this the attention it deserves — could I come back to you by tomorrow?", "I'd like to give this the attention it deserves — could I come back to you by tomorrow with a proper answer?"),
        ("I want to make sure I follow — could you walk me through that once more?", "I want to make sure I follow — could you walk me through that once more, especially the pricing part?"),
        ("This is strong work — the structure especially.", "This is strong work — the structure especially made the proposal easy to follow."),
        ("I'm wondering if it's worth stepping back and reconsidering the approach.", "I'm wondering if it's worth stepping back and reconsidering the approach before we invest more budget."),
     ]),
    ("Speaking to Senior Leadership (Executive Register)",
     "You're addressing a senior leader or C-level executive and need to be brief, outcome-focused, and light on process detail.",
     "used with senior leadership or C-level audiences — short, outcome-focused, light on process detail",
     [
        ("Before we commit, I'd flag one risk: [X]. Worth a look?", "Before we commit, I'd flag one risk: the vendor's SLA doesn't cover weekends. Worth a look?"),
        ("I'll have a considered answer by tomorrow morning rather than a rushed one now.", "I'll have a considered answer by tomorrow morning rather than a rushed one now — I'd rather get the numbers right."),
        ("Help me understand the reasoning here — I want to make sure I'm aligned before we move.", "Help me understand the reasoning here — I want to make sure I'm aligned before we move ahead with the acquisition."),
        ("This moves the needle. Nicely done.", "This moves the needle. Nicely done — this is the kind of result the board wants to see."),
        ("I'd recommend we pivot — here's the one reason why.", "I'd recommend we pivot — here's the one reason why: our current CAC is unsustainable at this growth rate."),
     ]),
    ("Building Rapport & Psychological Safety",
     "You're leading a discussion and want people to feel safe speaking up, disagreeing, or admitting confusion.",
     "used to create a safe, open atmosphere where people feel comfortable speaking up or disagreeing",
     [
        ("There are no bad questions here — if it's unclear to you, it's probably unclear to others too.", "There are no bad questions here — if it's unclear to you, it's probably unclear to others too, so just ask."),
        ("Feel free to jump in anytime — this works better as a conversation than a monologue.", "Feel free to jump in anytime — this works better as a conversation than a monologue, so interrupt me if needed."),
        ("I might be wrong on this, so push back if something doesn't land.", "I might be wrong on this, so push back if something doesn't land — I'd rather know now than after launch."),
        ("What am I missing? I'd genuinely rather hear it now.", "What am I missing? I'd genuinely rather hear it now than find out after we've shipped it."),
        ("No pressure to have the answer right now — just thinking out loud together.", "No pressure to have the answer right now — just thinking out loud together to see where this goes."),
        ("Thanks for being candid — that's exactly the kind of input I was hoping for.", "Thanks for being candid — that's exactly the kind of input I was hoping for on the pricing proposal."),
        ("Let's make this a safe space to disagree.", "Let's make this a safe space to disagree — I want to hear the counterarguments before we decide."),
     ]),
    ("Active Listening",
     "The other person just shared something important, and you want to show them you genuinely understood and value what they said.",
     "used to show the other person you've genuinely understood and value what they said",
     [
        ("Let me make sure I've got this right — you're saying that...", "Let me make sure I've got this right — you're saying that the delay started with the vendor, not our team?"),
        ("So if I'm hearing you correctly, the core concern is...", "So if I'm hearing you correctly, the core concern is that the new process adds too many approval steps?"),
        ("That's a really good point — I hadn't thought about it that way.", "That's a really good point — I hadn't thought about it that way. It changes how I'd approach the rollout."),
        ("Say more about that — I want to understand where you're coming from.", "Say more about that — I want to understand where you're coming from on the timeline concern."),
        ("What I'm hearing underneath that is... — am I close?", "What I'm hearing underneath that is you're worried about team morale, not just the deadline — am I close?"),
        ("Before I respond, I want to make sure I've fully understood you.", "Before I respond, I want to make sure I've fully understood you — can you repeat the last part?"),
        ("That makes sense. And what would you want to see happen instead?", "That makes sense. And what would you want to see happen instead of the current review process?"),
     ]),
    ("Influencing Without Authority",
     "You need someone who doesn't report to you to prioritize your request, and you have to persuade rather than instruct them.",
     "used to get cooperation from someone who doesn't report to you, through persuasion rather than authority",
     [
        ("I could really use your expertise on this — you know this system better than anyone.", "I could really use your expertise on this — you know this system better than anyone on the team."),
        ("This is your call, but here's what I'm seeing from my side.", "This is your call, but here's what I'm seeing from my side: the current schema will block next quarter's feature."),
        ("How can I make this easier for you?", "How can I make this easier for you — would a shared doc with the requirements help?"),
        ("If we solve this together, it makes both our lives easier down the line.", "If we solve this together, it makes both our lives easier down the line, once the integration goes live."),
        ("I'm not trying to add to your plate — I'm trying to save us both a headache later.", "I'm not trying to add to your plate — I'm trying to save us both a headache later when the audit comes around."),
        ("What would it take to get this on your radar?", "What would it take to get this on your radar before the end of the sprint?"),
        ("I'll own the coordination if you can own the technical call — deal?", "I'll own the coordination if you can own the technical call on the migration — deal?"),
        ("You've got more context here than I do — where do you think this should land?", "You've got more context here than I do — where do you think this ticket should land, engineering or design?"),
     ]),
    ("Managing Up",
     "You're updating your manager or a senior stakeholder and want to bring solutions, not just problems, and help them decide quickly.",
     "used when updating a manager or senior stakeholder — leads with solutions, not just problems, and helps them decide fast",
     [
        ("Here's the situation, here's my recommendation, and here's what I need from you.", "Here's the situation, here's my recommendation, and here's what I need from you: sign-off by Friday."),
        ("I want to flag this early rather than surprise you later.", "I want to flag this early rather than surprise you later — the launch date is at risk."),
        ("Two options — I'm leaning towards the first, but wanted your read.", "Two options — I'm leaning towards the first, but wanted your read before I commit to a vendor."),
        ("I don't need you to solve this, I just need a quick steer on direction.", "I don't need you to solve this, I just need a quick steer on direction — build it in-house or buy the tool?"),
        ("This is going well — here's the one thing I'd want your help unblocking.", "This is going well — here's the one thing I'd want your help unblocking: legal's review is stuck."),
        ("Just so you're not caught off guard in the meeting: here's the headline.", "Just so you're not caught off guard in the meeting: here's the headline — we're going to miss the Q3 target."),
        ("What's the best way for me to keep you updated on this without over-communicating?", "What's the best way for me to keep you updated on this without over-communicating — weekly email, or just flag exceptions?"),
     ]),
    ("Facilitating & Synthesizing a Discussion",
     "You're facilitating a meeting where multiple viewpoints are on the table, and you want to pull the threads together and make sure quieter voices are heard.",
     "used by a facilitator to pull ideas together, draw out quieter voices, and land on a shared conclusion",
     [
        ("Let me pull the threads together — it sounds like we're converging on...", "Let me pull the threads together — it sounds like we're converging on a phased rollout instead of a big-bang launch."),
        ("I want to make sure we hear from everyone — [name], you've been quiet, what's your take?", "I want to make sure we hear from everyone — Linh, you've been quiet, what's your take on the pricing model?"),
        ("Let's capture that and keep moving — we can go deeper offline.", "Let's capture that and keep moving — we can go deeper offline on the API design specifics."),
        ("We've got two competing views on the table — let me summarize both fairly.", "We've got two competing views on the table — let me summarize both fairly before we vote."),
        ("Building on what [name] just said...", "Building on what Marcus just said, I think we should test both options with a small user group first."),
        ("So where does that leave us? Let me play back what I think we've agreed.", "So where does that leave us? Let me play back what I think we've agreed: we ship the MVP by month-end."),
        ("Great discussion — let's land the plane. What's the one decision we're making?", "Great discussion — let's land the plane. What's the one decision we're making before we leave this room?"),
     ]),
    ("Networking & Warm Relationship-Building",
     "You're reaching out to someone in your professional network to reconnect or build the relationship, with no immediate work request attached.",
     "used to reconnect with a professional contact and build the relationship, without any transactional ask",
     [
        ("I've been meaning to reach out — I really enjoyed your talk on [topic].", "I've been meaning to reach out — I really enjoyed your talk on remote team culture at the conference."),
        ("No agenda, just wanted to catch up and see how things are going on your end.", "No agenda, just wanted to catch up and see how things are going on your end since you switched teams."),
        ("I thought of you when I saw this — figured it might be useful.", "I thought of you when I saw this — figured it might be useful for the hiring project you mentioned."),
        ("It's been too long — we should grab a coffee sometime soon.", "It's been too long — we should grab a coffee sometime soon, maybe next week?"),
        ("I'd love to pick your brain on something whenever you have a spare fifteen minutes.", "I'd love to pick your brain on something whenever you have a spare fifteen minutes — no rush at all."),
        ("Congratulations on the new role — really well deserved.", "Congratulations on the new role — really well deserved after everything you did on the platform migration."),
        ("Let's stay in touch — I have a feeling our paths will cross again.", "Let's stay in touch — I have a feeling our paths will cross again, especially if you move into product."),
     ]),
    ("Calm, Confident Everyday Presence",
     "You're put on the spot in a small, everyday moment — an unexpected question or a mistake — and want to respond with calm, confident presence instead of over-explaining or apologizing.",
     "used to respond to small everyday moments — questions, mistakes, pushback — with calm, confident presence instead of over-explaining",
     [
        ("Let me think about that for a moment.", "Let me think about that for a moment — comfortable with the pause instead of filling it with 'um'."),
        ("Good question. I don't know — but I'll find out.", "Good question. I don't know — but I'll find out and get back to you by end of day."),
        ("I'd rather get it right than get it fast.", "I'd rather get it right than get it fast — I'll take the extra day if you can spare it."),
        ("Let's not overcomplicate this.", "Let's not overcomplicate this — a simple spreadsheet will do for now."),
        ("I hear you. Here's where I land.", "I hear you. Here's where I land: we ship the smaller fix this week and revisit the bigger one next sprint."),
        ("That's fair. I've changed my mind.", "That's fair. I've changed my mind — your point about onboarding friction convinced me."),
        ("When you have a moment, could you...?", "When you have a moment, could you take a look at the deck before tomorrow's review?"),
        ("What questions do you have?", "What questions do you have? I want to make sure this is actually clear, not just quiet agreement."),
        ("I'd suggest we...", "I'd suggest we run a two-week pilot before rolling this out to the whole team."),
     ]),
]

if __name__ == "__main__":
    generate_topic(
        out_path=OUT_PATH,
        exam_id="collaboration-levels",
        title="Chunk Atlas — Situations: Collaboration Across Levels",
        tier_id=TIER_ID,
        tier_name=TIER_NAME,
        groups_def=groups_def,
    )
