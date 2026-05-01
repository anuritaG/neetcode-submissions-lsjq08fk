# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Search for the value in left/right sub-tree
        # When value found,replace deleted node with inorder successor of the value
        # Replace the parent -> deleted node with parent -> right child of deleted node
        # In case there is a single child, just do parent -> deleted node, parent -> deleted node's child
        if not root:
            return root
        if key > root.val:
            # takes care of new parent node -> deleted node conn
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # Find inorder successor
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            cur = root.right
            while cur.left:
                cur = cur.left
            cur.left = root.left
            res = root.right
            del root
            return res
        return root