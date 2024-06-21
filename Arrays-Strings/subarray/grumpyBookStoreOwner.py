# ### GRUMPY BOOK STORE OWNER

# There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.

# On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

# When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.

# The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.

# Return the maximum number of customers that can be satisfied throughout the day.

 
# https://leetcode.com/problems/grumpy-bookstore-owner/description/

# tc - O(N)

# template for rolling sum

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], mins: int) -> int:
        base = 0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                base += customers[i]
                customers[i] = 0
        
       # print(base, customers)


        #find subarray of length mins that has the most customers

        max_extra = 0
        window = 0

        for i in range(len(customers)):
            window += customers[i]
            if i >= mins:
                window -= customers[i - mins]
            max_extra = max(max_extra, window)

        return max_extra + base
        


        

