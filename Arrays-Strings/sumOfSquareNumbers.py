# ### SUM OF SQUARE NUMBERS

# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

# https://leetcode.com/problems/sum-of-square-numbers/description/

import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        lo, hi = 0, math.floor(math.sqrt(c))

        while lo <= hi:
          #  print(lo, hi)
            if lo ** 2 + hi ** 2 == c:
                return True
            elif lo ** 2 + hi ** 2 > c:
                hi -= 1
            else:
                lo += 1
        

        return False
                

        