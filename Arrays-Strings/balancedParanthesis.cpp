// ### MINIMUM NUMBER OF SWAPS TO MAKE THE STRING BALANCED

// You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets '[' 
// and n / 2 closing brackets ']'.

// A string is called balanced if and only if:

// It is the empty string, or
// It can be written as AB, where both A and B are balanced strings, or
// It can be written as [C], where C is a balanced string.
// You may swap the brackets at any two indices any number of times.

// Return the minimum number of swaps to make s balanced.

// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/

class Solution {
public:
    int minSwaps(string s) {
        int swaps = 0;
        int open = 0, close = 0;
        int last_open = s.length() - 1;

        for (int i = 0; i < last_open; i++) {
            if (s[i] == '[') open++;
            if (s[i] == ']') close++;

            if (close > open) {
                swaps++;
                close--;
                open++;
            }

        }      
        return swaps;
    }
};

// ### MINIMUM ADD TO MAKE PARANTHESES VALID

// A parentheses string is valid if and only if:

// It is the empty string,
// It can be written as AB (A concatenated with B), where A and B are valid strings, or
// It can be written as (A), where A is a valid string.
// You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

// For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
// Return the minimum number of moves required to make s valid.

// https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/

// time complexity -> O(N), space complexity -> O(1)

class Solution {
public:
    int minAddToMakeValid(string s) {
        int add = 0;
       // int open = 0, close = 0;
       int invalid = 0;

        for (auto bracket: s) {
            if (bracket == '(') invalid++;
            
            if (bracket == ')') {
                invalid--;
                if (invalid < 0) {
                    add++;
                    invalid = 0;
                }
            }
        }

        //cout << open << " " << close << " " << abs(open - close);

        if (invalid > 0) return invalid + add;
        else return add;
        
    }
};