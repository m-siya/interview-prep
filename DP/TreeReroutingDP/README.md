## TREE REROOTING DP

Given a tree of n vertices with n - 1 edges, each vertex of the tree has a value a assigned to it. 
Let dist(x, y) be the distance between the vertices x and y. the distance between the edges is the number of edges on the simple path between them.

Let's define the cost of the tree as the following value: 

Sum over i  dist(i, v). ai.       for some vertex v

find maximum possible cost of the tree.

solve such problems in O(n) using re rooting dp.

- do two dps
- in dp1 calculate all the sub answers or any other value u need
- in dp2, calculate dp2

example 
```python
from collections import defaultdict
from collections import deque
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
                    res[root] += res[neighbour] + count[neighbour] #add subanswer to subtrees rooted by child nodes + count of child nodes
            count[root] += 1

        # when we move from parent to child we are moving 1 step closer to all the child nodes and 1 step away from the parent nodes.
        
        def calculate_others(root, prev):
            for neighbour in adj[root]:
                if neighbour != prev:
                    res[neighbour] = res[root] - count[neighbour] + (n - count[neighbour])
                    calculate_others(neighbour, root)

     
        find_info(0, -1)
        calculate_others(0, -1)
        return res
```