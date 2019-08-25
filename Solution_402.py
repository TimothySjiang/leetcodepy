class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return '0'
        stack = []
        for d in num:
            while stack and k and stack[-1] > d:
                stack.pop()
                k -= 1
            stack.append(d)

        while k:
            stack.pop()
            k -= 1

        while stack and stack[0] == '0':
            stack.pop(0)

        return ''.join(stack) if stack else '0'