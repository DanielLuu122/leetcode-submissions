# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return "n"
        s = str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)
        # print(s)
        return s
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(",")
        i = -1
        def dfs():
            nonlocal i
            i += 1
            if arr[i] == "n":
                return None
            node = TreeNode(int(arr[i]))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

