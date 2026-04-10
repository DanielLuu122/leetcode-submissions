class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')] * n
        dist[src] = 0

        for _ in range(k + 1):
            tempDist = dist[:]
            for [s, d, p] in flights:
                if dist[s] + p < tempDist[d]:
                    tempDist[d] = dist[s] + p
            dist = tempDist[:]
        
        if dist[dst] == float('inf'):
            return -1
        return dist[dst]
