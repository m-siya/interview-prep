# ### NUMBER OF SUBSTRINGS CONTAINING ALL 3 CHARACTERS

# Given a string s consisting only of characters a, b and c.

# Return the number of substrings containing at least one occurrence of all these characters a, b and c.

# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

# method - keep the r pointer to keep track of the end of the substring. 
# as soon as s[l: r + 1] becomes a valid substring, increment l to decrease the window of the substring
# and check till where it is valid

# tc - O(N), sc - O(1)
class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        res = 0
        l = 0

        found = {'a': 0, 'b': 0, 'c': 0}
        for r in range(len(s)):
            #r increases the length of the substring
            found[s[r]] += 1

            while found['a'] and found['b'] and found['c']:
              #  print(s[l:r + 1])
                found[s[l]] -= 1
                l += 1
            res += l #because there can be l substrings starting from 0 to l which fit the criteria
            #[l - 1 .. r] represents minimum length sub-array ending at r which has all three characters.
                    #   this subarray could be extended left till l == 0 without compromising the count constraint
                    #   which is a total of length([0..l-1]) = l subarrays ending at r
        
        return res
    

