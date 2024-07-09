### XOR queries of a subarray

# You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].

# For each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).

# Return an array answer where answer[i] is the answer to the ith query.

# https://leetcode.com/problems/xor-queries-of-a-subarray/description/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = [0] * (len(arr)+ 1)

        for i in range(1, len(arr) + 1):
            prefix_xor[i] ^= (prefix_xor[i - 1] ^ arr[i - 1])
        
       # print(prefix_xor)
        ans = []

        for left, right in queries:
            ans.append(prefix_xor[right + 1] ^ prefix_xor[left])

        return ans
        