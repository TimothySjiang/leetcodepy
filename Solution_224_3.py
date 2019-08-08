class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        number = 0
        sign = 1
        i = 0
        while i < len(s):
            c = s[i]
            if c in '1234567890':
                number = number * 10 + int(c)
            elif c == '(':
                j = i
                k = 1
                while k:
                    j += 1
                    if s[j] == '(':
                        k+=1
                    if s[j] ==')':
                        k-= 1
                number = self.calculate(s[i+1:j])
                i = j + 1
                continue
            elif c == '+':
                result += sign * number
                sign = 1
                number = 0
            elif c == '-':
                result += sign * number
                sign = -1
                number = 0
            i += 1
        result += sign * number

        return result