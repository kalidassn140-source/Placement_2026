# builder/generate_unique_quant.py
import math
from q_helper import make_question
from audit_duplicates import normalize_text, template_fingerprint

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

def make_quant_q(qid, cat, grp, tid, tname, diff, directive, question_body, corr_opt, raw_distractors, pos_idx, hint, exp, step, tech, formula=""):
    full_q = f"{directive}\n{question_body}" if directive else question_body
    opts, ans_idx = make_4_options(corr_opt, raw_distractors, pos_idx)
    return make_question(qid, cat, grp, tid, tname, diff, full_q, opts, ans_idx, hint, exp, step, tech, formula)

def generate_quant_item(tid, tname, grp, diff, i):
    cat = "Quantitative Aptitude"
    pos = i % 4
    tid_lower = tid.lower()

    # 1. TIME AND WORK / PIPES AND CISTERNS
    if "work" in tid_lower or "pipe" in tid_lower or "cist" in tid_lower:
        directive = "Calculate the work duration or efficiency metric:"
        if diff == "Easy":
            d1 = 10 + i * 2
            d2 = 15 + i * 3
            comb = round((d1 * d2) / (d1 + d2), 1)
            corr = f"{comb} days"
            dist = [f"{round(comb + 3.2, 1)} days", f"{max(1.0, round(comb - 2.5, 1))} days", f"{round(comb * 1.5, 1)} days"]
            q_text = f"Basic Work Scenario #{i}: Worker Alpha completes a system overhaul in {d1} days, and Worker Beta completes it in {d2} days. If both collaborate simultaneously, how many days will the overhaul require?"
            exp = f"Combined daily work rate = (1/{d1}) + (1/{d2}) = ({d1+d2})/({d1*d2}). Total days = {d1*d2}/{d1+d2} = {comb} days."
            step = f"Step 1: Compute individual daily rates: 1/{d1} and 1/{d2}.\nStep 2: Add rates: ({d1+d2})/{d1*d2}.\nStep 3: Reciprocal gives total duration = {comb} days."
            tech = "Harmonic rate superposition."
            form = "T = \\frac{d_1 \\cdot d_2}{d_1 + d_2}"
        elif diff == "Medium":
            m = 4 + (i % 6)
            days = 12 + i * 2
            m2 = m + 2
            req_days = round((m * days) / m2, 1)
            corr = f"{req_days} days"
            dist = [f"{round(req_days + 4.5, 1)} days", f"{max(1.0, round(req_days - 3.2, 1))} days", f"{round(req_days * 1.3, 1)} days"]
            q_text = f"Team Scalability Task #{i}: A deployment team of {m} certified engineers finishes an infrastructure migration in {days} days. Assuming uniform individual efficiency, how many days will {m2} engineers take to complete the identical migration?"
            exp = f"Total work units = {m} * {days} = {m*days} man-days. Time with {m2} engineers = ({m*days}) / {m2} = {req_days} days."
            step = f"Step 1: Calculate total work invariant W = {m} * {days} = {m*days} engineer-days.\nStep 2: Divide total work by new workforce size ({m2}).\nStep 3: Duration = {req_days} days."
            tech = "Inverse proportional manpower conservation."
            form = "M_1 D_1 = M_2 D_2"
        else: # Hard
            d1 = 15 + i
            d2 = 20 + i * 2
            leave_day = 3 + (i % 4)
            # Work done in leave_day: leave_day * (1/d1 + 1/d2)
            done = leave_day * (d1 + d2) / (d1 * d2)
            rem = max(0.01, 1.0 - done)
            q_days = round(rem * d2, 1)
            corr = f"{q_days} days"
            dist = [f"{round(q_days + 5.1, 1)} days", f"{max(1.0, round(q_days - 4.2, 1))} days", f"{round(q_days * 1.4, 1)} days"]
            q_text = f"Alternating Departure Workflow #{i}: Engineers P and Q can complete a software deliverable in {d1} and {d2} days respectively. They begin work together, but P departs after {leave_day} days. How many additional days must Q work alone to complete the deliverable?"
            exp = f"Fraction completed in first {leave_day} days = {leave_day} * (1/{d1} + 1/{d2}) = {round(done, 3)}. Remaining fraction = {round(rem, 3)}. Q requires {round(rem, 3)} * {d2} = {q_days} days."
            step = f"Step 1: Combined rate in first {leave_day} days = {leave_day} * ({d1+d2})/({d1*d2}).\nStep 2: Compute remaining work fraction = 1 - completed.\nStep 3: Multiply remaining fraction by Q's solo duration ({d2}) to obtain {q_days} days."
            tech = "Piecewise linear multi-agent task execution."
            form = "D_{\\text{rem}} = \\left(1 - t_1\\left(\\frac{1}{d_1} + \\frac{1}{d_2}\\right)\\right) \\times d_2"
        return make_quant_q(f"{tid}_{diff.lower()[0]}_{i:03d}", cat, grp, tid, tname, diff, directive, q_text, corr, dist, pos, "Sum the individual fractional rates per unit time.", exp, step, tech, form)

    # 2. SPEED, TIME, DISTANCE / TRAINS / BOATS & STREAMS
    elif "speed" in tid_lower or "dist" in tid_lower or "train" in tid_lower or "boat" in tid_lower or "race" in tid_lower:
        directive = "Compute the kinematics transit parameter:"
        if diff == "Easy":
            speed_kmh = 36 + (i * 18) % 72
            time_h = 2 + (i % 4)
            dist_val = speed_kmh * time_h
            corr = f"{dist_val} km"
            dist = [f"{dist_val + 30} km", f"{max(10, dist_val - 25)} km", f"{dist_val * 2} km"]
            q_text = f"Uniform Speed Calculation #{i}: An automated telemetry transport vehicle travels at a steady speed of {speed_kmh} km/h for {time_h} hours. What total distance does it cover?"
            exp = f"Distance = Speed * Time = {speed_kmh} km/h * {time_h} h = {dist_val} km."
            step = f"Step 1: Formula D = s * t.\nStep 2: Multiply {speed_kmh} by {time_h}.\nStep 3: Distance = {dist_val} km."
            tech = "Uniform rectilinear kinematics."
            form = "d = v \\cdot t"
        elif diff == "Medium":
            speed_kmh = 54 + (i * 18) % 72
            speed_ms = speed_kmh * 5 // 18
            train_len = 150 + i * 10
            plat_len = 250 + i * 15
            total_d = train_len + plat_len
            t_sec = round(total_d / speed_ms, 1)
            corr = f"{t_sec} s"
            dist = [f"{round(t_sec + 5.5, 1)} s", f"{max(2.0, round(t_sec - 4.2, 1))} s", f"{round(t_sec * 1.4, 1)} s"]
            q_text = f"Platform Crossing Transit #{i}: A high-speed express train of length {train_len} m travels at {speed_kmh} km/h. How many seconds does it take to cross a stationary platform of length {plat_len} m?"
            exp = f"Speed = {speed_kmh} * 5/18 = {speed_ms} m/s. Total distance = {train_len} + {plat_len} = {total_d} m. Time = {total_d} / {speed_ms} = {t_sec} s."
            step = f"Step 1: Convert speed to m/s: {speed_kmh} * (5/18) = {speed_ms} m/s.\nStep 2: Total transit distance = {train_len} + {plat_len} = {total_d} m.\nStep 3: Time = Distance / Speed = {t_sec} s."
            tech = "Reference frame relative displacement."
            form = "t = \\frac{L_1 + L_2}{v}"
        else: # Hard
            b_speed = 15 + (i % 8)
            s_speed = 3 + (i % 4)
            d_dist = 40 + i * 3
            down_t = round(d_dist / (b_speed + s_speed), 2)
            up_t = round(d_dist / (b_speed - s_speed), 2)
            tot_t = round(down_t + up_t, 2)
            corr = f"{tot_t} hours"
            dist = [f"{round(tot_t + 2.4, 2)} hours", f"{max(1.0, round(tot_t - 1.8, 2))} hours", f"{round(tot_t * 1.3, 2)} hours"]
            q_text = f"Fluid Drift Round-Trip #{i}: A motorboat operates at {b_speed} km/h in still water. A river current flows at {s_speed} km/h. What is the total round-trip time required to travel {d_dist} km downstream and return upstream to the origin?"
            exp = f"Downstream speed = {b_speed}+{s_speed} = {b_speed+s_speed} km/h (time = {down_t} h). Upstream speed = {b_speed}-{s_speed} = {b_speed-s_speed} km/h (time = {up_t} h). Total time = {tot_t} hours."
            step = f"Step 1: Effective downstream velocity = v_b + v_s = {b_speed + s_speed} km/h.\nStep 2: Effective upstream velocity = v_b - v_s = {b_speed - s_speed} km/h.\nStep 3: Total duration = {d_dist}/{b_speed+s_speed} + {d_dist}/{b_speed-s_speed} = {tot_t} hours."
            tech = "Non-inertial fluid relative velocity superposition."
            form = "T = \\frac{D}{v_b + v_s} + \\frac{D}{v_b - v_s}"
        return make_quant_q(f"{tid}_{diff.lower()[0]}_{i:03d}", cat, grp, tid, tname, diff, directive, q_text, corr, dist, pos, "Account for relative velocity in opposing directions.", exp, step, tech, form)

    # 3. PERCENTAGE / PROFIT & LOSS / INTEREST / DISCOUNT
    elif "profit" in tid_lower or "loss" in tid_lower or "pct" in tid_lower or "percent" in tid_lower or "interest" in tid_lower or "discount" in tid_lower:
        directive = "Solve the commercial valuation calculation:"
        if diff == "Easy":
            base = 200 + i * 25
            pct = 10 + (i % 5) * 5
            val = (base * pct) // 100
            corr = f"${val}"
            dist = [f"${val + 15}", f"${max(5, val - 12)}", f"${val * 2}"]
            q_text = f"Direct Percentage Valuation #{i}: What is {pct}% of an enterprise hardware maintenance budget of ${base}?"
            exp = f"Calculation: ({pct} / 100) * ${base} = ${val}."
            step = f"Step 1: Express percentage as fraction: {pct}/100.\nStep 2: Multiply by total amount ${base}.\nStep 3: Output = ${val}."
            tech = "Proportional fraction arithmetic."
            form = "V = \\frac{P}{100} \\times B"
        elif diff == "Medium":
            cp = 150 + i * 20
            profit_pct = 12 + (i % 4) * 4
            profit = (cp * profit_pct) // 100
            sp = cp + profit
            corr = f"${sp}"
            dist = [f"${sp + 28}", f"${max(20, sp - 32)}", f"${sp + 65}"]
            q_text = f"Markup Selling Price #{i}: A network switch purchased at a cost price of ${cp} is sold to achieve a net profit margin of {profit_pct}%. What is its final selling price?"
            exp = f"Selling Price = Cost Price * (1 + Profit% / 100) = ${cp} * (1 + {profit_pct}/100) = ${sp}."
            step = f"Step 1: Compute profit value: ({profit_pct}/100) * ${cp} = ${profit}.\nStep 2: Add profit to cost price: ${cp} + ${profit} = ${sp}.\nStep 3: Selling Price = ${sp}."
            tech = "Commercial cost-plus pricing."
            form = "SP = CP \\times \\left(1 + \\frac{P}{100}\\right)"
        else: # Hard
            p = 1000 + i * 150
            r = 5 + (i % 5) * 2
            t = 2
            # Compound Interest: A = P(1 + r/100)^2, CI = A - P
            ci = round(p * ((1 + r/100)**t - 1), 2)
            si = round((p * r * t) / 100, 2)
            diff_ci_si = round(ci - si, 2)
            corr = f"${diff_ci_si}"
            dist = [f"${round(diff_ci_si + 8.5, 2)}", f"${max(1.0, round(diff_ci_si - 5.2, 2))}", f"${round(diff_ci_si * 1.5, 2)}"]
            q_text = f"Compounding Discrepancy #{i}: An institutional capital bond of ${p} is invested for 2 years at an annual interest rate of {r}%. What is the exact monetary difference between its Compound Interest (compounded annually) and Simple Interest?"
            exp = f"Difference between CI and SI for 2 years = P * (R/100)^2 = ${p} * ({r}/100)^2 = ${diff_ci_si}."
            step = f"Step 1: Simple Interest SI = (P * R * T) / 100 = ${si}.\nStep 2: Compound Interest CI = P * ((1 + R/100)^T - 1) = ${ci}.\nStep 3: Difference CI - SI = ${diff_ci_si}."
            tech = "Geometric compounding curvature discrepancy."
            form = "\\Delta = P \\times \\left(\\frac{R}{100}\\right)^2"
        return make_quant_q(f"{tid}_{diff.lower()[0]}_{i:03d}", cat, grp, tid, tname, diff, directive, q_text, corr, dist, pos, "Apply the 2-year difference formula P*(R/100)^2.", exp, step, tech, form)

    # 4. RATIO, PROPORTION, PARTNERSHIP, AVERAGE, ALLIGATION
    elif "ratio" in tid_lower or "prop" in tid_lower or "part" in tid_lower or "avg" in tid_lower or "average" in tid_lower or "allig" in tid_lower:
        directive = "Calculate the proportional or statistical metric:"
        if diff == "Easy":
            r1 = 2 + (i % 3)
            r2 = 3 + (i % 4)
            total = (r1 + r2) * (20 + i * 5)
            share_a = (total * r1) // (r1 + r2)
            corr = f"${share_a}"
            dist = [f"${share_a + 35}", f"${max(10, share_a - 28)}", f"${share_a * 2}"]
            q_text = f"Binary Ratio Allocation #{i}: A venture capital grant of ${total} is distributed between Startup Alpha and Startup Beta in the ratio {r1} : {r2}. How much capital is awarded to Startup Alpha?"
            exp = f"Alpha's share = ({r1} / ({r1} + {r2})) * ${total} = ${share_a}."
            step = f"Step 1: Sum ratio parts: {r1} + {r2} = {r1+r2}.\nStep 2: Multiply total grant by fraction {r1}/{r1+r2}.\nStep 3: Alpha's share = ${share_a}."
            tech = "Direct linear proportion partition."
            form = "S_A = T \\times \\frac{r_1}{r_1 + r_2}"
        elif diff == "Medium":
            count = 10 + (i % 6)
            old_avg = 50 + (i * 2) % 30
            new_val = old_avg + count * 2
            new_avg = old_avg + 2
            corr = f"{new_avg}"
            dist = [f"{new_avg + 4}", f"{max(10, new_avg - 3)}", f"{new_avg + 8}"]
            q_text = f"Mean Dynamic Adjustment #{i}: The average score of {count} engineering recruits in an assessment is {old_avg}. When an elite candidate scoring {new_val} joins the cohort, what is the revised average score?"
            exp = f"Total previous sum = {count} * {old_avg} = {count * old_avg}. New sum = {count * old_avg} + {new_val}. New count = {count + 1}. Revised average = {new_avg}."
            step = f"Step 1: Compute baseline sum: {count} * {old_avg} = {count * old_avg}.\nStep 2: Add incoming recruit's score: {count * old_avg} + {new_val} = {(count+1)*new_avg}.\nStep 3: Divide by {count + 1} to get revised mean: {new_avg}."
            tech = "Discrete dynamic expectation update."
            form = "\\bar{x}_{\\text{new}} = \\frac{N \\bar{x} + x_{\\text{new}}}{N + 1}"
        else: # Hard
            c1_pct = 15 + (i % 5) * 5
            c2_pct = 40 + (i % 4) * 5
            target_pct = c1_pct + 10
            r_ratio1 = c2_pct - target_pct
            r_ratio2 = target_pct - c1_pct
            gcd_val = math.gcd(r_ratio1, r_ratio2)
            s1 = r_ratio1 // gcd_val
            s2 = r_ratio2 // gcd_val
            corr = f"{s1} : {s2}"
            dist = [f"{s2} : {s1}", f"{s1 + 1} : {s2}", f"{s1} : {s2 + 2}"]
            q_text = f"Alligation Mixture Ratio #{i}: In what ratio must a chemical cleaning solution containing {c1_pct}% concentration be blended with a solution containing {c2_pct}% concentration to produce a resulting mixture with exactly {target_pct}% concentration?"
            exp = f"Rule of Alligation: (Quantity of Cheaper) / (Quantity of Dearer) = (Price of Dearer - Mean Price) / (Mean Price - Price of Cheaper) = ({c2_pct} - {target_pct}) / ({target_pct} - {c1_pct}) = {s1} : {s2}."
            step = f"Step 1: Compute high difference: {c2_pct} - {target_pct} = {r_ratio1}.\nStep 2: Compute low difference: {target_pct} - {c1_pct} = {r_ratio2}.\nStep 3: Simplify ratio: {s1} : {s2}."
            tech = "Weighted alligation cross-difference."
            form = "\\frac{q_1}{q_2} = \\frac{c_2 - c_m}{c_m - c_1}"
        return make_quant_q(f"{tid}_{diff.lower()[0]}_{i:03d}", cat, grp, tid, tname, diff, directive, q_text, corr, dist, pos, "Apply the weighted alligation cross-difference method.", exp, step, tech, form)

    # 5. PERMUTATION, COMBINATION, PROBABILITY
    elif "perm" in tid_lower or "comb" in tid_lower or "prob" in tid_lower:
        directive = "Determine the combinatorial or probabilistic count:"
        if diff == "Easy":
            n = 4 + (i % 4)
            fac = math.factorial(n)
            corr = f"{fac}"
            dist = [f"{fac + 12}", f"{max(2, fac - 8)}", f"{fac * 2}"]
            q_text = f"Linear Permutation #{i}: In how many distinct sequential ways can {n} unique server processes be queued for execution on a single core?"
            exp = f"Total distinct arrangements = {n}! = {fac}."
            step = f"Step 1: Identify that all {n} items are distinct.\nStep 2: Apply permutation factorial P = {n}!.\nStep 3: Evaluate {n}! = {fac}."
            tech = "Factorial permutation counting."
            form = "P = n!"
        elif diff == "Medium":
            n = 6 + (i % 5)
            r = 2 + (i % 2)
            c = math.comb(n, r)
            corr = f"{c}"
            dist = [f"{c + 6}", f"{max(1, c - 4)}", f"{c * 2}"]
            q_text = f"Committee Formation #{i}: From an engineering department of {n} staff members, in how many ways can a peer-review panel of {r} members be chosen?"
            exp = f"Combinations formula: C({n}, {r}) = {n}! / ({r}! * ({n}-{r})!) = {c}."
            step = f"Step 1: Unordered selection uses combination C(n, r).\nStep 2: Apply formula C({n}, {r}) = {n}! / ({r}! * {n-r}!).\nStep 3: Value = {c}."
            tech = "Combinatorial selection calculus."
            form = "C(n, r) = \\frac{n!}{r!(n - r)!}"
        else: # Hard
            red = 4 + (i % 4)
            blue = 5 + (i % 3)
            tot = red + blue
            # P(2 red) = C(red, 2) / C(tot, 2)
            num = math.comb(red, 2)
            den = math.comb(tot, 2)
            g = math.gcd(num, den)
            corr = f"{num//g}/{den//g}"
            dist = [f"{num//g + 1}/{den//g}", f"{max(1, num//g - 1)}/{den//g}", f"{num//g}/{den//g + 4}"]
            q_text = f"Hypergeometric Drawing Probability #{i}: An urn contains {red} red and {blue} blue data tokens. If 2 tokens are drawn randomly without replacement, what is the probability that both tokens drawn are red?"
            exp = f"Ways to draw 2 red = C({red}, 2) = {num}. Total ways to draw 2 = C({tot}, 2) = {den}. P = {num}/{den} = {num//g}/{den//g}."
            step = f"Step 1: Favorable outcomes = C({red}, 2) = {num}.\nStep 2: Sample space size = C({tot}, 2) = {den}.\nStep 3: Probability = {num}/{den} = {num//g}/{den//g}."
            tech = "Hypergeometric distribution sampling without replacement."
            form = "P(2R) = \\frac{\\binom{\\text{red}}{2}}{\\binom{\\text{total}}{2}}"
        return make_quant_q(f"{tid}_{diff.lower()[0]}_{i:03d}", cat, grp, tid, tname, diff, directive, q_text, corr, dist, pos, "Evaluate combinations for favorable outcomes over total sample space.", exp, step, tech, form)

    # 6. GEOMETRY, MENSURATION, HEIGHTS & DISTANCES
    elif "geom" in tid_lower or "area" in tid_lower or "vol" in tid_lower or "surf" in tid_lower or "mensur" in tid_lower or "height" in tid_lower:
        directive = "Calculate the geometric spatial dimension:"
        if diff == "Easy":
            s = 6 + i * 2
            perim = 4 * s
            corr = f"{perim} m"
            dist = [f"{perim + 8} m", f"{max(4, perim - 6)} m", f"{s * s} m"]
            q_text = f"Square Boundary Perimeter #{i}: A square server room enclosure has an edge length of {s} meters. What is its total perimeter boundary?"
            exp = f"Perimeter = 4 * side = 4 * {s} = {perim} m."
            step = f"Step 1: Formula for square perimeter P = 4s.\nStep 2: Multiply 4 by {s}.\nStep 3: Perimeter = {perim} m."
            tech = "Planar polygon perimeter."
            form = "P = 4s"
        elif diff == "Medium":
            r = 7 + (i * 7) % 49 # multiple of 7
            area = (22 * r * r) // 7
            corr = f"{area} sq m"
            dist = [f"{area + 44} sq m", f"{max(14, area - 38)} sq m", f"{area * 2} sq m"]
            q_text = f"Circular Coverage Footprint #{i}: A satellite receiver dishes out a circular coverage zone of radius {r} meters. Taking pi = 22/7, what is the exact surface area of the coverage zone?"
            exp = f"Area = pi * r^2 = (22/7) * {r}^2 = {area} sq m."
            step = f"Step 1: Formula A = pi * r^2.\nStep 2: Substitute r = {r} and pi = 22/7: (22 * {r*r}) / 7.\nStep 3: Area = {area} sq m."
            tech = "Circular Euclidean mensuration."
            form = "A = \\pi r^2"
        else: # Hard
            h = 10 + i * 3
            # Two observation angles: 30 deg and 45 deg on opposite sides of a tower
            # dist = h / tan(30) + h / tan(45) = h * sqrt(3) + h = h * (1.732 + 1) = h * 2.732
            d_val = round(h * 2.732, 1)
            corr = f"{d_val} m"
            dist = [f"{round(d_val + 14.5, 1)} m", f"{max(10.0, round(d_val - 12.2, 1))} m", f"{round(d_val * 1.4, 1)} m"]
            q_text = f"Trigonometric Bilateral Observation #{i}: Two monitoring vehicles are positioned on opposite sides of a transmission tower of height {h} meters. The observed angles of elevation to the top of the tower are 30 degrees and 45 degrees respectively. Taking sqrt(3) = 1.732, what is the total ground distance separating the two vehicles?"
            exp = f"Distance from vehicle 1 = {h} / tan(30 deg) = {h} * sqrt(3) = {round(h * 1.732, 1)} m. Distance from vehicle 2 = {h} / tan(45 deg) = {h} m. Total separation = {h}*(1.732 + 1) = {d_val} m."
            step = f"Step 1: Subdivide base into two right triangles.\nStep 2: Base 1 = h * cot(30 deg) = {h} * 1.732. Base 2 = h * cot(45 deg) = {h}.\nStep 3: Sum base segments: {h}*(2.732) = {d_val} m."
            tech = "Bilateral trigonometric elevation resolution."
            form = "D = h(\\cot 30^\\circ + \\cot 45^\\circ)"
        return make_quant_q(f"{tid}_{diff.lower()[0]}_{i:03d}", cat, grp, tid, tname, diff, directive, q_text, corr, dist, pos, "Sum the cotangent projections from both sides of the tower.", exp, step, tech, form)

    # 7. NUMBER SYSTEM, HCF/LCM, PROGRESSIONS, ALGEBRA
    else:
        directive = "Solve the numerical arithmetic or sequence property:"
        if diff == "Easy":
            a = 3 + (i % 5)
            d = 3 + (i % 4)
            n = 5 + (i % 6)
            term = a + (n - 1) * d
            corr = f"{term}"
            dist = [f"{term + d}", f"{max(1, term - d)}", f"{term + 2 * d}"]
            q_text = f"Arithmetic Progression Element #{i}: In an arithmetic sequence where the first term a = {a} and common difference d = {d}, what is the {n}th term?"
            exp = f"T_{n} = a + (n - 1) * d = {a} + ({n} - 1) * {d} = {term}."
            step = f"Step 1: Apply formula T_n = a + (n - 1)d.\nStep 2: Substitute a = {a}, d = {d}, n = {n}.\nStep 3: Result = {term}."
            tech = "Linear progression recurrence."
            form = "T_n = a + (n - 1)d"
        elif diff == "Medium":
            num1 = 24 + i * 6
            num2 = 36 + i * 9
            g = math.gcd(num1, num2)
            l = (num1 * num2) // g
            corr = f"{l}"
            dist = [f"{l + num1}", f"{max(num1, l - num2)}", f"{l * 2}"]
            q_text = f"Lowest Common Multiple #{i}: What is the Least Common Multiple (LCM) of the two operational periods {num1} minutes and {num2} minutes?"
            exp = f"LCM(a, b) = (a * b) / GCD(a, b). GCD({num1}, {num2}) = {g}. LCM = ({num1} * {num2}) / {g} = {l}."
            step = f"Step 1: Compute GCD({num1}, {num2}) = {g}.\nStep 2: Multiply {num1} by {num2} and divide by {g}.\nStep 3: LCM = {l}."
            tech = "Euclidean GCD/LCM relationship."
            form = "\\text{LCM}(a, b) = \\frac{a \\cdot b}{\\gcd(a, b)}"
        else: # Hard
            base = 7 + (i % 3) * 2  # 7 or 9
            exp_val = 100 + i * 5
            # Unit digit of base^exp
            # For 7: cycle is 7, 9, 3, 1 (length 4)
            # For 9: cycle is 9, 1 (length 2)
            u = pow(base, exp_val, 10)
            corr = f"{u}"
            dist = [f"{(u + 2) % 10}", f"{(u + 4) % 10}", f"{(u + 7) % 10}"]
            q_text = f"Modular Unit Digit Exponential #{i}: What is the final unit digit produced by evaluating the exponential expression {base}^{exp_val}?"
            exp = f"Powers of {base} exhibit a periodic cyclic pattern of unit digits. Modular reduction of exponent {exp_val} yields unit digit {u}."
            step = f"Step 1: Determine the cyclic period length for powers of {base}.\nStep 2: Compute exponent modulo cycle length: {exp_val} mod k.\nStep 3: The corresponding unit digit is {u}."
            tech = "Modular cyclic exponentiation."
            form = "U = b^e \\pmod{10}"
        return make_quant_q(f"{tid}_{diff.lower()[0]}_{i:03d}", cat, grp, tid, tname, diff, directive, q_text, corr, dist, pos, "Find the cyclicity of the base and take the exponent modulo the period.", exp, step, tech, form)

def build_unique_quant_topic(tid, tname, grp, existing_uniques=None):
    cat = "Quantitative Aptitude"
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
        q_obj = generate_quant_item(tid, tname, grp, "Easy", counter)
        counter += 1
        norm = normalize_text(q_obj['q'])
        if norm not in seen_texts:
            seen_texts.add(norm)
            cur_easy.append(q_obj)

    # Fill Medium
    while len(cur_med) < target_med:
        q_obj = generate_quant_item(tid, tname, grp, "Medium", counter)
        counter += 1
        norm = normalize_text(q_obj['q'])
        if norm not in seen_texts:
            seen_texts.add(norm)
            cur_med.append(q_obj)

    # Fill Hard
    while len(cur_hard) < target_hard:
        q_obj = generate_quant_item(tid, tname, grp, "Hard", counter)
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
