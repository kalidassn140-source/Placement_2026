# build_catalog.py
import json
import os

def create_catalog():
    topics = []
    
    # 1. CODING QUESTIONS (166 topics)
    coding_groups = [
        ("Programming Fundamentals", [
            ("coding_pf_basic", "Basic Coding Questions"),
            ("coding_pf_vars", "Variables and Data Types"),
            ("coding_pf_ops", "Operators"),
            ("coding_pf_cond", "Conditional Statements"),
            ("coding_pf_ifelse", "If-Else Statements"),
            ("coding_pf_nestedif", "Nested If-Else"),
            ("coding_pf_switch", "Switch Statements"),
            ("coding_pf_loops", "Loops"),
            ("coding_pf_for", "For Loop"),
            ("coding_pf_while", "While Loop"),
            ("coding_pf_dowhile", "Do-While Loop"),
            ("coding_pf_breakcont", "Break and Continue"),
            ("coding_pf_funcs", "Functions"),
            ("coding_pf_params", "Function Parameters and Return Values"),
            ("coding_pf_recursion", "Recursion"),
            ("coding_pf_patterns", "Pattern Printing"),
            ("coding_pf_numbers", "Number-Based Programs"),
            ("coding_pf_mathprob", "Mathematical Programming Problems")
        ]),
        ("String Programming", [
            ("coding_str_fund", "String Fundamentals"),
            ("coding_str_io", "String Input and Output"),
            ("coding_str_len", "String Length"),
            ("coding_str_rev", "String Reversal"),
            ("coding_str_palin", "Palindrome Strings"),
            ("coding_str_anagram", "Anagram Problems"),
            ("coding_str_freq", "Character Frequency"),
            ("coding_str_vowels", "Vowel and Consonant Problems"),
            ("coding_str_substr", "Substrings"),
            ("coding_str_search", "String Searching"),
            ("coding_str_sort", "String Sorting"),
            ("coding_str_manip", "String Manipulation"),
            ("coding_str_conv", "String Conversion"),
            ("coding_str_adv", "Advanced String Problems")
        ]),
        ("Arrays", [
            ("coding_arr_fund", "Array Fundamentals"),
            ("coding_arr_traversal", "Array Traversal"),
            ("coding_arr_insertion", "Array Insertion"),
            ("coding_arr_deletion", "Array Deletion"),
            ("coding_arr_search", "Array Searching"),
            ("coding_arr_sort", "Array Sorting"),
            ("coding_arr_minmax", "Maximum and Minimum Elements"),
            ("coding_arr_sec_large", "Second Largest Element"),
            ("coding_arr_dup", "Duplicate Elements"),
            ("coding_arr_freq", "Frequency Counting"),
            ("coding_arr_rev", "Array Reversal"),
            ("coding_arr_rot", "Rotation of Arrays"),
            ("coding_arr_2d", "Two-Dimensional Arrays"),
            ("coding_arr_matrix", "Matrix Operations"),
            ("coding_arr_subarr", "Subarrays"),
            ("coding_arr_prefix", "Prefix Sum"),
            ("coding_arr_slide", "Sliding Window"),
            ("coding_arr_twoptr", "Two-Pointer Technique")
        ]),
        ("Data Structures", [
            ("coding_ds_fund", "Data Structure Fundamentals"),
            ("coding_ds_stack", "Stack"),
            ("coding_ds_stack_ops", "Stack Operations"),
            ("coding_ds_queue", "Queue"),
            ("coding_ds_circ_queue", "Circular Queue"),
            ("coding_ds_prio_queue", "Priority Queue"),
            ("coding_ds_deque", "Deque"),
            ("coding_ds_singly_ll", "Singly Linked List"),
            ("coding_ds_doubly_ll", "Doubly Linked List"),
            ("coding_ds_circ_ll", "Circular Linked List"),
            ("coding_ds_ll_ins", "Linked List Insertion"),
            ("coding_ds_ll_del", "Linked List Deletion"),
            ("coding_ds_ll_rev", "Linked List Reversal"),
            ("coding_ds_hash_tbl", "Hash Tables"),
            ("coding_ds_hash_map", "Hash Maps"),
            ("coding_ds_sets", "Sets"),
            ("coding_ds_trees", "Trees"),
            ("coding_ds_bin_trees", "Binary Trees"),
            ("coding_ds_bst", "Binary Search Trees"),
            ("coding_ds_tree_trav", "Tree Traversal"),
            ("coding_ds_heap", "Heap"),
            ("coding_ds_graph_fund", "Graph Fundamentals"),
            ("coding_ds_graph_rep", "Graph Representation"),
            ("coding_ds_bfs", "Breadth-First Search (BFS)"),
            ("coding_ds_dfs", "Depth-First Search (DFS)")
        ]),
        ("Algorithms", [
            ("coding_algo_fund", "Algorithm Fundamentals"),
            ("coding_algo_time_comp", "Time Complexity"),
            ("coding_algo_space_comp", "Space Complexity"),
            ("coding_algo_big_o", "Big-O Notation"),
            ("coding_algo_lin_search", "Linear Search"),
            ("coding_algo_bin_search", "Binary Search"),
            ("coding_algo_bubble_sort", "Bubble Sort"),
            ("coding_algo_sel_sort", "Selection Sort"),
            ("coding_algo_ins_sort", "Insertion Sort"),
            ("coding_algo_merge_sort", "Merge Sort"),
            ("coding_algo_quick_sort", "Quick Sort"),
            ("coding_algo_heap_sort", "Heap Sort"),
            ("coding_algo_count_sort", "Counting Sort"),
            ("coding_algo_radix_sort", "Radix Sort"),
            ("coding_algo_twoptr", "Two-Pointer Algorithms"),
            ("coding_algo_sliding_win", "Sliding Window Algorithms"),
            ("coding_algo_greedy", "Greedy Algorithms"),
            ("coding_algo_dp", "Dynamic Programming"),
            ("coding_algo_backtrack", "Backtracking"),
            ("coding_algo_div_conq", "Divide and Conquer"),
            ("coding_algo_graphs", "Graph Algorithms"),
            ("coding_algo_shortest_path", "Shortest Path Algorithms")
        ]),
        ("Database and SQL", [
            ("coding_sql_db_fund", "Database Fundamentals"),
            ("coding_sql_dbms", "DBMS"),
            ("coding_sql_rdbms", "RDBMS"),
            ("coding_sql_fund", "SQL Fundamentals"),
            ("coding_sql_ddl", "DDL Commands"),
            ("coding_sql_dml", "DML Commands"),
            ("coding_sql_dcl", "DCL Commands"),
            ("coding_sql_tcl", "TCL Commands"),
            ("coding_sql_select", "SELECT Queries"),
            ("coding_sql_where", "WHERE Clause"),
            ("coding_sql_order_by", "ORDER BY"),
            ("coding_sql_group_by", "GROUP BY"),
            ("coding_sql_having", "HAVING Clause"),
            ("coding_sql_agg_funcs", "Aggregate Functions"),
            ("coding_sql_joins", "Joins"),
            ("coding_sql_inner_join", "Inner Join"),
            ("coding_sql_left_join", "Left Join"),
            ("coding_sql_right_join", "Right Join"),
            ("coding_sql_full_join", "Full Outer Join"),
            ("coding_sql_subqueries", "Subqueries"),
            ("coding_sql_nested_q", "Nested Queries"),
            ("coding_sql_pri_keys", "Primary Keys"),
            ("coding_sql_for_keys", "Foreign Keys"),
            ("coding_sql_constraints", "Constraints"),
            ("coding_sql_norm", "Normalization"),
            ("coding_sql_indexes", "Indexes"),
            ("coding_sql_views", "Views"),
            ("coding_sql_stored_proc", "Stored Procedures"),
            ("coding_sql_triggers", "Triggers"),
            ("coding_sql_er_diag", "ER Diagrams"),
            ("coding_sql_trans", "Transactions"),
            ("coding_sql_acid", "ACID Properties")
        ]),
        ("Object-Oriented Programming", [
            ("coding_oop_fund", "OOP Fundamentals"),
            ("coding_oop_class_obj", "Classes and Objects"),
            ("coding_oop_encap", "Encapsulation"),
            ("coding_oop_inherit", "Inheritance"),
            ("coding_oop_poly", "Polymorphism"),
            ("coding_oop_abstract", "Abstraction"),
            ("coding_oop_construct", "Constructors"),
            ("coding_oop_destruct", "Destructors"),
            ("coding_oop_fn_overload", "Function Overloading"),
            ("coding_oop_fn_override", "Function Overriding"),
            ("coding_oop_virtual_fn", "Virtual Functions"),
            ("coding_oop_access_mod", "Access Modifiers"),
            ("coding_oop_static", "Static Members"),
            ("coding_oop_except", "Exception Handling")
        ]),
        ("Technical Interview Preparation", [
            ("coding_ti_c", "C Interview Questions"),
            ("coding_ti_cpp", "C++ Interview Questions"),
            ("coding_ti_py", "Python Interview Questions"),
            ("coding_ti_java", "Java Interview Questions"),
            ("coding_ti_js", "JavaScript Interview Questions"),
            ("coding_ti_oop", "OOP Interview Questions"),
            ("coding_ti_dbms", "DBMS Interview Questions"),
            ("coding_ti_sql", "SQL Interview Questions"),
            ("coding_ti_dsa", "Data Structures Interview Questions"),
            ("coding_ti_algo", "Algorithms Interview Questions"),
            ("coding_ti_os", "Operating Systems"),
            ("coding_ti_cn", "Computer Networks"),
            ("coding_ti_se", "Software Engineering"),
            ("coding_ti_html", "HTML"),
            ("coding_ti_css", "CSS"),
            ("coding_ti_react", "React.js"),
            ("coding_ti_node", "Node.js"),
            ("coding_ti_express", "Express.js"),
            ("coding_ti_mern", "MERN Stack"),
            ("coding_ti_git", "Git and GitHub")
        ]),
        ("Special Python Topics", [
            ("coding_py_data_handling", "Python and Data Handling"),
            ("coding_py_charts", "Python Charts"),
            ("coding_py_stats_math", "Python Statistical and Mathematical Operations")
        ])
    ]

    for grp_name, t_list in coding_groups:
        for tid, title in t_list:
            if tid in ("coding_py_data_handling", "coding_py_stats_math"):
                req = 200
                diff = {"Hard": 150, "Easy": 30, "Medium": 20}
            else:
                req = 100
                diff = {"Hard": 75, "Easy": 15, "Medium": 10}
            topics.append({
                "id": tid,
                "title": title,
                "category": "Coding Questions",
                "group": grp_name,
                "required": req,
                "diff": diff
            })

    # 2. QUANTITATIVE APTITUDE (74 topics)
    quant_groups = [
        ("Number and Arithmetic", [
            ("quant_num_sys", "Number System"),
            ("quant_hcf_lcm", "HCF and LCM"),
            ("quant_dec_frac", "Decimal Fractions"),
            ("quant_simpl", "Simplification"),
            ("quant_sq_root", "Square Roots"),
            ("quant_cube_root", "Cube Roots"),
            ("quant_avg", "Average"),
            ("quant_prob_num", "Problems on Numbers"),
            ("quant_prob_ages", "Problems on Ages"),
            ("quant_sets", "Sets"),
            ("quant_quad_eq", "Quadratic Equations"),
            ("quant_log", "Logarithms"),
            ("quant_index_num", "Index Numbers"),
            ("quant_races_games", "Races and Games")
        ]),
        ("Percentage and Commercial Mathematics", [
            ("quant_pct", "Percentage"),
            ("quant_prof_loss", "Profit and Loss"),
            ("quant_disc", "Discount"),
            ("quant_ratio_prop", "Ratio and Proportion"),
            ("quant_partner", "Partnership"),
            ("quant_chain_rule", "Chain Rule"),
            ("quant_si", "Simple Interest"),
            ("quant_ci", "Compound Interest"),
            ("quant_true_disc", "True Discount"),
            ("quant_bank_disc", "Banker's Discount"),
            ("quant_stocks", "Stocks and Shares"),
            ("quant_alligation", "Alligation and Mixtures")
        ]),
        ("Time-Based Problems", [
            ("quant_time_work", "Time and Work"),
            ("quant_pipes_cist", "Pipes and Cisterns"),
            ("quant_time_dist", "Time and Distance"),
            ("quant_boats_str", "Boats and Streams"),
            ("quant_trains", "Problems on Trains"),
            ("quant_work_wages", "Work and Wages"),
            ("quant_races_time", "Races"),
            ("quant_clocks", "Clocks"),
            ("quant_calendars", "Calendars")
        ]),
        ("Geometry and Mensuration", [
            ("quant_area", "Area"),
            ("quant_perimeter", "Perimeter"),
            ("quant_volume", "Volume"),
            ("quant_surf_area", "Surface Area"),
            ("quant_plane_geom", "Plane Geometry"),
            ("quant_solid_geom", "Solid Geometry"),
            ("quant_height_dist", "Height and Distance"),
            ("quant_trig_fund", "Trigonometry Fundamentals")
        ]),
        ("Probability and Combinatorics", [
            ("quant_permutation", "Permutation"),
            ("quant_combination", "Combination"),
            ("quant_prob", "Probability"),
            ("quant_count_princ", "Basic Counting Principles"),
            ("quant_adv_count", "Advanced Counting Problems")
        ]),
        ("Logical and Numerical Patterns", [
            ("quant_odd_one", "Odd One Out"),
            ("quant_num_series", "Number Series"),
            ("quant_letter_series", "Letter Series"),
            ("quant_miss_num", "Missing Numbers"),
            ("quant_math_ops", "Mathematical Operations"),
            ("quant_num_puzzles", "Number Puzzles"),
            ("quant_data_suff_num", "Data Sufficiency")
        ]),
        ("Data Interpretation", [
            ("quant_di_fund", "Data Interpretation Fundamentals"),
            ("quant_di_tab", "Tabulation"),
            ("quant_di_bar", "Bar Graphs"),
            ("quant_di_pie", "Pie Charts"),
            ("quant_di_line", "Line Graphs"),
            ("quant_di_tables", "Tables"),
            ("quant_di_mixed", "Mixed Graphs"),
            ("quant_di_caselet", "Caselet Data Interpretation"),
            ("quant_di_comp", "Data Comparison"),
            ("quant_di_pct", "Percentage-Based Data Interpretation")
        ]),
        ("Additional Placement Aptitude Topics", [
            ("quant_surds_indices", "Surds and Indices"),
            ("quant_div_rules", "Divisibility Rules"),
            ("quant_remainders", "Remainders"),
            ("quant_factors_mult", "Factors and Multiples"),
            ("quant_approx", "Approximation"),
            ("quant_algebra", "Algebra"),
            ("quant_inequalities", "Inequalities"),
            ("quant_coord_geom", "Coordinate Geometry"),
            ("quant_di_prob", "Probability-Based Data Interpretation")
        ])
    ]

    for grp_name, t_list in quant_groups:
        for tid, title in t_list:
            topics.append({
                "id": tid,
                "title": title,
                "category": "Quantitative Aptitude",
                "group": grp_name,
                "required": 100,
                "diff": {"Hard": 75, "Easy": 15, "Medium": 10}
            })

    # 3. VERBAL ABILITY AND LOGICAL REASONING (87 topics)
    verbal_groups = [
        ("Verbal - Grammar", [
            ("verbal_parts_speech", "Parts of Speech"),
            ("verbal_nouns", "Nouns"),
            ("verbal_pronouns", "Pronouns"),
            ("verbal_verbs", "Verbs"),
            ("verbal_adjectives", "Adjectives"),
            ("verbal_adverbs", "Adverbs"),
            ("verbal_prepositions", "Prepositions"),
            ("verbal_conjunctions", "Conjunctions"),
            ("verbal_articles", "Articles"),
            ("verbal_tenses", "Tenses"),
            ("verbal_subj_verb", "Subject-Verb Agreement"),
            ("verbal_sing_plural", "Singular and Plural"),
            ("verbal_deg_comp", "Degrees of Comparison"),
            ("verbal_pos_deg", "Positive Degree"),
            ("verbal_comp_deg", "Comparative Degree"),
            ("verbal_super_deg", "Superlative Degree"),
            ("verbal_dir_speech", "Direct Speech"),
            ("verbal_indir_speech", "Indirect Speech"),
            ("verbal_act_voice", "Active Voice"),
            ("verbal_pass_voice", "Passive Voice"),
            ("verbal_cond_sent", "Conditional Sentences"),
            ("verbal_q_tags", "Question Tags"),
            ("verbal_sent_corr", "Sentence Correction"),
            ("verbal_err_spot", "Error Spotting"),
            ("verbal_sent_imp", "Sentence Improvement")
        ]),
        ("Verbal - Vocabulary", [
            ("verbal_synonyms", "Synonyms"),
            ("verbal_antonyms", "Antonyms"),
            ("verbal_one_word", "One-Word Substitution"),
            ("verbal_idioms", "Idioms and Phrases"),
            ("verbal_phrasal_verbs", "Phrasal Verbs"),
            ("verbal_prefixes", "Prefixes"),
            ("verbal_suffixes", "Suffixes"),
            ("verbal_compound_words", "Compound Words"),
            ("verbal_homophones", "Homophones"),
            ("verbal_homonyms", "Homonyms"),
            ("verbal_confused_words", "Commonly Confused Words"),
            ("verbal_word_usage", "Word Usage")
        ]),
        ("Verbal - Reading and Writing Skills", [
            ("verbal_rc", "Reading Comprehension"),
            ("verbal_para_jumbles", "Para Jumbles"),
            ("verbal_sent_rearr", "Sentence Rearrangement"),
            ("verbal_sent_comp", "Sentence Completion"),
            ("verbal_fill_blanks", "Fill in the Blanks"),
            ("verbal_cloze_tests", "Cloze Tests"),
            ("verbal_para_comp", "Paragraph Completion"),
            ("verbal_para_summary", "Paragraph Summary"),
            ("verbal_crit_reason", "Critical Reasoning"),
            ("verbal_analogies", "Verbal Analogies")
        ]),
        ("Logical Reasoning", [
            ("logical_fund", "Logical Reasoning Fundamentals"),
            ("logical_blood_rel", "Blood Relations"),
            ("logical_fam_tree", "Family Tree Problems"),
            ("logical_dir_sense", "Direction Sense"),
            ("logical_seat_arr", "Seating Arrangements"),
            ("logical_lin_arr", "Linear Arrangements"),
            ("logical_circ_arr", "Circular Arrangements"),
            ("logical_grp_q", "Group-Based Questions"),
            ("logical_sel_prob", "Selection Problems"),
            ("logical_rank_order", "Ranking and Ordering"),
            ("logical_code_decode", "Coding-Decoding"),
            ("logical_num_code", "Number Coding"),
            ("logical_letter_code", "Letter Coding"),
            ("logical_sym_code", "Symbol Coding"),
            ("logical_analogy", "Analogy"),
            ("logical_classif", "Classification"),
            ("logical_odd_one", "Odd One Out"),
            ("logical_num_series", "Number Series"),
            ("logical_letter_series", "Letter Series"),
            ("logical_alphanumeric", "Alphanumeric Series"),
            ("logical_miss_num", "Missing Numbers"),
            ("logical_syllogisms", "Syllogisms"),
            ("logical_venn", "Venn Diagrams"),
            ("logical_stmt_concl", "Statement and Conclusion"),
            ("logical_stmt_assump", "Statement and Assumption"),
            ("logical_stmt_arg", "Statement and Argument"),
            ("logical_cause_effect", "Cause and Effect"),
            ("logical_assert_reason", "Assertion and Reason"),
            ("logical_data_suff", "Data Sufficiency"),
            ("logical_puzzles", "Puzzles"),
            ("logical_cal_reason", "Calendar-Based Reasoning"),
            ("logical_clock_reason", "Clock-Based Reasoning"),
            ("logical_non_verbal", "Non-Verbal Reasoning"),
            ("logical_mirror_img", "Mirror Images"),
            ("logical_water_img", "Water Images"),
            ("logical_paper_fold", "Paper Folding"),
            ("logical_paper_cut", "Paper Cutting"),
            ("logical_fig_comp", "Figure Completion"),
            ("logical_embed_fig", "Embedded Figures"),
            ("logical_pat_recog", "Pattern Recognition")
        ])
    ]

    for grp_name, t_list in verbal_groups:
        for tid, title in t_list:
            topics.append({
                "id": tid,
                "title": title,
                "category": "Verbal Ability and Logical Reasoning",
                "group": grp_name,
                "required": 100,
                "diff": {"Hard": 75, "Easy": 15, "Medium": 10}
            })

    return topics

if __name__ == "__main__":
    t_list = create_catalog()
    total_q = sum(t["required"] for t in t_list)
    print(f"Total topics created: {len(t_list)}")
    print(f"Total required questions: {total_q}")
    
    # Save to catalog.json
    with open("f:/placement/1round ready2/topic_catalog.json", "w", encoding="utf-8") as f:
        json.dump(t_list, f, indent=2)
    print("Saved topic_catalog.json successfully.")
