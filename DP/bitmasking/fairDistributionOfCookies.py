# ### FAIR DISTRIBUTION OF COOKIES

# You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag. You are also given an integer k that denotes the number of children to distribute all the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.

# The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.

# Return the minimum unfairness of all distributions.

# https://leetcode.com/problems/fair-distribution-of-cookies/description/

class Solution:
    def sum_cookies(self, mask, cookies):
        tot_cookies = 0
        for i, cookie in enumerate(cookies):
            if (1 << i) & mask:
                tot_cookies += cookie
        
        return tot_cookies
    
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        # split len(cookies) bags among k children
        # unfairness - max cookies for 1 child
        # 2, 4, 4, 4, 4 - // 2 = 9  , k = 3
        # 
        dp = [[-1 for _ in range(1 << len(cookies))] for _ in range(k + 1)]

        def f(k, mask):
            if k == 0:
                return 0 if mask == 0 else 1e9
            
            if dp[k][mask] != -1: return dp[k][mask]

            ans = 1e9
            curr_mask = mask
            while curr_mask > 0: # while all cookies are not assigned
                # give to curr kid
                curr_kid_cookies = self.sum_cookies(curr_mask, cookies)
                # give rest of cookies (those not given to curr kid) to other kids
                other_kids_cookies = f(k - 1, mask ^ curr_mask)
                ans = min(ans, max(curr_kid_cookies, other_kids_cookies))

                curr_mask = (curr_mask - 1) & mask # ( to generate all subsets in decreasing order)
            
            dp[k][mask] = ans
            return ans

        return f(k, (1 << len(cookies)) - 1)
                



        