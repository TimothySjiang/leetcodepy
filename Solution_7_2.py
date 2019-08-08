class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            sign = -1
        else:
            sign = 1

        res = 0
        x = abs(x)

        while x:
            pop = x % 10
            x = x // 10
            if res > (2 ** 31) / 10 or ((res == 2 * 31 / 10) and (pop > 7)):
                return 0
            res = res * 10 + pop

        return sign * res