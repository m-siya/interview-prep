# House Robber II

# https://leetcode.com/problems/house-robber-ii/

# You are a professional robber planning to rob houses along a street. Each house has a 
# certain amount of money stashed. All houses at this place are arranged in a circle. That 
# means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a 
# security system connected, and it will automatically contact the police if two adjacent houses 
# were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum 
# amount of money you can rob tonight without alerting the police.


#approach : at each house, rob it or leave it
# to deal with the circular array condition, in a sol, you can either rob the first house or the last
# so pass 2 separate arrays to func, 1 without the last element and the other without the first.
#time complexity : O(N)
# space complexity : O(N)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp1 = [-1] * (len(nums) - 1)
        dp2 = [-1] * (len(nums) - 1)

        def f(i, nums, dp): #-> max money I can rob safely at ith house
            if i < 0:
                return 0

            if dp[i] != -1:
                return dp[i]

            leaveHouse = f(i - 1, nums, dp)
            robHouse = nums[i] + f(i - 2, nums, dp)

            dp[i] = max(leaveHouse, robHouse)
            return dp[i]

        #print(f(len(nums) - 2, nums[1:]), nums[1:])
        #print(f(len(nums) - 2, nums[:-1]), nums[:-1])
        return max(f(len(nums) - 2, nums[1:], dp1), f(len(nums) - 2, nums[:-1], dp2)) 