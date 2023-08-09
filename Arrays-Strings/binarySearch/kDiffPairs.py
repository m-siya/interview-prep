# ### K DIFF PAIRS IN AN ARRAY

# Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

# A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

# 0 <= i, j < nums.length
# i != j
# |nums[i] - nums[j]| == k
# Notice that |val| denotes the absolute value of val.


# https://leetcode.com/problems/k-diff-pairs-in-an-array/description/


# method - sort the array and run a for loop then do a binary search to find if pair exists
# tc - O(nlogn) and sc - O(N)

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()

        pair_count = 0
        pairs_seen = set()
        for i in range(len(nums)):
            start, end = i + 1, len(nums) - 1

            while start <= end:
                mid = (start + end) // 2
                if abs(nums[mid] - nums[i]) == k and (nums[i], nums[mid]) not in pairs_seen:
                    pair_count += 1
                    pairs_seen.add((nums[i], nums[mid]))
                    break
                elif abs(nums[mid] - nums[i]) > k:
                    end = mid - 1
                else:
                    start = mid + 1
            

        return pair_count
            

#optimised method -> make a Counter of all the frequencies of the elements and iterate through the unique elements.
# then if k > 0 and i + k in freq, or k == 0 and freq[i] > 1: increment count
# because only if k == 0 are the same elements counted

# tc - O(N), sc - O(N)

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        pair_count = 0

        freq = Counter(nums)

        for i in freq.keys():
            if k > 0 and i + k in freq or k == 0 and freq[i] > 1:
                pair_count += 1         

        return pair_count
            

        