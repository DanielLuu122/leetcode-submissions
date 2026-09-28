class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visiting = set()
        visited = set()
        def dfs(node, parent):
            # print("dfs on ", node)
            if node in visiting:
                print(node)
                return False
            if node in visited:
                return True
            visiting.add(node)
            for n in adj[node]:
                if n != parent and not dfs(n, node):
                    return False
            visiting.remove(node)
            visited.add(node)
            return True
        for i in range(n):
            if not dfs(i, -1):
                return False
        return len(edges) == n-1