class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pc = collections.Counter(p)
        lp = len(p)
        result = []
        sc = collections.Counter(s[:lp-1])
        for i in range(lp-1,len(s)):
            sc[s[i]] += 1
            if sc == pc:
                result.append(i-lp+1)
            sc[s[i-lp+1]] -= 1
            if sc[s[i-lp+1]] == 0:
                del sc[s[i-lp+1]]   # remove the count if it is 0
        return result