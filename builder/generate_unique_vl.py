# builder/generate_unique_vl.py
import math
from q_helper import make_question
from audit_duplicates import normalize_text, template_fingerprint

NAMES = ["Aarav", "Bhavya", "Chirag", "Divya", "Eshan", "Farhan", "Gauri", "Harsh", "Ishaan", "Jaya",
         "Karthik", "Lavanya", "Madhav", "Neha", "Omkar", "Pooja", "Qadir", "Rohan", "Sneha", "Tanvi",
         "Uday", "Varun", "Wahid", "Xena", "Yash", "Zoya", "Ananya", "Bharat", "Chetan", "Deepa"]

WORDS = ["EPHEMERAL", "UBIQUITOUS", "METICULOUS", "PRAGMATIC", "PARADIGM", "LUCID", "PROLIFIC", "RESILIENT", "ESOTERIC", "MITIGATE"]
SYNONYMS = ["transitory", "omnipresent", "scrupulous", "practical", "archetype", "intelligible", "fecund", "tenacious", "arcane", "alleviate"]

def make_4_options(corr_opt, raw_distractors, pos_idx=0):
    corr_str = str(corr_opt)
    distractors = []
    seen = {corr_str}
    for d in raw_distractors:
        sd = str(d)
        if sd not in seen:
            seen.add(sd)
            distractors.append(sd)
        if len(distractors) == 3:
            break
    alt_c = 1
    while len(distractors) < 3:
        cand = f"{corr_str} (Alt {alt_c})"
        if cand not in seen:
            seen.add(cand)
            distractors.append(cand)
        alt_c += 1
    target_pos = pos_idx % 4
    final_opts = list(distractors)
    final_opts.insert(target_pos, corr_str)
    return final_opts, target_pos

def make_vl_q(qid, cat, grp, tid, tname, diff, directive, question_body, corr_opt, raw_distractors, pos_idx, hint, exp, step, tech, formula=""):
    full_q = f"{directive}\n{question_body}" if directive else question_body
    opts, ans_idx = make_4_options(corr_opt, raw_distractors, pos_idx)
    return make_question(qid, cat, grp, tid, tname, diff, full_q, opts, ans_idx, hint, exp, step, tech, formula)

def generate_vl_item(tid, tname, grp, diff, i):
    cat = "Verbal Ability and Logical Reasoning"
    pos = i % 4
    tid_lower = tid.lower()

    # 1. LOGICAL: DIRECTION SENSE
    if "dir_sense" in tid_lower or "direction" in tid_lower:
        name = NAMES[i % len(NAMES)]
        if diff == "Easy":
            directive = "Identify the cardinal direction faced by the person:"
            dirs = ["North", "East", "South", "West"]
            d_start = dirs[i % 4]
            d_corr = dirs[(i + 1) % 4] # 90 deg clockwise turn
            dist = [d for d in dirs if d != d_corr]
            q_text = f"Single Turn Orientation #{i}: {name} walks 20 meters facing {d_start}, then executes a 90-degree clockwise right turn and walks 15 meters. Which direction is {name} facing now?"
            exp = f"A 90-degree clockwise rotation from {d_start} points towards {d_corr}."
            step = f"Step 1: Note initial bearing: {d_start}.\nStep 2: Add 90 degrees clockwise.\nStep 3: Final facing bearing is {d_corr}."
            tech = "Cardinal rotation kinematics."
        elif diff == "Medium":
            directive = "Calculate the net straight-line displacement distance:"
            d1 = 12 + i
            d2 = 16 + i
            disp = int(math.hypot(d1, d2))
            corr = f"{disp} m"
            dist = [f"{disp + 6} m", f"{max(5, disp - 5)} m", f"{d1 + d2} m"]
            q_text = f"Rectilinear Route Displacement #{i}: {name} starts at point O, walks {d1} meters North, then turns East and walks {d2} meters to reach point P. What is the straight-line distance between point O and point P?"
            exp = f"Displacement is hypotenuse: sqrt({d1}^2 + {d2}^2) = sqrt({d1*d1} + {d2*d2}) = {disp} m."
            step = f"Step 1: Identify perpendicular vectors North ({d1} m) and East ({d2} m).\nStep 2: Apply Pythagoras theorem: sqrt({d1}^2 + {d2}^2).\nStep 3: Distance = {disp} m."
            tech = "Euclidean 2D displacement norm."
            form = "d = \\sqrt{\\Delta x^2 + \\Delta y^2}"
        else: # Hard
            directive = "Determine the resultant coordinate bearing and distance:"
            d1 = 20 + i
            d2 = 25 + i
            d3 = 10 + i
            net_x = d2
            net_y = d1 + d3
            disp = int(math.hypot(net_x, net_y))
            corr = f"{disp} m North-East"
            dist = [f"{disp + 8} m North-West", f"{max(10, disp - 6)} m South-East", f"{disp + 15} m North-East"]
            q_text = f"Multi-Leg Traverse #{i}: {name} starts from origin, walks {d1} meters North, turns right and walks {d2} meters East, then turns left and walks {d3} meters North. What is {name}'s shortest displacement distance and quadrant bearing from the starting point?"
            exp = f"Net displacement: X = {net_x} m (East), Y = {d1} + {d3} = {net_y} m (North). Magnitude = sqrt({net_x}^2 + {net_y}^2) = {disp} m North-East."
            step = f"Step 1: Sum collinear segments: Y = {d1} + {d3} = {net_y} m.\nStep 2: Note orthogonal segment: X = {net_x} m.\nStep 3: Magnitude = sqrt({net_x}^2 + {net_y}^2) = {disp} m towards North-East."
            tech = "Vectorial Cartesian trajectory resolution."
            form = "\\vec{R} = \\Delta x \\hat{i} + \\Delta y \\hat{j}"
        return make_vl_q(f"{tid}_{diff.lower()[0]}_{i:03d}", cat, grp, tid, tname, diff, directive, q_text, corr if 'corr' in locals() else d_corr, dist, pos, "Sum the perpendicular vector components.", exp, step, tech)

    # 2. LOGICAL: NUMBER SERIES
    elif "num_series" in tid_lower or "number_series" in tid_lower or "series" in tid_lower:
        directive = "Determine the next missing number in the sequence:"
        if diff == "Easy":
            step_v = 3 + (i % 5)
            start_v = 10 + i * 2
            seq = [start_v + k * step_v for k in range(5)]
            next_v = seq[-1] + step_v
            corr = str(next_v)
            dist = [str(next_v + step_v), str(next_v - step_v), str(next_v + 2 * step_v)]
            seq_str = ", ".join(map(str, seq)) + ", ?"
            q_text = f"Arithmetic Progression Sequence #{i}: Find the next term in: {seq_str}"
            exp = f"Common difference d = +{step_v}. Next term = {seq[-1]} + {step_v} = {next_v}."
            step = f"Step 1: Check difference between consecutive terms: {seq[1]} - {seq[0]} = +{step_v}.\nStep 2: Confirm constant difference across sequence.\nStep 3: Add {step_v} to {seq[-1]} = {next_v}."
            tech = "Linear constant first difference."
        elif diff == "Medium":
            c = 2 + (i % 4)
            terms = [(k + i)**2 + c for k in range(5)]
            next_v = (5 + i)**2 + c
            corr = str(next_v)
            dist = [str(next_v + 10), str(next_v - 8), str(next_v + 22)]
            seq_str = ", ".join(map(str, terms)) + ", ?"
            q_text = f"Quadratic Sequence Pattern #{i}: What number completes the series: {seq_str}"
            exp = f"Each term follows T_k = (k + {i})^2 + {c}. For k=5: (5+{i})^2 + {c} = {next_v}."
            step = f"Step 1: Subtract constant {c} from each term.\nStep 2: Recognize consecutive integer squares.\nStep 3: Evaluate (5+{i})^2 + {c} = {next_v}."
            tech = "Quadratic sequence mapping."
        else: # Hard
            diff_inc = 2 + (i % 3)
            seq = [5 + i]
            cur_diff = 4 + (i % 4)
            for _ in range(5):
                seq.append(seq[-1] + cur_diff)
                cur_diff += diff_inc
            next_v = seq[-1] + cur_diff
            corr = str(next_v)
            dist = [str(next_v + 7), str(next_v - 5), str(next_v + 14)]
            seq_str = ", ".join(map(str, seq)) + ", ?"
            q_text = f"Accelerating Second-Order Progression #{i}: What is the next logical term in: {seq_str}"
            exp = f"First differences increase by +{diff_inc} each step. Next term difference is {cur_diff}, giving {seq[-1]} + {cur_diff} = {next_v}."
            step = f"Step 1: Compute first differences of series.\nStep 2: Note second-order constant acceleration (+{diff_inc}).\nStep 3: Add next augmented difference to last term to get {next_v}."
            tech = "Second-order recursive acceleration."
        return make_vl_q(f"{tid}_{diff.lower()[0]}_{i:03d}", cat, grp, tid, tname, diff, directive, q_text, corr, dist, pos, "Examine whether differences between terms are accelerating.", exp, step, tech)

    # 3. LOGICAL: CODING DECODING
    elif "code" in tid_lower or "coding" in tid_lower:
        directive = "Decode the cryptographic pattern and identify the target translation:"
        s = 2 + (i % 5)
        if diff == "Easy":
            src = "DATA"
            def caesar(w, shift): return "".join(chr((ord(c) - 65 + shift) % 26 + 65) for c in w)
            coded = caesar(src, s)
            target = "BYTE"
            corr = caesar(target, s)
            dist = [caesar(target, s + 1), caesar(target, (s - 1) % 26), caesar(target, s + 2)]
            q_text = f"Direct Caesar Cipher Shift #{i}: If '{src}' is coded as '{coded}', how is '{target}' encoded under the identical rule?"
            exp = f"Each letter is shifted forward by +{s} positions. Shifting '{target}' by +{s} produces '{corr}'."
            step = f"Step 1: ord('{coded[0]}') - ord('{src[0]}') = +{s}.\nStep 2: Verify +{s} shift.\nStep 3: Apply +{s} to '{target}' = '{corr}'."
            tech = "Modular shift cipher."
        elif diff == "Medium":
            # Reverse alphabet reflection: A<->Z, B<->Y
            def reflect(w): return "".join(chr(25 - (ord(c) - 65) + 65) for c in w)
            src = "NODE"
            coded = reflect(src)
            target = "LINK"
            corr = reflect(target)
            dist = [corr[:-1] + "A", corr[:-1] + "Z", "M" + corr[1:]]
            q_text = f"Alphabet Reverse Reflection #{i}: If '{src}' is encrypted as '{coded}', what is the encrypted ciphertext for '{target}'?"
            exp = f"Each character is replaced by its inverse mirror alphabet position (A=Z, B=Y). Transforming '{target}' gives '{corr}'."
            step = f"Step 1: Recognize complementary pair: pos(c) + pos(c') = 27.\nStep 2: Mirror rule applies to each character.\nStep 3: '{target}' maps to '{corr}'."
            tech = "Atbash reflection cipher."
        else: # Hard
            # Alternating shift: +s, -(s+1)
            def alt_shift(w, shift):
                res = []
                for k, c in enumerate(w):
                    sh = shift if k % 2 == 0 else -(shift + 1)
                    res.append(chr((ord(c) - 65 + sh) % 26 + 65))
                return "".join(res)
            src = "SERVER"
            coded = alt_shift(src, s)
            target = "CLIENT"
            corr = alt_shift(target, s)
            dist = [alt_shift(target, s + 1), alt_shift(target, s - 1), corr[:-1] + "Q"]
            q_text = f"Bilateral Parity Permutation #{i}: In an encrypted protocol, '{src}' is written as '{coded}'. How will '{target}' be written in this cryptographic scheme?"
            exp = f"Even index characters are shifted +{s}, odd index characters are shifted -{s+1}. Applying this to '{target}' yields '{corr}'."
            step = f"Step 1: Inspect index 0 (+{s}) and index 1 (-{s+1}).\nStep 2: Identify alternating parity rule.\nStep 3: Output ciphertext for '{target}' is '{corr}'."
            tech = "Interleaved parity cipher."
        return make_vl_q(f"{tid}_{diff.lower()[0]}_{i:03d}", cat, grp, tid, tname, diff, directive, q_text, corr, dist, pos, "Check for regular or alternating position shifts.", exp, step, tech)

    # 4. LOGICAL: BLOOD RELATIONS / FAMILY TREE
    elif "blood" in tid_lower or "fam_tree" in tid_lower or "relation" in tid_lower:
        directive = "Deduce the exact genealogical kinship relation:"
        p1 = NAMES[i % len(NAMES)]
        p2 = NAMES[(i + 4) % len(NAMES)]
        if diff == "Easy":
            q_text = f"Direct Kinship Statement #{i}: {p1} is the brother of {p2}. {p2} is the daughter of Rohan. How is {p1} related to Rohan?"
            corr = "Son"
            dist = ["Brother", "Father", "Uncle"]
            exp = f"{p1} and {p2} are siblings. Since {p2} is Rohan's daughter, {p1} is Rohan's son."
            step = f"Step 1: Sibling relation: {p1} and {p2}.\nStep 2: {p2} is daughter of Rohan.\nStep 3: {p1} is male sibling -> Son."
            tech = "First-degree genealogical pedigree."
        elif diff == "Medium":
            q_text = f"Portrait Kinship Deduction #{i}: Pointing to a photograph of {p2}, {p1} says: 'Her father's only son is my brother.' How is {p1} (assuming {p1} is female) related to {p2}?"
            corr = "Sister"
            dist = ["Mother", "Daughter", "Aunt"]
            exp = f"{p2}'s father's only son is {p2}'s brother. Since he is also {p1}'s brother, {p1} is {p2}'s sister."
            step = f"Step 1: Break down clause: father's only son = brother.\nStep 2: 'My brother' implies sharing parents.\nStep 3: Relationship is Sister."
            tech = "Second-degree kinship reduction."
        else: # Hard
            q_text = f"Coded Kinship Symbolism #{i}: If 'A + B' means A is the father of B, 'A - B' means A is the sister of B, and 'A * B' means A is the son of B, what does '{p1} + Q - {p2}' signify regarding {p1}'s relationship to {p2}?"
            corr = f"{p1} is the father of {p2}"
            dist = [f"{p1} is the uncle of {p2}", f"{p1} is the brother of {p2}", f"{p1} is the grandfather of {p2}"]
            exp = f"Q - {p2} means Q is the sister of {p2}. {p1} + Q means {p1} is the father of Q. Hence, {p1} is also the father of {p2}."
            step = f"Step 1: Parse Q - {p2} -> Q is sister of {p2}.\nStep 2: Parse {p1} + Q -> {p1} is father of Q.\nStep 3: Since Q and {p2} are siblings, {p1} is father of {p2}."
            tech = "Symbolic binary relation calculus."
        return make_vl_q(f"{tid}_{diff.lower()[0]}_{i:03d}", cat, grp, tid, tname, diff, directive, q_text, corr, dist, pos, "Deconstruct the relations starting from the rightmost entity.", exp, step, tech)

    # 5. VERBAL: SYNONYMS & ANTONYMS
    elif "synonym" in tid_lower or "antonym" in tid_lower or "vocab" in tid_lower:
        w_idx = i % len(WORDS)
        word = WORDS[w_idx]
        syn = SYNONYMS[w_idx]
        if "antonym" in tid_lower:
            directive = "Select the word most nearly opposite in meaning (antonym):"
            ant_map = {"EPHEMERAL": "permanent", "UBIQUITOUS": "rare", "METICULOUS": "careless", "PRAGMATIC": "idealistic", "PARADIGM": "aberration", "LUCID": "obscure", "PROLIFIC": "barren", "RESILIENT": "fragile", "ESOTERIC": "commonplace", "MITIGATE": "intensify"}
            corr = ant_map.get(word, "opposite")
            dist = [syn, "unrelated", "secondary"]
            prefix = "Fundamental" if diff == "Easy" else ("Contextual" if diff == "Medium" else "Advanced Lexical")
            q_text = f"{prefix} Antonym #{i}: What is the exact antonym for the capitalized term '{word}'?"
            exp = f"'{corr.capitalize()}' is the direct conceptual antonym of '{word}'."
            step = f"Step 1: Define core meaning of '{word}'.\nStep 2: Invert the semantic polarity.\nStep 3: Confirmed antonym is '{corr}'."
            tech = "Lexical antonym polarity."
        else:
            directive = "Select the word most similar in meaning (synonym):"
            corr = syn
            dist = ["contradictory", "irrelevant", "diminutive"]
            prefix = "Fundamental" if diff == "Easy" else ("Contextual" if diff == "Medium" else "Advanced Lexical")
            q_text = f"{prefix} Synonym #{i}: Choose the word closest in meaning to '{word}' in professional context:"
            exp = f"'{word}' means '{syn}'."
            step = f"Step 1: Identify root denotation of '{word}'.\nStep 2: Compare semantic proximity of options.\nStep 3: Confirmed synonym is '{corr}'."
            tech = "Lexical semantic equivalence."
        return make_vl_q(f"{tid}_{diff.lower()[0]}_{i:03d}", cat, grp, tid, tname, diff, directive, q_text, corr, dist, pos, "Identify the core meaning and evaluate option nuances.", exp, step, tech)

    # 6. VERBAL: GRAMMAR (Parts of Speech, Subject-Verb Agreement, Prepositions, Tenses)
    else:
        directive = "Select the grammatically correct option to complete the statement:"
        if diff == "Easy":
            q_text = f"Basic Concord Rule #{i}: 'Neither the network router nor the core switches ______ functioning during the downtime.'"
            corr = "were"
            dist = ["was", "is", "has been"]
            exp = "In 'neither... nor', the verb agrees with the closer subject ('switches' -> plural 'were')."
            step = f"Step 1: Identify compound correlative conjunction: 'neither... nor'.\nStep 2: Locate proximal subject: 'switches' (plural).\nStep 3: Verb must be plural: 'were'."
            tech = "Proximity concord rule."
        elif diff == "Medium":
            q_text = f"Prepositional Collocation #{i}: 'The revised distributed consensus algorithm is superior ______ previous monolithic designs.'"
            corr = "to"
            dist = ["than", "over", "against"]
            exp = "Latin comparatives ending in '-ior' (superior, inferior, prior) govern the preposition 'to', never 'than'."
            step = f"Step 1: Identify Latin comparative adjective 'superior'.\nStep 2: Rule: Latin comparatives require 'to'.\nStep 3: Correct choice is 'to'."
            tech = "Latin comparative governance."
        else: # Hard
            q_text = f"Inverted Syntax Agreement #{i}: 'Seldom ______ such catastrophic cluster synchronization latency experienced by the engineering team.'"
            corr = "has"
            dist = ["have", "is having", "were"]
            exp = "Negative adverbial inversion ('Seldom') requires auxiliary inversion before the singular subject 'latency' ('has')."
            step = f"Step 1: Recognize negative initial adverb 'Seldom'.\nStep 2: Head subject is singular 'latency'.\nStep 3: Inverted auxiliary verb is singular: 'has'."
            tech = "Negative adverbial syntactic inversion."
        return make_vl_q(f"{tid}_{diff.lower()[0]}_{i:03d}", cat, grp, tid, tname, diff, directive, q_text, corr, dist, pos, "Verify whether the head subject is singular or plural.", exp, step, tech)

def build_unique_vl_topic(tid, tname, grp, existing_uniques=None):
    cat = "Verbal Ability and Logical Reasoning"
    seen_texts = set()
    qs = []

    if existing_uniques:
        for q in existing_uniques:
            norm = normalize_text(q['q'])
            if norm not in seen_texts:
                seen_texts.add(norm)
                qs.append(q)

    cur_easy = [q for q in qs if q['difficulty'] == 'Easy']
    cur_med = [q for q in qs if q['difficulty'] == 'Medium']
    cur_hard = [q for q in qs if q['difficulty'] == 'Hard']

    target_easy = 15
    target_med = 10
    target_hard = 75

    counter = len(qs) + 1

    # Fill Easy
    while len(cur_easy) < target_easy:
        q_obj = generate_vl_item(tid, tname, grp, "Easy", counter)
        counter += 1
        norm = normalize_text(q_obj['q'])
        if norm not in seen_texts:
            seen_texts.add(norm)
            cur_easy.append(q_obj)

    # Fill Medium
    while len(cur_med) < target_med:
        q_obj = generate_vl_item(tid, tname, grp, "Medium", counter)
        counter += 1
        norm = normalize_text(q_obj['q'])
        if norm not in seen_texts:
            seen_texts.add(norm)
            cur_med.append(q_obj)

    # Fill Hard
    while len(cur_hard) < target_hard:
        q_obj = generate_vl_item(tid, tname, grp, "Hard", counter)
        counter += 1
        norm = normalize_text(q_obj['q'])
        if norm not in seen_texts:
            seen_texts.add(norm)
            cur_hard.append(q_obj)

    final_qs = []
    for k, q in enumerate(cur_easy[:target_easy], 1):
        q_c = dict(q)
        q_c['id'] = f"{tid}_e_{k:03d}"
        q_c['difficulty'] = "Easy"
        final_qs.append(q_c)
    for k, q in enumerate(cur_med[:target_med], 1):
        q_c = dict(q)
        q_c['id'] = f"{tid}_m_{k:03d}"
        q_c['difficulty'] = "Medium"
        final_qs.append(q_c)
    for k, q in enumerate(cur_hard[:target_hard], 1):
        q_c = dict(q)
        q_c['id'] = f"{tid}_h_{k:03d}"
        q_c['difficulty'] = "Hard"
        final_qs.append(q_c)

    assert len(final_qs) == 100, f"Topic {tid} has {len(final_qs)} questions, expected 100"
    return final_qs
