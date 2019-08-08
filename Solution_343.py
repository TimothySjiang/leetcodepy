class Solution:
    def integerBreak(self, n: int) -> int:
        if n ==2: return 1
        if n ==3: return 2
        base = n//3
        m = n%3
        if m == 1:
            return 3**(base-1) * 4
        if m == 2:
            return 3**base * 2
        return 3**base