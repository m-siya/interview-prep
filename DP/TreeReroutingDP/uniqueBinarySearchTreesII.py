# ### UNIQUE BINARY SEARCH TREES II

# Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

# https://leetcode.com/problems/unique-binary-search-trees-ii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        res = []

        def f(i, j):
            if i > j:
                return [None]
            
            trees = []
            for k in range(i, j + 1):
                left, right = f(i, k - 1), f(k + 1, j)
                
                for l in left:
                    for r in right:
                        root = TreeNode(k)
                        root.left = l
                        root.right = r
                        trees.append(root)
            
            return trees
        
        return f(1, n)
        
            



            
        