# ### PASCAL'S TRIANGLE

# Given an integer numRows, return the first numRows of Pascal's triangle.

# https://leetcode.com/problems/pascals-triangle/description/

# tc - O(n ^ 2), sc - O(1)

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []

        for n in range(numRows):
            row = []
            for r in range(n + 1):
                row.append(math.comb(n, r))
            answer.append(row)

        return answer




                
                
            