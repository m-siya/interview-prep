# ### 2192. All Ancestors of a Node in a Directed Acyclic Graph

# You are given a positive integer n representing the number of nodes of a Directed Acyclic Graph (DAG). The nodes are numbered from 0 to n - 1 (inclusive).

# You are also given a 2D integer array edges, where edges[i] = [fromi, toi] denotes that there is a unidirectional edge from fromi to toi in the graph.

# Return a list answer, where answer[i] is the list of ancestors of the ith node, sorted in ascending order.

# A node u is an ancestor of another node v if u can reach v via a set of edges.

# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/description/

class Graph:
    def __init__(self, n, edges):
        self.indegree = [0] * n
        self.adjList = collections.defaultdict(list)

        for edge in edges:
            v1, v2 = edge[0], edge[1]
            self.adjList[v1].append(v2)
            self.indegree[v2] += 1

class Solution:
    def topSort(self, n, graph):
        ans = collections.defaultdict(set)
        indegree = graph.indegree

        S = collections.deque([i for i in range(n) if indegree[i] == 0])

        while S:
            n = S.pop()

            for m in graph.adjList[n]:
                indegree[m] = indegree[m] - 1
                # there is edge from n to m
                ans[m].add(n)

                if indegree[m] == 0:
                    S.append(m)

                for j in ans[n]:
                    # is there is an edge from j to m, and an edge from n to m, there is a path from m to j
                    ans[m].add(j)
        return ans

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        # make graph
        g = Graph(n, edges)

        ans = self.topSort(n, g)

        return [sorted(ans[i]) for i in range(n)]
         
        