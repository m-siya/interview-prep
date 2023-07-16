# ### LONGEST INCREASING PATH IN A MATRIX

# Given an m x n integers matrix, return the length of the longest increasing path in matrix.

# From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or
# move outside the boundary (i.e., wrap-around is not allowed).

# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/


# method - naive dfs
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        max_path_len = 0

        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(r, c, curr_path_len):
            nonlocal max_path_len
            max_path_len = max(max_path_len, curr_path_len)

            for dr, dc in directions:
                row, col = r + dr, c + dc
                if row < 0 or col < 0 or row == ROWS or col == COLS or matrix[row][col] <= matrix[r][c] :
                    continue
                
                dfs(row, col, curr_path_len + 1)
        

        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, 1)
                if max_path_len == ROWS * COLS:
                    return max_path_len
        
        return max_path_len


# method - Top Down DP
# notes - no need to use visited here since by the nature of a longest increasing path, we will not be able to visit
# a node again that has already been convered by the current path.

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        max_path_len = 0

        memo = [[-1 for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(r, c):
            if memo[r][c] != -1:
                return memo[r][c]

            max_path_len_gain = 0

            for dr, dc in directions:
                row, col = r + dr, c + dc
                if row < 0 or col < 0 or row == ROWS or col == COLS or matrix[row][col] <= matrix[r][c]:
                    continue
      
                max_path_len_gain = max(max_path_len_gain, dfs(row, col))
        
            memo[r][c] = 1 + max_path_len_gain
            return memo[r][c]
            
  

        for i in range(ROWS):
            for j in range(COLS):
                max_path_len = max(max_path_len, dfs(i, j))
        
        return max_path_len

# method - topological sort with BFS

# each cell in the matrix is a node and there exists an edge from node x to node y if x.val < y.val

# there can be no cycles in the graph since a (<) relation is not symmetric or reflexive
# so this is a DAG

# use topological sort while counting the levels

# the for loop in the q is necessary to ensure each 'level' in bfs accounts for an increment of 1 in path len

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        indegree = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row < 0 or col < 0 or row == ROWS or col == COLS:
                        continue
                    
                    if matrix[row][col] < matrix[r][c]:
                        indegree[r][c] += 1
                
                if indegree[r][c] == 0:
                    q.append((r, c))
        
        max_path_len = 0
        while q:
            print(q)

            q_len = len(q)

            for _ in range(q_len):
                r, c = q.popleft()
            
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row < 0 or col < 0 or row == ROWS or col == COLS:
                        continue
                    #edge from r, c to row, col
                    if matrix[r][c] < matrix[row][col]:
                        indegree[row][col] -= 1

                        if indegree[row][col] == 0:
                            q.append((row, col))

            max_path_len += 1
        
        return max_path_len






        





        
