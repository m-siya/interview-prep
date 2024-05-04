### MAXIMUM NUMBER OF EVENTS THAT CAN BE ATTENDED

# You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

# You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.

# # Return the maximum number of events you can attend.

# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

from collections import defaultdict
import heapq as hq
# different from max num of meetings/classes u can do because in them you need to attend the whole 
# event/class/meeting but here we will attend each event for one day only. so pick the events as they come

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: (x[0], x[1]))

    #    print(events)

        pq = []

        count = 0
        curr_day = events[0][0]
        i = 0
        while not(i == len(events) and not pq) and curr_day <= 100000:

            while i < len(events) and events[i][0] == curr_day:
                event = events[i]
                hq.heappush(pq, (event[1], event))
                i += 1
              # print(curr_day, pq)

            while pq:
                dur, event = hq.heappop(pq)
                if event[0] <= curr_day <= event[1]:
                    count += 1
                    break
                
                
            curr_day += 1

        return count


        

        