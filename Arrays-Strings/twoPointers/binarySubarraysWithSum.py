# ### BINARY SUBARRAY WITH SUM

# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

# A subarray is a contiguous part of the array.

# https://leetcode.com/problems/binary-subarrays-with-sum/description/\

# tc - O(N), sc - O(1)
class Solution:
    def numSubarraysWithSum(self, A: List[int], goal: int) -> int:
        #number of subarrays of len n is n * (n + 1) / 2

        def atMost(S):
            if S < 0:
                return 0
            preSum = res = l = 0

            #use r to expand the window, when sum of all numbers is bigger than S, 
            #time to shorten the window and increment l. count subarrays
            
            #we add the length of the subarray because every 1 that contributes to r - l  1 can be a subarray
            #with length < S. so all subarrays with sum less than S are counted
            for r in range(len(A)):
                preSum += A[r]
                while preSum > S:
                    preSum -= A[l]
                    l += 1
                res += r - l + 1
            
            return res
        return atMost(goal) - atMost(goal - 1)
            

        
        



