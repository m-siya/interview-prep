# ### SUBSETS

# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 
# https://leetcode.com/problems/subsets/description/

# backtracking
# time complexity - O(N * 2 ^ N), space - O(N)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr, i):
            if i == len(nums):
                return True

            include_status = backtrack(curr + [nums[i]], i + 1)
            if include_status:
                res.append(curr + [nums[i]])

            exclude_status = backtrack(curr, i + 1)
            if exclude_status:
                res.append(curr)

        backtrack([], 0)

        return res
    
# backtracking approach II
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(subset, index):
            res.append(subset)

            for i in range(index, len(nums)):
                subset.append(nums[i])
                backtrack(subset[:], i + 1)
                subset.pop()
        
        backtrack([], 0)
        return res
    
# Lexicographic (Binary Sorted) Subsets
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        for i in range(2**n, 2**(n + 1)):
            bitmask = bin(i)[3:]
            res.append([nums[bit] for bit in range(n) if bitmask[bit] == '1'])

        return res
                
                

