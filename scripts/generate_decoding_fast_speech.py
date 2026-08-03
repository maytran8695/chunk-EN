import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from lib import generate_topic

OUT_PATH = os.path.join(SCRIPT_DIR, "..", "data", "decoding-fast-speech.json")

# Phrase content copied by hand from "The Ear: Decoding Fast Speech" topic
# (tier "presence" / nav tab "Voice & Presence") — sections P3.1-P3.4, V3.6.
# P3.5 is skipped entirely: it's pure exercise-strategy advice (dictation,
# word-counting, slow-to-fast playback) with no quotable English chunk.
# Several source lines bundle multiple full-form/reduced-form pairs
# separated by "|" or ";" — these are split into separate phrase entries,
# the same way "/"-separated alternatives are split elsewhere, since each
# pair is a genuinely distinct chunk to recognize. P3.2's reduction pairs
# are grouped by the meaning they reduce (future/desire/obligation/etc.)
# rather than lumped into one giant group, so a question's distractors are
# other reduced forms with a different underlying meaning — real discrimination.
TIER_ID = "presence"
TIER_NAME = "Voice & Presence"

groups_def = [
    ("Whole-phrase blending",
     "You hear a fast native speaker say something that sounds like one blended block, not several separate words — you need to recognize the phrase as a whole.",
     "used to illustrate that native speech chunks whole phrases into blended sound-blocks rather than clearly separated words",
     [
        ("make a cup of tea",
         'Fancy a brew?" — she was already moving to **make a cup of tea**, the phrase blurring into three quick blocks: /meɪkə kʌpə tiː/.'),
     ]),
    ("Reduction: gonna",
     "You hear someone announce a future plan or intention, and the words 'going to' have blurred into one quick syllable.",
     "used as the fast-speech reduction of 'going to', signaling a future plan or intention",
     [
        ("gonna",
         'I\'m **gonna** call the client after lunch." — heard fast, \'going to\' collapses into \'gonna\'.'),
     ]),
    ("Reduction: wanna",
     "You hear someone express what they want to do, and 'want to' has blurred into one syllable.",
     "used as the fast-speech reduction of 'want to', expressing desire or preference",
     [
        ("wanna",
         'Do you **wanna** grab lunch before the call?" — \'want to\' reduces to \'wanna\' in casual speech.'),
     ]),
    ("Reduction: obligation",
     "You hear someone talk about something they're obligated to do, and 'have to' or 'got to' has collapsed into one blended syllable.",
     "used as the fast-speech reduction of 'have to' or 'got to', expressing obligation",
     [
        ("hafta",
         'I **hafta** finish this before five." — \'have to\' reduces to \'hafta\'.'),
        ("gotta",
         'We\'ve **gotta** move this meeting." — \'got to\' reduces to \'gotta\'.'),
     ]),
    ("Reduction: everyday verbs",
     "You hear a short, blended sound where a common verb phrase like 'don't know', 'let me', or 'give me' used to be.",
     "used as the fast-speech reduction of common verb phrases like 'don't know', 'let me', or 'give me'",
     [
        ("dunno",
         'Honestly, I **dunno** what he meant by that." — \'don\'t know\' collapses to \'dunno\'.'),
        ("lemme",
         '**Lemme** take a look at that file." — \'let me\' reduces to \'lemme\'.'),
        ("gimme",
         '**Gimme** a second, I\'ll pull up the numbers." — \'give me\' reduces to \'gimme\'.'),
     ]),
    ("Reduction: hedging",
     "You hear someone soften a claim with a quick blended syllable where 'kind of' or 'sort of' used to be.",
     "used as the fast-speech reduction of hedging phrases 'kind of' and 'sort of'",
     [
        ("kinda",
         'It\'s **kinda** late to change the plan now." — \'kind of\' reduces to \'kinda\'.'),
        ("sorta",
         'I\'m **sorta** worried about the timeline." — \'sort of\' reduces to \'sorta\'.'),
     ]),
    ("Reduction: quantity & cause",
     "You hear a blended syllable standing in for a common quantity phrase like 'a lot of', 'out of', or the word 'because'.",
     "used as the fast-speech reduction of 'a lot of', 'out of', or 'because'",
     [
        ("a lotta",
         'There\'s **a lotta** feedback to go through before Friday." — \'a lot of\' reduces to \'a lotta\'.'),
        ("outta",
         'We\'re **outta** time for this discussion." — \'out of\' reduces to \'outta\'.'),
        ("cuz",
         'We delayed it **cuz** the vendor missed the deadline." — \'because\' reduces to \'cuz\'.'),
     ]),
    ("Reduction: modal-perfect",
     "You hear a modal verb followed by a quick unstressed syllable where 'have' used to be, in a sentence about a hypothetical past.",
     "used as the fast-speech reduction of 'would have', 'should have', or 'could have' in hypothetical statements about the past",
     [
        ("would've",
         'I **would\'ve** told you sooner if I\'d known." — \'would have\' reduces to \'would\'ve\'.'),
        ("should've",
         'We **should\'ve** tested this before launch." — \'should have\' reduces to \'should\'ve\'.'),
        ("could've",
         'They **could\'ve** warned us earlier." — \'could have\' reduces to \'could\'ve\'.'),
     ]),
    ("Reduction: question openers",
     "You hear a fast question opener where 'what are you', 'what do you', 'did you', or 'would you' has fused into one quick sound.",
     "used as the fast-speech reduction of common question openers like 'what are/do you', 'did you', or 'would you'",
     [
        ("whaddaya",
         '**Whaddaya** think of the new layout?" — \'what do you\' fuses into \'whaddaya\'.'),
        ("didja",
         '**Didja** send the invoice yet?" — \'did you\' fuses into \'didja\'.'),
        ("wouldja",
         '**Wouldja** mind forwarding that email?" — \'would you\' fuses into \'wouldja\'.'),
     ]),
    ("Extreme reduction",
     "You hear someone respond with almost no consonants at all — just a fast rise and fall of pitch — where a full sentence used to be.",
     "used to illustrate the extreme end of reduction: 'I don't know' can shrink to almost no consonants, just a pitch contour",
     [
        ("I don't know (barely three pitch notes)",
         'I don\'t know," she said, so fast and reduced it came out as barely three notes of pitch, no consonants audible at all.'),
     ]),
    ("Weak forms",
     "You hear a fast native sentence where a small grammatical word — a preposition, conjunction, or auxiliary — has been swallowed down to a bare schwa sound.",
     "used to illustrate that common function words (prepositions, conjunctions, auxiliaries) weaken to a schwa sound /ə/ in connected speech and are easy to miss",
     [
        ("to", 'I\'m going **to** call him." — \'to\' shrinks to /tə/, almost disappearing.'),
        ("for", 'This is **for** you." — \'for\' weakens to /fə/ in fast speech.'),
        ("of", 'A cup **of** tea." — \'of\' reduces to /əv/ or just /ə/.'),
        ("and", 'Fish **and** chips." — \'and\' can shrink to a single /n/ sound.'),
        ("can", 'We **can** fix that today." — \'can\' weakens to /kən/, almost inaudible.'),
        ("was", 'It **was** already sent." — \'was\' reduces to /wəz/.'),
        ("are", 'They **are** on their way." — \'are\' shrinks to just /ə/.'),
        ("have", 'We **have** to check first." — \'have\' reduces to /əv/.'),
        ("at", 'Meet me **at** noon." — \'at\' weakens to /ət/.'),
     ]),
    ("Weak forms in fixed phrases",
     "You hear a familiar two-part everyday phrase where the little connecting word in the middle has almost vanished.",
     "used to illustrate how the connecting word inside a fixed everyday phrase (like 'and' or 'of') almost disappears in fast speech",
     [
        ("fish and chips",
         'Let\'s grab **fish and chips** on the way home." — \'and\' shrinks to a single /n/ sound: /fɪʃ n̩ tʃɪps/.'),
        ("cup of tea",
         'Fancy a **cup of tea**?" — \'of\' reduces to just /ə/: /kʌpə tiː/.'),
     ]),
    ("Catenation",
     "You hear a short phrase where the final consonant of one word glides straight into the vowel that starts the next word, erasing the word boundary.",
     "used to illustrate catenation: a final consonant links into the next word's vowel, blurring the boundary between words",
     [
        ("turn it off",
         'Can you **turn it off**?" — heard as one glided block, /tɜːnɪtɒf/, with no gap between the words.'),
     ]),
    ("Assimilation",
     "You hear two words blend so that one sound shifts to match the sound next to it, producing a completely different consonant.",
     "used to illustrate assimilation: a sound changes to match its neighboring sound, producing a blended consonant",
     [
        ("did you",
         '**Did you** finish the report?" — heard as /dɪdʒə/, the \'d\' and \'y\' merging into a \'j\' sound.'),
        ("meet you",
         'Nice to **meet you**." — heard as /miːtʃə/, the \'t\' and \'y\' merging into a \'ch\' sound.'),
        ("ten boys",
         'There were **ten boys** in the room." — heard as /tem bɔɪz/, the \'n\' shifting to an \'m\' before the \'b\'.'),
     ]),
    ("Elision",
     "You hear a word where a whole consonant sound has dropped out completely, not just weakened.",
     "used to illustrate elision: a consonant sound disappears completely rather than just weakening",
     [
        ("next day",
         'Let\'s follow up the **next day**." — heard as /neks deɪ/, the \'t\' disappearing entirely.'),
        ("friendship",
         'They built a real **friendship** over the years." — heard as /frenʃɪp/, the \'d\' dropping out.'),
        ("asked",
         'I already **asked** him twice." — heard as /ɑːst/, the \'k\' disappearing.'),
     ]),
    ("Fast-speech phrase recognition",
     "You hear a common everyday phrase compressed into a fast, blended spoken form, and need to recognize the phrase it actually is.",
     "used to illustrate a common phrase's fast, blended spoken form that learners often fail to recognize",
     [
        ("Do you want to...?",
         '**Do you want to** grab lunch?" — spoken fast, this comes out as \'D\'you wanna grab lunch?\''),
        ("What do you think?",
         '**What do you think?**" — spoken fast, this comes out as \'Whaddaya think?\''),
        ("Did you get it?",
         '**Did you get it?**" — spoken fast, this comes out as /dɪdʒə gedɪt/, \'Didja gedit?\''),
        ("I don't know.",
         '**I don\'t know.**" — spoken fast, this can shrink all the way down to just \'dunno\'.'),
        ("Let me have a look.",
         '**Let me have a look.**" — spoken fast, this comes out as \'Lemme av\'a look.\''),
        ("Give me a minute.",
         '**Give me a minute.**" — spoken fast, this comes out as \'Gimme a minute.\''),
        ("Come on!",
         '**Come on!**" — spoken fast, this comes out as one blended syllable, \'C\'mon!\''),
        ("How is it going?",
         '**How is it going?**" — spoken fast, this comes out as \'Howzit goin\'?\''),
        ("A lot of people",
         '**A lot of people** showed up." — spoken fast, this comes out as \'A lotta people.\''),
        ("Should have known",
         'I **should have known** better." — spoken fast, this comes out as \'shoulda known\' — not \'should of\', even though it sounds like it.'),
        ("What are you up to?",
         '**What are you up to** this weekend?" — spoken fast, this comes out as \'Whatcha up to?\''),
        ("Nice to meet you",
         '**Nice to meet you**." — spoken fast, this comes out as \'Nice ta meetcha.\''),
     ]),
]

if __name__ == "__main__":
    generate_topic(
        out_path=OUT_PATH,
        exam_id="decoding-fast-speech",
        title="Chunk Atlas — Voice & Presence: Decoding Fast Speech",
        tier_id=TIER_ID,
        tier_name=TIER_NAME,
        groups_def=groups_def,
    )
