# ### LONGEST CONTINUOUS SUBARRAY WITH DIFFERENCE EQUAL TO OR LESS THAN LIMIT

# Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/


# make two deques, monotonic desc and asc. the invariant is when the largest element of desc deque and
# smallest element of asc deque is greater than limit.



from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        asc_stack = deque()
        desc_stack = deque()
        j = 0
        max_len = 0
        for i in range(len(nums)):
          #  print(desc_stack , asc_stack)

            while desc_stack and nums[i] >= desc_stack[-1][0]:
                desc_stack.pop()
            
            desc_stack.append((nums[i], i))

            while asc_stack and nums[i] <= asc_stack[-1][0]:
                asc_stack.pop()
            
            asc_stack.append((nums[i], i))
        
            while j < len(nums) and abs(desc_stack[0][0] - asc_stack[0][0]) > limit:
                j += 1
                if desc_stack and desc_stack[0][1] < j:
                    desc_stack.popleft()
                if asc_stack and asc_stack[0][1] < j:
                    asc_stack.popleft()


            max_len = max(max_len, i - j + 1)
            #print(desc_stack, asc_stack)
        return max_len
        