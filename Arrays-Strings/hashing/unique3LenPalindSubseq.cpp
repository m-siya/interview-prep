// ### Unique Length-3 Palindromic Subsequences

// Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

// Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

// A palindrome is a string that reads the same forwards and backwards.

// A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted
//  without changing the relative order of the remaining characters.

// For example, "ace" is a subsequence of "abcde".

// method -> make a vector range to act as a hashmap to store first and last occurences of all characters
// then iterate through the characters and find all the unique characters between their first and last occurences
// time complexity -> O(N + (26 * N)), space complexity -> O(26 + N)

class Solution {
public:
    int countPalindromicSubsequence(string s) {
        vector<pair<int, int>> range (26, {-1, -1});
        int length = s.length();

        for (int i = 0; i < length; i++) {
            if (range[s[i] - 'a'].first == -1) range[s[i] - 'a'].first = i;
            else range[s[i] - 'a'].second = i;
        }

        int result = 0;
        for (int i = 0; i < 26; i++) {
            if (range[i].second != -1) {
                unordered_set<char> set;
                for (int j = range[i].first + 1; j < range[i].second; j++) {
                    set.insert(s[j]);
                }

                result += (int)set.size();
            }
        }
        return result;
    }
};