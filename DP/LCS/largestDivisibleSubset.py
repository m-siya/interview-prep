# ### Largest Divisible Subset

# Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

# answer[i] % answer[j] == 0, or
# answer[j] % answer[i] == 0
# If there are multiple solutions, return any of them.

 
# https://leetcode.com/problems/largest-divisible-subset/description/


from functools import lru_cache
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # arr = [1, 2, 3, 4, 6, 8]
        # 
        nums.sort()
        
        @lru_cache(None)
        def f(i):
           # print(i)
            if i == len(nums) : return []

            pick = []
            found = False
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0:
                    new_pick = [nums[i]] + f(j)
                    pick = max(pick, new_pick, key=lambda x: len(x))
                    found = True
            if not found:
                pick = [nums[i]]
                                         
           # leave = f(i + 1)
            return pick

            #a = max(pick, leave, key= lambda x: len(x))
           # print(pick, leave)
        

        ans = []

        for i in range(len(nums)):
            ans = max(ans, f(i), key= lambda x: len(x))
        
        return ans
        
            

        