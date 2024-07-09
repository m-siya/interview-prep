# ### CANDY

# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.

# https://leetcode.com/problems/candy/description/


## 
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy = n
        i = 1

        while i < n:
            #print(i)
            if ratings[i] == ratings[i - 1]:
                i += 1
                continue
            
            peak = 0
            while ratings[i] > ratings[i - 1]:
                peak += 1
                candy += peak
                i += 1
                if (i == n): return candy
            
            valley = 0
            while i < n and ratings[i] < ratings[i - 1]:
                valley += 1
                candy += valley
                i += 1
            
            candy -= min(valley, peak)
        
        return candy
            

            
            
        