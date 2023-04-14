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


