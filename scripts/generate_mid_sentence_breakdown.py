import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from lib import generate_topic

OUT_PATH = os.path.join(SCRIPT_DIR, "..", "data", "mid-sentence-breakdown.json")

# Phrase content below is copied by hand from the "Mid-Sentence Breakdown"
# topic (tier "fluency" / F8-F9) in the source content set. F8.6 is a
# supplementary "kho" (repository) list that mostly repeats the earlier
# sections verbatim; only its NEW, non-duplicate phrasings were folded into
# the matching functional group below (e.g. "Basically: ..." and
# "In one sentence: ..." into the "untangling" group; "Anyway. / Moving on. /
# Where were we? / Back to it." became their own group since they serve a
# distinct function — resuming flow after a recovery, not the recovery
# itself).
TIER_ID = "fluency"
TIER_NAME = "Real-Time Fluency"

groups_def = [
    ("Blanking out mid-sentence",
     "You've completely lost your train of thought mid-sentence and your mind has gone blank.",
     "used when your mind goes blank mid-sentence and you need to name it and buy time",
     [
        ("Sorry — I've completely lost my train of thought.", "Sorry — I've completely lost my train of thought, give me one second."),
        ("I had a point, and it's gone. Give me a second.", "I had a point about the timeline, and it's gone. Give me a second."),
        ("Where was I?", "Where was I? Right, the budget numbers."),
        ("What was I saying?", "Sorry, what was I saying before the phone rang?"),
        ("It'll come back to me.", "It'll come back to me — anyway, let's move to the next slide for now."),
        ("My brain just went blank. Bear with me.", "My brain just went blank. Bear with me for a second."),
        ("What was the question again?", "Sorry, what was the question again? I lost it halfway through answering."),
        ("I've lost my thread.", "I've lost my thread — can someone remind me what I was building up to?"),
        ("It's gone.", "It's gone. I had the number in my head a second ago and now it's just gone."),
     ]),
    ("Untangling a sentence that's gone wrong",
     "You started a sentence that's grammatically gotten too complicated to finish cleanly.",
     "used when a sentence has gotten too tangled to finish, so you simplify and restart",
     [
        ("Sorry, that sentence got away from me. Let me try again.", "Sorry, that sentence got away from me. Let me try again: we need two more days."),
        ("...I'm tangling myself up. Simply put: [short sentence].", "...I'm tangling myself up. Simply put: the API is returning stale data."),
        ("Let me start that sentence again.", "Let me start that sentence again — that came out completely backwards."),
        ("...anyway, you get the idea — basically [short sentence].", "...anyway, you get the idea — basically, the fix isn't ready yet."),
        ("That came out more complicated than it needed to be.", "That came out more complicated than it needed to be — sorry, let me simplify."),
        ("Basically: ...", "Basically: the client wants the same feature, just faster."),
        ("In one sentence: ...", "In one sentence: we're behind, but it's recoverable."),
     ]),
    ("Recovering your train of thought",
     "You've lost track of the point you were building toward and need to find your way back.",
     "used when you've lost track of the point you were building toward and need to find your way back",
     [
        ("Hold on — what was I getting at?", "Hold on — what was I getting at? Sorry, I lost the thread there."),
        ("I'm going somewhere with this, I promise.", "I'm going somewhere with this, I promise — bear with me."),
        ("The reason I bring this up is...", "The reason I bring this up is that it directly affects the release date."),
        ("...anyway, the point I'm making is: [conclusion].", "...anyway, the point I'm making is: we can't skip QA this time."),
        ("Sorry, I went off on a tangent. Back to [topic].", "Sorry, I went off on a tangent. Back to the deployment plan."),
     ]),
    ("Cutting a rambling answer short",
     "You've been talking for a while and realize you need to wrap up your answer before you lose the listener.",
     "used to cut a rambling answer short before you lose the listener",
     [
        ("...but I'm rambling. In short: [one sentence].", "...but I'm rambling. In short: we're on track, just tight on time."),
        ("Let me land this: [conclusion].", "Let me land this: we need one more sprint before launch."),
        ("...I'll stop there. The headline is [X].", "...I'll stop there. The headline is: the migration is delayed by a week."),
        ("Sorry — long answer to a short question. The answer is [X].", "Sorry — long answer to a short question. The answer is yes, we can make the deadline."),
        ("Am I answering your question, or did you mean something else?", "Am I answering your question, or did you mean something else by 'scope'?"),
     ]),
    ("Correcting yourself after contradicting your own point",
     "You just realized what you're saying now contradicts what you said a moment ago.",
     "used when you realize what you're saying contradicts something you said moments ago",
     [
        ("Actually, that contradicts what I said earlier — let me think.", "Actually, that contradicts what I said earlier about the timeline — let me think."),
        ("Hang on, I'm arguing against myself. Let me be clearer.", "Hang on, I'm arguing against myself. Let me be clearer about what I actually mean."),
        ("I've just talked myself out of my own point.", "I've just talked myself out of my own point — maybe we shouldn't rush this after all."),
        ("Let me correct myself: earlier I said X, but actually Y.", "Let me correct myself: earlier I said the fix was live, but actually it's still in review."),
        ("I think I misspoke earlier. To be accurate: [X].", "I think I misspoke earlier. To be accurate: only two of the three tickets are done."),
     ]),
    ("Signaling you're moving on after a recovery",
     "You've just recovered from a stumble and want to signal you're back on track and moving forward.",
     "used right after a recovery, to signal you're back on track and moving forward",
     [
        ("Anyway.", "Anyway. So, back to the roadmap."),
        ("Moving on.", "Moving on. Let's look at the next item."),
        ("Where were we?", "Where were we? Right, the Q3 numbers."),
        ("Back to it.", "Back to it — sorry about that detour."),
     ]),
]

if __name__ == "__main__":
    generate_topic(
        out_path=OUT_PATH,
        exam_id="mid-sentence-breakdown",
        title="Chunk Atlas — Real-Time Fluency: Mid-Sentence Breakdown",
        tier_id=TIER_ID,
        tier_name=TIER_NAME,
        groups_def=groups_def,
    )
