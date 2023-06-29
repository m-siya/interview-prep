# ### NON-DECREASING ARRAY

# Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one 
# element.

# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

# https://leetcode.com/problems/non-decreasing-array/description/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        decreased = False

        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                if decreased == True: return False
                
                if i - 1 == 0 or i - 1 == len(nums) - 2:
                    decreased = True
                else:
                    if nums[i - 2] > nums[i] and nums[i - 1] > nums[i + 1]: 
                       # print(nums[i])
                        return False
                    decreased = True
        return True
        

