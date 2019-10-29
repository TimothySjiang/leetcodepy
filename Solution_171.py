class Solution:
    def titleToNumber(self, s: str) -> int:
        s = list(s)[::-1]
        res = 0
        while s:
            res *= 26
            res += ord(s.pop()) - ord('A') + 1
        return res