# ## MAX PRODUCT AFTER K INCREMENTS

# You are given an array of non-negative integers nums and an integer k. In one operation, you may choose any element from nums and increment it by 1.

# Return the maximum product of nums after at most k operations. Since the answer may be very large, return it modulo 109 + 7. Note that you should maximize the product before taking the modulo. 

# https://leetcode.com/problems/maximum-product-after-k-increments/description/

## always increment the smallest number -> min heap

import heapq as hq
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        hq.heapify(nums)

        while k:
            top = hq.heappop(nums)
            hq.heappush(nums, top + 1)
            k -= 1
        

        res = 1

        for n in nums:
            res *= n
            res %= (10 **9 + 7)
        
        return res

        
            
        

