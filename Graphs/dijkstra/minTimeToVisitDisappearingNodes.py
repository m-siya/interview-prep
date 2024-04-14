# ### MINIMUM TIME TO VISIT DISAPPEARING NODES

# There is an undirected graph of n nodes. You are given a 2D array edges, where edges[i] = [ui, vi, lengthi] describes an edge between node ui and node vi with a traversal time of lengthi units.

# Additionally, you are given an array disappear, where disappear[i] denotes the time when the node i disappears from the graph and you won't be able to visit it.

# Notice that the graph might be disconnected and might contain multiple edges.

# Return the array answer, with answer[i] denoting the minimum units of time required to reach node i from node 0. If node i is unreachable from node 0 then answer[i] is -1.

# https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/description/

import heapq as hq
class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        neighbours = {i: [] for i in range(n)}

        for i, edge in enumerate(edges):
            neighbours[edge[0]].append((edge[1], edge[2])) #(node, cost)
            neighbours[edge[1]].append((edge[0], edge[2]))

      #  print(neighbours)
        visited = set()

        def dijkstra(neighbours):
            #source is 0 node
            pq = [(0, 0)] #dist, node
            min_distances = [float('inf')] * len(neighbours)
            min_distances[0] = 0

            while pq:
                curr_dist, curr = hq.heappop(pq)
                if curr in visited: continue
                visited.add(curr)

                if curr_dist >= disappear[curr]: continue # do not process node which already disappeared

                for neighbour, dist in neighbours[curr]:

                    new_dist = curr_dist + dist
                    if  new_dist < min_distances[neighbour] and new_dist < disappear[neighbour]:
                        min_distances[neighbour] = new_dist
                        hq.heappush(pq, (new_dist, neighbour))
            
            for d in range(len(min_distances)):
                if min_distances[d] == float('inf'):
                    min_distances[d] = -1
            
            return min_distances
        
        return dijkstra(neighbours)
        

        

        

        