class Node:
    def __init__(self, ch):
        self.ch = ch
        self.neighbours = {}
        self.leaf = False

class WordDictionary:

    def __init__(self):
        self.root = Node("-")

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c in cur.neighbours:
                cur = cur.neighbours[c]
            else:
                node = Node(c)
                cur.neighbours[c] = node
                cur = node
        cur.leaf = True
        

    def search(self, word: str) -> bool:
        #print("searching for :", word)
        def dfs(w, node):
            cur = node
            for i, c in enumerate(w):
                if c == ".":
                    for n in cur.neighbours.values():
                        #print("neighbour ", n.ch)
                        if dfs(w[i+1:], n):
                            #print("failed on ", w)
                            return True
                    return False
                else:
                    # print(cur.neighbours)
                    if c in cur.neighbours:
                        cur = cur.neighbours[c]
                    else:
                        # print("failed on ", w, c)
                        return False
            return cur.leaf
        return dfs(word, self.root)
