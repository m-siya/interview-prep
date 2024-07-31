# ### MAX SCORE OF GOOD SUBARRAY

# You are given an array of integers nums (0-indexed) and an integer k.

# The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j.

# Return the maximum possible score of a good subarray.

# https://leetcode.com/problems/maximum-score-of-a-good-subarray/description/

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # that means kth index must be included in the good subarray
        # or consider all subarrays which include the kth index

        # find next smaller element
        stack = [(-1, -1)]
        res = 0

        for i, n in enumerate(nums):

            while stack and stack[-1][1] > n:
                j, m = stack.pop()
                # find right and left bounds where m is the min element
                # is bounds include k, then update res

                right = i
                left = stack[-1][0]
                if left < k < right:
                    res = max(res, m * (right - left - 1))
            
            stack.append((i, n))
        
        for i in range(len(stack)):
            j, n = stack[i]
            right = len(nums)
            left = stack[i - 1][0]
            if left < k < right:
                res = max(res, n * (right - left - 1))
        
        return res

        
