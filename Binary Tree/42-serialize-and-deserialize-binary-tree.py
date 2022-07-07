"""
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Topics: String, Binary Tree, Preorder Traversal

https://www.youtube.com/watch?v=suj1ro8TIVY
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = list()
        def helper(root):
            if not root:
                result.append("#")
            else:
                result.append(str(root.val))
                helper(root.left)
                helper(root.right)
        helper(root)
        return ' '.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = iter(data.split())
        def helper():
            val = next(vals)
            if val == "#":
                return None
            root = TreeNode(int(val))
            root.left = helper()
            root.right = helper()
            return root
        return helper()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
