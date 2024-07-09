# ### NETWORK DELAY TIME

# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
    
# https://leetcode.com/problems/network-delay-time/description/

import heapq as hq
class Solution:
    def dijkstra(self, adjList, s, n):
        visited = set()

        pq = [(s, 0)]

        min_times = [float('inf') for _ in range(n)]
        min_times[s] = 0

        while pq:
            curr_node, curr_time = hq.heappop(pq)

            for neighbour, time in adjList[curr_node]:
                if curr_time + time < min_times[neighbour]:
                    min_times[neighbour] = curr_time + time
                    hq.heappush(pq, (neighbour, curr_time + time))
        

        return min_times

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # edges with weights == times
        # find min time for signal to travel from k to all nodes => dijkstra
        adjList = collections.defaultdict(list)

        for src, dst, time in times:
            adjList[src - 1].append((dst - 1, time))
        
       # print(adjList)
        
        min_times = self.dijkstra(adjList, k - 1, n)
       # print(min_times)
        max_min_time = 0
        for time in min_times:
            if time == float('inf'):
                return -1

            max_min_time = max(max_min_time, time)

        return max_min_time


        





        