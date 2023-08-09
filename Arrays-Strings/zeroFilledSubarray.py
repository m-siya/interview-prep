# ### ZERO-FILLED SUBARRAY
# Given an integer array nums, return the number of subarrays filled with 0.

# A subarray is a contiguous non-empty sequence of elements within an array.

# https://leetcode.com/problems/number-of-zero-filled-subarrays/description/

# time complexity -> O(N), space complexity - O(1)

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        subArrLen = 0
        subArrNum = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                subArrLen += 1
            
            elif nums[i] != 0:
                subArrNum += (subArrLen * (subArrLen + 1)) // 2
                subArrLen = 0

        
        subArrNum += (subArrLen * (subArrLen + 1)) // 2
        return subArrNum


