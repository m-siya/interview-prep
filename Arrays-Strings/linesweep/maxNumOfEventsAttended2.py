# ### MAXIMUM NUMBER OF EVENTS THAT CAN BE ATTENDED

# You are given an array of events where events[i] = [startDayi, endDayi, valuei]. The ith event starts at startDayi and ends at endDayi, and if you attend this event, you will receive a value of valuei. You are also given an integer k which represents the maximum number of events you can attend.

# You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. Note that the end day is inclusive: that is, you cannot attend two events where one of them starts and the other ends on the same day.

# Return the maximum sum of values that you can receive by attending events.

# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/description/

# the value throws a wrench in the greedy strategy. we need to use DP now

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: (x[0], x[1]))

        dp = [[-1 for _ in range(k + 1)] for _ in range(len(events) + 1)]
        
        @cache
        def f(i, k):
            if k == 0 or i == len(events):
                return 0
            
            if dp[i][k] != -1: return dp[i][k]
            
            start, end, value = events[i][0], events[i][1], events[i][2]

            attend, leave = 0, 0


            # this line finds the next viable event IF we attend the current event i.
            # *useful* so we dont need to keep track of curr_day and dp becomes 2D from 3D
            j = bisect.bisect(events, [end+1])

            attend = value + f(j, k - 1)
            leave = f(i + 1, k)

            dp[i][k] = max(attend, leave)
            return dp[i][k]

        x = f(0, k)
      #  print(dp)
        return x

        