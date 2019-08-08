class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k==0: return num
        if k > len(num): return '0'
        num += '0'
        stack = []
        for i in range(len(num)):
            while k and stack and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])

        i = 0
        while i < len(stack) and stack[i] == '0':
            i += 1
        res = ''.join(stack[i:-1])
        return res if res else '0'