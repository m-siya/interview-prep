# ### MINIMUM NUMBER OF ARROWS TO BURST BALLOONS

# There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

# Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

# Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/

# method - sort the array and iterate through the points. keep track of the lowest end coordinate
# seen yet which overlaps with start of balloons. if encounter a balloon whoose start > end:
# we need a new arrow

# tc - O(nlogn + n), sc - O(1)

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # min number of arrows is 1, max = len(points)
        # method - do binary search over min -max and at each point, check if mid is able to burst all arrows

        points = sorted(points, key = lambda x: x[0])

        last_min_end = float('-inf')
        #print(points[0][0] > -1e9)
        arrows = 0

        for x, y in points:
            if x > last_min_end:
                #we need new arrow now
                arrows += 1
                last_min_end = y
            else:
                last_min_end = min(last_min_end, y)

        return arrows




        

