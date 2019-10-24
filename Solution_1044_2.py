#MLE
class Solution:
    def longestDupSubstring(self, S: str) -> str:
        n = len(S)
        l = 0
        r = n
        res = ''
        while l < r:
            L = l + (r - l) // 2
            newres = self.search(L, S)
            if newres:
                res = newres
                l = L + 1
            else:
                r = L
        return res

    def search(self, length, s):
        seen = set()
        for start in range(len(s) - length + 1):
            tmp = s[start:start + length]
            if tmp in seen:
                return tmp
            seen.add(tmp)
        return ''