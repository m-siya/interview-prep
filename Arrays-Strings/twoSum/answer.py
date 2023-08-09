#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #solve using sorting and searching
        seen = {}
        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [i, seen[target - nums[i]]]
            else:
                seen[nums[i]] = i
                 
