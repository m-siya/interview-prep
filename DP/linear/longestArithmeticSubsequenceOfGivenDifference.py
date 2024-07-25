# ### LONGEST ARITHMETIC SUBSEQUENCE OF GIVEN DIFFERENCE

# Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.

# A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the order of the remaining elements.

# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/?envType=problem-list-v2&envId=50vlu3z5&

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        #this works here because difference is given and this can only be a arithmetic progression so
        # suppose we have arr a1, a2, ...ai,... an
        # and we are at num ai. i always need to choose ai inorder to choose some num aj such that aj - ai == difference and where ai and aj are part of the longest subseq so to say that if it fits the bill, then it will need to be added.
        
        dp = collections.defaultdict(int)

        for i in range(len(arr)):
            if arr[i] - difference in dp:
                dp[arr[i]] = dp[arr[i] - difference] + 1
            else:
                dp[arr[i]] = 1
        
        return max(dp.values())
           
# also tried:
# top down 2d dp
from functools import lru_cache
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        dp = [[-1 for _ in range(len(arr))] for _ in range(len(arr))]
        def f(i, j):
            # j is prev index taken
            #def take/leave
            if i == len(arr):
                return 0
            
            if dp[i][j] != -1: return dp[i][j]

            take, leave = 0, 0
            if j == -1 or arr[i] - arr[j] == difference:
                take = 1 + f(i + 1, i)
            leave = f(i + 1, j)

            dp[i][j] = max(take, leave)
            return dp[i][j]
        

        return f(0, -1)

        
# top down 1d dp
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        dp = [-1] * len(arr)
        def f(i):
            # j is prev index taken
            #def take/leave
            if i == len(arr):
                return 0
            
            if dp[i] != -1: return dp[i]

            # take, leave = 0, 0
            # if j == -1 or arr[i] - arr[j] == difference:
            #     take = 1 + f(i + 1, i)
            # leave = f(i + 1, j)
            res = 0
            for j in range(i + 1, len(arr)):
                subseq_len = 0
                if arr[j] - arr[i] == difference:
                    subseq_len = 1 + f(j)
                
                res = max(res, subseq_len)

            dp[i] = res
            return dp[i]
        

        res = 0
        for i in range(len(arr)):
            subseq_len = 1 + f(i)
            res = max(res, subseq_len)
        
        return res
        
# bottom up dp
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        dp = [1] * len(arr)

        for i in range(len(arr) - 1, -1, -1):
            res = 1
            for j in range(i + 1, len(arr)):
                subseq_len = 1
                if arr[j] - arr[i] == difference:
                    # if we are taking elem at jth index
                    subseq_len = 1 + dp[j]
                res = max(res, subseq_len)
            
            dp[i] = res 
        
       #print(dp)
        return max(dp)
                    
