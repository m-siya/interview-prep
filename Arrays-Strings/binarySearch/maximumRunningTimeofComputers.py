# ### MAXIMUM RUNNING TIME OF N COMPUTERS

# You have n computers. You are given the integer n and a 0-indexed integer array 
# batteries where the ith battery can run a computer for batteries[i] minutes. You are 
# interested in running all n computers simultaneously using the given batteries.

# Initially, you can insert at most one battery into each computer. After that and at
# any integer time moment, you can remove a battery from a computer and insert another
# battery any number of times. The inserted battery can be a totally new battery or a 
# battery from another computer. You may assume that the removing and inserting 
# processes take no time.

# Note that the batteries cannot be recharged.

# Return the maximum number of minutes you can run all the n computers simultaneously.       

# https://leetcode.com/problems/maximum-running-time-of-n-computers/description/

# intuition - if one of the batteries has a lot of charge, we may not be able to use it  up
# if we cannot run n - 1 computers long enough on the remaining (smaller) batteries.

# let the juiciest battery have life of x minutes.
# if charge per computer (sum(batteries) / n) < x:
#   then this battery will to the end of the period when all computers run simultaneously
# now do same for n - 1 computers. (we assume that we are assigning batteries from 
# larger to smaller and the juiciest battery has been assigned to the nth computer)
# when we find that charge per computer > x :
#   then all the current computers (n - i) can run the remaining (sum(batteries[:i]) / i) 
# minutes.
# tc - O(nlogn(sort) + n), sc - O(1)

class Solution:

    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        total_battery_life = sum(batteries)
        while batteries[-1] > total_battery_life / n:
            n -= 1
            total_battery_life -= batteries.pop()
           # print(batteries)
        return total_battery_life // n


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