// Given a string s, find the longest palindromic subsequence's length in s.

// A subsequence is a sequence that can be derived from another sequence by 
// deleting some or no elements without changing the order of the remaining elements.

// https://leetcode.com/problems/longest-palindromic-subsequence/description/


// approach - using iterative DP which means bottom up.
// in the dp table, dp[row][col] = length of longest palindromic subsequence of substring formed from index i to j

// if in dp table, row == column, we are talking about the same letter so it _can_ be considered for palindromic 
// subsequence so dp[i][i] = 1
// if in dp table, s[row] == s[column], then the characters are equal and together add +2 to the palindromic subsequence 
// length

// else we need to find max of dp[row + 1][col], dp[row][col - 1]; i.e longest palindromic subsequence not considering start 
// and end respectively.

//
class Solution {
public:
    int longestPalindromeSubseq(string s) {
       // vector<vector<int>> dp(s.size(), vector<int> (s.size(), -1));
        int n = s.size();
        vector<vector<int>> dp(n, vector<int>(n));

        for (int i = n - 1; i >= 0; i--) {
            dp[i][i] = 1;

            for (int j = i + 1; j < n; j++) {
                if (s[i] == s[j]) {
                    dp[i][j] = 2 + dp[i + 1][j - 1];
                }
                else {
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j]);
                }
            }
        }      
        return dp[0][n - 1];
    }
};