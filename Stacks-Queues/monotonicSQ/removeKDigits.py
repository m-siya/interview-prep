### REMOVE K DIGITS

#Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

# if number is before and bigger, remove

#tc : O(N)
# SC: O(N)


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
        

    
        