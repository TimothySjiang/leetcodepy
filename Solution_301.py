class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        left, right = self._LeftRightCount(s)
        self._dfs(s, left, right, 0, res)
        return res

    def _dfs(self, s, left, right, start, res):
        if left == 0 and right == 0:
            if self._isvalid(s):
                res.append(s)
            return

        for i in range(start, len(s)):
            if i > start and s[i] == s[i - 1]:
                continue
            if s[i] == '(':
                self._dfs(s[:i] + s[i + 1:], left - 1, right, i, res)
            if s[i] == ')':
                self._dfs(s[:i] + s[i + 1:], left, right - 1, i, res)

    def _isvalid(self, s):
        left, right = self._LeftRightCount(s)
        return left == 0 and right == 0

    def _LeftRightCount(self, s):
        left = right = 0
        for ch in s:
            if ch == '(':
                left += 1
            if ch == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
        return left, right