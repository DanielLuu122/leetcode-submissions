class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        curr = self
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                curr.children[c] = TrieNode()
                curr = curr.children[c]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        res = set()
        def dfs(r, c, node: TrieNode, word):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return
            if (r, c) in visit:
                return
            if board[r][c] not in node.children:
                return
            visit.add((r, c))
            ch = board[r][c]
            node = node.children[ch]
            word += ch
            if node.isWord:
                res.add(word)
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)
            visit.remove((r, c))
            

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(res)
        