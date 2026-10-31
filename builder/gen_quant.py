# builder/gen_quant.py
import math
from q_helper import make_question

def generate_topic_quant(topic_id, topic_name, group_name):
    qs = []
    cat = "Quantitative Aptitude"
    
    # Exactly 15 Easy, 10 Medium, 75 Hard
    for i in range(15):
        qid = f"{topic_id}_e_{i+1:03d}"
        q, opts, ans, h, exp, step, tech, form = get_easy_quant_item(topic_id, topic_name, group_name, i + 1)
        qs.append(make_question(qid, cat, group_name, topic_id, topic_name, "Easy", q, opts, ans, h, exp, step, tech, form))
        
    for i in range(10):
        qid = f"{topic_id}_m_{i+1:03d}"
        q, opts, ans, h, exp, step, tech, form = get_med_quant_item(topic_id, topic_name, group_name, i + 1)
        qs.append(make_question(qid, cat, group_name, topic_id, topic_name, "Medium", q, opts, ans, h, exp, step, tech, form))

    for i in range(75):
        qid = f"{topic_id}_h_{i+1:03d}"
        q, opts, ans, h, exp, step, tech, form = get_hard_quant_item(topic_id, topic_name, group_name, i + 1)
        qs.append(make_question(qid, cat, group_name, topic_id, topic_name, "Hard", q, opts, ans, h, exp, step, tech, form))

    assert len(qs) == 100, f"Topic {topic_id} count mismatch"
    return qs

def get_easy_quant_item(topic_id, topic_name, group_name, idx):
    n = idx + 2
    if "pct" in topic_id or "percent" in topic_id:
        val = n * 50
        pct = 10 + (idx % 4) * 5
        res = (val * pct) // 100
        q = f"What is {pct}% of {val}?"
        opts = [str(res), str(res + 5), str(res - 5), str(res + 10)]
        exp = f"To find {pct}% of {val}: ({pct} / 100) * {val} = {res}."
        step = f"Step 1: Convert percentage to fraction: {pct}/100.\nStep 2: Multiply by base value: ({pct}/100) * {val}.\nStep 3: Compute final value = {res}."
        tech = "Basic percentage conversion."
        form = "\\text{Value} = \\frac{P}{100} \\times \\text{Total}"
        return f"[{topic_name} Basic #{idx}] {q}", opts, 0, f"Divide {val} by 100 and multiply by {pct}.", exp, step, tech, form
        
    if "hcf" in topic_id:
        a = n * 6
        b = n * 8
        gcd_val = math.gcd(a, b)
        q = f"Find the Highest Common Factor (HCF) of {a} and {b}."
        opts = [str(gcd_val), str(gcd_val * 2), str(max(1, gcd_val // 2)), str(gcd_val + 4)]
        exp = f"Prime factorizing {a} and {b} gives the greatest common divisor as {gcd_val}."
        step = f"Step 1: Factoring {a} and {b}.\nStep 2: Identify common prime factors.\nStep 3: Product of lowest powers gives HCF = {gcd_val}."
        tech = "Euclidean division algorithm."
        form = "\\gcd(a, b) = \\gcd(b, a \\pmod b)"
        return f"[{topic_name} Basic #{idx}] {q}", opts, 0, "Use prime factorization or division method.", exp, step, tech, form

    # Default Quant Easy Item
    base_val = n * 12
    ans_val = base_val // 3
    q = f"A quantity increases by 20% to reach {int(base_val * 1.2)}. What was the original value?"
    opts = [str(base_val), str(base_val + 6), str(base_val - 6), str(base_val + 12)]
    exp = f"Original value = {int(base_val * 1.2)} / 1.20 = {base_val}."
    step = f"Step 1: New value = Original * (1 + 0.20) = 1.2 * Original.\nStep 2: Original = {int(base_val * 1.2)} / 1.2.\nStep 3: Original = {base_val}."
    tech = "Base percentage scaling."
    form = "X_0 = \\frac{X_{\\text{new}}}{1 + r}"
    return f"[{topic_name} Basic #{idx}] {q}", opts, 0, "Divide the increased total by 1.20.", exp, step, tech, form

def get_med_quant_item(topic_id, topic_name, group_name, idx):
    p = idx * 1000 + 4000
    r = 5 + (idx % 5)
    t = 2
    si = (p * r * t) // 100
    
    q = f"In '{topic_name}', a principal of Rs. {p} is invested at an annual interest rate of {r}% simple interest for {t} years. What is the total interest earned?"
    opts = [f"Rs. {si}", f"Rs. {si + 150}", f"Rs. {si - 100}", f"Rs. {si + 250}"]
    exp = f"SI = (P * R * T) / 100 = ({p} * {r} * {t}) / 100 = Rs. {si}."
    step = f"Step 1: Identify P = {p}, R = {r}%, T = {t} years.\nStep 2: Substitute into SI formula: ({p} * {r} * {t}) / 100.\nStep 3: Calculate = {si}."
    tech = "Direct formula substitution."
    form = "\\text{SI} = \\frac{P \\times R \\times T}{100}"
    return f"[{topic_name} Problem #{idx}] {q}", opts, 0, "Use formula SI = (P * R * T) / 100.", exp, step, tech, form

def get_hard_quant_item(topic_id, topic_name, group_name, idx):
    # 75 Hard items with real mathematical depth, traps and shortcuts
    n = idx + 5
    mod = idx % 5
    
    if mod == 0:
        # Time and Work / Efficiency problem
        days_a = n * 2
        days_b = n * 3
        # 1/days_a + 1/days_b = (3 + 2)/(6n) = 5/(6n) => T = 6n / 5
        ans_num = 6 * n
        ans_den = 5
        ans_dec = round(ans_num / ans_den, 2)
        q = (f"Worker A can complete a project in {days_a} days, while Worker B alone requires {days_b} days. "
             f"If they collaborate together for the first 2 days and then Worker A leaves, how many days will Worker B take alone to finish the remaining work?")
        # Work done in 2 days = 2 * (1/days_a + 1/days_b) = 2 * (5/(6n)) = 5/(3n)
        # Rem work = 1 - 5/(3n) = (3n - 5)/(3n)
        # Days for B alone = Rem work * days_b = ((3n - 5)/(3n)) * 3n = 3n - 5 days!
        ans_days = 3 * n - 5
        opts = [f"{ans_days} days", f"{ans_days + 3} days", f"{max(1, ans_days - 2)} days", f"{ans_days + 5} days"]
        hint = "Calculate the fraction of work completed in the initial 2 days, then divide remaining work by B's daily rate."
        exp = f"A's daily rate is 1/{days_a} and B's is 1/{days_b}. Together their combined rate is 1/{days_a} + 1/{days_b} = 5/({6*n}). In 2 days they finish 2 * 5/({6*n}) = 5/({3*n}) of the total work. The remaining work is 1 - 5/({3*n}) = ({3*n}-5)/({3*n}). B alone finishes this in (Remaining Work) * {days_b} = {ans_days} days."
        step = f"Step 1: Daily rate of A = 1/{days_a}; Daily rate of B = 1/{days_b}.\nStep 2: Combined 2-day work = 2 * (1/{days_a} + 1/{days_b}) = 5/{3*n}.\nStep 3: Remaining work = 1 - 5/{3*n} = ({3*n}-5)/{3*n}.\nStep 4: Time for B = Remaining Work / (1/{days_b}) = {ans_days} days."
        tech = "Unitary work rate method."
        form = "T_{\\text{rem}} = \\frac{1 - W_{\\text{done}}}{\\text{Rate}_B}"
        return f"[{topic_name} Advanced #{idx}] {q}", opts, 0, hint, exp, step, tech, form
        
    elif mod == 1:
        # Profit and Loss with Marked Price & Consecutive Discounts
        cp = n * 40
        markup_pct = 50
        mp = int(cp * 1.5)
        d1 = 20
        d2 = 10
        # sp = mp * 0.8 * 0.9 = mp * 0.72 = (1.5 * cp) * 0.72 = 1.08 * cp
        # profit = 8%
        sp = int(mp * 0.8 * 0.9)
        profit_amt = sp - cp
        profit_pct = round((profit_amt / cp) * 100, 1)
        q = (f"A merchant marks up goods by {markup_pct}% above the cost price of Rs. {cp}. "
             f"He then offers two successive discounts of {d1}% and {d2}% on the marked price. What is the merchant's net profit percentage?")
        opts = [f"{profit_pct}%", f"{profit_pct + 4}%", f"{profit_pct - 3}%", f"{profit_pct + 8}%"]
        hint = "Remember that successive discounts of 20% and 10% equal a net discount of 28%, NOT 30%."
        exp = f"Cost Price (CP) = Rs. {cp}. Marked Price (MP) = {cp} * 1.50 = Rs. {mp}. Equivalent discount = 20 + 10 - (20*10)/100 = 28%. Selling Price (SP) = MP * (1 - 0.28) = {mp} * 0.72 = Rs. {sp}. Net Profit = {sp} - {cp} = Rs. {profit_amt}. Profit % = ({profit_amt} / {cp}) * 100 = {profit_pct}%."
        step = f"Step 1: MP = CP * (1 + 0.50) = Rs. {mp}.\nStep 2: Net Discount = d1 + d2 - (d1 * d2)/100 = 20 + 10 - 2 = 28%.\nStep 3: SP = MP * (1 - 0.28) = Rs. {sp}.\nStep 4: Profit % = (SP - CP)/CP * 100 = {profit_pct}%."
        tech = "Successive discount equivalence shortcut."
        form = "D_{\\text{eq}} = d_1 + d_2 - \\frac{d_1 d_2}{100}"
        return f"[{topic_name} Advanced #{idx}] {q}", opts, 0, hint, exp, step, tech, form

    elif mod == 2:
        # Time, Speed and Distance (Trains / Relative Speed)
        speed1 = 60
        speed2 = 40
        len1 = n * 10
        len2 = n * 15
        total_len = len1 + len2
        rel_speed_kmh = speed1 + speed2 # opposite direction
        rel_speed_ms = rel_speed_kmh * (5 / 18)
        time_sec = round(total_len / rel_speed_ms, 2)
        q = (f"Two trains of lengths {len1} m and {len2} m are traveling in opposite directions on parallel tracks at speeds of {speed1} km/h and {speed2} km/h respectively. "
             f"How many seconds will they take to completely pass each other?")
        opts = [f"{time_sec} s", f"{round(time_sec + 2.5, 2)} s", f"{round(time_sec - 1.8, 2)} s", f"{round(time_sec + 5.0, 2)} s"]
        hint = "When traveling in opposite directions, relative speed is the sum of both speeds. Convert km/h to m/s by multiplying by 5/18."
        exp = f"Total distance to clear = length_1 + length_2 = {len1} + {len2} = {total_len} m. Since they travel in opposite directions, relative speed = {speed1} + {speed2} = {rel_speed_kmh} km/h = {rel_speed_kmh} * (5/18) = {rel_speed_ms:.3f} m/s. Time = Distance / Speed = {total_len} / {rel_speed_ms:.3f} = {time_sec} seconds."
        step = f"Step 1: Total crossing distance = {len1} + {len2} = {total_len} m.\nStep 2: Relative speed = {speed1} + {speed2} = {rel_speed_kmh} km/h.\nStep 3: Convert to m/s: {rel_speed_kmh} * (5/18) = {rel_speed_ms:.2f} m/s.\nStep 4: Time = {total_len} / {rel_speed_ms:.2f} = {time_sec} s."
        tech = "Relative speed opposite direction formulation."
        form = "T = \\frac{L_1 + L_2}{(S_1 + S_2) \\times \\frac{5}{18}}"
        return f"[{topic_name} Advanced #{idx}] {q}", opts, 0, hint, exp, step, tech, form

    elif mod == 3:
        # Alligation and Mixture
        c_price = 15 + (idx % 5) * 2
        d_price = c_price + 15
        # mean price in between
        m_price = c_price + 6
        # ratio = (d - m) / (m - c) = (d_price - m_price) / (m_price - c_price)
        ratio_c = d_price - m_price
        ratio_d = m_price - c_price
        gcd_val = math.gcd(ratio_c, ratio_d)
        rc = ratio_c // gcd_val
        rd = ratio_d // gcd_val
        q = (f"In what ratio must tea worth Rs. {c_price} per kg be mixed with tea worth Rs. {d_price} per kg "
             f"so that the resulting mixture is worth Rs. {m_price} per kg?")
        opts = [f"{rc} : {rd}", f"{rd} : {rc}", f"{rc + 1} : {rd}", f"{rc} : {rd + 1}"]
        hint = "Apply rule of alligation: Cheaper quantity / Dearer quantity = (Dearer price - Mean price) / (Mean price - Cheaper price)."
        exp = f"By Rule of Alligation:\n(Quantity of Cheaper) / (Quantity of Dearer) = ({d_price} - {m_price}) / ({m_price} - {c_price}) = {ratio_c} / {ratio_d} = {rc} : {rd}."
        step = f"Step 1: Identify Cheaper price C = {c_price}, Dearer price D = {d_price}, Mean price M = {m_price}.\nStep 2: D - M = {d_price} - {m_price} = {ratio_c}.\nStep 3: M - C = {m_price} - {c_price} = {ratio_d}.\nStep 4: Required ratio = {ratio_c} : {ratio_d} = {rc} : {rd}."
        tech = "Rule of Alligation."
        form = "\\frac{Q_{\\text{cheaper}}}{Q_{\\text{dearer}}} = \\frac{D - M}{M - C}"
        return f"[{topic_name} Advanced #{idx}] {q}", opts, 0, hint, exp, step, tech, form

    else:
        # Combinatorics / Probability
        total_items = n + 4
        k_pick = 2
        # Combinations total_items C 2 = total_items * (total_items - 1) / 2
        comb = total_items * (total_items - 1) // 2
        q = (f"From a group of {total_items} candidates representing different departments, in how many distinct ways can a committee of 2 delegates be selected without regard to rank or ordering?")
        opts = [str(comb), str(comb + 10), str(comb - 5), str(comb * 2)]
        hint = "Use combination formula nCr = n! / (r! * (n - r)!)."
        exp = f"Since order of selection does not matter, the number of ways is {total_items}C2 = ({total_items} * {total_items - 1}) / (2 * 1) = {comb}."
        step = f"Step 1: Formula nCr = n! / [r! (n-r)!].\nStep 2: Here n = {total_items}, r = 2.\nStep 3: {total_items}C2 = ({total_items} * {total_items - 1}) / 2 = {comb}."
        tech = "Subset combination principle."
        form = "\\binom{n}{2} = \\frac{n(n - 1)}{2}"
        return f"[{topic_name} Advanced #{idx}] {q}", opts, 0, hint, exp, step, tech, form
