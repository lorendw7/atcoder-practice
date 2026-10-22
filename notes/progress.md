# Practice log

| Date | Task | Assistance | Local result | Official verdict | Takeaway |
| --- | --- | --- | --- | --- | --- |
| 2026-10-20 | [ABC081B](https://atcoder.jp/contests/abc081/tasks/abc081_b) | Independent | 3/3 official samples passed locally | Not recorded | Check every element before dividing; count only completed operations. |
| 2026-10-20 | [ABC083B](https://atcoder.jp/contests/abc083/tasks/abc083_b) | Problem statement clarification; learner reported completing the implementation | Not recorded | AC, 200 points; confirmed by the user's AtCoder submission screenshot (12:52:02 JST); submission URL not recorded | Use the digit sum to select an integer, then add the original integer to the answer. |
| 2026-10-20 | [ABC087B](https://atcoder.jp/contests/abc087/tasks/abc087_b) | Editorial-based explanation and reference implementation | Assistant reference passed all 3 official samples and a zero-count edge case; learner solution not tested locally by assistant | AC, 200 points; user supplied a submission screenshot after ABC087B practice (task name obscured by dropdown); submission URL not recorded | Enumerate each coin count from zero through its available count, inclusive, and count triples totaling exactly X. |
| 2026-10-20 | [ABC088B](https://atcoder.jp/contests/abc088/tasks/abc088_b) | Hint: greedy choice confirmed, C++ descending-sort syntax, and turn-indexing prompt | Not recorded | AC, 200 points; confirmed by the user's submission screenshot (13:35:41 JST); submission URL not recorded | Sort in descending order, then alternate cards between Alice and Bob and calculate the score difference. |
| 2026-10-20 | [ABC088C](https://atcoder.jp/contests/abc088/tasks/abc088_c) | Guided derivation of row differences, correctness argument, and implementation outline; learner answered the observation exercise | Not recorded | AC, 300 points; confirmed by the user's submission screenshot (14:06:28 JST); submission URL not recorded | Compare each row with the first row: the difference must be constant across columns. |
| 2026-10-20 | [ABC088D](https://atcoder.jp/contests/abc088/tasks/abc088_d) | Guided shortest-path reduction, BFS core code, and diagnosis of the grid-reading column bound | Learner's final source not separately tested by assistant | AC, 400 points; confirmed by the user's submission screenshot (14:35:40 JST); submission URL not recorded | Preserve shortest-path cells, including the start; iterate columns using the width, and test rectangular grids. |
| 2026-10-23 | [DP A - Frog 1](https://atcoder.jp/contests/dp/tasks/dp_a) | Guided state and transition derivation; full reference implementation requested and provided | Assistant reference passed all 3 official samples and the four-stone lesson exercise | AC, 100 points at 01:28:38 JST after two CE submissions; confirmed by the user's AtCoder screenshot; submission URL not recorded | Compare the total cost to reach a predecessor plus the last jump cost; compute states in dependency order. Diagnose compiler errors locally before resubmitting. |

## Current dashboard

Updated 2026-10-23.

| Metric | Current evidence | Next checkpoint |
| --- | --- | --- |
| Target | Rating 1600 (blue) | Record current rating and each future contest performance |
| Recorded official ACs | 6 | Keep submission URLs for future ACs |
| Independent mastery | ABC081B locally verified; most other tasks used some assistance | Independent blank-file rewrites of DP A and ABC088D |
| Timed unfamiliar ABCs | None recorded | Complete one 100-minute virtual ABC this week |
| Current topic | Basic one-dimensional DP | DP B, DP C, then DP D/E |
| Error signal | Two CE submissions before DP A AC | Compile and run samples locally before every submission |

### Next seven sessions

1. Reimplement DP A from a blank file without the prior code; target 25 minutes.
2. Solve DP B and explain why the complexity is `O(NK)`.
3. Solve DP C using a day/activity state.
4. Reimplement ABC088D independently and test rectangular grids.
5. Solve ABC085C and Traveling without solution lookup.
6. Run one unfamiliar 100-minute virtual ABC with no help.
7. Upsolve the first missed task and record the exact failure category.

## Current guided practice

- The learner requested C- and D-level instruction after ABC088B. ABC088C and ABC088D are now accepted after guided instruction. The learner next requested the knowledge needed for consistent E-level solving and continued lessons.
- C lesson completed: The learner correctly identified constant row differences and how changing one cell breaks them. Guided instruction then connected this condition to a row-plus-column construction and a two-loop implementation outline. Reimplement independently on 2026-10-22.
- D lesson completed with guidance: The learner correctly explained that four moves use five cells, leaving two repaintable cells in a seven-white-cell example. Instruction covered FIFO queues, BFS distance layers, and marking cells when enqueued. The learner assembled a solution; review identified an input loop using the height instead of the width. The subsequent submission was accepted. Reimplement BFS independently on 2026-10-22 and include both wide and tall rectangular tests.
- DP foundation lesson completed with guidance: [Educational DP A - Frog 1](https://atcoder.jp/contests/dp/tasks/dp_a). Define dp[i] as the minimum total cost to reach stone i. The learner correctly computed dp[3] = 10 for heights 10, 30, 20, then dp[4] = 15 after appending height 25. A full reference implementation was requested and provided; the learner later submitted an AC after two CE attempts. Independent reproduction is still pending.
- Planned DP bridge: DP B, DP C, DP D, and DP E, then [ABC153E - Crested Ibis vs Monster](https://atcoder.jp/contests/abc153/tasks/abc153_e). Teach the difference between one-use choices and reusable choices before implementing the E task.
- Teaching reference: [Official ABC088 editorial](https://img.atcoder.jp/abc088/editorial.pdf). Use guided questions before supplying a complete implementation.

## ABC087B review

- Reference: [Official ABC087 / ARC090 editorial, Problem B](https://img.atcoder.jp/arc090/editorial.pdf).
- Approach: Enumerate all triples (i, j, k), where 0 <= i <= A, 0 <= j <= B, and 0 <= k <= C. Count a triple when 500i + 100j + 50k equals X.
- Correctness: Each permitted selection corresponds to exactly one triple. The loops visit every triple once, and the equality check counts exactly the valid selections.
- Time: O((A + 1)(B + 1)(C + 1)), at most 51^3 = 132651 checks. Auxiliary space: O(1).
- Boundary reminder: A denomination may be unused or unavailable, so each loop must start at zero and include its upper bound.
- Submission evidence: On 2026-10-20, the user supplied an AtCoder screenshot showing AC and 200 points after this practice. The task name is obscured by the open dropdown, so the ABC087B association follows the conversation context; the submission URL is not available.
- Follow-up: Reimplement without the reference on 2026-10-22.
- Next task completed: ABC088B; see the practice table for its result and assistance level.

## Review template

- Task / URL:
- Time spent:
- Assistance: independent / hint / editorial
- Algorithm:
- Why it works:
- Time and space complexity:
- Edge cases:
- Mistake or missing observation:
- Local result / official submission URL:
- Review date:
