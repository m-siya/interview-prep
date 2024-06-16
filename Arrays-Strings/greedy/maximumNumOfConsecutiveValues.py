# ### MAXIMUM NUMBER OF CONSECUTIVE VALUES YOU CAN MAKE

# You are given an integer array coins of length n which represents the n coins that you own. The value of the ith coin is coins[i]. You can make some value x if you can choose some of your n coins such that their values sum up to x.

# Return the maximum number of consecutive integer values that you can make with your coins starting from and including 0.

# Note that you may have multiple coins of the same value.

# https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/description/

## same idea as patching array

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        max_sum = 0
        i = 0

        while True:
            if i < len(coins) and coins[i] <= max_sum + 1:
                max_sum += coins[i]
                i += 1

            else:
                break
        
        return max_sum + 1

        

