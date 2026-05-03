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
        # Use BFS to mark the range 
        queue = []
        queue.append((root, float("-inf"), float("inf")))
        while queue:
            node, leftB , rightB = queue.pop()
            if not (leftB < node.val < rightB):
                return False
            if node.left:
                queue.append((node.left, leftB, node.val))
            if node.right:
                queue.append((node.right, node.val, rightB))
        return True