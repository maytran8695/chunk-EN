import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from lib import generate_topic

OUT_PATH = os.path.join(SCRIPT_DIR, "..", "data", "response-tokens.json")

# Phrase content below is copied by hand from the "Response Tokens &
# Active Listenership" topic (tier "fluency" / F5) in the source content
# set. F5.3, F5.5, and F5.6 are each the source's own "bank" sections that
# bundle several distinct listener-response functions (positive
# assessments vs. sympathy vs. surprise/agreement; different flavors of
# newsmarkers and realization tokens; reacting to a happy/boasting speaker
# vs. an angry one vs. a worried/apologetic one), so each is split into
# finer sub-groups. Phrasings that exactly duplicate an earlier section
# (down to punctuation, e.g. "Right." vs "Right, right.") were folded
# rather than repeated. Example sentences are written as short exchanges,
# since these tokens only make sense as a listener's reaction to something
# just said.
TIER_ID = "fluency"
TIER_NAME = "Real-Time Fluency"

groups_def = [
    ("Continuers — Keeping the Channel Open",
     "You're listening to someone talk and want to signal you're following along, without taking the turn yourself.",
     "used while listening to signal you're following along, without taking the turn",
     [
        ("Mm-hm.", "\"...and then the client called back at five.\" \"Mm-hm.\" \"...saying they wanted a full refund.\""),
        ("Uh-huh.", "\"So first we tried the old server...\" \"Uh-huh.\" \"...and that didn't fix it either.\""),
        ("Yeah.", "\"We looked at three vendors...\" \"Yeah.\" \"...and none of them could meet the deadline.\""),
        ("Right.", "\"So the issue started on Tuesday...\" \"Right.\" \"...and it got worse by Thursday.\""),
        ("Sure.", "\"I'll walk you through the whole process...\" \"Sure.\" \"...starting with the intake form.\""),
        ("Okay.", "\"We're going to restructure the team a bit...\" \"Okay.\" \"...so you'll report to Maria now.\""),
        ("Go on.", "\"There's actually more to the story...\" \"Go on.\""),
        ("And then?", "\"He said he'd get back to us by Friday...\" \"And then?\""),
        ("Right, right.", "\"...so the whole system went down for an hour.\" \"Right, right.\" \"...and support was flooded with tickets.\""),
     ]),
    ("Newsmarkers — Marking Something as New",
     "The other person just told you something you didn't already know, and you want to show genuine interest.",
     "used to mark information as new or noteworthy and show genuine interest",
     [
        ("Oh really?", "\"We're moving the whole team to a new floor.\" \"Oh really?\""),
        ("Did you?", "\"I actually used to work at that company.\" \"Did you?\""),
        ("Is that right?", "\"The client doubled their order this month.\" \"Is that right?\""),
        ("Oh wow.", "\"We hit a million users last week.\" \"Oh wow.\""),
        ("Really!", "\"He's leaving the company next month.\" \"Really!\""),
        ("That's interesting.", "\"They're changing the whole pricing model.\" \"That's interesting.\""),
        ("I didn't know that.", "\"This building used to be a factory.\" \"I didn't know that.\""),
        ("Oh!", "\"Actually, the deadline moved to Monday.\" \"Oh!\""),
     ]),
    ("Assessments — Positive",
     "Someone just shared good news or a win, and you want to react warmly.",
     "used to react warmly to good news or a win someone just shared",
     [
        ("That's great.", "\"We just closed the deal.\" \"That's great.\""),
        ("Nice one.", "\"I finally fixed that bug.\" \"Nice one.\""),
        ("Brilliant.", "\"The client loved the pitch.\" \"Brilliant.\""),
        ("Good for you.", "\"I turned down the extra project — I just didn't have time.\" \"Good for you.\""),
        ("Well deserved.", "\"I got the promotion.\" \"Well deserved.\""),
     ]),
    ("Assessments — Sympathizing",
     "Someone just told you something frustrating or bad happened, and you want to show you feel for them.",
     "used to show empathy after someone shares something frustrating or bad",
     [
        ("Oh no.", "\"The server crashed right before the demo.\" \"Oh no.\""),
        ("That's rough.", "\"I've been in back-to-back meetings all week.\" \"That's rough.\""),
        ("Ugh, that's frustrating.", "\"They rejected the proposal after three months of work.\" \"Ugh, that's frustrating.\""),
        ("What a nightmare.", "\"The flight got cancelled and I missed the whole conference.\" \"What a nightmare.\""),
     ]),
    ("Assessments — Surprise & Strong Agreement",
     "Someone just said something surprising, or made a point you strongly agree with.",
     "used to react with surprise, or to strongly back up a point someone just made",
     [
        ("You're kidding.", "\"They cancelled the whole event.\" \"You're kidding.\""),
        ("No way.", "\"He quit without telling anyone.\" \"No way.\""),
        ("Seriously?", "\"The budget got cut in half.\" \"Seriously?\""),
        ("Exactly.", "\"I think we're overcomplicating this.\" \"Exactly.\""),
        ("Absolutely.", "\"We need more testing time before we ship.\" \"Absolutely.\""),
        ("Couldn't agree more.", "\"The old process was way too slow.\" \"Couldn't agree more.\""),
        ("Tell me about it.", "\"Mondays are always chaos.\" \"Tell me about it.\""),
     ]),
    ("Formulations — Playing Back What You Heard",
     "You want to summarize the other person's point in your own words to confirm you understood correctly.",
     "used to summarize the other person's point in your own words, to confirm understanding",
     [
        ("So basically you're saying...", "So basically you're saying we should delay the launch entirely?"),
        ("So what it comes down to is...", "So what it comes down to is a lack of budget, not a lack of will?"),
        ("If I've got this right, the issue is...", "If I've got this right, the issue is that the two systems don't sync."),
        ("So the real problem isn't X, it's Y?", "So the real problem isn't the price, it's the delivery time?"),
        ("Let me play that back to you...", "Let me play that back to you — you want to keep scope the same but move the deadline?"),
     ]),
    ("More Continuers / Encouraging the Speaker",
     "You're listening to someone tell a story and want to prompt them to keep going.",
     "used while listening to a story to prompt the speaker to keep going",
     [
        ("Mm.", "\"...and then I realized the file was never sent.\" \"Mm.\""),
        ("Yep.", "\"...so we had to redo the whole slide deck.\" \"Yep.\""),
        ("And?", "\"I finally called the client back...\" \"And?\""),
        ("Then what?", "\"He just went silent for a second...\" \"Then what?\""),
        ("What happened?", "\"So the meeting took a weird turn.\" \"What happened?\""),
     ]),
    ("More Newsmarkers (Showing Interest)",
     "You want a lighter, quicker way to show you're interested in what someone just said.",
     "used as a light, quick way to show interest in what was just said",
     [
        ("Oh?", "\"I heard they're restructuring the whole department.\" \"Oh?\""),
        ("Really?", "\"She's actually fluent in four languages.\" \"Really?\""),
        ("Was it?", "\"The presentation went a lot better than I expected.\" \"Was it?\""),
        ("Has it?", "\"The project's already gone way over budget.\" \"Has it?\""),
     ]),
    ("More Surprise & Agreement Tokens",
     "You want a stronger or more colorful way to react to surprising news or back up a strong point.",
     "used as a stronger or more colorful reaction to surprising news or a strong point",
     [
        ("You're joking.", "\"They're cutting the whole team's budget in half.\" \"You're joking.\""),
        ("Get out.", "\"I ran into our old manager at the airport.\" \"Get out.\""),
        ("Blimey.", "\"The bill came to nearly two thousand pounds.\" \"Blimey.\""),
        ("Precisely.", "\"So the real issue is trust, not process.\" \"Precisely.\""),
        ("100%.", "\"We should test this before rolling it out company-wide.\" \"100%.\""),
        ("Spot on.", "\"I think the delay is coming from procurement, not us.\" \"Spot on.\""),
     ]),
    ("More Sympathy Tokens (Bad News)",
     "Someone just told you something went wrong for them, and you want a stronger sympathetic reaction.",
     "used as a stronger sympathetic reaction when someone shares bad news",
     [
        ("Ouch.", "\"I locked myself out of the building this morning.\" \"Ouch.\""),
        ("Nightmare.", "\"The whole system went down during the demo.\" \"Nightmare.\""),
        ("Poor you.", "\"I've been stuck in meetings since 8am.\" \"Poor you.\""),
        ("That's rotten.", "\"They gave the project to another team at the last minute.\" \"That's rotten.\""),
     ]),
    ("More Positive Reaction Tokens (Good News)",
     "Someone just shared good news, and you want a warmer or more casual way to react.",
     "used as a warm, casual reaction when someone shares good news",
     [
        ("Nice.", "\"I finally got the visa approved.\" \"Nice.\""),
        ("Lovely.", "\"We managed to get the whole team together for lunch.\" \"Lovely.\""),
        ("Amazing.", "\"The client renewed the contract for another two years.\" \"Amazing.\""),
        ("Chuffed for you.", "\"I got accepted into the program.\" \"Chuffed for you.\""),
     ]),
    ("Realization Tokens",
     "Something the other person just said suddenly makes a confusing situation click into place.",
     "used when something just said suddenly makes a confusing situation click into place",
     [
        ("Ah, I see.", "\"The delay was on the vendor's side, not ours.\" \"Ah, I see.\""),
        ("Right, got it.", "\"You need the report before the client call, not after.\" \"Right, got it.\""),
        ("That makes sense.", "\"They changed the requirements halfway through.\" \"That makes sense.\""),
        ("Ah, of course.", "\"He's out today, that's why nobody replied.\" \"Ah, of course.\""),
     ]),
    ("Reacting When They're Happy or Boasting",
     "Someone is clearly excited or a little proud about something, and you want to match their energy.",
     "used to match a colleague's excitement when they're happy or a bit proud about something",
     [
        ("Get in!", "\"We just hit our quarterly target early.\" \"Get in!\""),
        ("That's great news.", "\"The client signed the renewal today.\" \"That's great news.\""),
        ("Look at you!", "\"I just finished my certification.\" \"Look at you!\""),
        ("You must be pleased.", "\"The review went really well.\" \"You must be pleased.\""),
     ]),
    ("Reacting When They're Complaining or Angry",
     "Someone is venting about something that annoyed or angered them, and you want to react in kind.",
     "used to react to someone venting about something that annoyed or angered them",
     [
        ("Ugh.", "\"They rescheduled the meeting for the third time.\" \"Ugh.\""),
        ("What a pain.", "\"I have to redo the whole form because of one typo.\" \"What a pain.\""),
        ("Fair enough.", "\"So I told them we needed more notice next time.\" \"Fair enough.\""),
        ("I'd be fuming.", "\"They gave my idea to another team without credit.\" \"I'd be fuming.\""),
        ("That's not on.", "\"He took credit for the whole project in the meeting.\" \"That's not on.\""),
        ("Understandably.", "\"I was pretty annoyed after the third delay.\" \"Understandably.\""),
     ]),
    ("Reacting When They're Worried, Explaining, or Apologizing",
     "Someone is anxious, explaining themselves, or apologizing to you, and you want to respond appropriately.",
     "used to respond appropriately when someone is anxious, explaining themselves, or apologizing",
     [
        ("That sounds stressful.", "\"I've got three deadlines colliding this week.\" \"That sounds stressful.\""),
        ("I get why.", "\"That's why I didn't want to commit to the date.\" \"I get why.\""),
        ("Anything I can do?", "\"I'm completely swamped trying to finish this report.\" \"Anything I can do?\""),
        ("What did you say?", "\"So I finally told him the timeline wasn't realistic.\" \"What did you say?\""),
        ("Got it.", "\"So just send it to Sarah, not the whole team.\" \"Got it.\""),
        ("Honestly, don't worry.", "\"I'm really sorry I missed the call.\" \"Honestly, don't worry.\""),
        ("It's fine, really.", "\"Sorry I'm late again.\" \"It's fine, really.\""),
        ("These things happen.", "\"I completely forgot to cc you on that.\" \"These things happen.\""),
     ]),
]

if __name__ == "__main__":
    generate_topic(
        out_path=OUT_PATH,
        exam_id="response-tokens",
        title="Chunk Atlas — Real-Time Fluency: Response Tokens & Active Listenership",
        tier_id=TIER_ID,
        tier_name=TIER_NAME,
        groups_def=groups_def,
    )
