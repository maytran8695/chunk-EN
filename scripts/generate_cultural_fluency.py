import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from lib import generate_topic

OUT_PATH = os.path.join(SCRIPT_DIR, "..", "data", "cultural-fluency.json")

# Phrase content below is copied by hand from the "Cultural Fluency &
# Varieties" topic (tier "presence" / nav tab "Voice & Presence") in
# final_topics.json, sections P7.1-P7.4, P7.6, V7.7.
#
# P7.1 ("Anh vs Mỹ") is skipped entirely: it's a glossary of single-word
# British/American swaps (lift/elevator, flat/apartment...) and spelling
# variants, not situational chunks a speaker selects for a communicative
# function the way every other group here works — it's vocabulary trivia,
# not a "which chunk fits this situation" choice.
# P7.4 ("Bản đồ ngữ dụng: Việt ↔ Anh-Mỹ") is skipped as pure meta-advice:
# almost all of its actionable language lives in the "c" comparison blocks
# (skipped per spec), leaving only generic single words ("Thank you!",
# "Sorry!") with no real distinguishing chunk content of their own.
# P7.2 ("Chủ đề small talk — an toàn & vùng cấm") yields only one real
# chunk ("Do you have family nearby?", the suggested-safe-alternative to
# an off-limits question) — folded into the P7.3-based "cultural
# references" group below since it's the same underlying skill (handling
# a small-talk moment gracefully).
# P7.3 is split into two groups: sports idioms (a distinct, self-contained
# device) vs. the weather-ritual/gap-admitting/culture-sharing lines
# (a "handling the moment" skill, which is where P7.2's leftover phrase
# was folded in).
# P7.6 ("small talk theo bối cảnh") bundles 8 sub-categories; paired up by
# related theme into 4 groups (weather+travel, weekend+holiday,
# work+events, food+exit) rather than 8 near-single-purpose groups.
# V7.7 (British colloquial vocabulary) is split by function into 4 groups:
# address/farewell terms, feeling words, outcome/quality words, and
# invitations/reactions/intensifiers — mirroring the multi-way split used
# for bundled headers elsewhere (e.g. H14 in Core Patterns).
TIER_ID = "presence"
TIER_NAME = "Voice & Presence"

groups_def = [
    ("Sports idioms as office shorthand",
     "You want to make a point using a sports idiom that's common shorthand in Western offices.",
     "used as a sports-derived idiom that doubles as everyday office shorthand",
     [
        ("That's a slam dunk.", "Getting the client's sign-off after that demo? That's a slam dunk."),
        ("That's an own goal.", "Cancelling the loyalty programme right before renewals? That's an own goal."),
        ("It's a level playing field.", "Once we open the pricing page to every vendor, it's a level playing field."),
        ("The ball's in their court.", "We've sent the revised contract over — the ball's in their court now."),
        ("That came out of left field.", "The resignation came out of left field, nobody saw it coming."),
     ]),
    ("Handling & contributing cultural references",
     "You're in small talk and hit a moment where you don't share the cultural reference, or you want to add your own culture's angle.",
     "used to keep small talk warm and inclusive — joining a ritual exchange, admitting a gap, or contributing your own culture's angle",
     [
        ("Lovely day, isn't it?", "Lovely day, isn't it? — perfect for the walk over here."),
        ("That's one for the locals — what am I missing?", "Everyone laughed at that reference and I had no idea — that's one for the locals, what am I missing?"),
        ("In Vietnam we'd say...", "In Vietnam we'd say the fish rots from the head — same idea as your saying about leadership."),
        ("Do you have family nearby?", "Do you have family nearby, or did you move here for work?"),
     ]),
    ("Small talk openers: weather & travel",
     "You're making small talk before a meeting and want a safe opener about the weather or someone's journey in.",
     "used as a safe small-talk opener about the weather or someone's commute",
     [
        ("Miserable out there, isn't it?", "Miserable out there, isn't it? I got soaked just crossing the car park."),
        ("Lovely day for it.", "Lovely day for it — shame we're stuck in here all morning."),
        ("Bit nippy today.", "Bit nippy today, isn't it? I should've brought a coat."),
        ("How was the journey?", "How was the journey? The trains can be a nightmare on Mondays."),
        ("Traffic bad?", "Traffic bad? You cut it pretty close."),
        ("Did you find us alright?", "Did you find us alright? The building's a bit hidden from the main road."),
     ]),
    ("Small talk openers: weekend & holidays",
     "You're catching up with a colleague and want a safe opener about their weekend or time off.",
     "used as a safe small-talk opener about someone's weekend or holiday",
     [
        ("Get up to much at the weekend?", "Get up to much at the weekend? You look well rested."),
        ("Any plans for the weekend?", "Any plans for the weekend, or just taking it easy?"),
        ("Going anywhere nice?", "Going anywhere nice for the half-term break?"),
        ("How was the break?", "How was the break? Did you manage to switch off?"),
        ("Back to reality, eh?", "Back to reality, eh? Inbox must be a mess."),
     ]),
    ("Small talk openers: work & events",
     "You're making small talk at the start of a meeting or event and want to ask about someone's week or the occasion itself.",
     "used as a safe small-talk opener about work in general or the event you're both at",
     [
        ("How's your week looking?", "How's your week looking? Anything exciting on, or just the usual grind?"),
        ("Busy period for you?", "Busy period for you at the moment, or has it calmed down?"),
        ("How's the new role treating you?", "How's the new role treating you so far?"),
        ("First time at one of these?", "First time at one of these? The talks are usually pretty good."),
        ("How do you know [host]?", "How do you know Sarah? Old colleagues, or from the conference circuit?"),
        ("What did you make of the talk?", "What did you make of the talk? I thought the Q&A ran a bit long."),
     ]),
    ("Small talk: food comments & graceful exits",
     "You're at a work social and want a light comment about the food, or a polite way to wrap up and move on to someone else.",
     "used to comment lightly on food at a work event, or to exit a conversation politely",
     [
        ("Have you tried the...?", "Have you tried the mini quiches? They're going fast."),
        ("This is dangerous, I've had four.", "This is dangerous, I've had four of these already."),
        ("Right, I'd better circulate.", "Right, I'd better circulate — great to finally meet you though."),
        ("Lovely to meet you.", "Lovely to meet you — I'll send that document over tomorrow."),
        ("Enjoy the rest of it.", "Enjoy the rest of it, I'm going to go find some coffee."),
     ]),
    ("Informal address & farewells (UK)",
     "You're being casual and friendly with a British colleague you know well.",
     "used as a casual, friendly British way to address someone or say goodbye",
     [
        ("Cheers!", "Cheers for sorting that out so quickly!"),
        ("mate", "Cheers, mate — I owe you one."),
        ("pal", "Alright, pal? Long time no see."),
        ("love", "You alright, love? Haven't seen you in ages."),
        ("mind how you go", "Right, I'm off — mind how you go!"),
     ]),
    ("Naming a feeling, casually (UK)",
     "You want to describe how you're feeling, in the casual way a British colleague would.",
     "used to casually name how you're feeling, British-colloquial register",
     [
        ("knackered", "I'm absolutely knackered after that flight."),
        ("gutted", "I was gutted when the trip got cancelled."),
        ("chuffed", "She was chuffed with the feedback from the client."),
        ("gobsmacked", "I was gobsmacked when they announced the merger."),
     ]),
    ("Describing outcomes/quality, casually (UK)",
     "You want to casually describe how something turned out, or how annoying or good it was, the way a British colleague would.",
     "used to casually describe the quality or outcome of something, British-colloquial register",
     [
        ("faff", "Renewing my visa was such a faff."),
        ("dodgy", "That Wi-Fi connection in the meeting room is a bit dodgy."),
        ("naff", "The old logo was a bit naff, to be honest."),
        ("a bit of a nightmare", "Getting a refund from them was a bit of a nightmare."),
        ("sorted", "Don't worry, I've got it sorted."),
        ("spot on", "Your estimate was spot on — nearly to the pound."),
     ]),
    ("Casual invitations, reactions & intensifiers (UK)",
     "You want to casually invite someone, react to what they said, or add emphasis, the way a British colleague would.",
     "used to casually invite, react, or add emphasis, British-colloquial register",
     [
        ("fancy a...?", "Fancy a coffee before the meeting?"),
        ("are you up for it?", "We're doing drinks after work — are you up for it?"),
        ("I'm easy", "Pizza or curry? I'm easy, honestly."),
        ("fair play", "Fair play, she pulled that presentation together in a day."),
        ("nice one", "You closed the deal? Nice one!"),
        ("reckon", "I reckon we'll be done by lunchtime."),
        ("proper", "That was a proper mess of a meeting."),
        ("dead easy", "Once you know the trick, it's dead easy."),
     ]),
]

if __name__ == "__main__":
    generate_topic(
        out_path=OUT_PATH,
        exam_id="cultural-fluency",
        title="Chunk Atlas — Voice & Presence: Cultural Fluency & Varieties",
        tier_id=TIER_ID,
        tier_name=TIER_NAME,
        groups_def=groups_def,
    )
