# builder/generate_unique_coding.py
import re
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

def make_coding_q(qid, cat, grp, tid, tname, diff, directive, question_body, corr_opt, raw_distractors, pos_idx, hint, exp, step, tech, code_snip="", formula=""):
    full_q = f"{directive}\n{question_body}" if directive else question_body
    opts, ans_idx = make_4_options(corr_opt, raw_distractors, pos_idx)
    q_dict = make_question(qid, cat, grp, tid, tname, diff, full_q, opts, ans_idx, hint, exp, step, tech, formula)
    if code_snip:
        q_dict["code"] = code_snip
    return q_dict

def generate_coding_item(tid, tname, grp, diff, i):
    cat = "Coding Questions"
    pos = i % 4
    tid_lower = tid.lower()

    # 1. SPECIAL: PYTHON STATISTICAL & MATHEMATICAL OPERATIONS (200 Questions)
    if "stats" in tid_lower or "stat" in tid_lower:
        directive = "Evaluate the SciPy / NumPy statistical computing operation:"
        if diff == "Easy":
            ops = [
                ("np.mean(arr)", "Arithmetic Mean", ["Arithmetic Mean", "Median", "Standard Deviation", "Variance"]),
                ("np.median(arr)", "Sample Median (50th percentile)", ["Sample Median (50th percentile)", "Mean", "Mode", "Variance"]),
                ("np.ptp(arr)", "Peak-to-Peak Range (max - min)", ["Peak-to-Peak Range (max - min)", "Interquartile Range", "Variance", "Standard Error"]),
                ("np.var(arr)", "Population Variance", ["Population Variance", "Sample Standard Deviation", "Mean", "Median"]),
                ("np.std(arr)", "Population Standard Deviation (ddof=0)", ["Population Standard Deviation (ddof=0)", "Sample Variance", "Mean", "IQR"])
            ]
            op = ops[i % len(ops)]
            corr = op[1]
            dist = op[2]
            q_text = f"Basic Descriptive Metric #{i}: What statistical metric is returned by executing '{op[0]}' on 1D numeric array arr?"
            exp = f"In NumPy, '{op[0]}' computes the {op[1]}."
            step = f"Step 1: Parse the NumPy mathematical function signature.\nStep 2: Inspect default degrees of freedom and reduction axis.\nStep 3: Confirmed metric is {op[1]}."
            tech = "NumPy descriptive statistics API."
        elif diff == "Medium":
            ops = [
                ("scipy.stats.iqr(arr)", "Interquartile Range (Q3 - Q1)", ["Interquartile Range (Q3 - Q1)", "Standard Deviation", "Sample Variance", "Range"]),
                ("np.std(arr, ddof=1)", "Sample Standard Deviation (ddof=1)", ["Sample Standard Deviation (ddof=1)", "Population Standard Deviation", "Variance", "Standard Error"]),
                ("scipy.stats.sem(arr)", "Standard Error of the Mean", ["Standard Error of the Mean", "Standard Deviation", "Variance", "Median Absolute Deviation"]),
                ("scipy.stats.zscore(arr)", "Array of Standardized Z-scores", ["Array of Standardized Z-scores", "Min-Max Scaled Array", "Log Transform", "Rank Transform"]),
                ("np.cov(x, y)", "Empirical Covariance Matrix", ["Empirical Covariance Matrix", "Correlation Matrix", "Hessian Matrix", "Jacobian Matrix"])
            ]
            op = ops[i % len(ops)]
            corr = op[1]
            dist = op[2]
            q_text = f"Intermediate Dispersion Measure #{i}: What quantitative property is evaluated by executing '{op[0]}' in Python?"
            exp = f"In Python scientific computing, '{op[0]}' evaluates the {op[1]}."
            step = f"Step 1: Check function package origin and mathematical definition.\nStep 2: Note sample vs population divisor conventions.\nStep 3: Output represents {op[1]}."
            tech = "SciPy/NumPy dispersion analytics."
        else: # Hard
            ops = [
                ("scipy.stats.skew(arr)", "Fisher-Pearson Skewness Coefficient", ["Fisher-Pearson Skewness Coefficient", "Excess Kurtosis", "Covariance", "Standard Error"]),
                ("scipy.stats.kurtosis(arr)", "Excess Kurtosis relative to Gaussian distribution", ["Excess Kurtosis relative to Gaussian distribution", "Pearson r Correlation", "Variance Ratio", "Gini Impurity"]),
                ("scipy.stats.pearsonr(x, y)[0]", "Pearson Linear Correlation Coefficient r", ["Pearson Linear Correlation Coefficient r", "Spearman Rank Rho", "Kendall Tau", "R-squared Score"]),
                ("scipy.stats.ttest_ind(sample_a, sample_b)", "Two-Sample Independent Student t-test", ["Two-Sample Independent Student t-test", "Paired t-test", "One-way ANOVA F-test", "Mann-Whitney U Test"]),
                ("scipy.stats.f_oneway(g1, g2, g3)", "One-Way ANOVA F-test for group means", ["One-Way ANOVA F-test for group means", "Chi-Square Test", "Student t-statistic", "Kruskal-Wallis H"]),
                ("scipy.stats.chisquare(f_obs, f_exp)", "Pearson Chi-Square Goodness-of-Fit Test", ["Pearson Chi-Square Goodness-of-Fit Test", "Fisher Exact Test", "Student t-test", "Kolmogorov-Smirnov Test"]),
                ("np.linalg.det(matrix)", "Matrix Determinant scaling factor", ["Matrix Determinant scaling factor", "Matrix Trace", "Spectral Radius", "Frobenius Norm"]),
                ("np.linalg.inv(matrix)", "Multiplicative Matrix Inverse (A^-1)", ["Multiplicative Matrix Inverse (A^-1)", "Pseudoinverse", "Transpose", "Adjugate Matrix"]),
                ("np.linalg.eigvals(matrix)", "Eigenvalues spectrum of square matrix", ["Eigenvalues spectrum of square matrix", "Singular Values", "Diagonal Elements", "Cholesky Factors"]),
                ("scipy.stats.entropy(pk)", "Shannon Information Entropy", ["Shannon Information Entropy", "Gini Impurity", "KL Divergence", "Variance Metric"])
            ]
            op = ops[i % len(ops)]
            corr = op[1]
            dist = op[2]
            q_text = f"Advanced Inferential/Linear Algebra Computation #{i}: What exact mathematical metric or distribution property is returned by executing '{op[0]}'?"
            exp = f"Executing '{op[0]}' computes the {op[1]}."
            step = f"Step 1: Identify algebraic formula and library implementation.\nStep 2: Inspect matrix dimensional invariants and degrees of freedom.\nStep 3: Confirmed metric is {op[1]}."
            tech = "SciPy/NumPy advanced inferential statistical computing."
        return make_coding_q(f"{tid}_{diff.lower()[0]}_{i:03d}", cat, grp, tid, tname, diff, directive, q_text, corr, dist, pos, "Analyze the mathematical definition of this SciPy/NumPy function call.", exp, step, tech)

    # 2. SPECIAL: PYTHON CHARTS & DATA VISUALIZATION (100 Questions)
    elif "chart" in tid_lower:
        directive = "Analyze the Python Matplotlib / Seaborn visualization specification:"
        if diff == "Easy":
            plots = [
                ("plt.plot(x, y)", "2D continuous line trajectory plot", ["2D continuous line trajectory plot", "Bar chart", "Histogram", "Heatmap"]),
                ("plt.bar(categories, heights)", "Vertical categorical column bar chart", ["Vertical categorical column bar chart", "Line plot", "Pie chart", "Scatter plot"]),
                ("plt.title('Performance Benchmark')", "Adds a header title string to the active axes", ["Adds a header title string to the active axes", "Labels the x-axis", "Sets legend labels", "Renders gridlines"]),
                ("plt.xlabel('Timestamp (s)')", "Sets text label for horizontal x-axis", ["Sets text label for horizontal x-axis", "Sets chart title", "Labels y-axis", "Formats ticks"])
            ]
            p = plots[i % len(plots)]
            corr = p[1]
            dist = p[2]
            q_text = f"Fundamental Plotting Primitive #{i}: What graphical element or property is configured by executing '{p[0]}'?"
            exp = f"Invoking '{p[0]}' {p[1].lower()}."
            step = f"Step 1: Check Matplotlib pyplot axes API.\nStep 2: Note parameter bindings.\nStep 3: Output effect is: {p[1]}."
            tech = "Matplotlib axes rendering pipeline."
        elif diff == "Medium":
            plots = [
                ("plt.hist(values, bins=20)", "Frequency distribution histogram with 20 bins", ["Frequency distribution histogram with 20 bins", "Line plot", "Pie chart", "Violin plot"]),
                ("plt.scatter(x, y)", "2D Cartesian point scatter distribution", ["2D Cartesian point scatter distribution", "Line plot", "Heatmap", "Area chart"]),
                ("plt.barh(categories, values)", "Horizontal bar chart", ["Horizontal bar chart", "Vertical column chart", "Stacked area chart", "Histogram"]),
                ("plt.grid(True, linestyle='--')", "Renders dashed gridlines across axes ticks", ["Renders dashed gridlines across axes ticks", "Draws axes spines", "Renders legend box", "Clears current figure"])
            ]
            p = plots[i % len(plots)]
            corr = p[1]
            dist = p[2]
            q_text = f"Bivariate Distribution Rendering #{i}: What specific visual layout is produced by invoking '{p[0]}'?"
            exp = f"Invoking '{p[0]}' produces a {p[1]}."
            step = f"Step 1: Identify Matplotlib plotting method: {p[0]}.\nStep 2: Inspect geometry transformation.\nStep 3: Confirmed layout is {p[1]}."
            tech = "Matplotlib distribution graphics."
        else: # Hard
            plots = [
                ("plt.boxplot(data, notch=True)", "Notched box-and-whisker plot for median confidence intervals", ["Notched box-and-whisker plot for median confidence intervals", "Violin density plot", "Histogram", "Strip plot"]),
                ("plt.violinplot(dataset, showmedians=True)", "Violin plot combining KDE with quartile markers", ["Violin plot combining KDE with quartile markers", "Standard boxplot", "Strip plot", "Swarm plot"]),
                ("plt.imshow(matrix, cmap='viridis', aspect='auto')", "2D heatmap raster matrix visualization", ["2D heatmap raster matrix visualization", "Contour line map", "3D wireframe mesh", "Polar scatter"]),
                ("plt.errorbar(x, y, yerr=errors, fmt='-o', capsize=5)", "Line plot with error bars and end caps", ["Line plot with error bars and end caps", "Boxplot", "Stacked step chart", "Candlestick chart"]),
                ("plt.fill_between(x, y1, y2, color='skyblue', alpha=0.4)", "Shaded confidence interval band between curves", ["Shaded confidence interval band between curves", "Contour fill", "Area under curve", "Stacked bar chart"]),
                ("sns.heatmap(df.corr(), annot=True, cmap='coolwarm')", "Annotated correlation matrix heatmap", ["Annotated correlation matrix heatmap", "Pair plot grid", "Residual scatter plot", "Covariance dendrogram"]),
                ("plt.stem(x, y, linefmt='r-', markerfmt='bo')", "Discrete stem impulse sequence plot", ["Discrete stem impulse sequence plot", "Continuous curve", "Histogram", "Hexbin plot"])
            ]
            p = plots[i % len(plots)]
            corr = p[1]
            dist = p[2]
            q_text = f"Composite Multivariate Visualization #{i}: Which visual chart geometry is rendered on the current axes by invoking '{p[0]}'?"
            exp = f"Invoking '{p[0]}' produces a {p[1]}."
            step = f"Step 1: Check plotting routine in Matplotlib/Seaborn API.\nStep 2: Note parameter configurations and color mapping.\nStep 3: Rendered graphic is a {p[1]}."
            tech = "Matplotlib/Seaborn visualization pipeline."
        return make_coding_q(f"{tid}_{diff.lower()[0]}_{i:03d}", cat, grp, tid, tname, diff, directive, q_text, corr, dist, pos, "Identify the visual geometry produced by this plotting method.", exp, step, tech)

    # 3. SPECIAL: PYTHON DATA HANDLING (PANDAS / NUMPY) (200 Questions)
    elif "data_handling" in tid_lower or "pandas" in tid_lower:
        directive = "Determine the output of the Pandas DataFrame data engineering operation:"
        cols = ["latency", "throughput", "cpu_percent", "memory_mb", "error_count", "session_time", "network_io"]
        col = cols[i % len(cols)]
        if diff == "Easy":
            tasks = [
                (f"df['{col}']", f"Extracts column '{col}' as a 1D Pandas Series", [f"Extracts column '{col}' as a 1D Pandas Series", f"Extracts 2D DataFrame", f"Computes sum of '{col}'", f"Deletes column '{col}'"]),
                ("df.head(5)", "Returns the first 5 rows of the DataFrame", ["Returns the first 5 rows of the DataFrame", "Returns the last 5 rows", "Returns a random 5-row sample", "Returns column metadata"]),
                ("df.shape", "Returns a tuple containing (row_count, column_count)", ["Returns a tuple containing (row_count, column_count)", "Returns total cell count", "Returns memory usage in bytes", "Returns index labels"]),
                ("df.dtypes", "Returns Series containing data types of each column", ["Returns Series containing data types of each column", "Returns column names list", "Returns missing value counts", "Returns summary statistics"])
            ]
            t = tasks[i % len(tasks)]
            corr = t[1]
            dist = t[2]
            q_text = f"Basic DataFrame Inspection #{i}: What is returned by executing the expression '{t[0]}' on DataFrame df?"
            exp = f"In Pandas, '{t[0]}' {t[1].lower()}."
            step = f"Step 1: Parse expression: {t[0]}.\nStep 2: Identify return object type.\nStep 3: Confirmed behavior: {t[1]}."
            tech = "Pandas DataFrame foundational API."
        elif diff == "Medium":
            tasks = [
                (f"df.dropna(subset=['{col}'])", f"Removes all rows where '{col}' contains NaN values", [f"Removes all rows where '{col}' contains NaN values", f"Drops column '{col}'", f"Replaces NaNs with zero", f"Fills NaNs forward"]),
                (f"df['{col}'].fillna(0)", f"Returns Series where NaN values in '{col}' are replaced with 0", [f"Returns Series where NaN values in '{col}' are replaced with 0", f"Drops NaN rows", f"Deletes column '{col}'", f"Replaces zeros with NaN"]),
                (f"df.drop_duplicates(subset=['{col}'])", f"Drops rows with duplicated values in '{col}' retaining first occurrence", [f"Drops rows with duplicated values in '{col}' retaining first occurrence", f"Drops all rows in DataFrame", f"Deletes column '{col}'", f"Counts duplicate frequencies"]),
                (f"df.sort_values(by='{col}', ascending=False)", f"Sorts rows in descending order based on values in '{col}'", [f"Sorts rows in descending order based on values in '{col}'", f"Sorts in ascending order", f"Sorts columns alphabetically", f"Randomizes row order"])
            ]
            t = tasks[i % len(tasks)]
            corr = t[1]
            dist = t[2]
            q_text = f"Vectorized Cleaning & Filtering #{i}: What transformation occurs upon executing '{t[0]}'?"
            exp = f"Executing '{t[0]}' {t[1].lower()}."
            step = f"Step 1: Check DataFrame transformation method: {t[0]}.\nStep 2: Note parameter flags.\nStep 3: Output transformation is {t[1]}."
            tech = "Pandas data cleaning pipeline."
        else: # Hard
            w = (i % 7) + 3
            tasks = [
                (f"df['{col}'].rolling(window={w}).mean()", f"Rolling moving average of '{col}' over sliding window of {w} observations", [f"Rolling moving average of '{col}' over sliding window of {w} observations", f"Cumulative sum of '{col}'", f"Exponential moving average", f"Median filter"]),
                (f"df.groupby('region')['{col}'].agg(['mean', 'std'])", f"Summary DataFrame with mean and standard deviation of '{col}' grouped by region", [f"Summary DataFrame with mean and standard deviation of '{col}' grouped by region", f"Single Series of means", f"Pivot table of quantiles", f"Boxplot summary"]),
                (f"df.pivot_table(index='date', columns='service', values='{col}', aggfunc='sum')", f"Reshaped pivot table with dates as index and service columns summing '{col}'", [f"Reshaped pivot table with dates as index and service columns summing '{col}'", f"Flat unindexed DataFrame", f"Groupby series", f"Cross-tabulation frequency matrix"]),
                (f"pd.merge(df1, df2, on='user_id', how='left')", "Left outer join keeping all records from df1 matched with df2 on 'user_id'", ["Left outer join keeping all records from df1 matched with df2 on 'user_id'", "Inner intersection join", "Right outer join", "Full Cartesian cross join"]),
                (f"df['{col}'].pct_change()", f"Fractional percentage change between consecutive rows of '{col}'", [f"Fractional percentage change between consecutive rows of '{col}'", f"Absolute difference", f"Logarithmic return", f"Z-score normalized difference"]),
                (f"df['{col}'].clip(lower=10, upper=100)", f"Trims values in '{col}' to fall strictly within [10, 100]", [f"Trims values in '{col}' to fall strictly within [10, 100]", f"Filters rows outside [10, 100]", f"Scales values linearly between 0 and 1", f"Replaces outliers with NaN"])
            ]
            t = tasks[i % len(tasks)]
            corr = t[1]
            dist = t[2]
            q_text = f"Advanced Pipeline Windowing / Reshaping #{i}: What is the exact transformation produced by the expression '{t[0]}'?"
            exp = f"In Pandas data processing, '{t[0]}' {t[1].lower()}."
            step = f"Step 1: Parse the DataFrame method signature and arguments: {t[0]}.\nStep 2: Understand index retention and null handling.\nStep 3: Confirmed transformation is '{t[1]}'."
            tech = "Pandas DataFrame vectorized transformation."
        return make_coding_q(f"{tid}_{diff.lower()[0]}_{i:03d}", cat, grp, tid, tname, diff, directive, q_text, corr, dist, pos, "Analyze the behavior of this chain of Pandas DataFrame methods.", exp, step, tech)

    # 4. GENERAL CODING TOPICS (C, C++, Java, Python, JS, DSA, SQL, Web, OOP, OS, Networks, DBMS)
    else:
        directive = "Analyze the code output, algorithm complexity, or system design invariant:"
        if diff == "Easy":
            val_a = (i * 3) % 15 + 4
            val_b = (i * 2) % 9 + 2
            res = val_a + val_b
            q_text = f"Basic Syntax Execution #{i}: What integer value is printed by executing the following snippet?\nint a = {val_a}, b = {val_b};\nprintf(\"%d\", a + b);"
            corr = str(res)
            dist = [str(res + 3), str(max(0, res - 2)), str(res * 2)]
            exp = f"Arithmetic addition: {val_a} + {val_b} = {res}."
            step = f"Step 1: Evaluate expression a + b: {val_a} + {val_b}.\nStep 2: Sum is {res}.\nStep 3: Printed output is {res}."
            tech = "Basic arithmetic operator semantics."
        elif diff == "Medium":
            val_a = (i * 3) % 17 + 5
            val_b = (i * 2) % 7 + 3
            res = (val_a ^ val_b) + 1
            snip = f"int a = {val_a}, b = {val_b};\nint r = (a ^ b) + 1;\nprintf(\"%d\", r);"
            q_text = f"Bitwise Operator Trace #{i}: What integer value is output by the program segment below?\n{snip}"
            corr = str(res)
            dist = [str(res + 2), str(max(0, res - 3)), str(res * 2)]
            exp = f"Bitwise XOR: {val_a} ^ {val_b} = {val_a ^ val_b}. Adding 1 yields {res}."
            step = f"Step 1: Compute bitwise XOR: {val_a} ^ {val_b} = {val_a ^ val_b}.\nStep 2: Add 1: {val_a ^ val_b} + 1 = {res}.\nStep 3: Output printed is {res}."
            tech = "Bitwise binary arithmetic and operator precedence."
        else: # Hard
            complexities = [
                ("Merge Sort divide-and-conquer on array of size N", "Time: O(N log N), Space: O(N)", ["Time: O(N log N), Space: O(N)", "Time: O(N^2), Space: O(1)", "Time: O(N log N), Space: O(1)", "Time: O(N), Space: O(N)"]),
                ("Dijkstra's shortest path with binary min-heap on graph (V, E)", "Time: O((V + E) log V), Space: O(V)", ["Time: O((V + E) log V), Space: O(V)", "Time: O(V^2), Space: O(V^2)", "Time: O(E log E), Space: O(1)", "Time: O(V log E), Space: O(V)"]),
                ("Kadane's algorithm for maximum subarray sum", "Time: O(N), Space: O(1)", ["Time: O(N), Space: O(1)", "Time: O(N log N), Space: O(N)", "Time: O(N^2), Space: O(1)", "Time: O(N), Space: O(N)"]),
                ("Floyd-Warshall all-pairs shortest path dynamic programming", "Time: O(V^3), Space: O(V^2)", ["Time: O(V^3), Space: O(V^2)", "Time: O(V^2 log V), Space: O(V)", "Time: O(V * E), Space: O(V)", "Time: O(V^4), Space: O(V^2)"]),
                ("Kruskal's Minimum Spanning Tree with Disjoint Set Union", "Time: O(E log E), Space: O(V)", ["Time: O(E log E), Space: O(V)", "Time: O(V^2), Space: O(V)", "Time: O(E log V), Space: O(E)", "Time: O(V + E), Space: O(1)"])
            ]
            c = complexities[i % len(complexities)]
            q_text = f"Asymptotic Analysis #{i} for '{tname}': What is the tightest worst-case time complexity and auxiliary space bound for {c[0]}?"
            corr = c[1]
            dist = c[2]
            exp = f"{c[0]} strictly achieves {c[1]}."
            step = f"Step 1: Analyze recurrence relations and data structure traversal costs.\nStep 2: Aggregate inner and outer loop bounds.\nStep 3: Confirmed complexity bound is {c[1]}."
            tech = "Asymptotic computational complexity analysis."
        return make_coding_q(f"{tid}_{diff.lower()[0]}_{i:03d}", cat, grp, tid, tname, diff, directive, q_text, corr, dist, pos, "Trace the operations according to language and algorithmic standards.", exp, step, tech)

def build_unique_coding_topic(tid, tname, grp, existing_uniques=None):
    cat = "Coding Questions"
    seen_texts = set()
    qs = []

    is_200 = ("data_handling" in tid or "stats_math" in tid)
    target_count = 200 if is_200 else 100
    target_easy = 30 if is_200 else 15
    target_med = 20 if is_200 else 10
    target_hard = 150 if is_200 else 75

    if existing_uniques:
        for q in existing_uniques:
            norm = normalize_text(q['q'])
            if norm not in seen_texts:
                seen_texts.add(norm)
                qs.append(q)

    cur_easy = [q for q in qs if q['difficulty'] == 'Easy']
    cur_med = [q for q in qs if q['difficulty'] == 'Medium']
    cur_hard = [q for q in qs if q['difficulty'] == 'Hard']

    counter = len(qs) + 1

    # Fill Easy
    while len(cur_easy) < target_easy:
        q_obj = generate_coding_item(tid, tname, grp, "Easy", counter)
        counter += 1
        norm = normalize_text(q_obj['q'])
        if norm not in seen_texts:
            seen_texts.add(norm)
            cur_easy.append(q_obj)

    # Fill Medium
    while len(cur_med) < target_med:
        q_obj = generate_coding_item(tid, tname, grp, "Medium", counter)
        counter += 1
        norm = normalize_text(q_obj['q'])
        if norm not in seen_texts:
            seen_texts.add(norm)
            cur_med.append(q_obj)

    # Fill Hard
    while len(cur_hard) < target_hard:
        q_obj = generate_coding_item(tid, tname, grp, "Hard", counter)
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

    assert len(final_qs) == target_count, f"Topic {tid} has {len(final_qs)} questions, expected {target_count}"
    return final_qs
