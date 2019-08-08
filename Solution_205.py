class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        ad = {}
        for i in range(len(s)):
            if (s[i] in d.keys()):
                if not d[s[i]] == t[i]:
                    return False
            else:
                d[s[i]] = t[i]

            if (t[i] in ad.keys()):
                if not ad[t[i]] == s[i]:
                    return False
            else:
                ad[t[i]] = s[i]

        return True