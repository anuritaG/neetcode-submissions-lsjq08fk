# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return True, 0
            leftBln, leftH = dfs(node.left)
            rightBln, rightH = dfs(node.right)
            isBln = False
            if abs(leftH-rightH) <= 1 and leftBln and rightBln:
                isBln = True
            return isBln, 1 + max(dfs(node.left)[1], dfs(node.right)[1])
        isBln, height = dfs(root)
        return isBln
