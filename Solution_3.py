class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return len(s)
        result = 1
        for i in range(n):
            p = i
            while p < n - 1:
                if s[p + 1] not in s[i:p + 1]:
                    p = p + 1
                else:
                    break

            result = max(result, p - i + 1)
        return result
