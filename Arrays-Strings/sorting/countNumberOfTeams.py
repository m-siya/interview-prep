# ### COUNT NUMBER OF TEAMS

# There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

# You have to form a team of 3 soldiers amongst them under the following rules:

# Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
# A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
# Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

# https://leetcode.com/problems/count-number-of-teams/description/?envType=daily-question&envId=2024-07-29

from sortedcontainers import SortedList
class Solution:
    def count_low_high(self, sl, x):
        lo = sl.bisect_left(x)
        hi = len(sl) - lo
        return lo, hi
    
    def numTeams(self, rating: List[int]) -> int:
        # check if from left -> right, how many downhills/uphills are there
        # where each downhill/uphill consists of 3 soldiers


        # method didnt work
        # one pass for uphill, one for downhill
        # maintain a stack
        # for each element, maintain a hashmap - count
        # rating = [2, 5, 3, 4, 1]
        # for 2, write down count of ele less than 2  -> 0, stack = [2]
        # for 5, [arr[i] > stack.top] so count[2] + 1, stack = [2, 5]
        # for 3, [arr[i] < stack.top] -> stack = [2]. count[3] = count[2] + 1, stack [2, 3]
        # for 4, [arr[i] > stack.top] -> count[4] = count[3] + 1, stack [2, 3, 4]
        # for 1, [arr[i] < stack.top] -> stack = [] = count[1] = 0

        # similarly for right -> left to count greater elements

        # stack = [] # (index, ele)
        # count = collections.defaultdict(int)

        # for i in range(len(rating)):

        #     while stack and stack[-1][1] > rating[i]:
        #         stack.pop()
            
        #     if stack:
        #         top_idx, top_ele = stack[-1]
        #         count[i] = count[top_idx] + 1
        #     else:
        #         count[i] = 0
            
        #     stack.append((i, rating[i]))
        
        # print(count)

        # return 0

        # actual answer starts here

        result = 0
        left, right = SortedList(), SortedList(rating)

        for x in rating:
            right.remove(x)
            lo_L, hi_L = self.count_low_high(left, x)
            lo_R, hi_R = self.count_low_high(right, x)
            result += lo_L * hi_R + hi_L * lo_R
            left.add(x)
        return result

    
    




