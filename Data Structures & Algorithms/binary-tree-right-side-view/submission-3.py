# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # In BFS, store the value and height as well
        # Same thing just share the last element in each level
        queue  = []
        res = []
        if not root:
            return []
        queue.append([root, 0])
        while queue:
            element = queue.pop(0)
            height = element[1]
            node = element[0]
            if height < len(res):
                res[height] = node.val
            else:
                res.append(node.val)
            if node.left:
                queue.append([node.left, height+1])
            if node.right:
                queue.append([node.right, height+1])
        return res