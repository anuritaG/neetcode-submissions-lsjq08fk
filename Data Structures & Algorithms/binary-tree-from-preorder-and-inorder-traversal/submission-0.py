# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Recursively build the tree. Find the index of root in inorder(mid)
        # Divide the array in 2 parts: inorder[0:mid] and preorder[1:mid+1]
        # Store the position in inorder - all elements left to a particular node in inorder belongs to its left subtree
        indices = {val: idx for idx, val in enumerate(inorder)}
        rootIndex = 0
        def dfs(l, r):
            nonlocal rootIndex
            if l > r:
                return None
            root_val = preorder[rootIndex]
            rootIndex += 1
            root = TreeNode(root_val)
            mid = indices[root_val]
            root.left = dfs(l, mid-1)
            root.right = dfs(mid + 1, r)
            return root
        return dfs(0, len(preorder)-1)
           
