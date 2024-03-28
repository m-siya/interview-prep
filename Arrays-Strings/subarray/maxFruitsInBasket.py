# ### FRUITS INTO BASKETS

# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.

# https://leetcode.com/problems/fruit-into-baskets/description/

# basically find the longest subarray that does not have more than 2 distinct elements

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        j = 0

        freq = {}

        max_length = 0

        for i in range(len(fruits)):
            freq[fruits[i]] = freq.get(fruits[i], 0) + 1
            
            while len(freq.keys()) > 2:
                #print(i, j, freq)
                if freq[fruits[j]] > 1:
                    freq[fruits[j]] = freq.get(fruits[j], 0) - 1
                    j += 1
                else:
                    del freq[fruits[j]]
                    j += 1
            
            max_length = max(max_length, i - j + 1)
        
        return max_length





        