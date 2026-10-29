class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "," + s
        return res


    def decode(self, s: str) -> List[str]:
        length = 0
        length_str = ""
        i = 0
        res = []
        print(s)
        while i < len(s):
            if s[i] == ",":
                length = int(length_str)
                length_str = ""
                i += 1
                res.append(s[i:i+length])
                i += length
            else:
                length_str += s[i]
                i += 1
        return res

