# You are given a list of bombs. The range of a bomb is defined as the area where its effect
# can be felt. This area is in the shape of a circle with the center as the location of the bomb.

# The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri].
# xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes 
# the radius of its range.

# You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that
# lie in its range. These bombs will further detonate the bombs that lie in their ranges.

# Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to 
# detonate only one bomb.

# https://leetcode.com/problems/detonate-the-maximum-bombs/description/

# procedure -> think of the bombs as nodes in a graph with directed edges towards bombs they can detonate upon 
#their own detonation.
# then do dfs/bfs on the adjancency matrix/list and the node  from which most other nodes are reachable is the ans.

from collections import deque
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj_map = {}

        for index, bomb in enumerate(bombs):
            x_0, y_0, r  = bomb[0], bomb[1], bomb[2]
            for other_index, other_bomb in enumerate(bombs):
                x, y = other_bomb[0], other_bomb[1]
                if (x - x_0) ** 2 + (y - y_0) ** 2 <= r ** 2:
                    if index in adj_map: 
                        adj_map[index].append(other_index)
                    else:
                        adj_map[index] = [other_index]


        #print(adj_map)

        #now do bfs
        def bfs(node):
            visited = set()
            queue = deque()
            queue.append(node)
            visited.add(node)

            while queue:
            # count = 0
            # while count < 5:
                curr = queue.popleft()
                for neighbour in adj_map[curr]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
               # count += 1


            return len(visited)
        
        max_detonated = 0
        for index in range(len(bombs)):
            max_detonated = max(max_detonated, bfs(index))
        
        return max_detonated


            

    

