# ### MINIMUM SPEED TO ARRIVE ON TIME

# You are given a floating-point number hour, representing the amount of time you have 
# to reach the office. To commute to the office, you must take n trains in sequential 
# order. You are also given an integer array dist of length n, where dist[i] describes
# the distance (in kilometers) of the ith train ride.

# Each train can only depart at an integer hour, so you may need to wait in between 
# each train ride.

# For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 
# 0.5 hours before you can depart on the 2nd train ride at the 2 hour mark.
# Return the minimum positive integer speed (in kilometers per hour) that all the trains
# must travel at for you to reach the office on time, or -1 if it is impossible to be 
# on time.

# Tests are generated such that the answer will not exceed 107 and hour will have at 
# most two digits after the decimal point.

# https://leetcode.com/problems/minimum-speed-to-arrive-on-time/description/

# method - speed can range from 1 to 10^7. then we do a binary search on range(1, 10^7, 1)
# to find which is the minimum speed possible. 
# if time needed to commute at mid speed > available_time: increase speed, else decrease speed

# tc - O(log(10^7))

class Solution:
    def getCommuteTime(self, dist, speed):
        answer = 0
        for d in dist[:-1]:
            answer += math.ceil(d / speed)
        
        answer += (dist[-1] / speed)
        return answer
            
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        low, high = 1, 10000000

        if self.getCommuteTime(dist, high) > hour: return -1

        while low <= high:
            mid = low + (high - low) // 2

            time = self.getCommuteTime(dist, mid)
            if time > hour:
                low = mid + 1
            if time == hour:
                return mid
            if time < hour:
                high = mid - 1
        
        
        return low

            
            