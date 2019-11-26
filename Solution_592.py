class Solution:
    def fractionAddition(self, expression: str) -> str:
        res, sign, ex = '0/1', 1, ''
        for s in expression:
            if s in ['-', '+']:
                if not ex: ex = '0/1'
                res = self.plus(res, ex, sign)
                if s == '-':
                    sign = -1
                else:
                    sign = 1
                ex = ''
            else:
                ex += s

        return self.plus(res, ex, sign)

    def plus(self, e1, e2, sign):
        n1, d1 = e1.split('/')
        n2, d2 = e2.split('/')
        n = int(n1) * int(d2) + sign * int(n2) * int(d1)
        d = int(d1) * int(d2)
        if not n:
            return '0/1'
        gcd = self.gcd(n, d)
        return str(n // gcd) + '/' + str(d // gcd)

    def gcd(self, x, y):
        while (y):
            x, y = y, x % y
        return x