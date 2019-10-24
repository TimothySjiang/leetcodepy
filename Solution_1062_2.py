class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        n = len(S)
        left, right = 1, n
        while left < right:
            L = left + (right - left) // 2
            if self.search(L, n, S) != -1:
                left = L + 1
            else:
                right = L

        return left - 1

    def search(self, L: int, n: int, S: str) -> str:
        seen = set()
        for start in range(0, n - L + 1):
            tmp = S[start:start + L]
            if tmp in seen:
                return start
            seen.add(tmp)
        return -1