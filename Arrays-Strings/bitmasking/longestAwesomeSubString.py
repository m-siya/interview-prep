# ### LONGEST AWESOME SUBSTRING
# You are given a string s. An awesome substring is a non-empty substring of s such that we can make any number of swaps in order to make it a palindrome.

# Return the length of the maximum length awesome substring of s.

# https://leetcode.com/problems/find-longest-awesome-substring/description/

class Solution:
    def longestAwesome(self, s: str) -> int:
        mask = 0
        res = 0
        last_seen_state = [-1] + [len(s)] * 1023

        for i, c in enumerate(s):
            mask ^= 1 << int(c) #flip bit
            
            for digit in range(10):
                oneOffMask = mask ^ ( 1 << digit)
        #        print(oneOffMask)
                res = max(res, i - last_seen_state[oneOffMask])     
            res = max(res, i - last_seen_state[mask])
            last_seen_state[mask] = min(last_seen_state[mask], i)

        return res
        