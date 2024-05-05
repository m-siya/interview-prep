# ### MAXIMUM PROFIT IN JOB SCHEDULING

# We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

# You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

# If you choose a job that ends at time X you will be able to start another job that starts at time X.

 
#  https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/

# same strategy as max earning in taxi and max num of events 2 due to presence of profits
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        jobs = [list(job) for job in zip(startTime, endTime, profit)]
        jobs.sort()

        dp = [-1] * len(jobs)
        
        #print(jobs)

        def f(i):
            if i == len(jobs): return 0

            if dp[i] != -1: return dp[i]

            start, end, profit = jobs[i]

            pick, leave = 0, 0

            j = bisect.bisect_right(jobs, [end])
            pick = profit + f(j)
            leave = f(i + 1)

            dp[i] = max(pick, leave)
            return dp[i]
        
        
        return f(0)
        