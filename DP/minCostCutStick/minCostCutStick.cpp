#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minCost(int n, vector<int>& cuts) {
        cuts.push_back(0);
        cuts.push_back(n);
        int m = cuts.size();
        sort(cuts.begin(), cuts.end());

        vector<vector<int>> dp (m, vector<int> (m, -1));

        //lambda function - to define an anonymous function (closure) right where it is invoked
        //introduced in c++ 11
        // can introduce new variables in  body (c++ 14) and capture var from surrounding scope
// A lambda begins with the capture clause. It specifies which variables are captured, 
// and whether the capture is by value or by reference. Variables that have the ampersand (&) 
// prefix are accessed by reference and variables that don't have it are accessed by value.

// An empty capture clause, [ ], indicates that the body of the lambda expression accesses no variables 
// in the enclosing scope.

// You can use a capture-default mode to indicate how to capture any outside variables referenced in the
//  lambda body: [&] means all variables that you refer to are captured by reference, and [=] means they're 
//  captured by value


        function <int(int, int)> cost = [&] (int i, int j) -> int {
            if (j - i <= 1)
                return 0;

            if (dp[i][j] != -1) 
                return dp[i][j];

            int res = INT_MAX;

            for (int k = i + 1; k < j; k++) {
                int cutCost = cost(i, k) + cost(k, j);

                res = min(res, cutCost);
            }

            return dp[i][j] = res + (cuts[j] - cuts[i]) ;

        };

        return cost(0, m - 1);
    }
};