class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(list)
        chars = set()

        if len(words) == 1:
            return words[0]

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i+1]
            for j in range(len(w1)):
                if j >= len(w2):
                    return ""
                if w1[j] != w2[j]:
                    # first char they differ
                    #w1 must come before w2
                    adj[w1[j]].append(w2[j])
                    # break after the first char, rest don't matter
                    break
            for c in w1:
                chars.add(c)
            for c in w2:
                chars.add(c)
        
            
        # toplogical sort with cycle detection

        visited = set()
        visiting = set()
        ans = list()

        def dfs(v):
            if v in visited:
                return True
            if v in visiting:
                return False
            visiting.add(v)
            for u in adj[v]:
                if dfs(u) == False:
                    return False
            visited.add(v)
            visiting.remove(v)
            ans.append(v)


        
        for c in chars:
            if dfs(c) == False:
                return ""

        ans.reverse()
        return "".join(ans)



            