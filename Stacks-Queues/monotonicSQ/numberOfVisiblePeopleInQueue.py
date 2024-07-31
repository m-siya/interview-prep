# ### NUMBER OF VISIBLE PEOPLE IN QUEUE

# There are n people standing in a queue, and they numbered from 0 to n - 1 in left to right order. You are given an array heights of distinct integers where heights[i] represents the height of the ith person.

# A person can see another person to their right in the queue if everybody in between is shorter than both of them. More formally, the ith person can see the jth person if i < j and min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1]).

# Return an array answer of length n where answer[i] is the number of people the ith person can see to their right in the queue.

# https://leetcode.com/problems/number-of-visible-people-in-a-queue/description/

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(heights)

        for i in range(len(heights)):
            curr_height = heights[i]

            while stack and heights[stack[-1]] < curr_height:
                prev_height_idx = stack.pop()
                ans[prev_height_idx] += 1
            
            if stack:
                ans[stack[-1]] += 1 # for every person, the last person in stack can see
            
            stack.append(i)
        
       # print(stack)
        
        return ans
        