# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            # print("left",node.val, " ", node.left, " ", node.right)
            if not node.left and not node.right and node.val == target:
                # print("nonde", node.val)
                return None
            return node
        dfs(root)
        if not root.left and not root.right and root.val == target:
            return None
        return root