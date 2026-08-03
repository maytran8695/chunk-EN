import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from lib import generate_topic

OUT_PATH = os.path.join(SCRIPT_DIR, "..", "data", "discourse-markers.json")

# Phrase content below is copied by hand from the "Discourse & Pragmatic
# Markers" topic (tier "mastery" / nav tab "Language Systems") — sections
# M3.1-M3.5 and L3.6-L3.7.
#
# Source lines already group near-synonymous markers with " / " separators
# (e.g. "So, ... / Now, ... / Right, ... / OK so..."), which were split
# into individual (phrase, example) tuples per the task spec. Several
# headers bundle multiple distinct pragmatic functions in one "h", so they
# are split into finer sub-groups, the same principle as the H14 split in
# generate_core_patterns.py.
# L3.6 ("kho marker cực thông dụng") and L3.7 (register-graded fillers)
# heavily duplicate M3.1-M3.5 (e.g. "Right./So./Well./Anyway./Look." repeats
# M3.1 almost verbatim) — those exact duplicates were skipped. Only the
# genuinely new items from L3.6 were kept, either folded into the closest
# matching M3.x group (e.g. "Honestly" added to the stance-framing group)
# or, where they named a function not covered elsewhere, given their own
# new group (buying thinking time, adding a point, expressing disbelief,
# segueing to a related topic). L3.7's three register tiers (informal /
# neutral / formal fillers) were kept as three separate small groups
# because the whole point of that section is that they are NOT
# interchangeable — that register mismatch is exactly what the quiz
# engine's random distractors from other groups will test.
# The "[Name], you've worked on this" templated item and the pure
# backchannel "Mm-hm." (too minimal to quiz as a standalone chunk) were
# skipped.
TIER_ID = "mastery"
TIER_NAME = "Language Systems"

groups_def = [
    ("Starting to speak, or buying a second to think",
     "You've just been asked a question in a meeting and need a natural way to start speaking while you gather your thoughts.",
     "used to open a turn or briefly stall for a second before answering, without an awkward silent pause",
     [
        ("Well, ...", "Well, I think it depends on which region we're talking about."),
        ("So, ...", "So, where should we start — the budget or the timeline?"),
        ("Now, ...", "Now, let's look at what actually caused the delay."),
        ("Right, ...", "Right, let's get into the numbers then."),
        ("OK so...", "OK so, the first thing to flag is the vendor issue."),
        ("Let me see.", "Let me see... I think we shipped that fix on the 12th."),
        ("Hang on.", "Hang on, let me pull up the actual figures before I answer."),
        ("Give me a sec.", "Give me a sec, I want to check the ticket before I commit to a date."),
        ("How can I put this.", "How can I put this — it's not quite ready, but it's close."),
     ]),
    ("Returning to the main topic after a digression",
     "The conversation has drifted off-topic and you want to naturally pull it back to what you were originally discussing.",
     "used to signal a return to the main topic after a side comment or tangent",
     [
        ("Anyway, ...", "Anyway, back to the budget — where were we?"),
        ("Anyhow, ...", "Anyhow, the point is we still need a decision by Friday."),
        ("In any case, ...", "In any case, the deadline hasn't moved, so let's focus on that."),
     ]),
    ("Signalling the core point or an obstacle",
     "You're about to say the one thing that really matters in this situation, and want to flag that clearly first.",
     "used to signal you're about to state the real point, or the real obstacle, behind a situation",
     [
        ("The thing is, ...", "The thing is, we never actually tested this with real users."),
        ("Here's the thing, ...", "Here's the thing — legal hasn't signed off yet."),
     ]),
    ("Formal transition to the next part",
     "You're wrapping up one part of a presentation and want a natural, professional way to move to the next.",
     "used for a more formal, deliberate shift from one part of a talk or discussion to the next",
     [
        ("Moving on, ...", "Moving on, let's look at what this means for next quarter."),
        ("That said, ...", "That said, I think we should still proceed with the pilot."),
        ("With that in mind, ...", "With that in mind, here's what I'd suggest we do next."),
     ]),
    ("Inserting a quick side point",
     "You want to slip in a small but relevant piece of extra information without derailing the main conversation.",
     "used to insert a short, related side point without derailing the main conversation",
     [
        ("Just quickly, ...", "Just quickly, the client also asked about pricing tiers."),
        ("Before I forget, ...", "Before I forget, HR needs your timesheet by Friday."),
        ("While we're on the subject, ...", "While we're on the subject, did we ever fix that login bug?"),
        ("Speaking of which, ...", "Speaking of which, has anyone heard back from the vendor?"),
        ("That reminds me, ...", "That reminds me, we still owe the client a follow-up email."),
        ("While I remember, ...", "While I remember, can you send me that spreadsheet later?"),
     ]),
    ("Correcting or restating what you just said",
     "You've just said something imprecise and want to immediately correct it more accurately.",
     "used to immediately correct or narrow down something you just said",
     [
        ("I mean, ...", "It's broken — I mean, it's technically working, just really slow."),
        ("That is, ...", "We need sign-off from the owner, that is, whoever's leading the account now."),
        ("Or rather, ...", "The launch is delayed — or rather, postponed until the fix is verified."),
     ]),
    ("Rephrasing in different words",
     "The listener seems confused, and you want to explain the same idea again in a different way.",
     "used to restate an idea in different words after the listener seemed confused",
     [
        ("What I'm trying to say is...", "What I'm trying to say is, we need more time, not more people."),
        ("Let me put it another way.", "Let me put it another way: it's not a bug, it's a design limitation."),
        ("Let me rephrase that.", "Let me rephrase that — I meant next Friday, not this one."),
     ]),
    ("Summarizing or simplifying what you said",
     "You've made a fairly complex point and want to boil it down to one simple sentence.",
     "used to boil a longer explanation down to its simplest form",
     [
        ("in other words", "In other words, we're over budget and behind schedule."),
        ("to put it simply", "To put it simply, the fix works, but it's slow."),
        ("simply put", "Simply put, we can't ship without more testing."),
        ("essentially", "Essentially, the two systems were never talking to each other."),
        ("in a nutshell", "In a nutshell, we lost the client over pricing, not the product."),
     ]),
    ("Cutting to the short version",
     "You've been asked what happened and don't want to go through every detail — just the outcome.",
     "used to skip the details and jump straight to the outcome of a longer story",
     [
        ("basically", "Basically, the vendor missed the deadline and we had no backup."),
        ("long story short", "Long story short, we had to rebuild the integration from scratch."),
        ("to cut a long story short", "To cut a long story short, we ended up switching providers."),
     ]),
    ("Approximating a word choice",
     "You're reaching for a word that isn't quite exact and want to flag that you're speaking loosely.",
     "used to signal that a word choice is approximate rather than exact",
     [
        ("if you like", "It's a workaround, if you like, rather than a real fix."),
        ("so to speak", "He's the unofficial team lead, so to speak."),
        ("for want of a better word", "The launch was, for want of a better word, chaotic."),
     ]),
    ("Assuming shared understanding and engaging the listener",
     "You're explaining something and want to draw the listener in, checking they're following along with you.",
     "used to draw the listener in and check they share your assumption or are following along",
     [
        ("you know", "It's one of those weeks, you know, where nothing goes to plan."),
        ("you see", "The issue, you see, is that the two teams use different tools."),
        ("look", "Look, we can't keep pushing this deadline."),
        ("listen", "Listen, I really think we should talk to the client before deciding."),
     ]),
    ("Softening a claim as approximate, not exact",
     "You want to describe a plan as roughly on track without committing to an exact, absolute claim.",
     "used to soften a statement, making it approximate rather than an absolute claim",
     [
        ("sort of", "We're sort of on track, but the last two tickets are risky."),
        ("kind of", "It's kind of a workaround more than a real solution."),
        ("in a way", "In a way, the delay actually gave us time to fix the bigger bug."),
        ("to some degree", "The rollout succeeded, to some degree, though adoption is slow."),
        ("a bit", "The estimate was a bit optimistic, to be honest."),
        ("more or less", "The numbers are more or less what we expected."),
     ]),
    ("Leaving room for correction or generous interpretation",
     "You're not fully sure you're right and want to leave room for the listener to correct you.",
     "used to leave room for the listener to correct you, or invite them to interpret generously",
     [
        ("if that makes sense", "We need to decouple the two services, if that makes sense."),
        ("if I'm being honest", "If I'm being honest, I don't think we tested this enough."),
        ("I don't know if...", "I don't know if this is the right call, but I'd delay the launch."),
        ("correct me if I'm wrong, but...", "Correct me if I'm wrong, but didn't we already try this fix?"),
     ]),
    ("Framing your honest stance before speaking",
     "You're about to say something a bit blunt and want to flag upfront that you're being straightforward.",
     "used to signal you're about to speak candidly, without dressing up the opinion",
     [
        ("to be honest", "To be honest, I don't think the new design is an improvement."),
        ("to be fair", "To be fair, the team did warn us this timeline was tight."),
        ("frankly", "Frankly, the pricing page needs a complete rewrite."),
        ("candidly", "Candidly, I don't think we're ready to launch this week."),
        ("honestly", "Honestly, I was surprised the demo went as smoothly as it did."),
     ]),
    ("Introducing a mildly surprising fact",
     "You want to introduce a fact that slightly contradicts what people assumed, without making a big deal of it.",
     "used to introduce information that's mildly surprising or gently corrects an assumption",
     [
        ("actually", "Actually, the client asked for this change themselves."),
        ("as it happens", "As it happens, we already have a draft of that document."),
        ("in fact", "In fact, the older version performed better in testing."),
     ]),
    ("Flagging something interesting or unusual",
     "You've noticed something a bit odd or coincidental and want to point it out to the listener.",
     "used to flag that something is a bit odd, coincidental, or noteworthy",
     [
        ("funnily enough", "Funnily enough, the same bug showed up in last year's release too."),
        ("oddly enough", "Oddly enough, traffic actually went up during the outage."),
        ("interestingly", "Interestingly, the churn rate dropped right after the price increase."),
     ]),
    ("Conceding a point before continuing",
     "You want to acknowledge something true about the other side's argument before pushing your own point.",
     "used to acknowledge a valid point, or partially agree, before adding a qualification or your own view",
     [
        ("admittedly", "Admittedly, the old process was slower, but it caught more errors."),
        ("granted", "Granted, the budget is tight, but this really can't wait."),
        ("true", "True, the timeline is aggressive, but the team's done it before."),
        ("mind you", "The client's happy, mind you they haven't seen the invoice yet."),
        ("I'll give you that.", "The new dashboard is faster — I'll give you that."),
        ("Point taken.", "Point taken — we probably should have tested on mobile first."),
     ]),
    ("Stating the obvious",
     "You want to point out something that should already be clear to everyone in the room.",
     "used to flag something as self-evident, though it can sound condescending if overused",
     [
        ("needless to say", "Needless to say, we won't be using that vendor again."),
        ("obviously", "Obviously, we'll need sign-off before this goes live."),
        ("clearly", "Clearly, the current process isn't scaling with the team's growth."),
     ]),
    ("Holding the floor when interrupted",
     "Someone tries to jump in while you're still mid-point, and you want to politely keep talking.",
     "used to politely keep the floor and finish your point when someone tries to interrupt",
     [
        ("Just to finish my thought...", "Just to finish my thought — the second issue is actually more urgent."),
        ("If I could just finish...", "If I could just finish, I think this connects to the budget question too."),
        ("Bear with me, I'm getting to that.", "Bear with me, I'm getting to that — it's the next slide."),
     ]),
    ("Asking to jump into the conversation",
     "Someone else is talking and you want to politely interrupt to add something.",
     "used to politely ask for a turn to speak while someone else is talking",
     [
        ("Can I jump in here?", "Can I jump in here? I think there's a simpler option."),
        ("Sorry to interrupt, but...", "Sorry to interrupt, but the client's actually on the call already."),
        ("If I may...", "If I may, I'd like to add some context on the budget."),
        ("Just to add to that...", "Just to add to that, we also saw the same issue in QA."),
     ]),
    ("Handing the floor to someone else",
     "You've finished making your point and want to invite someone else to share their perspective.",
     "used to hand the conversation over to someone else and invite their input",
     [
        ("What do you think?", "What do you think — does this timeline work for your team?"),
        ("Over to you.", "That's everything from my side — over to you."),
        ("I'd be interested in your take.", "I'd be interested in your take on the pricing change."),
     ]),
    ("Backchanneling agreement while listening",
     "Someone else is speaking and you want to show, in a word or two, that you're following and agree.",
     "used as a short verbal signal while listening, to show agreement or that you're following along",
     [
        ("Exactly.", "\"So the real issue is staffing, not budget.\" \"Exactly.\""),
        ("Fair enough.", "\"We just don't have the headcount right now.\" \"Fair enough.\""),
        ("Good point.", "\"We should test this on slower connections too.\" \"Good point.\""),
        ("That's true.", "\"Nobody actually reads the release notes.\" \"That's true.\""),
        ("Right, right.", "\"...and that's why the numbers looked off.\" \"Right, right.\""),
     ]),
    ("Adding another point",
     "You've made one point and want to naturally tack on another one without sounding repetitive.",
     "used to add another point to what you or someone else just said",
     [
        ("Also, ...", "Also, we still haven't heard back from the design team."),
        ("Plus, ...", "Plus, the new plan is actually cheaper for most customers."),
        ("On top of that, ...", "On top of that, the vendor raised their prices again."),
        ("And another thing, ...", "And another thing — the ticket queue is a mess right now."),
        ("Not to mention, ...", "Not to mention, the client already extended us once."),
     ]),
    ("Pivoting to a contrasting point",
     "You've just made one point and want to add a second thought that pulls slightly against it.",
     "used to add a thought that pulls slightly against what was just said",
     [
        ("Then again, ...", "It's risky — then again, doing nothing is riskier."),
        ("Having said that, ...", "Having said that, I don't think we should rush the fix."),
     ]),
    ("Expressing disbelief casually",
     "Someone just told you something you find hard to believe, and you want a natural way to push back on it.",
     "used casually to express disbelief or mild pushback at what someone just said",
     [
        ("I mean, really?", "They want another extension? I mean, really?"),
        ("Seriously though.", "Seriously though, has anyone actually tested this on mobile?"),
        ("Come on.", "Come on, we both know that estimate was never realistic."),
        ("Surely not.", "They're delaying it again? Surely not."),
     ]),
    ("Casual, informal register filler",
     "You're chatting informally with a close colleague and want a filler word that matches that relaxed tone.",
     "used in casual, informal conversation among friends or close colleagues — sounds out of place in a formal meeting",
     [
        ("like", "It was, like, the worst demo we've ever given."),
        ("kinda", "The plan's kinda falling apart, to be honest."),
        ("dunno", "I dunno, maybe we just push the launch."),
        ("whatever", "Whatever works for the team, honestly."),
     ]),
    ("Neutral register filler",
     "You're speaking in a fairly ordinary, everyday tone — not too casual, not too formal — and need a filler that matches.",
     "used in ordinary, everyday spoken register — neither noticeably casual nor formal",
     [
        ("I suppose", "I suppose we could try the smaller vendor instead."),
        ("I guess", "I guess we'll find out once the numbers come in."),
     ]),
    ("Formal register filler",
     "You're speaking in a formal or high-stakes setting, like a board meeting, and need a filler that matches that register.",
     "used in formal or high-stakes spoken register — sounds stiff or out of place in casual conversation",
     [
        ("as it were", "The team became, as it were, the client's de facto support desk."),
        ("if you will", "It's a soft launch, if you will, before the full rollout."),
        ("in a sense", "In a sense, the delay worked in our favor."),
     ]),
]

if __name__ == "__main__":
    generate_topic(
        out_path=OUT_PATH,
        exam_id="discourse-markers",
        title="Chunk Atlas — Language Systems: Discourse & Pragmatic Markers",
        tier_id=TIER_ID,
        tier_name=TIER_NAME,
        groups_def=groups_def,
    )
