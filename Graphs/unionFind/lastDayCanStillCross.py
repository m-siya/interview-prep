# ### LAST DAY WHEN YOU CAN STILL CROSS

# There is a 1-based binary matrix where 0 represents land and 1 represents water. You are given integers row and col representing the number of rows and columns in the matrix, respectively.

# Initially on day 0, the entire matrix is land. However, each day a new cell becomes flooded with water. You are given a 1-based 2D array cells, where cells[i] = [ri, ci] represents that on the ith day, the cell on the rith row and cith column (1-based coordinates) will be covered with water (i.e., changed to 1).

# You want to find the last day that it is possible to walk from the top to the bottom by only walking on land cells. You can start from any cell in the top row and end at any cell in the bottom row. You can only travel in the four cardinal directions (left, right, up, and down).

# Return the last day where it is possible to walk from the top to the bottom by only walking on land cells.

# https://leetcode.com/problems/last-day-where-you-can-still-cross/description/

## new concept - add a node each for start and end and connect it to all top and bottom cells respectively


class UF:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)

        if p1 == p2:
            return
        
        if self.rank[p1] > self.rank[p2]:
            self.rank[p1] += self.rank[p2]
            self.par[p2] = p1
        else:
            self.rank[p2] += self.rank[p1]
            self.par[p1] = p2
        
        self.n -= 1
        return 

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        grid = [[1 for _ in range(col)] for _ in range(row)]
        ds = UF(row * col + 2) # add two nodes at end and start for top and bottom rows

        for i in range(len(cells) - 1, -1, -1):
            r, c = cells[i][0] - 1, cells[i][1] - 1
           # print(r, c)
            grid[r][c] = 0
            index = r * col + c + 1 # shift by 1 for the top node

            if r - 1 >= 0 and grid[r - 1][c] == 0:
                ds.union(index, index - col)
            if c - 1 >= 0 and grid[r][c - 1] == 0:
                ds.union(index, index - 1)
            if r + 1 < row and grid[r + 1][c] == 0:
                ds.union(index, index + col)
            if c + 1 < col and grid[r][c + 1] == 0:
                ds.union(index, index + 1)
            
            if r == 0: 
                ds.union(0, index)
            if r == row - 1:
                ds.union(row * col + 1, index)

            if ds.find(0) == ds.find(row * col + 1):
                return i

        return 0

        