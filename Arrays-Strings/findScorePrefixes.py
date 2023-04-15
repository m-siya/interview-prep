# We define the conversion array conver of an array arr as follows:

# conver[i] = arr[i] + max(arr[0..i]) where max(arr[0..i]) is the 
# maximum value of arr[j] over 0 <= j <= i.
# We also define the score of an array arr as the sum of the values of the conversion 
# array of arr.

# Given a 0-indexed integer array nums of length n, return an array ans of length n where 
# ans[i] is the score of the prefix nums[0..i].

# https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/description/

# time complexity : O(N)
# space complexity : O(N)
class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        conver = [0] * len(nums)
        curr_max = nums[0]
        curr_conver = 0    
        
        for i in range(len(nums)):
            #print(nums[i], curr_max, conver)
            curr_max = max(curr_max, nums[i])
                      
            conver[i] = curr_conver + nums[i] + curr_max
            curr_conver += nums[i] + curr_max
            
        return conver
            
        
        