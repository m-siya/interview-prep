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
l