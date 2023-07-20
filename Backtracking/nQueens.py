# ### N QUEENS

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each 
# other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a 
# queen and an empty space, respectively.

# https://leetcode.com/problems/n-queens/description/

#first draft of solution
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        sols = []
        def backtrack(board, last_place):
            if board:
                last_col = last_place
                last_row = len(board) - 1
                for row in range(last_row):
                    for col in range(n):
                        if board[row][col] == 'Q' and ((col == last_col) or row - col == (last_row - last_col) or (row + col == last_row + last_col)):
                            #print(row, col, last_place, len(board) - 1)
                           # print("blocked") 
                            return

            if len(board) == n:
                sols.append(board[:])
                return

            for col in range(n):
                row = ('.' * col) + 'Q' + ('.' * (n - col - 1))
                board.append(row)
                backtrack(board, col)
                board.pop()
        
        backtrack([], 0)
       # print(len(sols))
        return sols
    
# leetcode solution, faster + cleaner
# doing DFS(queens + [queen], xy_diff + [rows - queen], xy_sum + [rows + queen]) is equivalent to 
# doing - queens.append(queen), xy_diff.append(rows - queen), xy_sum + [rows + queen] 
#       - DFS(queens, xy_diff, xy_sum)
#       - queens.pop(), xy_diff.pop(), xy_sum.pop()
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        sols = []

        def DFS(queens, xy_diff, xy_sum):
            rows = len(queens)
            if rows == n:
                sols.append(queens)
                return 
            
            for queen in range(n):
                if queen not in queens and rows - queen not in xy_diff and rows + queen not in xy_sum:
                    DFS(queens + [queen], xy_diff + [rows - queen], xy_sum + [rows + queen])

        DFS([], [], [])
#print(sols)
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in sol] for sol in sols]
