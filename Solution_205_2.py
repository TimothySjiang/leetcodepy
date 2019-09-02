class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return True
        d = {}
        rd = {}
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]] != t[i]:
                    return False
            else:
                d[s[i]] = t[i]

            if t[i] in rd:
                if rd[t[i]] != s[i]:
                    return False
            else:
                rd[t[i]] = s[i]

        return True