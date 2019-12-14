class Solution:
    def confusingNumber(self, N: int) -> bool:
        d = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        s = str(N)

        for c in s:
            if c not in d:
                return False

        for i in range(0, len(s) // 2 + 1):
            if d[s[i]] != s[-i - 1]:
                return True

        return False