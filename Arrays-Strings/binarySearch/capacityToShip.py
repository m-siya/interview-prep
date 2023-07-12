# ### CAPACITY TO SHIP PACKAGES WITHIN D DAYS

# A conveyor belt has packages that must be shipped from one port to another within days days.

# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the 
# conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped 
# within days days.

# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/


#capacity range is (low -> max(weights), high -> sum(weights))
# time complexity is O(nlogn), space is O(1)
class Solution:
    def possible(self, weights: List[int], max_days: int, capacity: int) -> bool:
        days = 1
        load = 0
        for weight in weights:
            if load + weight <= capacity:
                load += weight
            else:
                days += 1
                load = weight
        
        return days <= max_days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #capacity limit
        low = max(weights)
        high = sum(weights)
        ans = -1

        #print(low, high, self.possible(weights, days, 11))

        while low <= high:
            mid = low + (high - low) // 2
            if self.possible(weights, days, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans