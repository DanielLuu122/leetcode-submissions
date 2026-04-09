class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def remove_island(i, j):
            if i < 0 or i >= n or j < 0 or j >= m:
                return
            if grid[i][j] == '1':
                grid[i][j] = '0'
                remove_island(i + 1, j)
                remove_island(i, j+1)
                remove_island(i-1, j)
                remove_island(i, j-1)
            return
        total = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    total += 1
                    remove_island(i,j)
        
        return total