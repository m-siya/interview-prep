# ### MAXIMUM SUM OBTAINED OF ANY PERMUTATION

# We have an array of integers, nums, and an array of requests where requests[i] = [starti, endi]. The ith request asks for the sum of nums[starti] + nums[starti + 1] + ... + nums[endi - 1] + nums[endi]. Both starti and endi are 0-indexed.

# Return the maximum total sum of all requests among all permutations of nums.

# Since the answer may be too large, return it modulo 109 + 7.

# https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/ 

# assign the biggest num in nums to the index with the most weight (i.e the one ocurring the most frequently)

from collections import defaultdict
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        weights = [0] * (len(nums) + 1)

        for request in requests:
            start, end = request[0], request[1]
            weights[start] += 1
            weights[end + 1] -= 1

        for idx in range(1, len(nums) + 1):
            weights[idx] += weights[idx - 1]

        ans = 0

        for num, weight in zip(sorted(nums), sorted(weights[:-1])):
            ans += num * weight

        return ans % (10**9 + 7)
        