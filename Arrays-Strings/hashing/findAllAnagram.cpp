// ### FIND ALL ANAGRAMS IN A STRING

// Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the
//  answer in any order.

// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using
//  all the original letters exactly once.

// https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

// method used sliding window
// time complexity -> O(26 * N), space complexity -> O(26)

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> letters (26, 0);
        for (auto c: p) {
            letters[c - 'a']++;
        }

        vector<int> ans;

        int slen = s.length();
        int plen = p.length();

        if (slen < plen) return ans;

        vector<int> substr (26, 0);

        for (int i = 0; i < plen; i++) {
            substr[s[i] - 'a']++;
        }

        if (substr == letters) ans.push_back(0);

        for (int i = plen; i < slen; i++) {
            substr[s[i - plen] - 'a']--;
            substr[s[i] - 'a']++;

            if (substr == letters) ans.push_back(i - plen + 1);
        }

        return ans;
        
    }
};