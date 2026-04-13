class Solution:
    def isHappy(self, n: int) -> bool:
        def getDigits(v):
            ans = []
            while v != 0:
                ans.append(v % 10)
                v = v // 10
            return ans
        s = set()
        i = n
        while i not in s:
            if i == 1:
                return True
            newi = 0
            for d in getDigits(i):
                newi += d*d
            s.add(i)
            i = newi
        return False

