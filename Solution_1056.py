class Solution:
    def confusingNumber(self, N: int) -> bool:
        S = str(N)
        rotation = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        result = []

        for c in S[::-1]:
            if c not in rotation:
                return False
            result.append(rotation[c])

        return "".join(result) != S