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

    def minPathSum_BU(self, grid: List[List[int]]) -> int:
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
   
##TRIANGLE MIN PATH SUM

# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More 
# formally, if you are on index i on the current row, you may move to either index i or
#  index i + 1 on the next row.

# https://leetcode.com/problems/triangle/description/ 


# Notes - fixed starting point but no fixed destination

#top down solution recursive using memoization
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rowNo = len(triangle)
        dp = [[-1 for _ in range(i + 1)] for i in range(rowNo)]
        #print(dp)

        def f(row: int, i: int) -> int:
            #f(row, i) gives the min path sum from top to ith number of 
            #row
            if row == 0:
                return triangle[0][0]
            if i < 0 or i >= len(triangle[row]):
                return int(1e9)

            if dp[row][i] != -1:
                return dp[row][i]
            up = f(row - 1, i)
            diagonal = f(row - 1, i - 1)
            #print(row, i)
            dp[row][i] = triangle[row][i] + min(up, diagonal)
            return dp[row][i]

        minSum = int(1e9)
        for index, num in enumerate(triangle[rowNo - 1]):
            minSum = min(minSum, f(rowNo - 1, index))
        
        return minSum
    
## MINIMUM FALLING PATH SUM
# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

# A falling path starts at any element in the first row and chooses the element in the next row that is 
# either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be 
# (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

# https://leetcode.com/problems/minimum-falling-path-sum/


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        def f(i: int, j: int) -> int:
            #f(i, j) gives the minimum path sum from start to matrix[i][j]
            if i < 0 or j < 0 or j >= len(matrix[0]):
                return int(1e9)
            
            if i == 0:
                return matrix[i][j]

            goUp = f(i - 1, j)
            goDRight = f(i - 1, j + 1)
            goDLeft = f(i - 1, j - 1)
            return matrix[i][j] + min(goUp, goDRight, goDLeft)

        
        min_falling_path = int(1e9)
        for j in range(n):
            min_falling_path = min(min_falling_path, f(m - 1, j))


        return min_falling_path
    

