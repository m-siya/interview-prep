# ### MOST STONES REMOVED WITH SAME ROW OR COLUMN

# On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

# A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

# Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/

class UF:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)
    
    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    
    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)

        if p1 == p2:
            return 0
        
        if self.rank[p1] > self.rank[p2]:
            self.rank[p1] += self.rank[p2]
            self.par[p2] = p1
        else:
            self.rank[p2] += self.rank[p1]
            self.par[p1] = p2
        
        self.n -= 1
        return 1
    
    def isConnected(self):
        return self.n <= 1

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # max num of stones to remove == min number of stones to place?
        # lets assume all the coordinates are vertices of a graph
        # stones are connected if they share the same row/col

        # find min and max coord and make a matrix and add mark stones on that, then do union find

        # striver's impl - treat rows and cols as nodes of graph, not stones

        maxRow, maxCol = 0, 0
        for stone in stones:
            maxRow = max(maxRow, stone[0])
            maxCol = max(maxCol, stone[1])
        
        ds = UF(maxRow + maxCol + 1) # in ds, cols come after rows

        stoneNodes = set() # basically keeps track of which nodes (which are rows and cols in our impl) have stones and 
        # it can be any num of stones

        for stone in stones:
            nodeRow = stone[0]
            nodeCol = stone[1] + maxRow + 1
            ds.union(nodeRow, nodeCol)
            stoneNodes.add(nodeRow)
            stoneNodes.add(nodeCol)

        count = 0

        for stoneNode in stoneNodes:
            if stoneNode == ds.find(stoneNode):
                count += 1
        return len(stones) - count
        




