class Solution:
    def isHappy(self, n: int) -> bool:
        r1 = n
        r2 = n
        while (True):
            r1 = self.next(r1)
            r2 = self.next(self.next(r2))

            if (r1 == r2):
                return r1 == 1

    def next(self,n:int) -> int:
        Sum = 0
        while (n):
            Sum += (n % 10) ** 2
            n = n // 10
        return Sum
