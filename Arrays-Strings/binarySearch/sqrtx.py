# ### SQRT(X)

# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The 
# returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:

        low, high = 0, x
        ans = 0
        while low <= high:
            mid = low + (high - low) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                high = mid - 1
            else:
                ans = mid
                low = mid + 1
        
        return ans