# ### MINIMUM SIZE SUBARRAY SUM

# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# https://leetcode.com/problems/minimum-size-subarray-sum/


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        res = float("inf")
        
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(r - l +1, res)
                total -= nums[l]
                l+= 1
                
        return 0 if res == float("inf") else res