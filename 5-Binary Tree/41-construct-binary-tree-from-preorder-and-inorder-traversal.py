"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Topics: Binary Tree, Divide and Conquer, Hash Table

https://www.youtube.com/watch?v=PoBGyrIWisE
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34538/My-Accepted-Java-Solution

PRE[0] is the root node
Find PRE[0] in IN (say it is IN[5])
IN[5] is the root node, so IN[0:4] is the left subtree,
and IN[6:] is the right subtree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(preorder, preLow, preHigh,
                 inorder, inLow, inHigh):
            if preLow > preHigh or inLow > inHigh:
                return None
            
            # root in preorder is the lowest index
            root = TreeNode(preorder[preLow])
            
            # now find root in inorder
            inorderRoot = inLow
            for i in range(inLow, inHigh + 1):
                if inorder[i] == root.val:
                    inorderRoot = i
                    break
            
            lenLeftTree = inorderRoot - inLow
            root.left = build(preorder, preLow + 1, preLow + lenLeftTree,
                             inorder, inLow, inorderRoot - 1)
            root.right = build(preorder, preLow + lenLeftTree + 1, preHigh,
                              inorder, inorderRoot + 1, inHigh)
            return root
        
        return build(preorder, 0, len(preorder) - 1,
                    inorder, 0, len(inorder) - 1)
        
