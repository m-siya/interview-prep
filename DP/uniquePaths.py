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


# You are given an m x n integer array grid. There is a robot initially located at the top-left corner 
# (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot
# can only move either down or right at any point in time.

# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any
# square that is an obstacle.

# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The testcases are generated so that the answer will be less than or equal to 2 * 109.

# https://leetcode.com/problems/unique-paths-ii/description/

#TopDown solution with memoization

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