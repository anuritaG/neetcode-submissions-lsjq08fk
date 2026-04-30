# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def innode(node):
            if not node:
                return
            res.append(node.val)
            innode(node.left)
            innode(node.right)
        innode(root)
        return res