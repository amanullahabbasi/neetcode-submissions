# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# At every node, do three things in this order: everything on my left, then me, then everything on my right. That’s the whole definition. Inorder of a BST = values from smallest to largest.

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            if node is None:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        values = inorder(root)
        return values[k - 1]