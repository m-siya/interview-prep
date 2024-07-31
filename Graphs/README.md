## Algorithms

### Flood Fill

like the bucket tool in paint programs. 
1. Take the position of the starting point.
2. Decide wether you want to go in 4 directions (N, S, W, E) or 8 directions (N, S, W, E, NW, NE, SW, SE).
3. Choose a replacement color and a target color.
4. Travel in those directions.
5. If the tile you land on is a target, reaplce it with the chosen color.
6. Repeat 4 and 5 until you’ve been everywhere within the boundaries.

[code](floodFill.py)


### Topological Sort
only for directed acyclic graphs.

The topological sorting of a directed acyclic graph is nothing but the linear ordering of vertices such that if there is an edge between node u and v(u -> v), node u appears before v in that ordering.

1. dfs on graph
2. maintain a stack. in each dfs call, after all the neighbouring nodes of the current node are visited, push current node to stack.
3. stack contains the topological ordering

- if a cycle exists in the graph, no topological ordering is possible so, to detect cycle in a DAG, can use topological sort.

- since a DAG has no cycle, it only contains finite paths. That means there is atleast one path of largest length. 



### Kahn's Algorithm
to find topological sort using BFS instead of DFS

1. maintain an indegree array such that indegree[i] = k means that indegree of node i is k.
2. first calculate indegree of each node and store in indegree array. 
3. push the node with indegree = 0 to the q. as you pop nodes from the q, add to the answer array.
4. continue with bfs on the node just pushed into the q, and decrease the indegree of each neighbouring node
5. push the node with indegree 0 into the q.

useful when we need to answer 2 questions - 
1. is it possible to have a topological ordering?
2. if yes then print out one of all the orders.

**Note** 
    - a DAG has at least one vertex with the indegree as zero and one vertex with outdegree as zero.

    - time complexity is O(V + E). 

**Code**
```Python
from collections import deque
def TopologicalSort(graph, n):
 
    # list to store the sorted elements
    L = []
 
    # get in-degree information of the graph
    indegree = graph.indegree
 
    # Set of all nodes with no incoming edges
    S = deque([i for i in range(n) if indegree[i] == 0])
 
    while S:
        # remove node `n` from `S`
        n = S.pop()
 
        # add `n` at the tail of `L`
        L.append(n)
 
        for m in graph.adjList[n]:
            # remove an edge from `n` to `m` from the graph
            indegree[m] = indegree[m] - 1
 
            # if `m` has no other incoming edges, insert `m` into `S`
            if indegree[m] == 0:
                S.append(m)
 
    # if a graph has edges, then the graph has at least one cycle
    for i in range(n):
        if indegree[i]:
            return None
 
    return L
```

### Disjoint Set (Union Find)
Resources 
- https://takeuforward.org/data-structure/disjoint-set-union-by-rank-union-by-size-path-compression-g-46/
- https://www.youtube.com/watch?v=aBxjDBC4M1U

Problem Statement - given 2 components of an undirected graph, find if node m and node n are in the same component or not

This can be solved by BFS/DFS (O(V + E)) too but by disjoint set, takes constant time (O(1))

Usually used for dynamic (or constantly changing graphs)

ADT Functionalities :
1. Find parent of a node
2. Union (add edge between 2 nodes) 
    - Union by Rank
    - Union by Size

#### Union by Rank
1. Rank - distance between node and furthest leaf nodek

2. Ultimate Parent - root node

**Algorithm**
1. init rank array with 0, init parent array with node value. parent[i] = i

2. find ultimate parent of u and v, let pu and pv.

3. find rank of pu and pv

4. connect ultimate parent with smaller rank to other ultimate parent with larger rank.


Union(u, v)
1. find ultimate parent of u and v -> pu and pv
2. find rank of pu and pv
3. connect smaller rank to larger rank always

Find_Parent(u, v)
1. find ultimate parent of u and v.
2. if same, then u and v belong to the same component, else different components

by applying union by rank, this takes O(logn) time.

path compression - once you get ultimate parent of a node then just update its parent. then the next time, you dont have to go up the whole chain. this reduces the time complexity and tc becomes amortized O(1). 
                - do not change rank during path compression. rank is not equivalent to height. hence, height changes during path compression but rank does not.

**Why connect smaller to larger**
height of smaller component increases and consequently, the time needed to find ultimate parent also increases (since it depends on the heights of the trees)

```Python
class DisjointSet:
    def __init__(self, n: int):
        self.rank = [0] * (n + 1)
        self.parent = [i for i in range(n + 1)]

    def find_ult_parent(self, node: int):
        if (u == parent[u]):
            return u
        
        return parent[u] = self.find_ult_parent(parent[u])

    def union_by_rank(u: int, v: int):
        ult_parent_u = self.find_ult_parent(u)
        ult_parent_v = self.find_ult_parent(v)

        if ult_parent_u == ult_parent_v: return

        if rank[ult_parent_u] < rank[ult_parent_v]:
            #smaller attached to larger
            parent[ult_parent_u] = ult_parent_v
        elif rank[ult_parent_v] < rank[ult_parent_u]:
            parent[ult_parent_v] = ult_parent_u
        else:
            parent[ult_parent_v] = ult_parent_u
            rank[ult_parent_u] += 1
```

#### Union by Size
1. keep a size array instead of rank array

```Python
def __init__(self, n: int):
    size = [1] * (n + 1)

def union_by_size(self, u: int, v: int):
    ult_parent_u = self.find_ult_parent(u)
    ult_parent_v = self.find_ult_parent(v)

    if ult_parent_u == ult_parent_v: return

    if size[ult_parent_u] < size[ult_parent_v]:
        parent[ult_parent_u] = ult_parent_v
        size[ult_parent_v] += size[ult_parent_u]
    else:
        parent[ult_parent_v] = ult_parent_u
        size[ult_parent_u] += size[ult_parent_v]
```
---------------------------

## Tips
1. DFS vs BFs

|DFS |BFS|
|---|---|
|exhaust all possibilities and check which is best (think dp)|shortest path from source to dest|
|count all paths b/w source and dest|if there exists a path b/w nodes|
||will give the shortest path. usually much more efficient to find shortest path|


2. in BFS, if you need to iterate levelwise and find shortest path, you need a for loop to iterate through the length of the q. eg - [link](OnlyBFSorDFS\wordLadder.py)

3. Equivalent definitions of a bipartite graph:

    - There is no cycle of odd length

    - we can split the nodes of the graph  into 2 subsets so that there is all the edges go from 1 subset to the other subset.

    - The graph should be bi-colourable.

### Dijkstra
- for a weighted, undirected, connected graph with no negative weight cycle
- find shortest distancd of all vertices from source vertex S.
- will fall in infinite loop if negative cycle
- can apply dijkstra to every node to achieve same functionality as floyd warshall but fails for negative cycles


**Code**
```Python
import heapq as hq
#neighbours = {node: [(neighbour, cost)]}
def dijkstra(neighbours):
    #source is 0 node
    pq = [(0, 0)] #node, dist
    min_distances = [float('inf')] * len(neighbours)

    while pq:
        curr, curr_dist = hq.heappop(pq)

        for neighbour, dist in neighbours[curr]:
            if (curr_dist + dist < min_distances[neighbour]):
                min_distances[neighbour] = curr_dist + dist
                hq.heappush(pq, (neighbour, curr_dist + dist))
    
    return min_distances
```

### Floyd Warshall Algorithm

- multi source shortest path algorithm

- thought process - for a source A and dest B, go via every node and get shortest path - min(d[A][k] + d[k][B]) for all k in nodes

- also helps to detect negative cycles -> if cost of any node d[i][i] < 0, then it means there is a negative cycle

- TC - O(n^3), SC - O(n^2) because we use the 2d cost matrix

```python
def floyd_warshall(matrix: List[List[int]]) -> int:
    n = len(matrix)

    # assuming weight matrix with edges cost filled out and wherever no edge, then 1e9 and matrix[i][i] == 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
    
    # check negative cycle
    for i in range(n):
        if matrix[i][i] < 0:
            print("negative cycle found")
```

