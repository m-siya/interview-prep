# ### PACIFIC ATLANTIC WATER FLOW

# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean 
# touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c]
# represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and
# west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell 
# adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell 
# (ri, ci) to both the Pacific and Atlantic oceans.    

# https://leetcode.com/problems/pacific-atlantic-water-flow/description/

# WARNING -> very inefficient solution but passes on leetcode

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        reach_pacific = set()
        reach_atlantic = set()
        

        def can_reach_pacific(r, c, path):
            if r == ROWS or c == COLS or (r, c) in path:
                return False

            if r == 0 or c == 0:
                return True

            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (row == ROWS or col == COLS) or heights[row][col] > heights[r][c]: continue
                if can_reach_pacific(row, col, path | {(r, c)}):
                    return True

            return False

        def can_reach_atlantic(r, c, path):
            if r < 0 or c < 0 or (r, c) in path:
                return False

            if r == ROWS - 1 or c == COLS - 1:
                return True

            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (row < 0 or col < 0) or heights[row][col] > heights[r][c]: continue
                if can_reach_atlantic(row, col, path | {(r, c)}):
                    return True
            
            return False


        for r in range(ROWS):
            for c in range(COLS):
                if can_reach_pacific(r, c, set()) and can_reach_atlantic(r, c, set()):
                    reach_pacific.add((r, c))

        #print(reach_atlantic)
        return reach_pacific

# where i went wrong - what path is doing is  keep a track of all the cells visited from a node (r, c). and at the end of the path
# essentially lies the atlantic or pacific ocean depending on the dfs func. so 
# so if i can reach a cell r', c' from r, c and r', c' can reach a or p ocean then i add r, c to set of points that can 
# reach an ocean. But, r', c' is not being added which is adding quite a bit of redundancy to this code.

# let's go about this in the opposite direction. Instead of considering the cells which can receive water from (r, c), cosnider
# cells from which r, c can receive water.
# so 

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        reach_pacific = set()
        reach_atlantic = set()
        

        def dfs(r, c, path):
            path.add((r, c))
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if row < 0 or col < 0 or row == ROWS or col == COLS or heights[row][col] < heights[r][c] or (row, col) in path:
                    continue
                dfs(row, col, path)

        
        for r in range(ROWS):
            dfs(r, 0, reach_pacific)
            dfs(r, COLS - 1, reach_atlantic)
        
        for c in range(COLS):
            dfs(0, c, reach_pacific)
            dfs(ROWS -1, c, reach_atlantic)

        #print(reach_atlantic)
        return reach_pacific & reach_atlantic
                

            
            


        



        
        





            
            


        



        
        




