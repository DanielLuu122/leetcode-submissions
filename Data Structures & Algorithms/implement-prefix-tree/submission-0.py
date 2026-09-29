class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                cur.children[c] = Node()
                cur = cur.children[c]
        cur.is_word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.is_word
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True