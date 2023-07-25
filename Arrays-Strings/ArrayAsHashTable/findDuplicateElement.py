# ### DUPLICATE ELEMENT

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.


# https://leetcode.com/problems/find-the-duplicate-number/description/

# method - use fast and slow pointers

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]

            if slow == fast:
                break
        
        return fast

        
    