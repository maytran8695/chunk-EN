import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from lib import generate_topic

OUT_PATH = os.path.join(SCRIPT_DIR, "..", "data", "semantic-prosody.json")

# Phrase content below is copied by hand from the "Semantic Prosody &
# Connotation" topic (tier "mastery" / nav tab "Language Systems") —
# sections M2.1-M2.6 and L2.7.
#
# Every header here already bundles several distinct "hidden meaning"
# clusters (e.g. M2.1 mixes "cause + bad noun", "commit + wrongdoing",
# "set in / break out", general negative verbs, and negative office verbs),
# so nearly every header is split into several finer sub-groups — the
# same principle as the H14 split in generate_core_patterns.py, applied
# more heavily because connotation content is inherently made of small,
# tight positive/negative/neutral clusters rather than long lists of
# interchangeable synonyms.
# Bare verbs in the source that need a completing noun to be a real
# quotable chunk (e.g. "foster", "cultivate") were paired with a natural
# object the source itself suggests (e.g. "foster collaboration").
# M2.6's "to be fair" (defending someone) was dropped: it didn't share a
# tight single function with any other item in the section without
# forcing together phrases that aren't real alternatives for one situation.
# The "[Name], you've worked on this" style templated items and "Mm-hm"
# (too minimal to quiz as a standalone chunk) were skipped.
TIER_ID = "mastery"
TIER_NAME = "Language Systems"

groups_def = [
    ("Negative-prosody verb: cause + bad noun",
     "You want to say a system outage created real problems for customers, using the verb natives reach for with a bad outcome.",
     "used with \"cause\" + a negative noun (damage, delay, concern, confusion, disruption) — \"cause\" almost never pairs with something good",
     [
        ("cause damage", "The leak caused serious damage to the server room."),
        ("cause delay", "The customs hold-up caused a two-week delay to the shipment."),
        ("cause concern", "The sudden spike in errors caused concern across the team."),
        ("cause confusion", "The vague email caused confusion about who owned the task."),
        ("cause disruption", "The migration caused disruption to checkout for almost an hour."),
     ]),
    ("Negative-prosody verb: commit + wrongdoing",
     "You want to describe an employee falsifying expense reports, using the verb natives reach for with wrongdoing.",
     "used with \"commit\" + a noun describing a crime, fraud, or serious error — \"commit\" almost always signals wrongdoing",
     [
        ("commit a crime", "He was accused of committing a crime against company policy, not just breaking a rule."),
        ("commit fraud", "The finance team discovered someone had committed fraud on the expense reports."),
        ("commit an error", "The auditor committed an error that went unnoticed for months."),
        ("commit an offence", "Sharing client data like that could mean he committed an offence, not just a mistake."),
        ("commit a blunder", "Sending that email to the whole client list was a serious blunder to commit."),
     ]),
    ("Negative-prosody verb: something bad takes hold or erupts",
     "You want to describe doubts quietly building up among the team after a rocky launch, using the verb natives use for a bad thing settling in.",
     "used for something unpleasant beginning and settling in, or suddenly breaking out",
     [
        ("doubts set in", "After the third delay, doubts set in about whether we'd ship at all."),
        ("complacency set in", "Once the metrics looked good, complacency set in and testing slipped."),
        ("a fight broke out", "A fight broke out in the comments over the pricing change."),
        ("an epidemic broke out", "An epidemic of missed deadlines broke out across every team that quarter."),
     ]),
    ("Negative-prosody verb: worsening & undermining",
     "You want to say a small disagreement has gotten steadily worse over several weeks, using the verb natives reach for.",
     "used for something bad gradually getting worse, or something being weakened or threatened",
     [
        ("exacerbate", "Cutting the support team only exacerbated the response-time problem."),
        ("deteriorate", "Relations with the vendor have deteriorated since the missed shipment."),
        ("escalate", "The disagreement escalated into a formal complaint."),
        ("erode", "Constant missed deadlines have eroded the client's trust in us."),
        ("undermine", "Skipping the review process undermines the whole QA effort."),
        ("jeopardise", "One more delay could jeopardise the entire contract."),
     ]),
    ("Negative-prosody verb: office problems",
     "You want to say a project quietly kept incurring extra costs without anyone flagging it, using the natural office collocation.",
     "used in office contexts for problems that pile up, stall, or get quietly hidden",
     [
        ("incur costs", "Delays like this incur costs we didn't budget for."),
        ("incur delays", "Waiting on legal review always incurs delays we can't control."),
        ("rack up debt", "The department racked up debt buying software nobody used."),
        ("bog down", "The approval process gets bogged down in unnecessary sign-offs."),
        ("drag on", "The negotiation dragged on for three more months than expected."),
        ("sweep under the rug", "Management tried to sweep the complaint under the rug."),
     ]),
    ("Positive-prosody verb: provide/offer + good noun",
     "You want to say a mentor gave a new hire clear direction during onboarding, using the verb natives reach for with something helpful.",
     "used with \"provide\" or \"offer\" + a positive noun like support, guidance, or clarity",
     [
        ("provide support", "The customer success team provides support during the first thirty days."),
        ("offer guidance", "Her manager offered guidance on how to handle the difficult client."),
        ("provide clarity", "The revised roadmap finally provided clarity on priorities."),
        ("offer opportunities", "The new program offers opportunities for junior staff to lead projects."),
     ]),
    ("Positive-prosody verb: building something up",
     "You want to say a new manager is deliberately building trust across two teams that used to compete, using the natural positive verb.",
     "used for actively building up, strengthening, or unlocking something valuable",
     [
        ("foster collaboration", "The offsite was designed to foster collaboration between the two teams."),
        ("cultivate trust", "It takes months to cultivate trust with a new client."),
        ("enhance performance", "The new tooling is meant to enhance performance across the pipeline."),
        ("bolster confidence", "A strong Q1 bolstered confidence among the investors."),
        ("streamline the process", "We streamlined the approval process to cut it from five steps to two."),
        ("spearhead the initiative", "She agreed to spearhead the sustainability initiative."),
     ]),
    ("Neutral-safe cause/result verb",
     "You want to state that a policy change led to an outcome, without implying whether that outcome was good or bad.",
     "used to link a cause to a result without pre-judging whether the outcome is good or bad — safer than \"cause\" when you're not sure",
     [
        ("bring about", "The new leadership brought about real change in how decisions get made."),
        ("result in", "Skipping the beta test could result in more support tickets."),
        ("lead to", "Poor documentation often leads to repeated questions from new hires."),
        ("give rise to", "The merger gave rise to a whole new set of reporting requirements."),
        ("contribute to", "Slow page loads contribute to a large share of our drop-off."),
        ("translate into", "Better onboarding should translate into higher retention."),
     ]),
    ("Words for a bad reputation",
     "You want to describe someone who's well known for something they should be ashamed of, using the word that carries that negative charge.",
     "used for being famous in a bad, disreputable way",
     [
        ("notorious", "The vendor is notorious for missing delivery dates."),
        ("infamous", "That release is now infamous for breaking half our integrations."),
     ]),
    ("Words for a good reputation",
     "You want to describe an expert who's widely respected in their field, using the word that carries that positive charge.",
     "used for being famous in a respected, admired way",
     [
        ("renowned", "She's a renowned researcher in supply-chain optimization."),
        ("eminent", "The panel included an eminent economist from the region."),
        ("distinguished", "He had a distinguished career in public policy before joining us."),
        ("esteemed", "The award was presented by an esteemed member of the board."),
     ]),
    ("Negative-prosody noun: fallout and repeated bad events",
     "You want to describe the wave of angry customer emails that followed a price hike, using the noun that carries that negative charge.",
     "used for the negative consequences or repeated occurrence of something bad",
     [
        ("repercussions", "There were serious repercussions after the data breach became public."),
        ("fallout", "The fallout from the failed launch cost two people their jobs."),
        ("backlash", "The price increase triggered immediate backlash on social media."),
        ("ramifications", "Nobody had considered the legal ramifications of the new policy."),
        ("a spate of complaints", "There's been a spate of complaints since the redesign shipped."),
        ("symptomatic of", "The missed deadline is symptomatic of a deeper staffing problem."),
     ]),
    ("Neutral/positive-prosody noun: results and collections",
     "You want to describe the collection of measures a client is rolling out after a strong quarter, using the noun that carries a neutral-to-positive charge.",
     "used for the neutral or positive result of something, or a helpful collection of things",
     [
        ("outcome", "The outcome of the pilot was better than we'd hoped."),
        ("upshot", "The upshot of the review is that we're keeping the current vendor."),
        ("dividend", "The extra QA time paid a real dividend in fewer post-launch bugs."),
        ("a raft of measures", "The government announced a raft of measures to support small businesses."),
        ("a suite of tools", "The team rolled out a suite of tools to automate reporting."),
     ]),
    ("Workplace euphemism: job loss & underperformance",
     "You want to say someone lost their job in the recent restructuring, using the softer term managers actually use.",
     "used as a softer, less blunt way to say someone was fired or that something is going badly",
     [
        ("let go", "Two people on the design team were let go last week."),
        ("made redundant", "She was made redundant when the regional office closed."),
        ("a challenge", "Retention has been a real challenge this year."),
        ("a headwind", "Rising costs are a headwind for the whole industry right now."),
        ("room for improvement", "There's room for improvement in how we handle escalations."),
        ("underperforming", "The EU region has been underperforming against target."),
     ]),
    ("Workplace euphemism: sidelined, disagreement & cuts",
     "You want to say a project got quietly dropped without anyone officially cancelling it, using the softer term managers actually use.",
     "used as a softer way to say something was abandoned, that people disagreed, or that budgets were cut",
     [
        ("parked", "That feature request has been parked until next quarter."),
        ("on the back burner", "The redesign is on the back burner while we fix the outage issues."),
        ("a difference of opinion", "There was a difference of opinion about which vendor to choose."),
        ("not fully aligned", "The two teams weren't fully aligned on the launch date."),
        ("cost optimisation", "The layoffs were announced as part of a cost optimisation drive."),
        ("efficiency drive", "The new efficiency drive means fewer approvals per hire."),
     ]),
    ("Reporting verb: neutral",
     "You want to report what a colleague said in a meeting without implying whether you believe it, using a neutral reporting verb.",
     "used to report what someone said without signaling belief, doubt, or agreement either way",
     [
        ("said", "He said the numbers would be ready by Monday."),
        ("stated", "The spokesperson stated that the outage was resolved."),
        ("noted", "She noted that the budget hadn't changed since last quarter."),
        ("observed", "The auditor observed that two invoices were missing."),
        ("remarked", "He remarked that traffic was unusually low that week."),
        ("reported", "The team reported that testing was complete."),
     ]),
    ("Reporting verb: signals you believe it",
     "You want to report a finding you trust as solid, using a verb that signals confidence in the source.",
     "used to report something in a way that signals the speaker trusts or accepts it as true",
     [
        ("confirmed", "The lab confirmed the results were accurate."),
        ("demonstrated", "The test demonstrated that the fix actually worked."),
        ("established", "The investigation established that the delay was the vendor's fault."),
        ("showed", "The data showed a clear drop in churn after the change."),
        ("revealed", "The audit revealed a gap in the reconciliation process."),
     ]),
    ("Reporting verb: signals you doubt it",
     "You want to report what a vendor said about a delay while quietly signaling you're not fully convinced, using the right reporting verb.",
     "used to report something in a way that signals the speaker isn't fully convinced it's true",
     [
        ("claimed", "The vendor claimed the delay was due to customs, though we never got proof."),
        ("alleged", "The email alleged that the account had been compromised."),
        ("asserted", "He asserted that the bug had already been fixed."),
        ("insisted", "She insisted the numbers were correct despite the discrepancy."),
        ("maintained", "The supplier maintained that the shipment left on time."),
     ]),
    ("Reporting verb: signals agreement or reluctant concession",
     "You want to report that a colleague finally admitted a point you'd been making, using the verb that carries that implication.",
     "used to report something in a way that signals the speaker agrees with it, or that the person had to reluctantly admit it",
     [
        ("pointed out", "She pointed out that the deadline had already slipped once."),
        ("highlighted", "The report highlighted a growing gap between the two regions."),
        ("emphasised", "He emphasised how much the team had improved this quarter."),
        ("conceded", "The vendor eventually conceded that the delay was on their end."),
        ("admitted", "She admitted the plan hadn't been tested properly."),
        ("acknowledged", "Management acknowledged the rollout had gone badly."),
     ]),
    ("Diplomatically prefacing disagreement",
     "You're about to push back on a colleague's plan and want to signal, before you even start, that disagreement is coming.",
     "used at the start of a turn to soften an upcoming disagreement or criticism, said in a flat or careful tone",
     [
        ("with respect", "With respect, I don't think that timeline is realistic."),
        ("interesting", "\"Interesting,\" she said flatly, which everyone understood meant she disagreed."),
        ("happy to discuss", "I'm happy to discuss this further, though I don't see it the same way."),
     ]),
    ("Deflecting a topic to later or privately",
     "You want to avoid getting into a sensitive topic in front of the whole meeting, using the phrase natives use to defer it.",
     "used to postpone or move a sensitive discussion away from the current, more public setting",
     [
        ("circle back", "Let's circle back to the budget question after this call."),
        ("take offline", "Can we take this offline? I don't think we need to hash it out here."),
     ]),
    ("Signalling mild professional irritation",
     "You've already explained something once and are quietly annoyed at having to repeat it, using the phrase natives reach for.",
     "used to politely mask irritation, impatience, or a firm expectation that something won't happen again",
     [
        ("as per my previous email", "As per my previous email, the deadline is Thursday, not Friday."),
        ("it is what it is", "The client changed their mind again — it is what it is, let's move on."),
        ("going forward", "Going forward, let's loop in QA before any release."),
     ]),
    ("Diplomatically flagging an overly ambitious plan",
     "You think a colleague's timeline is unrealistic but want to say so gently, using the phrase natives reach for.",
     "used to gently suggest a plan is too risky or unrealistic without saying so directly",
     [
        ("ambitious", "That's an ambitious timeline for a launch this size."),
        ("let's be pragmatic", "Let's be pragmatic about what we can actually ship by March."),
     ]),
    ("Strong implicit praise about a person",
     "You want to say a colleague is completely dependable and always delivers, using the phrase natives reach for.",
     "used to praise someone as highly reliable, without using a plain word like \"good\"",
     [
        ("a safe pair of hands", "Put Dan on it — he's a safe pair of hands."),
        ("he delivers", "Whatever you give him, he delivers."),
        ("gets things done", "She's not flashy, but she gets things done."),
        ("rock solid", "Our ops process has been rock solid since she took over."),
     ]),
    ("Mild implicit criticism about a person",
     "You want to say a colleague is a bit difficult to work with, without being openly critical, using the phrase natives reach for.",
     "used to mildly, deniably criticize someone as difficult, without directly attacking them",
     [
        ("a bit of a character", "He's a bit of a character, but the clients love him."),
        ("high maintenance", "That account is a bit high maintenance — lots of last-minute changes."),
        ("not the easiest", "She's not the easiest to work with, but her output is excellent."),
        ("an acquired taste", "His presentation style is an acquired taste."),
     ]),
    ("Strong implicit criticism about a person",
     "You want to say a colleague talks big but doesn't actually deliver, using the phrase natives reach for.",
     "used to sharply criticize someone as unreliable or full of empty talk",
     [
        ("all talk", "He's all talk — the numbers never back up what he promises."),
        ("a lot of noise", "There's been a lot of noise from that team but nothing shipped."),
        ("spreads himself thin", "He spreads himself thin and drops half of what he commits to."),
        ("drops the ball", "She's dropped the ball on the last two handoffs."),
     ]),
    ("Safe, non-committal remarks about a person",
     "You're asked what a colleague is like and want to give a safe answer that avoids saying anything too positive or negative.",
     "used to describe someone in a neutral way that avoids committing to a clear positive or negative judgment",
     [
        ("hard to read", "He's hard to read in meetings — you never quite know what he's thinking."),
        ("very thorough", "She's very thorough, so reviews with her take a while."),
        ("has strong views", "He has strong views on tooling, so expect a debate."),
     ]),
    ("Hidden-meaning evaluation of an idea",
     "You've been asked what you think of a colleague's plan and want to hint at your real opinion diplomatically.",
     "used to hint at a real judgment about an idea — risky, unrealistic, or disliked — while sounding neutral",
     [
        ("ambitious", "\"That's ambitious,\" the director said, meaning he thought it was too risky."),
        ("optimistic", "Calling the timeline optimistic was her polite way of saying it wasn't realistic."),
        ("interesting", "\"Interesting approach,\" was all he said, which usually means he doesn't like it."),
     ]),
    ("Hidden-meaning evaluation of a deliverable",
     "You've reviewed a colleague's draft and want to signal, diplomatically, that it still needs real work.",
     "used to soften feedback on unfinished or weak work while still hinting it needs more",
     [
        ("a good first draft", "It's a good first draft — let's talk through what still needs work."),
        ("a solid start", "This is a solid start, but the middle section needs a lot more detail."),
     ]),
]

if __name__ == "__main__":
    generate_topic(
        out_path=OUT_PATH,
        exam_id="semantic-prosody",
        title="Chunk Atlas — Language Systems: Semantic Prosody & Connotation",
        tier_id=TIER_ID,
        tier_name=TIER_NAME,
        groups_def=groups_def,
    )
