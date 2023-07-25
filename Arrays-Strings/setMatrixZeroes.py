### SET MATRIX ZEROES

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

# https://leetcode.com/problems/set-matrix-zeroes/

# brute force - iterate through the matrix and for all matrix[i][j] == 0, add i to zero_rows and j to zero_cols. 
# then iterate though the matrix again and if i in zero_rows or j in zero_cols, set matrix[i][j] = 0
# tc - O(m * n), sc - O(m + n)

# method - iterate through the matrix, if matrix[i][j] == 0, set matrix[0][j] = 0 and set matrix[i][0] = 0.
# iterate through the matrix again and for each matrix[i][j] if matrix[0][j] or matrix[i][0] == 0, set matrix[i][j] = 0
# tc - O(m * n), sc - O(1)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        set_row_zero, set_col_zero = False, False
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[0][c], matrix[r][0] = 0, 0

                    if r == 0: set_row_zero = True
                    if c == 0: set_col_zero = True
        

        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if set_row_zero:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0
        
        if set_col_zero:
            for r in range(len(matrix)):
                matrix[r][0] = 0
                
        

        

                    