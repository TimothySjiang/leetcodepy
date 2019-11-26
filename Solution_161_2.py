class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1: return False
        if s == t: return False
        if not s or not t and abs(len(s) - len(t)) == 1: return True
        if s[0] == t[0]:
            return self.isOneEditDistance(s[1:], t[1:])
        elif abs(len(s) - len(t)) == 1:
            return s == t[1:] or s[1:] == t
        else:
            return s[1:] == t[1:]