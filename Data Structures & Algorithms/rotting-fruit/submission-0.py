from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        time = 0
        fresh = 0
        q = deque([])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1
        print(q)
        def add_q(i,j, t):
            nonlocal fresh
            if 0 <= i < n and 0 <= j < m and grid[i][j] == 1:
                grid[i][j] = 2
                fresh -= 1
                q.append((i, j, t))
        while q:
            i, j, t = q.popleft()
            time = max(time, t)
            add_q(i + 1, j, t + 1)
            add_q(i, j+1, t + 1)
            add_q(i-1, j, t + 1)
            add_q(i,j-1, t+1)
        return -1 if fresh > 0 else time


        