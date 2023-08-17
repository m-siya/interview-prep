# ### LARGEST RECTANGLE AREA

# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
# return the area of the largest rectangle in the histogram.

# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

# intuition - for every heights[i] in heights, 
#   if heights[i + 1] < heights[i], then
#       heights[i] cannpt be extended further. 
#   else:
#       heights[i] can be extended further.
#       add heights[i + 1] to stack
#  hence stack is sorted in increasing order

# tc - O(n), sc - O(n)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        max_area = 0

        stack = [] #pair (index where height started, height)

        for i in range(len(heights)):
            start = i
            while stack and heights[i] < stack[-1][1]:
                last_index, last_height = stack.pop()
                max_area = max(max_area, last_height * (i - last_index))
                start = last_index
            
            stack.append((start, heights[i]))

        while stack:
            last_index, height = stack.pop()
            max_area = max(max_area, height * (len(heights) - last_index))
        
        return max_area

                

