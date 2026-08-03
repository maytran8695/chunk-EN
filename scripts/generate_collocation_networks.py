import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from lib import generate_topic

OUT_PATH = os.path.join(SCRIPT_DIR, "..", "data", "collocation-networks.json")

# Phrase content below is copied by hand from the "Collocation Networks"
# topic (tier "mastery" / nav tab "Language Systems") — sections M1.1-M1.6
# and L1.7-L1.9. Comma-separated collocation lists in the source were split
# into individual (phrase, example) tuples; each phrase gets its own
# hand-written example sentence.
#
# M1.1 (delexical verbs make/do/take/have/get) is split into 5 finer
# sub-groups, one per verb, mirroring the H14 split in generate_core_patterns.py
# — grouping all five together would make "which delexical verb goes with
# this noun" un-testable (the whole point of that section).
# M1.2 (adjective+noun) is split into 3 finer sub-groups by the semantic
# field the source itself uses (opinions/arguments, problems/risk,
# opportunities/progress).
# M1.3 (intensifiers) is split into strengthening vs softening, since those
# are opposite communicative goals.
# M1.4 (verb+noun business) is split into 3 finer sub-groups by the
# semantic field the source itself uses.
# The "c" (common-error) comparison items throughout were skipped per the
# task spec (not "i" phrase items) — but they confirmed which collocations
# are the idiomatic ones worth quizzing on.
# L1.8/L1.9 paradigm lines (e.g. "point: make/take/miss/prove/raise/labour
# a point") bundle collocations with genuinely different meanings under one
# noun (making a point vs missing a point are not interchangeable), so
# rather than quiz them as one group of "equivalent" answers, individual
# combinations from these lines were folded into the semantically-matching
# group above where their real meaning fits (e.g. "raise an issue" is under
# Verb + noun: meetings & decisions).
TIER_ID = "mastery"
TIER_NAME = "Language Systems"

groups_def = [
    ("Delexical verb: make",
     "You want to describe finalizing a firm choice after weighing the options, using the right \"empty\" verb + noun pairing.",
     "used with \"make\" + an abstract noun for actions like decisions, effort, progress, or exceptions",
     [
        ("make a decision", "We need to make a decision on the vendor by Friday."),
        ("make an effort", "She made a real effort to get everyone aligned before the launch."),
        ("make progress", "We're finally making progress on the backlog."),
        ("make a mistake", "I made a mistake in the forecast — the numbers were off by 10%."),
        ("make sense", "None of this makes sense until you see the full dataset."),
        ("make an exception", "We don't normally extend deadlines, but we'll make an exception this time."),
        ("make a point", "She made a point of thanking the whole team publicly."),
     ]),
    ("Delexical verb: do",
     "You want to say your team investigated the competitor thoroughly before the pitch, using the right \"empty\" verb + noun pairing.",
     "used with \"do\" + a noun for tasks, chores, and routine work like research or paperwork",
     [
        ("do research", "We did some research on the competitor before the pitch."),
        ("do someone a favour", "Could you do me a favour and forward that email?"),
        ("do your best", "Just do your best — nobody's expecting perfection on the first draft."),
        ("do the paperwork", "I still need to do the paperwork before the contract is official."),
        ("do a review", "Let's do a review of the launch before we plan the next one."),
        ("do due diligence", "The investors did due diligence on the company before signing."),
     ]),
    ("Delexical verb: take",
     "You want to say you personally accept the blame for a missed deadline, using the right \"empty\" verb + noun pairing.",
     "used with \"take\" + a noun for actions like responsibility, risk, leadership, or initiative",
     [
        ("take responsibility", "I'll take responsibility for the missed deadline."),
        ("take a risk", "We decided to take a risk and launch a week early."),
        ("take advantage of", "Let's take advantage of the slow week to clear the backlog."),
        ("take the lead", "Maria is going to take the lead on the client migration."),
        ("take ownership", "He took ownership of the bug even though it wasn't his code."),
        ("take the initiative", "Nobody assigned it to her, but she took the initiative and fixed it."),
     ]),
    ("Delexical verb: have",
     "You want to say a pricing change noticeably affected customer behavior, using the right \"empty\" verb + noun pairing.",
     "used with \"have\" + a noun for impact, opinions, doubts, or quick actions",
     [
        ("have an impact", "The new pricing had a real impact on conversion rates."),
        ("have a say", "Everyone on the team should have a say in the naming decision."),
        ("have second thoughts", "I'm having second thoughts about launching before the audit's done."),
        ("have a look", "Can you have a look at this before I send it to the client?"),
        ("have reservations", "I have reservations about rushing the rollout."),
        ("have a word (with)", "I need to have a word with Dan about the missed handoff."),
     ]),
    ("Delexical verb: get",
     "You want to say the project finally received formal leadership approval, using the right \"empty\" verb + noun pairing.",
     "used with \"get\" + a noun for reaching approval, catching up, or a milestone",
     [
        ("get buy-in", "We need to get buy-in from finance before we scope this."),
        ("get sign-off", "We can't start until we get sign-off from legal."),
        ("get up to speed", "I'll spend Monday getting up to speed on the account."),
        ("get the green light", "We finally got the green light to hire two more engineers."),
        ("get the hang of", "It took a week, but she got the hang of the new dashboard."),
        ("get rid of", "We should get rid of the legacy script before the migration."),
     ]),
    ("Adjective + noun: opinions & arguments",
     "You want to describe a discussion that got emotionally intense, using the adjective natives actually pair with \"debate\".",
     "used to describe the strength or quality of an argument, opinion, or statement in a discussion",
     [
        ("a heated debate", "The pricing change turned into a heated debate at the all-hands."),
        ("a compelling argument", "He made a compelling argument for delaying the launch."),
        ("a valid point", "Actually, that's a valid point — we haven't tested the edge cases."),
        ("a nuanced view", "She offered a more nuanced view than the rest of the panel."),
        ("a sweeping statement", "\"Nobody reads the docs\" is a bit of a sweeping statement."),
     ]),
    ("Adjective + noun: problems & risk",
     "You want to describe an issue that needs attention right now, more urgent than most, using the right adjective + noun pairing.",
     "used to describe the seriousness or urgency of a problem, gap, or risk",
     [
        ("a pressing issue", "Staff turnover is a pressing issue we can't keep ignoring."),
        ("a recurring problem", "Late invoices have become a recurring problem with this client."),
        ("a glaring omission", "No mention of security testing was a glaring omission in the plan."),
        ("a fundamental flaw", "There's a fundamental flaw in how we calculate churn."),
        ("a looming deadline", "With a looming deadline, nobody wanted to touch the scope again."),
     ]),
    ("Adjective + noun: opportunities & progress",
     "You want to describe a rare chance that's too good to pass up, using the right adjective + noun pairing.",
     "used to describe the value of an opportunity or the shape of progress being made",
     [
        ("a viable option", "Outsourcing QA is starting to look like a viable option."),
        ("a golden opportunity", "This partnership is a golden opportunity to enter the EU market."),
        ("a fresh perspective", "Bringing in an outside consultant gave us a fresh perspective."),
        ("a steep learning curve", "The new CRM has a steep learning curve for the sales team."),
        ("a marked improvement", "Response times show a marked improvement since the update."),
        ("a daunting task", "Migrating ten years of data is a daunting task."),
     ]),
    ("Intensifying adverb + adjective/verb",
     "You want to intensify how concerned you are about a delay, without just relying on \"very\".",
     "used to intensify a specific adjective or verb naturally, instead of the generic \"very\"",
     [
        ("deeply concerned", "We're deeply concerned about the drop in retention this quarter."),
        ("bitterly disappointed", "The team was bitterly disappointed when the funding fell through."),
        ("highly unlikely", "It's highly unlikely we'll hit the original launch date now."),
        ("utterly ridiculous", "Charging extra for basic support seems utterly ridiculous to most users."),
        ("strongly recommend", "I strongly recommend we get legal's sign-off before proceeding."),
        ("flatly refuse", "The supplier flatly refused to renegotiate the contract terms."),
        ("categorically deny", "The company categorically denied any knowledge of the leak."),
     ]),
    ("Softening adverb + adjective (downtoners)",
     "You want to soften your degree of confidence in a forecast, without sounding evasive.",
     "used to soften the degree of an adjective, stating something as partial or approximate rather than absolute",
     [
        ("somewhat concerned", "I'm somewhat concerned about the vendor's recent delays."),
        ("fairly confident", "We're fairly confident the fix will hold through peak traffic."),
        ("reasonably certain", "I'm reasonably certain the numbers will hold up under review."),
        ("marginally better", "This quarter's churn is only marginally better than last quarter's."),
        ("broadly speaking", "Broadly speaking, customers are happy, though onboarding needs work."),
     ]),
    ("Verb + noun: meetings & decisions",
     "You want to say the group finally agreed on a direction after a long discussion, using the right verb + noun pairing.",
     "used for actions taken during meetings and decision-making, like proposing, raising, or weighing something",
     [
        ("reach a consensus", "It took two hours, but we finally reached a consensus on the roadmap."),
        ("table a proposal", "Legal tabled a proposal to change the vendor agreement."),
        ("put forward an idea", "One of the interns put forward an idea that actually stuck."),
        ("raise an issue", "She raised an issue about the data retention policy."),
        ("weigh the options", "Let's weigh the options before committing to a platform."),
        ("defer a decision", "The board decided to defer a decision until next quarter."),
     ]),
    ("Verb + noun: plans, progress & risk",
     "You want to say a project is slipping and no longer tracking to its original dates, using the right verb + noun pairing.",
     "used for actions related to timelines, milestones, and managing risk on a project",
     [
        ("meet a deadline", "There's no way we'll meet the deadline without more headcount."),
        ("hit a milestone", "We hit a major milestone by shipping the beta on time."),
        ("fall behind schedule", "The redesign has fallen behind schedule because of the vendor delay."),
        ("mitigate risk", "We added a rollback plan to mitigate risk during the migration."),
        ("escalate an issue", "I had to escalate the issue once support stopped responding."),
        ("close a gap", "The new hire helps close a gap in our data engineering coverage."),
     ]),
    ("Verb + noun: strategy & relationships",
     "You want to say a new product feature is finally starting to catch on with users, using the right verb + noun pairing.",
     "used for actions related to strategy, growth, and managing stakeholder relationships",
     [
        ("strike a balance", "We're trying to strike a balance between speed and quality."),
        ("bridge the gap", "The new onboarding flow helps bridge the gap between sign-up and first use."),
        ("gain traction", "The referral program is finally gaining traction."),
        ("build rapport", "It takes time to build rapport with a client over video calls."),
        ("manage expectations", "It's important to manage expectations before the demo, not after."),
        ("secure buy-in", "We secured buy-in from the regional teams before the rollout."),
     ]),
    ("Fixed noun/verb + preposition",
     "You want to describe the effect a new policy had on sales, using the preposition natives actually pair with \"impact\".",
     "used because certain nouns and verbs pair with one fixed preposition in standard usage, not others",
     [
        ("a solution to", "We need a solution to the onboarding drop-off, not just a workaround."),
        ("an impact on", "The outage had a serious impact on customer trust."),
        ("insight into", "The survey gave us real insight into why users churn."),
        ("comply with", "All vendors must comply with the new data policy."),
        ("result in", "Skipping code review tends to result in more bugs downstream."),
        ("account for", "Shipping costs account for nearly a third of our expenses."),
        ("depend on", "Whether we launch on time depends on the vendor's delivery."),
     ]),
    ("Verb + adverb & fixed prepositional phrases",
     "You want to say a project is still being reviewed and hasn't been finalized, using the fixed phrase natives actually use.",
     "used as fixed collocations for manner (verb + adverb) or formal status (prepositional phrase), not built freely word by word",
     [
        ("monitor closely", "We're monitoring the error rate closely after the deploy."),
        ("follow up promptly", "Please follow up promptly with anyone who hasn't responded."),
        ("proceed cautiously", "Given the audit findings, we should proceed cautiously with the rollout."),
        ("in principle", "The client agreed in principle, but we're still waiting on the signed contract."),
        ("on balance", "On balance, the pilot was a success despite the rocky start."),
        ("under review", "The pricing model is currently under review."),
     ]),
    ("Everyday collocations (life outside work)",
     "You want to describe waiting somewhere with nothing to do until your delayed flight boards, using the natural everyday collocation.",
     "used in everyday, non-work situations — time, money, health, food, and daily routines",
     [
        ("kill time", "We killed time at the airport by wandering through the shops."),
        ("run out of time", "We ran out of time and never got to the dessert menu."),
        ("tight budget", "We're on a tight budget this month after the car repair."),
        ("cost a fortune", "That hotel looked nice, but it cost a fortune."),
        ("catch a cold", "I caught a cold after standing in the rain for the bus."),
        ("feel under the weather", "I'm feeling a bit under the weather, so I might skip the gym."),
        ("grab a bite", "Do you want to grab a bite before the movie starts?"),
     ]),
]

if __name__ == "__main__":
    generate_topic(
        out_path=OUT_PATH,
        exam_id="collocation-networks",
        title="Chunk Atlas — Language Systems: Collocation Networks",
        tier_id=TIER_ID,
        tier_name=TIER_NAME,
        groups_def=groups_def,
    )
