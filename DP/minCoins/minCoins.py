# You are given an integer array coins representing coins of different denominations and
# an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money 
# cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

# https://leetcode.com/problems/coin-change/description/

# my solution
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1 for _ in range(amount + 1)]

        def f(amount):
            #f(amount) -> minimum number of coins needed
            if amount == 0:
                return 0

            if dp[amount] != -1:
                return dp[amount]
            min_coins = int(1e9)
            for coin in coins:
                if amount - coin >= 0:
                    min_coins = min(min_coins, 1 + f(amount - coin))
            
            dp[amount] = min_coins
            return min_coins

        min_coins = f(amount)
        return min_coins if min_coins != int(1e9) else -1
    
# Neetcode solution
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)  #maximum number of coins can be amount if we have only 1 dollar coins
        dp[0] = 0

        for a in range(1, amount + 1):
            #print(f"amount is {a}")
            for c in coins:
                #print(f"coin is {c}")

                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

                    #print(dp)

        return dp[amount] if dp[amount] != amount + 1 else -1

