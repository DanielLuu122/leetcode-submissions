class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[float('inf')] * n for _ in range(n)]
        dist[0][0] = grid[0][0]
        h = []
        heapq.heappush(h, (dist[0][0], 0, 0))
        def addHeap(h, old_d, i, j):
            if 0 <= i < n and 0 <= j < n:
                # valid pos
                if dist[i][j] > max(old_d, grid[i][j]):
                    dist[i][j] = max(old_d, grid[i][j])
                    heapq.heappush(h, (dist[i][j], i,j))

        while h:
            [d, r, c] = heapq.heappop(h)
            addHeap(h, d, r+1, c)
            addHeap(h, d, r - 1, c)
            addHeap(h, d ,r, c + 1)
            addHeap(h, d, r, c - 1)
        
        return dist[n-1][n-1]



