### COUNT TRIPLETS THAT CAN FORM TWO EQUAL ARRAYS OF EQUAL XOR

# Given an array of integers arr.

# We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

# Let's define a and b as follows:

# a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
# b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
# Note that ^ denotes the bitwise-xor operation.

# Return the number of triplets (i, j and k) Where a == b.

# https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/description/

# If a subarray XOR is zero, then any splitting point in this subarray will result in 2 subarrays with same XOR value.
# Because of this, we only need to find all subarrays whose XOR is zero. 
# We use prefix XOR to check if same XOR visited before. XOR with visited prefix is guaranteed to produce a "Zero XOR" subarray.
# if we have seen the XOR at i and then see it at j, then XOR(arr[i..j]) == 0
# prefix[xor]=[idxSum, cnt]
# "idxSum": is the sum of all "index" whose prefix XOR equals "xor".
# "cnt": means how many such "index" has prefix XOR being "xor".
# Why "idxSum"? Suppose index "a, b, c" all has the same prefix xor. Current index is "i", then the result is:
# (i-a-1)+(i-b-1)+(i-c-1) == i*3-(a+b+c)-3. We can't save "i" into prefix table, we can only save "a+b+c" and "cnt=3", so that when "i" comes, we can find result in O(1) time using: i*3-(a+b+c)-3

from typing import List
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # XOR(a1, a2, ..) == XOR(b1, b2, ...)
        # => XOR(a) == XOR(b)
        # => XOR(a, b) == 0
        # make array of xors??
        # prefix_xors = [0, xor(arr[0]), xor(arr[0], arr[1]), ...]
        # => xor(a[i..j) = XOR(prefix_xors[j + 1], prefix_xors[i])  since [prefix_xors[0] == 0]

        mp = {0: [-1, 1]} #mp[xor_val] = [index_sum, count]

        res, curr = 0, 0

        for i, num in enumerate(arr):
            curr ^= num
            index_sum, count = mp.get(curr, [0, 0])
            res += i * count - index_sum - count
            mp[curr] = [index_sum + i, count + 1]

        return res
            

