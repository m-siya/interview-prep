# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 
# which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# https://leetcode.com/problems/minimum-path-sum/description/


#Top Down memoization approach
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[-1 for _ in range(n)] for _ in range(m)]

        def f(i: int, j: int) -> int:
            #f(i, j) returns the minimum path sum from 0, 0 to grid[i][j]
            if i == 0 and j == 0:
                return grid[0][0]
            
            if i < 0 or j < 0:
                return int(1e9)

            if dp[i][j] != -1:
                return dp[i][j]

            up = f(i - 1, j)
            left = f(i, j - 1)
            dp[i][j] = grid[i][j] + min(up, left)
            return dp[i][j]
    
        return f(m - 1, n - 1)