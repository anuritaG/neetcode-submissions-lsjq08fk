# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = [root]
        while queue:
            cur = queue.pop(0)
            cur.left, cur.right = cur.right, cur.left

            if cur.right:
                queue.append(cur.right)
            if cur.left:
                queue.append(cur.left)
        return root
