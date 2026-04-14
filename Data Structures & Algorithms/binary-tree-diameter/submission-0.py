# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0
        def countPath(node):
            if node == None:
                return 0
            heightLeft = countPath(node.left)
            heightRight = countPath(node.right)
            self.maxDiameter = max(self.maxDiameter, heightLeft + heightRight)
            return max(heightLeft, heightRight) + 1
        countPath(root)
        return self.maxDiameter