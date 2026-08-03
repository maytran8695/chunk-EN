import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from lib import generate_topic

OUT_PATH = os.path.join(SCRIPT_DIR, "..", "data", "near-synonym.json")

# Phrase content copied by hand from the "Near-Synonym Discrimination"
# topic (tier "mastery" / nav tab "Language Systems") — sections
# M8.1-M8.8. M8.1-M8.5 are ALL "c" (comparison) blocks with no "i"
# items, so per spec they are skipped entirely (no quotable chunks to
# extract). Only M8.6, M8.7 and M8.8 contain real "i" items:
#   - M8.6 ("bo ba dong nghia theo muc do") is 9 ready-made intensity
#     ladders (good/bad/difficult/busy/tired/soon/angry/happy/surprised)
#     — each ladder becomes its own group, since the whole point is
#     choosing the right INTENSITY within one ladder, not mixing ladders.
#   - M8.7 ("cap de nham thong dung") is 11 confusable word-pairs; the
#     "advise/advice ... practise/practice" line bundles two separate
#     pairs and is split into two groups. Each pair becomes its own
#     2-item group so the nuance between the two words stays central.
#   - M8.8 ("chon tu dung sac thai o cong so") is 10 ready-made register
#     triads/tetrads (ask/demand/request etc.) — each becomes its own
#     group for the same reason as M8.6.
TIER_ID = "mastery"
TIER_NAME = "Language Systems"

groups_def = [
    ("Degree ladder: how good something was",
     "You want to describe how good a result was, choosing a word that matches the right intensity — from mildly okay to truly exceptional.",
     "a degree-ladder word describing how good something was, at one specific intensity level",
     [
        ("alright", "The demo was alright, nothing more."),
        ("good", "The pilot results were good, better than we expected."),
        ("great", "The client feedback was great across the board."),
        ("excellent", "Q2 revenue was excellent, well above target."),
        ("outstanding", "Her handling of the outage was outstanding."),
        ("exceptional", "This is an exceptional result for a first release."),
     ]),
    ("Degree ladder: how bad something was",
     "You want to describe how bad a result was, choosing a word that matches the right intensity — from merely disappointing to truly disastrous.",
     "a degree-ladder word describing how bad something was, at one specific intensity level",
     [
        ("not ideal", "The timing isn't ideal, but we can work with it."),
        ("poor", "Turnout for the workshop was poor."),
        ("bad", "The client's reaction was pretty bad."),
        ("awful", "The first version of the onboarding flow was awful."),
        ("terrible", "Response times last week were terrible."),
        ("disastrous", "The launch was disastrous — three outages in one day."),
     ]),
    ("Degree ladder: how difficult something was",
     "You want to describe how difficult a task was, choosing a word that matches the right intensity — from mildly fiddly to truly brutal.",
     "a degree-ladder word describing how difficult something was, at one specific intensity level",
     [
        ("fiddly", "Setting up the printer is a bit fiddly."),
        ("tricky", "This bug is tricky to reproduce."),
        ("difficult", "Negotiating the contract was difficult."),
        ("hard", "Hiring senior engineers right now is hard."),
        ("challenging", "The migration was challenging but manageable."),
        ("brutal", "This sprint has been absolutely brutal."),
     ]),
    ("Degree ladder: how busy someone was",
     "You want to describe how busy someone is, choosing a word that matches the right intensity — from lightly busy to completely underwater.",
     "a degree-ladder word describing how busy someone was, at one specific intensity level",
     [
        ("busy", "I'm busy this afternoon, can we talk tomorrow?"),
        ("stretched", "The support team is stretched this week."),
        ("slammed", "We're slammed with tickets after the release."),
        ("swamped", "I'm swamped, can this wait until Friday?"),
        ("underwater", "The whole team is underwater trying to hit this deadline."),
        ("drowning", "I'm drowning in approvals right now."),
     ]),
    ("Degree ladder: how tired someone was",
     "You want to describe how tired someone is, choosing a word that matches the right intensity — from a little tired to completely wiped out.",
     "a degree-ladder word describing how tired someone was, at one specific intensity level",
     [
        ("tired", "I'm a bit tired after the red-eye flight."),
        ("shattered", "I'm shattered after that all-hands week."),
        ("knackered (UK)", "I'm absolutely knackered after the conference."),
        ("wiped out", "The whole team is wiped out after the launch."),
        ("running on fumes", "I'm running on fumes at this point in the sprint."),
     ]),
    ("Degree ladder: how soon something will happen",
     "You want to describe how soon something will happen, choosing a word that matches the right urgency — from vaguely soon to any moment now.",
     "a degree-ladder word describing how soon something will happen, at one specific urgency level",
     [
        ("soon", "We'll have an update soon."),
        ("shortly", "The client will be joining shortly."),
        ("imminently", "The announcement is expected imminently."),
        ("any moment", "The fix should land any moment."),
     ]),
    ("Degree ladder: how angry someone was",
     "You want to describe how angry someone is, choosing a word that matches the right intensity — from mildly annoyed to truly livid.",
     "a degree-ladder word describing how angry someone was, at one specific intensity level",
     [
        ("annoyed", "She was a little annoyed the meeting ran late."),
        ("irritated", "He sounded irritated on the call."),
        ("frustrated", "The client is frustrated with the delays."),
        ("angry", "The team was angry about the last-minute change."),
        ("furious", "He was furious when he saw the invoice error."),
        ("livid", "The client was livid after the second missed deadline."),
     ]),
    ("Degree ladder: how happy someone was",
     "You want to describe how happy someone is, choosing a word that matches the right intensity — from simply pleased to over the moon.",
     "a degree-ladder word describing how happy someone was, at one specific intensity level",
     [
        ("pleased", "We're pleased with how the pilot went."),
        ("glad", "I'm glad the migration finally finished."),
        ("happy", "The client seems happy with the new design."),
        ("delighted", "We're delighted with the response to the launch."),
        ("thrilled", "She was thrilled to get the promotion."),
        ("over the moon", "The team was over the moon when the deal closed."),
     ]),
    ("Degree ladder: how surprised someone was",
     "You want to describe how surprised someone is, choosing a word that matches the right intensity — from mildly surprised to completely gobsmacked.",
     "a degree-ladder word describing how surprised someone was, at one specific intensity level",
     [
        ("surprised", "I was surprised the fix worked on the first try."),
        ("taken aback", "She was taken aback by how blunt the feedback was."),
        ("stunned", "We were stunned by the size of the contract."),
        ("floored", "I was floored when I saw the final numbers."),
        ("gobsmacked (UK)", "He was absolutely gobsmacked by the offer."),
     ]),
    ("borrow vs lend",
     "You want to say someone takes something temporarily from another person, not that they give it.",
     "the correct verb when someone RECEIVES something temporarily from someone else, not gives it",
     [
        ("borrow", "Can I borrow your laptop charger for the meeting?"),
        ("lend", "Can you lend me your laptop charger for the meeting?"),
     ]),
    ("bring vs take",
     "You want to describe moving something toward the speaker's current location, not away from it.",
     "the correct verb for moving something TOWARD the speaker's location, not away from it",
     [
        ("bring", "Please bring your laptop to the workshop tomorrow."),
        ("take", "Take these documents to the client's office on your way out."),
     ]),
    ("say vs tell",
     "You want to report what was said without naming the listener directly after the verb.",
     "the correct verb when the listener is NOT named directly after it (use 'tell' when it is)",
     [
        ("say", "She said the deadline had moved, but didn't say who to."),
        ("tell", "She told me the deadline had moved."),
     ]),
    ("remind vs remember",
     "You want to describe prompting someone else to recall something, not recalling it yourself.",
     "the correct verb for prompting SOMEONE ELSE to recall something, not recalling it yourself",
     [
        ("remind", "Can you remind me to send the invoice tomorrow?"),
        ("remember", "I need to remember to send the invoice tomorrow."),
     ]),
    ("economic vs economical",
     "You're describing something related to the economy in general, not something that saves money.",
     "the adjective for something related to the ECONOMY in general, not something money-saving",
     [
        ("economic", "The economic outlook for next quarter looks uncertain."),
        ("economical", "This printer is far more economical than our old one."),
     ]),
    ("historic vs historical",
     "You want to describe an event as important and memorable in history, not simply something that happened in the past.",
     "the adjective for something historically IMPORTANT and memorable, not just something from the past",
     [
        ("historic", "Signing this deal was a historic moment for the company."),
        ("historical", "We looked at historical sales data before setting the target."),
     ]),
    ("sensible vs sensitive",
     "You want to describe a decision as practical and well-reasoned, not describe a person's emotional delicacy.",
     "the adjective for something PRACTICAL and well-reasoned, not emotionally delicate",
     [
        ("sensible", "Delaying the launch was the sensible choice."),
        ("sensitive", "Be sensitive when you deliver this feedback, he's had a rough month."),
     ]),
    ("sympathy vs empathy",
     "You want to describe genuinely sharing and understanding someone's feelings, not just feeling sorry for them from a distance.",
     "the noun for genuinely SHARING someone's feelings, not just feeling sorry for them from a distance",
     [
        ("sympathy", "I have a lot of sympathy for the support team right now."),
        ("empathy", "Good managers show empathy, not just sympathy, when a project fails."),
     ]),
    ("advise vs advice",
     "You need the verb form for giving guidance, not the noun.",
     "the VERB form for giving guidance (spelled with an 's'), not the noun",
     [
        ("advise", "I'd advise you to get legal to review this first."),
        ("advice", "Thanks for the advice, I'll loop in legal first."),
     ]),
    ("practise vs practice",
     "You need the verb form, UK spelling, for the act of rehearsing, not the noun.",
     "the VERB form (UK spelling, with 's') for the act of rehearsing, not the noun",
     [
        ("practise", "You should practise the pitch a few times before the client call."),
        ("practice", "The pitch needs more practice before the client call."),
     ]),
    ("fewer vs less",
     "You're describing a countable noun, not an uncountable amount.",
     "the correct quantifier for a COUNTABLE noun, not an uncountable amount",
     [
        ("fewer", "We had fewer support tickets this week."),
        ("less", "We had less traffic this week."),
     ]),
    ("imply vs infer",
     "You want to describe the speaker hinting at something, not the listener drawing a conclusion.",
     "the correct verb for the SPEAKER hinting at something, not the listener drawing a conclusion",
     [
        ("imply", "Are you implying the numbers were manipulated?"),
        ("infer", "From his tone, I inferred he wasn't happy with the results."),
     ]),
    ("ask / demand / request",
     "You want to describe someone asking for something — choose the word matching the right register: neutral, forceful, or formal and polite.",
     "a word for asking for something, at one specific register level (neutral, forceful, or formal)",
     [
        ("ask", "She asked for an extra day to finish the report."),
        ("demand", "The client demanded a full refund within 24 hours."),
        ("request", "We formally requested an extension from the vendor."),
     ]),
    ("tell / inform / notify",
     "You want to describe telling someone something — choose the word matching the right register: neutral, formal, or official.",
     "a word for telling someone something, at one specific register level (neutral, formal, or official)",
     [
        ("tell", "I told the team about the schedule change."),
        ("inform", "Please inform the client of the delay as soon as possible."),
        ("notify", "We are required to notify affected users within 72 hours."),
     ]),
    ("help / assist / support",
     "You want to describe helping someone — choose the word matching the right register and scope: neutral, formal, or broader ongoing support.",
     "a word for helping someone, at one specific register and scope (neutral, formal, or ongoing support)",
     [
        ("help", "Can you help me finish this deck before the call?"),
        ("assist", "Our team will assist you with the migration process."),
        ("support", "We support over two hundred enterprise customers."),
     ]),
    ("change / amend / overhaul",
     "You want to describe modifying something — choose the word matching the right scale: neutral, a small formal edit, or a complete rebuild.",
     "a word for modifying something, at one specific scale (neutral, a small formal edit, or a complete rebuild)",
     [
        ("change", "We changed the button color after user testing."),
        ("amend", "Please amend clause 4 to reflect the new payment terms."),
        ("overhaul", "The whole pricing structure needs an overhaul, not a tweak."),
     ]),
    ("stop / halt / pause / cease",
     "You want to describe stopping something — choose the word matching the right tone: neutral, abrupt, temporary, or formal.",
     "a word for stopping something, with one specific tone (neutral, abrupt, temporary, or formal)",
     [
        ("stop", "We stopped the rollout after the first error report."),
        ("halt", "Production was halted the moment the defect was found."),
        ("pause", "Let's pause the campaign until the pricing page is fixed."),
        ("cease", "The vendor will cease support for this version in June."),
     ]),
    ("check / verify / audit",
     "You want to describe examining something — choose the word matching the right level of rigor: light, formal, or a serious full review.",
     "a word for examining something, at one specific level of rigor (light, formal, or a full review)",
     [
        ("check", "Can you check the numbers before I send them?"),
        ("verify", "Finance needs to verify the invoice before we pay it."),
        ("audit", "We're auditing every vendor contract after last quarter's overpayment."),
     ]),
    ("good / adequate / satisfactory",
     "You want to evaluate work — choose the word matching the right tone: genuinely positive, or a lukewarm 'just enough'.",
     "a word for evaluating work, with one specific tone (genuinely positive, or a lukewarm 'just enough')",
     [
        ("good", "This is genuinely good work, well above what we expected."),
        ("adequate", "The report was adequate, though it lacked real analysis."),
        ("satisfactory", "The results were satisfactory, but nothing more than that."),
     ]),
    ("quick / hasty / prompt",
     "You want to describe speed — choose the word matching the right connotation: neutral, careless, or admirably timely.",
     "a word for describing speed, with one specific connotation (neutral, careless, or admirably timely)",
     [
        ("quick", "That was a quick turnaround on the fix."),
        ("hasty", "That was a hasty decision — we didn't even test it."),
        ("prompt", "Thanks for the prompt response, it really helped."),
     ]),
    ("cheap / affordable / cost-effective",
     "You want to describe a low price — choose the word matching the right connotation: negative (low quality), neutral, or a smart business tradeoff.",
     "a word for describing a low price, with one specific connotation (negative, neutral, or a smart tradeoff)",
     [
        ("cheap", "The materials felt cheap for the price we paid."),
        ("affordable", "We priced the plan to be affordable for small teams."),
        ("cost-effective", "Switching vendors turned out to be a cost-effective move."),
     ]),
    ("old / outdated / established / legacy",
     "You want to describe something that isn't new — choose the word matching the right connotation: neutral age, negative obsolescence, positive reputation, or technical continuity.",
     "a word for describing something not new, with one specific connotation (neutral, negative, positive, or technical)",
     [
        ("old", "This is an old version of the app, but it still works fine."),
        ("outdated", "Our onboarding docs are outdated and confuse new hires."),
        ("established", "We're an established player in this market."),
        ("legacy", "The legacy system still handles about a third of our transactions."),
     ]),
]

if __name__ == "__main__":
    generate_topic(
        out_path=OUT_PATH,
        exam_id="near-synonym",
        title="Chunk Atlas — Language Systems: Near-Synonym Discrimination",
        tier_id=TIER_ID,
        tier_name=TIER_NAME,
        groups_def=groups_def,
    )
