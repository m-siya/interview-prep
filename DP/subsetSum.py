# We are given an array ‘ARR’ with N positive integers. We need to find if there is a 
# subset in “ARR” with a sum equal to K. If there is, return true else return false.

def isSubsetSum (N, arr, sum):
        # code here 
        
    def f(i, target):
            #f(i, target) -> if a subset exists in array[:i] with sum == target
        if i == 0:
            return arr[i] == target
        if target == 0:
            return True
            
        leave = f(i - 1, target)
        take = False
        if arr[i] <= target:
            take = f(i - 1, target - arr[i])
        
        return leave or take
            
        
                
        
    return f(len(arr) - 1,  sum)
        

print(isSubsetSum(6, [3, 34, 4, 12, 5, 2], 9))

### PARTITION EQUAL SUBSET SUM

# Given an integer array nums, return true if you can partition the array into two subsets such 
# that the sum of the elements in both subsets is equal or false otherwise.

# https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        full_sum = sum(nums)
        if full_sum % 2 != 0:
            return False
        # s1 + s2 = s
        # s1 == s2 == s/2
        # i.e find one subsequence with sum = s/2
        half_sum = full_sum // 2
        dp = [[-1 for i in range(half_sum + 1)] for j in range(len(nums))]

      #  print(half_sum)

        def f(i, target, arr):
            #f(i, target) -> if a subset exists in array[:i] (i inclusive) with sum == target
            if target == 0:
                return True
            if i == 0:
                return arr[i] == target
            

            if dp[i][target] != -1:
                return dp[i][target]
                
            leave = f(i - 1, target, arr)
            take = False
            if arr[i] <= target:
                take = f(i - 1, target - arr[i], arr)
            
            dp[i][target] = leave or take
            return dp[i][target]
        
        return f(len(nums) - 1, half_sum, nums)


### Partition Array Into Two Arrays to Minimize Sum Difference

#### Pre-requisite - Closest Subsequence Sum
# You are given an integer array nums and an integer goal.

# You want to choose a subsequence of nums such that the sum of its elements is the closest 
# possible to goal. That is, if the sum of the subsequence's elements is sum, then you want to minimize the 
# absolute difference abs(sum - goal).

# Return the minimum possible value of abs(sum - goal).

# Note that a subsequence of an array is an array formed by removing some elements (possibly all or none) of 
# the original array.

# https://leetcode.com/problems/closest-subsequence-sum/description/
from bisect import bisect_left

class Solution(object):
    def minAbsDifference(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """

        #generate all possible sums of subsequences
        # def dfs(i, curr, arr, sums):
        #     if i == len(arr):
        #         sums.add(curr)
        #         return 
        #     dfs(i + 1, curr, arr, sums)
        #     dfs(i + 1, curr + arr[i], arr, sums)

        
        # sums1, sums2 = set(), set()

        # #generate all possible sums for first half and second half
        # dfs(0, 0, nums[:len(nums) // 2], sums1)
        # dfs(0, 0, nums[len(nums)//2:], sums2)

        # takes too long, approx 3000 ms in lc

        #try
        def sums(arr):
            sums = {0}
            for element in arr:
                sums |= {subseq_sum + element for subseq_sum in sums}
            return sums
        
        # this is about 1000 ms in lc
        # sums1 = sums(nums[:len(nums) // 2])
        # sums2 = sorted(sums(nums[len(nums) // 2:]))


        # about 400 ms in lc, beats 100%
        sums1 = sums(nums[1::2])
        sums2 = sorted(sums(nums[::2]))

        #sort the possible sums of 2nd half
        #sums2 = sorted(sums2)
        min_difference = 10 ** 10
        for s in sums1:
            remaining = goal - s
            #find this remaining value in sums2
            i = bisect_left(sums2, remaining)
            if i < len(sums2):
                min_difference = min(min_difference, abs(remaining - sums2[i]))
            if i > 0:
                min_difference = min(min_difference, abs(remaining - sums2[i - 1]))
        
        return min_difference

        
        


