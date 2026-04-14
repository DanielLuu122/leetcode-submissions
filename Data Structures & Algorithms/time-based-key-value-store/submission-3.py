import bisect
class TimeMap:

    def __init__(self):
        self.m = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.m[key]
        index = bisect.bisect_right(arr, timestamp, key=lambda v:v[0]) - 1
        #print(index, arr, timestamp)
        if index > len(arr) or index < 0:
            return ""
        return arr[index][1]
