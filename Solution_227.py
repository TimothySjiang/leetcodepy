class Solution:
    def calculate(self, s: str) -> int:
        if not s: return "0"
        sign = '+'
        num = 0
        res = []
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            if s[i] in ['+','-','*','/'] or i == len(s)-1:
                if sign =='+':
                    res.append(num)
                elif sign =='-':
                    res.append(-num)
                elif sign == '*':
                    res.append(res.pop()*num)
                elif sign =='/':
                    res.append(int(res.pop()/num))
                sign = s[i]
                num = 0
        return sum(res)