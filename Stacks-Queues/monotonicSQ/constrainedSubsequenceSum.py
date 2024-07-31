# ### CONSTRAINED SUBSEQUENCE SUM

# Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

# A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

 
# https://leetcode.com/problems/constrained-subsequence-sum/description/

## top down dp

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        
        res = -1e9

        dp = [-1e9 for _ in range(len(nums))]

        def f(i):
            if i >= len(nums):
                return 0
            
           # print(i, nums[i], i + k + 1)
            if dp[i] != -1e9:
                return dp[i]
            
            take = -1e9
            for j in range(i + 1, min(i + k, len(nums)) + 1):
                take = max(take, nums[i] + f(j))   
            take = max(take, nums[i]) # take nothing

            dp[i] = take
            return take
        
        for i in range(len(nums)):
          #  print(f(i))
            res = max(res, f(i))
        
        return res #((max(nums) == 0 and res == 0) or res != 0

# top down dp

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        
        res = -1e9

        dp = [nums[i] for i in range(len(nums))]


        for i in range(len(nums) - 1, -1, -1):
            n = nums[i]
            take = nums[i]
            for j in range(i + 1, min(i + k + 1, len(nums))):
                take = max(take, nums[i] + dp[j])
            
            dp[i] = take
        
        return max(dp)


## deque solution

# get the max of each k-window in O(1) instead of scanning linearly

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        
        res = -1e9

        dp = [nums[i] for i in range(len(nums))]
        q = collections.deque() #(i)

        res = 0

        for i in range(len(nums)):
            n = nums[i]

            if i > k and q and q[0] < i - k:
                q.popleft()
            
            if q:
                dp[i] = max(dp[i], nums[i] + dp[q[0]])
        
            while q and dp[q[-1]] <= dp[i]:
                q.pop()

            q.append(i)

        return max(dp)