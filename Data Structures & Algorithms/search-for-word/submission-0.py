class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        visit = set()
        def dfs(r, c, w):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visit:
                return False
            visit.add((r, c))
            w += board[r][c]
            if w == word:
                return True
            
            found = dfs(r + 1, c, w) or dfs(r - 1, c, w) or dfs(r, c + 1, w) or dfs(r, c-1, w)
            visit.remove((r, c))
            return found
            

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, ""):
                    return True
        return False
