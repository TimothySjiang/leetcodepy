class Solution:
    # Binary search
    def mySqrt(self, x):
        l = 0
        r = x+1
        while l < r:
            m = l + (r-l)//2
            if m*m > x:
                r = m
            else:
                l = m + 1
        return l-1