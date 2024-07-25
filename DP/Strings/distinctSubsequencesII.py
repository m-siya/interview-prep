# ### DISTINCT SUBSEQUENCES II

# Given a string s, return the number of distinct non-empty subsequences of s. Since the answer may be very large, return it modulo 109 + 7.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not.
 
# https://leetcode.com/problems/distinct-subsequences-ii/description/

from functools import lru_cache
MOD = 10**9 + 7
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        
        last_occurrence = {}

        @lru_cache(None)
        def f(i):
            if i == -1:
                return 1
            
            if i in memo:
                return memo[i]
            
            res = (2 * f(i - 1)) % MOD

            char = s[i]

            if char in last_occurrence:
                res = (res - f(last_occurrence[char] - 1)) % MOD
            
            last_occurrence[char] = i
            memo[i] = res
            
            return res
        
        memo = {}
        return (f(len(s) - 1) - 1) % MOD

