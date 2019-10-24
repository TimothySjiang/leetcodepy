#TLE
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l = 0
        r = len(s) + 1
        while l < r:
            L = l + (r - l) // 2
            if self.search(L, k, s):
                l = L + 1
            else:
                r = L
        return l - 1

    def search(self, L, k, s):
        for i in range(len(s) - L + 1):
            if len(set(s[i:i + L])) <= k:
                return True
        return False

