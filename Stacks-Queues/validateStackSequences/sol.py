# Given two integer arrays pushed and popped each with distinct values, return true 
# if this could have been the result of a sequence of push and pop operations on an initially 
# empty stack, or false otherwise.

# https://leetcode.com/problems/validate-stack-sequences/description/

# my approach: simulate the pushing and popping sequences, if at the end, stack is empty then valid else invalid
# time complexity : O(N)
# space complexity : O(1)

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and (stack[-1] == popped[j]):
                stack.pop()
                j += 1
        

        return not stack