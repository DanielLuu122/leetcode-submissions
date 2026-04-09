class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        # construct edges, there are n^2 edges (one for every point)
        edges = []
        # edge = (weight, p1, p2)
        for i in range(n):
            for j in range(i + 1, n):
                p1 = points[i]
                p2 = points[j]
                distance = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                edges.append((distance, i, j))
        
        # component val
        parent = [i for i in range(n)]
        rank = [0 for _ in range(n)]
        def find(v):
            # not the root
            if parent[v] != v:
                parent[v] = find(parent[v])
            return parent[v]
        
        def union(p1, p2):
            root1 = find(p1)
            root2 = find(p2)
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1
        edges.sort()
        countEdges = 0
        total = 0
        for [distance, p1, p2] in edges:
            if find(p1) != find(p2):
                countEdges += 1
                union(p1, p2)
                total += distance
                if countEdges == n - 1:
                    return total
        return 0




