// 463. Island Perimeter

// You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

// Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

// The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

// run dfs starting from a tile of the island and add 1 whenever 
// a "boundary" is encountered i.e when met with water or bounds of
// the grid. return 0 if cell seen is already visited
// cut down on the use of a visited array by marking cells visited 
// by a -1.
// at the end iterate through the grid  till first island is found
// then run dfs there and return value of perimeter

// TC: O(NM)
// SC: O(NM) due to recursion
class Solution {
private:
    int p = 0;

    void dfs(vector<vector<int>>&grid, int i, int j) {
        if (i < 0 || j < 0 || i >= grid.size() || j >= grid[0].size() || grid[i][j] == 0) {
            p++;
            return;
        }

        if (grid[i][j] == -1) return;

        grid[i][j] = -1;
        dfs(grid, i + 1, j);
        dfs(grid, i, j + 1);
        dfs(grid, i - 1, j);
        dfs(grid, i, j - 1);
    }

public:
    int islandPerimeter(vector<vector<int>>& grid) {
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == 1){
                    dfs(grid, i, j);
                    return p;
                }
            }
        }
        return p;
        
    }
};

//optimization -> iterate through all cells and if find a cell with 1
// add +4 to the perim, if cell has upper and left neighbours then -2 for 
// each because that means two cells share a boundary.
// we dont do this for right and below because those have not been 
// seen yet and if we do it then it'll lead to duplication

// TC: O(MN)
// SC: O(1)

class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int perim = 0;
        for (int i = 0; i < grid.size(); i++){
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == 1){
                    perim += 4;
                    if (i > 0 && grid[i - 1][j] == 1){
                        perim -= 2;
                    }
                    if (j > 0 && grid[i][j - 1] == 1) {
                        perim -= 2;
                    }
                }
                
            }
        }

        return perim;
        
    }
};
