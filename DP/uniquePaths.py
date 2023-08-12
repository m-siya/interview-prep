# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or 
# right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the 
# bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

# https://leetcode.com/problems/unique-paths/description/

#top-down memoization solution
class Solution:
    def uniquePaths_TP(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        def f(i: int, j: int, dp: [[int]]) -> int:
            if i < 0 or j < 0:
                return 0
            
            if i == 0 and j == 0:
                return 1
            
            if dp[i][j] != -1:
                return dp[i][j]
            

            fromLeft = f(i, j - 1, dp)
            fromUp = f(i - 1, j, dp)

            dp[i][j] = fromLeft + fromUp
            return dp[i][j]

        return f(m - 1, n - 1, dp)
    
    #Bottom up iterative solution using tabulation method
    #Space Complexity = O(1)
    
    def uniquePaths_BU(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]

        def f() -> None:
            for i in range(m):
               for j in range(n):
                    if i == 0 and j == 0:
                       dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                   # print(dp[i][j], i, j)
        
                   
                    
        f()
       # print(dp)
        return dp[m - 1][n - 1]

# ### UNIQUE PATHS II

# You are given an m x n integer array grid. There is a robot initially located at the top-left corner 
# (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot
# can only move either down or right at any point in time.

# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any
# square that is an obstacle.

# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The testcases are generated so that the answer will be less than or equal to 2 * 109.

# https://leetcode.com/problems/unique-paths-ii/description/

#TopDown solution with memoization
# tc - O(m * n), sc - O(m * n)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[-1 for _ in range(n)] for _ in range(m)]

        def f(i: int, j: int) -> int:
            if obstacleGrid[i][j] == 1:
                return 0
            if i < 0 or j < 0:
                return 0
            if i == 0 and j == 0:
                return 1       
           
            if dp[i][j] != -1:
                return dp[i][j]

            up = f(i - 1, j)
            left = f(i, j - 1)
            
            dp[i][j] = up + left
            return dp[i][j]
        
        return f(m - 1, n )
    
# bottom up solution
# tc - O(m * n), sc - O(m * n)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0 and obstacleGrid[i][j] != 1: 
                    dp[i][j] = 1
                else:
                    up, left = 0, 0
                    if i > 0: up = dp[i - 1][j]
                    if j > 0: left = dp[i][j - 1]
                    dp[i][j] = up + left if not obstacleGrid[i][j] else 0

       # print(dp)
        return dp[- 1][- 1]


# ### DUNGEON GAME

# The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.

# The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

# Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).

# To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

# Return the knight's minimum initial health so that he can rescue the princess.

# Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

# https://leetcode.com/problems/dungeon-game/description/

# insight - we die if health goes below 1 so at every cell (isolated), health should be atleast 
# 1 + (- dungeon[i][j])

# if dungeon[i][j] < 0, then -dungeon[i][j] + 1 is the min health required. 
# if dungeon[i][j] > 0, then we return 1 since we need to find the min health required and not worry
# about excess health

# tc - O(ROWS * COLS), sc - O(ROWS * COLS)
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        ROWS, COLS = len(dungeon), len(dungeon[0])

        @cache
        def f(i, j): 
            #f(i, j) -> returns min health bottom right corner from (i, j)
            if i == ROWS or j == COLS:
                return 1e9
            #reached princess
            if  i == ROWS - 1 and j == COLS - 1:
                return max(1, - dungeon[i][j] + 1)
            
            cameRight = f(i, j + 1)
            cameDown = f(i + 1, j)
            

            return max(1, min(cameDown, cameRight) - dungeon[i][j])
            

        return f(0, 0)









