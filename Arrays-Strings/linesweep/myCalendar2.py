# ### MY CALENDAR 2
# You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a triple booking.

# A triple booking happens when three events have some non-empty intersection (i.e., some moment is common to all the three events.).

# The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

# Implement the MyCalendarTwo class:

# MyCalendarTwo() Initializes the calendar object.
# boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.
 

# https://leetcode.com/problems/my-calendar-ii/description/


# if there is no clash, a 'start' is always be followed by its corresponding end.. so 'count'
#  will never be more than 1 (this is because the end will decrement the counter) 
# If two time periods are clashing, you will see two consecutive 
# starts. So, if there is only a double clash 'count' can grow to 2. Similarly, if there is 
# a triple clash then 'count' can go to 3.

#TC: (n^2 logn)
#SC: O(n)

from collections import defaultdict
class MyCalendarTwo:

    def __init__(self):
        self.timeline = defaultdict(int)

        

    def book(self, start: int, end: int) -> bool:
        self.timeline[start] += 1
        self.timeline[end] -= 1

        count = 0

        for time in sorted(self.timeline):
            count += self.timeline[time]
            if count >= 3:
                self.timeline[start] -= 1
                self.timeline[end] += 1
                return False
        # self.timeline[end] -= 1


        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)