# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
# starting with word1. If a string is longer than the other, append the additional letters onto the
# end of the merged string.

# Return the merged string.

# https://leetcode.com/problems/merge-strings-alternately/description/

#my sol
#functional approach

from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pair_wise = (zip_longest(word1, word2, fillvalue = ''))
        return ''.join(map(''.join, pair_wise))
