# ### MAXIMAL RECTANGLE 

# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

# https://leetcode.com/problems/maximal-rectangle/description/

# tc - O(ROWS * COLS * COLS), sc - O(COLS)
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # take every row as the x axis of a histogram
        # then solve like largest rectangle in histogram

        ROWS, COLS = len(matrix), len(matrix[0])
        max_area = 0
        for row in range(ROWS):

            stack = []

            for i in range(COLS):
                #print(stack)

                height = 0
                if matrix[row][i] == "1":  
                    for j in range(row, ROWS):
                        if matrix[j][i] != "1":
                            break
                        height += 1

                #print(row, i, height)

                start = i
                while stack and stack[-1][1] > height:
                    last_index, last_height = stack.pop()
                    max_area = max(max_area, last_height * (i - last_index))
                    start = last_index
                    
                stack.append((start, height))
            
            while stack:
                index, height = stack.pop()
                max_area = max(max_area, height * (COLS - index))
        
        return max_area

# tc - O(ROWS * COLS), sc - (N + N)

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # take every row as the x axis of a histogram

        ROWS, COLS = len(matrix), len(matrix[0])
        max_area = 0

        heights = [0] * COLS
        for row in range(ROWS):

            stack = []

            for i in range(COLS):
                #print(stack)
                heights[i] = heights[i] + 1 if matrix[row][i] == '1' else 0

            print(heights)

                #print(row, i, height)
            for i in range(COLS):
                start = i
                while stack and stack[-1][1] > heights[i]:
                    last_index, last_height = stack.pop()
                    max_area = max(max_area, last_height * (i - last_index))
                    start = last_index
                    
                stack.append((start, heights[i]))
            
            while stack:
                index, height = stack.pop()
                max_area = max(max_area, height * (COLS - index))
        
        return max_area


            