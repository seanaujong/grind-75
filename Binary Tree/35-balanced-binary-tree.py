"""
https://leetcode.com/problems/balanced-binary-tree/

Topics: Binary Tree, DFS, Recursion

https://leetcode.com/problems/balanced-binary-tree/discuss/35691/The-bottom-up-O(N)-solution-would-be-better/198436
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # an empty tree is trivially balanced
        if not root:
            return True
        # height of tree starts from -1, so -2 is free to use as a flag
        return self.depth(root) != -2
        
    def depth(self, root: Optional[TreeNode]) -> int:
        # height of empty tree is -1
        if not root:
            return -1
        left = self.depth(root.left)
        right = self.depth(root.right)
        # balance check
        if abs(left - right) > 1 or left == -2 or right == -2:
            return -2
        return max(left, right) + 1
        
        
