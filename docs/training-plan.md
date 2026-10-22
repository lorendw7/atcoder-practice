# Training plan: AtCoder blue (rating 1600)

## Target and evidence

AtCoder blue is algorithm rating **1600-1999**. The target is not a fixed number of solved problem letters: task difficulty and required speed vary by contest. The official color boundary is documented by [AtCoder](https://info.atcoder.jp/overview/contest/rating).

The primary success condition is an actual rating of at least 1600. Before enough rated contests have accumulated, use these training proxies over a rolling five unfamiliar ABCs:

- finish A-C independently in 25 minutes or less in at least 4 of 5 contests;
- finish D independently in 50 minutes or less in at least 4 of 5 contests;
- solve E independently in at least 3 of 5 contests, or obtain comparable performance on a harder D/F mix;
- keep wrong submissions caused by implementation errors to at most one per contest on average;
- reach a median contest performance near or above 1600.

These are diagnostic targets, not a claim that A-E always equals blue performance.

## Baseline: 2026-10-23

The current record contains six official accepted tasks: ABC083B, ABC087B, ABC088B/C/D, and Educational DP A, plus a locally verified ABC081B. Most accepted tasks used clarification, hints, or guided explanations. This demonstrates early familiarity with enumeration, greedy sorting, an invariant check, BFS, and one-dimensional DP, but it does not yet demonstrate independent timed consistency.

Current priorities are therefore:

1. convert guided solutions into independent recall;
2. make A-C implementation fast and reliable;
3. build D-level breadth before specializing in E-level topics;
4. start unfamiliar timed contests immediately so progress is measured honestly.

No fixed date is promised for blue. Spend about **8-10 focused hours per week**, advance only after meeting each phase gate, and reassess every four weeks.

## Phase roadmap

| Phase | Typical duration | Main work | Exit gate on unfamiliar problems |
| --- | ---: | --- | --- |
| 0. Independence reset | 2-4 weeks | C++ fluency, simulation, enumeration, sorting, sets/maps, prefix sums; independent rewrites of guided work | A-C within 35 minutes in 4 of 5 virtual ABCs; independently reproduce DP A and ABC088D |
| 1. Stable D / green | 4-8 weeks | Binary search, two pointers, greedy proof, DFS/BFS, basic DP, coordinate compression | A-C within 25 minutes and D solved in 3 of 5 unfamiliar ABCs |
| 2. E entry / cyan | 6-10 weeks | Knapsack and counting DP, DSU, Dijkstra, trees, topological sort, number theory, modular arithmetic | D solved in 4 of 5; at least 10 independent solves around difficulty 1000-1400; occasional E within contest time |
| 3. Blue conversion | 8-16+ weeks | Fenwick/segment trees, stronger graph and DP modeling, combinatorics, mixed 1200-1800 practice | Meet the rolling-five contest proxies above and sustain performance around 1600 |

AtCoder Problems difficulty, when available, is a better training selector than the A-E letter. Difficulty ranges here are approximate; avoid memorized tasks and replace any problem whose solution is already known.

## Topic order

Do not study every technique before competing. Learn one small idea, solve a focused pair, then mix it with older topics.

1. **Implementation foundations:** complexity, integer bounds, STL containers, sorting, prefix sums, binary search, two pointers.
2. **Dynamic programming:** state meaning, transitions, initialization, dependency order; sequence, grid, 0/1 knapsack, unbounded knapsack, and counting.
3. **Graphs:** BFS/DFS, connected components, DSU, Dijkstra, trees, and topological ordering.
4. **Mathematics:** GCD, divisors, prime factorization, modular arithmetic, counting, and combinations.
5. **Range queries:** coordinate compression, Fenwick trees, segment trees, and offline query techniques.
6. **Blue-level integration:** choose the technique from constraints, combine two ideas, prove correctness, and implement under time pressure.

For each new technique, require three forms of evidence:

- explain the state/invariant and why the transition or operation is valid;
- implement one example with guidance if necessary;
- two or three days later, reimplement it and solve one related unfamiliar problem without help.

## Weekly cycle

| Session | Time | Work |
| --- | ---: | --- |
| Live or virtual ABC | 100 min | No hints, editorials, AI, or solution search; record split times and wrong submissions |
| Contest upsolve | 90 min | Solve the first missed task; request only the smallest useful hint after a genuine attempt |
| Topic session A | 60 min | Learn one technique and solve one focused task |
| Topic session B | 60 min | Solve a second related task independently |
| Topic session C | 60 min | Solve an unfamiliar variation without a topic label |
| Mixed set | 90 min | Three tasks from older topics; practice selecting the method |
| Spaced review | 45 min | Reimplement one assisted task and update the error log |
| Optional reading | 30-60 min | Editorial comparison only after solving or ending the timed attempt |

Take at least one rest day. More low-quality volume is not a substitute for timed evidence and review.

## Problem-attempt protocol

Before coding, write four short lines: constraints, intended complexity, algorithm, and correctness reason. For a normal task, attempt independently for 25 minutes; for the current stretch task, use 40-45 minutes. Continue while making concrete progress. Otherwise take one hint, mark the task as assisted, and schedule a rewrite.

After every WA/RE/TLE/CE, classify the cause:

- observation/modeling;
- proof gap;
- complexity choice;
- boundary or integer range;
- implementation/API/syntax;
- rushed reading.

An accepted guided solution counts as exposure, not mastery. A task graduates from the review queue only after an independent blank-file reimplementation and a related unfamiliar solve.

## Next two weeks

This sequence starts from the current evidence rather than jumping directly to arbitrary E tasks.

| Session | Task | Purpose and completion condition |
| ---: | --- | --- |
| 1 | Reimplement [DP A - Frog 1](https://atcoder.jp/contests/dp/tasks/dp_a) | Blank file, no reference, explain state/transition, AC within 25 minutes |
| 2 | [DP B - Frog 2](https://atcoder.jp/contests/dp/tasks/dp_b) | Generalize the transition and derive `O(NK)` from constraints |
| 3 | [DP C - Vacation](https://atcoder.jp/contests/dp/tasks/dp_c) | Use a two-dimensional state and explain why only the previous day is needed |
| 4 | Reimplement [ABC088D](https://atcoder.jp/contests/abc088/tasks/abc088_d) | Blank-file BFS; include wide and tall custom grids; AC without help |
| 5 | [ABC085C](https://atcoder.jp/contests/abc085/tasks/abc085_c) and [Traveling](https://atcoder.jp/contests/abs/tasks/arc089_a) | Enumeration bounds and necessary/sufficient conditions |
| 6 | Unfamiliar virtual ABC | Full 100 minutes without help; record A-D split times |
| 7 | Upsolve first missed task | Write cause, solution, proof, complexity, and review date |
| 8 | [DP D - Knapsack 1](https://atcoder.jp/contests/dp/tasks/dp_d) | Derive 0/1 choice and use 64-bit values where required |
| 9 | [DP E - Knapsack 2](https://atcoder.jp/contests/dp/tasks/dp_e) | Change the DP axis based on constraints rather than copying DP D |
| 10 | [ABC153E](https://atcoder.jp/contests/abc153/tasks/abc153_e) | Model reusable choices and overshoot; attempt only after DP D/E |
| 11 | Mixed A-D set | Three unfamiliar tasks, 90 minutes, no topic labels |
| 12 | Live or virtual ABC plus review | Compare against the first contest and choose the next bottleneck |

If DP A or ABC088D cannot yet be reproduced independently, repeat with a related easier task before proceeding. If the virtual contest reveals slower A-C implementation, pause the DP sequence for one week and repair that bottleneck.

## Four-week review

Every four weeks, record:

- current rating and recent performance values;
- five-contest A/B/C/D/E solve rates and median split times;
- independent solves by approximate difficulty band;
- WA/RE/TLE/CE causes;
- overdue assisted-task rewrites;
- the single largest bottleneck for the next cycle.

Advance a phase only from this evidence. Do not advance because the calendar elapsed or because a guided solution received AC.
