# ### CHECK EXISTENCE OF PATH LIMITED GRAPH

# An undirected graph of n nodes is defined by edgeList, where edgeList[i] = [ui, vi, disi] denotes an edge between nodes ui and vi with distance disi. Note that there may be multiple edges between two nodes.

# Given an array queries, where queries[j] = [pj, qj, limitj], your task is to determine for each queries[j] whether there is a path between pj and qj such that each edge on the path has a distance strictly less than limitj .

# Return a boolean array answer, where answer.length == queries.length and the jth value of answer is true if there is a path for queries[j] is true, and false otherwise.

# https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/description/

class UF:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)
    
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
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # for each query - check all paths between start and end
        # there must be one path such that all edges on path dist < limit => if we always choose the min weight edge, and that doesnt fit the bill, we can be sure that others wont too
        # so now there is only path between 2 nodes, that of min weight edges
        # brute force - for each query, do bfs and check if a path exists between 2 nodes
        # better sol - sort each query acc to limit and each edge acc to dist. then do dsu 
        # checking if path exists using dsu - start connecting edges, if start and end are connected, then path exists

        new_q = []
        for i in range(len(queries)):
            nq = queries[i]
            nq.append(i)
            new_q.append(nq)

      #  print(new_q)

        new_q.sort(key=lambda x: x[2])
        edgeList.sort(key=lambda x: x[2])

        ds = UF(n)
        edge_i = 0

        ans = [None] * len(queries)
        for q in new_q:
            start, end, limit, idx = q[0], q[1], q[2], q[3]


            while edge_i < len(edgeList) and edgeList[edge_i][2] < limit:
                src, dest, dist = edgeList[edge_i][0], edgeList[edge_i][1], edgeList[edge_i][2]
                ds.union(src, dest)

                edge_i += 1
            
            if ds.find(start) == ds.find(end):
                ans[idx] = True
            else:
                ans[idx] = False
        
        return ans
