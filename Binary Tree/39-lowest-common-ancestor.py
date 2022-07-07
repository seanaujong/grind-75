"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Topics: Binary Tree, DFS, Recursion

https://www.youtube.com/watch?v=13m9ZCB8gjw
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # base case: fail
        if not root:
            return None
        # base case: found p or q
        if root == p or root == q:
            return root
        # expand search
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # if we found p or q or the answer, propagate it
        # will also propagate null
        if not left: return right
        elif not right: return left
        # if we found p and q, propagate answer!
        else: return root
