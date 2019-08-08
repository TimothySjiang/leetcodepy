#TLE
class Solution:
    def minCut(self, s: str) -> int:
        if not s: return []
        results = []
        self.recursion(s, 0, 0, results)
        return min(results)-1

    def recursion(self, s, pos, result, results):
        if pos == len(s):
            results.append(result)
            return
        for i in range(pos, len(s)):
            if self.isPalindrome(s[pos:i + 1]):
                self.recursion(s, i + 1, result + 1, results)

    def isPalindrome(self, s):
        if not s: return False
        p1 = 0
        p2 = len(s) - 1
        while p1 < p2:
            if s[p1] == s[p2]:
                p1 += 1
                p2 -= 1
            else:
                return False
        return True