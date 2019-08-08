class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        res = ''
        for s in S:
            if s =='(':
                if stack:
                    res += s
                stack.append(s)
            else:
                stack.pop()
                if stack:res += s
        return res