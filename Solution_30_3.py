#Still TLE
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words: return []
        dic = collections.Counter(words)
        res = []
        step = len(words[0])
        self.res = set()
        for i in range(len(s)):
            if self.recursion(s, i, dic, len(dic), step):
                self.res.add(str((i,dic)))
                res.append(i)
        return res

    def recursion(self, s, start, dic, formed, step):
        if str((start,dic)) in self.res: return True
        if not formed: return True
        if dic[s[start:start + step]] > 0:
            dic[s[start:start + step]] -= 1
            if not dic[s[start:start + step]]:
                formed -= 1
            if self.recursion(s, start + step, dic, formed, step):
                dic[s[start:start + step]] += 1
                self.res.add(str((start,dic)))
                return True
            dic[s[start:start + step]] += 1
        return False