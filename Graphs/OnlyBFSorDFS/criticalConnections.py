# ### CRITICAL CONNECTIONS

# There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

# A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

# Return all critical connections in the network in any order.

 
# https://leetcode.com/problems/critical-connections-in-a-network/description/
# After the DFS for any adjacent node gets completed, we will just check if the edge,
#  whose starting point is the current node and ending point is that adjacent node,
#  is a bridge. For that, we will just check if any other path from the current node to 
# the adjacent node exists if we remove that particular edge. If any other alternative 
# path exists, this edge is not a bridge. Otherwise, it can be considered a valid bridge.

from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # An edge is a critical connection, if and only if it is not in a cycle.
        # critical connections are called bridges.

        adj = defaultdict(list)

        for src, dest in connections:
            adj[src].append(dest)
            adj[dest].append(src)

        
        visited = [False] * n
        timeInsertion = [0] * n
        lowestTime = [0] * n
        timer = 1
        bridges = []

        def dfs(node, parent):
            nonlocal timer
            visited[node] = True
            timeInsertion[node] = lowestTime[node] = timer
            timer += 1

            for neighbour in adj[node]:
                if neighbour == parent: continue

                if not visited[neighbour]:
                    dfs(neighbour, node)
                    lowestTime[node] = min(lowestTime[node], lowestTime[neighbour])

                    if lowestTime[neighbour] > timeInsertion[node] :
                        #lowestTime[neighbour] < timeInsertion[node] means we saw this neighbour before also through some other path than through node => must not be a bridge edge
                        bridges.append([node, neighbour])
                else:
                    lowestTime[node] = min(lowestTime[node], lowestTime[neighbour])
        
        dfs(0, -1)

        return bridges
        