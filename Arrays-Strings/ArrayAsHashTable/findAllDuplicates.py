# 442. Find All Duplicates in an Array

# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time and uses only constant extra space.

# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

# mark elements seen as negative. if see negative element again, add to ans

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums)):
            num = abs(nums[i])
            #print(num)
            if nums[num - 1] < 0:
                ans.append(abs(num))
            else:
                nums[num - 1] = -1 * nums[num - 1]
        
        return ans

        