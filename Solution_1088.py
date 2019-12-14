class Solution:
    def confusingNumberII(self, N: int) -> int:
        count = 0
        for i in range(1, N + 1):
            count += self.confusingNumber(i)
        return count

    def confusingNumber(self, N: int) -> bool:
        S = str(N)
        rotation = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        result = []

        for c in S[::-1]:
            if c not in rotation:
                return False
            result.append(rotation[c])

        return "".join(result) != S