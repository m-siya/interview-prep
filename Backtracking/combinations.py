# ### COMBINATIONS    

# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.

# https://leetcode.com/problems/combinations/description/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(comb, curr_num):
            if curr_num > n and len(comb) != k:
                return False
            if len(comb) == k:
                return True

            status_include = backtrack(comb + [curr_num], curr_num + 1)
            if status_include:
                res.append(comb + [curr_num])
            
            status_exclude = backtrack(comb, curr_num + 1)
            if status_exclude:
                res.append(comb)
            

        
        backtrack([], 1)
        return res
    
# backtracking approach 2
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(comb, curr_num):
            if curr_num > n and len(comb) != k:
                return 
            if len(comb) == k:
                res.append(comb[:])

            for num in range(curr_num, n + 1):
                comb.append(num)
                backtrack(comb, num + 1)
                comb.pop()
            

        
        backtrack([], 1)
        return res
    

# ### COMBINATION SUM

# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of 
# candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 
# combinations for the given input.
    
# https://leetcode.com/problems/combination-sum/description/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(comb, curr_index, curr_sum):
            if curr_sum == target:
                res.append(comb[:])
                return
            elif curr_sum > target:
                return
            
            for index in range(curr_index, len(candidates)):
                comb.append(candidates[index])
                curr_sum += candidates[index]
                backtrack(comb, index, curr_sum)
                comb.pop()
                curr_sum -= candidates[index]
        
        backtrack([], 0, 0)
        return res


