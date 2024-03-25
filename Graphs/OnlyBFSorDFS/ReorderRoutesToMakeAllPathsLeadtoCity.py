# 1466. Reorder Routes to Make All Paths Lead to the City Zero


# There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

# Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

# This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

# Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

# It's guaranteed that each city can reach city 0 after reorder.

# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/

# TC: O(n) because we only visit each node once
# SC: O(n) due to recursion + edges + neighbours
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        #propagate changes outwards starting from 0

        edges = {(a, b) for a, b in connections }
        neighbours = {city: [] for city in range(n)}

        changes = 0

        for a, b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)
        
      #  print(neighbours)
        
        def dfs(i, prev):
            nonlocal changes
            for neighbour in neighbours[i]:
                if neighbour == prev: continue
                if (neighbour, i) not in edges: 
                    changes += 1
                #print(i, neighbour, prev, changes)
                dfs(neighbour, i)

        dfs(0, 0)
        return changes
        