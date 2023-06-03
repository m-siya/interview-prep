### Resources
- https://leetcode.com/discuss/general-discussion/662866/DP-for-Beginners-Problems-or-Patterns-or-Sample-Solutions
- https://leetcode.com/discuss/general-discussion/458695/Dynamic-Programming-Patterns

### How to go about Solving
1. The order of solving a dp problem should be 1 ) come up with a recurrence relation first 2 ) code it up. The first part only needs a pen and paper.

2. When coming up with a recurrence relation, separately come up with a general case and base cases.
    2.1 when coming up with a general case, assign well defined English meaning to your dp term, dp[...][...][...]... e.g. for https://leetcode.com/problems/longest-increasing-subsequence/, dp[i] = the length of the longest increasing subsequence that ENDS on element i.

    2.2 once you define your meaning, express the answer to the original problem in terms of your dp terms. If you can't do this, then it means your dp definition likely lacks certain necessary information. e.g. for longest increasing subsequence, ans == max(dp[i]) for 0 <= i < n, n == length of an input array (because you don't know where an optimal solution ends)

    2.3 base cases are usually straightforwardly defined if you follow the top-down approach. i.e. the conditions in which your recursive function ends. If your recursive function is stuck in an infinite loop, you are probably missing a base case (though it is possible your general case is messed up and creates a cycle. see my point 4)

3. People usually prefer either the top-down or the bottom-up style. Stick with one or the other and always code in some template. Then, writing code is a matter of translating your recurrence relation. This way, you avoid mistakes.

4. At its core, DP problems are really graph problems. Here each dp[...][...][...] terms are nodes and edges are drawn based on recurrence relations. For your problem to have a DP solution, this graph MUST BE a DAG. This is usually what textbooks mean "optimal substructure". For me, this connection of DP to its graph representation greatly helped.

### Thinking Process
Source - https://leetcode.com/problems/target-sum/solutions/455024/dp-is-easy-5-steps-to-think-through-dp-questions/

1. Category
- 0/1 Knapsack
- Unbounded Knapsack
- Shortest Path (eg: Unique Paths I/II)
- Fibonacci Sequence (eg: House Thief, Jump Game)
- Longest Common Substring/Subsequeunce

Recognize the category to frame a new question into something familiar. 

2. States
what variables to keep track of to reach our optimal result?
Can be mapped to the paramters of the helper function f(), also maps to dimensions of the dp array.

3. Decisons
Making an optimal decision by considering all decisions. Each decision brings us closer to the base case.

4. Base Case
Relate directly to the conditions required by the answer we are seeking.



### start to (i, j) vs (i, j) to destination
    Assuming the problem is a minimum path sum in a matrix.
    1. f(i, j) -> minimum path sum from start to (i, j)
    Intuitively, fits the recursive top down approach. (think, induction - so to get the value of f(dest), find value of f(dest - one step) + some logic)

    Also intuitive for fixed start but different destination problems.

    2. f(i, j) -> minimum path sum from (i, j) to dest


-------------------------------------------------
1. Note - dimensions of dp are the mapping in the helper function, start with finding the mapping of the helper function as the first step


---------------------
### Meet in the Middle

a technique where search space is divided into two parts of equal size. A separate search is performed for both parts and results are combined. 

use if efficient way to combine results of the 2 searches, then time taken < time for 1 large search -> 2^n -> 2^(n/2).  (2^n because at each step, we choose to take or leave an element). (2^n/2 equals root(2^n))

use if you can solce problem for twice smaller k, like divide and conquer but without the step of recursively solving smaller subproblems

Q. given an array of n numbers, how many ways to choose a subset of the numbers of sum x?


