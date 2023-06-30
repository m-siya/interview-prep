# ### FIRST MISSING POSITIVE

# Given an unsorted integer array nums, return the smallest missing positive integer.

# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

# https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            if nums[0] == 1: return 2
            else: return 1

        for i in range(len(nums)):
            if 0 <= nums[i] < len(nums) and nums[i] != i:
                while True:
                    nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
                    #nums[i] index is all good now but i is disturbed

                    if nums[i] == i or nums[i] < 0 or nums[i] >= len(nums) or nums[i] == nums[nums[i]]: break
            if nums[i] == len(nums): 
                nums[0] = nums[i]


      #  print(nums)

        for i in range(len(nums)):
            if i != 0 and nums[i] != i: return i

            
        return len(nums) if nums[0] != len(nums) else len(nums) + 1

