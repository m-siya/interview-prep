# ### FIND LONGEST SUBSTRING CONTAINING VOWELS IN EVEN COUNTS

# Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/description/

# use a mask with as many bits as 'states'. here we have 2^5 states. each state
# represents a vowel with a bit on or off for even or odd. 
# also keep an array\hash map to keep track of when was a particular state
# seen the earliest. 
# if we see the state again, then we know that in the middle (between curr and prev
# occurence) vowel count was incremented evenly. (adding 2 brings us back to og state in modulo 2 adding).
# so this must be a valid substring in the middle.
# so lets record the earliest occurence so we can maximize the length of the substring.

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mask = 0
        res = 0 
        last_seen_state = [-1] * 32

        for i, c in enumerate(s):
            if c in 'aeiou':
                idx = ord(c) - ord('a')
               # print(idx)
                mask ^= 1 << ('aeiou'.find(c))
               # print(mask)
            
            #the earliest that mask was 0 is always the initial state 
            # so if we dont check for when mask != 0, we will lose this info
            
            if mask != 0 and last_seen_state[mask] == -1: 
                last_seen_state[mask] = i
            res = max(res, i - last_seen_state[mask])
        
        return res



