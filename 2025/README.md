## 2025 Advent Of Code Overview

This was my second year of Advent of Code, and I once again finished solving every puzzle
(though not all before Christmas Day). I solved most problems independently, with the main exceptions
being Day 9 Part 2 and Day 10 Part 2, where I referenced external discussions to understand more
advanced techniques. Compared to last year, I relied far less on outside references, aside from occasional AI-assisted
debugging.

### Brute Force
Exhaustively enumerate all possibilities where inputs are small and pruning is unnecessary.

Day: 2

Techniques:
- Full iteration over bounded numeric ranges 
- Nested loops over small input sizes 
- Direct condition checking without optimization

Why used: The input sizes were small enough that brute force was both feasible and simpler than introducing unnecessary
complexity.

---

### Heuristic / Guided Brute Force
Search-based solutions that reduce the brute-force space using heuristics, pruning, or randomness.

Day: 12

Techniques:
- Backtracking search over shape placements 
- Bitmask representation of occupied cells 
- Memoization of (`occupied_mask`, `remaining_counts`) states 
- Minimum-remaining-values (MRV) heuristic to choose the next shape 
- Early pruning when no valid placements remain

Why used: The problem is an exact-cover–style tiling problem with a very large theoretical search space. Applying
heuristics, pruning, and memoization dramatically reduces the number of explored states, making the search tractable.

---

### Graph Search / Shortest Path
Explicit graph traversal using BFS, Dijkstra, or augmented state graphs.

Days: 8, 9, 10

Techniques:
- Union-Find (Disjoint Set Union) for connectivity 
- Flood fill (BFS) on grids 
- BFS over bitmask-based state graphs 
- Coordinate compression to reduce graph size

Why used: These problems naturally model connectivity, reachability, or minimum-step transitions, making graph-based
approaches the most direct and reliable solution.

---

### Dynamic Programming / Memoization
Avoid recomputation by caching overlapping subproblems.

Day: 11

Techniques:
- Recursive depth-first search over a directed graph 
- Memoization with `lru_cache` to cache path counts 
- State augmentation to track additional constraints (visited special nodes)
- Counting paths rather than enumerating them

Why used: The number of distinct paths grows exponentially without caching. Memoization collapses repeated subproblems
into a manageable number of states, making path counting feasible even with additional constraints.

---

### Simulation / State Machines
Deterministic simulations where state evolves step-by-step.

Days: 1, 4, 7

Techniques:
- Step-by-step state updates 
- Grid-based rule application 
- Tracking evolving sets or counts of entities 
- Termination on convergence or exit conditions

Why used: The problems explicitly define mechanical systems whose behavior must be simulated directly over time.

---

### Greedy Algorithms
Make locally optimal decisions that lead to correct global results.

Days: 3 and 5

Techniques:
- Monotonic stack–based greedy selection 
- Interval sorting and merging 
- One-pass local optimization

Why used: Greedy strategies allow efficient solutions once the correct invariant or ordering is identified.

---

### Parsing / Pattern Matching

Extract structured meaning from raw text inputs.

Day: 6

Techniques:
- ASCII grid parsing 
- Column and region detection via whitespace 
- Structured extraction of numbers and operators

Why used: The primary challenge was interpreting a non-standard input format rather than algorithmic complexity.