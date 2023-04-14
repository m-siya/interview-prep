# Given an integer array nums where the elements are sorted in ascending order, convert it to a 
# height-balanced binary search tree.

# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# approach : use the concept of binary search to determine the middle element
# since the BST needs to be balanced, so the middle element should be the root
# then for each left and right subtree, we need the middle element in nums[l, mid - 1] and
# nums [mid + 1, r] to make the root.

# time complexity : O(N)
# space complexity : O(N) (due the the recursive stack)
def minimalBST(nums):
    def helper(l, r):
        if (l > r): return None
        else:
            mid = (l + r) // 2
            root = TreeNode(mid)
            root.left = helper(l, mid - 1)
            root.right = helper(mid + 1, r)
            return root
    
    return helper(0, len(nums) - 1)