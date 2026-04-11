class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for [u,v,t] in times:
            adj[u].append((v,t))
        heap = []
        heapq.heappush(heap, (0, k))
        d = [float('inf')] * (n + 1)
        d[k] = 0
        while heap:
            p, y = heapq.heappop(heap)
            if p > d[y]:
                continue # invalid entry, skip
            for z, t in adj[y]:
                if d[y] + t < d[z]:
                    d[z] = d[y] + t
                    heapq.heappush(heap, (d[z], z))
        m = max(d[1:])
        if m != float('inf'):
            return m
        return -1


            