# ### NUMBER OF SUBMATRICES THAT SUM TO TARGET

# Given a matrix and a target, return the number of non-empty submatrices that sum to target.

# A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

# Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

# 2D prefix sums
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        ROWS, COLS = len(matrix), len(matrix[0]) + 1

        ans = 0

        prefix_sums = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        for i in range(ROWS):
            for j in range(1, COLS):
                prefix_sums[i][j] += prefix_sums[i][j - 1] + matrix[i][j - 1]
        
       # print(prefix_sums)

        for j1 in range(COLS):
            for j2 in range(j1 + 1, COLS):
                #select 2 cols
                # iter down
                mp = collections.defaultdict(int)
                mp[0] = 1
                matrix_sum = 0
                for i in range(ROWS):
                    matrix_sum += prefix_sums[i][j2] - prefix_sums[i][j1]
                    #for subarray sum equals k:

                    # prefix_sums[i] - prefix_sums[j] == k
                    # prefix_sums[j] = prefix_sums[i] - k
                    if matrix_sum - target in mp:
                        ans += mp[matrix_sum - target]
                    mp[matrix_sum] += 1
        

        return ans
        