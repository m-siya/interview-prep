# ### PEAK ELEMENT

# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks,
# return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater 
# than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.

# https://leetcode.com/problems/find-peak-element/description/

# intuition for binary search: no two adjacent elements are same and the nums[-1] and nums[n] count as -inf. So
# after dividing the array into two and checking mid is not a peak element, 
# if nums[mid + 1] > nums[mid], then it means nums[mid + 1] has the potential to be a peak element. if nums[mid + 2] is less
# then nums[mid + 1], then it is a peak element, but if nums[mid + 2] > nums[mid + 1] then nums[mid + 2] is a potential peak
# and so on. At the end, nums[n - 1] is guaranteed to be a peak element in this situation. 

# time complexity - O(logn), space - O(1)

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if mid + 1 < len(nums) and nums[mid + 1] > nums[mid]:
                low = mid + 1
            elif mid - 1 >= 0 and nums[mid - 1] > nums[mid]:
                high = mid - 1
            else:
                return mid

        
        return len(nums) - 1