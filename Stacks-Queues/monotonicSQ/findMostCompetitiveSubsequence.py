# ### FIND MOST COMPETITIVE SUBSEQUENCE 

# Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.

# An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.

# We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position where a and b differ, subsequence a has a number less than the corresponding number in b. For example, [1,3,4] is more competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.

# https://leetcode.com/problems/find-the-most-competitive-subsequence/description/

class Solution:
    def mostCompetitive(self, arr: List[int], k: int) -> List[int]:

        # choose the min num possible 

        res = []

        stack = []

        for i in range(len(arr)):
           # print(i, arr[i], len(arr) - i, k)
            while stack and stack[-1] > arr[i] and (len(arr) - i) > k - len(stack):
                stack.pop()
            
            stack.append(arr[i])
        
        return stack[:k]
            
        