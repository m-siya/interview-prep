# ### LONGEST STRING CHAIN

# You are given an array of words where each word consists of lowercase English letters.

# wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

# For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
# A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

# Return the length of the longest possible word chain with words chosen from the given list of words.

# https://leetcode.com/problems/longest-string-chain/description/

from functools import lru_cache
class Solution:
    def compare(self, word1, word2):
        # return true if word1 is successor of word2

        if len(word1) != len(word2) + 1:
            return False
        
        extra = False
        i, j = 0, 0
       # print(word1, word2)
        while i < len(word1) and (not extra or j < len(word2)):
            if i < len(word1) and j < len(word2) :
                if word1[i] == word2[j]:
                    i += 1
                    j += 1
                else:
                    if extra: return False
                    i += 1
                    extra = True
            else:
                if not extra:
                    extra = True
                else:
                    return False
            
            
        return True
        
    def longestStrChain(self, words: List[str]) -> int:
        # to be a valid predecessor, must have same count of letters with 1 letter less
        # sequence should also be equal 
        # but how to check this in O(1)?
        # 

        words.sort(key=len)
        dp = [[-1 for _ in range(len(words) + 1)] for _ in range(len(words))]
        def f(i, prev_i):
            if i < 0: return 0

            if dp[i][prev_i] != -1:
                return dp[i][prev_i]

            #taking curr index
            leave = f(i - 1, prev_i)
            take = 0

            if (prev_i == len(words) or self.compare(words[prev_i], words[i])):
                take = 1 + f(i - 1, i)
            
            dp[i][prev_i] = max(take, leave)
            return dp[i][prev_i]
        
        return f(len(words) - 1, len(words))
        