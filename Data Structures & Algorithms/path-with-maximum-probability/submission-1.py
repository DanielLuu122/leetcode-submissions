class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        dist = [float('-inf')] * n
        dist[start_node] = 1

        h = []

        def hpop(h):
            [dist, v] = heapq.heappop(h)
            return (-dist, v)
        def hpush(h, dist, v):
            heapq.heappush(h, (-dist, v))
        
        adj = defaultdict(list)
        for i in range (len(edges)):
            [a, b] = edges[i]
            adj[a].append((b, succProb[i]))
            adj[b].append((a, succProb[i]))
        
        hpush(h, 1, start_node)

        while len(h) > 0:
            [d, v] = hpop(h)
            if d < dist[v]:
                continue
            if v == end_node:
                return d
            for [u, prob] in adj[v]:
                if dist[u] < dist[v] * prob:
                    dist[u] = dist[v] * prob
                    hpush(h, dist[u], u)
        if dist[end_node] == float('-inf'):
            return 0
        return dist[end_node]

        

            


