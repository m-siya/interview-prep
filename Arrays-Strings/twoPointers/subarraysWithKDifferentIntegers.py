# ### SUBARRAYS WITH K DIFFERENT INTEGERS

# Given an integer array nums and an integer k, return the number of good subarrays of nums.

# A good array is an array where the number of different integers in that array is exactly k.

# For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# A subarray is a contiguous part of an array.

# https://leetcode.com/problems/subarrays-with-k-different-integers/description/

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def atMost(S):
            freq = Counter()

            res, l = 0, 0
            curr_count = 0
            for r in range(len(nums)):
                if not freq[nums[r]]:
                    curr_count += 1
                freq[nums[r]] += 1
                
                while curr_count > S:
                    freq[nums[l]] -= 1
                    if not freq[nums[l]]:
                        curr_count -= 1
                    l += 1
                
                res += r - l + 1

            return res
        
        return atMost(k) - atMost(k - 1)
