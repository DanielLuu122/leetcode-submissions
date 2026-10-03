class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        m = {}
        for i in range(len(s)):
            m[s[i]] = i
        ans = []
        last_start = -1
        idx = 0
        for i in range(len(s)):
            idx = max(m[s[i]], idx)
            if idx == i:
                idx = 0
                ans.append(i - last_start)
                last_start = i
        return ans

