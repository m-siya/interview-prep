// ### TALLEST BILLBOARD
// You are installing a billboard and want it to have the largest height. The billboard will have two steel supports, one on each side. 
// Each steel support must be an equal height.

// You are given a collection of rods that can be welded together. For example, if you have rods of lengths 1, 2, and 3, you can weld them 
// together to make a support of length 6.

// Return the largest possible height of your billboard installation. If you cannot support the billboard, return 0.

// https://leetcode.com/problems/tallest-billboard/description/


//method - divide array into 2 subsets that have an equal sum. maximize that sum. this division is not exhaustive i.e we don't have to include
// all elements into our 2 subsets.
// this is a bit like partition equal subset except that not all elements need to be included
//

class Solution {
public:
    int tallestBillboard(vector<int>& rods) {
        int sum = reduce(rods.begin(), rods.end());

        vector<vector<vector<int>>> dp (rods.size(), vector<vector<int>> (sum + 1, vector<int> (sum + 1, -1)));

        function <int(int, int, int)> f = [&] (int i, int length1, int length2) -> int {
           // cout << length1 << " " << length2 << endl;
            if (length1 == length2) {
                //found a valid length
                return length1;
            }

            if (length2 < length1) {
                //invalid will not find any valid length now
                return 0;
            }

            if (i == rods.size()) {
                return 0;
            }

            if (dp[i][length1][length2] != -1) return dp[i][length1][length2]; 

            int addToFirst = f(i + 1, length1 + rods[i], length2 - rods[i]);
            int addToSecond = f(i + 1, length1, length2);
            int addToNone = f(i + 1, length1, length2 - rods[i]);
            //cout << addToFirst << " " << addToNone << endl;
            return dp[i][length1][length2] = max(addToNone, max(addToFirst, addToSecond));
        };

        return f(0, 0, sum);

        
    }
};