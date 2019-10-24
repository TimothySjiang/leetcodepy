#TLE
class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        d = collections.defaultdict(int)
        for i in range(len(S)):
            for j in range(i+1,len(S)+1):
                d[S[i:j]] += 1
        res = 0
        for k in d:
            if d[k] > 1:
                res = max(res,len(k))
        return res