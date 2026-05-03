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
            leftSub = max(dfs(node.left), 0)
            rightSub = max(dfs(node.right), 0)
            # considers the path leftSubtree + parent + rightSubtree
            maxVal = max(maxVal, node.val + leftSub + rightSub)
            # consider the path from parent to either of the subtree. 
            # this is to extend path upwards
            maxVal = max(maxVal, node.val + max(leftSub, rightSub))
            return node.val + max(leftSub, rightSub)
        dfs(root)
        return maxVal