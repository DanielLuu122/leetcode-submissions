class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def count_island(i, j):
            if i < 0 or i >= n or j < 0 or j >= m:
                return 0
            if grid[i][j] == 1:
                grid[i][j] = 0
                return (1 
                + count_island(i + 1, j)
                + count_island(i, j+1)
                + count_island(i-1, j)
                + count_island(i, j-1))
            return 0
        max_island = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    max_island = max(max_island, count_island(i,j))
        
        return max_island