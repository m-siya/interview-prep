// ### SURROUNDED REGIONS 

// Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

// A region is captured by flipping all 'O's into 'X's in that surrounded region.

//https://leetcode.com/problems/surrounded-regions/description/

//method -> dfs through all border adjacent O cells and set all of them as 'S'. then iterate through all the cells in 
//matrix and set the remaning O cells as X and the S cells as O.


class Solution {
    vector<vector<int>> directions = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
    set<pair<int, int>> visited;
    
public:
    void solve(vector<vector<char>>& board) {
        int ROWS = board.size(), COLS = board[0].size();

        for (int row = 0; row < ROWS; row++) {
            dfs(board, row, 0);
            dfs(board, row, COLS - 1);
        }

        for (int col = 0; col < COLS; col++) {
            dfs(board, 0, col);
            dfs(board, ROWS - 1, col);
        }

        for (int row = 0; row < ROWS; row++) {
            for (int col = 0; col < COLS; col++) {
                if (board[row][col] == 'O') board[row][col] = 'X';
                if (board[row][col] == 'S') board[row][col] = 'O';
            }
        }   
    }

    void dfs(vector<vector<char>>& board, int row, int col) {
        int ROWS = board.size(), COLS = board[0].size();

        if (row < 0 || col < 0 || row == ROWS || col == COLS || board[row][col] != 'O') return;

        board[row][col] = 'S';
        dfs(board, row + 1, col);
        dfs(board, row, col + 1);
        dfs(board, row - 1, col);
        dfs(board, row, col - 1);     
    }
};

// ### NUMBER OF ENCLAVES

// You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

// A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off 
// the boundary of the grid.

// Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

// https://leetcode.com/problems/number-of-enclaves/description/

// method -> same method as above [FLOOD FILL]. Requires changing the input grid.

class Solution {
public:
    int numEnclaves(vector<vector<int>>& board) {
        int ROWS = board.size(), COLS = board[0].size();

        for (int row = 0; row < ROWS; row++) {
            dfs(board, row, 0);
            dfs(board, row, COLS - 1);
        }

        for (int col = 0; col < COLS; col++) {
            dfs(board, 0, col);
            dfs(board, ROWS - 1, col);
        }

        int enclave_count = 0;

        for (int row = 0; row < ROWS; row++) {
            for (int col = 0; col < COLS; col++) {
                if (board[row][col] == 1) enclave_count++;
            }
        } 

        return enclave_count;        
    }

    void dfs(vector<vector<int>>& grid, int row, int col) {
        int ROWS = grid.size(), COLS = grid[0].size();

        if (row < 0 || col < 0 || row == ROWS || col == COLS || grid[row][col] == 0) return;

        grid[row][col] = 0;
        dfs(grid, row + 1, col);
        dfs(grid, row, col + 1);
        dfs(grid, row - 1, col);
        dfs(grid, row, col - 1);
    }
};

// method -> without modifying the input grid. we iterate throught the entire grid and do dfs on very land cell. if 
// while doing dfs we reach the boundary, return -1 to show that we must not consider this land cell cluster. else return
// the area of the land cluster

class Solution {
public:
    int numEnclaves(vector<vector<int>>& board) {
        int ROWS = board.size(), COLS = board[0].size();
        vector<vector<int>> visited (ROWS, vector<int> (COLS, 0));

        int enclave_count = 0;

        for (int row = 0; row < ROWS; row++) {
            for (int col = 0; col < COLS; col++) {
                if (board[row][col] == 1) {
                    int count = dfs(board, visited, row, col);
                    //cout << count << endl;
                    if (count != -1) enclave_count += count;
                }
            }
        } 

        return enclave_count;        
    }

    int dfs(vector<vector<int>>& grid, vector<vector<int>>& visited, int row, int col) {
        int ROWS = grid.size(), COLS = grid[0].size();

        if (row < 0 || col < 0 || row == ROWS || col == COLS) return -1;

        if (visited[row][col] == 1 || grid[row][col] == 0) return 0;

        visited[row][col] = 1;

        //grid[row][col] = 0;
        int bottom = dfs(grid, visited, row + 1, col);
        int right = dfs(grid, visited, row, col + 1);
        int up = dfs(grid, visited, row - 1, col);
        int left = dfs(grid, visited, row, col - 1);

        if (bottom == -1 || right == -1 || up == -1 || left == -1) return -1;
        else return 1 + bottom + right + up + left;
    }
};


 