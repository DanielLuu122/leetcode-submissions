class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            t = tuple(count)
            temp[t].append(s)
        res = []
        for arr in temp.values():
            res.append(arr)
        return res