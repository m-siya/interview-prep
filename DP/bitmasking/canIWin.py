# ### CAN I WIN 

# In the "100 game" two players take turns adding, to a running total, any integer from 1 to 10. The player who first causes the running total to reach or exceed 100 wins.

# What if we change the game so that players cannot re-use integers?

# For example, two players might take turns drawing from a common pool of numbers from 1 to 15 without replacement until they reach a total >= 100.

# Given two integers maxChoosableInteger and desiredTotal, return true if the first player to move can force a win, otherwise, return false. Assume both players play optimally.

# https://leetcode.com/problems/can-i-win/description/

from functools import lru_cache
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # f(turn, integers played, curr_total) -> can force win?
        # played num is bitmask of length maxChoosableInteger
        # if bit not set, then can play that number

        # no need to track currTotal in memo because obviously playedNums can tell u waht the curr total is

        if desiredTotal <= 0: return True

        if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
            return False

        dp = [-1 for _ in range((1 << maxChoosableInteger))]

        def f(playedNums, currTotal):
            # print(playedNums, currTotal)
            # if currTotal >= desiredTotal:
            #     return True if turn == 1 else False
            
            if currTotal >= desiredTotal: 
                return False

            if dp[playedNums] != -1: return dp[playedNums]
            
            wins = False
            for i in range(1, maxChoosableInteger + 1):
                if not ((1 << (i - 1)) & playedNums):
                    if currTotal + i >= desiredTotal or not f(playedNums | (1 << (i - 1)), currTotal + i):        
                        wins = True
                        dp[playedNums] = wins
                        return wins
            
            dp[playedNums] = wins
            return wins
        
        return f(0, 0)

