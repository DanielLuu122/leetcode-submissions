class Solution:
    def is_palindrome(self, l, r, s):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        used = False
        while l <= r:
            if s[r] != s[l]:
                # test if we can remove one
                return (self.is_palindrome(l + 1, r, s) or self.is_palindrome(l, r - 1, s))
            l += 1
            r -= 1
        return True