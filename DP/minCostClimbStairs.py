# You are given an integer array cost where cost[i] is the cost of ith step 
#on a staircase. Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.

# https://leetcode.com/problems/min-cost-climbing-stairs/description/

class Solution:
    #my sol 
    #time complexity : O(N)
    #space complexity : O(N) due to recursive stack and dp array
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [ -1 for _ in range(len(cost) + 1)]
        # dp[i] is the min cost to pay to reach the ith step
        dp[0], dp[1] = cost[0], cost[1]

        def helper(i, cost):
            if i < 0:
                return float('inf')
            if i == 0 or i == 1:
                return dp[i]
            
            if dp[i] == -1:
                if i == len(cost):
                    climbedOne = helper(i - 1, cost)
                    climbedTwo = helper(i - 2, cost)
                else:
                    climbedOne = cost[i] + helper(i - 1, cost)
                    climbedTwo = cost[i] + helper(i - 2, cost)
                dp[i] = min(climbedOne, climbedTwo)

            return dp[i]
        return helper(len(cost), cost)
    
    #we should remove the redundant i == len(cost) statement
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [ -1 for _ in range(len(cost))]
        # dp[i] is the min cost to pay to reach the ith step
        dp[0], dp[1] = cost[0], cost[1]

        def helper(i, cost):
            if i < 0:
                return float('inf')
            if i == 0 or i == 1:
                return dp[i]
            
            if dp[i] == -1:
                climbedOne = cost[i] + helper(i - 1, cost)
                climbedTwo = cost[i] + helper(i - 2, cost)
            dp[i] = min(climbedOne, climbedTwo)

            return dp[i]
        return min(helper(len(cost) - 1), helper(len(cost) - 2))
    
    #iterative or bottom up solution
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [ -1 for _ in range(len(cost) + 1)]
        # dp[i] is the min cost to pay to reach the ith step
        
        for i in range(len(cost)):
            if i < 2:
                dp[i] = cost[i]
            else:
                dp[i] = cost[i] + min(cost[i - 1], cost[i - 2])
        
        return min(dp[len(cost) - 1], dp[len(cost) - 2])
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costLength = len(cost)
        first, second = cost[0], cost[1]

        #if (costLength <= 2) : return min(first, second)

        for i in range(2, len(cost)):
            curr = cost[i] + min(first, second)
            first = second
            second = curr

        return min(first, second)


    
    
    