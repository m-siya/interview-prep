# ### MOST PROFIT ASSIGNING WORK

# You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

# difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
# worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
# Every worker can be assigned at most one job, but one job can be completed multiple times.

# For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
# Return the maximum profit we can achieve after assigning the workers to the jobs.

# https://leetcode.com/problems/most-profit-assigning-work/description/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        dp = [[d, p] for d, p in zip(difficulty, profit)]

        dp.sort(key=lambda x: x[0])
        worker.sort()

       # print(dp, worker)

        tot_profit = 0
        max_profit_seen = 0
        j = 0

        for i in range(len(worker)):
            while j < len(dp) and worker[i] >= dp[j][0]:
                max_profit_seen = max(max_profit_seen, dp[j][1])
                #print(worker[i], dp[j][0])
                j += 1
            
           # print(max_profit_seen)
            tot_profit += max_profit_seen
            
        return tot_profit

