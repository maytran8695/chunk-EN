import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from lib import generate_topic

OUT_PATH = os.path.join(SCRIPT_DIR, "..", "data", "under-fire.json")

# Phrase content below is copied by hand from the "Under Fire: Pressure
# Situations" topic (tier "fluency" / F11) in the source content set —
# sections F11.1-F11.6. F10.7 is a supplementary "kho" (repository) list
# that mostly repeats F11.1-F11.6 verbatim; only its NEW, non-duplicate
# phrasings were folded into the matching functional group below (e.g.
# "I'd have to look." into group 2, "Can I come back to you?" into group 1,
# "Can I have a moment?" into group 5).
TIER_ID = "fluency"
TIER_NAME = "Real-Time Fluency"

groups_def = [
    ("Admitting you don't know, with a next step",
     "You've just been asked a direct question you genuinely don't know the answer to, in front of others.",
     "used to admit you don't know something confidently, while committing to a next step",
     [
        ("I don't know — but I'll find out and come back to you by [time].", "I don't know — but I'll find out and come back to you by end of day."),
        ("Honestly, that's outside what I know. [Name] would be the person to ask.", "Honestly, that's outside what I know. Minh would be the person to ask."),
        ("I don't want to guess and give you the wrong answer.", "I don't want to guess and give you the wrong answer — let me check the logs first."),
        ("I don't have that off the top of my head. Can I follow up this afternoon?", "I don't have that off the top of my head. Can I follow up this afternoon?"),
        ("Good question — I should know that, and I don't. Let me check.", "Good question — I should know that, and I don't. Let me check and get back to you."),
        ("Can I come back to you?", "Can I come back to you on the exact figure? I don't want to misquote it."),
     ]),
    ("Buying structured thinking time when put on the spot",
     "You've been put on the spot with a question you weren't prepared for and need a moment to think without going silent.",
     "used to buy structured thinking time out loud, right after being put on the spot",
     [
        ("Off the top of my head...", "Off the top of my head, I'd say we're around 80% done, but let me confirm."),
        ("Without having looked at it recently...", "Without having looked at it recently, I believe the contract renews in March."),
        ("Let me think out loud for a second.", "Let me think out loud for a second — there are a couple of ways to approach this."),
        ("I'll give you my instinct, and I'll verify it after.", "I'll give you my instinct, and I'll verify it after: I think it's a data issue, not a code issue."),
        ("There are two ways to answer that.", "There are two ways to answer that — depends on whether you mean this sprint or this quarter."),
        ("Can I have thirty seconds on that?", "Can I have thirty seconds on that? I want to give you an accurate number."),
        ("Can you come back to me at the end?", "Can you come back to me at the end? I'd like to check something first."),
        ("I'd rather give you a considered answer than a fast one.", "I'd rather give you a considered answer than a fast one — give me a moment."),
        ("I'd have to look.", "I'd have to look — I don't want to quote the wrong version number."),
     ]),
    ("Handling multiple questions at once",
     "Someone just fired off several questions at once and you need to answer them in an organized way.",
     "used to organize your response when someone asks several questions at once",
     [
        ("There are three questions there. Let me take them one at a time.", "There are three questions there. Let me take them one at a time, starting with the budget."),
        ("Let me start with the last one, because it's the most important.", "Let me start with the last one, because it's the most important: yes, we can hit the date."),
        ("Can I park the second question and come back to it?", "Can I park the second question and come back to it once I've answered the first?"),
        ("Remind me of the second part after I answer this one.", "Remind me of the second part after I answer this one — I don't want to lose it."),
        ("Which of those matters most to you? I'll start there.", "Which of those matters most to you? I'll start there and work through the rest."),
     ]),
    ("Defusing a loaded or hostile question",
     "Someone just asked you a loaded or hostile question that has a shaky assumption baked into it.",
     "used to calmly defuse a loaded or hostile question instead of getting defensive",
     [
        ("That question assumes [X] — I'd challenge that first.", "That question assumes we already agreed on scope — I'd challenge that first."),
        ("I think the more useful question is...", "I think the more useful question is whether we have the resources, not whether we should try."),
        ("I wouldn't frame it that way. Here's how I'd put it.", "I wouldn't frame it that way. Here's how I'd put it: it's a trade-off, not a failure."),
        ("Can you be more specific about what concerns you?", "Can you be more specific about what concerns you? I want to address it directly."),
        ("That's a fair challenge. Let me address it directly.", "That's a fair challenge. Let me address it directly instead of dancing around it."),
        ("I hear the frustration. Let's look at the facts.", "I hear the frustration. Let's look at the facts before we decide anything."),
     ]),
    ("Steadying your nerves out loud",
     "You can feel your nerves creeping into your voice and want to acknowledge it instead of pretending it's not happening.",
     "used to acknowledge nerves out loud instead of pretending they're not there",
     [
        ("Bear with me, I'm a bit nervous — this matters to me.", "Bear with me, I'm a bit nervous — this presentation matters to me."),
        ("Give me a second to gather my thoughts.", "Give me a second to gather my thoughts before I answer that."),
        ("Let me take that from the top.", "Let me take that from the top — I don't think I explained it well."),
        ("Can I have a moment?", "Can I have a moment? I want to answer this properly."),
     ]),
    ("Holding the floor when talked over",
     "Someone keeps talking over you and you need to hold onto your turn without losing your temper.",
     "used to hold onto your turn when someone talks over you",
     [
        ("Can I just finish this thought?", "Can I just finish this thought? I'm almost at the point."),
        ("Let me finish this point.", "Let me finish this point, then I'll hand it over to you."),
        ("Hang on — I'm almost there.", "Hang on — I'm almost there, one more sentence."),
        ("One second, let me land this.", "One second, let me land this before we move on."),
        ("Good point — let me finish and I'll come to it.", "Good point — let me finish and I'll come to it right after."),
        ("Coming back to what I was saying...", "Coming back to what I was saying, before we got interrupted."),
        ("You cut me off earlier — my point was...", "You cut me off earlier — my point was that the timeline is unrealistic."),
        ("I'd like to finish.", "I'd like to finish, if that's okay — I'm nearly done."),
        ("I haven't had a chance to finish.", "I haven't had a chance to finish — can I get one more minute?"),
     ]),
]

if __name__ == "__main__":
    generate_topic(
        out_path=OUT_PATH,
        exam_id="under-fire",
        title="Chunk Atlas — Real-Time Fluency: Under Fire",
        tier_id=TIER_ID,
        tier_name=TIER_NAME,
        groups_def=groups_def,
    )
