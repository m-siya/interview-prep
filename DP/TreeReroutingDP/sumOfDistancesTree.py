# ### SUM OF DISTANCES IN TREE

# There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

# You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

# Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

# https://leetcode.com/problems/sum-of-distances-in-tree/description/


#bfs sol 
# TC: O(N^2)
# SC: O(N)

from collections import defaultdict
from collections import deque
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        def f(root):
            q = deque()
            q.append((root, -1, 0))
            total_dist = 0

            while q:
                curr, prev, dist = q.popleft()
                total_dist += dist

                for neighbour in adj[curr]:
                    if (prev != -1 and neighbour != prev) or prev == -1:
                        q.append((neighbour, curr, dist + 1))
        

            return total_dist

        lengths = []

        for node in range(n):
            lengths.append(f(node))
        
        return lengths

 
# TC: O(N)
# SC: O(N)
from collections import defaultdict
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        res = [0] * n #store the answer
        count = [0] * n #number of nodes in each subtree routed by ith indx (includes root as well)
        
        # f(root) -> return distances to every node in subtree routed by it

        def find_info(root, prev):    
            for neighbour in adj[root]:
                if neighbour != prev:
                    find_info(neighbour, root)
                    count[root] += count[neighbour]
                    res[root] += res[neighbour] + count[neighbour]
            count[root] += 1
        
        def calculate_others(root, prev):
            for neighbour in adj[root]:
                if neighbour != prev:
                    res[neighbour] = res[root] - count[neighbour] + (n - count[neighbour])
                    calculate_others(neighbour, root)

     
        find_info(0, -1)
        calculate_others(0, -1)
        return res





        