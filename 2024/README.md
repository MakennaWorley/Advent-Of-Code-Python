### 2024 Advent Of Code Overview

This was my first year of Advent of Code but I got to solving every puzzle. For some of the harder
problems, I referenced community discussions or solution outlines to understand more advanced techniques

#### Brute Force
Exhaustively enumerate all possibilities where inputs are small and pruning is unnecessary.

Days: 7, 14, 18, 23 (part 1)

Techniques:
- Recursive operator enumeration
- Full time-step simulation
- Re-running BFS after incremental changes
- Triple nested loops (triangle enumeration)

Why used: Problem constraints make exhaustive search feasible and simpler than over-optimizing.

#### Heuristic / Guided Brute Force
Search-based solutions that reduce the brute-force space using heuristics, pruning, or randomness.

Days: 17 (part 2) and 23 (part 2)

Techniques:
- Incremental search guided by partial matches
- Randomized greedy clique construction
- Early termination based on heuristics

Why used: Theoretical optimal solutions are complex; heuristic search converges quickly in practice.

#### Graph Search / Shortest Path
Explicit graph traversal using BFS, Dijkstra, or augmented state graphs.

Days: 4, 6, 10, 15, 16, 20, 21

Techniques:
- BFS / multi-source BFS
- Dijkstra with state expansion
- Reverse shortest-path distance pruning
- Flood fill / connected components

Why used: Problems naturally model movement, connectivity, or cost minimization.

#### Dynamic Programming / Memoization
Avoid recomputation by caching overlapping subproblems.

Days: 10 (part 2), 11, 13 (part 1), 19

Techniques:
- Memoized recursion
- State-based caching
- DP tables with constrained dimensions

Why used: Naive recursion would be exponential without memoization.

#### Simulation / State Machines
Deterministic simulations where state evolves step-by-step.

Days: 3, 6, 9, 14, 15, 17 (part 1), 22, 24, 25

Techniques:
- Rule-driven execution
- Grid and memory simulations
- Circuit evaluation
- VM emulation

Why used: The problem statements explicitly define mechanical systems.

#### Greedy Algorithms
Make locally optimal decisions that lead to correct global results.

Days: 5, 9, 15, 25

Techniques:
- Topological ordering
- Greedy relocation
- Dependency resolution

Why used: Ordering constraints allow deterministic greedy solutions.

#### Parsing / Pattern Matching

Extract structured meaning from raw text inputs.

Days: 1, 3, 22, 24

Techniques:
- Regex parsing
- Token scanning
- Structured input decoding

#### Math / Bitwise Reasoning
Closed-form or algebraic solutions replacing iteration.

Days: 13 (part 2), 22, 24

Techniques:
- Linear algebra / determinants
- Bitwise arithmetic
- Modular arithmetic