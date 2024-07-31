# ### SUM OF SUBARRAY MINIMUMS

# Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

# https://leetcode.com/problems/sum-of-subarray-minimums/description/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # what j does is consider all subarrays starting from jth index
        # so if for arr[j], there exists a smaller num at right end of q then for all subarrays involving indices j and q[-1][0], that min is smallest and should be added to res       
        n = len(arr)
        stack = []
        result = [0] * (n + 1) # result[i] == sum of all arrays that end at position i

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            
            j = stack[-1] if stack else -1
            # i is next greater element than element j
            result[i] = result[j] + (i - j) * arr[i]
            stack.append(i)
        
        return sum(result) % (10**9 + 7)

#https://dwf.dev/blog/2024/04/26/2024/monotonic-stacks-queues/#monotonic-stacks-and-queues-deques

#the current value we consider to be a minimum or maximum, curr_min_or_max, should be as far left or as far right as possible to ensure subsequently encountered values that are equivalent to curr_min_or_max are handled appropriately (i.e., not overcounted).

# everytime we see something smaller, we can disregard evertything that came before
# -> next smaller element??

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res =0
        stack = [] # (index, num)

        # for every single n, count how many times it is the smallest ele in a subarray
        for i, n in enumerate(arr):
            # loosly increasing stack
            # pop if n smaller than elements seen before because then
            # the other (bigger) elements will never be used
            while stack and stack[-1][1] > n:
                j, m = stack.pop()

                #    j        i
                # 1, 2, 3, 4, 1

                right = i - j # subarr starting with j
                left = j - stack[-1][0] if stack else j + 1 # subarr ending with j
                res = (res + m * left * right) 
            
            stack.append((i, n))
        
        # eg if [(1, i1), (2, i2), (4, i3)] left in stack
        # we know that these are the smallest elements for subarrs starting with 
        # index i. so
        # now take top of stack, its (4, i3)
        # subarray we can make to the right (starting with 4)
        # are len(arr) - j. because we reached end of arr.
        # and to the left (ending with 4)
        # look in stack, the previous element to 4. if in stack (let it be ik), then for all indices
        # greater than ik, 4 is the min element. so thats why do j - stack[i - 1][0]
        
        
        for i in range(len(stack)):
            j, n = stack[i]
            left = j - stack[i - 1][0] if i > 0 else j + 1
            right = len(arr) - j
            res = (res + n * left * right)
        
        return res


