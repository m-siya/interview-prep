### LENGTH OF LONGEST SUBARRAY WITH ATMOST K FREQUENCY

# You are given an integer array nums and an integer k.

# The frequency of an element x is the number of times it occurs in an array.

# An array is called good if the frequency of each element in this array is less than or equal to k.

# Return the length of the longest good subarray of nums.

# A subarray is a contiguous non-empty sequence of elements within an array.

# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/

# tc : O(N)
# sc: O(N)

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        max_length = 0
        max_freq = 0
        j = 0
        freq = dict()

        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
            max_freq = max(max_freq, freq[nums[i]])

            while max_freq > k:
                freq[nums[j]] = freq.get(nums[j], 0) - 1

                if nums[j] == nums[i]:
                    max_freq -= 1
    
                j += 1
            
            max_length = max(max_length, i - j + 1)
        
        return max_length

        