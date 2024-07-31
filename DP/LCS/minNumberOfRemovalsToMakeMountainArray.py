# ### MINIMUM NUMBER OF REMOVALS TO MAKE MOUNTAIN ARRAY

# You may recall that an array arr is a mountain array if and only if:

# arr.length >= 3
# There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given an integer array nums​​​, return the minimum number of elements to remove to make nums​​​ a mountain array.


# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/description/

# find lis ending at every i for i in nums
# find lds starting at every i for i in nums
# answer is len(nums) - lis[i] - lds[i] - 1

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        lis_dp = [0] * len(nums)
        lds_dp = [0] * len(nums)
        n = len(nums)

        #lis 
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    lis_dp[i] = max(lis_dp[i], lis_dp[j] + 1)
        
        #lds
        for i in range(n - 2, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[i] > nums[j]:
                    lds_dp[i] = max(lds_dp[i], lds_dp[j] + 1)
        

        res = 0
        for i in range(n):
            if lis_dp[i] and lds_dp[i]:
                res = max(res, lis_dp[i] + lds_dp[i])
    
        return n - res - 1


        