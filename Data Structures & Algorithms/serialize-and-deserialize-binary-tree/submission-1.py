# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Store all the children in BFS. If children do not exist store null in that place
        values = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                values.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                values.append("null")
        res = ",".join(map(str, values))
        return res
            
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        if values[0] == "null":
            return None
        idx = 1
        root = TreeNode(values[0])
        queue = [root]
        # Append the children in queue. 
        # For the popped element, the unappended next 2 elements will be its children
        while queue:
            node = queue.pop(0)
            if idx < len(values):
                if values[idx] != "null":
                    nodeleft = TreeNode(values[idx])
                    node.left = nodeleft
                    queue.append(nodeleft)
                idx += 1
            if idx < len(values):
                if values[idx] != "null":
                    noderight = TreeNode(values[idx])
                    node.right = noderight
                    queue.append(noderight)
                idx += 1
            
        # root = TreeNode(12)
        return root

