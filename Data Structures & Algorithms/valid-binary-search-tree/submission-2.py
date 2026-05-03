# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Highest Value in the left < node.val
        # Lowest Value in the right > node.val
        # DFS method
        def dfs(node, leftB, rightB):
            # print(node.val, " ", leftB, " ",rightB)
            if not (leftB < node.val < rightB):
                # print(node.val, " ", leftB, " ",rightB)
                return False
            val = True
            if node.left:
                # print("yes", node.left.val, " ", leftB)
                val = val and dfs(node.left, leftB, node.val)
            if node.right:
                val = val and dfs(node.right, node.val, rightB)
            return val
        return dfs(root, float("-inf"), float("inf"))
       