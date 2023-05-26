# Alice plays the following game, loosely based on the card game "21".

# Alice starts with 0 points and draws numbers while she has less than k points. 
# During each draw, she gains an integer number of points randomly from the range [1, maxPts], 
# where maxPts is an integer. Each draw is independent and the outcomes have equal probabilities.

# Alice stops drawing numbers when she gets k or more points.

# Return the probability that Alice has n or fewer points.

# https://leetcode.com/problems/new-21-game/description/

# Note - Neetcode Sol
# https://www.youtube.com/watch?v=zKi4LzjK27k
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        cache = {}
        
        def dfs(score): #start at score, return probablity
            if score >= k:
                return 1 /  if score <= n else 0
            
            if score in cache:
                return cache[score]
            
            prob = 0
            for i in range(1, maxPts + 1):
                prob += dfs(score + i)
            
            cache[score] = prob / maxPts
            return cache[score]

            



class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [-1] * (n + 1)
        #dp[i] is probablility of getting n points
        dp[0] = 0
        dp[1] = 0.1
        
        def f(i): #-> probality of getting i points:
            if i == 1:
                return 0.1
            if i == 0:
                return 0

            if dp[i] != -1:
                return dp[i]

            probablity = 0
            for pt in range(1, i):
                if pt == k
                probablity += f(pt) * f(i - pt)

            dp[i] = probablity
            return dp[i]           
        
        
        for i in range(n + 1):
            print(f(i))
        
        print(dp)
        return sum(dp[k:])