#from typing import List
# Given a wooden stick of length n units. The stick is labelled from 0 to n. For example, a 
# stick of length 6 is labelled as follows:


# Given an integer array cuts where cuts[i] denotes a position you should perform a cut at.

# You should perform the cuts in order, you can change the order of the cuts as you wish.

# The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of all 
# cuts. When you cut a stick, it will be split into two smaller sticks (i.e. the sum of their lengths 
# is the length of the stick before the cut). Please refer to the first example for a better explanation.

# Return the minimum total cost of the cuts.

# https://leetcode.com/problems/minimum-cost-to-cut-a-stick/description/

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(n)
        cuts.insert(0, 0)
        cuts.sort()
        dp = [[-1 for _ in range(len(cuts))] for _ in range(len(cuts))]

        def f(i, j):
            #f(i, j) returns min cost to cut stick between i and j:
            if (j - i) <= 1:
                return 0
            
         #   print(i, j)
            if dp[i][j] != -1:
                return dp[i][j]

            res = int(1e9)
            for index in range(i + 1, j):
                res = min(res, f(i, index) + f(index, j))

            dp[i][j] = res + cuts[j] - cuts[i]
            return dp[i][j]

        
        return f(0, len(cuts) - 1)