# ### MAXIMUM EARNINGS FROM TAXI

# There are n points on a road you are driving your taxi on. The n points on the road are labeled from 1 to n in the direction you are going, and you want to drive from point 1 to point n to make money by picking up passengers. You cannot change the direction of the taxi.

# The passengers are represented by a 0-indexed 2D integer array rides, where rides[i] = [starti, endi, tipi] denotes the ith passenger requesting a ride from point starti to point endi who is willing to give a tipi dollar tip.

# For each passenger i you pick up, you earn endi - starti + tipi dollars. You may only drive at most one passenger at a time.

# Given n and rides, return the maximum number of dollars you can earn by picking up the passengers optimally.

# Note: You may drop off a passenger and pick up a different passenger at the same point.

# https://leetcode.com/problems/maximum-earnings-from-taxi/description/

# again, having the values of 'tips' prevents greedy strategy since these can be 
# any arbitrary value

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort()

        dp = [-1] * len(rides)

        def f(i):
            if i == len(rides): return 0

            if dp[i] != -1: return dp[i]

            pick, leave = 0, 0

            start, end, tip = rides[i][0], rides[i][1], rides[i][2]

            j = bisect.bisect_left(rides, [end])

            pick = end - start + tip + f(j)
            leave = f(i + 1)

            dp[i] = max(pick, leave)
            return dp[i]
        
        return f(0)
        