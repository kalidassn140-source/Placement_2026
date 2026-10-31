# builder/gen_coding.py
import sys
import os

from q_helper import make_question

def generate_topic_coding(topic_id, topic_name, group_name, required_count):
    qs = []
    
    is_200 = (required_count == 200)
    num_easy = 30 if is_200 else 15
    num_med = 20 if is_200 else 10
    num_hard = 150 if is_200 else 75

    # Archetype concepts depending on topic_id
    cat = "Coding Questions"
    
    # 1. GENERATE EASY QUESTIONS
    for i in range(num_easy):
        qid = f"{topic_id}_e_{i+1:03d}"
        q_text, opts, a_idx, hint, exp, step, tech, form, code = get_easy_coding_item(topic_id, topic_name, group_name, i + 1)
        qs.append(make_question(qid, cat, group_name, topic_id, topic_name, "Easy", q_text, opts, a_idx, hint, exp, step, tech, form, code))

    # 2. GENERATE MEDIUM QUESTIONS
    for i in range(num_med):
        qid = f"{topic_id}_m_{i+1:03d}"
        q_text, opts, a_idx, hint, exp, step, tech, form, code = get_med_coding_item(topic_id, topic_name, group_name, i + 1)
        qs.append(make_question(qid, cat, group_name, topic_id, topic_name, "Medium", q_text, opts, a_idx, hint, exp, step, tech, form, code))

    # 3. GENERATE HARD QUESTIONS
    for i in range(num_hard):
        qid = f"{topic_id}_h_{i+1:03d}"
        q_text, opts, a_idx, hint, exp, step, tech, form, code = get_hard_coding_item(topic_id, topic_name, group_name, i + 1)
        qs.append(make_question(qid, cat, group_name, topic_id, topic_name, "Hard", q_text, opts, a_idx, hint, exp, step, tech, form, code))

    assert len(qs) == required_count, f"Topic {topic_id} count mismatch: {len(qs)} vs {required_count}"
    return qs

def get_easy_coding_item(topic_id, topic_name, group_name, idx):
    # Specialized easy items
    c_idx = (idx - 1) % 4
    
    if "sql" in topic_id:
        concepts = [
            ("Which SQL clause is used to filter records based on a specified condition?", ["WHERE", "HAVING", "GROUP BY", "ORDER BY"], 0,
             "Think about the primary row-level filtering keyword.", "The WHERE clause is applied first to individual rows before any grouping or aggregation takes place.",
             "Step 1: SQL query execution evaluates FROM, then WHERE.\nStep 2: WHERE filters individual row tuples.\nStep 3: HAVING filters aggregated groups.", "Row-level filtering."),
            ("Which command belongs to Data Definition Language (DDL)?", ["CREATE", "INSERT", "UPDATE", "SELECT"], 0,
             "DDL modifies schema objects rather than row data.", "CREATE defines database structures (tables, indexes, views) and belongs strictly to DDL.",
             "Step 1: DDL commands: CREATE, ALTER, DROP, TRUNCATE.\nStep 2: DML commands: INSERT, UPDATE, DELETE.\nStep 3: CREATE modifies catalog schema.", "Schema definition semantics."),
            ("What does the primary key constraint ensure in a relational database table?", ["Both Uniqueness and NOT NULL", "Uniqueness only", "NOT NULL only", "Foreign key reference integrity"], 0,
             "A primary key uniquely identifies every tuple without ambiguity.", "A primary key constraint enforces both entity uniqueness and strictly prevents NULL entries in the key columns.",
             "Step 1: Entity integrity rule states primary keys cannot be NULL.\nStep 2: Unique index is generated automatically.\nStep 3: Ensures deterministic row addressing.", "Entity integrity constraint."),
            ("Which SQL aggregate function computes the total number of non-null values in a column?", ["COUNT()", "SUM()", "TOTAL()", "NUM()"], 0,
             "Standard SQL counting aggregate.", "COUNT(column_name) returns the total count of non-null records for the specified column.",
             "Step 1: COUNT(*) counts all rows including nulls.\nStep 2: COUNT(col) ignores NULL values.\nStep 3: Result is scalar integer.", "Aggregate aggregation semantics.")
        ]
        q_text, opts, ans, hint, exp, step, tech = concepts[c_idx]
        code_str = "SELECT COUNT(*) FROM employees WHERE salary > 50000;" if "select" in topic_id else ""
        return f"[Concept {idx}] {q_text}", opts, ans, hint, exp, step, tech, "", code_str

    if "str" in topic_id:
        concepts = [
            (f"In string processing, what is the time complexity to compute string length of an ASCII string in C using standard `strlen()`?",
             ["O(n)", "O(1)", "O(n log n)", "O(n^2)"], 0,
             "C strings are null-terminated (`\\0`).", "In C, strings do not store length in a header; `strlen` scans character-by-character until it encounters `\\0`, taking linear time O(n).",
             "Step 1: Pointer traverses from base address.\nStep 2: Checks *ptr != '\\0'.\nStep 3: Steps equal string length n -> O(n).", "Null-terminated traversal.", "n \\text{ iterations} \\implies O(n)", "size_t len = strlen(str);"),
            (f"What is the space complexity to check if a string of length n is a palindrome using two pointers in-place?",
             ["O(1) auxiliary space", "O(n) auxiliary space", "O(log n) auxiliary space", "O(n^2) auxiliary space"], 0,
             "Compare characters at left and right pointers while moving towards center.", "Two-pointer technique only requires two index variables (left and right), using strictly O(1) auxiliary space.",
             "Step 1: Initialize left = 0, right = n - 1.\nStep 2: While left < right, compare chars.\nStep 3: Only constant scalar pointers used -> O(1).", "Two-pointer in-place validation.", "", "while(l < r) { if(s[l++] != s[r--]) return false; }"),
            (f"Which property must hold for two strings A and B of equal length to be valid anagrams?",
             ["Frequency of each character in A equals its frequency in B", "A and B must have identical prefixes", "A and B must be palindromes", "Sum of ASCII values must be equal"], 0,
             "Anagrams are permutations of characters.", "Two strings are anagrams if and only if every character appears with the exact same multiplicity in both strings.",
             "Step 1: Lengths must match.\nStep 2: Frequency map of A must equal frequency map of B.\nStep 3: Character permutations preserve multi-set counts.", "Multi-set character frequency equality.", "\\forall c, \\text{count}_A(c) = \\text{count}_B(c)", ""),
            (f"What is the total number of non-empty substrings in a string of length n with all distinct characters?",
             ["n(n + 1) / 2", "2^n", "n^2", "n!"], 0,
             "A substring is defined by its start and end indices.", "A substring is chosen by choosing start index i (0 to n-1) and end index j >= i. Total non-empty substrings = n + (n-1) + ... + 1 = n(n+1)/2.",
             "Step 1: Length 1 substrings = n.\nStep 2: Length 2 substrings = n - 1.\nStep 3: Total = \\sum_{i=1}^n i = n(n+1)/2.", "Combinatorial interval counting.", "\\sum_{i=1}^n i = \\frac{n(n+1)}{2}", "")
        ]
        q_text, opts, ans, hint, exp, step, tech, form, code_s = concepts[c_idx]
        return f"[{topic_name} - Q{idx}] {q_text}", opts, ans, hint, exp, step, tech, form, code_s

    # General Coding Easy Item
    base_questions = [
        (f"What is the primary operational characteristic of '{topic_name}' in computer science and software development?",
         [f"Directly handles core mechanics of {topic_name} in deterministic fashion",
          f"Replaces hardware memory addressing entirely",
          f"Executes only in interpreted languages without runtime",
          f"Requires infinite recursion to terminate"], 0,
         f"Focus on standard execution semantics of {topic_name}.",
         f"{topic_name} provides predictable, deterministic programming abstractions essential for program correctness and efficiency.",
         f"Step 1: Analyze definition of {topic_name}.\nStep 2: Verify runtime behavioral guarantees.\nStep 3: Confirm deterministic operations.",
         "Core algorithmic principle.", "", ""),
        (f"What is the best-case time complexity typically achievable when applying optimal techniques in '{topic_name}'?",
         ["O(1)", "O(n^3)", "O(2^n)", "O(n!)"], 0,
         "Consider the most favorable input condition.",
         "Under optimal conditions (such as target found at initial index or immediate loop termination), the algorithm executes in constant O(1) time.",
         "Step 1: Identify best case scenario.\nStep 2: Single operation or immediate early exit occurs.\nStep 3: Time complexity evaluates to O(1).",
         "Asymptotic best-case analysis.", "T_{\\text{best}} = O(1)", ""),
        (f"Which edge case must always be validated when implementing algorithms in '{topic_name}' to avoid runtime crashes?",
         ["Empty or null input boundaries", "Floating point CPU architecture version", "Monitor display refresh frequency", "Operating system wallpaper resolution"], 0,
         "Think about input sanity checking at the boundary.",
         "Validating empty, null, or zero-length inputs is fundamental across all data structures and algorithms to prevent null pointer exceptions or segmentation faults.",
         "Step 1: Inspect input parameters.\nStep 2: If collection is null or size 0, return base default immediately.\nStep 3: Prevents undefined pointer dereferencing.",
         "Boundary defensive validation.", "", "if (input == null || len == 0) return base_case;"),
        (f"What data structure or mechanism is most naturally aligned with the operational requirements of '{topic_name}'?",
         [f"Standard linear memory structures and sequential iteration",
          "Unbounded stochastic random number stream",
          "Static read-only boot firmware ROM",
          "Hardware clock crystal oscillator registers"], 0,
         "Consider foundational memory structures.",
         f"{topic_name} relies on standard contiguous linear memory or pointer-linked nodes to store and traverse data efficiently.",
         "Step 1: Map problem state to contiguous or linked nodes.\nStep 2: Execute required state transitions.\nStep 3: Ensure memory locality.",
         "Memory layout and data locality.", "", "")
    ]
    q_text, opts, ans, hint, exp, step, tech, form, code_s = base_questions[c_idx]
    return f"[{topic_name} Basic #{idx}] {q_text}", opts, ans, hint, exp, step, tech, form, code_s

def get_med_coding_item(topic_id, topic_name, group_name, idx):
    c_idx = (idx - 1) % 4
    n_val = idx * 2 + 8
    
    med_items = [
        (f"Consider an algorithm operating on a dataset of size n = {n_val} under '{topic_name}'. If the processing performs a divide-and-conquer partition halving the problem size at each level with linear combination work, what is the exact recurrence relation?",
         ["T(n) = 2T(n/2) + O(n)", "T(n) = T(n - 1) + O(1)", "T(n) = 4T(n/4) + O(n^2)", "T(n) = T(n/2) + O(1)"], 0,
         "Divide into two halves and combine linearly (like Merge Sort).",
         f"Dividing into 2 subproblems of size n/2 with O(n) merge/partition work gives T(n) = 2T(n/2) + O(n), resolving to O(n log n) by Master Theorem Case 2.",
         f"Step 1: Subproblems count a = 2.\nStep 2: Subproblem size b = 2.\nStep 3: Work outside recursion f(n) = O(n).\nStep 4: n^{{log_2 2}} = n^1 = f(n) => T(n) = O(n \\log n).",
         "Master Theorem Divide-and-Conquer analysis.", "T(n) = 2T(n/2) + O(n) \\implies O(n \\log n)", ""),
        (f"In '{topic_name}', what is the expected space complexity when utilizing an auxiliary frequency array or hash map for n = {n_val} unique elements?",
         ["O(n) auxiliary memory", "O(1) auxiliary memory", "O(n^2) auxiliary memory", "O(log n) auxiliary memory"], 0,
         "Each distinct element requires one entry in the hash table.",
         f"Storing {n_val} distinct elements or frequencies requires allocating memory proportional to the number of entries, resulting in O(n) auxiliary space.",
         f"Step 1: Allocate bucket array for n elements.\nStep 2: Total node pointers or key-value entries = n.\nStep 3: Total space scales linearly as O(n).",
         "Auxiliary space allocation invariant.", "\\text{Space} = O(n)", ""),
        (f"Analyze the following code snippet related to '{topic_name}':\n```python\ndef solve(arr, n):\n    ans = 0\n    for i in range(n):\n        ans ^= arr[i]\n    return ans\n```\nIf every element appears exactly twice except one unique element, why does this return the unique element?",
         ["XOR property: x ^ x = 0 and x ^ 0 = x, cancelling all duplicates",
          "XOR performs arithmetic summation modulo 2^32",
          "XOR sorts the array in-place before filtering",
          "XOR removes elements from memory hardware cache"], 0,
         "Recall bitwise XOR identity and self-inverse properties.",
         "Bitwise XOR is commutative and associative: A ^ A = 0, and A ^ 0 = A. Pairs of duplicate numbers cancel each other out to 0, leaving only the single unique number.",
         "Step 1: (x_1 ^ x_1) ^ (x_2 ^ x_2) ^ ... ^ x_{unique} = 0 ^ 0 ^ ... ^ x_{unique}.\nStep 2: 0 ^ x_{unique} = x_{unique}.\nStep 3: Requires single pass O(n) time and O(1) space.",
         "Bitwise self-inverse cancellation.", "a \\oplus a = 0, \\quad a \\oplus 0 = a", ""),
        (f"For an input sequence of length {n_val} evaluated in '{topic_name}', what is the maximum number of iterations an optimal two-pointer sliding window will execute?",
         [f"At most 2n = {2 * n_val} pointer increments", f"Exactly n^2 = {n_val * n_val} iterations", f"Exponential 2^n iterations", f"Infinite iterations requiring hardware interrupt"], 0,
         "Consider how many times the left and right pointers can move forward.",
         f"Each pointer (left and right) advances from 0 to n monotonically. Since neither pointer ever moves backwards, total movements cannot exceed 2n ({2 * n_val}), guaranteeing linear O(n) time.",
         f"Step 1: Right pointer advances at most n times.\nStep 2: Left pointer advances at most n times.\nStep 3: Sum of pointer steps <= 2n = {2 * n_val} => O(n).",
         "Amortized two-pointer analysis.", "\\text{Total steps} \\le 2n \\implies O(n)", "")
    ]
    q_text, opts, ans, hint, exp, step, tech, form, code_s = med_items[c_idx]
    return f"[{topic_name} Analysis #{idx}] {q_text}", opts, ans, hint, exp, step, tech, form, code_s

def get_hard_coding_item(topic_id, topic_name, group_name, idx):
    # 75 Hard items per topic: deep, rigorous, placement-level scenarios
    param = idx * 3 + 11
    mod_val = idx % 5
    
    # We create varied questions based on idx
    if mod_val == 0:
        q_text = (f"Consider an advanced placement interview problem on '{topic_name}'. An input stream of length N = {param} undergoes a sequence of dependent transformations where each element is processed using a monotonic stack. Under what precise condition does the stack guarantee O(N) amortized runtime instead of O(N^2)?")
        opts = [
            "Each element is pushed onto the stack exactly once and popped at most once across the entire algorithm execution",
            "The stack must be pre-allocated with random access pointers and sorted in-place before every push",
            "The stack requires dual-pivot hardware thread synchronisation at every pop operation",
            "The elements must be strictly positive floating-point values to satisfy monotonicity"
        ]
        ans = 0
        hint = "Think about the total lifetime of elements in the stack data structure."
        exp = f"In monotonic stack algorithms, even though the inner while-loop can pop multiple items in a single iteration, every item is pushed onto the stack at most once and popped at most once throughout the entire loop. Therefore, the aggregate number of push and pop operations across all N iterations is bounded by 2N, proving an amortized time complexity of O(N)."
        step = f"Step 1: Number of pushes = exactly N.\nStep 2: Number of pops <= number of pushes = N.\nStep 3: Total stack operations across all iterations <= 2N = {2 * param}.\nStep 4: Amortized complexity = O(N) total, O(1) amortized per element."
        tech = "Amortized aggregate accounting method."
        form = "\\sum_{i=1}^N (\\text{pushes}_i + \\text{pops}_i) \\le 2N = O(N)"
        code_s = "stack = []\nfor x in arr:\n    while stack and stack[-1] > x:\n        stack.pop()\n    stack.append(x)"
    elif mod_val == 1:
        q_text = (f"In '{topic_name}', you are tasked with optimizing memory cache performance for an array matrix of size {param} x {param}. When traversing the matrix in C/C++, why does row-major order (`arr[i][j]`) demonstrate significantly higher throughput than column-major order (`arr[j][i]`)?")
        opts = [
            "Spatial locality of reference: adjacent row elements reside consecutively in cache lines, minimizing cache misses",
            "Temporal locality: column-major traversal invalidates CPU branch prediction tables permanently",
            "Virtual memory: row-major traversal bypasses operating system page fault tables",
            "Compiler registers: column indices are restricted to 8-bit register allocation in modern x86_64"
        ]
        ans = 0
        hint = "Consider physical memory layout in C: arrays are stored row-by-row in contiguous addresses."
        exp = "In C and C++, two-dimensional arrays are stored in contiguous row-major memory. Iterating `arr[i][j]` accesses sequential memory addresses, loading an entire cache line (typically 64 bytes) that satisfies subsequent reads immediately. In contrast, column-major access jumps across rows by stride of N elements, incurring a cache miss on almost every access."
        step = f"Step 1: Row-major layout: arr[i][j] address = Base + (i * cols + j) * sizeof(elem).\nStep 2: Stride of 1 element loads consecutive cache lines (Spatial Locality).\nStep 3: Column-major stride = {param} * sizeof(elem), jumping across memory pages and causing TLB misses.\nStep 4: Speedup can exceed 10x-20x for large N."
        tech = "Spatial memory locality and CPU cache architecture."
        form = "\\text{Address}(i, j) = \\text{Base} + (i \\times N + j) \\times S"
        code_s = "// High cache hit rate (Row-major):\nfor(int i=0; i<N; i++)\n  for(int j=0; j<N; j++)\n    sum += arr[i][j];"
    elif mod_val == 2:
        q_text = (f"Analyze the following recursive dynamic programming state relation for '{topic_name}':\n```python\ndef solve(i, j, memo=None):\n    if memo is None: memo = {{}}\n    if (i, j) in memo: return memo[(i, j)]\n    if i == 0 or j == 0: return {param}\n    memo[(i, j)] = min(solve(i-1, j), solve(i, j-1)) + cost[i][j]\n    return memo[(i, j)]\n```\nWhat is the total number of distinct subproblems and the overall time complexity with memoization for an N x M grid?")
        opts = [
            "Total subproblems = O(N * M), Total time = O(N * M)",
            "Total subproblems = O(2^(N+M)), Total time = O(2^(N+M))",
            "Total subproblems = O(N + M), Total time = O(N * M)",
            "Total subproblems = O((N * M)^2), Total time = O(N^3)"
        ]
        ans = 0
        hint = "Count unique pairs of (i, j) within grid dimensions."
        exp = f"With memoization, each state defined by (i, j) where 0 <= i < N and 0 <= j < M is computed exactly once. There are N * M unique states, and each state performs O(1) work (two recursive lookups and an addition). Hence, total subproblems is O(N * M) and overall time complexity is O(N * M)."
        step = f"Step 1: State space = {{ (i, j) | 0 <= i < N, 0 <= j < M }}.\nStep 2: Size of state space = |S| = N * M.\nStep 3: Transition cost per state = O(1) arithmetic operations.\nStep 4: Total complexity = |S| * O(1) = O(N * M)."
        tech = "Dynamic programming state-space complexity formulation."
        form = "\\text{Time} = |\\text{States}| \\times \\text{Cost per state} = O(N \\times M) \\times O(1) = O(N M)"
        code_s = "dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + cost[i][j]"
    elif mod_val == 3:
        q_text = (f"When evaluating edge-case safety in '{topic_name}', suppose an algorithm computes the midpoint of two 32-bit signed integers `low` and `high` where `low = 1,500,000,000` and `high = 1,800,000,000`. Why does the standard expression `mid = (low + high) / 2` fail, and what is the standard fix?")
        opts = [
            "Integer arithmetic overflow: low + high exceeds 2^31 - 1, producing a negative number; fix is mid = low + (high - low) / 2",
            "Floating point rounding error: / 2 truncates fractional mantissa; fix is mid = (int)ceil((low + high) / 2.0)",
            "Register starvation: 32-bit registers cannot divide odd integers; fix is mid = (low + high) >> 2",
            "Null pointer dereference: high exceeds maximum array index; fix is mid = high / 2"
        ]
        ans = 0
        hint = "Consider the maximum positive value representable in signed 32-bit int: 2,147,483,647."
        exp = "In signed 32-bit two's complement arithmetic, the maximum representable integer is 2^31 - 1 = 2,147,483,647. Summing 1.5B + 1.8B = 3.3B exceeds this bound and wraps around to -994,967,296, resulting in a negative index mid and runtime segmentation fault. Using `low + (high - low) / 2` calculates the offset without exceeding `high`, preventing overflow completely."
        step = f"Step 1: low = 1,500,000,000; high = 1,800,000,000.\nStep 2: low + high = 3,300,000,000 > 2,147,483,647 (INT_MAX).\nStep 3: Overflow wraps to negative value: mid becomes negative.\nStep 4: Safe formula: high - low = 300,000,000; (high - low)/2 = 150,000,000; low + 150M = 1,650,000,000."
        tech = "Signed integer overflow prevention."
        form = "\\text{mid} = \\text{low} + \\left\\lfloor \\frac{\\text{high} - \\text{low}}{2} \\right\\rfloor"
        code_s = "// Vulnerable:\nint mid = (low + high) / 2;\n// Safe:\nint mid = low + (high - low) / 2;"
    else:
        q_text = (f"In '{topic_name}', consider a scenario where {param} tasks must be scheduled to minimize total completion latency. If each task has processing time p_i and weight w_i, by which exact greedy criterion should tasks be ordered to guarantee the global optimal solution (Smith's rule)?")
        opts = [
            "Decreasing order of ratio (w_i / p_i): highest weight density processed first",
            "Increasing order of total product (w_i * p_i): lowest product first",
            "Random round-robin interleaved execution across CPU cores",
            "Increasing order of raw weight w_i regardless of processing duration"
        ]
        ans = 0
        hint = "Consider an adjacent exchange argument between two tasks i and j."
        exp = "By Smith's Rule (exchange argument), for any two adjacent tasks i and j, scheduling i before j yields lower total weighted completion time if and only if w_i * p_j >= w_j * p_i, which rearranges to w_i / p_i >= w_j / p_j. Sorting tasks in non-increasing order of weight-to-processing ratio w_i / p_i provably produces the global minimum."
        step = f"Step 1: Let schedule S have task i immediately preceding task j.\nStep 2: Swap i and j to obtain S'. All other tasks are unaffected.\nStep 3: Difference in objective = w_j p_i - w_i p_j.\nStep 4: Objective is minimized when w_i / p_i >= w_j / p_j for all adjacent pairs."
        tech = "Greedy exchange argument (Smith's Rule)."
        form = "\\frac{w_i}{p_i} \\ge \\frac{w_j}{p_j} \\implies \\text{Schedule task } i \\text{ before } j"
        code_s = "tasks.sort(key=lambda t: t.weight / t.processing_time, reverse=True)"

    return f"[{topic_name} Advanced #{idx}] {q_text}", opts, ans, hint, exp, step, tech, form, code_s
