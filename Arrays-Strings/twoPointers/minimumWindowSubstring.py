# ### MINIMUM WINDOW SUBSTRING
# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

#  https://leetcode.com/problems/minimum-window-substring/

# there may be other characters in the substring of s

# method - brute force, gives tle on the last test case
# tc - O(m ^ 2), sc - O(n)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = float('inf')

        t_counts = Counter(t)
        ans = []

        for l in range(len(s)):
            seen = defaultdict(int)
            
            r = l
            while r < len(s):
                if t_counts[s[r]] > 0 and seen[s[r]] < t_counts[s[r]]:

                    seen[s[r]] += 1
                res = min(res, r - l + 1)
                r += 1
            
                if seen == t_counts:
                    ans.append(s[l : r])
                    break
        
        if ans: 
            ans = sorted(ans, key = lambda x: len(x))
            print(ans)
            return ans[0]

        return ""        



# optimised sol based on substr template in README.md

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = Counter(t)

        start, end = 0, 0

        min_window_length, min_window_start = len(s) + 1, 0

        num_char_t = len(t)

        while end < len(s):
            if s[end] in t_counts:
                if t_counts[s[end]] > 0:
                    num_char_t -= 1
                t_counts[s[end]] -= 1
            

            while num_char_t == 0:
                #current window has all desired chars
                #see if window can be smaller

                if end - start + 1 < min_window_length:
                    min_window_length = end - start + 1
                    min_window_start = start

                #basically remove s[start] from consideration
                if s[start] in t_counts:
                    t_counts[s[start]] += 1

                    if t_counts[s[start]] > 0:
                        num_char_t += 1
                
                start += 1
            
            end += 1

        
        return s[min_window_start:min_window_start+min_window_length] if min_window_length != len(s) + 1 else ""
