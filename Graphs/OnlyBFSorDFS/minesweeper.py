# ### MINESWEEPER

# https://leetcode.com/problems/minesweeper/description/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        r, c = click

        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board

        else:
            self.revealBlank(board, r, c)

        return board

    
    def revealBlank(self, grid, r, c):
        ROWS, COLS = len(grid), len(grid[0])

        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        bomb_count = 0
        for dr, dc in directions:
            row, col = r + dr, c + dc
            if row < 0 or col < 0 or row == ROWS or col == COLS:
                continue
            
            if grid[row][col] == 'M':
                bomb_count += 1
        

        if not bomb_count: 
            #grid[r][c] = bomb_count
            grid[r][c] = 'B'
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if row < 0 or col < 0 or row == ROWS or col == COLS or grid[row][col] in 'MBX' or grid[r][c].isnumeric():
                    continue

                self.revealBlank(grid, row, col)
        else:
            grid[r][c] = str(bomb_count)
            

