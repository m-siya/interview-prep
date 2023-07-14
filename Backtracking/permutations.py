### PERMUTATIONS

#Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

#https://leetcode.com/problems/permutations/description/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
    
        def backtrack(curr, seen):
            #base case
          #  print(curr, seen)
            if len(curr) == len(nums):
                #print(curr, seen)
                return True

            for index, num in enumerate(nums):
                if num in seen:
                    continue
                
                new_curr = curr + [num]
                status = backtrack(new_curr, seen | {num})
                if status:
                    res.append(new_curr)
                

            return False
        
        backtrack([], set())

        return res



