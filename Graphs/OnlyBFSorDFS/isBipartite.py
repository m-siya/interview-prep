# ### IS GRAPH BIPARTITE

# There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

# There are no self-edges (graph[u] does not contain u).
# There are no parallel edges (graph[u] does not contain duplicate values).
# If v is in graph[u], then u is in graph[v] (the graph is undirected).
# The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
# A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

# Return true if and only if it is bipartite.

# https://leetcode.com/problems/is-graph-bipartite/description/
# recursive dfs sol
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        coloring = [-1] * len(graph)

        coloring[0] = 0

        #self.dfs(graph, coloring, 0)
        #print(coloring)
        for node in range(len(graph)):
            if not self.dfs(graph, coloring, node): return False
        
        return True
        


    def dfs(self, graph, coloring, node):
        for neighbour in graph[node]:
            if coloring[neighbour] == -1:
                coloring[neighbour] = 1 - coloring[node]
                if not self.dfs(graph, coloring, neighbour): return False
            elif coloring[neighbour] == coloring[node]:
                return False
        return True

# bfs sol
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        coloring = [-1] * len(graph)

        coloring[0] = 0

        #self.dfs(graph, coloring, 0)
        #print(coloring)
        for node in range(len(graph)):
            if not self.bfs(graph, coloring, node): return False
        
        return True

    def bfs(self, graph, coloring, node):
        q = deque()
        if coloring[node] == -1:
            coloring[node] = 0
        q.append(node)    

        while q:
            curr_node = q.popleft()
            for neighbour in graph[curr_node]:
                if coloring[neighbour] == -1:
                    coloring[neighbour] = 1 - coloring[curr_node]
                    q.append(neighbour)
                elif coloring[neighbour] == coloring[curr_node]:
                    return False
        return True
                    
