class Solution:
    def calculate(self, s: str) -> int:
        if not s: return '0'
        stack = []
        sign = '+'
        num = 0
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            if s[i] == '(':
                j = i
                k = 1
                while k:
                    j += 1
                    if s[j] == '(':
                        k+=1
                    if s[j] ==')':
                        k-= 1
                num = self.calculate(s[i+1:j])
                i = j
                continue
            if s[i] in ['+','-','*','/'] or i == len(s)-1:
                if sign =='+':
                    stack.append(num)
                elif sign =='-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                elif sign =='/':
                    stack.append(int(stack.pop()/num))
                sign = s[i]
                num = 0
            i += 1
        return sum(stack)