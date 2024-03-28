# ### SUBARRAY SUM EQUALS K

# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# https://leetcode.com/problems/subarray-sum-equals-k/description/

# TC: O(N)
# SC: O(N)


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # keep a running cumulative sum. and a dict that maps cumulative sum -> times it was seen in the array
        # iterate through array and add to cumulative sum
        # we know that differences between prefix sums is sums of subarrays
        # so aim is to find:  prefix-sum1 - prefix_sum2 = k 
        # or -> prefix-sum2 = prefix-sum1 - k
        # so we see this in the dict then we know that we found a subarr of type we're looking for
        # then just add count for current cumulative_sum in dict

        
        count = 0
        cumulative_sum = 0
        d = dict()
        d[0] = 1

        for i in range(len(nums)):
            cumulative_sum += nums[i]
            count += d.get(cumulative_sum - k, 0)
            d[cumulative_sum] = d.get(cumulative_sum, 0) + 1
        return count

        