#TLE
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        modulo = 10 ** 9 + 7
        self.count = 0
        self.recursive(0, d, f, target, 0)
        return self.count % modulo

    def recursive(self, index, d, f, target, result):
        if result == target and index == d:
            self.count += 1
        if index < d:
            for i in range(1, f + 1):
                if result + i <= target:
                    self.recursive(index + 1, d, f, target, result + i)
