class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.split()
        if len(s) == 0: return 0
        s = s[0]
        sign = ''
        result = 0
        start = 0
        for c in s:
            if c == '-' and start == 0:
                sign = '-'
                start = 1
                continue
            if c == '+' and start == 0:
                sign = '+'
                start = 1
                continue

            if ord(c) < ord('0') or ord(c) > ord('9'):
                if start == 0:
                    return 0
                break
            else:
                start = 1
                result = result * 10 + int(c)

        if sign == '-':
            if -result < -2 ** 31:
                return -2 ** 31
            else:
                return -result
        else:
            if result > 2 ** 31 - 1:
                return 2 ** 31 - 1
            else:
                return result