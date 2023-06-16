### COUNT SUB ISLANDS

You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's 
(representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells 
outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up 
this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.

https://leetcode.com/problems/count-sub-islands/description/

class Solution {
    int subIslands = 0;
public:
    int countSubIslands(vector<vector<int>>& grid1, vector<vector<int>>& grid2) {
        int ROWS = grid2.size(), COLS = grid2[0].size();
        vector<vector<int>> visited (ROWS, vector<int> (COLS, 0));

        vector<vector<int>> directions = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
               // bool match = false;
                if (visited[r][c] == 1 || grid2[r][c] == 0 || grid1[r][c] == 0) continue;
                //bfs(grid2, grid1, visited, r, c, true);
                bool match = true;

                queue<pair<int, int>> q;
                visited[r][c] = 1;
                q.push({r, c});

                while(!q.empty()) {
                    pair <int, int> curr = q.front(); q.pop();
                    for (int i = 0; i < 4; i++) {
                        int row = curr.first + directions[i][0], col = curr.second + directions[i][1];
                        if (row < 0 || row == ROWS || col < 0 || col == COLS || visited[row][col] == 1 || grid2[row][col] == 0) continue;
                        
                        if (grid1[row][col] != 1) {
                            match = false;
                        }
                        visited[row][col] = 1;
                        q.push({row,col});
                    }
                }

                if (match == true) subIslands++;            
            }
        }

        return subIslands;
        
    }
};