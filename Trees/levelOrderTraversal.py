# ### BINARY TREE RIGHT SIDE VIEW


# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes
# you can see ordered from top to bottom.

# https://leetcode.com/problems/binary-tree-right-side-view/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        q = collections.deque()
        q.append(root)
        
        while q:
            level = []
            q_len = len(q)

            for _ in range(q_len):
                curr_node = q.popleft()
                if curr_node:
                    level.append(curr_node.val)
                    q.append(curr_node.left)
                    q.append(curr_node.right)
            
            if level:
                answer.append(level[-1])
        
        return answer
