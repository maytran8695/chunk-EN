import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from lib import generate_topic

OUT_PATH = os.path.join(SCRIPT_DIR, "..", "data", "adjacency-pairs.json")

# Phrase content below is copied by hand from the "Adjacency Pairs &
# Preference Design" topic (tier "fluency" / F4) in the source content set.
# F4.1 is skipped entirely: it's the "dispreferred = delay + soften +
# reason" principle itself plus comparison blocks, with no standalone
# quotable chunk. F4.5 (the source's "common pairs" bonus bank) bundles
# many unrelated prompt/response functions (small talk, thanks, greetings,
# congrats, permission, requests) and is split into five sub-groups
# accordingly; phrasings that exactly duplicate an earlier section were
# folded rather than repeated. Example sentences are written as short
# prompt -> response exchanges since these chunks only make sense as the
# second half of a conversational pair.
TIER_ID = "fluency"
TIER_NAME = "Real-Time Fluency"

groups_def = [
    ("Standard Adjacency-Pair Responses (Preferred vs. Dispreferred)",
     "Someone just made an invitation, assessment, suggestion, or compliment, and you need a natural second half of the exchange.",
     "used as the natural second half of a common conversational pair (invitation, assessment, suggestion, or compliment)",
     [
        ("Yeah, love to.", "\"Fancy lunch?\" \"Yeah, love to.\""),
        ("I'd love to, but I've got...", "\"Fancy lunch?\" \"I'd love to, but I've got a call at twelve.\""),
        ("Rain check?", "\"Fancy lunch?\" \"I can't today — rain check?\""),
        ("Wasn't it?", "\"That was a great session.\" \"Wasn't it? Really useful.\""),
        ("Yeah... I mean, parts of it were.", "\"That was great.\" \"Yeah... I mean, parts of it were. I wasn't sure about the ending.\""),
        ("Good idea.", "\"Shall we park this?\" \"Good idea.\""),
        ("Thanks — the team did the heavy lifting.", "\"Great work.\" \"Thanks — the team did the heavy lifting.\""),
     ]),
    ("Pre-Expansion — Clearing the Way First",
     "You're about to ask for a favor, make an invitation, or raise something difficult, and want to check the moment is right first.",
     "used to check the moment is right before asking a favor, making an invitation, or raising something difficult",
     [
        ("Are you busy?", "Are you busy? I wanted to ask you about the report."),
        ("Have you got a sec?", "Have you got a sec? I need a quick favor."),
        ("Is now a good time?", "Is now a good time, or should I come back later?"),
        ("What are you doing Friday?", "What are you doing Friday? A few of us are getting dinner."),
        ("Any plans this weekend?", "Any plans this weekend? We're thinking of a team hike."),
        ("Have you got a minute?", "Have you got a minute? There's something I need to tell you."),
        ("Are you sitting down?", "Are you sitting down? I've got some bad news about the budget."),
        ("Can I ask you something?", "Can I ask you something — has anyone else mentioned the layoffs?"),
        ("Do you mind if I ask...?", "Do you mind if I ask... why the project got cancelled?"),
     ]),
    ("Repair Sequences — Catching Misunderstandings",
     "You realize something you said (or heard) got misunderstood, and need to repair it before it snowballs.",
     "used to catch and repair a misunderstanding before it snowballs",
     [
        ("Sorry, that came out wrong.", "Sorry, that came out wrong — I didn't mean to blame your team."),
        ("I don't think I said that clearly.", "I don't think I said that clearly, let me try again."),
        ("No no, I meant...", "No no, I meant next Friday, not this Friday."),
        ("That's not quite what I meant.", "That's not quite what I meant — I wasn't criticizing the design."),
        ("Let me clarify.", "Let me clarify — this only affects the EU customers."),
        ("Just so I understand — you're saying...?", "Just so I understand — you're saying we should pause the whole project?"),
        ("I think we're talking past each other.", "I think we're talking past each other on this budget question."),
        ("Can we reset?", "Can we reset? I don't think either of us is getting through."),
     ]),
    ("Small Talk Openers — Responding",
     "Someone opens with casual small talk and you need a natural, quick response.",
     "used as a quick, natural reply to casual small talk",
     [
        ("Good thanks, you?", "\"How are you?\" \"Good thanks, you?\""),
        ("Not bad, yourself?", "\"How are you?\" \"Not bad, yourself?\""),
        ("Yeah, all good.", "\"How are you?\" \"Yeah, all good.\""),
        ("Lovely, thanks — too short though.", "\"How was your holiday?\" \"Lovely, thanks — too short though.\""),
     ]),
    ("Responding to Thanks & Apologies",
     "Someone just thanked you or apologized to you, and you need a natural response.",
     "used as a natural response to being thanked or apologized to",
     [
        ("No problem.", "\"Thanks so much.\" \"No problem.\""),
        ("Any time.", "\"Thanks so much for covering my shift.\" \"Any time.\""),
        ("You're welcome.", "\"Thanks so much.\" \"You're welcome.\""),
        ("Not at all.", "\"Thanks so much for the help.\" \"Not at all.\""),
        ("My pleasure.", "\"Thanks so much.\" \"My pleasure.\""),
        ("No worries.", "\"Sorry about that.\" \"No worries.\""),
        ("Don't worry about it.", "\"Sorry about that.\" \"Don't worry about it.\""),
        ("These things happen.", "\"Sorry about that.\" \"These things happen.\""),
        ("All good.", "\"Sorry about that.\" \"All good.\""),
     ]),
    ("Meeting & Parting Exchanges",
     "Someone just greeted you for the first time or wished you a good weekend, and you need the natural reply.",
     "used as the natural second half of a greeting or parting exchange",
     [
        ("You too.", "\"Nice to meet you.\" \"You too.\""),
        ("And you.", "\"Nice to meet you.\" \"And you.\""),
        ("Likewise.", "\"Nice to meet you.\" \"Likewise.\""),
        ("You too!", "\"Have a good weekend.\" \"You too!\""),
        ("Thanks, you as well.", "\"Have a good weekend.\" \"Thanks, you as well.\""),
        ("Cheers, you too.", "\"Have a good weekend.\" \"Cheers, you too.\""),
     ]),
    ("Responding to News — Congrats, Luck & Sympathy",
     "Someone just congratulated you, wished you luck, or expressed sympathy, and you need a natural reply.",
     "used as a natural reply to congratulations, well-wishes, or sympathy",
     [
        ("Thank you!", "\"Congratulations!\" \"Thank you!\""),
        ("Thanks — I'm pleased.", "\"Congratulations on the promotion!\" \"Thanks — I'm pleased.\""),
        ("Cheers!", "\"Congratulations!\" \"Cheers!\""),
        ("Thanks, I'll need it!", "\"Good luck with the presentation!\" \"Thanks, I'll need it!\""),
        ("Cheers.", "\"Good luck!\" \"Cheers.\""),
        ("Thanks, that's kind of you.", "\"I'm so sorry to hear that.\" \"Thanks, that's kind of you.\""),
     ]),
    ("Agreeing to Requests & Suggestions",
     "Someone just asked permission, made a request, or suggested doing something, and you need to agree naturally.",
     "used to naturally agree to a permission request, a favor, or a suggestion",
     [
        ("Go ahead.", "\"Do you mind if I sit here?\" \"Go ahead.\""),
        ("Please do.", "\"Do you mind if I take notes?\" \"Please do.\""),
        ("Be my guest.", "\"Do you mind if I use your charger?\" \"Be my guest.\""),
        ("Of course.", "\"Could you send me the file?\" \"Of course.\""),
        ("Sure thing.", "\"Could you close the door?\" \"Sure thing.\""),
        ("Yeah, no problem.", "\"Could you forward that email?\" \"Yeah, no problem.\""),
        ("Leave it with me.", "\"Could you look into the invoice issue?\" \"Leave it with me.\""),
        ("Let's do it.", "\"Shall we move the meeting to Monday?\" \"Let's do it.\""),
        ("Why not.", "\"Shall we try the new format this time?\" \"Why not.\""),
     ]),
    ("Refusing Gracefully — Delay, Soften, Give a Reason",
     "You need to decline an invitation or request, but a flat \"no\" would sound rude — you need the full softened version.",
     "used to decline an invitation or request politely, with hesitation, regret, and a reason built in",
     [
        ("Ah, I'd love to, but I've got something on. Another time?", "\"Drinks after work?\" \"Ah, I'd love to, but I've got something on. Another time?\""),
        ("That's really kind — I can't this time, unfortunately.", "\"Want to join the team trip?\" \"That's really kind — I can't this time, unfortunately.\""),
        ("Oh, I wish I could. I'm completely swamped this week.", "\"Can you help me review the deck?\" \"Oh, I wish I could. I'm completely swamped this week.\""),
        ("Hmm, that's tricky for me. Could we do...", "\"Can we meet at 8am?\" \"Hmm, that's tricky for me. Could we do 9 instead?\""),
        ("I don't think I can commit to that, sorry. What I could do is...", "\"Can you lead the whole project?\" \"I don't think I can commit to that, sorry. What I could do is help part-time.\""),
        ("Let me be honest — that doesn't work for me. Here's why.", "\"Can we push the deadline to you?\" \"Let me be honest — that doesn't work for me. Here's why.\""),
        ("Can I be really annoying and say no?", "\"So you're in for Saturday?\" \"Can I be really annoying and say no?\""),
     ]),
]

if __name__ == "__main__":
    generate_topic(
        out_path=OUT_PATH,
        exam_id="adjacency-pairs",
        title="Chunk Atlas — Real-Time Fluency: Adjacency Pairs & Preference Design",
        tier_id=TIER_ID,
        tier_name=TIER_NAME,
        groups_def=groups_def,
    )
