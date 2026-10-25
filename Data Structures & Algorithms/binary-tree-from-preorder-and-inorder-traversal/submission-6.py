# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#Slow O(n2)
# class Solution:        
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         if not preorder or not inorder:
#             return None
#         root = TreeNode(preorder[0])
#         mid = inorder.index(preorder[0])
#         root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
#         root.right = self.buildTree(preorder[mid +1 :], inorder[mid + 1:])
#         return root

#On we need to use dictionary for this

class Solution: 
    def buildTree(self, preorder: List[int], inorder: List[int]):
        pos = {}
        for i, val in enumerate(inorder):
            pos[val] = i

        pre_idx = 0

        def build(l, r):
            nonlocal pre_idx
            if l > r:
                return None
            root = TreeNode(preorder[pre_idx])
            pre_idx += 1
            mid = pos[root.val]
            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)
            return root

        return build(0, len(inorder) - 1)

#Inorder and preorder are traversals 
#Inorder is used to find left and right teams 
#preorder is used to find the root boss each time.
#Dic is more efficient then indexing 
#Slicing inorder makes copies, passing ranges is better (l,r) and having mid from dict
#slicing preorder is inefficient its better to have ponter which iterates over the list to help us track bosses(roots)
