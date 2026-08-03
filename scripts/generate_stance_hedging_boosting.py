import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from lib import generate_topic

OUT_PATH = os.path.join(SCRIPT_DIR, "..", "data", "stance-hedging-boosting.json")

# Phrase content below is copied by hand from the "Stance, Hedging &
# Boosting" topic (tier "mastery" / nav tab "Language Systems") — sections
# M4.1-M4.6 and L4.7.
#
# Source lines already group near-synonymous hedges/boosters with " / "
# separators, split into individual (phrase, example) tuples per the task
# spec. Every header bundles several distinct calibration points (e.g.
# M4.1 mixes hedging adverbs, vague-degree expressions, sentence frames,
# source hedges, credibility retreats, and conditional hedges), so each
# header is split into finer sub-groups, mirroring the H14 split in
# generate_core_patterns.py — this is especially natural here since the
# whole point of the topic is that each degree of certainty is its own
# distinct, non-interchangeable "situation".
# L4.7 heavily duplicates M4.5 (e.g. "I'm confident that", "I'd say", "I
# think/I reckon/I'd guess/probably" all repeat earlier groups almost
# verbatim) — exact duplicates were dropped and only genuinely new items
# kept, either folded into the closest matching group (e.g. "I firmly
# believe" folded into maximum-strength boosting) or given a new group
# where L4.7 named a function not covered elsewhere (uncertain, don't
# know at all, changed your mind).
# M4.4's "on [name]'s read..." template was dropped (placeholder, not a
# standalone quotable chunk); its "what we know is X; what we're assuming
# is Y" / "that's a fact; this is my inference" frames were kept as
# reusable framing chunks in their own group.
TIER_ID = "mastery"
TIER_NAME = "Language Systems"

groups_def = [
    ("Hedging adverbs (formal, softening a claim)",
     "You want to soften a claim about the market without stating it as a flat, undeniable fact, using a single formal hedging adverb.",
     "used as a single adverb to soften a claim, common in more formal or written register",
     [
        ("arguably", "This is arguably the strongest quarter we've had in two years."),
        ("presumably", "The client hasn't replied, presumably because they're still reviewing the contract."),
        ("seemingly", "The bug appeared seemingly out of nowhere after the last deploy."),
        ("ostensibly", "The meeting was ostensibly about budget, though it was really about headcount."),
        ("conceivably", "We could conceivably finish early if nothing else goes wrong."),
     ]),
    ("Hedging: how something looks, not how it necessarily is",
     "You want to say a plan looks solid on the surface, while leaving room for reality to turn out different.",
     "used to describe how something looks or is designed, while leaving room for reality to differ",
     [
        ("ideally", "Ideally, we'd have two more weeks of testing before launch."),
        ("in theory", "In theory, the new process should cut approval time in half."),
        ("on paper", "On paper, the merger makes perfect sense."),
     ]),
    ("Hedging vague-degree expressions",
     "You want to say a plan mostly worked, without claiming it was a complete, unqualified success.",
     "used to express a vague, partial degree instead of an absolute one",
     [
        ("to some extent", "The redesign helped, to some extent, but drop-off is still high."),
        ("by and large", "By and large, the migration went smoothly."),
        ("more or less", "The estimate turned out to be more or less accurate."),
        ("if anything", "If anything, the delay gave us more time to test."),
        ("broadly speaking", "Broadly speaking, customers responded well to the change."),
        ("for the most part", "For the most part, the new process is working fine."),
     ]),
    ("Hedging sentence openers (personal impression)",
     "You want to share your impression of a situation without stating it as a confirmed fact.",
     "used to introduce a personal impression or guess rather than a confirmed fact",
     [
        ("It seems that...", "It seems that the outage was caused by a bad config push."),
        ("It appears that...", "It appears that the vendor missed the shipping window again."),
        ("I'd imagine...", "I'd imagine the client will push back on that price."),
        ("My sense is...", "My sense is that the team is overcommitted this sprint."),
        ("My read is...", "My read is that they're not going to renew."),
     ]),
    ("Hedging by limited or secondhand evidence",
     "You want to share something you heard secondhand or only partly observed, flagging that your evidence is limited.",
     "used to flag that a claim is based on limited, partial, or secondhand information",
     [
        ("as far as I can tell", "As far as I can tell, the fix is holding up in production."),
        ("from what I gather", "From what I gather, the client's happy with the new pricing."),
        ("if I had to guess", "If I had to guess, I'd say the delay is on the vendor's side."),
        ("based on what I've seen", "Based on what I've seen, the smaller team ships faster."),
        ("apparently", "Apparently, the outage affected the EU region only."),
        ("reportedly", "The competitor is reportedly raising another funding round."),
        ("supposedly", "The fix was supposedly deployed last night."),
        ("I've heard", "I've heard the whole team is being reorganized next month."),
        ("word is", "Word is they're switching agencies after this contract ends."),
     ]),
    ("Pre-emptively hedging your own credibility",
     "You're about to share a guess you're not confident in, and want to signal upfront that you might be wrong.",
     "used to signal upfront that a claim is uncertain and the speaker might be wrong",
     [
        ("I could be wrong, but...", "I could be wrong, but I think the issue is on our end, not theirs."),
        ("Don't quote me on this, but...", "Don't quote me on this, but I think the deal is already signed."),
        ("Take this with a pinch of salt.", "Take this with a pinch of salt — I only heard it secondhand."),
     ]),
    ("Hedging with conditions",
     "You want to state a forecast while flagging that it depends on nothing unexpected happening.",
     "used to make a claim conditional on nothing unexpected happening",
     [
        ("all things being equal", "All things being equal, we should hit the target by June."),
        ("assuming nothing changes", "Assuming nothing changes, the launch stays on the 14th."),
        ("barring any surprises", "Barring any surprises, this should be a quiet quarter."),
     ]),
    ("Everyday light hedging",
     "You want to give your casual opinion on something without sounding like you're stating a hard fact.",
     "used for a light, everyday hedge on an opinion or guess, common in casual speech",
     [
        ("I think", "I think we should push the launch by a week."),
        ("I reckon", "I reckon the client will ask for a discount."),
        ("I'd say", "I'd say we're about 80% ready."),
        ("probably", "We'll probably need another round of testing."),
        ("most likely", "The delay is most likely on the vendor's end."),
        ("I'd guess", "I'd guess around half the team missed the announcement."),
     ]),
    ("Hedging with generalizations",
     "You want to describe a usual pattern without claiming it's true every single time.",
     "used to describe a general tendency rather than an absolute rule",
     [
        ("it tends to", "The queue tends to back up on Mondays."),
        ("generally", "Generally, smaller clients respond faster to emails."),
        ("typically", "Reviews typically take two to three days."),
        ("in most cases", "In most cases, the default settings work fine."),
        ("as a rule", "As a rule, we don't skip code review, even for small fixes."),
     ]),
    ("Academic-style hedging",
     "You want to raise a possibility in a formal or written context without committing to it as your own claim.",
     "used in formal or academic-style writing to raise a possibility without fully committing to it",
     [
        ("it could be argued", "It could be argued that the pricing change came too late."),
        ("one might say", "One might say the rollout was rushed."),
        ("there's a case for", "There's a case for delaying the launch by a week."),
     ]),
    ("Neutral cautious framing",
     "You want to share a first impression while flagging that you haven't looked closely yet.",
     "used to frame an observation as a first, cautious impression rather than a settled conclusion",
     [
        ("from what I can see", "From what I can see, the numbers look healthy this month."),
        ("on the face of it", "On the face of it, the proposal looks reasonable."),
        ("at first glance", "At first glance, the bug looks like a caching issue."),
     ]),
    ("Boosting adverbs (formal, strengthening a claim)",
     "You want to state something as completely beyond doubt, using a strong formal adverb.",
     "used as a single strong adverb to state something as certain or beyond doubt",
     [
        ("undoubtedly", "This is undoubtedly the best offer we've had all year."),
        ("decidedly", "The feedback on the new UI has been decidedly positive."),
        ("unquestionably", "She's unquestionably the strongest candidate we've seen."),
        ("categorically", "The company categorically ruled out further layoffs."),
        ("emphatically", "The board emphatically rejected the proposal."),
        ("without question", "This is, without question, our biggest client."),
     ]),
    ("Boosting with personal confidence",
     "You want to state that you're personally certain about an outcome, using a confident sentence frame.",
     "used as a sentence opener to state personal confidence or certainty about a claim",
     [
        ("It's clear that...", "It's clear that the old process just isn't scaling."),
        ("There's no question that...", "There's no question that the client is happy with the results."),
        ("I have no doubt that...", "I have no doubt that this feature will drive signups."),
        ("Make no mistake...", "Make no mistake, this delay is going to cost us the client."),
        ("I'm confident that...", "I'm confident that the fix will hold under load."),
        ("I'm sure", "I'm sure the numbers will look better once the promo kicks in."),
        ("no doubt", "No doubt the client will have questions about pricing."),
        ("absolutely", "Absolutely, this is the right call."),
     ]),
    ("Everyday light boosting",
     "You want to agree with something firmly but casually, without overdoing the emphasis.",
     "used as a light, everyday way to state something firmly in casual conversation",
     [
        ("definitely", "We definitely need to fix this before launch."),
        ("certainly", "It's certainly the fastest option we've tested."),
        ("clearly", "Clearly, the new pricing confused people."),
        ("obviously", "Obviously, we'll need to loop in legal first."),
        ("of course", "Of course we'll cover the cost of the fix."),
     ]),
    ("Maximum-strength, emphatic boosting",
     "You want to state something with the strongest possible conviction, leaving no room for doubt.",
     "used to state something with maximum emphasis and conviction, leaving no room for doubt",
     [
        ("I'd go so far as to say...", "I'd go so far as to say this is our best release ever."),
        ("if anything, it's an understatement", "Calling it a rough quarter is, if anything, an understatement."),
        ("without a shadow of a doubt", "Without a shadow of a doubt, that was the right call."),
        ("I'd bet on it", "They'll ask for an extension — I'd bet on it."),
        ("mark my words", "Mark my words, this feature is going to change the product."),
        ("I firmly believe", "I firmly believe we made the right call delaying the launch."),
        ("I'd stake money on it", "I'd stake money on it that the bug is in the payment module."),
     ]),
    ("Boosting through personal commitment",
     "You want to personally vouch for a claim, staking your own credibility on it.",
     "used to back a claim with personal credibility or a firm promise",
     [
        ("You have my word.", "You have my word — this won't happen again."),
        ("I stand by that.", "I stand by that, even after seeing the pushback."),
        ("I'll put my name to it.", "I've reviewed the numbers myself, and I'll put my name to it."),
     ]),
    ("Stating something as an absolute, undeniable fact",
     "You want to state something not as an opinion but as a plain, undeniable fact.",
     "used to present a claim as an established fact, not a personal opinion",
     [
        ("I know for a fact...", "I know for a fact that the contract was signed last week."),
        ("I can tell you categorically...", "I can tell you categorically that we never received that email."),
        ("There's no question.", "The client's unhappy — there's no question."),
     ]),
    ("Calibrated disagreement: acknowledge, then push back",
     "You disagree with a colleague's point, but want to first acknowledge it before pushing back.",
     "used to acknowledge the other person's point before pushing back on it",
     [
        ("I take your point, but...", "I take your point, but I still think we need more testing time."),
        ("That may be so, but...", "That may be so, but the client still expects the original date."),
        ("I see where you're coming from, but...", "I see where you're coming from, but the data says otherwise."),
     ]),
    ("Calibrated disagreement: casting doubt without a direct attack",
     "You're not convinced by a claim, but want to express that doubt gently rather than flatly rejecting it.",
     "used to express doubt about a claim without directly attacking it",
     [
        ("I'm not so sure about that.", "I'm not so sure about that — the sample size feels too small."),
        ("I'd be careful about...", "I'd be careful about promising that date to the client."),
        ("That's not necessarily the case.", "That's not necessarily the case — churn varies a lot by segment."),
     ]),
    ("Calibrated disagreement: a direct but polite challenge",
     "You want to directly challenge an assumption in the discussion, while staying professional and polite.",
     "used to directly but politely challenge an assumption or claim",
     [
        ("I'd push back on that slightly.", "I'd push back on that slightly — I don't think the data supports it."),
        ("I'd challenge that assumption.", "I'd challenge that assumption — are we sure users actually want this?"),
        ("With respect, I read it differently.", "With respect, I read it differently — I think the risk is much higher."),
     ]),
    ("Calibrated disagreement: offering an alternative view",
     "You want to introduce a different perspective without directly saying the other person is wrong.",
     "used to introduce an alternative perspective on the discussion",
     [
        ("There's another way of looking at it.", "There's another way of looking at it — maybe the delay actually helped us."),
        ("I'm going to be the dissenting voice here.", "I'm going to be the dissenting voice here — I don't think we should launch yet."),
     ]),
    ("Careful evidence verbs (not overclaiming)",
     "You want to describe what your data shows without overclaiming it as absolute proof.",
     "used to describe what evidence points toward, without overclaiming it as proof",
     [
        ("The data suggests...", "The data suggests users are dropping off at checkout, not sign-up."),
        ("The data indicates...", "The data indicates a slight uptick in engagement this week."),
        ("The data points to...", "The data points to a pricing issue rather than a product issue."),
     ]),
    ("Citing a specific source for a claim",
     "You want to attribute a claim to a specific external source rather than presenting it as your own view.",
     "used to attribute a claim to a specific external source",
     [
        ("according to", "According to the vendor, the shipment left the warehouse on Monday."),
        ("per the report", "Per the report, conversion dropped two points after the redesign."),
     ]),
    ("Rough, informal qualifiers for imprecise figures",
     "You want to give a rough estimate while flagging clearly that it's not precise.",
     "used to flag that a figure or claim is a rough estimate, not a precise one",
     [
        ("anecdotally", "Anecdotally, support tickets seem to be down this month."),
        ("directionally", "The numbers are directionally right, even if the exact figure is off."),
        ("rough order of magnitude", "As a rough order of magnitude, we're looking at a six-figure cost."),
     ]),
    ("Explicitly separating fact from inference",
     "You want to be very clear about which part of what you're saying is confirmed and which part is your own guess.",
     "used to explicitly separate a confirmed fact from your own inference or assumption",
     [
        ("What we know is X; what we're assuming is Y.", "What we know is the server crashed; what we're assuming is it was the new deploy."),
        ("That's a fact; this is my inference.", "The client cancelled — that's a fact; this is my inference: it was about price."),
     ]),
    ("Expressing near-certainty",
     "You want to say an outcome is essentially guaranteed to happen.",
     "used to describe an outcome as essentially guaranteed",
     [
        ("bound to", "With this much interest, the event is bound to sell out."),
        ("certain to", "He's certain to ask about the budget in the review."),
        ("all but guaranteed", "A renewal is all but guaranteed at this point."),
        ("a safe bet", "Given the trend, a Q4 rebound is a safe bet."),
     ]),
    ("Expressing high likelihood",
     "You want to say an outcome is quite likely, though not fully guaranteed.",
     "used to describe an outcome as likely, though not fully certain",
     [
        ("likely to", "We're likely to hear back from the client by Friday."),
        ("on track to", "We're on track to hit the Q3 target."),
        ("every chance", "There's every chance they'll want to renegotiate the price."),
        ("odds are", "Odds are the delay is on the vendor's side, not ours."),
     ]),
    ("Expressing 50-50 uncertainty",
     "You genuinely don't know which way an outcome will go — it's a real toss-up.",
     "used to describe a genuine toss-up, where either outcome is equally possible",
     [
        ("could go either way", "Honestly, this deal could go either way at this point."),
        ("a coin flip", "Whether they renew is basically a coin flip right now."),
        ("touch and go", "It was touch and go whether we'd make the deadline."),
        ("up in the air", "The budget for next year is still up in the air."),
     ]),
    ("Expressing low likelihood",
     "You want to say an outcome probably won't happen, though it's not completely impossible.",
     "used to describe an outcome as unlikely, though not completely impossible",
     [
        ("unlikely", "It's unlikely we'll get sign-off before the holidays."),
        ("a long shot", "Winning that account was always a long shot."),
        ("an outside chance", "There's an outside chance the client extends the contract."),
        ("I wouldn't bank on it.", "They might approve it early, but I wouldn't bank on it."),
     ]),
    ("Expressing near-impossibility",
     "You want to say an outcome is essentially never going to happen.",
     "used to describe an outcome as almost impossible",
     [
        ("slim to none", "The chances of getting that budget approved are slim to none."),
        ("not a chance", "Not a chance they'll agree to that price."),
        ("I'd be amazed.", "If that ships on time, I'd be amazed."),
        ("when pigs fly", "He'll apologize when pigs fly."),
     ]),
    ("Admitting you're not sure",
     "You genuinely don't know the answer to something and want a natural way to say so.",
     "used to admit you're genuinely unsure about something",
     [
        ("I'm not sure.", "I'm not sure — I'd have to check with the finance team."),
        ("It's hard to say.", "It's hard to say without seeing the full report."),
        ("Your guess is as good as mine.", "Why the numbers dropped? Your guess is as good as mine."),
     ]),
    ("Admitting you don't know at all",
     "You have no idea about something and want to be clear it's completely outside what you know.",
     "used to admit total lack of knowledge on a topic",
     [
        ("I honestly don't know.", "I honestly don't know why the migration failed."),
        ("That's outside my knowledge.", "The legal implications are outside my knowledge — you'd need to ask the lawyers."),
        ("I'd be guessing.", "If I answered that, I'd be guessing."),
     ]),
    ("Signalling you've changed your mind",
     "You used to believe something different and want to openly acknowledge that your view has shifted.",
     "used to openly acknowledge that your opinion has changed since earlier",
     [
        ("I've changed my mind on this.", "I've changed my mind on this — I now think we should wait."),
        ("I was wrong about that.", "I was wrong about that; the smaller team actually shipped faster."),
        ("On reflection, ...", "On reflection, I think we rushed the decision."),
     ]),
]

if __name__ == "__main__":
    generate_topic(
        out_path=OUT_PATH,
        exam_id="stance-hedging-boosting",
        title="Chunk Atlas — Language Systems: Stance, Hedging & Boosting",
        tier_id=TIER_ID,
        tier_name=TIER_NAME,
        groups_def=groups_def,
    )
