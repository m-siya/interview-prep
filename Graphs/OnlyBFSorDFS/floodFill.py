### FLOOD FILL

# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the 
# pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel 
# of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

# Return the modified image after performing the flood fill.

# https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, grid: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(grid), len(grid[0])

        prev_color = grid[sr][sc]

        if prev_color != color:
            q = deque()
            q.append((sr, sc))
        #grid[sr][sc] = color
        
            directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

            while q:
                r, c = q.popleft()
                grid[r][c] = color
                for dr, dc in directions:
                    #print(row, col)
                    row, col = r + dr, c + dc
                    # if (row < 0 or row == ROWS or 
                    #     col < 0 or col == COLS or
                    #     grid[row][col] != prev_color):
                    #     continue
                    if 0 <= row and row < ROWS and 0 <= col and col < COLS and grid[row][col] == prev_color: 
                        q.append((row, col))

        return grid
