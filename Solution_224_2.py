class Solution:
    def calculate(self, s: str) -> int:
        s = s.strip()
        stack = [0,'+']
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append(0)
                stack.append('+')
            elif s[i] == ')':
                if stack[-2] == '+':
                    stack[-3] += stack[-1]
                else:
                    stack[-3] -= stack[-1]
                stack.pop()
                stack.pop()
            elif s[i] in ['+','-']:
                stack.append(s[i])
            elif s[i].isdigit():
                start = i
                while i+1 < len(s) and s[i+1].isdigit():
                    i = i + 1
                if stack[-1] == '+':
                    stack[-2] += int(s[start:i+1])
                else:
                    stack[-2] -= int(s[start:i+1])
                stack.pop()
            i += 1
        return stack[0]