# ### NUMBER OF WONDERFUL SUBSTRINGS

# A wonderful string is a string where at most one letter appears an odd number of times.

# For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
# Given a string word that consists of the first ten lowercase English letters ('a' through 'j'), return the number of wonderful non-empty substrings in word. If the same substring appears multiple times in word, then count each occurrence separately.

# A substring is a contiguous sequence of characters in a string.

# https://leetcode.com/problems/number-of-wonderful-substrings/description/


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = [0] * 1024
        count[0] = 1 #empty string mean all char have even freq
        mask = 0 #curr state
        res = 0

        for c in word:
            idx = ord(c) - ord('a') 
            mask ^= 1 << idx  #
#1 << idx shifts the binary representation of 1 to the left by idx positions, effectively creating a number with a single 1 bit at the position corresponding to the index of the current character.
#XORing this number with mask flips the bit at the corresponding position in mask.
            res += count[mask] #update how many times weve seen that state prev

            for i in range(10):
                look_for = mask ^ (1 << i)
                res += count[look_for]

            count[mask] += 1
        
        return res

        
            
