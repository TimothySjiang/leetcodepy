class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        for i in range(2, n):
            count += self.isPrime(i)

        return count

    def isPrime(self, n: int) -> int:
        for i in range(2, n**0.5 + 1):
            if not n % i:
                return 0
        return 1