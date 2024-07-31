# ### MIN COST TO CONVERT STRING I

# You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English letters. You are also given two 0-indexed character arrays original and changed, and an integer array cost, where cost[i] represents the cost of changing the character original[i] to the character changed[i].

# You start with the string source. In one operation, you can pick a character x from the string and change it to the character y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.

# Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.

# Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].

# https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=daily-question&envId=2024-07-27

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(changed)
        matrix = [[0 if i == j else 1e9 for i in range(26)] for j in range(26)]
       # print(matrix)

        for i in range(n):
            o, ch, c = original[i], changed[i], cost[i]
            matrix[ord(o) - ord('a')][ord(ch) - ord('a')] = min(c, matrix[ord(o) - ord('a')][ord(ch) - ord('a')])
        

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
        
        res = 0
        for i in range(len(source)):
            s, t = source[i], target[i]
            cost = matrix[ord(s) - ord('a')][ord(t) - ord('a')]
            if cost == 1e9:
                return -1
            res += cost

        return res
        