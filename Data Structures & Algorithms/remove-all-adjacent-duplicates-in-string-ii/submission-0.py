class Solution:

    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        def pop_top():
            idx = len(stack) - 1
            c = stack[idx]
            idx -= 1
            for i in range(k - 1):
                if idx - i < 0 or stack[idx - i] != c:
                    return False
            print(stack)
            for i in range(k):
                stack.pop()
            return True

        for c in s:
            stack.append(c)
            while stack:
                res = pop_top()
                if res == False:
                    break
        res = ""
        for c in stack:
            res += c
        return res

