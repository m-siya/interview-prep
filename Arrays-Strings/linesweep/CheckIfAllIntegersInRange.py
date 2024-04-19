### CHECK IF ALL THE INTEGERS IN A RANGE ARE COVERED

# You are given a 2D integer array ranges and two integers left and right. Each ranges[i] = [starti, endi] represents an inclusive interval between starti and endi.

# Return true if each integer in the inclusive range [left, right] is covered by at least one interval in ranges. Return false otherwise.

# An integer x is covered by an interval ranges[i] = [starti, endi] if starti <= x <= endi.

# https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

from collections import defaultdict
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        numberline = defaultdict(int)

        for interval in ranges:
            numberline[interval[0]] += 1
            numberline[interval[1] + 1] -= 1 #since interval is inclusive

        count = 0
        for i in range(1, 51):
            count += numberline[i]
            if i in range(left, right + 1):
                if count == 0: return False
        
        return True



        