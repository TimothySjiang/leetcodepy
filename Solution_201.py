#TLE
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        res = m
        for i in range(m+1,n+1):
            res &= i
        return res