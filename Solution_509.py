class Solution:
    def fib(self, N: int) -> int:
        first = 0
        second = 1

        for _ in range(N):
            third = first + second
            first = second
            second = third

        return first
