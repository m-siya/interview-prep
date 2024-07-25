# ### PALINDROME PARTITIONING

# Given a string s, partition s such that every 
# substring
#  of the partition is a 
# palindrome
# . Return all possible palindrome partitioning of s.

# https://leetcode.com/problems/palindrome-partitioning/description/?envType=problem-list-v2&envId=50v8wybv&

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # check every cut off point and check if substr[j..i] is a palindrome
        # at every point can cut or not cut

        def isPalindrome(j, i):
            while j < i:
                if s[j] != s[i]:
                    return False
                
                i -= 1
                j += 1
            
            return True
        
        res = []
        
        def f(j, partitions):
            # f(j) should return multiple lists of how partitioning can be done starting from index j
            if j == len(s):
                res.append(partitions[:])
                return
            
            for i in range(j, len(s)):
               # print(isPalindrome(j, i), j, i, s[j: i + 1])
                if isPalindrome(j, i):
                    partitions.append(s[j:i + 1])
                    f(i + 1, partitions)
                    partitions.pop()
        
        f(0, [])
        return res
            

                    
        