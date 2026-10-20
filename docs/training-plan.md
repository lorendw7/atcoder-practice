# Training toward a full ABC solve

## Objective and baseline

Solve every A-G task independently within the contest duration across unfamiliar ABCs. Start with a 12-week training cycle, then reassess; this is not a 12-week full-solve guarantee. Budget approximately 7-9 hours per week.

Baseline on 2026-10-20: returning after a long break; independently implemented ABC081B with a correct simulation. Historical rating is not treated as a current skill assessment. Use the first two weeks to diagnose current fluency.

| Stage | Focus | Exit check on unfamiliar contests |
| --- | --- | --- |
| Weeks 1-2: rebuild | Simulation, enumeration, strings, sorting, sets/maps, complexity | Independently finish A-C in at least 4 of 5 timed attempts |
| Weeks 3-6: D | Prefix sums, binary search, two pointers, greedy reasoning, DFS/BFS | Finish A-D within the contest time in at least 3 of 5 attempts |
| Weeks 7-12: E | Basic DP, DSU, shortest paths, heaps, elementary number theory | Improve D consistency and independently solve selected E tasks |
| Later cycles: F/G | Trees/graphs, advanced DP, Fenwick/segment trees, combinatorics, proof and speed | Solve individual F/G tasks independently, then work toward timed full solves |

Letters vary in difficulty. Repeat or shorten a stage based on evidence, not the calendar. Rating checkpoints are 400, 800, 1200, 1600, and 2000; they are not guaranteed mappings from solved task counts.

## Weekly routine

- Three 60-minute topic sessions: learn one small idea, then solve one or two relevant tasks.
- One 60-minute mixed session: hide topic labels and identify the technique independently.
- One 100-minute unfamiliar contest or virtual contest without help.
- One 90-minute upsolving session focused on the nearest missed task.
- One 30-minute spaced review; rest with the remaining time.

Before coding, write the algorithm, why it works, and its complexity. For basic tasks, try independently for 15-20 minutes; for stretch tasks, 30-45 minutes. Continue if making progress. Otherwise request one hint rather than a full implementation. Reimplement assisted tasks after 2-3 days and solve a related unfamiliar task.

Track assistance as **independent / hint / editorial**. Distinguish local sample success from the official submission verdict.

## First week

| Day | Task |
| --- | --- |
| 1 | Submit ABC081B; solve [ABC083B](https://atcoder.jp/contests/abc083/tasks/abc083_b) |
| 2 | [ABC087B](https://atcoder.jp/contests/abc087/tasks/abc087_b); bound the iteration count |
| 3 | [ABC088B](https://atcoder.jp/contests/abc088/tasks/abc088_b) and [ABC085B](https://atcoder.jp/contests/abc085/tasks/abc085_b) |
| 4 | [ABC085C](https://atcoder.jp/contests/abc085/tasks/abc085_c); explain why it fits the time limit |
| 5 | [Traveling](https://atcoder.jp/contests/abs/tasks/arc089_a); derive conditions before coding |
| 6 | An unseen old ABC, 100 minutes, no hints |
| 7 | Upsolve one missed task and rewrite one previously assisted task |

Replace tasks whose solutions you remember. Do not read or generate future solutions before attempting them. Review the log every two weeks and choose the next tasks from actual bottlenecks.
