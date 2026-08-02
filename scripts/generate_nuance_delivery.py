import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from lib import generate_topic

OUT_PATH = os.path.join(SCRIPT_DIR, "..", "data", "nuance-delivery.json")

# Phrase content below is copied by hand from the "Nuance, Delivery &
# Written Register" topic (tier "core" / nav tab "Situations") — sections
# N1-N6 (indirectness/register/softening), E1 (academic discourse markers),
# J1-J5 (email register), and L1-L4 (interview/negotiation register).
#
# Skipped entirely (pure "how to speak" meta-advice about pronunciation,
# not actual lexical chunks — same exception as H15 in Core Patterns):
# M1 (sentence stress theory), M2 (linking/reduction phonology), M3
# (intonation contours), M4 (pace/clarity advice), M5 (shadowing exercise
# instructions).
# Also skipped: E2 and E3, which the source itself flags as "reference
# material to study argument structure, not content to adopt" — long,
# topic-specific philosophical/rhetorical excerpts rather than reusable,
# swappable communicative chunks.
# N3 ("Reading between the lines") mixes English quoted chunks with pure
# Vietnamese behavioral descriptions that have no English phrase at all
# (e.g. "long silence after a proposal", "sudden topic change") — those
# non-English items were dropped since there is no chunk to quiz on; only
# the items with an actual quoted English phrase were kept.
# E1 bundles 10 distinct rhetorical functions (signposting, hedging,
# contrasting, etc.) in one header and is split into 9 finer sub-groups,
# mirroring how generate_core_patterns.py split H14.
# L1's closing item ("Can you walk me through a time when you had to...?")
# was dropped — it's the interviewer's question, not the candidate's
# answer chunk, so it doesn't belong with the other STAR-answer phrases.
TIER_ID = "core"
TIER_NAME = "Situations"

groups_def = [
    ("Reading & Using Indirect, Understated Signals",
     "You want to react to something you don't actually like, or make a request, without sounding blunt or starting a confrontation.",
     "used to soften disagreement, a request, or a boundary so it doesn't sound blunt — the real meaning is usually stronger than the literal words",
     [
        ("That's interesting.", "When I don't love an idea but don't want to shut it down outright, I'll just say, 'That's interesting.'"),
        ("I hear what you're saying.", "I hear what you're saying, but I still think we should wait until Q2."),
        ("With respect...", "With respect, I think that timeline is unrealistic given our current headcount."),
        ("With all due respect...", "With all due respect, I don't think the board will accept that explanation."),
        ("I only have a few minor comments.", "I only have a few minor comments on the draft — mostly around section three."),
        ("Perhaps we could consider...", "Perhaps we could consider pushing the deadline by a week instead of cutting scope."),
        ("It's not bad.", "I tried the new dashboard — it's not bad, actually."),
        ("We should catch up sometime.", "We should catch up sometime, once things calm down after the launch."),
        ("Let's take that offline.", "Let's take that offline — I don't think we need to debate pricing in front of the whole team."),
        ("No worries if not!", "Could you send that over today? No worries if not!"),
     ]),
    ("Adjusting Directness of a Request by Formality",
     "You need to ask someone to change a deadline, and want to choose how direct or cushioned the request sounds depending on who you're asking.",
     "used to make the same request at different levels of directness, depending on seniority and closeness of the relationship",
     [
        ("I don't suppose there's any chance we could move the deadline?", "I don't suppose there's any chance we could move the deadline, given the vendor delay?"),
        ("Would it be possible to move the deadline?", "Would it be possible to move the deadline by a few days?"),
        ("Could we move the deadline?", "Could we move the deadline to next Friday instead?"),
        ("We need to move the deadline.", "We need to move the deadline — there's no way we finish testing by Thursday."),
     ]),
    ("Decoding Passive or Deflecting Written Signals",
     "You've received a short, clipped, or oddly formal reply and need to recognize the real signal behind the wording.",
     "a short or formal-sounding phrase that often signals irritation, reluctant agreement, or a soft no, rather than its literal meaning",
     [
        ("per my last email", "She replied with 'per my last email,' which told me she was annoyed I'd asked twice."),
        ("as mentioned below", "The reply just said 'as mentioned below' — a polite way of saying I'd missed it the first time."),
        ("Noted.", "I asked for feedback on my proposal and just got back 'Noted.'"),
        ("Ok.", "He replied with a flat 'Ok.' — I couldn't tell if he was on board or just done arguing."),
        ("Let me think about it.", "When I pitched the idea, she said, 'Let me think about it,' and I never heard back."),
     ]),
    ("Matching Formality to Audience (Register)",
     "You want to ask someone for five minutes of their time, and need to pick the wording that matches how well you know them.",
     "used to ask for the same thing at a formality level matched to the audience — casual chat, work peer, or senior/client",
     [
        ("wanna grab 5 mins?", "I messaged my teammate, 'wanna grab 5 mins?' to quickly sync on the bug."),
        ("Do you have five minutes to sync?", "Do you have five minutes to sync on the ticket before standup?"),
        ("Would you have five minutes to align on this?", "Would you have five minutes to align on this before the client call?"),
     ]),
    ("Softening & Face-Saving Language",
     "You want to disagree with an idea or make a suggestion, without sounding confrontational or overly certain.",
     "used to soften a disagreement or suggestion so the other person doesn't feel attacked or cornered",
     [
        ("I might be missing something, but...", "I might be missing something, but doesn't this contradict the numbers from last week?"),
        ("Just to play devil's advocate...", "Just to play devil's advocate, what happens if the vendor misses this deadline too?"),
        ("Correct me if I'm wrong...", "Correct me if I'm wrong, but I thought we'd already agreed on the March 1st launch."),
        ("Would it make sense to...?", "Would it make sense to run a smaller pilot before the full rollout?"),
        ("I'd lean towards X, but I'm open.", "I'd lean towards the in-house build, but I'm open to hearing the vendor's pitch first."),
        ("That's a fair point — and...", "That's a fair point — and I'd add that we should also budget for support costs."),
     ]),
    ("Diplomatic Responses to Pushback",
     "Someone has just challenged your idea or asked a pointed question, and you want to respond diplomatically while holding your ground.",
     "used to respond to pushback or a challenging question diplomatically, without backing down or getting defensive",
     [
        ("I take your point, though I'd offer a different perspective.", "I take your point, though I'd offer a different perspective on why churn actually went up."),
        ("That's a fair observation — could we explore an alternative?", "That's a fair observation — could we explore an alternative pricing tier instead?"),
        ("I appreciate the feedback — just to clarify, are we saying X or Y?", "I appreciate the feedback — just to clarify, are we saying we cut scope or extend the deadline?"),
        ("Would you be able to share a bit more context on that?", "Would you be able to share a bit more context on that decision before we proceed?"),
        ("Let me make sure I understand before I respond.", "Let me make sure I understand before I respond — you're saying the budget was cut entirely?"),
     ]),
    ("Academic Signposting",
     "You're writing or presenting a formal, academic-style argument and need to signal you're moving to a new stage of your reasoning.",
     "used in formal academic writing or speaking to signal a new stage in the argument",
     [
        ("To begin with...", "To begin with, let's define what we mean by 'success' in this context."),
        ("Let's unpack this...", "Let's unpack this a little — there are really two separate issues here."),
        ("This brings us to...", "This brings us to the central question of the report: is the model actually generalizable?"),
        ("To put a finer point on it...", "To put a finer point on it, the issue isn't awareness, it's incentives."),
     ]),
    ("Academic Hedging",
     "You're making an academic-style claim and want to avoid stating it as an absolute fact.",
     "used in academic register to avoid stating a claim as an absolute fact",
     [
        ("It could be argued that...", "It could be argued that the policy did more harm than good in the short term."),
        ("There's a tendency to...", "There's a tendency to overestimate how much control we actually have in these situations."),
        ("To a certain extent...", "To a certain extent, both explanations are true, but neither is complete."),
     ]),
    ("Acknowledging Complexity (Academic)",
     "You're writing academically and want to acknowledge that an issue is more complicated than a simple explanation would suggest.",
     "used in academic writing to acknowledge that an issue is more complicated than it first appears",
     [
        ("This is a multifaceted issue...", "This is a multifaceted issue, and no single policy change will fix it."),
        ("The situation is more layered than it appears...", "The situation is more layered than it appears, once you factor in the regional differences."),
     ]),
    ("Academic Rhetorical Questions",
     "You're building an academic argument and want to pose a rhetorical question that highlights a tension in the evidence.",
     "used to pose a rhetorical question that highlights a tension or contradiction in an academic argument",
     [
        ("What are we to make of this?", "The data contradicts the theory entirely — so what are we to make of this?"),
        ("How do we reconcile these ideas?", "How do we reconcile these ideas with the earlier finding that contradicts them?"),
     ]),
    ("Emphasizing Key Points (Academic)",
     "You're writing academically and want to stress that a particular point is central to your whole argument.",
     "used in academic register to stress that a point is central to the whole argument",
     [
        ("This is of paramount importance...", "This is of paramount importance to the argument as a whole."),
        ("This is the linchpin of the argument...", "This is the linchpin of the argument — remove it, and the whole case collapses."),
     ]),
    ("Contrasting Ideas (Academic)",
     "You're building an academic argument and need to introduce a contrasting or counterintuitive idea.",
     "used in academic register to introduce a contrasting or counterintuitive idea",
     [
        ("While it's true that..., it's also the case that...", "While it's true that costs went down, it's also the case that quality suffered."),
        ("Contrary to popular belief...", "Contrary to popular belief, most successful negotiations aren't about winning."),
     ]),
    ("Addressing Counterarguments (Academic)",
     "You're writing academically and want to acknowledge an opposing view fairly before responding to it.",
     "used in academic register to acknowledge an opposing view fairly before responding to it",
     [
        ("It might be tempting to think that..., however...", "It might be tempting to think that more data always helps, however, it can also introduce noise."),
        ("Let's steelman the opposing view...", "Let's steelman the opposing view before we dismiss it outright."),
     ]),
    ("Academic Metaphors & Analogies",
     "You're writing an academic argument and want to explain an abstract idea through a vivid metaphor.",
     "used in academic writing to explain an abstract idea through a vivid metaphor or analogy",
     [
        ("The self is a center of narrative gravity...", "As one theory puts it, the self is a center of narrative gravity, not a fixed thing."),
        ("Ideas propagate like viruses...", "Ideas propagate like viruses, spreading fastest through the networks we trust most."),
     ]),
    ("Clarifying Definitions (Academic)",
     "You're writing academically and need to define exactly what you mean by a key term before using it further.",
     "used in academic register to define precisely what you mean by a key term",
     [
        ("By 'X,' I mean...", "By 'engagement,' I mean daily active use, not just sign-ups."),
        ("Let's operationalize this term...", "Let's operationalize this term before we start measuring it."),
     ]),
    ("Philosophical & Academic Terms",
     "You're writing or discussing an academic or philosophical topic and need precise technical vocabulary rather than a vague paraphrase.",
     "a precise academic or philosophical term used in formal discussion or writing",
     [
        ("epistemic humility", "Good researchers practice epistemic humility — they hold their conclusions loosely."),
        ("phenomenological experience", "The study focused on the phenomenological experience of chronic pain, not just its clinical markers."),
        ("moral framework", "Their moral framework prioritizes outcomes over intentions."),
        ("the illusion of the self", "The lecture explored the illusion of the self as a stable, unchanging entity."),
     ]),
    ("Opening & Stating Purpose in an Email",
     "You're starting a professional email and need to state clearly why you're writing.",
     "used to open a professional email and state its purpose clearly",
     [
        ("I hope this email finds you well.", "I hope this email finds you well — it's been a while since we last spoke."),
        ("I am writing to follow up on...", "I am writing to follow up on the proposal I sent last Tuesday."),
        ("I am writing to request...", "I am writing to request an extension on the submission deadline."),
        ("Further to our conversation earlier today, ...", "Further to our conversation earlier today, I've attached the revised contract."),
        ("Following up on our call, I wanted to confirm...", "Following up on our call, I wanted to confirm the go-live date is still March 15th."),
        ("I wanted to flag/highlight the following before we proceed.", "I wanted to flag/highlight the following before we proceed: the budget line hasn't been approved yet."),
     ]),
    ("Making a Clear Written Request",
     "You're writing a professional email and need to make a clear, polite request for action.",
     "used to make a clear, polite written request for action",
     [
        ("Could you please confirm by [date]?", "Could you please confirm by Friday whether the venue is booked?"),
        ("Please could you advise at your earliest convenience?", "Please could you advise at your earliest convenience whether the terms are acceptable?"),
        ("I would appreciate it if you could review this by [date].", "I would appreciate it if you could review this by end of day Wednesday."),
        ("Please let me know if you have any questions or concerns.", "Please let me know if you have any questions or concerns about the attached scope of work."),
        ("Kindly find attached...", "Kindly find attached the updated invoice for last month's services."),
        ("Please see attached for your reference.", "Please see attached for your reference — the full meeting notes are in the PDF."),
        ("I would be grateful if you could clarify...", "I would be grateful if you could clarify which department owns this approval."),
     ]),
    ("Transferring Information / Status Updates in Writing",
     "You're writing an email to pass along information or confirm a status update, in a way that's easy to reference later.",
     "used in writing to pass along information or confirm a status update for the record",
     [
        ("For your awareness, looping in [name].", "For your awareness, looping in Anh from finance on this thread."),
        ("For your reference, looping in [name].", "For your reference, looping in David, who handled the original contract."),
        ("For visibility, looping in [name].", "For visibility, looping in the whole project team on this update."),
        ("Just to confirm, the following action items were agreed: ...", "Just to confirm, the following action items were agreed: legal reviews by Monday, finance signs off by Wednesday."),
        ("This is to formally document what we discussed on the call.", "This is to formally document what we discussed on the call regarding the revised delivery schedule."),
        ("As discussed, please find below a summary of next steps.", "As discussed, please find below a summary of next steps for the onboarding process."),
     ]),
    ("Apologizing in Writing",
     "You need to apologize for a mistake or delay in a written, professional way.",
     "used to apologize for a mistake or delay in formal written communication",
     [
        ("Apologies for the delay in responding.", "Apologies for the delay in responding — I was out of office until yesterday."),
        ("I apologize for any inconvenience this may have caused.", "I apologize for any inconvenience this may have caused during the system outage."),
        ("Please accept my apologies for the oversight.", "Please accept my apologies for the oversight — the attachment is included now."),
        ("I take full responsibility for this and will ensure it does not happen again.", "I take full responsibility for this and will ensure it does not happen again going forward."),
        ("Thank you for your patience while we resolve this.", "Thank you for your patience while we resolve this billing issue."),
     ]),
    ("Closing a Professional Email",
     "You're finishing a professional email and need a natural, polite way to close it.",
     "used to close a professional email politely",
     [
        ("Please do not hesitate to reach out should you have any questions.", "Please do not hesitate to reach out should you have any questions about the proposal."),
        ("I look forward to hearing from you.", "I look forward to hearing from you regarding next steps."),
        ("Looking forward to your feedback.", "Looking forward to your feedback on the revised draft."),
        ("Thank you for your time and consideration.", "Thank you for your time and consideration during the interview process."),
        ("Best regards,", "Best regards, Minh"),
        ("Kind regards,", "Kind regards, the Operations Team"),
        ("Many thanks,", "Many thanks, looking forward to catching up soon."),
     ]),
    ("Answering Behavioral Questions (STAR Method)",
     "You're in a job interview and the interviewer asks about a specific past situation — you want to structure your answer clearly.",
     "used to structure a behavioral interview answer using the STAR method (Situation, Task, Action, Result)",
     [
        ("In my previous role, we were facing...", "In my previous role, we were facing a 20% drop in customer retention."),
        ("I was responsible for...", "I was responsible for coordinating the migration between the old and new systems."),
        ("So what I did was...", "So what I did was set up a weekly check-in with both teams to track blockers."),
        ("I took the initiative to...", "I took the initiative to build a shared dashboard so everyone saw the same numbers."),
        ("As a result, we were able to...", "As a result, we were able to cut the reporting time from three days to one."),
        ("This led to a 20% improvement in...", "This led to a 20% improvement in on-time delivery over the following quarter."),
     ]),
    ("Self-Introduction (Elevator Pitch)",
     "You're introducing yourself professionally, such as at the start of an interview or when meeting someone new in your field.",
     "used to introduce yourself professionally in a concise elevator pitch",
     [
        ("I'm currently a Business Analyst working across fintech and mortgage domains for UK clients.", "I'm currently a Business Analyst working across fintech and mortgage domains for UK clients, mostly on requirements and process mapping."),
        ("My background is in [finance], and I've spent the last [X years] specializing in...", "My background is in finance, and I've spent the last four years specializing in regulatory reporting."),
        ("What draws me to this role is the opportunity to combine my BA experience with my growing finance/investment background.", "What draws me to this role is the opportunity to combine my BA experience with my growing finance/investment background."),
     ]),
    ("Asking Thoughtful Questions in an Interview",
     "You've reached the end of an interview and the interviewer asks if you have any questions — you want to ask something that shows genuine engagement.",
     "used to ask a thoughtful, engaged question at the end of a job interview",
     [
        ("What does success look like in this role after the first six months?", "What does success look like in this role after the first six months?"),
        ("What are the biggest challenges the team is currently facing?", "What are the biggest challenges the team is currently facing?"),
        ("How is the BA function positioned within the broader product/investment team?", "How is the BA function positioned within the broader product/investment team?"),
        ("What growth opportunities exist for someone moving from a general BA background into capital markets?", "What growth opportunities exist for someone moving from a general BA background into capital markets?"),
     ]),
    ("Negotiating Salary & Offers",
     "You've received a job offer and want to negotiate the compensation package professionally.",
     "used to negotiate salary or offer terms professionally after receiving a job offer",
     [
        ("Thank you for the offer — I'm very excited about the opportunity. I'd like to discuss the compensation package before confirming.", "Thank you for the offer — I'm very excited about the opportunity. I'd like to discuss the compensation package before confirming."),
        ("Based on my research and experience, I was expecting a range closer to...", "Based on my research and experience, I was expecting a range closer to $95,000."),
        ("Is there any flexibility on the base salary?", "Is there any flexibility on the base salary, even if the sign-on stays the same?"),
        ("Is there any flexibility on the sign-on bonus?", "Is there any flexibility on the sign-on bonus if the base salary can't move?"),
        ("Is there any flexibility on the remote work arrangement?", "Is there any flexibility on the remote work arrangement — say, two days from home?"),
        ("I'm confident I can bring strong value here — is there room to revisit this number?", "I'm confident I can bring strong value here — is there room to revisit this number?"),
        ("Could we possibly meet in the middle at...?", "Could we possibly meet in the middle at $90,000?"),
        ("I'd like a bit of time to consider this properly — could I get back to you by [date]?", "I'd like a bit of time to consider this properly — could I get back to you by Friday?"),
     ]),
]

if __name__ == "__main__":
    generate_topic(
        out_path=OUT_PATH,
        exam_id="nuance-delivery",
        title="Chunk Atlas — Situations: Nuance, Delivery & Written Register",
        tier_id=TIER_ID,
        tier_name=TIER_NAME,
        groups_def=groups_def,
    )
