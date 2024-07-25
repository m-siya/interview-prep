# ### FORM LARGEST INTEGER WITH DIGITS THAT SUM TO TARGET

# Given an array of integers cost and an integer target, return the maximum integer you can paint under the following rules:

# The cost of painting a digit (i + 1) is given by cost[i] (0-indexed).
# The total cost used must be equal to target.
# The integer does not have 0 digits.
# Since the answer may be very large, return it as a string. If there is no way to paint any integer given the condition, return "0".

# https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/description/?envType=problem-list-v2&envId=50vlu3z5&

# good for how to deal with strings in dp

from functools import lru_cache
class Solution:
    def largestNumber(self, costs: List[int], target: int) -> str:
        # obviously more integers is better
        # (greedy?) choose the nums with lower cost
        # if same cost, choose bigger int
        def myMax(a, b):
            if '0' in a:
                return b
            elif '0' in b:
                return a
            elif len(a) > len(b):
                return a
            elif len(b) > len(a):
                return b
            else:
                return max(a, b)
        
        @lru_cache(None)
        def f(i, target):
            if target == 0:
                return ''
            if target < 0 or i == len(costs):
                return '0'
            
            take = str(i + 1) + f(0, target - costs[i])
            leave = f(i + 1, target)

            #print(max(take, leave))

            return myMax(take, leave)
        
        return f(0, target)
    
#with dp array

from functools import lru_cache
class Solution:
    def largestNumber(self, costs: List[int], target: int) -> str:
        # obviously more integers is better
        # (greedy?) choose the nums with lower cost
        # if same cost, choose bigger int
        def myMax(a, b):
            if '0' in a:
                return b
            elif '0' in b:
                return a
            elif len(a) > len(b):
                return a
            elif len(b) > len(a):
                return b
            else:
                return max(a, b)
        
        dp = [[None for _ in range(target + 1)] for _ in range(len(costs))]

        def f(i, target):
            if target == 0:
                return ''
            if target < 0 or i == len(costs):
                return '0'
            
            if dp[i][target] != None: return dp[i][target]

            take = str(i + 1) + f(0, target - costs[i])
            leave = f(i + 1, target)

            #print(max(take, leave))

            dp[i][target] = myMax(take, leave)
            return dp[i][target]
        
        return f(0, target)
    
    