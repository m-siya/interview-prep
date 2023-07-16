### DIAMETER OF BINARY TREE

# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or 
# may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

# https://leetcode.com/problems/diameter-of-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        if not root:
            return 0
        else:
            return 1 + max(self.height(root.left), self.height(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        else:
            return max(self.height(root.left) + self.height(root.right), max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right)))
        

        


