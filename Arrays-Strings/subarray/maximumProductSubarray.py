# ### MAXIMUM PRODUCT SUBARRAY

# Given an integer array nums, find a 
# subarray
#  that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# https://leetcode.com/problems/maximum-product-subarray/description/

# TC: O(N)
# SC: O(1)

# curr max because we want the maximum product seen yet
# curr min because there might be a large negative product which when multiplied
# with another negative might give a larger (positive) product
# then at last update ans


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n = len(nums)

        curr_max = nums[0]
        curr_min = nums[0]
        ans = nums[0]

        for i in range(1, n):
            curr = curr_max
            curr_max = max(curr * nums[i], curr_min * nums[i], nums[i])
            curr_min = min(curr * nums[i], curr_min * nums[i], nums[i])

            ans = max(curr_max, ans)
        
        return ans
        

