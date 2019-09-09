class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.recursion('', 0, 0, n, ans)
        return ans

    def recursion(self, s, l, r, n, ans):
        if len(s) == 2 * n:
            ans.append(s)
        if l < n:
            self.recursion(s + '(', l + 1, r, n, ans)
        if r < l:
            self.recursion(s + ')', l, r + 1, n, ans)
