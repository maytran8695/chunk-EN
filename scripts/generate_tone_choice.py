import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from lib import generate_topic

OUT_PATH = os.path.join(SCRIPT_DIR, "..", "data", "tone-choice.json")

# Phrase content copied by hand from the "Tone Choice: Fall, Rise, Fall-Rise"
# topic (tier "presence" / nav tab "Voice & Presence") — sections P2.1-P2.4,
# V2.5. Each header bundles several distinct grammatical functions of a
# given pitch direction (e.g. Fall covers statements, Wh-questions, and
# commands), so each is split into finer single-function groups, mirroring
# the reference script's H14 split.
TIER_ID = "presence"
TIER_NAME = "Voice & Presence"

groups_def = [
    ("Falling tone: statements",
     "You're stating something as settled and certain, not open for debate.",
     "used with a falling tone to state something as settled and certain",
     [
        ("That's the decision.↘",
         'Should we revisit this next week?" — "That\'s the decision.↘ We\'re moving on.'),
        ("We're going with option A.↘",
         'So which vendor did we pick?" — "We\'re going with option A.↘'),
     ]),
    ("Falling tone: Wh- questions",
     "You're asking a straightforward Wh- question and want to sound neutral and native, not tentative.",
     "used to show that Wh- questions normally fall in pitch, unlike Yes/No questions",
     [
        ("What time is it?↘",
         'What time is it?↘" she asked, pitch falling naturally at the end, not rising like a Yes/No question.'),
     ]),
    ("Falling tone: instructions",
     "You're giving a direct, matter-of-fact instruction.",
     "used with a falling tone to give a direct, matter-of-fact instruction",
     [
        ("Close the door.↘",
         "Close the door.↘ It's freezing in here."),
        ("Send it today.↘",
         "Send it today.↘ Don't wait for sign-off."),
     ]),
    ("Rising tone: Yes/No questions",
     "You're asking a Yes/No question or making a casual invitation, and want to sound genuinely open, not certain.",
     "used with a rising tone for Yes/No questions and casual invitations",
     [
        ("Are you coming?↗",
         'Are you coming?↗" she asked, pitch rising to invite a real answer.'),
        ("Does that make sense?↗",
         'Does that make sense?↗" he checked, before moving to the next slide.'),
        ("Coffee?↗",
         'Coffee?↗" she offered, rising to make it a genuine invitation.'),
     ]),
    ("Rising tone: lists & confirming",
     "You're listing several items, or repeating a single word back to confirm you heard it right.",
     "used with a rising tone to list unfinished items, or to repeat a word back for confirmation",
     [
        ("We need budget↗, people↗, and time↘.",
         'We need budget↗, people↗, and time↘." — the first two items rise to show more is coming, the last falls to close the list.'),
        ("Tuesday?↗",
         'So we\'re meeting Tuesday?↗" she repeated, rising to check she\'d heard right.'),
     ]),
    ("Rise-fall tone: reactions",
     "You want to react to news with a tone that can land as genuinely impressed or as sarcastic, depending on your face and the situation.",
     "used with a rise-fall tone for a reaction that can be impressed or sarcastic depending on context",
     [
        ("Oh really↗↘.",
         'We closed the deal." — "Oh really↗↘." (said with raised eyebrows, genuinely impressed).'),
     ]),
    ("Uptalk (statements rising)",
     "You want to recognize the habit of letting a plain statement rise at the end, as if asking permission — and know it can undercut your credibility in formal meetings.",
     "used to illustrate uptalk — rising pitch on a statement, which can sound like the speaker is seeking approval",
     [
        ("So I finished the report?↗",
         'So I finished the report?↗" said in a client meeting, made the update sound like a request for permission rather than a fact.'),
     ]),
    ("Falling tone: statements (extra)",
     "You want more practice recognizing a falling tone used for flat, certain statements.",
     "used with a falling tone for a flat, certain statement — practice example",
     [
        ("That's decided.",
         'Can we still change the venue?" — "That\'s decided.↘ We\'re not reopening it.'),
        ("We're doing it.",
         'Are we really launching Friday?" — "We\'re doing it.↘ No more delays.'),
        ("No.",
         'Can we push the deadline again?" — "No.↘" — flat, final, no room for negotiation.'),
     ]),
    ("Falling tone: Wh- questions (extra)",
     "You're asking a quick Wh- question and want the pitch to fall, as native speakers do by default.",
     "used with a falling tone for a quick Wh- question — practice example",
     [
        ("What time?",
         'The call got moved." — "What time?↘" — pitch falls, as Wh- questions normally do.'),
        ("Who's leading?",
         'We need someone on point for this." — "Who\'s leading?↘'),
        ("Why now?",
         'They want the report by Friday." — "Why now?↘ We just sent one last week.'),
     ]),
    ("Rising tone: Yes/No (extra)",
     "You're asking a quick Yes/No question or casual invitation and want the pitch to rise.",
     "used with a rising tone for a Yes/No question or casual invitation — practice example",
     [
        ("Are we ready?",
         'Are we ready?↗" he asked before opening the call to the client.'),
        ("Does that work?",
         "I've moved the meeting to 3pm — does that work?↗"),
        ("Coffee?",
         'Coffee?↗" he asked, holding up the pot before the meeting started.'),
     ]),
    ("Rising tone: confirming (extra)",
     "You're repeating back a word or short phrase just to confirm you heard it correctly.",
     "used with a rising tone to repeat something back and confirm you heard it right",
     [
        ("Tuesday?",
         'Let\'s confirm for Tuesday?↗" she said, rising to double-check the date.'),
        ("You mean now?",
         'We need this today." — "You mean now?↗" — rising in surprise, seeking confirmation.'),
     ]),
    ("Fall-rise: reservation",
     "You want to signal polite reservation — partial agreement with something left unsaid — without stating your objection outright.",
     "used with a fall-rise tone to signal polite reservation: agreement with something left unsaid",
     [
        ("I like it...↘↗",
         'What do you think of the design?" — "I like it...↘↗" (meaning: but something\'s still bothering me).'),
        ("It's possible...↘↗",
         'Can we hit Friday?" — "It\'s possible...↘↗" (meaning: but unlikely).'),
        ("Well...↘↗",
         'So we\'re all agreed?" — "Well...↘↗" (meaning: not quite — there\'s a but coming).'),
        ("I could do that...↘↗",
         'Could you take this on too?" — "I could do that...↘↗" (meaning: reluctantly, or with conditions).'),
     ]),
    ("Fall-rise: hinting more",
     "You're partly agreeing, but signaling with a fall-rise tone that there's more to say — maybe a better option or a catch.",
     "used with a fall-rise tone to partly agree while hinting there's more (a better option, or a catch)",
     [
        ("That's one way of looking at it.↘↗",
         'So it\'s settled, right?" — "That\'s one way of looking at it.↘↗" (meaning: I see a better option).'),
        ("He's good...↘↗",
         'Should we put him on the client account?" — "He\'s good...↘↗" — hinting at an unspoken concern.'),
     ]),
    ("Rising list, falling close",
     "You're listing several items and want to signal you're not finished until the last one, which falls.",
     "used to keep items in a list rising until the final item, which falls to signal the list is complete",
     [
        ("budget↗, people↗, and time↘",
         'What do we need to hit this deadline?" — "We need budget↗, people↗, and time↘." — rising through the list, falling only on the last item.'),
     ]),
]

if __name__ == "__main__":
    generate_topic(
        out_path=OUT_PATH,
        exam_id="tone-choice",
        title="Chunk Atlas — Voice & Presence: Tone Choice",
        tier_id=TIER_ID,
        tier_name=TIER_NAME,
        groups_def=groups_def,
    )
