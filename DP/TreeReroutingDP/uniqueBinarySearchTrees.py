# ### UNIQUE BINARY SEARCH TREES

# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

# https://leetcode.com/problems/unique-binary-search-trees/description/?envType=problem-list-v2&envId=50vlu3z5&

from functools import lru_cache
class Solution:
    def numTrees(self, n: int) -> int:

        # to make all bst, can put all numbers 1..n as root
        # for ith root, (1 .. (i - 1)) will be left child and ((i + 1) .. n) will be right child and so on
        #so f(i, j) -> gives num of bsts possible for range i..j
        # but we dont need actual range, the nums dont matter so just knowing number of nodes will suffice => f(i)

        dp = [-1] * (n + 1)

        def f(i):
           # print(i)
            if i == 1 or i == 0:
                return 1
            
            if dp[i] != -1: return dp[i]

            trees = 0
            for j in range(1, i + 1):
                trees += (f(j - 1) * f(i - j))
            
            dp[i] = trees
            return dp[i]
        
        return f(n)
                
