# ### 132 PATTERN 

# Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

# Return true if there is a 132 pattern in nums, otherwise, return false.

# https://leetcode.com/problems/132-pattern/

# intuition - since the pattern is in an increasing then decreasing sequence, we can think of a 
# monotonic stack
# iterate throught the array in reverse. 
# keep adding elements as long as decreasing order of stack is maintained i.e essentionally we are
# keeping a track of the smallest element seen so far .
# if you encounter an element greater than the top of the stack now, it means that we have found
# a potential 3(curr element) and 2 (in stack). so the presence of the 3 indicates we found 2 as well
# so we can pop off the stack till 3 is no longer greater than the top of the stack
# keep a track of the biggest element (2)  encountered so far than is less than 3. (this is so because
# it maximizes chances of finding an element smaller than 2)
# if we encounter an element now than is less than our biggest smallest then that is our 1.

# tc - O(n), sc - (n)
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        stack = []
        
        biggest_smallest = -1e9
        for n in nums[::-1]:
            if n < biggest_smallest:
                return True
            while stack and stack[-1] < n:
                biggest_smallest = stack.pop()
            
            stack.append(n)

        return False
            

    

                

        