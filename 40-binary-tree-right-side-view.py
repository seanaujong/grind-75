"""
https://leetcode.com/problems/binary-tree-right-side-view/

Topics: Binary Tree, DFS, BFS
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
DFS
1. This is a special pre-order traversal which checks right first
before left
2. depth == len(result) makes sure only the first element
of that level (which will be the rightmost) will be added
3. if we switch the visit order, then we would see the left-side-view
"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        def rightView(root, result, depth):
            if not root: return
            if depth == len(result):
                result.append(root.val)
            rightView(root.right, result, depth + 1)
            rightView(root.left, result, depth + 1)
        rightView(root, result, 0)
        return result

"""
BFS
1. Append the rightmost node at each level
"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        if not root: return result
        queue = list()
        queue.append(root)
        
        while queue:
            right_most = float("-inf")
            for _ in range(len(queue)):
                cur = queue.pop(0)
                right_most = cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(right_most)
        return result
        
