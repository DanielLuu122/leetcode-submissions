from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for p in prerequisites:
            adj[p[0]].append(p[1])
        visited = set()
        visiting = set()
        def dfs(v):
            if v in visited:
                return True
            if v in visiting:
                return False
            visiting.add(v)
            for n in adj[v]:
                if dfs(n) == False:
                    return False
            visited.add(v)
            visiting.remove(v)
            return True
        for i in range(numCourses):
            if i not in visited:
                if dfs(i) == False:
                    return False
        return True