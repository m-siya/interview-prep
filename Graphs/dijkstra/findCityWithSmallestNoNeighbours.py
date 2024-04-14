# ### FIND CITY WITH SMALLEST NUMBER OF NEIGHBOURS AT A THRESHOLD

# There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

# Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

# Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

#  https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/

import heapq as hq
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        neighbours = {i: [] for i in range(n)}

        for i, edge in enumerate(edges):
            neighbours[edge[0]].append((edge[1], edge[2])) #(node, cost)
            neighbours[edge[1]].append((edge[0], edge[2]))

        #print(neighbours)
        def dijkstra(neighbours, source):
            #source is 0 node
            pq = [(0, source)] #dist, node
            min_distances = {}

            visited = set()

            while pq:
                curr_dist, curr = hq.heappop(pq)
                if curr in visited or curr_dist > distanceThreshold: continue

                visited.add(curr)

                for neighbour, dist in neighbours[curr]:
                    if neighbour == source: continue
                    new_dist = curr_dist + dist

                    compare_with = min_distances[neighbour] if min_distances.get(neighbour, None) else float('inf')

                    if  new_dist < compare_with and new_dist <= distanceThreshold:
                        min_distances[neighbour] = new_dist
                        hq.heappush(pq, (new_dist, neighbour))
           # print(min_distances)
            
            return len([node for node in min_distances if node != float('inf')])

        ans = 0
        min_neighbours = float('inf')
        
        for i in neighbours.keys():
            reachable_cities = dijkstra(neighbours, i)
          #  print(reachable_cities, i)
            if reachable_cities < min_neighbours:
                ans = i
                min_neighbours = reachable_cities
            elif reachable_cities == min_neighbours and i > ans:
                ans = i
            else:
                continue
        
        return ans



            
        


        