### MINIMUM ABSOLUTE DIFFERENCE IN BINARY 

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two 
different nodes in the tree.

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int res = INT_MAX;
    int prev = - 1;

    int getMinimumDifference(TreeNode* root) {
        if (root == NULL) return res;

        getMinimumDifference(root->left);
        if (prev != -1) {
            res = min(res, root->val - prev);
        }
        prev = root->val;
        getMinimumDifference(root->right);
        return res;
        
    }
};