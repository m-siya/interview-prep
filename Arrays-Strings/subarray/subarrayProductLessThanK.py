### SUBARRAY PRODUCT LESS THAN K

#Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

#The idea is always keep an max-product-window less than K;
# Every time shift window by adding a new number on the right(j), if the product is greater than k, then try to reduce numbers on the left(i), until the subarray product fit less than k again, (subarray could be empty);
# Each step introduces x new subarrays, where x is the size of the current window (j + 1 - i);

#TC: O(n)
#SC: O(1)

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        product = 1
        j = 0
        for i in range(len(nums)):
            product *= nums[i]

            while  j <= i and product >= k:
                product /= nums[j]
                j += 1
            
            count += (i - j + 1)


        return count
        