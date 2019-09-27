class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)

        def lcm(a, b):
            return a * b // gcd(a, b)

        def count(n, a, b, c):
            # count ugly number n's position
            return n // a + n // b + n // c - n // lcm(a, b) - n // lcm(a, c) - n // lcm(b, c) + n // lcm(lcm(a, b), c)

        l = 1
        r = n * min(a, b, c)
        while l < r:
            mid = (l + r) // 2
            if count(mid, a, b, c) < n:
                l = mid + 1
            else:
                r = mid

        return r