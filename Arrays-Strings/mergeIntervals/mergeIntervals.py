# ### MERGE INTERVALS

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

# https://leetcode.com/problems/merge-intervals/description/

# sort intervals in increasing order of start position
# scan sorted intervals and maintain active set for overlapping intervals. 
# if curr.start < prev.end, merge, update active set
# if no overlap, renew active set


# tc - O(nlogn), sc - O(n) [to store answer]

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])

        answer = []
        prev_start, prev_end = -1, -1
        for interval in intervals:
            start, end = interval
            if start <= prev_end:
                prev_end = max(prev_end, end)
            
            else:
                if prev_start != -1 and prev_end != -1:
                    answer.append([prev_start, prev_end])
                prev_start, prev_end = start, end

        answer.append([prev_start, prev_end])
        return answer


