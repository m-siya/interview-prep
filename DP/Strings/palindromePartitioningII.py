# ### PALINDROME PARTITIONING II

# Given a string s, partition s such that every substring of the partition is a palindrome

# Return the minimum cuts needed for a palindrome partitioning of s.
 
#  https://leetcode.com/problems/palindrome-partitioning-ii/description/?envType=problem-list-v2&envId=50v8wybv&

class Solution:
    def minCut(self, s: str) -> int:
        # brute force: write the backtracking sol again and get the partitioning with min length

        # or write dp function f(j) such that f(j) -> min partitions for s[:j + 1]
        def isPalindrome(j, i):
            if j >= i: return True
            if dp_pali[j][i] != None: return dp_pali[j][i]

            if s[i] == s[j]:
                dp_pali[j][i] = isPalindrome(j + 1, i - 1)
                return dp_pali[j][i]

            return False
        
        dp = [-1] * len(s)
        dp_pali = [[None for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]

        def f(j):
            if j >= len(s):
                return 0
            
            if dp[j] != -1: return dp[j]
            
            partitions = len(s) + 1
            for i in range(j, len(s)):
                if isPalindrome(j, i):
                    partitions = min(partitions, 1 + f(i + 1))
            
            dp[j] = partitions
            return partitions
        
        return f(0) - 1
                
