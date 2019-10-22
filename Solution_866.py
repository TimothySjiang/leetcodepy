class Solution:
    def primePalindrome(self, N: int) -> int:
        def is_prime(n):
            return n > 1 and all(n%d for d in range(2, int(n**.5) + 1))

        for length in range(1, 6):
            for root in range(10**(length - 1), 10**length):
                s = str(root)
                x = int(s + s[-2::-1]) #eg. s = '123' to x = int('12321')
                if x >= N and is_prime(x):
                    return x

            for root in range(10**(length - 1), 10**length):
                s = str(root)
                x = int(s + s[-1::-1])
                if x >= N and is_prime(x):
                    return x