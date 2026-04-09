# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        q = deque()
        ans = []
        level = {}
        q.append(root)
        level[root] = 0
        currLevel = 0
        tempLevel = []
        while len(q) > 0:
            v = q.popleft()
            if level[v] != currLevel:
                ans.append(tempLevel)
                tempLevel = []
                currLevel += 1
            tempLevel.append(v.val)
            l = v.left
            r = v.right
            if l != None:
                q.append(l)
                level[l] = level[v] + 1
            if r != None:
                level[r] = level[v] + 1
                q.append(r)
        ans.append(tempLevel)
        return ans




        