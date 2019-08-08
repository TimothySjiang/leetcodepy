class Solution:
    def decodeString(self, s: str) -> str:
        stack = [["", 1]]
        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                stack.append(["", num])
                num = 0
            elif c == ']':
                st, k = stack.pop()
                stack[-1][0] += st * k
            else:
                stack[-1][0] += c
        return stack[0][0]]