"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Topics: Binary Tree, Recursion

This is a quintessential pattern that is used in other problems
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def depth(root):
            # base case: depth of empty tree is 0
            if not root: return 0
            left = depth(root.left)
            right = depth(root.right)
            return max(left, right) + 1
        
        return depth(root)
