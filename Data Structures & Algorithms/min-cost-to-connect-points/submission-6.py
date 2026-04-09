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
        component = [i for i in range(n)]
        def find(v):
            return component[v]
        def union(l1, l2):
            for i in range(n):
                if component[i] == l2:
                    component[i] = l1
        edges.sort()
        countEdges = 0
        total = 0
        for [distance, p1, p2] in edges:
            if find(p1) != find(p2):
                countEdges += 1
                union(find(p1), find(p2))
                total += distance
                if countEdges == n - 1:
                    return total
        return 0




