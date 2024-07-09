# ### LEXICOGRAPHICALLY SMALLEST EQUIVALENT STRING

# You are given two strings of the same length s1 and s2 and a string baseStr.

# We say s1[i] and s2[i] are equivalent characters.

# For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
# Equivalent characters follow the usual rules of any equivalence relation:

# Reflexivity: 'a' == 'a'.
# Symmetry: 'a' == 'b' implies 'b' == 'a'.
# Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
# For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.

# Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.


# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/description/

class UF:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n + 1)]
        self.smallest = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    
    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)

        if p1 == p2:
            self.smallest[p1] = min(self.smallest[p1], self.smallest[p2])
            return 0
        
        if self.rank[p1] > self.rank[p2]:
            self.rank[p1] += self.rank[p2]
            self.par[p2] = p1
        else:
            self.rank[p2] += self.rank[p1]
            self.par[p1] = p2

        
        self.smallest[p2] = min(self.smallest[p2], self.smallest[p1])
        self.smallest[p1] = min(self.smallest[p2], self.smallest[p1])

        self.n -= 1
        return 0
    
    def isConnected(self):
        return self.n <= 1
    
    def getSmallest(self, x):
        return self.smallest[self.find(x)]
              
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # letters are nodes and equivalent nodes are connected/have an edge
        # so for each node (letter) in given base str, find the lexographically smallest char in the connected comp of that letter
        ds = UF(26)
       # letters = {i: }
        for i in range(len(s1)):
            ds.union(ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a'))
        
        res = []
        for i in range(len(baseStr)):
           # print(ord(baseStr[i]) - ord('a'))
            node = ds.getSmallest(ord(baseStr[i]) - ord('a'))
            letter = chr(node + ord('a'))
            res.append(letter)
        
        return ''.join(res)
        





        