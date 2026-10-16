class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        n = len(username)
        temp = []
        for i in range(n):
            temp.append((timestamp[i], website[i], username[i]))
        temp.sort()
        
        mp = defaultdict(list)
        for time, website, user in temp:
            mp[user].append(website)
        
        count = defaultdict(int)
        for user in mp:
            patterns = set()
            cur = mp[user]
            for i in range(len(cur)):
                for j in range(i + 1, len(cur)):
                    for k in range(j + 1, len(cur)):
                        patterns.add((cur[i], cur[j], cur[k]))
            for p in patterns:
                count[p] += 1
        
        max_score = 0
        res = tuple()
        for p in count:
            if count[p] > max_score or (max_score == count[p] and p < res):
                max_score = count[p]
                res = p
        return list(res)
