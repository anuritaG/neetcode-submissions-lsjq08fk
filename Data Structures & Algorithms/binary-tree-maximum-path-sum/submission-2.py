# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxVal = -1000
        # if not root.left and not root.
        def dfs(node):
            nonlocal maxVal
            if not node:
                return 0
            leftSub = dfs(node.left)
            rightSub = dfs(node.right)
            if leftSub < 0:
                leftSub = 0
            rightSub = max(rightSub, 0)
            maxVal = max(maxVal, node.val + leftSub + rightSub)
            maxVal = max(maxVal, node.val + max(leftSub, rightSub))
            return node.val + max(leftSub, rightSub)
        dfs(root)
        return maxVal