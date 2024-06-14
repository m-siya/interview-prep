### MIN INCREMENT TO MAKE ARRAY UNIQUE

# You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

# Return the minimum number of moves to make every value in nums unique.

# The test cases are generated so that the answer fits in a 32-bit integer.

# https://leetcode.com/problems/minimum-increment-to-make-array-unique/description/


# sort the array and keep track of the highest num seen yet

# tc - O(nlogn)
# sc - O(1)


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:

        nums.sort()

        last_seen_max = nums[0]
        moves = 0
       # print(nums)
        for i in range(1, len(nums)):
           # print(nums[i], last_seen_max, last_seen_max - nums[i] + 1 )
            if nums[i] <= last_seen_max:
                diff = last_seen_max - nums[i] + 1 
                moves += diff
                nums[i] += diff
           # print(nums[i], last_seen_max, moves)  
            last_seen_max = max(nums[i], last_seen_max)
        
        return moves
        