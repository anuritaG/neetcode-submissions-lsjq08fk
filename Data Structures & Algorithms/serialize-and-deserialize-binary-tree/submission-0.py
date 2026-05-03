# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        values = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                print(node.val)
                if node.left:
                    print("left", node.left.val)
                if node.right:
                    print("right", node.right.val)
                values.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                values.append("null")
        res = ",".join(map(str, values))
        print(res)
        return res
            
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        if values[0] == "null":
            return None
        idx = 1
        root = TreeNode(values[0])
        queue = [root]
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

