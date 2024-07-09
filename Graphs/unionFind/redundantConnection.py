# ## REDUNDANT CONNECTION

# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

# https://leetcode.com/problems/redundant-connection/description/

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
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.rank[p1] += self.rank[p2]
            self.par[p2] = p1
        else:
            self.rank[p2] += self.rank[p1]
            self.par[p1] = p2
        
        self.n -= 1
        return True
    
    def isConnected(self):
        return self.n <= 1


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = 0
        for edge in edges:
            v1, v2 = edge[0], edge[1]
            n = max(n, v1, v2)
        
        #print(n)
        ds = UF(n)

        for edge in edges:
            v1, v2 = edge[0] - 1, edge[1] - 1

            if not ds.union(v1, v2):
                return edge
        

## REDUNDANT CONNECTION 2

# In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

# The given input is a directed graph that started as a rooted tree with n nodes (with distinct values from 1 to n), with one additional directed edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.

# The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [ui, vi] that represents a directed edge connecting nodes ui and vi, where ui is a parent of child vi.

# Return an edge that can be removed so that the resulting graph is a rooted tree of n nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.

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
            return False # redundant connection
        if self.rank[p1] > self.rank[p2]:
            self.rank[p1] += self.rank[p2]
            self.par[p2] = p1
        else:
            self.rank[p2] += self.rank[p1]
            self.par[p1] = p2
    
        self.n -= 1
        return True
    
    def isConnected(self):
        return self.n <= 1

class Solution:
    def detectCycle(self, n, edges, skipEdge):
        ds = UF(n + 1)

        for edge in edges:
            if edge == skipEdge: continue
            if not ds.union(edge[0], edge[1]): return edge
        
        return []

    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        # for invalid tree structure but from which an edge ca
            #node has 2 parents 
            #circle

        n = len(edges)
        indegrees = [0] * (n + 1)
        hasTwoIndegrees = -1
        for edge in edges:
            v1, v2 = edge[0], edge[1]

            indegrees[v2] += 1
            
            if indegrees[v2] == 2:
                hasTwoIndegrees = v2
                break
        
        if hasTwoIndegrees == -1:
            return self.detectCycle(n, edges, [])
        
        for i in range(n - 1, -1, -1):
            if edges[i][1] == hasTwoIndegrees:
                if not self.detectCycle(n, edges, edges[i]):
                    # if without this edge, there is no cycle then lets remove this one only
                    return edges[i]




        

