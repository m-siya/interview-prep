# ### COUNT NUMBER OF NICE SUBARRAYS

# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

# Return the number of nice sub-arrays.

# https://leetcode.com/problems/count-number-of-nice-subarrays/description/

# if we replace even elements with 0 and odd elements with 1, then problem reduced to number of subarrays with sum k

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        def atMost(S):
            if S < 0:
                return 0
            odd_count = 0
            res = 0
            l = 0

            for r in range(len(nums)):
                if nums[r] % 2 != 0:
                    odd_count += 1
                #while valid
                while odd_count > S:
                    if nums[l] % 2 != 0:
                        odd_count -= 1
                    l += 1
                #print(res, r - l + 1)
                res += r- l + 1
           # print(res)
            return res

        return atMost(k) - atMost(k - 1)

