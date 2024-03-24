/*

    Given grid where '1' is land & '0' is water, return # of islands

    DFS, s et visited land to '0' to not visit it again, count islands

    https://leetcode.com/problems/number-of-islands/description/

    Time: O(m x n)
    Space: O(m x n)
*/

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        int result = 0;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    dfs(grid, i, j, m, n);
                    result++;
                }
            }
        }
        
        return result;
    }
private:
    void dfs(vector<vector<char>>& grid, int i, int j, int m, int n) {
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == '0') {
            return;
        }
        grid[i][j] = '0';
        
        dfs(grid, i - 1, j, m, n);
        dfs(grid, i + 1, j, m, n);
        dfs(grid, i, j - 1, m, n);
        dfs(grid, i, j + 1, m, n);
    }
};


//bfs solution
class Solution {
private:
    void bfs(int row, int col, vector<vector<char>>&grid) {
        grid[row][col] = '0';
        queue<pair<int, int>> q;

        q.push({row, col});
        int ROW = grid.size();
        int COL = grid[0].size();

        vector<pair<int, int>> directions = {{-1, 0}, {0, - 1}, {1, 0}, {0, 1}};

        while (!q.empty()) {
            int r = q.front().first;
            int c = q.front().second;
            q.pop();
            
            
            for (auto dir: directions) {
                int newRow = r + dir.first;
                int newCol = c + dir.second;

                if (newRow < 0 || newCol < 0 || newRow >= ROW || newCol >= COL || grid[newRow][newCol] == '0') {
                    continue;
                }
                grid[newRow][newCol] = '0';
                q.push({newRow, newCol});
            }
        }
    }
public:
    int numIslands(vector<vector<char>>& grid) {
        int ROW = grid.size();
        int COL = grid[0].size();

        int ans = 0;

        for (int i = 0; i < ROW; i++){
            for (int j = 0; j < COL; j++) {
                if (grid[i][j] == '1') {
                    bfs(i, j, grid);
                    ans += 1;
                }
            }
        }

        return ans;        
    }
};