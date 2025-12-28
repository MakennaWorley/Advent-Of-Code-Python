## 2024 Advent Of Code Overview

This was my first year of Advent of Code but I got to solving every puzzle. For some of the harder
problems, I referenced community discussions or solution outlines to understand more advanced techniques.

---

### Brute Force
Exhaustively enumerate all possibilities where inputs are small and pruning is unnecessary.

Days: 2, 7, 8, 14, 18

Techniques:
- Recursive operator enumeration
- Full time-step simulation
- Re-running BFS after incremental changes
- Triple nested loops (triangle enumeration)

Why used: Problem constraints make exhaustive search feasible and simpler than over-optimizing.

---

### Heuristic / Guided Brute Force
Search-based solutions that reduce the brute-force space using heuristics, pruning, or randomness.

Days: 17 and 23

Techniques:
- Incremental search guided by partial matches
- Randomized greedy clique construction
- Early termination based on heuristics

Why used: Theoretical optimal solutions are complex; heuristic search converges quickly in practice.

---

### Graph Search / Shortest Path
Explicit graph traversal using BFS, Dijkstra, or augmented state graphs.

Days: 4, 12, 16, 20, 21

Techniques:
- BFS / multi-source BFS
- Dijkstra with state expansion
- Reverse shortest-path distance pruning
- Flood fill / connected components

Why used: Problems naturally model movement, connectivity, or cost minimization.

---

### Dynamic Programming / Memoization
Avoid recomputation by caching overlapping subproblems.

Days: 10, 11, 19

Techniques:
- Memoized recursion
- State-based caching
- DP tables with constrained dimensions

Why used: Naive recursion would be exponential without memoization.

---

### Simulation / State Machines
Deterministic simulations where state evolves step-by-step.

Days: 6, 15, 24

Techniques:
- Rule-driven execution
- Grid and memory simulations
- Circuit evaluation
- VM emulation

Why used: The problem statements explicitly define mechanical systems.

---

### Greedy Algorithms
Make locally optimal decisions that lead to correct global results.

Days: 5, 9, 25

Techniques:
- Topological ordering
- Greedy relocation
- Dependency resolution

Why used: Ordering constraints allow deterministic greedy solutions.

---

### Parsing / Pattern Matching

Extract structured meaning from raw text inputs.

Days: 1 and 3

Techniques:
- Regex parsing
- Token scanning
- Structured input decoding

Why used:
For these problems, the primary challenge was transforming raw, irregular input into a usable structured representation.
Regex and token-based parsing allowed the solutions to cleanly separate input interpretation from the core logic, making
the downstream algorithms simpler, safer, and easier to reason about.

---

#### Math / Bitwise Reasoning
Closed-form or algebraic solutions replacing iteration.

Days: 13 and 22

Techniques:
- Linear algebra / determinants
- Bitwise arithmetic
- Modular arithmetic

Why used:
In these problems, direct simulation or dynamic programming would be infeasible due to extremely large input values or
iteration counts. Mathematical reasoning and bitwise operations allow the solution to collapse large iterative processes
into constant-time or logarithmic computations, dramatically improving performance and numerical stability.