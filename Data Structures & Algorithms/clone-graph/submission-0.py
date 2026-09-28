"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.m = {}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        if node.val in self.m:
            return self.m[node.val]
        new = Node(node.val)
        self.m[new.val] = new
        for n in node.neighbors:
            new.neighbors.append(self.cloneGraph(n))
        return new
