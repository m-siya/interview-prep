// ### 01 MATRIX

// Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

// The distance between two adjacent cells is 1.

// https://leetcode.com/problems/01-matrix/description/

class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
        // start bfs from the zero cells and update distances for all non-zero cells in the bfs path
        int ROWS = matrix.size();
        if (ROWS == 0) return matrix;

        int COLS = matrix[0].size();

        // vector<vector<int>> dist (ROWS, vector<int> (COLS, ))
        queue<pair<int, int>> q;

        for (int r = 0; r < ROWS; r++) {
           for (int c = 0; c < COLS; c++) {
                if (matrix[r][c] == 0) 
                   q.push({r, c});
                else 
                    matrix[r][c] = -1;
           }
       }

    //    for (int i = 0; i < ROWS; i++) {
    //        for (int j = 0; j < COLS; j++) {
    //            cout << matrix[i][j] << " ";
    //        }
    //        cout << endl;
    //    }

        vector<vector<int>> directions = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};

        while (!q.empty()) {
           pair <int, int> curr = q.front(); q.pop();
           for (int i = 0; i < 4; i++) {
               int row = curr.first + directions[i][0], col = curr.second + directions[i][1];

               if (row < 0 || row == ROWS || col < 0 || col == COLS || matrix[row][col] != -1) continue;

               matrix[row][col] = matrix[curr.first][curr.second] + 1;
               q.push({row, col});
           }
        }

        return matrix;


    }
};