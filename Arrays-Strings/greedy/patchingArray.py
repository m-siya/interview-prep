# ### PATCHING ARRAY

# Given a sorted integer array nums and an integer n, add/patch elements to the array such that any number in the range [1, n] inclusive can be formed by the sum of some elements in the array.

# Return the minimum number of patches required.

# https://leetcode.com/problems/patching-array/description/

#  if we can already cover range [1, k], then by just taking in the next integer k+1, we will 
# be able to cover a new range [1, k+(k+1)] inclusive. There is no need to investigate all
#  the numbers falling in between one by one as explained above.

# basically if the next num in the nums array is less or equal to max_sum seen yet, then it ensures
# that all numbers in the new range [1, k + (k + 1)] are covered. 
# if not, then we need to add nums one by one.

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        i = 0
        max_sum = 0
        count = 0

        while max_sum < n:

            if i < len(nums) and nums[i] <= max_sum + 1:
                max_sum += nums[i]
                i += 1
            
            else:
                count += 1
                max_sum += (max_sum + 1)
        
        return count

            



        