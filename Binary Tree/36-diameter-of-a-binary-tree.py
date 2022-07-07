"""
https://leetcode.com/problems/diameter-of-binary-tree/

Topics: Recursion, Binary Tree

https://leetcode.com/problems/diameter-of-binary-tree/discuss/101145/Simple-Python/591034

https://xlinux.nist.gov/dads/HTML/height.html

https://stackoverflow.com/questions/2603692/what-is-the-difference-between-tree-depth-and-height

https://stackoverflow.com/questions/11987358/why-nested-functions-can-access-variables-from-outer-functions-but-are-not-allo
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def height(root: Optional[TreeNode]) -> int:
            # height of an empty tree is -1 (undefined)
            if not root: return -1
            
            left = height(root.left)
            right = height(root.right)
            
            # +2 for the "not root" on the left
            # plus the "not root" on the right
            ans[0] = max(ans[0], 2 + left + right)
            
            return max(left, right) + 1
        height(root)
        return ans[0]
        
        
