### BINARY TREE MAXIMUM PATH SUM

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge
# connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass 
# through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float('-inf')

        def get_max_path_sum(root):
            nonlocal max_path
            if not root:
                return 0
            
            left_gain = max(get_max_path_sum(root.left), 0)
            right_gain = max(get_max_path_sum(root.right), 0)
            current_max_path = root.val + left_gain + right_gain
            max_path = max(max_path, current_max_path)

            return root.val + max(left_gain, right_gain)
        
        get_max_path_sum(root)
        return max_path

        
        
