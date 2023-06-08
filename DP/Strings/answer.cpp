#include <iostream>
#include <vector>

using namespace std;

// ### LONGEST COMMON SUBSEQUENCE

// Given two strings text1 and text2, return the length of their longest common subsequence. If 
// there is no common subsequence, return 0.

// A subsequence of a string is a new string generated from the original string with some characters 
// (can be none) deleted without changing the relative order of the remaining characters.

// For example, "ace" is a subsequence of "abcde".
// A common subsequence of two strings is a subsequence that is common to both strings.

// https://leetcode.com/problems/longest-common-subsequence/description/

class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int length1 = text1.length();
        int length2 = text2.length();
        vector<vector<int>> dp (length1, vector <int> (length2, -1));

        function <int(int, int)> f = [&] (int i, int j) -> int {
            // f(i, j) -> length of longest common subsequence till ith character of 
            // text1 and jth character of text2
            if (i < 0 || j < 0)
                return 0;

            if (dp[i][j] != -1) 
                return dp[i][j];

            if (text1[i] == text2[j]) 
                return dp[i][j] = 1 + f(i - 1, j - 1);
            else 
                return dp[i][j] = max(f(i - 1, j), f(i, j - 1));
        };

        return f(length1 - 1, length2 - 1);      
    }
};

// ### LONGEST COMMON SUBSTRING
// A substring of a string is a subsequence in which all the characters are consecutive. Given 
// two strings, we need to find the longest common substring.

class Solution {
    public:
    int longestCommonSubstring(string text1, string text2) {
        int length1 = text1.length();
        int length2 = text2.length();
        vector<vector<int>> dp (length1, vector <int> (length2, -1));

        function <int(int, int)> f = [&] (int i, int j) -> int {
            // f(i, j) -> length of longest common subsequence till ith character of 
            // text1 and jth character of text2
            if (i < 0 || j < 0)
                return 0;

            if (dp[i][j] != -1) 
                return dp[i][j];

            if (text1[i] == text2[j]) 
                return dp[i][j] = 1 + f(i - 1, j - 1);
            else 
                return dp[i][j] = 0;
        };

        return f(length1 - 1, length2 - 1);      
    }
};

// ### LONGEST PALINDROMIC SUBSEQUENCE
// Given a string s, find the longest palindromic subsequence's length in s.

// A subsequence is a sequence that can be derived from another sequence by deleting some 
// or no elements without changing the order of the remaining elements.

class Solution {
public:
    int longestPalindromeSubseq(string s) {
       // vector<vector<int>> dp(s.size(), vector<int> (s.size(), -1));
        int length = s.size();
        vector<vector<int>> dp (length, vector<int> (length, -1));

        function <int(int, int)> f = [&] (int start, int end) -> int {
            // f(start, end) -> length of longest palindromic subsequence between
            // start index and end index
            if (start > end)
                return 0;

            if (start == end)
                return 1;
            
            if (dp[start][end] != -1)
                return dp[start][end];

            if (s[start] == s[end]) 
                return dp[start][end] = 2 + f(start + 1, end - 1);
            else
                return dp[start][end] = max(f(start, end - 1), f(start + 1, end));
        };

        return f(0, length - 1);
        
    }
};


// ### LONGEST PALINDROMIC SUBSTRING
// Given a string s, return the longest palindromic substring in s.

// https://leetcode.com/problems/longest-palindromic-substring/




// ### MINIMUM INSERTIONS TO MAKE A STRING PALINDROME

// Given a string s. In one step you can insert any character at any index of the string.

// Return the minimum number of steps to make s palindrome.

// A Palindrome String is one that reads the same backward as well as forward.

// https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/description/

class Solution {
public:
    int minInsertions(string s) {
        int length = s.size();
        vector<vector<int>> dp (length, vector<int> (length, -1));

        function <int(int, int)> longestPalindromicSubseq = [&] (int start, int end) -> int {
            if (start > end)
                return 0;
            if (start == end)
                return 1;

            if (dp[start][end] != -1)
                return dp[start][end];

            if (s[start] == s[end])     
                return dp[start][end] = 2 + longestPalindromicSubseq(start + 1, end - 1);
            else
                return dp[start][end] = max(longestPalindromicSubseq(start, end - 1), longestPalindromicSubseq(start + 1, end));
        };

        return length - longestPalindromicSubseq(0, length - 1);
        
    }
};

// ### DELETE OPERATIONS FOR TWO STRINGS

// Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

// In one step, you can delete exactly one character in either string.

// https://leetcode.com/problems/delete-operation-for-two-strings/description/

// find the longest common subsequence and subtract that from the sum of the 
// lengths of the two strings.

class Solution {
public:
    int minDistance(string word1, string word2) {
        int length1 = word1.length();
        int length2 = word2.length();

        vector<vector<int>> dp (length1 + 1, vector<int> (length2 + 1, 0));

        for (int i = 0; i < length1; i++) {
            dp[i][0] = 0;
        }
        
        for (int i = 0; i < length2; i++) {
            dp[0][i] = 0;
        }

        for(int i = 1; i < length1 + 1; i++) {
            for(int j = 1; j <length2 + 1; j ++) {
                //cout << i << " " << j << endl;
                // if (i == 0 || j == 0) 
                //     dp[i][j] = 0;
                if (word1[i - 1] == word2[j - 1])
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                else
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
       // cout << length1 << length2 << dp[length1][length2];
        return length1 + length2 - 2 * dp[length1][length2];
    }
};



