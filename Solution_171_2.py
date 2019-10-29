class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += (ord(s[i]) - ord('A') + 1) * 26 ** (len(s) - i -1)
        return res