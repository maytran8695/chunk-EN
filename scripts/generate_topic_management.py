import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from lib import generate_topic

OUT_PATH = os.path.join(SCRIPT_DIR, "..", "data", "topic-management.json")

# Phrase content below is copied by hand from the "Topic Management" topic
# (tier "fluency" / F6) in the source content set — sections F6.1-F6.5.
# F6.2 is split into 4 finer sub-groups (bridging / acknowledging /
# returning / introducing) since it bundles distinct functions, mirroring
# how generate_core_patterns.py split H14. F6.5 is a supplementary
# "kho" (repository) list that mostly repeats F6.1-F6.4 verbatim; only its
# NEW, non-duplicate phrasings were folded into the matching group below.
TIER_ID = "fluency"
TIER_NAME = "Real-Time Fluency"

groups_def = [
    ("Opening with someone you know",
     "You're catching up with a colleague you already know and need a natural way to start.",
     "used to open a conversation naturally with someone you already know",
     [
        ("How's your week going?", "Hey, how's your week going? I heard it's been chaotic with the release."),
        ("Busy day?", "Busy day? You look like you haven't stopped since nine."),
        ("How's the [project] going?", "How's the migration project going? Did you get the sign-off yet?"),
        ("It's been a while!", "It's been a while! Last time I saw you was at the offsite."),
        ("Long time no see.", "Long time no see — did you switch teams or something?"),
        ("How have you been?", "How have you been? I feel like I haven't seen you since the reorg."),
        ("How did that thing with [X] turn out?", "How did that thing with the client escalation turn out? You were pretty stressed about it last time."),
        ("Hey, how's it going?", "Hey, how's it going? Grab a coffee before the standup?"),
        ("Alright?", "Alright? Saw you were buried in tickets yesterday."),
        ("Long time!", "Long time! Were you on leave or just hiding from meetings?"),
     ]),
    ("Opening with strangers or new people",
     "You're striking up a conversation with someone you've never met — at an event, in a queue, or on a new team.",
     "used to start a conversation with someone you don't know yet",
     [
        ("Is this seat taken?", "Is this seat taken? Mind if I join you for lunch?"),
        ("Have you been to one of these before?", "Have you been to one of these before? It's my first company all-hands."),
        ("Hi, I'm [name].", "Hi, I'm Linh — I just joined the design team last week."),
        ("Mind if I join?", "Mind if I join? I don't know anyone else at this table yet."),
        ("Is this seat free?", "Is this seat free? Everywhere else looks full."),
     ]),
    ("Opening a call or a meeting",
     "You're starting a call or meeting and need a quick line before getting into the actual topic.",
     "used to open a call or meeting with a quick check-in before the real topic starts",
     [
        ("Hey, can you hear me okay?", "Hey, can you hear me okay? Your audio was cutting out earlier."),
        ("How's things on your end?", "How's things on your end — is the connection stable today?"),
        ("Morning all.", "Morning all, hope everyone survived the Monday traffic."),
        ("Right, shall we?", "Right, shall we? Looks like everyone's here now."),
        ("Are we all here?", "Are we all here, or are we still waiting on marketing?"),
        ("Hi, is now still okay?", "Hi, is now still okay, or did the earlier meeting run over?"),
        ("Have you got five minutes?", "Have you got five minutes? I want to run something by you before the call."),
     ]),
    ("Bridging into a new topic",
     "You want to move the conversation to a related topic without switching subject abruptly.",
     "used to move to a related topic smoothly instead of switching abruptly",
     [
        ("That reminds me...", "That reminds me — did you ever hear back from the vendor?"),
        ("Speaking of which...", "Speaking of which, have you seen the new dashboard yet?"),
        ("On that note...", "On that note, I should probably loop in the QA lead too."),
     ]),
    ("Acknowledging you're changing the subject",
     "You want to openly signal you're moving to a different topic, rather than switching without warning.",
     "used to openly signal you're switching topics, instead of cutting away without warning",
     [
        ("Anyway — how about you?", "Anyway — how about you? How's the new apartment coming along?"),
        ("Right, shall we get to the agenda?", "Right, shall we get to the agenda? We've caught up enough for now."),
        ("Anyway, tell me about...", "Anyway, tell me about the interview — how did it go?"),
     ]),
    ("Returning to a topic you left",
     "You got sidetracked and now want to pick the earlier topic back up.",
     "used to pick a topic back up after you got sidetracked",
     [
        ("Sorry, back to what you were saying...", "Sorry, back to what you were saying about the budget cut — what happened next?"),
        ("You were telling me about...", "You were telling me about the new hire before we got interrupted."),
     ]),
    ("Introducing a new topic before you forget",
     "You suddenly remember something you want to bring up before the conversation moves on.",
     "used to bring up something new before it slips your mind",
     [
        ("Oh, before I forget —...", "Oh, before I forget — can you send me that spreadsheet later?"),
        ("Actually, while I have you...", "Actually, while I have you, can I ask about the leave request I sent?"),
     ]),
    ("Digging deeper into what someone said",
     "Someone gave you a short answer and you want to draw out more detail and show real interest.",
     "used to draw out more detail from a short answer and show genuine interest",
     [
        ("What are you working on that you're actually excited about?", "Instead of the usual \"how's work,\" I asked, \"What are you working on that you're actually excited about?\""),
        ("You mentioned [X] earlier — how did that come about?", "You mentioned a possible move to Da Nang earlier — how did that come about?"),
        ("What drew you to that?", "You picked UX over engineering — what drew you to that?"),
        ("What made you go that route?", "You went freelance instead of staying in-house — what made you go that route?"),
        ("I'll be honest, I found that hard at first. How about you?", "I'll be honest, I found presenting to leadership hard at first. How about you?"),
        ("Tell me more about...", "Tell me more about the trip — where did you end up going in the end?"),
        ("What made you decide that?", "You decided to switch companies right before the bonus — what made you decide that?"),
        ("How so?", "You said the new manager changed everything — how so?"),
        ("What happened then?", "So the client pushed back on the price — what happened then?"),
        ("And how did that feel?", "You finally shipped it after six months of work — and how did that feel?"),
     ]),
    ("Signaling the conversation is winding down",
     "You want to hint that the conversation is coming to a close, before you actually excuse yourself.",
     "used to signal a conversation is winding down, before you actually excuse yourself",
     [
        ("Anyway...", "Anyway... I should probably let you get back to your desk."),
        ("Right...", "Right... I think that covers everything for now."),
        ("So yeah...", "So yeah... that's pretty much where things stand."),
     ]),
    ("Giving a reason to leave",
     "You need to end the conversation and want to give a polite reason for stepping away.",
     "used to give a polite reason for ending a conversation and stepping away",
     [
        ("I'd better let you go.", "I'd better let you go — I know you've got that call in five minutes."),
        ("I should get back to it.", "I should get back to it, I've still got two tickets to close before EOD."),
        ("I won't keep you.", "I won't keep you — I know it's a busy day for the whole team."),
     ]),
    ("Promising to reconnect",
     "You're wrapping up a conversation and want to leave the door open for next time.",
     "used to end a conversation by leaving the door open for next time",
     [
        ("Let's catch up soon.", "Let's catch up soon — maybe grab lunch once things calm down."),
        ("See you Thursday.", "See you Thursday at the retro, then."),
        ("Talk soon.", "Talk soon — text me once you hear back from HR."),
        ("Speak soon.", "Speak soon — good luck with the interview tomorrow."),
     ]),
    ("Saying goodbye",
     "You're closing out a conversation and need a friendly final line.",
     "used as a friendly final line when closing out a conversation",
     [
        ("Take care.", "Take care, and say hi to the team for me."),
        ("Have a good one.", "Have a good one — enjoy the long weekend."),
        ("Cheers.", "Cheers, thanks again for the help earlier."),
        ("Bye for now.", "Bye for now, I'll ping you once the deploy's done."),
     ]),
    ("Politely exiting a group conversation",
     "You're at a group conversation or event and want to move on to talk to other people without being rude.",
     "used to leave a group conversation politely, without seeming rude",
     [
        ("It was lovely to chat — I'm going to grab another coffee.", "It was lovely to chat — I'm going to grab another coffee before the next session starts."),
        ("Lovely to meet you — I'm going to say hello to a few people.", "Lovely to meet you — I'm going to say hello to a few people before the room empties out."),
     ]),
]

if __name__ == "__main__":
    generate_topic(
        out_path=OUT_PATH,
        exam_id="topic-management",
        title="Chunk Atlas — Real-Time Fluency: Topic Management",
        tier_id=TIER_ID,
        tier_name=TIER_NAME,
        groups_def=groups_def,
    )
