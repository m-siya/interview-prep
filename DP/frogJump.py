class Solution:
    def minimumEnergy(self, height, n):
        # Code here
        dp = [-1] * n
        #dp[i] is the min energy to reach the ith step
        
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
       
s = Solution()
print(s.minimumEnergy([10, 20, 30], 3))