class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or not k: return 0
        window = collections.defaultdict(int)
        p1 = 0
        p2 = 0
        res = 0
        while p2 < len(s):
            window[s[p2]] = p2
            if len(window) > k:
                del_index = min(window.values())
                del window[s[del_index]]
                p1 = del_index + 1
            res = max(res, p2 - p1 + 1)
            p2 += 1

        return res