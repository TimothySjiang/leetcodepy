class Solution:
    def confusingNumberII(self, N: int) -> int:
        valid = [0, 1, 6, 8, 9]
        mapping = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        self.count = 0
        self.backtrack(1, 1, N, 10, valid, mapping)
        self.backtrack(6, 9, N, 10, valid, mapping)
        self.backtrack(8, 8, N, 10, valid, mapping)
        self.backtrack(9, 6, N, 10, valid, mapping)

        return self.count

    def backtrack(self, v, rotation, N, digit, valid, mapping):
        if v and v != rotation:
            self.count += 1
        for i in valid:
            if v * 10 + i > N:
                break
            else:
                self.backtrack(v * 10 + i, mapping[i] * digit + rotation, N, digit * 10, valid, mapping)