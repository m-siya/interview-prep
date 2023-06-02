#include <iostream>
#include <vector>
#include <bitset>

using namespace std;

class Solution {
public:
    int dfs(int i, vector<vector<int>> &adj_matrix, bitset <100> &detonated) {
        if (!detonated[i]) {
            detonated[i] = 1;
            for (int neighbour: adj_matrix[i])
                dfs(neighbour, adj_matrix, detonated);
        }
        return detonated.count();
    }

    int maximumDetonation(vector<vector<int>>& bombs) {
        int bombNumber = bombs.size();
        vector<vector<int>> adj_matrix(bombNumber);
        
        for (int i = 0; i < bombNumber; i++) {
            long long x_0 = bombs[i][0];
            long long y_0 = bombs[i][1];
            long long r = bombs[i][2];

            for (int j = 0; j < bombNumber; j++) {
                long long x = bombs[j][0];
                long long y = bombs[j][1];

                if ((x_0 - x) * (x_0 - x) + (y_0 - y) * (y_0 - y) <= r * r)     
                    adj_matrix[i].push_back(j);
            }
        }
        int max_detonated = 0;
        bitset <100> detonated = {};
        for (int i = 0; i < bombNumber; i++) {
            // initialize a new bitset for all dfs calls 
            max_detonated = max(max_detonated, dfs(i, adj_matrix, bitset<100>() = {}));
        }
        return max_detonated;
        
    }
};