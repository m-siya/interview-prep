# You are given an integer array coins representing coins of different denominations and an 
# integer amount representing a total amount of money.

# Return the number of combinations that make up that amount. If that amount of money cannot be made 
# up by any combination of the coins, return 0.

# You may assume that you have an infinite number of each kind of coin.

# The answer is guaranteed to fit into a signed 32-bit integer.

# https://leetcode.com/problems/coin-change-ii/description/

class Solution:
    def change(self, total: int, coins: List[int]) -> int:
        dp = [[-1 for _ in range(total + 1)] for _ in range(len(coins))]
      #  print(dp)

        def f(index, curr_amount):
           #f(index, amount) -> total combinations possible when considering coins[:index] (inclusive) to make up amount money
            if index < 0:
                if curr_amount == total:
                    return 1
                else:
                    return 0
           # print(index, curr_amount)
            if dp[index][curr_amount] != -1:
                return dp[index][curr_amount]


            #at each step, take or leave the coin[index]
            leave = f(index - 1, curr_amount)
            if curr_amount + coins[index] <= total:
                take = f(index, curr_amount + coins[index])
            else:
                take = 0

            dp[index][curr_amount] = leave + take
            return leave + take

        return f(len(coins) - 1, 0)