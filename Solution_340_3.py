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
        window = collections.Counter(s[:L])
        if len(window) <= k:
            return True
        for i in range(1,len(s) - L + 1 ):
            window[s[i-1]] -= 1
            if not window[s[i-1]]:
                del window[s[i-1]]
            window[s[i+L-1]] += 1
            if len(window) <= k:
                return True
        return False
