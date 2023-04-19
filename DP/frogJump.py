# Given a number of stairs and a frog, the frog wants to climb from the 0th stair to the (N-1)th stair. 
# At a time the frog can climb either one or two steps. A height[N] array is also given. Whenever the frog
# jumps from a stair i to stair j, the energy consumed in the jump is abs(height[i]- height[j]), where abs() 
# means the absolute difference.
# We need to return the minimum energy that can be used by the frog to jump from stair 0 to stair N-1.

class Solution:
    #Top Down/ Memoization Method
    def minimumEnergy(self, height, n):
        # Code here
        dp = [-1] * n
        #dp[i] is the min energy to reach the ith step
        
        #the overlapping subproblems will return the answer in constant time O(1). so, the total number
        #of new subproblems we solve is 'n'. so Time complexity is O(N)

        #space complexity : O(N) due to recursive stack + dp array

        #f(i) -> min energy to reach ith step
        def f(i):
            if i == 0:
                return 0
            
            if dp[i] != -1:
                return dp[i]
        
            climbOne = abs(height[i] - height[i - 1]) + f(i - 1)
            climbTwo = float('inf')
            if i > 1:
                climbTwo = abs(height[i - 2] - height[i]) + f(i - 2)
            
            dp[i] =  min(climbOne, climbTwo)
         
            return dp[i]     
        
        return f(n - 1)
    
    #Bottom-Up/Tabulation Method
    def minimumEnergy_BU(self, height, n):
        dp = [-1] * n
        dp[0] = 0
        dp[1] = abs(height[1] - height[0])

        for i in range(2, n):
            climbOne = dp[i - 1] + abs(height[i] - height[i - 1])
            climbTwo = dp[i - 2] + abs(height[i] - height[i - 2])
            dp[i] = min(climbOne, climbTwo)

        return dp[n - 1]
    
    #Optimizing space -> O(1)
    def minimumEnergy_SO(self, height, n):
        climbedOne = 0
        climbedTwo = 0
        currCost = 0

        for i in range(1, n):
            choice1 = climbedOne + abs(height[i] - height[i - 1])
            choice2 = float('inf')
            if i > 1:
                choice2 = climbedTwo + abs(height[i] - height[i - 2])

            currCost = min(choice1, choice2)

            climbedTwo = climbedOne
            climbedOne = currCost

        return currCost
            



       
s = Solution()
print(s.minimumEnergy_SO([10, 20, 30], 3))
print(s.minimumEnergy([10, 20, 30], 3))


## VARIABLE FROG JUMP   
# There are n stones and an array of heights and a frog is standing at stone 1 and can jump 
# to one of the following: Stone i+1, i+2, ... i+k stone and cost will be [hi-hj] is incurred,
# where j is the stone to land on. Find the minimum possible total cost incurred before the frog 
# reaches Stone N.

class SolutionV:
    #time complexity : O(N * K) -> an additional k factor for the for loop in function body
    #space complexity : O(N)
    def minimumEnergy(self, height, n, k):
        
        #f(i) -> min cost incurred to jump to ith stone
        dp = [-1] * n

        def f(i):
            if i == 0:
                return 0

            if dp[i] != -1:
                return dp[i]
                   
            minCost = float('inf')
            for j in range(i - 1, i - k - 1, -1):
                if j >= 0 and (i - j) >= 0:
                    currCost = abs(height[i] - height[j]) + f(j)
                    minCost = min(minCost, currCost)
            dp[i] = minCost    
            return dp[i]
            
        
        return f(n - 1)
                
s = SolutionV()
#print(s.minimumEnergy_SO([10, 20, 30], 3))
print(s.minimumEnergy([10, 30, 40, 50, 20], 5, 3))                