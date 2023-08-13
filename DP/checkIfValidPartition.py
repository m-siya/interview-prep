# ### CHECK IF THERE IS A VALID PARTITION FOR THE ARRAY

# You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.

# We call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:

# The subarray consists of exactly 2 equal elements. For example, the subarray [2,2] is good.
# The subarray consists of exactly 3 equal elements. For example, the subarray [4,4,4] is good.
# The subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements is 1. For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.
# Return true if the array has at least one valid partition. Otherwise, return false.

# https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/description/

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        dp = [None] * n

        def f(i):
            #f(i) -> whether a valid partition exists for nums[i:]
            if i == n:
                return True
            
            if i > n:
                return False

            if dp[i] != None:
                return dp[i]

            take2Equal, take3Equal, take3Increasing = False, False, False
            if i + 2 <= n and nums[i] == nums[i + 1]:
                take2Equal = f(i + 2)
            if i + 3  <= n and nums[i] == nums[i + 1] and nums[i] == nums[i + 2]:
                take3Equal = f(i + 3)
            if i + 3 <= n and nums[i + 1] - nums[i]==1 and nums[i + 2] - nums[i + 1]==1:
                take3Increasing = f(i + 3)
            
            dp[i] = take2Equal or take3Equal or take3Increasing
            return dp[i]

        return f(0)

            