from collections import Counter
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = Counter(t)
        curr = defaultdict(int)
        l = 0
        r = 0
        have = 0
        need = len(freq)
        min_l = 0
        min_r = 0
        minLen = float("inf")
        while r < len(s):
            curr[s[r]] += 1
            
            if s[r] in freq and curr[s[r]] == freq[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < minLen:
                    minLen = r - l + 1
                    min_r = r
                    min_l = l
                curr[s[l]] -= 1
                if s[l] in freq and curr[s[l]] < freq[s[l]]:
                    have -= 1
                l += 1
            r += 1
        return s[min_l:min_r + 1] if minLen != float("inf") else ""
            
