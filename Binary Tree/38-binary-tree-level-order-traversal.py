"""
https://leetcode.com/problems/binary-tree-level-order-traversal/

Topics: BFS, Binary Tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        queue = list()
        result = list()
        level = list()
        cur_level = 0
        
        queue.append((root, cur_level))

        while queue:
            n, nl = queue.pop(0)
            if cur_level != nl:
                result.append(level)
                level = list()
                cur_level += 1
            level.append(n.val)
            if n.left:
                queue.append((n.left, nl + 1))
            if n.right:
                queue.append((n.right, nl + 1))
                
        result.append(level)
        return result
            
