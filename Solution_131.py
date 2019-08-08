class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s: return []
        results = []
        self.recursion(s, 0, [], results)
        return results

    def recursion(self, s, pos, result, results):
        if pos == len(s):
            results.append(result)
            return
        for i in range(pos, len(s)):
            if self.isPalindrome(s[pos:i + 1]):
                self.recursion(s, i + 1, result + [s[pos:i + 1]], results)

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