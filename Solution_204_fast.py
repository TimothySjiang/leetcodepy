class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * n
        for i in range(min(n, 2)):
            isPrime[i] = False

        i = 2
        while i * i < n:
            if (not isPrime[i]):
                i = i + 1
                continue
            for j in range(i ** 2, n, i):
                isPrime[j] = False

            i = i + 1

        return sum(isPrime)