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

if a cycle exists in the graph, no topological ordering is possible so, to detect cycle in a DAG, can use topological sort.

### Kahn's Algorithm
to find topological sort using BFS instead of DFS

1. maintain an indegree array such that indegree[i] = k means that indegree of node i is k.
2. first calculate indegree of each node and store in indegree array. 
3. push the node with indegree = 0 to the q. as you pop nodes into the q, add to the answer array.
4. continue with bfs on the node just pushed into the q, and decrease the indegree of each neighbouring node
5. push the node with indegree 0 into the q.

useful when we need to answer 2 questions - 
1. is it possible to have a topological ordering?
2. if yes then print out one of all the orders.

**Note** a DAG has at least one vertex with the indegree as zero and one vertex with outdegree as zero.


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

> There is no cycle of odd length

> we can split the nodes of the graph  into 2 subsets so that there is all the edges go from 1 subset to the other subset.

> The graph should be bi-colourable.