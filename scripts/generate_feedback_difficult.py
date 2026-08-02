import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from lib import generate_topic

OUT_PATH = os.path.join(SCRIPT_DIR, "..", "data", "feedback-difficult.json")

# Phrase content below is copied by hand from the "Feedback & Difficult
# Conversations" topic (tier "core" / nav tab "Situations") — sections
# P1-P8. Each header already represents a single coherent communicative
# function, so no further splitting was needed (unlike Core Patterns' H14).
TIER_ID = "core"
TIER_NAME = "Situations"

groups_def = [
    ("Giving Feedback to Peers or Reports",
     "You need to give constructive feedback to a peer or someone you manage, and want to do it directly but supportively.",
     "used to give direct, supportive feedback to a peer or direct report, focused on behavior not the person",
     [
        ("Can I share some feedback? I think it'll help.", "Can I share some feedback? I think it'll help before you send the deck to the client."),
        ("Here's what worked really well... and here's one thing I'd do differently next time.", "Here's what worked really well — the data visuals — and here's one thing I'd do differently next time: shorten the intro."),
        ("This is about the work, not about you — you're doing great overall.", "This is about the work, not about you — you're doing great overall, I just want to flag one section."),
        ("I noticed [specific behavior]. What was going on there?", "I noticed you skipped the code review on Tuesday's release. What was going on there?"),
        ("The impact on the team was [X] — I don't think that was your intention, but I wanted you to know.", "The impact on the team was two late nights fixing the bug — I don't think that was your intention, but I wanted you to know."),
        ("What would help you get there? Let's figure it out together.", "What would help you get there? Let's figure it out together — maybe pairing with Sam on the next ticket."),
        ("I'm telling you this because I know you can handle it and I want you to grow.", "I'm telling you this because I know you can handle it and I want you to grow into the lead role."),
     ]),
    ("Giving Feedback Upward",
     "You need to give feedback to your manager or someone senior to you, and want to do it respectfully, framed around impact.",
     "used to give feedback to someone senior — asks permission first and frames it around impact, not criticism",
     [
        ("Can I offer a perspective? You might not have visibility into this from where you sit.", "Can I offer a perspective? You might not have visibility into this from where you sit, since you're not in the daily standups."),
        ("I might be missing context, but from the team's side, here's how this landed.", "I might be missing context, but from the team's side, here's how this landed: people felt blindsided by the new deadline."),
        ("This is just my read, and you may have reasons I'm not aware of, but...", "This is just my read, and you may have reasons I'm not aware of, but the reorg announcement felt rushed."),
        ("Would it be helpful if I shared what I'm hearing on the ground?", "Would it be helpful if I shared what I'm hearing on the ground about the new expense policy?"),
        ("I want to raise something — not to criticize, but because I think it affects the outcome you care about.", "I want to raise something — not to criticize, but because I think it affects the outcome you care about: customer retention."),
        ("When [X] happened, the effect was [Y] — I wanted to flag it in case it's useful.", "When the meeting got moved twice last week, the effect was two missed deadlines — I wanted to flag it in case it's useful."),
     ]),
    ("Receiving Feedback Gracefully",
     "Someone just gave you critical feedback, and you want to respond with openness instead of getting defensive.",
     "used to respond to critical feedback with openness and curiosity instead of defensiveness",
     [
        ("Thank you for telling me — I'd rather know than not know.", "Thank you for telling me — I'd rather know than not know, even if it's hard to hear."),
        ("That's fair. Let me sit with that.", "That's fair. Let me sit with that for a day before I respond properly."),
        ("Can you give me a specific example so I can understand it better?", "Can you give me a specific example so I can understand it better — which meeting did this happen in?"),
        ("I appreciate the honesty — that couldn't have been easy to say.", "I appreciate the honesty — that couldn't have been easy to say, especially in front of the team."),
        ("You're right, and I'm going to work on that.", "You're right, and I'm going to work on that — I'll slow down before jumping to conclusions in reviews."),
        ("Help me understand — what would 'better' look like to you?", "Help me understand — what would 'better' look like to you for the next status update?"),
        ("I hadn't seen it that way. Thanks for the perspective.", "I hadn't seen it that way. Thanks for the perspective — it changes how I'll approach the next release."),
     ]),
    ("Delivering Bad News",
     "You have to tell someone difficult news — a delay, a failure, a setback — and want to be direct and give them context and next steps right away.",
     "used to deliver difficult news directly and early, with context and next steps, instead of burying it",
     [
        ("I've got some difficult news, and I want to be straight with you about it.", "I've got some difficult news, and I want to be straight with you about it: we're going to miss the launch date."),
        ("This isn't the update I was hoping to give, but here's where we are.", "This isn't the update I was hoping to give, but here's where we are: the vendor pulled out of the contract."),
        ("Let me give you the headline first, then the context: [bad news]. Here's what we're doing about it.", "Let me give you the headline first, then the context: we lost the client. Here's what we're doing about it."),
        ("I take responsibility for this. Here's my plan to fix it.", "I take responsibility for this. Here's my plan to fix it: I'll personally review every ticket before it ships this week."),
        ("I know this is frustrating. It's frustrating for me too — let's talk through options.", "I know this is frustrating. It's frustrating for me too — let's talk through options for recovering the timeline."),
        ("I'd rather tell you now while we still have time to react.", "I'd rather tell you now while we still have time to react than wait until it's too late to fix."),
        ("Here's what I can commit to, and here's what I can't promise yet.", "Here's what I can commit to, and here's what I can't promise yet: the fix by Friday, but not full test coverage."),
     ]),
    ("Disagreeing Without Damaging the Relationship",
     "You disagree with someone on a substantive issue and want to push back on the idea without it feeling like an attack on them personally.",
     "used to disagree with an idea firmly while making clear it's not personal",
     [
        ("I see it differently, and I think that's actually useful here — let me explain.", "I see it differently, and I think that's actually useful here — let me explain why I'd keep the feature simple."),
        ("I respect that view. Here's where I land and why.", "I respect that view. Here's where I land and why: I still think we need a second reviewer on this change."),
        ("We might just have to disagree on this one, and that's okay.", "We might just have to disagree on this one, and that's okay — let's just make sure the decision-maker knows both sides."),
        ("I'm pushing on this because I think it matters, not because I'm against you.", "I'm pushing on this because I think it matters, not because I'm against you — the data retention policy affects every team."),
        ("Can I offer a counterpoint — not to shoot it down, but to stress-test it?", "Can I offer a counterpoint — not to shoot it down, but to stress-test it before we present to the board?"),
        ("I want the same outcome you do; I just see a different path to it.", "I want the same outcome you do; I just see a different path to it — I'd rather build in-house than buy the license."),
        ("Let's argue this out now so we don't have to redo it later.", "Let's argue this out now so we don't have to redo it later, once the architecture is already locked in."),
     ]),
    ("Saying No Gracefully",
     "Someone is asking you to take on something you can't or shouldn't say yes to, and you want to decline clearly but kindly.",
     "used to decline a request clearly and kindly, without over-apologizing or leaving false hope",
     [
        ("I'd love to help, but I can't take this on without dropping something else — which should it be?", "I'd love to help, but I can't take this on without dropping something else — which should it be, the audit or the migration?"),
        ("The honest answer is no, and here's why.", "The honest answer is no, and here's why: we don't have the headcount to support a second product line right now."),
        ("I'm going to pass on this one, but here's who might be a better fit.", "I'm going to pass on this one, but here's who might be a better fit — Priya has more bandwidth this month."),
        ("Not right now — but let's revisit this next quarter.", "Not right now — but let's revisit this next quarter once the migration is behind us."),
        ("I want to say yes, but I'd be overpromising, and I'd rather be reliable.", "I want to say yes, but I'd be overpromising, and I'd rather be reliable than take on a deadline I can't hit."),
        ("That doesn't work for me, but here's what I can do instead.", "That doesn't work for me, but here's what I can do instead: a shorter version by Friday, not the full report."),
        ("I appreciate you thinking of me. This time I'll have to decline.", "I appreciate you thinking of me. This time I'll have to decline — my plate is already full through the end of the sprint."),
     ]),
    ("Repairing After Friction",
     "There was some tension or a bad exchange with a colleague recently, and you want to proactively repair the relationship.",
     "used to proactively repair a relationship after tension or a bad exchange",
     [
        ("I've been thinking about how that conversation went, and I don't think I handled it well.", "I've been thinking about how that conversation went, and I don't think I handled it well — I cut you off a few times."),
        ("I owe you an apology — I was short with you earlier, and that wasn't fair.", "I owe you an apology — I was short with you earlier, and that wasn't fair, I was just stressed about the deadline."),
        ("Can we reset? I value working with you and I don't want that to get lost.", "Can we reset? I value working with you and I don't want that to get lost over one bad meeting."),
        ("I think we got off on the wrong foot — can we start over?", "I think we got off on the wrong foot — can we start over on this project, properly this time?"),
        ("I hear that I upset you, and that wasn't my intention. Can we talk it through?", "I hear that I upset you, and that wasn't my intention. Can we talk it through over coffee this week?"),
        ("No hard feelings on my end — I hope none on yours either.", "No hard feelings on my end — I hope none on yours either, it was a tough call either way."),
        ("We're on the same team here. Let's not let this drive a wedge.", "We're on the same team here. Let's not let this drive a wedge between engineering and design."),
     ]),
    ("Navigating Tension in the Moment",
     "A discussion is getting heated right now, and you want to de-escalate it before it damages the conversation or the relationship.",
     "used to de-escalate a heated discussion in the moment, before it damages the conversation",
     [
        ("Let's take a breath — I don't think we're as far apart as it feels right now.", "Let's take a breath — I don't think we're as far apart as it feels right now, we both want the launch to succeed."),
        ("I can feel this getting heated. Can we slow down for a second?", "I can feel this getting heated. Can we slow down for a second and go back to the actual numbers?"),
        ("I don't want to win this argument, I want to solve the problem.", "I don't want to win this argument, I want to solve the problem — can we focus on that instead?"),
        ("Help me understand why this matters so much to you — I think I'm missing something.", "Help me understand why this matters so much to you — I think I'm missing something about the timeline risk."),
        ("Let's park the emotion for a moment and look at the facts together.", "Let's park the emotion for a moment and look at the facts together: what did the test data actually show?"),
        ("I might have said that badly. Let me try again.", "I might have said that badly. Let me try again — I didn't mean it to come across as blaming you."),
        ("Can we agree to disagree on the 'how' and align on the 'what'?", "Can we agree to disagree on the 'how' and align on the 'what' — we both want this shipped by Friday."),
     ]),
]

if __name__ == "__main__":
    generate_topic(
        out_path=OUT_PATH,
        exam_id="feedback-difficult",
        title="Chunk Atlas — Situations: Feedback & Difficult Conversations",
        tier_id=TIER_ID,
        tier_name=TIER_NAME,
        groups_def=groups_def,
    )
