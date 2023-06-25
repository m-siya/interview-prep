### BRICK WALL

# There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of 
# bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each 
# row is the same.

# Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge 
# of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical
# edges of the wall, in which case the line will obviously cross no bricks.

# Given the 2D array wall that contains the information about the wall, return the minimum number of crossed 
# bricks after drawing such a vertical line.

# https://leetcode.com/problems/brick-wall/description/

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        wallWidth = sum(wall[0])

        pos_map = defaultdict(int)


        for row in wall:
            pos = 0
            for brick in row[:-1]:
                pos += brick
                pos_map[pos] += 1
        
        min_hits = len(wall) - max(pos_map.values(), default = 0)
        return min_hits




