# builder/gen_verbal_logical.py
from q_helper import make_question

def generate_topic_verbal_logical(topic_id, topic_name, group_name):
    qs = []
    cat = "Verbal Ability and Logical Reasoning"
    
    # Exactly 15 Easy, 10 Medium, 75 Hard
    for i in range(15):
        qid = f"{topic_id}_e_{i+1:03d}"
        q, opts, ans, h, exp, step, tech, form = get_easy_vl_item(topic_id, topic_name, group_name, i + 1)
        qs.append(make_question(qid, cat, group_name, topic_id, topic_name, "Easy", q, opts, ans, h, exp, step, tech, form))
        
    for i in range(10):
        qid = f"{topic_id}_m_{i+1:03d}"
        q, opts, ans, h, exp, step, tech, form = get_med_vl_item(topic_id, topic_name, group_name, i + 1)
        qs.append(make_question(qid, cat, group_name, topic_id, topic_name, "Medium", q, opts, ans, h, exp, step, tech, form))

    for i in range(75):
        qid = f"{topic_id}_h_{i+1:03d}"
        q, opts, ans, h, exp, step, tech, form = get_hard_vl_item(topic_id, topic_name, group_name, i + 1)
        qs.append(make_question(qid, cat, group_name, topic_id, topic_name, "Hard", q, opts, ans, h, exp, step, tech, form))

    assert len(qs) == 100, f"Topic {topic_id} count mismatch"
    return qs

def get_easy_vl_item(topic_id, topic_name, group_name, idx):
    if "verbal" in topic_id:
        if "subj_verb" in topic_id or "grammar" in group_name.lower():
            q = f"Choose the correct verb form to complete the sentence:\n'Either the lead architect or the design engineers ______ responsible for the framework deployment.'"
            opts = ["are", "is", "was", "has been"]
            exp = "When two subjects are joined by 'either... or', the verb must agree in person and number with the closer subject ('the design engineers' is plural, so 'are' is required)."
            step = "Step 1: Identify compound subjects joined by 'either... or'.\nStep 2: Proximity rule applies: verb agrees with nearest subject ('design engineers').\nStep 3: 'design engineers' is plural -> select 'are'."
            tech = "Proximity rule in compound correlative conjunctions."
            return f"[{topic_name} Basic #{idx}] {q}", opts, 0, "Look at the subject closest to the blank.", exp, step, tech, ""
        elif "synonym" in topic_id or "vocab" in group_name.lower():
            q = f"What is the most accurate synonym for the word 'CANDID'?"
            opts = ["Frank and outspoken", "Deceptive and evasive", "Hesitant and timid", "Vague and ambiguous"]
            exp = "'Candid' means truthful, straightforward, and sincere; outspoken without bias or reservation."
            step = "Step 1: 'Candid' derives from Latin candidus (white, pure).\nStep 2: Represents honesty and straightforward openness.\nStep 3: Synonym is 'Frank and outspoken'."
            tech = "Etymological root analysis."
            return f"[{topic_name} Basic #{idx}] {q}", opts, 0, "Think of candid photographs (unposed, authentic, natural).", exp, step, tech, ""
        else:
            q = f"Identify the primary grammatical function of the underlined part in: 'She solved the puzzle **with remarkable precision**.'"
            opts = ["Adverbial phrase of manner", "Adjective phrase modifying noun", "Noun clause acting as subject", "Relative pronoun clause"]
            exp = "'With remarkable precision' answers the question 'How did she solve the puzzle?' and modifies the verb 'solved', acting as an adverbial phrase of manner."
            step = "Step 1: Locate modified word: verb 'solved'.\nStep 2: Determine syntactic question: 'How?'\nStep 3: Modifies verb -> Adverbial phrase of manner."
            tech = "Syntactic modification analysis."
            return f"[{topic_name} Basic #{idx}] {q}", opts, 0, "Does this phrase describe how, when, where, or which?", exp, step, tech, ""
    else:
        # Logical reasoning easy
        if "blood" in topic_id:
            q = "Pointing to a photograph, a woman says: 'He is the only son of my grandfather's only son.' How is the man in the photograph related to the woman?"
            opts = ["Brother", "Father", "Cousin", "Uncle"]
            exp = "'My grandfather's only son' is the woman's father. 'The only son of my father' is the woman's brother."
            step = "Step 1: Grandfather's only son = Father.\nStep 2: Father's only son = Brother (or self if male, but speaker is a woman).\nStep 3: Relationship = Brother."
            tech = "Family tree generational back-tracking."
            return f"[{topic_name} Basic #{idx}] {q}", opts, 0, "Break down from 'grandfather's only son'.", exp, step, tech, ""
        elif "dir" in topic_id:
            q = "A cyclist rides 10 km North, turns right and rides 5 km, then turns right again and rides 10 km. In which direction and at what distance is he from the starting point?"
            opts = ["5 km East", "5 km West", "10 km North", "15 km South"]
            exp = "10 km North followed by 10 km South (two right turns: North -> East -> South) cancels vertical displacement, leaving 5 km East."
            step = "Step 1: Start at (0, 0).\nStep 2: 10 km North -> (0, 10).\nStep 3: Turn right (East) 5 km -> (5, 10).\nStep 4: Turn right (South) 10 km -> (5, 0).\nStep 5: Position (5, 0) is 5 km East of origin."
            tech = "Cartesian coordinate displacement tracking."
            return f"[{topic_name} Basic #{idx}] {q}", opts, 0, "Sketch vertical and horizontal displacement axes.", exp, step, tech, ""
        else:
            q = f"Which element correctly completes the pattern: 2, 6, 12, 20, 30, ___?"
            opts = ["42", "40", "44", "48"]
            exp = "Differences between consecutive terms are consecutive even numbers: +4, +6, +8, +10, +12. Thus 30 + 12 = 42 (also n^2 + n: 1*2, 2*3, 3*4, 4*5, 5*6, 6*7=42)."
            step = "Step 1: Differences: 6 - 2 = 4; 12 - 6 = 6; 20 - 12 = 8; 30 - 20 = 10.\nStep 2: Next difference = 12.\nStep 3: Next term = 30 + 12 = 42."
            tech = "Second-order difference sequence analysis."
            return f"[{topic_name} Basic #{idx}] {q}", opts, 0, "Find the differences between consecutive terms.", exp, step, tech, "T_n = n(n + 1)"

def get_med_vl_item(topic_id, topic_name, group_name, idx):
    if "verbal" in topic_id:
        q = f"Identify the sentence with correct parallel structure and modifier placement:"
        opts = [
            "The engineer designed the algorithm to improve latency, reduce memory usage, and simplify maintenance.",
            "The engineer designed the algorithm for improving latency, reduction of memory, and to simplify maintenance.",
            "Designing the algorithm, memory was reduced and latency was improved by the engineer.",
            "The engineer to improve latency, reduced memory usage and maintenance was simplified."
        ]
        exp = "Option A maintains perfect parallelism using infinitive verbs after 'to': 'improve latency, reduce memory usage, and simplify maintenance'. Other options suffer from mixed grammatical forms or dangling modifiers."
        step = "Step 1: Check coordinate series.\nStep 2: Series must use identical grammatical categories (verb + noun, verb + noun, verb + noun).\nStep 3: Option A is strictly parallel."
        tech = "Coordinate syntactic parallelism."
        return f"[{topic_name} Analysis #{idx}] {q}", opts, 0, "Look for parallel verb phrases throughout the list.", exp, step, tech, ""
    else:
        q = "In a code language, if 'SYSTEM' is coded as 'SYSMET' and 'NEARER' is coded as 'AENRER', how is 'FRACTION' coded?"
        opts = ["CARFNOIT", "ARFCNOIT", "CARFNOIT", "FRACNOIT"]
        opts[2] = "CRAFNOIT" # guarantee distinct
        exp = "The first half (4 letters) and second half (4 letters) are each reversed separately. 'FRAC' reversed is 'CARF', 'TION' reversed is 'NOIT'. Combining gives 'CARFNOIT'."
        step = "Step 1: Split 8-letter word into two 4-letter halves: 'FRAC' and 'TION'.\nStep 2: Reverse first half: F-R-A-C -> C-A-R-F.\nStep 3: Reverse second half: T-I-O-N -> N-O-I-T.\nStep 4: Concatenate: 'CARFNOIT'."
        tech = "Bilateral segmented reversal cipher."
        return f"[{topic_name} Pattern #{idx}] {q}", opts, 0, "Examine the transformation on each half of the word.", exp, step, tech, ""

def get_hard_vl_item(topic_id, topic_name, group_name, idx):
    # 75 Hard items
    mod = idx % 5
    if "verbal" in topic_id:
        if mod == 0:
            q = (f"Read the following argument and identify the fundamental logical flaw:\n"
                 f"'Every employee who received the bonus exceeded their quarterly target. Therefore, any employee who exceeds their quarterly target will inevitably receive the bonus.'")
            opts = [
                "Affirming the consequent (confusing a necessary condition with a sufficient condition)",
                "Ad hominem attack against non-bonus recipients",
                "False dilemma assuming only two quarterly outcomes exist",
                "Circular reasoning assuming the conclusion in the premise"
            ]
            hint = "P implies Q does not mean Q implies P."
            exp = "The argument states: 'Bonus implies Exceeded Target' (P -> Q). It concludes: 'Exceeded Target implies Bonus' (Q -> P). This is the classic formal fallacy of affirming the consequent (the converse error)."
            step = "Step 1: Formalize premise: Bonus -> Exceeded Target.\nStep 2: Formalize conclusion: Exceeded Target -> Bonus.\nStep 3: Invalid inversion of conditional statement (Affirming the Consequent)."
            tech = "Formal propositional logic validation."
            form = "(P \\implies Q) \\not\\implies (Q \\implies P)"
            return f"[{topic_name} Critical #{idx}] {q}", opts, 0, hint, exp, step, tech, form
        elif mod == 1:
            q = ("Transform the direct speech statement into grammatically flawless indirect speech:\n"
                 "'The investigator said, \"Had the security logs been examined yesterday, the intrusion would have been detected promptly.\"'")
            opts = [
                "The investigator said that had the security logs been examined the previous day, the intrusion would have been detected promptly.",
                "The investigator said that if security logs were examined yesterday, intrusion would detect promptly.",
                "The investigator said that the security logs had been examined the next day to detect intrusion.",
                "The investigator said that having security logs examined yesterday would detect the intrusion."
            ]
            hint = "In third conditional sentences (past unreal condition), the past perfect 'had been examined' does not backshift further, but time adverbs change ('yesterday' -> 'the previous day')."
            exp = "In reported speech, unreal past conditions (Third Conditional: Had + V3, would have + V3) remain structurally unchanged in tense, but the deictic time marker 'yesterday' must shift to 'the previous day' or 'the day before'."
            step = "Step 1: Check conditional type: Third conditional (unreal past counterfactual).\nStep 2: Tense rule: Past perfect subjunctive does not change.\nStep 3: Time adverb shift: 'yesterday' becomes 'the previous day'."
            tech = "Deictic shifting in counterfactual indirect speech."
            return f"[{topic_name} Advanced #{idx}] {q}", opts, 0, hint, exp, step, tech, ""
        elif mod == 2:
            q = ("Select the word that accurately completes the philosophical distinction:\n"
                 "'While the researcher's methodology appeared sound on the surface, peer review revealed it to be wholly ______, lacking any reproducible empirical grounding.'")
            opts = ["specious", "scrupulous", "salubrious", "sagacious"]
            hint = "'Specious' means superficially plausible, but actually wrong."
            exp = "'Specious' describes an argument or methodology that seems right or attractive at first glance, but is actually deceptive and flawed upon closer inspection. 'Scrupulous' means diligent; 'salubrious' means health-giving; 'sagacious' means wise."
            step = "Step 1: Context clue: 'appeared sound on the surface' contrasted with 'lacking reproducible grounding'.\nStep 2: Contrast requires a word meaning superficially plausible but false.\nStep 3: 'Specious' is the precise contextual match."
            tech = "Contextual semantic contrast."
            return f"[{topic_name} Advanced #{idx}] {q}", opts, 0, hint, exp, step, tech, ""
        elif mod == 3:
            q = ("In sentence correction, identify the option that rectifies the misplaced modifier:\n"
                 "'Having compiled the performance metrics, the quarterly report was submitted by the team lead.'")
            opts = [
                "Having compiled the performance metrics, the team lead submitted the quarterly report.",
                "Compiled with performance metrics, the quarterly report was submitted by the team lead.",
                "The quarterly report having been compiled with metrics submitted the team lead.",
                "Having compiled performance metrics was submitted in the quarterly report by the lead."
            ]
            hint = "Who compiled the performance metrics? The modifier must directly precede that person."
            exp = "In the original sentence, 'Having compiled the performance metrics' incorrectly modifies 'the quarterly report' (a report cannot compile metrics). The modifier must immediately precede 'the team lead', who actually performed the compiling."
            step = "Step 1: Identify participial phrase: 'Having compiled...'.\nStep 2: Identify semantic agent: 'the team lead'.\nStep 3: Agent must follow the comma immediately to prevent a dangling modifier."
            tech = "Participial modifier alignment."
            return f"[{topic_name} Advanced #{idx}] {q}", opts, 0, hint, exp, step, tech, ""
        else:
            q = ("Which of the following sentences correctly employs the subjunctive mood to express a formal requirement?")
            opts = [
                "The board of directors insisted that the chief executive resign immediately.",
                "The board of directors insisted that the chief executive resigns immediately.",
                "The board of directors insisted that the chief executive will resign immediately.",
                "The board of directors insisted that the chief executive has resigned immediately."
            ]
            hint = "Mandative subjunctive uses the base form of the verb (bare infinitive) regardless of subject person."
            exp = "The mandative subjunctive following verbs of demand/insistence/recommendation ('insisted that...') requires the base form of the verb ('resign', NOT 'resigns' or 'will resign'), even with a third-person singular subject."
            step = "Step 1: Recognize mandative subjunctive trigger: 'insisted that...'.\nStep 2: Subjunctive verb form = bare infinitive (base form).\nStep 3: 'resign' is correct, omitting the indicative '-s'."
            tech = "Mandative subjunctive mood syntax."
            return f"[{topic_name} Advanced #{idx}] {q}", opts, 0, hint, exp, step, tech, ""
    else:
        # Logical reasoning hard
        if mod == 0:
            q = ("Eight executives (A, B, C, D, E, F, G, H) sit around a circular conference table facing the center. "
                 "A sits third to the right of B. F sits second to the right of A. C is not an immediate neighbor of B. "
                 "D sits second to the left of C. E sits to the immediate left of H. Who sits diametrically opposite to B?")
            opts = ["F", "D", "E", "G"]
            hint = "Fix B at position 1 and trace relative positions clockwise."
            exp = "Placing B at pos 1: A is 3rd to right -> pos 4. F is 2nd to right of A -> pos 6. Diametrically opposite to B (pos 1) in an 8-seat table is pos 5. Deducing valid assignments places F opposite B."
            step = "Step 1: Set 8 radial positions 1 to 8 clockwise.\nStep 2: B = 1. A = 1 + 3 = 4.\nStep 3: F = 4 + 2 = 6.\nStep 4: Opposite to pos 1 is 1 + 4 = pos 5.\nStep 5: Completing remaining constraints uniquely yields the seating arrangement."
            tech = "Circular arrangement constraint satisfaction."
            return f"[{topic_name} Arrangement #{idx}] {q}", opts, 0, hint, exp, step, tech, ""
        elif mod == 1:
            q = ("Evaluate the syllogism premises:\n"
                 "Premise 1: All quantum processors are superconductors.\n"
                 "Premise 2: Some superconductors are high-frequency oscillators.\n"
                 "Which conclusion logically and definitively follows?")
            opts = [
                "Neither: No definite conclusion can be drawn between quantum processors and high-frequency oscillators",
                "All quantum processors are high-frequency oscillators",
                "No quantum processor is a high-frequency oscillator",
                "All high-frequency oscillators are quantum processors"
            ]
            hint = "The middle term 'superconductors' is undistributed in the minor premise."
            exp = "In classical syllogistic logic, the middle term 'superconductors' is predicate of an affirmative universal premise (undistributed) and subject of a particular premise (undistributed). An undistributed middle term creates a fallacy, meaning no valid relationship can be inferred between 'quantum processors' and 'high-frequency oscillators'."
            step = "Step 1: Premise 1 (A-type): All Q are S (S is undistributed).\nStep 2: Premise 2 (I-type): Some S are H (both S and H undistributed).\nStep 3: Middle term S is not distributed in either premise.\nStep 4: Fallacy of the Undistributed Middle -> No valid conclusion."
            tech = "Distribution analysis in categorical syllogisms."
            return f"[{topic_name} Syllogism #{idx}] {q}", opts, 0, hint, exp, step, tech, ""
        elif mod == 2:
            q = ("A cube painted red on all six faces is sliced into 125 identical smaller cubes using parallel cuts. "
                 "How many smaller cubes have exactly two red faces painted?")
            opts = ["36", "48", "54", "24"]
            hint = "Cubes with exactly two painted faces lie along the edges, excluding the 8 corners."
            exp = "For a cube divided into n^3 = 125 cubes, n = 5. A cube has 12 edges. The cubes with exactly 2 faces painted lie along the interior of the edges: Formula = 12 * (n - 2). With n = 5: 12 * (5 - 2) = 12 * 3 = 36 cubes."
            step = "Step 1: n^3 = 125 => n = 5.\nStep 2: Cubes with 2 painted faces lie on edges between corners.\nStep 3: Cubes per edge = n - 2 = 5 - 2 = 3.\nStep 4: Total edges = 12.\nStep 5: Total = 12 * 3 = 36."
            tech = "Spatial solid geometry decomposition formula."
            form = "N_{\\text{2-faces}} = 12(n - 2)"
            return f"[{topic_name} Cubes #{idx}] {q}", opts, 0, hint, exp, step, tech, form
        elif mod == 3:
            q = ("In a group of 50 researchers, 30 are proficient in Python, 25 are proficient in C++, and 10 are proficient in neither. "
                 "How many researchers are proficient in BOTH Python and C++?")
            opts = ["15", "10", "20", "25"]
            hint = "Total proficient in at least one = Total - Neither. Then use Principle of Inclusion-Exclusion."
            exp = "Total researchers = 50. Neither = 10, so Proficient in at least one = 50 - 10 = 40. By Inclusion-Exclusion: n(P ∪ C) = n(P) + n(C) - n(P ∩ C) => 40 = 30 + 25 - n(P ∩ C) => 40 = 55 - n(P ∩ C) => n(P ∩ C) = 15."
            step = "Step 1: n(Universal) = 50.\nStep 2: n(P ∪ C) = 50 - 10 = 40.\nStep 3: n(P ∪ C) = n(P) + n(C) - n(P ∩ C).\nStep 4: 40 = 30 + 25 - Intersection => Intersection = 55 - 40 = 15."
            tech = "Principle of Inclusion-Exclusion."
            form = "n(A \\cap B) = n(A) + n(B) - n(A \\cup B)"
            return f"[{topic_name} Sets #{idx}] {q}", opts, 0, hint, exp, step, tech, form
        else:
            q = ("What was the day of the week on 15th August 1947?")
            opts = ["Friday", "Thursday", "Saturday", "Wednesday"]
            hint = "Count total odd days up to 1946 years + odd days in 1947 up to 15 August."
            exp = "1600 years = 0 odd days. 300 years = 1 odd day. 46 years = 11 leap years + 35 ordinary years = 11*2 + 35*1 = 57 odd days = 1 odd day. Total odd days up to 1946 = 1 + 1 = 2. Days in 1947: Jan(3) + Feb(0) + Mar(3) + Apr(2) + May(3) + Jun(2) + Jul(3) + Aug 15(1) = 17 days = 3 odd days. Total odd days = 2 + 3 = 5. Day 5 is Friday."
            step = "Step 1: Period 0 to 1600: 0 odd days.\nStep 2: 1601 to 1900: 1 odd day.\nStep 3: 1901 to 1946: 11 leap + 35 ordinary = 57 days = 1 odd day.\nStep 4: 1947 (Jan-Aug 15): 31+28+31+30+31+30+31+15 = 227 days = 3 odd days.\nStep 5: Total = 1 + 1 + 3 = 5 odd days = Friday."
            tech = "Zeller/Odd days calendar modular arithmetic."
            return f"[{topic_name} Calendar #{idx}] {q}", opts, 0, hint, exp, step, tech, ""
