# ### MINIMUM NUMBER OF SWAPS TO GROUP ALL ONES TOGETHER II

# A swap is defined as taking two distinct positions in an array and swapping the values in them.

# A circular array is defined as an array where we consider the first element and the last element to be adjacent.

# Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.

# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/description/?envType=daily-question&envId=2024-08-02

class Solution:
    def minSwaps(self, nums: List[int]) -> int:     
        # for any question with the circular array problem, just append the array at the end of the same array to get rid of the subproblem

       #  check for every subarray of size total (possibly wrapped around), how many swaps are required to have the subarray be all 1’s.
       # The number of swaps required is the number of 0’s in the subarray.
       
        ones = sum(nums[i] == 1 for i in range(len(nums))) # size of sliding window
        nums = nums + nums

        onesInWindow, maxOnesInWindow = 0, 0
        for i in range(len(nums)):
            if i >= ones and nums[i - ones]:
              onesInWindow -= 1
            if nums[i] == 1:
              onesInWindow += 1
            
            maxOnesInWindow = max(onesInWindow, maxOnesInWindow)
        
        return ones - maxOnesInWindow




        