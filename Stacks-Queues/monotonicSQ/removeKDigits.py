### REMOVE K DIGITS

#Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

# if number is before and bigger, remove
# tc : O(N)
# SC : O(N)

#ref https://leetcode.com/problems/remove-k-digits/solutions/5006003/easy-o-n-solution-with-thought-process-clean-code-with-explanation-python3/
# But if we have peaks in digits such as 2193 (2 > 1 < 9 ..), observe that 
# 2xx will always be greater than 1xx, so there is no point in keeping the 2. 
# We should remove the peak and keep the 193.

# We can also observe the repeated nature of these removals - that is, after
# one removal the adjacent digits become eligible for removal again. So a 
# stack should be useful here to perform these repeated removals via popping.




class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []

        for i in range(len(num)):

            while stack and stack[-1] > num[i] and k:
                stack.pop()
                k -= 1
            
            stack.append(num[i])
        
        if k:
            stack = stack[:-k]
        return "".join(stack).lstrip("0") or "0"
        

    
        