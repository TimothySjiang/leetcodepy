class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s and not p: return True
        if not p: return False
        if not s:
            if not all([ch == '*' for ch in p]):
                return False
            else:
                return True

        if p[0] == '?':
            return self.isMatch(s[1:], p[1:])
        if p[0] == '*':
            return any([self.isMatch(s, p[1:]), self.isMatch(s[1:], p[1:]), self.isMatch(s[1:], p)])
        if s[0] == p[0]:
            return self.isMatch(s[1:], p[1:])
        return False