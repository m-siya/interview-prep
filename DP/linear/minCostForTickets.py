# ### MINIMUM COST FOR TICKETS

# You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

# Train tickets are sold in three different ways:

# a 1-day pass is sold for costs[0] dollars,
# a 7-day pass is sold for costs[1] dollars, and
# a 30-day pass is sold for costs[2] dollars.
# The passes allow that many days of consecutive travel.

# For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
# Return the minimum number of dollars you need to travel every day in the given list of days.

# https://leetcode.com/problems/minimum-cost-for-tickets/description/?envType=problem-list-v2&envId=50vlu3z5&

# used binary search to find next day


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [-1] * len(days)


        def f(i):
           # print(i)
            #f(i) -> min dollars to travel every day in days[:i] (included)

            if i >= len(days):
                return 0

            if dp[i] != -1: return dp[i]
            
            min_cost = 1e9
            for idx, day_pass in enumerate(costs):
                if idx == 0:
                    #next_day = bisect.bisect_left(i + 1)
                    cost = day_pass + f(i + 1)
                if idx == 1:
                    next_day = bisect.bisect_left(days, days[i] + 7) 
                    cost = day_pass + f(next_day)
                if idx == 2:
                    next_day = bisect.bisect_left(days, days[i] + 30)
                    cost = day_pass + f(next_day)
                
                min_cost = min(min_cost, cost)
                dp[i] = min_cost
            
            return min_cost
        
        return f(0)
            

                





        