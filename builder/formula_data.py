# builder/formula_data.py

FORMULA_ENTRIES = [
    {
        "category": "Quantitative Aptitude",
        "topic": "Percentage",
        "title": "Successive Percentage Changes",
        "latex": "\\text{Net \\% Change} = a + b + \\frac{a \\times b}{100}",
        "vars": "a = first % change (+ for increase, - for decrease), b = second % change.",
        "usage": "Use when a value is sequentially modified by two percentages, such as consecutive discounts, inflation, or multi-dimensional changes in area.",
        "traps": "Always apply negative signs for discounts or reductions. Two discounts of 20% and 10% give a net of -20 - 10 + 2 = -28%, not -30%.",
        "example": "If length increases by 25% and breadth decreases by 20%: Net Change = 25 - 20 + (25 * -20)/100 = 5 - 5 = 0% (Area remains unchanged)."
    },
    {
        "category": "Quantitative Aptitude",
        "topic": "Percentage",
        "title": "Constant Expenditure Invariant",
        "latex": "\\text{Required Consumption Reduction} = \\frac{R}{100 + R} \\times 100\\%",
        "vars": "R = percentage increase in price.",
        "usage": "When the price of an essential commodity rises by R% and the family wishes to keep overall expenditure constant.",
        "traps": "Do not decrease consumption by R%. Since the base cost is higher, the needed fraction is always R/(100 + R).",
        "example": "If fuel price rises by 25%: Reduction = (25 / 125) * 100% = 20% reduction in consumption."
    },
    {
        "category": "Quantitative Aptitude",
        "topic": "Profit and Loss",
        "title": "Selling Price from Cost Price and Profit",
        "latex": "\\text{SP} = \\text{CP} \\times \\left(1 + \\frac{P}{100}\\right), \\quad \\text{Profit \\%} = \\frac{\\text{SP} - \\text{CP}}{\\text{CP}} \\times 100",
        "vars": "SP = Selling Price, CP = Cost Price, P = Profit percentage.",
        "usage": "Primary commercial calculation for determining revenues and profit margins.",
        "traps": "Unless stated otherwise, Profit % is strictly calculated on Cost Price (CP), not Selling Price (SP).",
        "example": "CP = Rs. 500, Profit = 16%: SP = 500 * (1 + 0.16) = Rs. 580."
    },
    {
        "category": "Quantitative Aptitude",
        "topic": "Profit and Loss",
        "title": "Dishonest Dealer Weight Fraud",
        "latex": "\\text{Gain \\%} = \\frac{\\text{True Weight} - \\text{False Weight}}{\\text{False Weight}} \\times 100\\%",
        "vars": "True Weight = standard nominal weight, False Weight = actual weight dispensed to customer.",
        "usage": "Use when a trader claims to sell goods at cost price but uses underweight measuring balances.",
        "traps": "The denominator MUST be the False Weight (the trader's actual cost base), not the True Weight.",
        "example": "If a shopkeeper uses a 900g weight instead of 1 kg: Gain % = ((1000 - 900) / 900) * 100% = 100/9 = 11.11% gain."
    },
    {
        "category": "Quantitative Aptitude",
        "topic": "Number System",
        "title": "HCF and LCM Product Duality",
        "latex": "A \\times B = \\text{HCF}(A, B) \\times \\text{LCM}(A, B)",
        "vars": "A, B = two positive integers, HCF = Greatest Common Divisor, LCM = Least Common Multiple.",
        "usage": "Rapidly finding the 4th term when any three of A, B, HCF, LCM are known.",
        "traps": "This product theorem strictly holds ONLY for TWO numbers. For three numbers A, B, C: A*B*C != HCF*LCM.",
        "example": "If HCF = 15, LCM = 180, and A = 45: B = (15 * 180) / 45 = 60."
    },
    {
        "category": "Quantitative Aptitude",
        "topic": "Time and Work",
        "title": "Reciprocal Parallel Work Rates",
        "latex": "\\frac{1}{T_{\\text{together}}} = \\frac{1}{A} + \\frac{1}{B} \\implies T = \\frac{A \\times B}{A + B}",
        "vars": "A = days taken by A alone, B = days taken by B alone, T = combined days together.",
        "usage": "Solving multi-worker efficiency problems and pipe cistern filling questions.",
        "traps": "Days never add directly; work rates add reciprocally.",
        "example": "A takes 10 days, B takes 15 days: T = (10 * 15) / (10 + 15) = 150 / 25 = 6 days."
    },
    {
        "category": "Quantitative Aptitude",
        "topic": "Time and Distance",
        "title": "Harmonic Average Speed over Equal Distances",
        "latex": "\\text{Average Speed} = \\frac{2xy}{x + y}",
        "vars": "x = speed on outward journey, y = speed on return journey over the exact same distance.",
        "usage": "Round trips or two journeys spanning equal geographic distances at different speeds.",
        "traps": "Average speed is NOT (x + y)/2. Because more time is spent at the lower speed, it is a harmonic mean.",
        "example": "Go at 60 km/h, return at 40 km/h: Avg Speed = 2(60)(40)/(60 + 40) = 4800 / 100 = 48 km/h."
    },
    {
        "category": "Quantitative Aptitude",
        "topic": "Simple & Compound Interest",
        "title": "Compound Interest and Difference from SI",
        "latex": "A = P\\left(1 + \\frac{R}{100}\\right)^n, \\quad \\text{Diff}_{2\\text{ yrs}} = P\\left(\\frac{R}{100}\\right)^2",
        "vars": "P = Principal, R = Annual rate %, n = years, Diff = Difference between CI and SI for 2 years.",
        "usage": "Rapidly solving placement interview questions comparing compound interest to simple interest.",
        "traps": "When compounding half-yearly, double n (n -> 2n) and halve the rate (R -> R/2).",
        "example": "If Difference between CI and SI for 2 years at 10% is Rs. 50: 50 = P * (10/100)^2 = P * 0.01 => P = Rs. 5,000."
    },
    {
        "category": "Quantitative Aptitude",
        "topic": "Alligation and Mixtures",
        "title": "Rule of Alligation Ratio",
        "latex": "\\frac{\\text{Quantity of Cheaper}}{\\text{Quantity of Dearer}} = \\frac{D - M}{M - C}",
        "vars": "C = price of cheaper item, D = price of dearer item, M = mean target price.",
        "usage": "Determines mixing ratio to produce a desired blended cost.",
        "traps": "All three units (C, D, M) must represent identical base costs (e.g. all CP per kg, never mix SP with CP).",
        "example": "Mix tea at Rs. 20/kg with tea at Rs. 30/kg to get Rs. 26/kg: Ratio = (30 - 26) / (26 - 20) = 4 / 6 = 2 : 3."
    },
    {
        "category": "Quantitative Aptitude",
        "topic": "Permutation & Combination",
        "title": "Combinations and Permutations",
        "latex": "P(n, r) = \\frac{n!}{(n - r)!}, \\quad \\binom{n}{r} = \\frac{n!}{r!(n - r)!}, \\quad \\binom{n}{r} = \\binom{n}{n - r}",
        "vars": "n = total items available, r = chosen subset.",
        "usage": "Selection (combination) vs ranking/arrangement (permutation).",
        "traps": "Remember 0! = 1. If arrangements around a circle are considered with no fixed reference, circular permutations = (n - 1)!.",
        "example": "Pick 3 students from 8: 8C3 = (8 * 7 * 6) / (3 * 2 * 1) = 56 ways."
    },
    {
        "category": "Coding & Algorithms",
        "topic": "Binary Search",
        "title": "Safe Midpoint Calculation",
        "latex": "\\text{mid} = \\text{low} + \\left\\lfloor \\frac{\\text{high} - \\text{low}}{2} \\right\\rfloor, \\quad T(n) = O(\\log_2 n)",
        "vars": "low = left index pointer, high = right index pointer.",
        "usage": "Guarantees 32-bit signed integer overflow will never occur during binary search in C, C++, and Java.",
        "traps": "(low + high)/2 overflows when low + high >= 2^31 - 1, producing a negative number and index out-of-bounds.",
        "example": "low = 2,000,000,000; high = 2,100,000,000: Safe mid = 2,000,000,000 + (100,000,000)/2 = 2,050,000,000."
    },
    {
        "category": "Coding & Algorithms",
        "topic": "Divide and Conquer",
        "title": "Master Theorem for Algorithmic Recurrences",
        "latex": "T(n) = a T(n/b) + \\Theta(n^k \\log^p n)",
        "vars": "a = subproblems count (>=1), b = problem shrink factor (>1), k, p = driving work exponents.",
        "usage": "Determines asymptotic time complexity of recursive algorithms like Merge Sort, Karatsuba, Strassen.",
        "traps": "Check if a < b^k (Case 3), a = b^k (Case 2), or a > b^k (Case 1).",
        "example": "Merge Sort: a=2, b=2, k=1, p=0 => a = b^k => Case 2 gives Theta(n^1 log n) = O(n log n)."
    },
    {
        "category": "Coding & Statistics",
        "topic": "Python & Data Science",
        "title": "Sample Variance with Bessel's Correction",
        "latex": "s^2 = \\frac{1}{n - 1} \\sum_{i=1}^n (x_i - \\bar{x})^2, \\quad s = \\sqrt{s^2}",
        "vars": "x_i = sample values, \\bar{x} = sample arithmetic mean, n = sample size.",
        "usage": "Unbiased estimation of population variance from a sample in pandas and numpy (`ddof=1`).",
        "traps": "Default in numpy.var() is ddof=0 (population variance), while pandas.Series.var() defaults to ddof=1 (sample variance).",
        "example": "Values = [2, 4, 6], mean = 4. Squared deviations: 4, 0, 4 (sum=8). Sample variance s^2 = 8 / (3 - 1) = 4. s = 2."
    },
    {
        "category": "Coding & Statistics",
        "topic": "Python & Data Science",
        "title": "Interquartile Range and Outlier Detection",
        "latex": "\\text{IQR} = Q_3 - Q_1, \\quad \\text{Outliers} < Q_1 - 1.5\\times\\text{IQR} \\;\\text{ or }\\; > Q_3 + 1.5\\times\\text{IQR}",
        "vars": "Q_1 = 25th percentile, Q_3 = 75th percentile, IQR = Interquartile Range.",
        "usage": "Standard statistical rule used in Matplotlib boxplots and data cleaning pipelines to filter anomalies.",
        "traps": "Extreme outliers (far points) are sometimes classified using 3.0 * IQR instead of 1.5 * IQR.",
        "example": "Q1 = 20, Q3 = 40 => IQR = 20. Lower fence = 20 - 1.5(20) = -10. Upper fence = 40 + 1.5(20) = 70. Any point > 70 is an outlier."
    }
]
