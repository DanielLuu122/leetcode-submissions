class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for [a, b] in prerequisites:
            # edge from b to a
            adj[b].append(a)
        ans = deque()
        visited = set()
        visiting = set()
        def dfs(v):
            if v in visited:
                return True
            if v in visiting:
                # cycle, return false
                return False
            visiting.add(v)
            for u in adj[v]:
                if dfs(u) == False:
                    return False
            visiting.remove(v)
            visited.add(v)
            ans.appendleft(v)
        for i in range(numCourses):
            if i not in visited and dfs(i) == False:
                return []
        return list(ans)