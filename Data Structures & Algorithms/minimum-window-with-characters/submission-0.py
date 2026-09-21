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
        subs = ""
        minLen = float("inf")
        while r < len(s):
            curr[s[r]] += 1
            
            if s[r] in freq and curr[s[r]] == freq[s[r]]:
                have += 1
            r += 1
            while have == need:
                curr[s[l]] -= 1
                if (r - l + 1) < minLen:
                    minLen = r - l + 1
                    subs = s[l:r]
                if s[l] in freq and curr[s[l]] < freq[s[l]]:
                    have -= 1
                l += 1
        return subs
            
