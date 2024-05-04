# ### NON OVERLAPPING INTERVALS 

# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# https://leetcode.com/problems/non-overlapping-intervals/description/


# if iterating from start to end, sorting on basis of end time makes sense. 
# this is because u first want to get all the events that end the earliest leaving the 
# most time left to schedule events. this is the greedy strategy

# tc: O(nlogn)
# sc: O(1)

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x: x[1])

        last_event_end = intervals[0][1]

        to_remove = 0

        for interval in intervals[1:]:
            start, end = interval[0], interval[1]

            if start < last_event_end:
                to_remove += 1
            else:
                last_event_end = end
        
        return to_remove


        

