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

#maximize alice and minimize bob - THE MINMAX ALGORITHM 
# at each step, one player tries to maximize the solution and the other tries to minimize the first player's
# score when it is the other's turn. this is assuming both players play optimally

# this is useful in a zero-sum game i.e alice getting more points means bob gets less and bob getting more
# means alice gets less.
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
                    res = min(res, f(x + i, max(m, i), 1 - turn)) # here, we dont add stones because in bob's turn
                    #alice will not get the stone value added to her stone

           # print(stones,turn)
            dp[turn][x][m] = res
            return res
        
        return f(0, M, 1)

### STONE GAME III

# Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and 
# each stone has an associated value which is an integer given in the array stoneValue.

# Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take 1, 2, or 3 
# stones from the first remaining stones in the row.

# The score of each player is the sum of the values of the stones taken. The score of each player is 0 initially.

# The objective of the game is to end with the highest score, and the winner is the player with the highest score
#  and there could be a tie. The game continues until all the stones have been taken.

# Assume Alice and Bob play optimally.

# Return "Alice" if Alice will win, "Bob" if Bob will win, or "Tie" if they will end the game with the same score.

# https://leetcode.com/problems/stone-game-iii/description/

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [[-1 for _ in range(len(stoneValue))] for _ in range(0, 2)]

        def f(i, turn):
        # f(i, turn) -> who will win or is game a tie if index of first stone remaining is i and turn = turn
        #turn (1) -> Bob's turn
        #turn (0) -> Alice's turn

        #pick x stones
            if i == len(stoneValue):
                return 0

            if dp[turn][i] != -1:
                return dp[turn][i]

            score = 0
            res = -int(1e9) if turn == 0 else int(1e9)
            for x in range(1, 4):
                if i + x - 1 < len(stoneValue):
                    score += stoneValue[i + x - 1]
                    if turn == 0:
                        res = max(res, score + f(i + x, 1 - turn))

                    if turn == 1:
                        res = min(res, f(i + x, 1 - turn))
                    
            
            dp[turn][i] =  res
            return res

        ans = f(0, 0)
        if ans < sum(stoneValue) - ans:
            return "Bob"
        elif ans > sum(stoneValue) - ans:
            return "Alice"
        else:
            return "Tie"

                
