# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        cur = root
        valueNode = TreeNode(val)
        if not root:
            return valueNode
        while cur:
            if val < cur.val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = valueNode
                    break
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = valueNode
                    break
        
        return root