#Tle
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words: return []
        dic = collections.Counter(words)
        res = []
        step = len(words[0])
        for i in range(len(s)):
            if self.recursion(s, i, dic, len(dic), step):
                res.append(i)
        return res

    def recursion(self, s, start, dic, formed, step):
        if not formed: return True
        if dic[s[start:start + step]] > 0:
            dic[s[start:start + step]] -= 1
            if not dic[s[start:start + step]]:
                formed -= 1
            if self.recursion(s, start + step, dic, formed, step):
                dic[s[start:start + step]] += 1
                return True
            dic[s[start:start + step]] += 1
        return False