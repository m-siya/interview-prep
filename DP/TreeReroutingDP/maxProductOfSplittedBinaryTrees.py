# ### MAXIMUM PRODUCT OF SPLITTED BINARY TREES    

# Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

# Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

# Note that you need to maximize the answer before taking the mod and not after taking it.

# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        
        # dp to select which edge to remove
        # two options at each root, remove left edge or remove right edge
        memo = {}

        def getSum(root):
            if not root:
                return 0
            
            if root in memo:
                return memo[root]
            
            res = root.val + getSum(root.left) + getSum(root.right)
            memo[root] = res
            return res
        
        totSum = getSum(root)
       # print(totSum)

        def f(root):
            if not root:
                return 0

            # find sum of subtree
            subtree_sum = getSum(root)

            return max(subtree_sum * (totSum - subtree_sum), f(root.left), f(root.right))

        return f(root) % MOD



