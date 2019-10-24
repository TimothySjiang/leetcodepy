#TLE
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if len(set(s[i:j])) <= k:
                    res = max(res,j-i)
        return res