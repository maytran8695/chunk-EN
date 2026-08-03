import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from lib import generate_topic

OUT_PATH = os.path.join(SCRIPT_DIR, "..", "data", "emotional-attunement.json")

# Phrase content below is copied by hand from the "Emotional Attunement"
# topic (tier "presence" / nav tab "Voice & Presence") in final_topics.json,
# sections P8.1-P8.4, P8.6, V8.7.
#
# P8.5 ("Nguyên tắc cuối cùng") is skipped entirely: it's a closing set of
# aphorisms about communication philosophy addressed to the learner
# ("people forget what you said, they remember how you made them feel"),
# not chunks you'd say to a counterpart the way every other group here
# works.
# P8.3 ("Đọc phòng") is mostly behavioural-cue description (silence, glancing
# at a watch, curt one-word replies) with nothing sayable — only the two
# "Câu nói phù hợp" / "Chỉnh hướng" lines are actual quotable chunks, so
# only those made it into the group.
# P8.1 and P8.2 are each one header -> one group (labelling / validate-
# before-solving), since P8.6 ("kho câu đồng cảm & ấm áp") is a grab-bag
# whose items are explicitly labelled by the SAME functions ("Gọi tên" =
# labelling, "Công nhận"/"Đồng hành"/"Hỏi trước khi giải" = validate-then-
# solve) — those were folded into P8.1/P8.2, dropping any line that was a
# near-duplicate of a phrase already present (e.g. P8.6's "I'm with you."
# vs. P8.2's existing "I'm with you on that.").
# P8.6's two remaining items with no earlier home ("Ghi nhận" = acknowledging
# vulnerability, "Theo dõi sau" = following up later) became their own new
# small groups, and its "Sau tin xấu" line ("I'm sorry — that's really
# hard.") was folded into the sad/hard-news group built from V8.7.
# V8.7 ("kho câu cho tình huống cảm xúc") bundles 8 emotion-specific
# categories (sad, anxious, angry, happy, failure, unwell, loss, at a loss
# for words) — each is a genuinely distinct trigger situation, so each
# became its own small group, mirroring how bundled headers are split
# elsewhere (e.g. H14 in Core Patterns). V8.7's "at a loss for words" item
# duplicates P8.6's own version almost verbatim; only V8.7's was kept.
TIER_ID = "presence"
TIER_NAME = "Voice & Presence"

groups_def = [
    ("Labelling someone's emotion",
     "You can tell from someone's tone or body language that they're upset, even though their words sound fine, and you want to gently name what you're picking up on.",
     "used to gently name the emotion you're picking up on in someone else, without diagnosing or dismissing it",
     [
        ("It sounds like this has been frustrating.", "It sounds like this has been frustrating — you've raised it three times now."),
        ("It seems like you're under a lot of pressure.", "It seems like you're under a lot of pressure with the deadline moved up."),
        ("It looks like this matters a lot to you.", "It looks like this matters a lot to you — want to talk it through?"),
        ("I get the sense you're not convinced.", "I get the sense you're not convinced — what's holding you back?"),
        ("You seem hesitant — am I reading that right?", "You seem hesitant — am I reading that right, or is it just me?"),
        ("That must have been difficult.", "That must have been difficult, having to deliver that news yourself."),
        ("I imagine that wasn't easy.", "I imagine that wasn't easy, especially with everyone watching."),
        ("It sounds like...", "It sounds like you're still waiting to hear back — is that right?"),
        ("It seems like...", "It seems like the timing caught everyone off guard."),
     ]),
    ("Validating before solving",
     "A colleague is venting about a problem, and before jumping to a fix, you want to show them you actually heard what they said.",
     "used to acknowledge someone's reaction as reasonable before offering any solution",
     [
        ("That's a fair reaction.", "That's a fair reaction, honestly — I'd be annoyed too."),
        ("I'd feel the same in your position.", "I'd feel the same in your position, given how late the update came."),
        ("That makes sense given what you've been dealing with.", "That makes sense given what you've been dealing with these past few weeks."),
        ("I hear you.", "I hear you — that's the third time this month it's happened."),
        ("I'm with you on that.", "I'm with you on that, the process really does need fixing."),
        ("Do you want me to help fix it, or do you just want to vent?", "Do you want me to help fix it, or do you just want to vent for a minute?"),
        ("That's completely fair.", "That's completely fair — you did flag this risk weeks ago."),
        ("Of course you are.", "You're annoyed? Of course you are, nobody told you in time."),
        ("You're not wrong to feel that.", "You're not wrong to feel that — the deadline really was unrealistic."),
        ("What would help right now?", "What would help right now — a shoulder to cry on or an action plan?"),
     ]),
    ("Reading the room",
     "The room's gone quiet or people seem hesitant after your proposal, and you want to check in rather than just plough ahead.",
     "used to check in when you sense unspoken hesitation or discomfort in a group",
     [
        ("I'm sensing some hesitation.", "I'm sensing some hesitation — is now not the right time to push this?"),
        ("I feel like there's something unsaid.", "I feel like there's something unsaid here — anyone want to jump in?"),
        ("Is now a bad time?", "Is now a bad time? We can pick this up tomorrow instead."),
        ("Let me pause here — where is everyone on this?", "Let me pause here — where is everyone on this? I want to hear the room."),
     ]),
    ("Deliberate warmth",
     "You want to show a colleague you actually remember and care about their life outside work, not just default small talk.",
     "used to show deliberate, specific warmth rather than a generic check-in",
     [
        ("How did your daughter's recital go?", "How did your daughter's recital go? You'd mentioned it last week."),
        ("Did you get that issue with the landlord sorted?", "Did you get that issue with the landlord sorted in the end?"),
        ("The point you made about X last week really stuck with me.", "The point you made about onboarding last week really stuck with me."),
        ("Thanks for making time — I know how full your week is.", "Thanks for making time for this — I know how full your week is."),
        ("How are you doing — actually?", "How are you doing — actually? Not the meeting-status version."),
        ("No rush at all — take the time you need.", "No rush at all — take the time you need, we'll cover for you."),
        ("Thinking of you.", "Just wanted to say I'm thinking of you this week."),
        ("That was [name]'s idea, credit where it's due.", "That was Priya's idea, credit where it's due — she spotted it first."),
     ]),
    ("Responding when someone's sad or shares hard news",
     "A colleague just told you something upsetting or shared some hard personal news.",
     "used to respond to someone sharing sad news or a hard moment",
     [
        ("I'm really sorry.", "I'm really sorry — that's a lot to deal with all at once."),
        ("That's awful.", "That's awful, I had no idea it had gotten that bad."),
        ("Do you want to talk about it?", "Do you want to talk about it, or would you rather just get on with the day?"),
        ("I'm sorry — that's really hard.", "I'm sorry — that's really hard. Let me know what you need from me."),
     ]),
    ("Responding when someone's anxious",
     "A colleague is clearly worried about something coming up and needs a response that doesn't brush it off.",
     "used to respond to someone who's anxious or worried about something",
     [
        ("That sounds stressful.", "That sounds stressful, juggling both launches in the same week."),
        ("What's the worst case?", "What's the worst case here — walk me through it."),
        ("How can I help?", "How can I help — do you need another pair of hands before Friday?"),
     ]),
    ("Responding when someone's angry",
     "A colleague is clearly angry about something that happened, and you want to respond without dismissing it.",
     "used to respond to someone who's angry, without dismissing the feeling",
     [
        ("I'd be annoyed too.", "I'd be annoyed too if they changed the requirements this late."),
        ("That's not on.", "That's not on — you should have been told before the announcement went out."),
        ("You've every right to be.", "You've every right to be upset, that email was out of line."),
     ]),
    ("Responding when someone's happy",
     "A colleague just shared good news and you want your reaction to actually match their excitement.",
     "used to respond warmly to someone sharing good news",
     [
        ("That's brilliant!", "That's brilliant! You've been working towards this for months."),
        ("I'm so pleased for you.", "I'm so pleased for you — you completely deserve it."),
        ("You must be delighted.", "You must be delighted, that's a huge win for the team."),
     ]),
    ("Responding to someone's setback or failure",
     "A colleague's project or attempt just didn't work out, and you want to respond in a way that doesn't pile on.",
     "used to respond to someone's setback or failed attempt without piling on",
     [
        ("These things happen.", "These things happen — the numbers looked solid going in."),
        ("You gave it a proper go.", "You gave it a proper go, nobody could say you didn't try."),
        ("Onwards.", "Onwards — let's see what we can salvage for next quarter."),
     ]),
    ("Responding when someone's unwell",
     "A colleague tells you they're sick or heading off unwell.",
     "used to respond to a colleague who's unwell",
     [
        ("Get well soon.", "Get well soon — don't worry about the deck, I've got it covered."),
        ("Don't rush back.", "Don't rush back, we'll manage until you're properly better."),
        ("Look after yourself.", "Look after yourself, the inbox can wait."),
     ]),
    ("Responding to loss",
     "A colleague has just told you about a death in their family or a significant personal loss.",
     "used to respond to someone dealing with a death or significant loss",
     [
        ("I'm so sorry for your loss.", "I'm so sorry for your loss — take whatever time you need."),
        ("I'm thinking of you.", "I'm thinking of you, and the whole team is too."),
        ("There are no words.", "There are no words, I just wanted you to know I'm here."),
     ]),
    ("When you don't know what to say",
     "Someone has just shared something heavy and you genuinely don't have the right words, but staying silent feels worse.",
     "used when you genuinely don't know what to say but don't want to stay silent",
     [
        ("I don't know what to say.", "I don't know what to say, honestly — that's really tough."),
        ("I'm just glad you told me.", "I'm just glad you told me, I want to know when things are hard for you."),
     ]),
    ("Acknowledging vulnerability",
     "A colleague just told you something personal that clearly wasn't easy for them to bring up.",
     "used to acknowledge that what someone just shared took courage to say",
     [
        ("That can't have been easy to say.", "That can't have been easy to say, thank you for telling me."),
        ("Thanks for trusting me with that.", "Thanks for trusting me with that — it stays between us."),
     ]),
    ("Following up after a hard conversation",
     "It's been a few days since a colleague shared something difficult, and you want to check back in rather than let it drop.",
     "used to follow up after a difficult conversation, days or weeks later",
     [
        ("I've been thinking about what you said.", "I've been thinking about what you said last week — how are you holding up?"),
        ("How are things now?", "How are things now? You mentioned it had been a rough patch."),
     ]),
]

if __name__ == "__main__":
    generate_topic(
        out_path=OUT_PATH,
        exam_id="emotional-attunement",
        title="Chunk Atlas — Voice & Presence: Emotional Attunement",
        tier_id=TIER_ID,
        tier_name=TIER_NAME,
        groups_def=groups_def,
    )
