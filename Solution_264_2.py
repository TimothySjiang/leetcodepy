class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = []

        i2 = i3 = i5 = -1
        v2 = v3 = v5 = 1

        for i in range(n):
            r = min(v2, v3, v5)
            ugly.append(r)

            if r == v2:
                i2 += 1
                v2 = ugly[i2] * 2

            if r == v3:
                i3 += 1
                v3 = ugly[i3] * 3

            if r == v5:
                i5 += 1
                v5 = ugly[i5] * 5

        return r