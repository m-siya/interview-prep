# ### SQUARES OF A SORTED ARRAY

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number 
# sorted in non-decreasing order.

# https://leetcode.com/problems/squares-of-a-sorted-array/description/

#Time Complexity -> O(N), space complexity -> O(1)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start, end = 0, len(nums) - 1

        squares = [-1] * len(nums)
        last_added = len(nums)
        while start <= end:
            if abs(nums[start]) > abs(nums[end]) :
                last_added -= 1
                squares[last_added] = nums[start] * nums[start]
                start += 1

            else:
                last_added -= 1
                squares[last_added] = nums[end] * nums[end]
                end -= 1
        

        return squares
        