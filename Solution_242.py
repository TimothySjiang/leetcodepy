class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = collections.Counter(s)
        c2 = collections.Counter(t)
        return c1==c2