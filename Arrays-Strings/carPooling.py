# ### CARPOOLING

# There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

# You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

# Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.


# https://leetcode.com/problems/car-pooling/description/

# tc - O(n + nlogn + n), sc - O(2* n)

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        stops = []

        for num, start, end in trips:
            stops.append([start, num])
            stops.append([end, -num])

        stops.sort()

        curr_capacity = 0
        for stop, num in stops:
            curr_capacity += num
            if curr_capacity > capacity:
                return False

        return True
