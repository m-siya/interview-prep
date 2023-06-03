# You are given an integer array nums and an integer target.

# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer 
# in nums and then concatenate all the integers.

# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build 
# the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.

# https://leetcode.com/problems/target-sum/description/

### thinking process
# 1. Category - 0/1 Knapsack - our capacity is the target we want to reach and our items are the numbers in the input 
#subset, our weights are the values of the items themselves. We can use each number only once. Variation - we have to all 
# all the items to the knapsack

# 2. States - knapsack usually requires 2 states. index, current sum

# 3. Decisons - (take or leave). Here, we need to take all items but we add the postitive
#  or the negative value of the item.

# 4. Base Case - Valid: Index is out of bounds AND current sum is equal to target 'S'
# Invalid: Index is out of bounds


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        dp = [[None for _ in range(2 * sum(nums) + 1)] for _ in range(len(nums))]
      #  print(dp)

        def f(i, currValue):
           # f(i) -> no. of expressions using nums[:i] (inclusive)
            if i < 0:
                if currValue == target:
                    return 1
                else:
                    return 0
            #print(i, currValue)

            currValue_index = total_sum + currValue

            if dp[i][currValue_index] != None:
                return dp[i][currValue_index]

            addPlus = f(i - 1, currValue + nums[i])
            addMinus = f(i - 1, currValue - nums[i])

            dp[i][currValue_index] = addPlus + addMinus
            return addPlus + addMinus
        
        ans = f(len(nums) - 1, 0)
      #  print(dp)
        return ans

