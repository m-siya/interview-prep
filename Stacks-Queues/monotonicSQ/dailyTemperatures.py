# ### DAILY TEMPERATURES

# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] 
# is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for 
# which this is possible, keep answer[i] == 0 instead.

# https://leetcode.com/problems/daily-temperatures/

# method- use monotonic stack. stack stores numbers in decreasing order
# as we iterate from right to left, we store the greatest number seen on the stack since
# eg - if we store nums[i] on stack, then for all numbers for k < i and for which nums[k] < nums[i], the next warmer
# temperature cannot be any temperature to the left of nums[i].

# tc - O(n), sc - O(n)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # i.e find next bigger number in array

        stack = []
        answer = []

        for i in range(len(temperatures) - 1, -1, -1):
            #print(i, stack, answer)
            if stack and temperatures[i] >= temperatures[stack[-1]]:
                
                while stack and temperatures[i] >= temperatures[stack[-1]]:
                    stack.pop()
                
                days = stack[-1] - i if stack else 0
                answer.append(days)
                stack.append(i)
            elif stack and temperatures[i] < temperatures[stack[-1]]:
                answer.append(stack[-1] - i)
                stack.append(i)
            else:
                answer.append(0)
                stack.append(i)
           # print(stack, answer)
        
        return answer[::-1]


# more elegant solution
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # i.e find next bigger number in array

        stack = []
        answer = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            #print(i, stack, answer)
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            
            answer[i] = stack[-1] - i if stack else 0
            stack.append(i)
        return answer

# going from left to right

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):

            curr_temp = temperatures[i]

            while stack and curr_temp > temperatures[stack[-1]]:
                prev_temp_idx = stack.pop()
                ans[prev_temp_idx] = i - prev_temp_idx
            
            stack.append(i)
        
        return ans


        
        

