### STONE GAME II
# Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, 
# and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the 
# most stones. 

# Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

# On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M. 
# Then, we set M = max(M, X).

# The game continues until all the stones have been taken.

# Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

 
# https://leetcode.com/problems/stone-game-ii/description/

#maximize alice and minimize bob
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        total_piles = len(piles)
        M = 1
        turn = 1
        dp = [[[-1] * (total_piles + 1) for i in range(total_piles + 1)] for p in range(0, 2)]


        def f(x, m, turn):
            #f(x, m) -> maximum stones that can be taken if first x pile 
            #is remaining and M = m 
            
            # if turn == 1, we add stones to sum since it is alice's turn

            #each person can take piles in range(1, 2m + 1)
            # m = max(m, x)
            if x >= total_piles:
                return 0

            if dp[turn][x][m] != -1:
                return dp[turn][x][m]

            res = int(1e9) if turn == 0 else -1
            stones = 0
            max_piles_to_take = min(2 * m, total_piles - x)
            for i in range(1, max_piles_to_take + 1):
                stones += piles[x + i - 1]
                if turn == 1:
                    res = max(res, stones + f(x + i, max(m, i), 1 - turn))
                else:
                    res = min(res, f(x + i, max(m, i), 1 - turn))

           # print(stones,turn)
            dp[turn][x][m] = res
            return res
        
        return f(0, M, 1)

