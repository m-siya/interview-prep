# ### MAXIMUM NUMBER OF EDGES WE CAN REMOVE

# Alice and Bob have an undirected graph of n nodes and three types of edges:

# Type 1: Can be traversed by Alice only.
# Type 2: Can be traversed by Bob only.
# Type 3: Can be traversed by both Alice and Bob.
# Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

# Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.

# https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/description/

class UF:
    def __init__(self, n):
        self.n = n #num of components
        self.par = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1) # size

    #find parent
    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    
    # return 1 if success, 0 otherwise
    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2: # if same parent
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
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # how to know if A/B can traverse a graph fully? bfs visits all nodes
        # possible sol - iterate through all edges and check if can be removed or not. but will order of iteration matter? 
        alice, bob = UF(n), UF(n)
        count = 0 #edges we are keeping

        for t, src, dst in edges:
            if t == 3:
                count += (alice.union(src, dst) | bob.union(src, dst)) # no need to keep all green edges also
        
        for t, src, dst in edges:
            if t == 1:
                count += alice.union(src, dst)
            elif t == 2:
                count += bob.union(src, dst)
        
        if bob.isConnected() and alice.isConnected():
           # print(len(edges), count)
            return len(edges) - count
        
        else:
            return -1