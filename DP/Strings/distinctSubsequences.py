# ### DISTINCT SUBSEQUENCES

# Given two strings s and t, return the number of distinct 
# subsequences
#  of s which equals t.

# The test cases are generated so that the answer fits on a 32-bit signed integer.

# https://leetcode.com/problems/distinct-subsequences/description/

# top down approach

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        dp = [[-1 for _ in range(len(t))] for _ in range(len(s))]
        
        def f(i, j):
            # f(i, j) -> number of distinct subsequences of s[i:] equaling t[j:]
            if j == len(t):
                return 1
            if i == len(s):
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            if s[i] == t[j]:
                dp[i][j] = f(i + 1, j + 1) + f(i + 1, j)
            else:
                dp[i][j] =  f(i + 1, j)
            return dp[i][j]

        
        return f(0, 0)
        

# bottom up approach

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]

        for i in range(len(s) + 1):
            dp[i][len(t)] = 1
            
        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]
        
        return dp[0][0]