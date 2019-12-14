class Solution:
    def confusingNumberII(self, N: int) -> int:
        mapping = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        self.count = 0
        for num in mapping:
            if num:
                self.backtrack(num, mapping[num], N, 10, mapping)
        return self.count

    def backtrack(self, v, rotation, N, digit,  mapping):
        if v != rotation:
            self.count += 1
        for i in mapping:
            if v * 10 + i > N:
                break
            else:
                self.backtrack(v * 10 + i, mapping[i] * digit + rotation, N, digit * 10, mapping)