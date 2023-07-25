# ### FIRST MISSING POSITIVE

# Given an unsorted integer array nums, return the smallest missing positive integer.

# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

# https://leetcode.com/problems/first-missing-positive/

# intuition - is a positive integer is not in the given array,it must be in the range [1..n]
# better framing of the problem is - smallest postive integer not in the array
# method - use array as hash table
# iterate through the array and swap(nums[i] with nums[nums[i]) which ensure nums[i] reaches the postion where
# nums[k] == k. 
# eg nums[3] = 5, => swap(5, nums[5]) => ... => till nums[5] == 5
# do not do anything for negative numbers
# if nums[i] == len(nums): put it at nums[0] since we do not care for 0 as well.

# iterate through nums again. if at any point, nums[i] != i then that i is our missing positive. return that
# else return len(nums) if it does not exist or if it does then len(nums) + 1

# time complexity - O(n^2)

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

