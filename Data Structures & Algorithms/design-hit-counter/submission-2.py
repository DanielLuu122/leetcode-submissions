from bisect import bisect_right
class HitCounter:

    def __init__(self):
        self.q = []

    def hit(self, timestamp: int) -> None:
        if self.q and self.q[-1][0] == timestamp:
            self.q[-1][1] += 1
        else:
            self.q.append([timestamp, 1])
    
    def getHits(self, timestamp: int) -> int:
        idx = bisect_right(self.q, timestamp - 300, key=lambda x: x[0])
        hits = 0
        while idx < len(self.q) and self.q[idx][0] <= timestamp:
            hits += self.q[idx][1]
            idx += 1
        return hits
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
